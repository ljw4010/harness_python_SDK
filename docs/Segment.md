# Segment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **int** | The data and time in milliseconds when the group was created | [optional] 
**environment** | **str** | The environment this target group belongs to | [optional] 
**excluded** | [**list[Target]**](Target.md) | A list of Targets who are excluded from this target group | [optional] 
**identifier** | **str** | Unique identifier for the target group. | 
**included** | [**list[Target]**](Target.md) | A list of Targets who belong to this target group | [optional] 
**modified_at** | **int** | The data and time in milliseconds when the group was last modified | [optional] 
**name** | **str** | Name of the target group. | 
**rules** | [**list[Clause]**](Clause.md) | An array of rules that can cause a user to be included in this segment. | [optional] 
**tags** | [**list[Tag]**](Tag.md) | Tags for this target group | [optional] 
**version** | **int** | The version of this group.  Each time it is modified the version is incremented | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

