# InputSetErrorWrapper

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_pipeline_yaml** | **str** | If an Input Set save fails, this field contains the error fields, with the field values replaced with a UUID | [optional] 
**uuid_to_error_response_map** | [**dict(str, InputSetErrorWrapper)**](InputSetErrorWrapper.md) | If an Input Set save fails, this field contains the map from FQN to why that FQN threw an error | [optional] 
**invalid_input_set_references** | **list[str]** | List of Input Sets that are invalid | [optional] 
**type** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

