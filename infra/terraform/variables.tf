variable "location" {
  description = "Azure region"
  type        = string
  default     = "UK South"
}

variable "resource_group_name" {
  description = "Resource group name"
  type        = string
  default     = "rg-foundryops-platform"
}

variable "storage_account_name" {
  description = "Storage account name"
  type        = string
  default     = "stfoundryopsplatform"
}
