# harness_python_sdk.PipelineInputSetApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_input_set**](PipelineInputSetApi.md#delete_input_set) | **DELETE** /pipeline/api/inputSets/{inputSetIdentifier} | Delete an Input Set
[**get_input_set**](PipelineInputSetApi.md#get_input_set) | **GET** /pipeline/api/inputSets/{inputSetIdentifier} | Fetch an Input Set
[**get_overlay_input_set**](PipelineInputSetApi.md#get_overlay_input_set) | **GET** /pipeline/api/inputSets/overlay/{inputSetIdentifier} | Gets an Overlay Input Set by identifier
[**list_input_set**](PipelineInputSetApi.md#list_input_set) | **GET** /pipeline/api/inputSets | List Input Sets
[**post_input_set**](PipelineInputSetApi.md#post_input_set) | **POST** /pipeline/api/inputSets | Create an Input Set
[**post_overlay_input_set**](PipelineInputSetApi.md#post_overlay_input_set) | **POST** /pipeline/api/inputSets/overlay | Create an Overlay Input Set for a pipeline
[**put_input_set**](PipelineInputSetApi.md#put_input_set) | **PUT** /pipeline/api/inputSets/{inputSetIdentifier} | Update an Input Set
[**put_overlay_input_set**](PipelineInputSetApi.md#put_overlay_input_set) | **PUT** /pipeline/api/inputSets/overlay/{inputSetIdentifier} | Update an Overlay Input Set for a pipeline
[**runtime_input_template**](PipelineInputSetApi.md#runtime_input_template) | **POST** /pipeline/api/inputSets/template | Fetch Runtime Input Template
[**update_input_set_git_details**](PipelineInputSetApi.md#update_input_set_git_details) | **PUT** /pipeline/api/inputSets/{inputSetIdentifier}/update-git-metadata | Update git-metadata in remote input-set

# **delete_input_set**
> ResponseDTOBoolean delete_input_set(input_set_identifier, account_identifier, org_identifier, project_identifier, pipeline_identifier, if_match=if_match, branch=branch, repo_identifier=repo_identifier, root_folder=root_folder, file_path=file_path, commit_msg=commit_msg, last_object_id=last_object_id)

Delete an Input Set

Deletes the Input Set by Identifier

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
api_instance = harness_python_sdk.PipelineInputSetApi(harness_python_sdk.ApiClient(configuration))
input_set_identifier = 'input_set_identifier_example' # str | Identifier of the Input Set that should be deleted.
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
pipeline_identifier = 'pipeline_identifier_example' # str | Pipeline Identifier for the entity.
if_match = 'if_match_example' # str | Version of Entity to match (optional)
branch = 'branch_example' # str | Name of the branch. (optional)
repo_identifier = 'repo_identifier_example' # str | Git Sync Config Id. (optional)
root_folder = 'root_folder_example' # str | Path to the root folder of the Entity. (optional)
file_path = 'file_path_example' # str | File Path of the Entity. (optional)
commit_msg = 'commit_msg_example' # str | Commit Message to use for the merge commit. (optional)
last_object_id = 'last_object_id_example' # str | Last Object Id (optional)

try:
    # Delete an Input Set
    api_response = api_instance.delete_input_set(input_set_identifier, account_identifier, org_identifier, project_identifier, pipeline_identifier, if_match=if_match, branch=branch, repo_identifier=repo_identifier, root_folder=root_folder, file_path=file_path, commit_msg=commit_msg, last_object_id=last_object_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineInputSetApi->delete_input_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_set_identifier** | **str**| Identifier of the Input Set that should be deleted. | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **pipeline_identifier** | **str**| Pipeline Identifier for the entity. | 
 **if_match** | **str**| Version of Entity to match | [optional] 
 **branch** | **str**| Name of the branch. | [optional] 
 **repo_identifier** | **str**| Git Sync Config Id. | [optional] 
 **root_folder** | **str**| Path to the root folder of the Entity. | [optional] 
 **file_path** | **str**| File Path of the Entity. | [optional] 
 **commit_msg** | **str**| Commit Message to use for the merge commit. | [optional] 
 **last_object_id** | **str**| Last Object Id | [optional] 

### Return type

[**ResponseDTOBoolean**](ResponseDTOBoolean.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_input_set**
> ResponseDTOInputSetResponse get_input_set(input_set_identifier, account_identifier, org_identifier, project_identifier, pipeline_identifier, pipeline_branch=pipeline_branch, pipeline_repo_id=pipeline_repo_id, load_from_fallback_branch=load_from_fallback_branch, branch=branch, repo_identifier=repo_identifier, get_default_from_other_repo=get_default_from_other_repo, load_from_cache=load_from_cache)

Fetch an Input Set

Returns Input Set for a Given Identifier (Throws an Error if no Input Set Exists)

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
api_instance = harness_python_sdk.PipelineInputSetApi(harness_python_sdk.ApiClient(configuration))
input_set_identifier = 'input_set_identifier_example' # str | Identifier for the Input Set
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
pipeline_identifier = 'pipeline_identifier_example' # str | Pipeline Identifier for the entity.
pipeline_branch = 'pipeline_branch_example' # str | Github branch of the Pipeline for which the Input Set is to be fetched (optional)
pipeline_repo_id = 'pipeline_repo_id_example' # str | Github Repo identifier of the Pipeline for which the Input Set is to be fetched (optional)
load_from_fallback_branch = false # bool |  (optional) (default to false)
branch = 'branch_example' # str | Name of the branch. (optional)
repo_identifier = 'repo_identifier_example' # str | Git Sync Config Id. (optional)
get_default_from_other_repo = true # bool | if true, return all the default entities (optional)
load_from_cache = 'false' # str |  (optional) (default to false)

try:
    # Fetch an Input Set
    api_response = api_instance.get_input_set(input_set_identifier, account_identifier, org_identifier, project_identifier, pipeline_identifier, pipeline_branch=pipeline_branch, pipeline_repo_id=pipeline_repo_id, load_from_fallback_branch=load_from_fallback_branch, branch=branch, repo_identifier=repo_identifier, get_default_from_other_repo=get_default_from_other_repo, load_from_cache=load_from_cache)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineInputSetApi->get_input_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_set_identifier** | **str**| Identifier for the Input Set | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **pipeline_identifier** | **str**| Pipeline Identifier for the entity. | 
 **pipeline_branch** | **str**| Github branch of the Pipeline for which the Input Set is to be fetched | [optional] 
 **pipeline_repo_id** | **str**| Github Repo identifier of the Pipeline for which the Input Set is to be fetched | [optional] 
 **load_from_fallback_branch** | **bool**|  | [optional] [default to false]
 **branch** | **str**| Name of the branch. | [optional] 
 **repo_identifier** | **str**| Git Sync Config Id. | [optional] 
 **get_default_from_other_repo** | **bool**| if true, return all the default entities | [optional] 
 **load_from_cache** | **str**|  | [optional] [default to false]

### Return type

[**ResponseDTOInputSetResponse**](ResponseDTOInputSetResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_overlay_input_set**
> ResponseDTOOverlayInputSetResponse get_overlay_input_set(input_set_identifier, account_identifier, org_identifier, project_identifier, pipeline_identifier, pipeline_branch=pipeline_branch, pipeline_repo_id=pipeline_repo_id, load_from_fallback_branch=load_from_fallback_branch, branch=branch, repo_identifier=repo_identifier, get_default_from_other_repo=get_default_from_other_repo, load_from_cache=load_from_cache)

Gets an Overlay Input Set by identifier

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
api_instance = harness_python_sdk.PipelineInputSetApi(harness_python_sdk.ApiClient(configuration))
input_set_identifier = 'input_set_identifier_example' # str | Identifier for the Overlay Input Set
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
pipeline_identifier = 'pipeline_identifier_example' # str | Pipeline Identifier for the entity.
pipeline_branch = 'pipeline_branch_example' # str | Github branch of the Pipeline for which the Input Set is to be fetched (optional)
pipeline_repo_id = 'pipeline_repo_id_example' # str | Github Repo identifier of the Pipeline for which the Input Set is to be fetched (optional)
load_from_fallback_branch = false # bool |  (optional) (default to false)
branch = 'branch_example' # str | Name of the branch. (optional)
repo_identifier = 'repo_identifier_example' # str | Git Sync Config Id. (optional)
get_default_from_other_repo = true # bool | if true, return all the default entities (optional)
load_from_cache = 'false' # str |  (optional) (default to false)

try:
    # Gets an Overlay Input Set by identifier
    api_response = api_instance.get_overlay_input_set(input_set_identifier, account_identifier, org_identifier, project_identifier, pipeline_identifier, pipeline_branch=pipeline_branch, pipeline_repo_id=pipeline_repo_id, load_from_fallback_branch=load_from_fallback_branch, branch=branch, repo_identifier=repo_identifier, get_default_from_other_repo=get_default_from_other_repo, load_from_cache=load_from_cache)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineInputSetApi->get_overlay_input_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_set_identifier** | **str**| Identifier for the Overlay Input Set | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **pipeline_identifier** | **str**| Pipeline Identifier for the entity. | 
 **pipeline_branch** | **str**| Github branch of the Pipeline for which the Input Set is to be fetched | [optional] 
 **pipeline_repo_id** | **str**| Github Repo identifier of the Pipeline for which the Input Set is to be fetched | [optional] 
 **load_from_fallback_branch** | **bool**|  | [optional] [default to false]
 **branch** | **str**| Name of the branch. | [optional] 
 **repo_identifier** | **str**| Git Sync Config Id. | [optional] 
 **get_default_from_other_repo** | **bool**| if true, return all the default entities | [optional] 
 **load_from_cache** | **str**|  | [optional] [default to false]

### Return type

[**ResponseDTOOverlayInputSetResponse**](ResponseDTOOverlayInputSetResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_input_set**
> ResponseDTOPageResponseInputSetSummaryResponse list_input_set(account_identifier, org_identifier, project_identifier, pipeline_identifier, page_index=page_index, page_size=page_size, input_set_type=input_set_type, search_term=search_term, sort_orders=sort_orders, branch=branch, repo_identifier=repo_identifier, get_default_from_other_repo=get_default_from_other_repo)

List Input Sets

Lists all Input Sets for a Pipeline

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
api_instance = harness_python_sdk.PipelineInputSetApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
pipeline_identifier = 'pipeline_identifier_example' # str | Pipeline identifier for which we need the Input Sets list.
page_index = 0 # int | Page Index of the results to fetch.Default Value: 0 (optional) (default to 0)
page_size = 100 # int | Results per page (optional) (default to 100)
input_set_type = 'ALL' # str | Type of Input Set. The default value is ALL. (optional) (default to ALL)
search_term = 'search_term_example' # str | Search term to filter out Input Sets based on name, identifier, tags. (optional)
sort_orders = ['sort_orders_example'] # list[str] | Sort criteria for the elements. (optional)
branch = 'branch_example' # str | Name of the branch. (optional)
repo_identifier = 'repo_identifier_example' # str | Git Sync Config Id. (optional)
get_default_from_other_repo = true # bool | if true, return all the default entities (optional)

try:
    # List Input Sets
    api_response = api_instance.list_input_set(account_identifier, org_identifier, project_identifier, pipeline_identifier, page_index=page_index, page_size=page_size, input_set_type=input_set_type, search_term=search_term, sort_orders=sort_orders, branch=branch, repo_identifier=repo_identifier, get_default_from_other_repo=get_default_from_other_repo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineInputSetApi->list_input_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **pipeline_identifier** | **str**| Pipeline identifier for which we need the Input Sets list. | 
 **page_index** | **int**| Page Index of the results to fetch.Default Value: 0 | [optional] [default to 0]
 **page_size** | **int**| Results per page | [optional] [default to 100]
 **input_set_type** | **str**| Type of Input Set. The default value is ALL. | [optional] [default to ALL]
 **search_term** | **str**| Search term to filter out Input Sets based on name, identifier, tags. | [optional] 
 **sort_orders** | [**list[str]**](str.md)| Sort criteria for the elements. | [optional] 
 **branch** | **str**| Name of the branch. | [optional] 
 **repo_identifier** | **str**| Git Sync Config Id. | [optional] 
 **get_default_from_other_repo** | **bool**| if true, return all the default entities | [optional] 

### Return type

[**ResponseDTOPageResponseInputSetSummaryResponse**](ResponseDTOPageResponseInputSetSummaryResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_input_set**
> ResponseDTOInputSetResponse post_input_set(body, account_identifier, org_identifier, project_identifier, pipeline_identifier, pipeline_branch=pipeline_branch, pipeline_repo_id=pipeline_repo_id, branch=branch, repo_identifier=repo_identifier, root_folder=root_folder, file_path=file_path, commit_msg=commit_msg, is_new_branch=is_new_branch, base_branch=base_branch, connector_ref=connector_ref, store_type=store_type, repo_name=repo_name)

Create an Input Set

Creates an Input Set for a Pipeline

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
api_instance = harness_python_sdk.PipelineInputSetApi(harness_python_sdk.ApiClient(configuration))
body = '{   \"summary\" : \"Sample Input Set YAML\",   \"description\" : \"Sample Input Set YAML\",   \"value\" : \"inputSet:\\n    name: Sample Input Set\\n    tags: {}\\n    identifier: Sample_Input_Set\\n    orgIdentifier: default\\n    projectIdentifier: MISC\\n    pipeline:\\n        identifier: Sample_Pipeline\\n        stages:\\n            - stage:\\n                  identifier: Sample_Stage\\n                  type: Approval\\n                  spec:\\n                      execution:\\n                          steps:\\n                              - step:\\n                                    identifier: Approval_Step\\n                                    type: HarnessApproval\\n                                    spec:\\n                                        approvers:\\n                                            userGroups:\\n                                                - account.Admins\\n                              - step:\\n                                    identifier: Shellscript_Step\\n                                    type: ShellScript\\n                                    spec:\\n                                        source:\\n                                            type: Inline\\n                                            spec:\\n                                                script: echo \\\"ShellScript\\\"\\n            - stage:\\n                  identifier: Sample_Deploy_Stage\\n                  type: Deployment\\n                  spec:\\n                      serviceConfig:\\n                          serviceRef: Service1\\n                      infrastructure:\\n                          environmentRef: Env1\\n                          infrastructureDefinition:\\n                              type: KubernetesDirect\\n                              spec:\\n                                  connectorRef: account.harnessciplatform\\n                                  namespace: sample\\n\" }' # str | Input set YAML to be created. The Account, Org, Project, and Pipeline identifiers inside the YAML should match the query parameters.
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
pipeline_identifier = 'pipeline_identifier_example' # str | Pipeline Identifier for the entity.
pipeline_branch = 'pipeline_branch_example' # str | Github branch of the Pipeline for which the Input Set is to be created (optional)
pipeline_repo_id = 'pipeline_repo_id_example' # str | Github Repo identifier of the Pipeline for which the Input Set is to be created (optional)
branch = 'branch_example' # str | Name of the branch. (optional)
repo_identifier = 'repo_identifier_example' # str | Git Sync Config Id. (optional)
root_folder = 'root_folder_example' # str | Path to the root folder of the Entity. (optional)
file_path = 'file_path_example' # str | File Path of the Entity. (optional)
commit_msg = 'commit_msg_example' # str | File Path of the Entity. (optional)
is_new_branch = false # bool | Checks the new branch (optional) (default to false)
base_branch = 'base_branch_example' # str | Name of the default branch. (optional)
connector_ref = 'connector_ref_example' # str | Identifier of Connector needed for CRUD operations on the respective Entity (optional)
store_type = 'store_type_example' # str | Tells whether the Entity is to be saved on Git or not (optional)
repo_name = 'repo_name_example' # str | Name of the repository. (optional)

try:
    # Create an Input Set
    api_response = api_instance.post_input_set(body, account_identifier, org_identifier, project_identifier, pipeline_identifier, pipeline_branch=pipeline_branch, pipeline_repo_id=pipeline_repo_id, branch=branch, repo_identifier=repo_identifier, root_folder=root_folder, file_path=file_path, commit_msg=commit_msg, is_new_branch=is_new_branch, base_branch=base_branch, connector_ref=connector_ref, store_type=store_type, repo_name=repo_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineInputSetApi->post_input_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| Input set YAML to be created. The Account, Org, Project, and Pipeline identifiers inside the YAML should match the query parameters. | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **pipeline_identifier** | **str**| Pipeline Identifier for the entity. | 
 **pipeline_branch** | **str**| Github branch of the Pipeline for which the Input Set is to be created | [optional] 
 **pipeline_repo_id** | **str**| Github Repo identifier of the Pipeline for which the Input Set is to be created | [optional] 
 **branch** | **str**| Name of the branch. | [optional] 
 **repo_identifier** | **str**| Git Sync Config Id. | [optional] 
 **root_folder** | **str**| Path to the root folder of the Entity. | [optional] 
 **file_path** | **str**| File Path of the Entity. | [optional] 
 **commit_msg** | **str**| File Path of the Entity. | [optional] 
 **is_new_branch** | **bool**| Checks the new branch | [optional] [default to false]
 **base_branch** | **str**| Name of the default branch. | [optional] 
 **connector_ref** | **str**| Identifier of Connector needed for CRUD operations on the respective Entity | [optional] 
 **store_type** | **str**| Tells whether the Entity is to be saved on Git or not | [optional] 
 **repo_name** | **str**| Name of the repository. | [optional] 

### Return type

[**ResponseDTOInputSetResponse**](ResponseDTOInputSetResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_overlay_input_set**
> ResponseDTOOverlayInputSetResponse post_overlay_input_set(body, account_identifier, org_identifier, project_identifier, pipeline_identifier, branch=branch, repo_identifier=repo_identifier, root_folder=root_folder, file_path=file_path, commit_msg=commit_msg, is_new_branch=is_new_branch, base_branch=base_branch, connector_ref=connector_ref, store_type=store_type, repo_name=repo_name)

Create an Overlay Input Set for a pipeline

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
api_instance = harness_python_sdk.PipelineInputSetApi(harness_python_sdk.ApiClient(configuration))
body = 'body_example' # str | Overlay Input Set YAML to be created. The Account, Org, Project, and Pipeline identifiers inside the YAML should match the query parameters
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
pipeline_identifier = 'pipeline_identifier_example' # str | Pipeline Identifier for the entity.
branch = 'branch_example' # str | Name of the branch. (optional)
repo_identifier = 'repo_identifier_example' # str | Git Sync Config Id. (optional)
root_folder = 'root_folder_example' # str | Path to the root folder of the Entity. (optional)
file_path = 'file_path_example' # str | File Path of the Entity. (optional)
commit_msg = 'commit_msg_example' # str | File Path of the Entity. (optional)
is_new_branch = false # bool | Checks the new branch (optional) (default to false)
base_branch = 'base_branch_example' # str | Name of the default branch. (optional)
connector_ref = 'connector_ref_example' # str | Identifier of Connector needed for CRUD operations on the respective Entity (optional)
store_type = 'store_type_example' # str | Tells whether the Entity is to be saved on Git or not (optional)
repo_name = 'repo_name_example' # str | Name of the repository. (optional)

try:
    # Create an Overlay Input Set for a pipeline
    api_response = api_instance.post_overlay_input_set(body, account_identifier, org_identifier, project_identifier, pipeline_identifier, branch=branch, repo_identifier=repo_identifier, root_folder=root_folder, file_path=file_path, commit_msg=commit_msg, is_new_branch=is_new_branch, base_branch=base_branch, connector_ref=connector_ref, store_type=store_type, repo_name=repo_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineInputSetApi->post_overlay_input_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| Overlay Input Set YAML to be created. The Account, Org, Project, and Pipeline identifiers inside the YAML should match the query parameters | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **pipeline_identifier** | **str**| Pipeline Identifier for the entity. | 
 **branch** | **str**| Name of the branch. | [optional] 
 **repo_identifier** | **str**| Git Sync Config Id. | [optional] 
 **root_folder** | **str**| Path to the root folder of the Entity. | [optional] 
 **file_path** | **str**| File Path of the Entity. | [optional] 
 **commit_msg** | **str**| File Path of the Entity. | [optional] 
 **is_new_branch** | **bool**| Checks the new branch | [optional] [default to false]
 **base_branch** | **str**| Name of the default branch. | [optional] 
 **connector_ref** | **str**| Identifier of Connector needed for CRUD operations on the respective Entity | [optional] 
 **store_type** | **str**| Tells whether the Entity is to be saved on Git or not | [optional] 
 **repo_name** | **str**| Name of the repository. | [optional] 

### Return type

[**ResponseDTOOverlayInputSetResponse**](ResponseDTOOverlayInputSetResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_input_set**
> ResponseDTOInputSetResponse put_input_set(body, account_identifier, org_identifier, project_identifier, pipeline_identifier, input_set_identifier, if_match=if_match, pipeline_branch=pipeline_branch, pipeline_repo_id=pipeline_repo_id, branch=branch, repo_identifier=repo_identifier, root_folder=root_folder, file_path=file_path, commit_msg=commit_msg, last_object_id=last_object_id, resolved_conflict_commit_id=resolved_conflict_commit_id, base_branch=base_branch, connector_ref=connector_ref, is_new_branch=is_new_branch)

Update an Input Set

Updates the Input Set for a Pipeline

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
api_instance = harness_python_sdk.PipelineInputSetApi(harness_python_sdk.ApiClient(configuration))
body = '{   \"summary\" : \"Sample Input Set YAML\",   \"description\" : \"Sample Input Set YAML\",   \"value\" : \"inputSet:\\n    name: Sample Input Set\\n    tags: {}\\n    identifier: Sample_Input_Set\\n    orgIdentifier: default\\n    projectIdentifier: MISC\\n    pipeline:\\n        identifier: Sample_Pipeline\\n        stages:\\n            - stage:\\n                  identifier: Sample_Stage\\n                  type: Approval\\n                  spec:\\n                      execution:\\n                          steps:\\n                              - step:\\n                                    identifier: Approval_Step\\n                                    type: HarnessApproval\\n                                    spec:\\n                                        approvers:\\n                                            userGroups:\\n                                                - account.Admins\\n                              - step:\\n                                    identifier: Shellscript_Step\\n                                    type: ShellScript\\n                                    spec:\\n                                        source:\\n                                            type: Inline\\n                                            spec:\\n                                                script: echo \\\"ShellScript\\\"\\n            - stage:\\n                  identifier: Sample_Deploy_Stage\\n                  type: Deployment\\n                  spec:\\n                      serviceConfig:\\n                          serviceRef: Service1\\n                      infrastructure:\\n                          environmentRef: Env1\\n                          infrastructureDefinition:\\n                              type: KubernetesDirect\\n                              spec:\\n                                  connectorRef: account.harnessciplatform\\n                                  namespace: sample\\n\" }' # str | Input set YAML to be updated. The query parameters should match the Account, Org, Project, and Pipeline Ids in the YAML.
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
pipeline_identifier = 'pipeline_identifier_example' # str | Pipeline Identifier for the entity.
input_set_identifier = 'input_set_identifier_example' # str | Identifier for the Input Set that needs to be updated. An Input Set corresponding to this identifier should already exist.
if_match = 'if_match_example' # str | Version of Entity to match (optional)
pipeline_branch = 'pipeline_branch_example' # str | Github branch of the Pipeline for which the Input Set is to be updated (optional)
pipeline_repo_id = 'pipeline_repo_id_example' # str | Github Repo Id of the Pipeline for which the Input Set is to be updated (optional)
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
    # Update an Input Set
    api_response = api_instance.put_input_set(body, account_identifier, org_identifier, project_identifier, pipeline_identifier, input_set_identifier, if_match=if_match, pipeline_branch=pipeline_branch, pipeline_repo_id=pipeline_repo_id, branch=branch, repo_identifier=repo_identifier, root_folder=root_folder, file_path=file_path, commit_msg=commit_msg, last_object_id=last_object_id, resolved_conflict_commit_id=resolved_conflict_commit_id, base_branch=base_branch, connector_ref=connector_ref, is_new_branch=is_new_branch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineInputSetApi->put_input_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| Input set YAML to be updated. The query parameters should match the Account, Org, Project, and Pipeline Ids in the YAML. | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **pipeline_identifier** | **str**| Pipeline Identifier for the entity. | 
 **input_set_identifier** | **str**| Identifier for the Input Set that needs to be updated. An Input Set corresponding to this identifier should already exist. | 
 **if_match** | **str**| Version of Entity to match | [optional] 
 **pipeline_branch** | **str**| Github branch of the Pipeline for which the Input Set is to be updated | [optional] 
 **pipeline_repo_id** | **str**| Github Repo Id of the Pipeline for which the Input Set is to be updated | [optional] 
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

[**ResponseDTOInputSetResponse**](ResponseDTOInputSetResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_overlay_input_set**
> ResponseDTOOverlayInputSetResponse put_overlay_input_set(body, account_identifier, org_identifier, project_identifier, pipeline_identifier, input_set_identifier, if_match=if_match, branch=branch, repo_identifier=repo_identifier, root_folder=root_folder, file_path=file_path, commit_msg=commit_msg, last_object_id=last_object_id, resolved_conflict_commit_id=resolved_conflict_commit_id, base_branch=base_branch, connector_ref=connector_ref, is_new_branch=is_new_branch)

Update an Overlay Input Set for a pipeline

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
api_instance = harness_python_sdk.PipelineInputSetApi(harness_python_sdk.ApiClient(configuration))
body = 'body_example' # str | Overlay Input Set YAML to be updated. The Account, Org, Project, and Pipeline identifiers inside the YAML should match the query parameters, and the Overlay Input Set identifier cannot be changed.
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
pipeline_identifier = 'pipeline_identifier_example' # str | Pipeline Identifier for the entity.
input_set_identifier = 'input_set_identifier_example' # str | Identifier for the Overlay Input Set that needs to be updated.
if_match = 'if_match_example' # str | Version of Entity to match (optional)
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
    # Update an Overlay Input Set for a pipeline
    api_response = api_instance.put_overlay_input_set(body, account_identifier, org_identifier, project_identifier, pipeline_identifier, input_set_identifier, if_match=if_match, branch=branch, repo_identifier=repo_identifier, root_folder=root_folder, file_path=file_path, commit_msg=commit_msg, last_object_id=last_object_id, resolved_conflict_commit_id=resolved_conflict_commit_id, base_branch=base_branch, connector_ref=connector_ref, is_new_branch=is_new_branch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineInputSetApi->put_overlay_input_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| Overlay Input Set YAML to be updated. The Account, Org, Project, and Pipeline identifiers inside the YAML should match the query parameters, and the Overlay Input Set identifier cannot be changed. | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **pipeline_identifier** | **str**| Pipeline Identifier for the entity. | 
 **input_set_identifier** | **str**| Identifier for the Overlay Input Set that needs to be updated. | 
 **if_match** | **str**| Version of Entity to match | [optional] 
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

[**ResponseDTOOverlayInputSetResponse**](ResponseDTOOverlayInputSetResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **runtime_input_template**
> ResponseDTOInputSetTemplateWithReplacedExpressionsResponse runtime_input_template(account_identifier, org_identifier, project_identifier, pipeline_identifier, body=body, load_from_cache=load_from_cache, branch=branch, repo_identifier=repo_identifier, get_default_from_other_repo=get_default_from_other_repo)

Fetch Runtime Input Template

Returns Runtime Input Template for a Pipeline

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
api_instance = harness_python_sdk.PipelineInputSetApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
pipeline_identifier = 'pipeline_identifier_example' # str | Pipeline identifier for which we need the Runtime Input Template.
body = harness_python_sdk.InputSetTemplateRequest() # InputSetTemplateRequest |  (optional)
load_from_cache = 'false' # str |  (optional) (default to false)
branch = 'branch_example' # str | Name of the branch. (optional)
repo_identifier = 'repo_identifier_example' # str | Git Sync Config Id. (optional)
get_default_from_other_repo = true # bool | if true, return all the default entities (optional)

try:
    # Fetch Runtime Input Template
    api_response = api_instance.runtime_input_template(account_identifier, org_identifier, project_identifier, pipeline_identifier, body=body, load_from_cache=load_from_cache, branch=branch, repo_identifier=repo_identifier, get_default_from_other_repo=get_default_from_other_repo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineInputSetApi->runtime_input_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **pipeline_identifier** | **str**| Pipeline identifier for which we need the Runtime Input Template. | 
 **body** | [**InputSetTemplateRequest**](InputSetTemplateRequest.md)|  | [optional] 
 **load_from_cache** | **str**|  | [optional] [default to false]
 **branch** | **str**| Name of the branch. | [optional] 
 **repo_identifier** | **str**| Git Sync Config Id. | [optional] 
 **get_default_from_other_repo** | **bool**| if true, return all the default entities | [optional] 

### Return type

[**ResponseDTOInputSetTemplateWithReplacedExpressionsResponse**](ResponseDTOInputSetTemplateWithReplacedExpressionsResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_input_set_git_details**
> ResponseDTOInputSetGitUpdateResponse update_input_set_git_details(account_identifier, org_identifier, project_identifier, pipeline_identifier, input_set_identifier, connector_ref=connector_ref, repo_name=repo_name, file_path=file_path)

Update git-metadata in remote input-set

Update git-metadata in remote input-set and return the updated input-set

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
api_instance = harness_python_sdk.PipelineInputSetApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
pipeline_identifier = 'pipeline_identifier_example' # str | Pipeline Identifier for the entity.
input_set_identifier = 'input_set_identifier_example' # str | Identifier for the Input Set
connector_ref = 'connector_ref_example' # str | Identifier of Connector needed for CRUD operations on the respective Entity (optional)
repo_name = 'repo_name_example' # str | Name of the repository. (optional)
file_path = 'file_path_example' # str | File Path of the Entity. (optional)

try:
    # Update git-metadata in remote input-set
    api_response = api_instance.update_input_set_git_details(account_identifier, org_identifier, project_identifier, pipeline_identifier, input_set_identifier, connector_ref=connector_ref, repo_name=repo_name, file_path=file_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineInputSetApi->update_input_set_git_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **pipeline_identifier** | **str**| Pipeline Identifier for the entity. | 
 **input_set_identifier** | **str**| Identifier for the Input Set | 
 **connector_ref** | **str**| Identifier of Connector needed for CRUD operations on the respective Entity | [optional] 
 **repo_name** | **str**| Name of the repository. | [optional] 
 **file_path** | **str**| File Path of the Entity. | [optional] 

### Return type

[**ResponseDTOInputSetGitUpdateResponse**](ResponseDTOInputSetGitUpdateResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

