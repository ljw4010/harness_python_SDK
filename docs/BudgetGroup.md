# BudgetGroup

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**account_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**budget_group_monthly_breakdown** | [**BudgetMonthlyBreakdown**](BudgetMonthlyBreakdown.md) |  | [optional] 
**period** | **str** |  | [optional] 
**budget_group_amount** | **float** |  | [optional] 
**actual_cost** | **float** |  | [optional] 
**forecast_cost** | **float** |  | [optional] 
**last_month_cost** | **float** |  | [optional] 
**alert_thresholds** | [**list[AlertThreshold]**](AlertThreshold.md) |  | [optional] 
**child_entities** | [**list[BudgetGroupChildEntityDTO]**](BudgetGroupChildEntityDTO.md) |  | [optional] 
**parent_budget_group_id** | **str** |  | [optional] 
**cascade_type** | **str** |  | [optional] 
**start_time** | **int** |  | [optional] 
**end_time** | **int** |  | [optional] 
**created_at** | **int** |  | [optional] 
**last_updated_at** | **int** |  | [optional] 
**budget_group_history** | [**dict(str, BudgetCostData)**](BudgetCostData.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

