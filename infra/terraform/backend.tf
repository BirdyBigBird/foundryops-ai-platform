terraform {
  backend "azurerm" {
    resource_group_name  = "rg-foundryops-platform"
    storage_account_name = "stfoundryopsplatform"
    container_name       = "tfstate"
    key                  = "foundryops.terraform.tfstate"
  }
}
