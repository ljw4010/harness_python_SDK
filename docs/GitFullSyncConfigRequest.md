# GitFullSyncConfigRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branch** | **str** | Name of the branch to which the entities will be pushed and from which pull request will be created. | 
**repo_identifier** | **str** | Git Sync Config Id. | 
**root_folder** | **str** | Path of the root folder inside which the entities will be pushed. | 
**is_new_branch** | **bool** |  | [optional] 
**base_branch** | **str** | Name of the branch from which new branch will be forked out. | [optional] 
**create_pull_request** | **bool** | If true a pull request will be created from branch to target branch.Default: false. | [optional] 
**target_branch** | **str** | Name of the branch to which pull request will be merged. | [optional] 
**pr_title** | **str** | Title of the pull request. | [optional] 
**new_branch** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

