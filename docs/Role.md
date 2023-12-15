# Role

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Unique identifier of the role | 
**name** | **str** | Name of the role | 
**permissions** | **list[str]** | List of the permission identifiers (Subset of the list returned by GET /authz/api/permissions) | [optional] 
**allowed_scope_levels** | **list[str]** | The scope levels at which this role can be used | [optional] 
**description** | **str** | Description of the role | [optional] 
**tags** | **dict(str, str)** | Tags | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

