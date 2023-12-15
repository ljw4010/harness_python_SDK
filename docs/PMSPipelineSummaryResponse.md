# PMSPipelineSummaryResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**identifier** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**tags** | **dict(str, str)** |  | [optional] 
**version** | **int** |  | [optional] 
**num_of_stages** | **int** |  | [optional] 
**created_at** | **int** |  | [optional] 
**last_updated_at** | **int** |  | [optional] 
**modules** | **list[str]** |  | [optional] 
**execution_summary_info** | [**ExecutionSummaryInfo**](ExecutionSummaryInfo.md) |  | [optional] 
**filters** | **dict(str, dict(str, object))** |  | [optional] 
**stage_names** | **list[str]** |  | [optional] 
**git_details** | [**PipelineEntityGitDetails**](PipelineEntityGitDetails.md) |  | [optional] 
**entity_validity_details** | [**PipelineEntityGitDetails**](PipelineEntityGitDetails.md) |  | [optional] 
**store_type** | **str** |  | [optional] 
**connector_ref** | **str** |  | [optional] 
**is_draft** | **bool** |  | [optional] 
**yaml_version** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

