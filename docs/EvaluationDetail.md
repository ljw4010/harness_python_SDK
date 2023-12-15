# EvaluationDetail

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | Harness account ID associated with this policy set | [default to '']
**action** | **str** | Action that triggers the policy set | 
**created** | **int** | Time the policy set was created | 
**description** | **str** | Description of the policy set | [optional] 
**details** | [**list[EvaluatedPolicy]**](EvaluatedPolicy.md) |  | 
**enabled** | **bool** | Only enabled policy sets are evaluated when evaluating by type/action | 
**identifier** | **str** | Identifier of the policy set | 
**name** | **str** | Name of the policy set | 
**org_id** | **str** | Harness organization ID associated with this policy set | [default to '']
**project_id** | **str** | Harness project ID associated with this policy set | [default to '']
**status** | **str** | The overall status for this policy set indicating whether it passed | 
**type** | **str** | Type of input suitable for the policy set | 
**updated** | **int** | Time the policy set was last updated | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

