# Budget

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**account_id** | **str** |  | 
**name** | **str** |  | 
**scope** | [**BudgetScope**](BudgetScope.md) |  | [optional] 
**type** | **str** | Whether the Budget is based on a specified amount or based on previous month&#x27;s actual spend | [optional] 
**budget_monthly_breakdown** | [**BudgetMonthlyBreakdown**](BudgetMonthlyBreakdown.md) |  | [optional] 
**budget_amount** | **float** |  | [optional] 
**period** | **str** |  | [optional] 
**growth_rate** | **float** |  | [optional] 
**actual_cost** | **float** |  | [optional] 
**forecast_cost** | **float** |  | [optional] 
**last_month_cost** | **float** |  | [optional] 
**alert_thresholds** | [**list[AlertThreshold]**](AlertThreshold.md) |  | [optional] 
**email_addresses** | **list[str]** |  | [optional] 
**user_group_ids** | **list[str]** |  | [optional] 
**parent_budget_group_id** | **str** |  | [optional] 
**notify_on_slack** | **bool** |  | [optional] 
**is_ng_budget** | **bool** |  | [optional] 
**start_time** | **int** |  | [optional] 
**end_time** | **int** |  | [optional] 
**created_at** | **int** |  | [optional] 
**last_updated_at** | **int** |  | [optional] 
**budget_history** | [**dict(str, BudgetCostData)**](BudgetCostData.md) |  | [optional] 
**disable_currency_warning** | **bool** |  | [optional] 
**ng_budget** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

