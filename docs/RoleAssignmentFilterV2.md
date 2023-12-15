# RoleAssignmentFilterV2

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_group_filter** | **list[str]** | Filter role assignments based on resource group identifiers | [optional] 
**role_filter** | **list[str]** | Filter role assignments based on role identifiers | [optional] 
**scope_filters** | [**list[ScopeSelector]**](ScopeSelector.md) | Filter role assignments based on scope filters | [optional] 
**principal_filter** | [**AuthzPrincipal**](AuthzPrincipal.md) |  | [optional] 
**harness_managed_filter** | **bool** | Filter role assignments based on role assignments being harness managed | [optional] 
**disabled_filter** | **bool** | Filter role assignments based on whether they are enabled or disabled | [optional] 
**principal_type_filter** | **list[str]** | Filter role assignments based on principal type | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

