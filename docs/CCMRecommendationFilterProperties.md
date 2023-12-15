# CCMRecommendationFilterProperties

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**k8s_recommendation_filter_properties_dto** | [**K8sRecommendationFilterProperties**](K8sRecommendationFilterProperties.md) |  | [optional] 
**perspective_filters** | [**list[QLCEViewFilterWrapper]**](QLCEViewFilterWrapper.md) | Get Recommendations for a perspective | [optional] 
**min_saving** | **float** | Fetch recommendations with Saving more than minSaving | [optional] 
**min_cost** | **float** | Fetch recommendations with Cost more than minCost | [optional] 
**days_back** | **int** | Fetch recommendations generated in last daysBack days | [optional] 
**offset** | **int** | Query Offset | [optional] 
**limit** | **int** | Query Limit | [optional] 
**tags** | **dict(str, str)** | Filter tags as a key-value pair. | [optional] 
**filter_type** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

