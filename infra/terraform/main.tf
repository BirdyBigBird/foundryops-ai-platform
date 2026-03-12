terraform {
  required_version = ">= 1.5"

  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~>3.100"
    }
  }
}

module "resource_group" {
  source = "./modules/resource-group"

  resource_group_name = var.resource_group_name
  location            = var.location
}

module "storage_account" {
  source = "./modules/storage-account"

  storage_account_name = var.storage_account_name
  resource_group_name  = var.resource_group_name
  location             = var.location
}
