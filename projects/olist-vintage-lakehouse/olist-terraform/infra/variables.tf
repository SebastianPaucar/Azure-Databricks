variable "location" {
  type    = string
  default = "eastus2"
}

variable "rg_name" {
  type    = string
  default = "rg-olist-tf"
}

variable "workspace_name" {
  description = "Databricks workspace name. The auto-created catalog is this name with '-' replaced by '_'."
  type        = string
  default     = "dbw-olist-tf"
}

variable "human_object_id" {
  description = "Object ID of your user (az ad signed-in-user show --query id -o tsv). Gets Key Vault Secrets Officer."
  type        = string
}

variable "containers" {
  description = "ADLS containers to create. Only raw is used by the pipeline."
  type        = list(string)
  default     = ["raw"]
}
