# ECSRecommendationDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**cluster_name** | **str** |  | [optional] 
**service_arn** | **str** |  | [optional] 
**service_name** | **str** |  | [optional] 
**launch_type** | **str** |  | [optional] 
**current** | **dict(str, str)** |  | [optional] 
**percentile_based** | **dict(str, dict(str, str))** |  | [optional] 
**last_day_cost** | [**Cost**](Cost.md) |  | [optional] 
**cpu_histogram** | [**HistogramExp**](HistogramExp.md) |  | [optional] 
**memory_histogram** | [**HistogramExp**](HistogramExp.md) |  | [optional] 
**jira_details** | [**CCMJiraDetails**](CCMJiraDetails.md) |  | [optional] 
**service_now_details** | [**CCMServiceNowDetails**](CCMServiceNowDetails.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

