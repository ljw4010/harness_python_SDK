# PolicyManagementPolicySet

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | Harness account ID associated with this policy set | [default to '']
**action** | **str** | Action that triggers the policy set | 
**created** | **int** | Time the policy set was created | 
**description** | **str** | Description of the policy set | [optional] 
**enabled** | **bool** | Only enabled policy sets are evaluated when evaluating by type/action | 
**entity_selector** | **str** | A string enum value which determines which entities the policy set applies to during evaluation | 
**identifier** | **str** | Identifier of the policy set | 
**name** | **str** | Name of the policy set | 
**org_id** | **str** | Harness organization ID associated with this policy set | [default to '']
**policies** | [**list[LinkedPolicy]**](LinkedPolicy.md) | Policies linked to this policy set | [optional] 
**project_id** | **str** | Harness project ID associated with this policy set | [default to '']
**resource_groups** | [**list[PolicyManagementResourceGroup]**](PolicyManagementResourceGroup.md) | The groups of resources that this policy set should be applied to | [optional] 
**type** | **str** | Type of input suitable for the policy set | 
**updated** | **int** | Time the policy set was last updated | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

