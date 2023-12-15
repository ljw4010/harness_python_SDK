# harness_python_sdk.EnvironmentGroupApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_environment_group**](EnvironmentGroupApi.md#delete_environment_group) | **DELETE** /ng/api/environmentGroup/{envGroupIdentifier} | Delete en Environment Group by Identifier
[**get_environment_group**](EnvironmentGroupApi.md#get_environment_group) | **GET** /ng/api/environmentGroup/{envGroupIdentifier} | Gets an Environment Group by identifier
[**get_environment_group_list**](EnvironmentGroupApi.md#get_environment_group_list) | **POST** /ng/api/environmentGroup/list | Gets Environment Group list
[**post_environment_group**](EnvironmentGroupApi.md#post_environment_group) | **POST** /ng/api/environmentGroup | Create an Environment Group
[**update_environment_group**](EnvironmentGroupApi.md#update_environment_group) | **PUT** /ng/api/environmentGroup/{envGroupIdentifier} | Update an Environment Group by Identifier

# **delete_environment_group**
> ResponseDTOEnvironmentGroupDelete delete_environment_group(env_group_identifier, account_identifier, if_match=if_match, org_identifier=org_identifier, project_identifier=project_identifier, branch=branch, repo_identifier=repo_identifier, root_folder=root_folder, file_path=file_path, commit_msg=commit_msg, last_object_id=last_object_id, force_delete=force_delete)

Delete en Environment Group by Identifier

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
api_instance = harness_python_sdk.EnvironmentGroupApi(harness_python_sdk.ApiClient(configuration))
env_group_identifier = 'env_group_identifier_example' # str | Environment Group Identifier for the entity
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
if_match = 'if_match_example' # str |  (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
branch = 'branch_example' # str | Name of the branch. (optional)
repo_identifier = 'repo_identifier_example' # str | Git Sync Config Id. (optional)
root_folder = 'root_folder_example' # str | Path to the root folder of the Entity. (optional)
file_path = 'file_path_example' # str | File Path of the Entity. (optional)
commit_msg = 'commit_msg_example' # str | Commit Message to use for the merge commit. (optional)
last_object_id = 'last_object_id_example' # str | Last Object Id (optional)
force_delete = false # bool | If true, the Entity will be forced delete, without checking any references/usages (optional) (default to false)

try:
    # Delete en Environment Group by Identifier
    api_response = api_instance.delete_environment_group(env_group_identifier, account_identifier, if_match=if_match, org_identifier=org_identifier, project_identifier=project_identifier, branch=branch, repo_identifier=repo_identifier, root_folder=root_folder, file_path=file_path, commit_msg=commit_msg, last_object_id=last_object_id, force_delete=force_delete)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentGroupApi->delete_environment_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **env_group_identifier** | **str**| Environment Group Identifier for the entity | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **if_match** | **str**|  | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **branch** | **str**| Name of the branch. | [optional] 
 **repo_identifier** | **str**| Git Sync Config Id. | [optional] 
 **root_folder** | **str**| Path to the root folder of the Entity. | [optional] 
 **file_path** | **str**| File Path of the Entity. | [optional] 
 **commit_msg** | **str**| Commit Message to use for the merge commit. | [optional] 
 **last_object_id** | **str**| Last Object Id | [optional] 
 **force_delete** | **bool**| If true, the Entity will be forced delete, without checking any references/usages | [optional] [default to false]

### Return type

[**ResponseDTOEnvironmentGroupDelete**](ResponseDTOEnvironmentGroupDelete.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_environment_group**
> ResponseDTOEnvironmentGroup get_environment_group(env_group_identifier, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, deleted=deleted, branch=branch, repo_identifier=repo_identifier, get_default_from_other_repo=get_default_from_other_repo)

Gets an Environment Group by identifier

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
api_instance = harness_python_sdk.EnvironmentGroupApi(harness_python_sdk.ApiClient(configuration))
env_group_identifier = 'env_group_identifier_example' # str | Environment Group Identifier for the entity
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
deleted = false # bool | Specify whether environment group is deleted or not (optional) (default to false)
branch = 'branch_example' # str | Name of the branch. (optional)
repo_identifier = 'repo_identifier_example' # str | Git Sync Config Id. (optional)
get_default_from_other_repo = true # bool | if true, return all the default entities (optional)

try:
    # Gets an Environment Group by identifier
    api_response = api_instance.get_environment_group(env_group_identifier, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, deleted=deleted, branch=branch, repo_identifier=repo_identifier, get_default_from_other_repo=get_default_from_other_repo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentGroupApi->get_environment_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **env_group_identifier** | **str**| Environment Group Identifier for the entity | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **deleted** | **bool**| Specify whether environment group is deleted or not | [optional] [default to false]
 **branch** | **str**| Name of the branch. | [optional] 
 **repo_identifier** | **str**| Git Sync Config Id. | [optional] 
 **get_default_from_other_repo** | **bool**| if true, return all the default entities | [optional] 

### Return type

[**ResponseDTOEnvironmentGroup**](ResponseDTOEnvironmentGroup.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_environment_group_list**
> ResponseDTOPageResponseEnvironmentGroup get_environment_group_list(account_identifier, body=body, org_identifier=org_identifier, project_identifier=project_identifier, env_group_identifiers=env_group_identifiers, search_term=search_term, page=page, size=size, sort=sort, filter_identifier=filter_identifier, branch=branch, repo_identifier=repo_identifier, get_default_from_other_repo=get_default_from_other_repo, include_all_env_groups_accessible_at_scope=include_all_env_groups_accessible_at_scope)

Gets Environment Group list

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
api_instance = harness_python_sdk.EnvironmentGroupApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
body = harness_python_sdk.FilterProperties() # FilterProperties | This is the body for the filter properties for listing Environment Groups (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
env_group_identifiers = ['env_group_identifiers_example'] # list[str] |  (optional)
search_term = 'search_term_example' # str | The word to be searched and included in the list response (optional)
page = 0 # int | Page Index of the results to fetch.Default Value: 0 (optional) (default to 0)
size = 25 # int | Results per page (optional) (default to 25)
sort = ['sort_example'] # list[str] | Sort criteria for the elements. (optional)
filter_identifier = 'filter_identifier_example' # str | Filter identifier (optional)
branch = 'branch_example' # str | Name of the branch. (optional)
repo_identifier = 'repo_identifier_example' # str | Git Sync Config Id. (optional)
get_default_from_other_repo = true # bool | if true, return all the default entities (optional)
include_all_env_groups_accessible_at_scope = false # bool | Specify true if all accessible environment groups are to be included (optional) (default to false)

try:
    # Gets Environment Group list
    api_response = api_instance.get_environment_group_list(account_identifier, body=body, org_identifier=org_identifier, project_identifier=project_identifier, env_group_identifiers=env_group_identifiers, search_term=search_term, page=page, size=size, sort=sort, filter_identifier=filter_identifier, branch=branch, repo_identifier=repo_identifier, get_default_from_other_repo=get_default_from_other_repo, include_all_env_groups_accessible_at_scope=include_all_env_groups_accessible_at_scope)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentGroupApi->get_environment_group_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **body** | [**FilterProperties**](FilterProperties.md)| This is the body for the filter properties for listing Environment Groups | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **env_group_identifiers** | [**list[str]**](str.md)|  | [optional] 
 **search_term** | **str**| The word to be searched and included in the list response | [optional] 
 **page** | **int**| Page Index of the results to fetch.Default Value: 0 | [optional] [default to 0]
 **size** | **int**| Results per page | [optional] [default to 25]
 **sort** | [**list[str]**](str.md)| Sort criteria for the elements. | [optional] 
 **filter_identifier** | **str**| Filter identifier | [optional] 
 **branch** | **str**| Name of the branch. | [optional] 
 **repo_identifier** | **str**| Git Sync Config Id. | [optional] 
 **get_default_from_other_repo** | **bool**| if true, return all the default entities | [optional] 
 **include_all_env_groups_accessible_at_scope** | **bool**| Specify true if all accessible environment groups are to be included | [optional] [default to false]

### Return type

[**ResponseDTOPageResponseEnvironmentGroup**](ResponseDTOPageResponseEnvironmentGroup.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_environment_group**
> ResponseDTOEnvironmentGroup post_environment_group(body, account_identifier, branch=branch, repo_identifier=repo_identifier, get_default_from_other_repo=get_default_from_other_repo)

Create an Environment Group

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
api_instance = harness_python_sdk.EnvironmentGroupApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.EnvironmentGroupRequest() # EnvironmentGroupRequest | Details of the Environment Group to be created
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
branch = 'branch_example' # str | Name of the branch. (optional)
repo_identifier = 'repo_identifier_example' # str | Git Sync Config Id. (optional)
get_default_from_other_repo = true # bool | if true, return all the default entities (optional)

try:
    # Create an Environment Group
    api_response = api_instance.post_environment_group(body, account_identifier, branch=branch, repo_identifier=repo_identifier, get_default_from_other_repo=get_default_from_other_repo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentGroupApi->post_environment_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EnvironmentGroupRequest**](EnvironmentGroupRequest.md)| Details of the Environment Group to be created | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **branch** | **str**| Name of the branch. | [optional] 
 **repo_identifier** | **str**| Git Sync Config Id. | [optional] 
 **get_default_from_other_repo** | **bool**| if true, return all the default entities | [optional] 

### Return type

[**ResponseDTOEnvironmentGroup**](ResponseDTOEnvironmentGroup.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_environment_group**
> ResponseDTOEnvironmentGroup update_environment_group(body, account_identifier, env_group_identifier, if_match=if_match, branch=branch, repo_identifier=repo_identifier, root_folder=root_folder, file_path=file_path, commit_msg=commit_msg, last_object_id=last_object_id, resolved_conflict_commit_id=resolved_conflict_commit_id, base_branch=base_branch, connector_ref=connector_ref, is_new_branch=is_new_branch)

Update an Environment Group by Identifier

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
api_instance = harness_python_sdk.EnvironmentGroupApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.EnvironmentGroupRequest() # EnvironmentGroupRequest | Details of the Environment Group to be updated
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
env_group_identifier = 'env_group_identifier_example' # str | Environment Group Identifier for the entity
if_match = 'if_match_example' # str |  (optional)
branch = 'branch_example' # str | Name of the branch. (optional)
repo_identifier = 'repo_identifier_example' # str | Git Sync Config Id. (optional)
root_folder = 'root_folder_example' # str | Path to the root folder of the Entity. (optional)
file_path = 'file_path_example' # str | Path to the root folder of the Entity. (optional)
commit_msg = 'commit_msg_example' # str | Commit Message to use for the merge commit. (optional)
last_object_id = 'last_object_id_example' # str | Its required field during update call request. It can be fetched from the response of GET API call for the entity (optional)
resolved_conflict_commit_id = 'resolved_conflict_commit_id_example' # str | If the entity is git-synced, this parameter represents the commit id against which file conflicts are resolved (optional)
base_branch = 'base_branch_example' # str | Name of the default branch. (optional)
connector_ref = 'connector_ref_example' # str | Identifier of Connector needed for CRUD operations on the respective Entity (optional)
is_new_branch = false # bool | Checks the new branch (optional) (default to false)

try:
    # Update an Environment Group by Identifier
    api_response = api_instance.update_environment_group(body, account_identifier, env_group_identifier, if_match=if_match, branch=branch, repo_identifier=repo_identifier, root_folder=root_folder, file_path=file_path, commit_msg=commit_msg, last_object_id=last_object_id, resolved_conflict_commit_id=resolved_conflict_commit_id, base_branch=base_branch, connector_ref=connector_ref, is_new_branch=is_new_branch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentGroupApi->update_environment_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EnvironmentGroupRequest**](EnvironmentGroupRequest.md)| Details of the Environment Group to be updated | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **env_group_identifier** | **str**| Environment Group Identifier for the entity | 
 **if_match** | **str**|  | [optional] 
 **branch** | **str**| Name of the branch. | [optional] 
 **repo_identifier** | **str**| Git Sync Config Id. | [optional] 
 **root_folder** | **str**| Path to the root folder of the Entity. | [optional] 
 **file_path** | **str**| Path to the root folder of the Entity. | [optional] 
 **commit_msg** | **str**| Commit Message to use for the merge commit. | [optional] 
 **last_object_id** | **str**| Its required field during update call request. It can be fetched from the response of GET API call for the entity | [optional] 
 **resolved_conflict_commit_id** | **str**| If the entity is git-synced, this parameter represents the commit id against which file conflicts are resolved | [optional] 
 **base_branch** | **str**| Name of the default branch. | [optional] 
 **connector_ref** | **str**| Identifier of Connector needed for CRUD operations on the respective Entity | [optional] 
 **is_new_branch** | **bool**| Checks the new branch | [optional] [default to false]

### Return type

[**ResponseDTOEnvironmentGroup**](ResponseDTOEnvironmentGroup.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

