# ResourceGroupsResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Resource Group Identifier | 
**name** | **str** | Resource Group Name | 
**color** | **str** | Color associated with the Resource Group. | [optional] 
**tags** | **dict(str, str)** | Resource Group tags | [optional] 
**description** | **str** | Resource Group description | [optional] 
**allowed_scope_levels** | **list[str]** | Allowed scope levels for this Resource Group. | [optional] 
**included_scope** | [**list[ResourceGroupScope]**](ResourceGroupScope.md) | Included scopes for the resources belonging to the Resource Group. | [optional] 
**resource_filter** | [**list[ResourceFilter]**](ResourceFilter.md) | Specifies the actual resources present in the Resource Group. | [optional] 
**include_all_resources** | **bool** | Boolean value for including all resources in Resource Group. | [optional] 
**harness_managed** | **bool** | This indicates if this Resource Group is managed by Harness or not. If true, Harness can manage and modify this Resource Group. | [optional] 
**created** | **int** | Creation timestamp for Resource Group. | [optional] 
**updated** | **int** | Last modification timestamp for Resource Group. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

