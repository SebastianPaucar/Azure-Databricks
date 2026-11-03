terraform {
  required_version = ">= 1.6"
  required_providers {
    databricks = { source = "databricks/databricks", version = "~> 1.50" }
  }
}

# Uses a profile from the Databricks CLI config (host + PAT of the NEW workspace).
# A PAT cannot create Key Vault-backed secret scopes (see create_secret_scope).
provider "databricks" {
  profile = var.databricks_profile
}
