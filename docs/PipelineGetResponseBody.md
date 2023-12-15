# PipelineGetResponseBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pipeline_yaml** | **str** | Pipeline YAML (returned as a String). | [optional] 
**template_applied_pipeline_yaml** | **str** | Pipeline YAML after resolving Templates (returned as a String). | [optional] 
**identifier** | **str** | Pipeline identifier | [optional] 
**name** | **str** | Pipeline name | [optional] 
**org** | **str** | Organization identifier | [optional] 
**project** | **str** | Project identifier | [optional] 
**description** | **str** | Pipeline description | [optional] 
**tags** | **dict(str, str)** | Pipeline tags | [optional] 
**modules** | **list[str]** | Modules utilised in the Pipeline. | [optional] 
**git_details** | [**GitDetails**](GitDetails.md) |  | [optional] 
**valid** | **bool** | Specifies whether Pipeline is a valid or not. | [optional] 
**yaml_error_wrapper** | [**list[YAMLSchemaErrorWrapper]**](YAMLSchemaErrorWrapper.md) | YAML schema errors. | [optional] 
**cache_response_metadata** | [**CacheResponseMetadataDTO**](CacheResponseMetadataDTO.md) |  | [optional] 
**created** | **int** | Creation timestamp for Pipeline. | [optional] 
**updated** | **int** | Last modification timestamp for Pipeline. | [optional] 
**validation_uuid** | **str** | UUID of the asynchronous validation event started, if any | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

