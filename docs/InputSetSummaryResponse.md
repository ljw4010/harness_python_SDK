# InputSetSummaryResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Input Set Identifier | [optional] 
**name** | **str** | Input Set Name | [optional] 
**pipeline_identifier** | **str** | Pipeline Identifier for the entity. | [optional] 
**description** | **str** | Input Set description | [optional] 
**input_set_type** | **str** | Type of Input Set. The default value is ALL. | [optional] 
**tags** | **dict(str, str)** | Input Set tags | [optional] 
**git_details** | [**PipelineEntityGitDetails**](PipelineEntityGitDetails.md) |  | [optional] 
**created_at** | **int** | Time at which the entity was created | [optional] 
**last_updated_at** | **int** | Time at which the entity was last updated | [optional] 
**is_outdated** | **bool** | This field is true if a Pipeline update has made this Input Set invalid, and cannot be used for Pipeline Execution | [optional] 
**input_set_error_details** | [**InputSetErrorWrapper**](InputSetErrorWrapper.md) |  | [optional] 
**overlay_set_error_details** | **dict(str, str)** | This contains the invalid references in the Overlay Input Set, along with a message why they are invalid | [optional] 
**entity_validity_details** | [**PipelineEntityGitDetails**](PipelineEntityGitDetails.md) |  | [optional] 
**modules** | **list[str]** | Modules in which the Pipeline belongs | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

