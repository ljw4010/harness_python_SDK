# ResourceGroupFilterRequestBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** | Filter by Account identifier. | [optional] 
**org** | **str** | Filter by Organization identifier. | [optional] 
**project** | **str** | Filter by Project identifier. | [optional] 
**search_term** | **str** | Filter Resource Group matching by identifier/name. | [optional] 
**identifier_filter** | **list[str]** | Filter by Resource Group identifiers | [optional] 
**resource_selector_filter** | [**list[ResourceSelectorFilter]**](ResourceSelectorFilter.md) | Filter based on whether it has a particular Resource. | [optional] 
**managed_filter** | **str** | Filter based on whether the Resource Group is Harness Managed. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

