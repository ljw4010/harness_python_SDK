# PipelineExecutionSummary

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pipeline_identifier** | **str** |  | [optional] 
**org_identifier** | **str** |  | 
**project_identifier** | **str** |  | 
**plan_execution_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**yaml_version** | **str** |  | [optional] 
**status** | **str** | This is the Execution Status of the entity | [optional] 
**tags** | [**list[NGTag]**](NGTag.md) |  | [optional] 
**execution_trigger_info** | [**ExecutionTriggerInfo**](ExecutionTriggerInfo.md) |  | [optional] 
**execution_error_info** | [**ExecutionErrorInfo**](ExecutionErrorInfo.md) |  | [optional] 
**governance_metadata** | [**PipelineGovernanceMetadata**](PipelineGovernanceMetadata.md) |  | [optional] 
**failure_info** | [**FailureInfoDTO**](FailureInfoDTO.md) |  | [optional] 
**module_info** | **dict(str, dict(str, object))** |  | [optional] 
**layout_node_map** | [**dict(str, GraphLayoutNode)**](GraphLayoutNode.md) |  | [optional] 
**modules** | **list[str]** |  | [optional] 
**starting_node_id** | **str** |  | [optional] 
**start_ts** | **int** |  | [optional] 
**end_ts** | **int** |  | [optional] 
**created_at** | **int** |  | [optional] 
**can_retry** | **bool** |  | [optional] 
**show_retry_history** | **bool** |  | [optional] 
**run_sequence** | **int** |  | [optional] 
**successful_stages_count** | **int** |  | [optional] 
**running_stages_count** | **int** |  | [optional] 
**failed_stages_count** | **int** |  | [optional] 
**total_stages_count** | **int** |  | [optional] 
**git_details** | [**PipelineEntityGitDetails**](PipelineEntityGitDetails.md) |  | [optional] 
**store_type** | **str** |  | [optional] 
**connector_ref** | **str** |  | [optional] 
**execution_input_configured** | **bool** |  | [optional] 
**is_stages_execution** | **bool** |  | [optional] 
**parent_stage_info** | [**PipelineStageInfo**](PipelineStageInfo.md) |  | [optional] 
**stages_executed** | **list[str]** |  | [optional] 
**stages_executed_names** | **dict(str, str)** |  | [optional] 
**allow_stage_executions** | **bool** |  | [optional] 
**aborted_by** | [**AbortedBy**](AbortedBy.md) |  | [optional] 
**execution_mode** | **str** |  | [optional] 
**notes_exist_for_plan_execution_id** | **bool** |  | [optional] 
**should_use_simplified_key** | **bool** |  | [optional] 
**stages_execution** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

