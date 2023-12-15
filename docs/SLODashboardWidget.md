# SLODashboardWidget

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slo_identifier** | **str** |  | 
**title** | **str** |  | 
**monitored_service_identifier** | **str** |  | [optional] 
**monitored_service_name** | **str** |  | [optional] 
**health_source_identifier** | **str** |  | [optional] 
**health_source_name** | **str** |  | [optional] 
**service_identifier** | **str** |  | [optional] 
**service_name** | **str** |  | [optional] 
**environment_identifier** | **str** |  | [optional] 
**environment_name** | **str** |  | [optional] 
**monitored_service_details** | [**list[MonitoredServiceDetail]**](MonitoredServiceDetail.md) |  | [optional] 
**tags** | **dict(str, str)** |  | [optional] 
**evaluation_type** | **str** |  | [optional] 
**slo_type** | **str** |  | 
**burn_rate** | [**BurnRate**](BurnRate.md) |  | 
**time_remaining_days** | **int** |  | 
**error_budget_remaining_percentage** | **float** |  | 
**error_budget_remaining** | **int** |  | 
**total_error_budget** | **int** |  | 
**slo_target_type** | **str** |  | 
**current_period_length_days** | **int** |  | 
**current_period_start_time** | **int** |  | 
**current_period_end_time** | **int** |  | 
**slo_target_percentage** | **float** |  | 
**error_budget_burndown** | [**list[Point]**](Point.md) |  | 
**slo_performance_trend** | [**list[Point]**](Point.md) |  | 
**is_total_error_budget_applicable** | **bool** |  | [optional] 
**is_recalculating_sli** | **bool** |  | [optional] 
**is_calculating_sli** | **bool** |  | [optional] 
**slo_error** | [**SLOError**](SLOError.md) |  | [optional] 
**recalculating_sli** | **bool** |  | [optional] 
**error_budget_risk** | **str** |  | 
**calculating_sli** | **bool** |  | [optional] 
**total_error_budget_applicable** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

