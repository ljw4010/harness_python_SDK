# PolicyManagementPolicy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | Harness account ID associated with this policy | [default to '']
**created** | **int** | Time the policy was created | 
**git_commit_sha** | **str** | The commit sha of the commit that last effected the file | [optional] 
**git_connector_ref** | **str** | The harness connector used for authenticating on the git provider | [optional] 
**git_default_branch** | **str** | The default branch, the service pulls in changes from from this branch for policy evaluation | [optional] 
**git_default_branch_commit_sha** | **str** | The commit sha of the commit that last effected the file in the default branch | [optional] 
**git_default_branch_file_id** | **str** | The file id of the file in the default branch, may be empty for bitbucket files | [optional] 
**git_default_branch_file_url** | **str** | The url of the file in the default branch | [optional] 
**git_default_branch_update_error** | [**GitErrorResult**](GitErrorResult.md) |  | [optional] 
**git_default_branch_updated** | **int** | The last time the service successfully pulled in changes from the default branch | [optional] 
**git_file_id** | **str** | The file id of the file, may be empty for bitbucket files | [optional] 
**git_file_url** | **str** | The url of the file on the fit provider | [optional] 
**git_path** | **str** | The path to the file in the git repo | [optional] 
**git_repo** | **str** | The git repo the policy resides in | [optional] 
**identifier** | **str** | identifier of the policy | 
**name** | **str** | Name of the policy | 
**org_id** | **str** | Harness organization ID associated with this policy | [default to '']
**project_id** | **str** | Harness project ID associated with this policy | [default to '']
**rego** | **str** | Rego that defines the policy | 
**updated** | **int** | Time the policy was last updated | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

