# InputSetErrorDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**valid** | **bool** | Specifies whether Input Set is a valid or not. | [optional] 
**message** | **str** | Failure message for Input Set. | [optional] 
**outdated** | **bool** | Input Set is outdated with respect to the Pipeline or not. | [optional] 
**error_pipeline_yaml** | **str** | If an Input Set save fails, this field contains the Pipeline YAML as a String, with the field values replaced by a UUID. | [optional] 
**fqn_errors** | [**list[FQNtoError]**](FQNtoError.md) |  | [optional] 
**invalid_refs** | **list[str]** | List of Input Set References that are invalid. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

