# FeatureEnvProperties

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_serve** | [**Serve**](Serve.md) |  | 
**environment** | **str** | The environment identifier | 
**jira_enabled** | **bool** | Indicates whether jira functionality is enabled for the given account, project, org, and environment | [optional] 
**jira_issues** | [**list[JiraIssue]**](JiraIssue.md) | An array of Jira Issues linked to this Feature. Returns empty if none exist | [optional] 
**modified_at** | **int** | The last time the flag was modified in this environment | [optional] 
**off_variation** | **str** | The variation to serve for this flag in this environment when the flag is off | 
**pipeline_configured** | **bool** |  | 
**pipeline_details** | [**FeaturePipeline**](FeaturePipeline.md) |  | [optional] 
**pipeline_error_reason** | **str** |  | [optional] 
**pipeline_error_state** | **bool** |  | [optional] 
**rules** | [**list[ServingRule]**](ServingRule.md) | A list of rules to use when evaluating this flag in this environment | [optional] 
**state** | [**FeatureState**](FeatureState.md) |  | 
**variation_map** | [**list[VariationMap]**](VariationMap.md) | A list of the variations that will be served to specific targets or target groups in an environment. | [optional] 
**version** | **int** | The version of the flag.  This is incremented each time it is changed | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

