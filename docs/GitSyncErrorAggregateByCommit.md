# GitSyncErrorAggregateByCommit

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**git_commit_id** | **str** | Commit Id | [optional] 
**failed_count** | **int** | The number of active errors in a commit | [optional] 
**repo_id** | **str** | Git Sync Config Id. | [optional] 
**branch_name** | **str** | Name of the branch. | [optional] 
**commit_message** | **str** | Commit Message to use for the merge commit. | [optional] 
**created_at** | **int** | This is the time at which the Git Sync error was logged | [optional] 
**errors_for_summary_view** | [**list[GitSyncError]**](GitSyncError.md) | This has the list of Git Sync errors corresponding to a specific Commit Id | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

