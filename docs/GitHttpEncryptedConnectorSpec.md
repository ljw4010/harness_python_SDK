# GitHttpEncryptedConnectorSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | This specifies the type of connector | 
**url** | **str** | Git repo url | 
**branch** | **str** | branch name | [optional] 
**connection_type** | **str** |  | 
**username_ref** | **str** | Reference to encrypted Harness secret for git username | 
**password_ref** | **str** | Reference to encrypted Harness secret for git password | 
**validation_repo** | **str** | validation repo | [optional] 
**delegate_selectors** | **list[str]** | List of unique delegate selectors | [optional] 
**execute_on_delegate** | **bool** | execute on delegate | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

