# AzureKeyVaultConnector

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | Application ID of the Azure App. | [optional] 
**secret_key** | **str** | This is the Harness text secret with the Azure authentication key as its value. | [optional] 
**tenant_id** | **str** | The Azure Active Directory (AAD) directory ID where you created your application. | [optional] 
**vault_name** | **str** | The Azure Vault name | 
**subscription** | **str** | Azure Subscription ID. | 
**is_default** | **bool** |  | [optional] 
**vault_configured_manually** | **bool** |  | [optional] 
**azure_environment_type** | **str** | This specifies the Azure Environment type, which is AZURE by default. | [optional] 
**delegate_selectors** | **list[str]** | List of Delegate Selectors that belong to the same Delegate and are used to connect to the Secret Manager. | [optional] 
**use_managed_identity** | **bool** | Boolean value to indicate if managed identity is used | [optional] 
**azure_managed_identity_type** | **str** | Managed Identity Type | [optional] 
**managed_client_id** | **str** | Client Id of the ManagedIdentity resource | [optional] 
**enable_purge** | **bool** | Boolean value to indicate if purge is enabled | [optional] 
**default** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

