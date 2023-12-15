# AzureRepoConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | SSH | HTTP URL based on type of connection | 
**validation_repo** | **str** | The repo to validate AzureRepo credentials. Only valid for Account type connector | [optional] 
**authentication** | [**AzureRepoAuthentication**](AzureRepoAuthentication.md) |  | 
**api_access** | [**AzureRepoApiAccess**](AzureRepoApiAccess.md) |  | [optional] 
**delegate_selectors** | **list[str]** | Selected Connectivity Modes | [optional] 
**execute_on_delegate** | **bool** |  | [optional] 
**type** | **str** | Project | Repository connector type | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

