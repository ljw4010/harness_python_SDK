# ExecutionNode

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**setup_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**identifier** | **str** |  | [optional] 
**base_fqn** | **str** |  | [optional] 
**outcomes** | [**dict(str, OrchestrationMap)**](OrchestrationMap.md) |  | [optional] 
**step_parameters** | [**OrchestrationMap**](OrchestrationMap.md) |  | [optional] 
**start_ts** | **int** |  | [optional] 
**end_ts** | **int** |  | [optional] 
**step_type** | **str** |  | [optional] 
**status** | **str** | This is the Execution Status of the entity | [optional] 
**failure_info** | [**FailureInfoDTO**](FailureInfoDTO.md) |  | [optional] 
**skip_info** | [**SkipInfo**](SkipInfo.md) |  | [optional] 
**node_run_info** | [**NodeRunInfo**](NodeRunInfo.md) |  | [optional] 
**executable_responses** | [**list[ExecutableResponse]**](ExecutableResponse.md) |  | [optional] 
**unit_progresses** | [**list[UnitProgress]**](UnitProgress.md) |  | [optional] 
**progress_data** | [**OrchestrationMap**](OrchestrationMap.md) |  | [optional] 
**delegate_info_list** | [**list[DelegateInfo]**](DelegateInfo.md) |  | [optional] 
**interrupt_histories** | [**list[InterruptEffectDTO]**](InterruptEffectDTO.md) |  | [optional] 
**step_details** | [**dict(str, OrchestrationMap)**](OrchestrationMap.md) |  | [optional] 
**strategy_metadata** | [**StrategyMetadata**](StrategyMetadata.md) |  | [optional] 
**execution_input_configured** | **bool** |  | [optional] 
**log_base_key** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

