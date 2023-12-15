# GitFullSyncConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_identifier** | **str** | Account Identifier for the Entity. | [optional] 
**org_identifier** | **str** | Organization Identifier for the Entity. | [optional] 
**project_identifier** | **str** | Project Identifier for the Entity. | [optional] 
**base_branch** | **str** | Name of the branch from which the new branch will be forked out. | [optional] 
**branch** | **str** | Name of the branch. Entities were pushed to this branch, and a pull request was made from it. | [optional] 
**pr_title** | **str** | Title of the pull request. | [optional] 
**create_pull_request** | **bool** | Determines if pull request was created. | [optional] 
**repo_identifier** | **str** | Git Sync Config Id. | [optional] 
**is_new_branch** | **bool** |  | [optional] 
**target_branch** | **str** | Name of the target branch of the pull request. | [optional] 
**root_folder** | **str** | Path of the root folder inside which entities were pushed. | [optional] 
**new_branch** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

