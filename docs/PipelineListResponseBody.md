# PipelineListResponseBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Pipeline identifier | [optional] 
**name** | **str** | Pipeline name | [optional] 
**description** | **str** | Pipeline description | [optional] 
**tags** | **dict(str, str)** | Pipeline tags | [optional] 
**created** | **int** | Creation timestamp for Pipeline. | [optional] 
**updated** | **int** | Last modification timestamp for Pipeline. | [optional] 
**modules** | **list[str]** | Modules utilised in the Pipeline. | [optional] 
**recent_execution_info** | [**list[RecentExecutionInfo]**](RecentExecutionInfo.md) | Array of recent Execution information | [optional] 
**store_type** | **str** | Specifies whether the Entity is to be stored in Git or not (for Git Experience). | [optional] 
**connector_ref** | **str** | Identifier of the Harness Connector used for CRUD operations on the Entity (for Git Experience). | [optional] 
**valid** | **bool** | Specifies whether Pipeline is a valid or not. | [optional] 
**git_details** | [**GitDetails**](GitDetails.md) |  | [optional] 
**yaml_version** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

