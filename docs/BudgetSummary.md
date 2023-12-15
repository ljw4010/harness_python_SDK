# BudgetSummary

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**perspective_id** | **str** |  | [optional] 
**perspective_name** | **str** |  | [optional] 
**folder_id** | **str** |  | [optional] 
**budget_amount** | **float** |  | [optional] 
**actual_cost** | **float** |  | [optional] 
**forecast_cost** | **float** |  | [optional] 
**time_left** | **int** |  | [optional] 
**time_unit** | **str** |  | [optional] 
**time_scope** | **str** |  | [optional] 
**actual_cost_alerts** | **list[float]** |  | [optional] 
**forecast_cost_alerts** | **list[float]** |  | [optional] 
**alert_thresholds** | [**list[AlertThreshold]**](AlertThreshold.md) |  | [optional] 
**period** | **str** |  | [optional] 
**type** | **str** | Whether the Budget is based on a specified amount or based on previous month&#x27;s actual spend | [optional] 
**growth_rate** | **float** |  | [optional] 
**start_time** | **int** |  | [optional] 
**budget_monthly_breakdown** | [**BudgetMonthlyBreakdown**](BudgetMonthlyBreakdown.md) |  | [optional] 
**child_entity_proportions** | [**list[BudgetGroupChildEntityDTO]**](BudgetGroupChildEntityDTO.md) |  | [optional] 
**is_budget_group** | **bool** |  | [optional] 
**cascade_type** | **str** |  | [optional] 
**parent_id** | **str** |  | [optional] 
**disable_currency_warning** | **bool** |  | [optional] 
**budget_group** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

