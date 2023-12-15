# RoleAssignmentFilter

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_group_filter** | **list[str]** | Filter role assignments based on resource group identifiers | [optional] 
**role_filter** | **list[str]** | Filter role assignments based on role identifiers | [optional] 
**principal_type_filter** | **list[str]** | Filter role assignments based on principal type | [optional] 
**principal_scope_level_filter** | **list[str]** | Filter role assignments based on principal scope level | [optional] 
**principal_filter** | [**list[AuthzPrincipal]**](AuthzPrincipal.md) | Filter role assignments based on principals | [optional] 
**harness_managed_filter** | **list[bool]** | Filter role assignments based on role assignments being harness managed | [optional] 
**disabled_filter** | **list[bool]** | Filter role assignments based on whether they are enabled or disabled | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

