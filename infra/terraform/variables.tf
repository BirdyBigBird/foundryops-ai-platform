variable "location" {
  description = "Azure region for resources"
  type        = string
  default     = "UK South"
}

variable "resource_group_name" {
  description = "Name of the platform resource group"
  type        = string
  default     = "rg-foundryops-platform"
}

variable "storage_account_name" {
  description = "Storage account for platform data"
  type        = string
  default     = "stfoundryopsplatform"
}
