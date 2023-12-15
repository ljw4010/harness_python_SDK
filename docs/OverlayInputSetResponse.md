# OverlayInputSetResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | Account Identifier for the Entity. | [optional] 
**org_identifier** | **str** | Organization Identifier for the Entity. | [optional] 
**project_identifier** | **str** | Project Identifier for the Entity. | [optional] 
**pipeline_identifier** | **str** | Pipeline Identifier for the entity. | [optional] 
**identifier** | **str** | Input Set Identifier | [optional] 
**name** | **str** | Input Set Name | [optional] 
**description** | **str** | Input Set description | [optional] 
**input_set_references** | **list[str]** | Input Set References in the Overlay Input Set | [optional] 
**overlay_input_set_yaml** | **str** | Overlay Input Set YAML | [optional] 
**tags** | **dict(str, str)** | Input Set tags | [optional] 
**is_outdated** | **bool** |  | [optional] 
**is_error_response** | **bool** |  | [optional] 
**invalid_input_set_references** | **dict(str, str)** | This contains the invalid references in the Overlay Input Set, along with a message why they are invalid | [optional] 
**git_details** | [**PipelineEntityGitDetails**](PipelineEntityGitDetails.md) |  | [optional] 
**entity_validity_details** | [**PipelineEntityGitDetails**](PipelineEntityGitDetails.md) |  | [optional] 
**outdated** | **bool** |  | [optional] 
**error_response** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

