# AzureClientSecretKeyConnectorSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | This specifies the type of connector | 
**delegate_selectors** | **list[str]** | List of Delegate Selectors that belong to the same Delegate and are used to connect to the Secret Manager | [optional] 
**azure_environment_type** | **str** | This specifies the Azure Environment type, which is AZURE by default. | [default to 'AZURE']
**execute_on_delegate** | **bool** | execute on delegate | [optional] [default to True]
**application_id** | **str** | Application ID of the Azure App | 
**tenant_id** | **str** | The Azure Active Directory (AAD) directory ID where you created your application | 
**secret_ref** | **str** | Reference to encrypted Harness secret for Azure client secret | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

