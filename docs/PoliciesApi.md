# harness_python_sdk.PoliciesApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**policies_create**](PoliciesApi.md#policies_create) | **POST** /pm/api/v1/policies | 
[**policies_delete**](PoliciesApi.md#policies_delete) | **DELETE** /pm/api/v1/policies/{identifier} | 
[**policies_find**](PoliciesApi.md#policies_find) | **GET** /pm/api/v1/policies/{identifier} | 
[**policies_list**](PoliciesApi.md#policies_list) | **GET** /pm/api/v1/policies | 
[**policies_update**](PoliciesApi.md#policies_update) | **PATCH** /pm/api/v1/policies/{identifier} | 

# **policies_create**
> PolicyManagementPolicy policies_create(body, x_api_key=x_api_key, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, git_commit_msg=git_commit_msg, git_import=git_import, git_branch=git_branch, git_is_new_branch=git_is_new_branch, git_base_branch=git_base_branch)



Create a policy

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
api_instance = harness_python_sdk.PoliciesApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.CreateRequestBody() # CreateRequestBody | 
x_api_key = 'x_api_key_example' # str | Harness PAT key used to perform authorization (optional)
account_identifier = '' # str | Harness account ID (optional)
org_identifier = '' # str | Harness organization ID (optional)
project_identifier = '' # str | Harness project ID (optional)
git_commit_msg = 'git_commit_msg_example' # str | The commit message used in git when creating the policy (optional)
git_import = true # bool | A flag to determine if the api should try and import and existing policy from git (optional)
git_branch = 'git_branch_example' # str | The git branch the policy will be created in (optional)
git_is_new_branch = true # bool | A flag to determine if the api should try and commit to a new branch (optional)
git_base_branch = 'git_base_branch_example' # str | If committing to a new branch, git_base_branch tells the api which branch to base the new branch from (optional)

try:
    api_response = api_instance.policies_create(body, x_api_key=x_api_key, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, git_commit_msg=git_commit_msg, git_import=git_import, git_branch=git_branch, git_is_new_branch=git_is_new_branch, git_base_branch=git_base_branch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoliciesApi->policies_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateRequestBody**](CreateRequestBody.md)|  | 
 **x_api_key** | **str**| Harness PAT key used to perform authorization | [optional] 
 **account_identifier** | **str**| Harness account ID | [optional] 
 **org_identifier** | **str**| Harness organization ID | [optional] 
 **project_identifier** | **str**| Harness project ID | [optional] 
 **git_commit_msg** | **str**| The commit message used in git when creating the policy | [optional] 
 **git_import** | **bool**| A flag to determine if the api should try and import and existing policy from git | [optional] 
 **git_branch** | **str**| The git branch the policy will be created in | [optional] 
 **git_is_new_branch** | **bool**| A flag to determine if the api should try and commit to a new branch | [optional] 
 **git_base_branch** | **str**| If committing to a new branch, git_base_branch tells the api which branch to base the new branch from | [optional] 

### Return type

[**PolicyManagementPolicy**](PolicyManagementPolicy.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/vnd.goa.error

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **policies_delete**
> policies_delete(identifier, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, x_api_key=x_api_key)



Delete a policy by identifier

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
api_instance = harness_python_sdk.PoliciesApi(harness_python_sdk.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of the policy
account_identifier = '' # str | Harness account ID (optional)
org_identifier = '' # str | Harness organization ID (optional)
project_identifier = '' # str | Harness project ID (optional)
x_api_key = 'x_api_key_example' # str | Harness PAT key used to perform authorization (optional)

try:
    api_instance.policies_delete(identifier, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, x_api_key=x_api_key)
except ApiException as e:
    print("Exception when calling PoliciesApi->policies_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of the policy | 
 **account_identifier** | **str**| Harness account ID | [optional] 
 **org_identifier** | **str**| Harness organization ID | [optional] 
 **project_identifier** | **str**| Harness project ID | [optional] 
 **x_api_key** | **str**| Harness PAT key used to perform authorization | [optional] 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.goa.error

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **policies_find**
> PolicyManagementPolicy policies_find(identifier, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, git_branch=git_branch, show_summary=show_summary, x_api_key=x_api_key)



Find a policy by identifier

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
api_instance = harness_python_sdk.PoliciesApi(harness_python_sdk.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of the policy to retrieve
account_identifier = '' # str | Harness account ID (optional)
org_identifier = '' # str | Harness organization ID (optional)
project_identifier = '' # str | Harness project ID (optional)
git_branch = 'git_branch_example' # str | The git branch the policy resides in (optional)
show_summary = true # bool | Setting to true returns the metadata about the        requested policy including the information held about the status of this policy in the default branch.        git_branch is ignored as no git operation takes place. (optional)
x_api_key = 'x_api_key_example' # str | Harness PAT key used to perform authorization (optional)

try:
    api_response = api_instance.policies_find(identifier, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, git_branch=git_branch, show_summary=show_summary, x_api_key=x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoliciesApi->policies_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of the policy to retrieve | 
 **account_identifier** | **str**| Harness account ID | [optional] 
 **org_identifier** | **str**| Harness organization ID | [optional] 
 **project_identifier** | **str**| Harness project ID | [optional] 
 **git_branch** | **str**| The git branch the policy resides in | [optional] 
 **show_summary** | **bool**| Setting to true returns the metadata about the        requested policy including the information held about the status of this policy in the default branch.        git_branch is ignored as no git operation takes place. | [optional] 
 **x_api_key** | **str**| Harness PAT key used to perform authorization | [optional] 

### Return type

[**PolicyManagementPolicy**](PolicyManagementPolicy.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.goa.error

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **policies_list**
> list[PolicyManagementPolicy] policies_list(account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, per_page=per_page, page=page, search_term=search_term, sort=sort, x_api_key=x_api_key)



List all policies

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
api_instance = harness_python_sdk.PoliciesApi(harness_python_sdk.ApiClient(configuration))
account_identifier = '' # str | Harness account ID (optional)
org_identifier = '' # str | Harness organization ID (optional)
project_identifier = '' # str | Harness project ID (optional)
per_page = 50 # int | Number of results per page (optional) (default to 50)
page = 0 # int | Page number (starting from 0) (optional) (default to 0)
search_term = '' # str | Filter results by partial name match (optional)
sort = 'name,ASC' # str | Sort order for results (optional) (default to name,ASC)
x_api_key = 'x_api_key_example' # str | Harness PAT key used to perform authorization (optional)

try:
    api_response = api_instance.policies_list(account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, per_page=per_page, page=page, search_term=search_term, sort=sort, x_api_key=x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoliciesApi->policies_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Harness account ID | [optional] 
 **org_identifier** | **str**| Harness organization ID | [optional] 
 **project_identifier** | **str**| Harness project ID | [optional] 
 **per_page** | **int**| Number of results per page | [optional] [default to 50]
 **page** | **int**| Page number (starting from 0) | [optional] [default to 0]
 **search_term** | **str**| Filter results by partial name match | [optional] 
 **sort** | **str**| Sort order for results | [optional] [default to name,ASC]
 **x_api_key** | **str**| Harness PAT key used to perform authorization | [optional] 

### Return type

[**list[PolicyManagementPolicy]**](PolicyManagementPolicy.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.goa.error

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **policies_update**
> policies_update(body, identifier, x_api_key=x_api_key, git_commit_msg=git_commit_msg, git_is_new_branch=git_is_new_branch, git_base_branch=git_base_branch, git_branch=git_branch, git_commit_sha=git_commit_sha, git_file_id=git_file_id, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)



Update a policy by identifier

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
api_instance = harness_python_sdk.PoliciesApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.UpdateRequestBody() # UpdateRequestBody | 
identifier = 'identifier_example' # str | Identifier of the policy
x_api_key = 'x_api_key_example' # str | Harness PAT key used to perform authorization (optional)
git_commit_msg = 'git_commit_msg_example' # str | The commit message used in git when creating the policy (optional)
git_is_new_branch = true # bool | A flag to determine if the api should try and commit to a new branch (optional)
git_base_branch = 'git_base_branch_example' # str | If committing to a new branch, git_base_branch tells the api which branch to base the new branch from (optional)
git_branch = 'git_branch_example' # str | The git branch the policy resides in (optional)
git_commit_sha = 'git_commit_sha_example' # str | The existing commit sha of the file being updated (optional)
git_file_id = 'git_file_id_example' # str | The existing file id of the file being updated, not required for bitbucket files (optional)
account_identifier = '' # str | Harness account ID (optional)
org_identifier = '' # str | Harness organization ID (optional)
project_identifier = '' # str | Harness project ID (optional)

try:
    api_instance.policies_update(body, identifier, x_api_key=x_api_key, git_commit_msg=git_commit_msg, git_is_new_branch=git_is_new_branch, git_base_branch=git_base_branch, git_branch=git_branch, git_commit_sha=git_commit_sha, git_file_id=git_file_id, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
except ApiException as e:
    print("Exception when calling PoliciesApi->policies_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateRequestBody**](UpdateRequestBody.md)|  | 
 **identifier** | **str**| Identifier of the policy | 
 **x_api_key** | **str**| Harness PAT key used to perform authorization | [optional] 
 **git_commit_msg** | **str**| The commit message used in git when creating the policy | [optional] 
 **git_is_new_branch** | **bool**| A flag to determine if the api should try and commit to a new branch | [optional] 
 **git_base_branch** | **str**| If committing to a new branch, git_base_branch tells the api which branch to base the new branch from | [optional] 
 **git_branch** | **str**| The git branch the policy resides in | [optional] 
 **git_commit_sha** | **str**| The existing commit sha of the file being updated | [optional] 
 **git_file_id** | **str**| The existing file id of the file being updated, not required for bitbucket files | [optional] 
 **account_identifier** | **str**| Harness account ID | [optional] 
 **org_identifier** | **str**| Harness organization ID | [optional] 
 **project_identifier** | **str**| Harness project ID | [optional] 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/vnd.goa.error

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

