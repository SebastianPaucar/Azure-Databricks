terraform {
  required_version = ">= 1.6"
  required_providers {
    azurerm = { source = "hashicorp/azurerm", version = "~> 4.0" }
    random  = { source = "hashicorp/random", version = "~> 3.6" }
    time    = { source = "hashicorp/time", version = "~> 0.12" }
  }
}

# Auth comes from env vars: ARM_CLIENT_ID, ARM_CLIENT_SECRET, ARM_TENANT_ID, ARM_SUBSCRIPTION_ID
provider "azurerm" {
  features {
    key_vault {
      purge_soft_delete_on_destroy    = true # no manual `az keyvault purge` after destroy
      recover_soft_deleted_key_vaults = false
    }
    resource_group {
      prevent_deletion_if_contains_resources = false
    }
  }
  resource_provider_registrations = "none" # providers were registered by hand earlier
  storage_use_azuread             = true   # shared-key access is disabled on the lake
}
