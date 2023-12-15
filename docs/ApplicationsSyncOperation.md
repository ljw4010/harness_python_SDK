# ApplicationsSyncOperation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**revision** | **str** | Revision is the revision (Git) or chart version (Helm) which to sync the application to If omitted, will use the revision specified in app spec. | [optional] 
**prune** | **bool** |  | [optional] 
**dry_run** | **bool** |  | [optional] 
**sync_strategy** | [**ApplicationsSyncStrategy**](ApplicationsSyncStrategy.md) |  | [optional] 
**resources** | [**list[ApplicationsSyncOperationResource]**](ApplicationsSyncOperationResource.md) |  | [optional] 
**source** | [**ApplicationsApplicationSource**](ApplicationsApplicationSource.md) |  | [optional] 
**manifests** | **list[str]** |  | [optional] 
**sync_options** | **list[str]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

