# harness_python_sdk.GitBranchesApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_list_of_branches_with_status**](GitBranchesApi.md#get_list_of_branches_with_status) | **GET** /ng/api/git-sync-branch/listBranchesWithStatus | Lists branches with their status(Synced, Unsynced) by Git Sync Config Id for the given scope
[**sync_git_branch**](GitBranchesApi.md#sync_git_branch) | **POST** /ng/api/git-sync-branch/sync | Sync the content of new Git Branch into harness with Git Sync Config Id

# **get_list_of_branches_with_status**
> ResponseDTOGitBranchList get_list_of_branches_with_status(yaml_git_config_identifier, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, page=page, size=size, search_term=search_term, branch_sync_status=branch_sync_status)

Lists branches with their status(Synced, Unsynced) by Git Sync Config Id for the given scope

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
api_instance = harness_python_sdk.GitBranchesApi(harness_python_sdk.ApiClient(configuration))
yaml_git_config_identifier = 'yaml_git_config_identifier_example' # str | Git Sync Config Id.
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
page = 0 # int | Page Index of the results to fetch.Default Value: 0 (optional) (default to 0)
size = 56 # int | Results per page (optional)
search_term = '' # str | Search Term. (optional)
branch_sync_status = 'branch_sync_status_example' # str | Used to filter out Synced and Unsynced branches (optional)

try:
    # Lists branches with their status(Synced, Unsynced) by Git Sync Config Id for the given scope
    api_response = api_instance.get_list_of_branches_with_status(yaml_git_config_identifier, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, page=page, size=size, search_term=search_term, branch_sync_status=branch_sync_status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GitBranchesApi->get_list_of_branches_with_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **yaml_git_config_identifier** | **str**| Git Sync Config Id. | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **page** | **int**| Page Index of the results to fetch.Default Value: 0 | [optional] [default to 0]
 **size** | **int**| Results per page | [optional] 
 **search_term** | **str**| Search Term. | [optional] 
 **branch_sync_status** | **str**| Used to filter out Synced and Unsynced branches | [optional] 

### Return type

[**ResponseDTOGitBranchList**](ResponseDTOGitBranchList.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, text/yaml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_git_branch**
> ResponseDTOBoolean sync_git_branch(repo_identifier, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, branch=branch)

Sync the content of new Git Branch into harness with Git Sync Config Id

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
api_instance = harness_python_sdk.GitBranchesApi(harness_python_sdk.ApiClient(configuration))
repo_identifier = 'repo_identifier_example' # str | Git Sync Config Id.
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
branch = 'branch_example' # str | Name of the branch. (optional)

try:
    # Sync the content of new Git Branch into harness with Git Sync Config Id
    api_response = api_instance.sync_git_branch(repo_identifier, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, branch=branch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GitBranchesApi->sync_git_branch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_identifier** | **str**| Git Sync Config Id. | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **branch** | **str**| Name of the branch. | [optional] 

### Return type

[**ResponseDTOBoolean**](ResponseDTOBoolean.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, text/yaml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

