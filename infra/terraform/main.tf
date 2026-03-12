terraform {
  required_version = ">= 1.5"

  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~>3.100"
    }
  }
}

provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "foundryops_rg" {
  name     = "rg-foundryops-platform"
  location = "UK South"
}

resource "azurerm_storage_account" "platform_storage" {
  name                     = "stfoundryopsplatform"
  resource_group_name      = azurerm_resource_group.foundryops_rg.name
  location                 = azurerm_resource_group.foundryops_rg.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}
