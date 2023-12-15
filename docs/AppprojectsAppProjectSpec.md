# AppprojectsAppProjectSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_repos** | **list[str]** |  | [optional] 
**destinations** | [**list[AppprojectsApplicationDestination]**](AppprojectsApplicationDestination.md) |  | [optional] 
**description** | **str** |  | [optional] 
**roles** | [**list[AppprojectsProjectRole]**](AppprojectsProjectRole.md) |  | [optional] 
**cluster_resource_whitelist** | [**list[V1GroupKind]**](V1GroupKind.md) |  | [optional] 
**namespace_resource_blacklist** | [**list[V1GroupKind]**](V1GroupKind.md) |  | [optional] 
**orphaned_resources** | [**AppprojectsOrphanedResourcesMonitorSettings**](AppprojectsOrphanedResourcesMonitorSettings.md) |  | [optional] 
**sync_windows** | [**list[AppprojectsSyncWindow]**](AppprojectsSyncWindow.md) |  | [optional] 
**namespace_resource_whitelist** | [**list[V1GroupKind]**](V1GroupKind.md) |  | [optional] 
**signature_keys** | [**list[AppprojectsSignatureKey]**](AppprojectsSignatureKey.md) |  | [optional] 
**cluster_resource_blacklist** | [**list[V1GroupKind]**](V1GroupKind.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

