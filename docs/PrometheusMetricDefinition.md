# PrometheusMetricDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** |  | 
**metric_name** | **str** |  | 
**risk_profile** | [**RiskProfile**](RiskProfile.md) |  | [optional] 
**analysis** | [**AnalysisDTO**](AnalysisDTO.md) |  | [optional] 
**sli** | [**SLIDTO**](SLIDTO.md) |  | [optional] 
**query** | **str** |  | [optional] 
**group_name** | **str** |  | [optional] 
**service_instance_field_name** | **str** |  | [optional] 
**prometheus_metric** | **str** |  | [optional] 
**service_filter** | [**list[PrometheusFilter]**](PrometheusFilter.md) |  | [optional] 
**env_filter** | [**list[PrometheusFilter]**](PrometheusFilter.md) |  | [optional] 
**additional_filters** | [**list[PrometheusFilter]**](PrometheusFilter.md) |  | [optional] 
**aggregation** | **str** |  | [optional] 
**is_manual_query** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

