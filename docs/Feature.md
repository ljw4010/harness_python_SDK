# Feature

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archived** | **bool** | Indicates if the flag has been archived and is no longer used | [optional] 
**created_at** | **int** | The date the flag was created in milliseconds | 
**default_off_variation** | **str** | The default value returned when a flag is off | 
**default_on_variation** | **str** | The default value returned when a flag is on | 
**description** | **str** | A description for this flag | [optional] 
**env_properties** | [**FeatureEnvProperties**](FeatureEnvProperties.md) |  | [optional] 
**evaluation** | **str** | The value that the flag will return for the current user | [optional] 
**evaluation_identifier** | **str** | The identifier for the returned evaluation | [optional] 
**identifier** | **str** | The Feature Flag identifier | 
**kind** | **str** | The type of Feature flag | 
**modified_at** | **int** | The date the flag was last modified in milliseconds | [optional] 
**name** | **str** | The name of the Feature Flag | 
**owner** | **list[str]** | The user who created the flag | [optional] 
**permanent** | **bool** | Indicates if this is a permanent flag, or one that should expire | [optional] 
**prerequisites** | [**list[Prerequisite]**](Prerequisite.md) |  | [optional] 
**project** | **str** | The project this Feature belongs to | 
**results** | [**list[Results]**](Results.md) | The results shows which variations have been evaluated, and how many times each of these have been evaluated. | [optional] 
**services** | [**list[CfService]**](CfService.md) | A list of services linked to this Feature Flag | [optional] 
**stale** | **bool** | Whether the flag is stale or not | [optional] 
**stale_reason** | **str** | The reason that the flag was marked as stale | [optional] 
**status** | [**FeatureStatus**](FeatureStatus.md) |  | [optional] 
**tags** | [**list[Tag]**](Tag.md) | A list of tags for this Feature Flag | [optional] 
**variations** | [**list[Variation]**](Variation.md) | The variations that can be returned for this flag | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

