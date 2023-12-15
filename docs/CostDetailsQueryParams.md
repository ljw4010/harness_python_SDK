# CostDetailsQueryParams

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**list[FieldFilter]**](FieldFilter.md) | Filters to be applied on the response. | [optional] 
**group_by** | **list[str]** | Fields on which the response will be grouped by. | [optional] 
**time_resolution** | **str** | Only applicable for Time Series Endpoints, defaults to DAY | [optional] 
**limit** | **int** | Limit on the number of cost values returned, 0 by default. | [optional] 
**sort_order** | **str** | Order of sorting on cost, Descending by default. | [optional] 
**offset** | **int** | Offset on the cost values returned, 10 by default. | [optional] 
**skip_round_off** | **bool** | Skip Rounding off the cost values returned, false by default. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

