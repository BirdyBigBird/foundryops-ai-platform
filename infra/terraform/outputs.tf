output "resource_group_name" {
  value = azurerm_resource_group.foundryops_rg.name
}

output "storage_account_name" {
  value = azurerm_storage_account.platform_storage.name
}

output "tfstate_container_name" {
  value = azurerm_storage_container.tfstate.name
}
