# GraphLayoutNode

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_type** | **str** |  | [optional] 
**node_group** | **str** |  | [optional] 
**node_identifier** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**node_uuid** | **str** |  | [optional] 
**status** | **str** | This is the Execution Status of the entity | [optional] 
**module** | **str** |  | [optional] 
**module_info** | **dict(str, dict(str, object))** |  | [optional] 
**start_ts** | **int** |  | [optional] 
**end_ts** | **int** |  | [optional] 
**edge_layout_list** | [**EdgeLayoutList**](EdgeLayoutList.md) |  | [optional] 
**skip_info** | [**SkipInfo**](SkipInfo.md) |  | [optional] 
**node_run_info** | [**NodeRunInfo**](NodeRunInfo.md) |  | [optional] 
**barrier_found** | **bool** |  | [optional] 
**failure_info** | [**ExecutionErrorInfo**](ExecutionErrorInfo.md) |  | [optional] 
**failure_info_dto** | [**FailureInfoDTO**](FailureInfoDTO.md) |  | [optional] 
**step_details** | [**dict(str, PmsStepDetails)**](PmsStepDetails.md) |  | [optional] 
**hidden** | **bool** |  | [optional] 
**node_execution_id** | **str** |  | [optional] 
**strategy_metadata** | [**StrategyMetadata**](StrategyMetadata.md) |  | [optional] 
**execution_input_configured** | **bool** |  | [optional] 
**is_rollback_stage_node** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

