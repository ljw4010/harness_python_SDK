# CreateResourceGroupRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Resource Group identifier | 
**name** | **str** | Resource Group name | 
**color** | **str** | Color associated with the Resource Group. | [optional] 
**tags** | **dict(str, str)** | Resource Group tags | [optional] 
**description** | **str** | Resource Group description | [optional] 
**included_scope** | [**list[ResourceGroupScope]**](ResourceGroupScope.md) | Included scopes for the resources belonging to the Resource Group. | [optional] 
**resource_filter** | [**list[ResourceFilter]**](ResourceFilter.md) | Specifies the actual resources present in the Resource Group. | [optional] 
**include_all_resources** | **bool** | Boolean value for including all resources in Resource Group. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

