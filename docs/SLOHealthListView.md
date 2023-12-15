# SLOHealthListView

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slo_identifier** | **str** | Identifier of the SLO. | 
**name** | **str** | Name of the SLO. | 
**org_name** | **str** | Organization Name to which the SLO belongs. | [optional] 
**project_name** | **str** | Project Name to which the SLO belongs. | [optional] 
**monitored_service_identifier** | **str** | Identifier of the Monitored Service to which the SLO is associated. | [optional] 
**monitored_service_name** | **str** | Name of the Monitored Service to which the SLO is associated. | [optional] 
**service_identifier** | **str** | Identifier of the Service to which the SLO is associated. | [optional] 
**health_source_identifier** | **str** | Identifier of the Health Source to which the SLO is associated. | [optional] 
**health_source_name** | **str** | Identifier of the Health Source to which the SLO is associated. | [optional] 
**service_name** | **str** | Name of the Service to which the SLO is associated. | [optional] 
**environment_identifier** | **str** | Identifier of the Environment to which the SLO is associated. | [optional] 
**environment_name** | **str** | Name of the Environment to which the SLO is associated. | [optional] 
**tags** | **list[str]** | List of tags for SLO. | [optional] 
**description** | **str** | Description for the SLO. | [optional] 
**user_journey_name** | **str** | Name of the first User Journey for the SLO. | [optional] 
**user_journeys** | [**list[UserJourney]**](UserJourney.md) |  | [optional] 
**burn_rate** | **float** | Burn rate per day of the SLO. The unit is \&quot;Minutes\&quot; if the Evaluation type is Window, for Request based it&#x27;s \&quot;Request\&quot;. | 
**error_budget_remaining_percentage** | **float** | Error Budget Remaining Percentage of the SLO. | 
**error_budget_remaining** | **int** | Error Budget Remaining of the SLO. The unit is \&quot;Minutes\&quot; if the Evaluation type is Window, for Request based it&#x27;s \&quot;Request\&quot;. | 
**total_error_budget** | **int** | Total Error Budget of the SLO. The unit is \&quot;Minutes\&quot; if the Evaluation type is Window, for Request based it&#x27;s \&quot;Request\&quot;. | 
**slo_target_type** | [**SLOTargetType**](SLOTargetType.md) |  | [optional] 
**slo_type** | [**ServiceLevelObjectiveType**](ServiceLevelObjectiveType.md) |  | 
**slo_target_percentage** | **float** | Target Percentage of the SLO defined by the user. | 
**no_of_active_alerts** | **int** | Number of Notification Rules defined for the SLO. | 
**evaluation_type** | [**SLIEvaluationType**](SLIEvaluationType.md) |  | 
**downtime_status_details** | [**DowntimeStatusDetails**](DowntimeStatusDetails.md) |  | [optional] 
**project_params** | [**ProjectParams**](ProjectParams.md) |  | 
**slo_error** | [**SLOError**](SLOError.md) |  | [optional] 
**error_budget_risk** | **str** | Error Budget Risk for the SLO. - It&#x27;s Healthy if Error Budget Remaining Percentage &gt;&#x3D; 75. - It&#x27;s Observe if Error Budget Remaining Percentage &gt;&#x3D; 50 &lt; 75. - It&#x27;s Need Attention if Error Budget Remaining Percentage &gt;&#x3D; 25 &lt; 50. - It&#x27;s Unhealthy if Error Budget Remaining Percentage &gt;&#x3D; 0 &lt; 25. - It&#x27;s Exhausted if Error Budget Remaining Percentage &lt; 0.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

