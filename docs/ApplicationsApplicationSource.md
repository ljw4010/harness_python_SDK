# ApplicationsApplicationSource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repo_url** | **str** |  | [optional] 
**path** | **str** | Path is a directory path within the Git repository, and is only valid for applications sourced from Git. | [optional] 
**target_revision** | **str** | TargetRevision defines the revision of the source to sync the application to. In case of Git, this can be commit, tag, or branch. If omitted, will equal to HEAD. In case of Helm, this is a semver tag for the Chart&#x27;s version. | [optional] 
**helm** | [**ApplicationsApplicationSourceHelm**](ApplicationsApplicationSourceHelm.md) |  | [optional] 
**kustomize** | [**ApplicationsApplicationSourceKustomize**](ApplicationsApplicationSourceKustomize.md) |  | [optional] 
**ksonnet** | [**ApplicationsApplicationSourceKsonnet**](ApplicationsApplicationSourceKsonnet.md) |  | [optional] 
**directory** | [**ApplicationsApplicationSourceDirectory**](ApplicationsApplicationSourceDirectory.md) |  | [optional] 
**plugin** | [**ApplicationsApplicationSourcePlugin**](ApplicationsApplicationSourcePlugin.md) |  | [optional] 
**chart** | **str** | Chart is a Helm chart name, and must be specified for applications sourced from a Helm repo. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

