# MonitoredServiceListItemDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**identifier** | **str** |  | [optional] 
**service_ref** | **str** |  | [optional] 
**environment_ref** | **str** |  | [optional] 
**environment_ref_list** | **list[str]** |  | [optional] 
**service_name** | **str** |  | [optional] 
**environment_name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**health_monitoring_enabled** | **bool** |  | [optional] 
**current_health_score** | [**RiskData**](RiskData.md) |  | [optional] 
**dependent_health_score** | [**list[RiskData]**](RiskData.md) |  | [optional] 
**historical_trend** | [**HistoricalTrend**](HistoricalTrend.md) |  | [optional] 
**change_summary** | [**ChangeSummaryDTO**](ChangeSummaryDTO.md) |  | [optional] 
**tags** | **dict(str, str)** |  | [optional] 
**service_monitoring_enabled** | **bool** |  | [optional] 
**slo_health_indicators** | [**list[SloHealthIndicatorDTO]**](SloHealthIndicatorDTO.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

