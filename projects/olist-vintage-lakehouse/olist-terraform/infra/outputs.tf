output "storage_account_name" { value = azurerm_storage_account.lake.name }
output "key_vault_name" { value = azurerm_key_vault.this.name }
output "key_vault_id" { value = azurerm_key_vault.this.id }
output "key_vault_uri" { value = azurerm_key_vault.this.vault_uri }
output "workspace_url" { value = "https://${azurerm_databricks_workspace.this.workspace_url}" }
output "access_connector_id" { value = azurerm_databricks_access_connector.this.id }
output "catalog_name" { value = local.catalog_name }
