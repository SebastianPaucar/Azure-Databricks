locals {
  raw_url = "abfss://raw@${var.storage_account_name}.dfs.core.windows.net/"
}

resource "databricks_storage_credential" "olist" {
  name = "cred-olist-tf"
  azure_managed_identity {
    access_connector_id = var.access_connector_id
  }
}

resource "databricks_external_location" "raw" {
  name            = "loc-olist-tf"
  url             = local.raw_url
  credential_name = databricks_storage_credential.olist.id
  skip_validation = var.skip_validation
}

resource "databricks_schema" "layers" {
  for_each     = toset(["bronze", "silver", "gold", "ops"])
  catalog_name = var.catalog_name
  name         = each.value
}

resource "databricks_volume" "raw" {
  name             = "raw"
  catalog_name     = var.catalog_name
  schema_name      = databricks_schema.layers["bronze"].name
  volume_type      = "EXTERNAL"
  storage_location = local.raw_url
  depends_on       = [databricks_external_location.raw]
}

resource "databricks_volume" "libs" {
  name         = "libs"
  catalog_name = var.catalog_name
  schema_name  = databricks_schema.layers["bronze"].name
  volume_type  = "MANAGED"
}

resource "databricks_secret_scope" "kv" {
  count = var.create_secret_scope ? 1 : 0
  name  = "kv-olist"
  keyvault_metadata {
    resource_id = var.key_vault_id
    dns_name    = var.key_vault_uri
  }
}
