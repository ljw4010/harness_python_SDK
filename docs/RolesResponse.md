# RolesResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Role Identifier | 
**name** | **str** | Role Name | 
**permissions** | **list[str]** | Permissions for this Role. | [optional] 
**allowed_scope_levels** | **list[str]** | The Scope levels at which this Role can be used. | [optional] 
**description** | **str** | Role description | [optional] 
**tags** | **dict(str, str)** | Role tags | [optional] 
**scope** | [**RoleScope**](RoleScope.md) |  | [optional] 
**created** | **int** | Creation timestamp for Role. | [optional] 
**updated** | **int** | Last modification timestamp for Role. | [optional] 
**harness_managed** | **bool** | This indicates if this Role is managed by Harness or not. If true, Harness can manage and modify this Role. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

