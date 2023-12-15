# ApplicationsApplicationSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**ApplicationsApplicationSource**](ApplicationsApplicationSource.md) |  | [optional] 
**destination** | [**ApplicationsApplicationDestination**](ApplicationsApplicationDestination.md) |  | [optional] 
**project** | **str** | Project is a reference to the project this application belongs to. The empty string means that application belongs to the &#x27;default&#x27; project. | [optional] 
**sync_policy** | [**ApplicationsSyncPolicy**](ApplicationsSyncPolicy.md) |  | [optional] 
**ignore_differences** | [**list[ApplicationsResourceIgnoreDifferences]**](ApplicationsResourceIgnoreDifferences.md) |  | [optional] 
**info** | [**list[ApplicationsInfo]**](ApplicationsInfo.md) |  | [optional] 
**revision_history_limit** | **str** | RevisionHistoryLimit limits the number of items kept in the application&#x27;s revision history, which is used for informational purposes as well as for rollbacks to previous versions. This should only be changed in exceptional circumstances. Setting to zero will store no history. This will reduce storage used. Increasing will increase the space used to store the history, so we do not recommend increasing it. Default is 10. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

