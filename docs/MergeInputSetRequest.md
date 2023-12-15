# MergeInputSetRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_set_references** | **list[str]** | List of Input Set References to be merged | [optional] 
**with_merged_pipeline_yaml** | **bool** | This is a boolean value that indicates if the response must contain the YAML for the merged Pipeline. The default value is False. | [optional] 
**stage_identifiers** | **list[str]** | List of Stage Ids. Input Sets corresponding to these Ids will be merged. | [optional] 
**last_yaml_to_merge** | **str** | Runtime Input Yaml needed to be merged into the result of the merged Yaml of the inputSetReferences | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

