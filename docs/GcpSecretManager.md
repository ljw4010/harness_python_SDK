# GcpSecretManager

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_default** | **bool** |  | [optional] 
**credentials_ref** | **str** | Reference to the secret containing credentials of IAM service account for Google Secret Manager | [optional] 
**delegate_selectors** | **list[str]** | List of Delegate Selectors that belong to the same Delegate and are used to connect to the Secret Manager. | [optional] 
**assume_credentials_on_delegate** | **bool** | Boolean value to indicate that Credentials are taken from the Delegate. | [optional] 
**default** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

