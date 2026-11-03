data "azurerm_client_config" "current" {} # the identity running Terraform (the service principal)

resource "random_string" "suffix" {
  length  = 5
  upper   = false
  special = false
}

locals {
  sa_name      = "stolist${random_string.suffix.result}"
  kv_name      = "kv-olist-${random_string.suffix.result}"
  catalog_name = replace(var.workspace_name, "-", "_")
}

resource "azurerm_resource_group" "this" {
  name     = var.rg_name
  location = var.location
}

# ---------- Storage (ADLS Gen2, Entra-only) ----------
resource "azurerm_storage_account" "lake" {
  name                            = local.sa_name
  resource_group_name             = azurerm_resource_group.this.name
  location                        = azurerm_resource_group.this.location
  account_tier                    = "Standard"
  account_replication_type        = "LRS"
  account_kind                    = "StorageV2"
  is_hns_enabled                  = true
  min_tls_version                 = "TLS1_2"
  allow_nested_items_to_be_public = false
  shared_access_key_enabled       = false
  default_to_oauth_authentication = true
}

# The identity running Terraform needs data-plane rights to create containers.
resource "azurerm_role_assignment" "tf_sp_storage" {
  scope                = azurerm_storage_account.lake.id
  role_definition_name = "Storage Blob Data Contributor"
  principal_id         = data.azurerm_client_config.current.object_id
}

# Role assignments take 1-5 min to propagate.
resource "time_sleep" "rbac_propagation" {
  depends_on      = [azurerm_role_assignment.tf_sp_storage]
  create_duration = "120s"
}

resource "azurerm_storage_data_lake_gen2_filesystem" "containers" {
  for_each           = toset(var.containers)
  name               = each.value
  storage_account_id = azurerm_storage_account.lake.id
  depends_on         = [time_sleep.rbac_propagation]
}

# ---------- Key Vault (RBAC) ----------
resource "azurerm_key_vault" "this" {
  name                       = local.kv_name
  resource_group_name        = azurerm_resource_group.this.name
  location                   = azurerm_resource_group.this.location
  tenant_id                  = data.azurerm_client_config.current.tenant_id
  sku_name                   = "standard"
  rbac_authorization_enabled = true
  soft_delete_retention_days = 7
  purge_protection_enabled   = false
}

resource "azurerm_role_assignment" "human_kv_officer" {
  scope                = azurerm_key_vault.this.id
  role_definition_name = "Key Vault Secrets Officer"
  principal_id         = var.human_object_id
}

resource "azurerm_role_assignment" "sp_kv_user" {
  scope                = azurerm_key_vault.this.id
  role_definition_name = "Key Vault Secrets User"
  principal_id         = data.azurerm_client_config.current.object_id
}

# ---------- Azure Databricks ----------
resource "azurerm_databricks_workspace" "this" {
  name                        = var.workspace_name
  resource_group_name         = azurerm_resource_group.this.name
  location                    = azurerm_resource_group.this.location
  sku                         = "premium"
  managed_resource_group_name = "databricks-rg-${var.workspace_name}-managed"
}

resource "azurerm_databricks_access_connector" "this" {
  name                = "dbac-olist-tf"
  resource_group_name = azurerm_resource_group.this.name
  location            = azurerm_resource_group.this.location
  identity {
    type = "SystemAssigned"
  }
}

resource "azurerm_role_assignment" "connector_storage" {
  scope                = azurerm_storage_account.lake.id
  role_definition_name = "Storage Blob Data Contributor"
  principal_id         = azurerm_databricks_access_connector.this.identity[0].principal_id
}
