# harness_python_sdk.GitSyncErrorsApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_git_sync_errors_count**](GitSyncErrorsApi.md#get_git_sync_errors_count) | **GET** /ng/api/git-sync-errors/count | Get Errors Count for the given scope, Repo and Branch
[**list_git_sync_errors**](GitSyncErrorsApi.md#list_git_sync_errors) | **GET** /ng/api/git-sync-errors | Lists Git to Harness Errors by file or connectivity errors for the given scope, Repo and Branch
[**list_git_to_harness_error_for_commit**](GitSyncErrorsApi.md#list_git_to_harness_error_for_commit) | **GET** /ng/api/git-sync-errors/commits/{commitId} | Lists Git to Harness Errors for the given Commit Id
[**list_git_to_harness_errors_grouped_by_commits**](GitSyncErrorsApi.md#list_git_to_harness_errors_grouped_by_commits) | **GET** /ng/api/git-sync-errors/aggregate | Lists Git to Harness Errors grouped by Commits for the given scope, Repo and Branch

# **get_git_sync_errors_count**
> ResponseDTOGitSyncErrorCount get_git_sync_errors_count(account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, search_term=search_term, branch=branch, repo_identifier=repo_identifier, get_default_from_other_repo=get_default_from_other_repo)

Get Errors Count for the given scope, Repo and Branch

### Example
```python
from __future__ import print_function
import time
import harness_python_sdk
from harness_python_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: x-api-key
configuration = harness_python_sdk.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = harness_python_sdk.GitSyncErrorsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
search_term = 'search_term_example' # str | Search Term. (optional)
branch = 'branch_example' # str | Name of the branch. (optional)
repo_identifier = 'repo_identifier_example' # str | Git Sync Config Id. (optional)
get_default_from_other_repo = true # bool | if true, return all the default entities (optional)

try:
    # Get Errors Count for the given scope, Repo and Branch
    api_response = api_instance.get_git_sync_errors_count(account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, search_term=search_term, branch=branch, repo_identifier=repo_identifier, get_default_from_other_repo=get_default_from_other_repo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GitSyncErrorsApi->get_git_sync_errors_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **search_term** | **str**| Search Term. | [optional] 
 **branch** | **str**| Name of the branch. | [optional] 
 **repo_identifier** | **str**| Git Sync Config Id. | [optional] 
 **get_default_from_other_repo** | **bool**| if true, return all the default entities | [optional] 

### Return type

[**ResponseDTOGitSyncErrorCount**](ResponseDTOGitSyncErrorCount.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, text/yaml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_git_sync_errors**
> ResponseDTOPageResponseGitSyncError list_git_sync_errors(account_identifier, page_index=page_index, page_size=page_size, sort_orders=sort_orders, page_token=page_token, org_identifier=org_identifier, project_identifier=project_identifier, search_term=search_term, branch=branch, repo_identifier=repo_identifier, get_default_from_other_repo=get_default_from_other_repo, git_to_harness=git_to_harness)

Lists Git to Harness Errors by file or connectivity errors for the given scope, Repo and Branch

### Example
```python
from __future__ import print_function
import time
import harness_python_sdk
from harness_python_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: x-api-key
configuration = harness_python_sdk.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = harness_python_sdk.GitSyncErrorsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
page_index = 0 # int | Page Index of the results to fetch.Default Value: 0 (optional) (default to 0)
page_size = 50 # int | Results per page(max 100)Default Value: 50 (optional) (default to 50)
sort_orders = [harness_python_sdk.SortOrder()] # list[SortOrder] | Sort criteria for the elements. (optional)
page_token = 'page_token_example' # str | Page Token of the next results to fetch.Default Value: '' (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
search_term = 'search_term_example' # str | Search Term. (optional)
branch = 'branch_example' # str | Name of the branch. (optional)
repo_identifier = 'repo_identifier_example' # str | Git Sync Config Id. (optional)
get_default_from_other_repo = true # bool | if true, return all the default entities (optional)
git_to_harness = true # bool | This specifies which errors to show - (Git to Harness or Connectivity), Put true to show Git to Harness Errors (optional) (default to true)

try:
    # Lists Git to Harness Errors by file or connectivity errors for the given scope, Repo and Branch
    api_response = api_instance.list_git_sync_errors(account_identifier, page_index=page_index, page_size=page_size, sort_orders=sort_orders, page_token=page_token, org_identifier=org_identifier, project_identifier=project_identifier, search_term=search_term, branch=branch, repo_identifier=repo_identifier, get_default_from_other_repo=get_default_from_other_repo, git_to_harness=git_to_harness)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GitSyncErrorsApi->list_git_sync_errors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **page_index** | **int**| Page Index of the results to fetch.Default Value: 0 | [optional] [default to 0]
 **page_size** | **int**| Results per page(max 100)Default Value: 50 | [optional] [default to 50]
 **sort_orders** | [**list[SortOrder]**](SortOrder.md)| Sort criteria for the elements. | [optional] 
 **page_token** | **str**| Page Token of the next results to fetch.Default Value: &#x27;&#x27; | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **search_term** | **str**| Search Term. | [optional] 
 **branch** | **str**| Name of the branch. | [optional] 
 **repo_identifier** | **str**| Git Sync Config Id. | [optional] 
 **get_default_from_other_repo** | **bool**| if true, return all the default entities | [optional] 
 **git_to_harness** | **bool**| This specifies which errors to show - (Git to Harness or Connectivity), Put true to show Git to Harness Errors | [optional] [default to true]

### Return type

[**ResponseDTOPageResponseGitSyncError**](ResponseDTOPageResponseGitSyncError.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, text/yaml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_git_to_harness_error_for_commit**
> ResponseDTOPageResponseGitSyncError list_git_to_harness_error_for_commit(account_identifier, commit_id, page_index=page_index, page_size=page_size, sort_orders=sort_orders, page_token=page_token, org_identifier=org_identifier, project_identifier=project_identifier, branch=branch, repo_identifier=repo_identifier, get_default_from_other_repo=get_default_from_other_repo)

Lists Git to Harness Errors for the given Commit Id

### Example
```python
from __future__ import print_function
import time
import harness_python_sdk
from harness_python_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: x-api-key
configuration = harness_python_sdk.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = harness_python_sdk.GitSyncErrorsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
commit_id = 'commit_id_example' # str | Commit Id
page_index = 0 # int | Page Index of the results to fetch.Default Value: 0 (optional) (default to 0)
page_size = 50 # int | Results per page(max 100)Default Value: 50 (optional) (default to 50)
sort_orders = [harness_python_sdk.SortOrder()] # list[SortOrder] | Sort criteria for the elements. (optional)
page_token = 'page_token_example' # str | Page Token of the next results to fetch.Default Value: '' (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
branch = 'branch_example' # str | Name of the branch. (optional)
repo_identifier = 'repo_identifier_example' # str | Git Sync Config Id. (optional)
get_default_from_other_repo = true # bool | if true, return all the default entities (optional)

try:
    # Lists Git to Harness Errors for the given Commit Id
    api_response = api_instance.list_git_to_harness_error_for_commit(account_identifier, commit_id, page_index=page_index, page_size=page_size, sort_orders=sort_orders, page_token=page_token, org_identifier=org_identifier, project_identifier=project_identifier, branch=branch, repo_identifier=repo_identifier, get_default_from_other_repo=get_default_from_other_repo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GitSyncErrorsApi->list_git_to_harness_error_for_commit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **commit_id** | **str**| Commit Id | 
 **page_index** | **int**| Page Index of the results to fetch.Default Value: 0 | [optional] [default to 0]
 **page_size** | **int**| Results per page(max 100)Default Value: 50 | [optional] [default to 50]
 **sort_orders** | [**list[SortOrder]**](SortOrder.md)| Sort criteria for the elements. | [optional] 
 **page_token** | **str**| Page Token of the next results to fetch.Default Value: &#x27;&#x27; | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **branch** | **str**| Name of the branch. | [optional] 
 **repo_identifier** | **str**| Git Sync Config Id. | [optional] 
 **get_default_from_other_repo** | **bool**| if true, return all the default entities | [optional] 

### Return type

[**ResponseDTOPageResponseGitSyncError**](ResponseDTOPageResponseGitSyncError.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, text/yaml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_git_to_harness_errors_grouped_by_commits**
> ResponseDTOPageResponseGitSyncErrorAggregateByCommit list_git_to_harness_errors_grouped_by_commits(account_identifier, page_index=page_index, page_size=page_size, sort_orders=sort_orders, page_token=page_token, org_identifier=org_identifier, project_identifier=project_identifier, search_term=search_term, branch=branch, repo_identifier=repo_identifier, get_default_from_other_repo=get_default_from_other_repo, number_of_errors_in_summary=number_of_errors_in_summary)

Lists Git to Harness Errors grouped by Commits for the given scope, Repo and Branch

### Example
```python
from __future__ import print_function
import time
import harness_python_sdk
from harness_python_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: x-api-key
configuration = harness_python_sdk.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = harness_python_sdk.GitSyncErrorsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
page_index = 0 # int | Page Index of the results to fetch.Default Value: 0 (optional) (default to 0)
page_size = 50 # int | Results per page(max 100)Default Value: 50 (optional) (default to 50)
sort_orders = [harness_python_sdk.SortOrder()] # list[SortOrder] | Sort criteria for the elements. (optional)
page_token = 'page_token_example' # str | Page Token of the next results to fetch.Default Value: '' (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
search_term = 'search_term_example' # str | Search Term. (optional)
branch = 'branch_example' # str | Name of the branch. (optional)
repo_identifier = 'repo_identifier_example' # str | Git Sync Config Id. (optional)
get_default_from_other_repo = true # bool | if true, return all the default entities (optional)
number_of_errors_in_summary = 5 # int | Number of errors that will be displayed in the summary (optional) (default to 5)

try:
    # Lists Git to Harness Errors grouped by Commits for the given scope, Repo and Branch
    api_response = api_instance.list_git_to_harness_errors_grouped_by_commits(account_identifier, page_index=page_index, page_size=page_size, sort_orders=sort_orders, page_token=page_token, org_identifier=org_identifier, project_identifier=project_identifier, search_term=search_term, branch=branch, repo_identifier=repo_identifier, get_default_from_other_repo=get_default_from_other_repo, number_of_errors_in_summary=number_of_errors_in_summary)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GitSyncErrorsApi->list_git_to_harness_errors_grouped_by_commits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **page_index** | **int**| Page Index of the results to fetch.Default Value: 0 | [optional] [default to 0]
 **page_size** | **int**| Results per page(max 100)Default Value: 50 | [optional] [default to 50]
 **sort_orders** | [**list[SortOrder]**](SortOrder.md)| Sort criteria for the elements. | [optional] 
 **page_token** | **str**| Page Token of the next results to fetch.Default Value: &#x27;&#x27; | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **search_term** | **str**| Search Term. | [optional] 
 **branch** | **str**| Name of the branch. | [optional] 
 **repo_identifier** | **str**| Git Sync Config Id. | [optional] 
 **get_default_from_other_repo** | **bool**| if true, return all the default entities | [optional] 
 **number_of_errors_in_summary** | **int**| Number of errors that will be displayed in the summary | [optional] [default to 5]

### Return type

[**ResponseDTOPageResponseGitSyncErrorAggregateByCommit**](ResponseDTOPageResponseGitSyncErrorAggregateByCommit.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, text/yaml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

