# UpdateRequestBody2

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Action that triggers the policy set | [optional] 
**description** | **str** | Description of the policy set | [optional] 
**enabled** | **bool** | Only enabled policy sets are evaluated when evaluating by type/action | [optional] 
**entity_selector** | **str** | A string enum value which determines which entities the policy set applies to during evaluation. This feature is not available for all accounts, Contact support if you wish to have it enabled. | [optional] 
**name** | **str** | Name of the policy set | [optional] 
**policies** | [**list[Linkedpolicyidentifier]**](Linkedpolicyidentifier.md) | Policies linked to this policy set | [optional] 
**resource_groups** | [**list[ResourceGroupIdentifier]**](ResourceGroupIdentifier.md) | Resource groups that contain the resources that this policy set should be evaluated for. Resource groups are not supported for flag or custom policy sets. This feature is not available for all accounts, Contact support if you wish to have it enabled. | [optional] 
**type** | **str** | Type of input suitable for the policy set | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

