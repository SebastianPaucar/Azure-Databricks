variable "databricks_profile" {
  type    = string
  default = "azure-tf"
}

variable "catalog_name" {
  description = "Auto-created catalog. Confirm with: databricks -p azure-tf catalogs list"
  type        = string
}

variable "storage_account_name" { type = string }
variable "access_connector_id" { type = string }
variable "key_vault_id" { type = string }
variable "key_vault_uri" { type = string }

variable "skip_validation" {
  description = "Set true if external location validation fails on the optional file-events checks."
  type        = bool
  default     = false
}

variable "create_secret_scope" {
  description = "Key Vault-backed scopes need Entra (not PAT) auth; leave false and create it in the UI."
  type        = bool
  default     = false
}
