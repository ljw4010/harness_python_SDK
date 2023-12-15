# harness_python_sdk.PipelineApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_pipeline**](PipelineApi.md#delete_pipeline) | **DELETE** /pipeline/api/pipelines/{pipelineIdentifier} | Delete a Pipeline
[**get_pipeline**](PipelineApi.md#get_pipeline) | **GET** /pipeline/api/pipelines/{pipelineIdentifier} | Fetch a Pipeline
[**get_pipeline_list**](PipelineApi.md#get_pipeline_list) | **POST** /pipeline/api/pipelines/list | List Pipelines
[**get_pipeline_summary**](PipelineApi.md#get_pipeline_summary) | **GET** /pipeline/api/pipelines/summary/{pipelineIdentifier} | Fetch Pipeline Summary
[**import_pipeline**](PipelineApi.md#import_pipeline) | **POST** /pipeline/api/pipelines/import/{pipelineIdentifier} | Import and Create Pipeline from Git Repository
[**post_pipeline**](PipelineApi.md#post_pipeline) | **POST** /pipeline/api/pipelines | Create a Pipeline
[**post_pipeline_v2**](PipelineApi.md#post_pipeline_v2) | **POST** /pipeline/api/pipelines/v2 | Create a Pipeline
[**update_pipeline**](PipelineApi.md#update_pipeline) | **PUT** /pipeline/api/pipelines/{pipelineIdentifier} | Update a Pipeline
[**update_pipeline_git_details**](PipelineApi.md#update_pipeline_git_details) | **PUT** /pipeline/api/pipelines/{pipelineIdentifier}/update-git-metadata | Update git-metadata in remote pipeline Entity
[**update_pipeline_v2**](PipelineApi.md#update_pipeline_v2) | **PUT** /pipeline/api/pipelines/v2/{pipelineIdentifier} | Update a Pipeline

# **delete_pipeline**
> ResponseDTOBoolean delete_pipeline(account_identifier, org_identifier, project_identifier, pipeline_identifier, if_match=if_match, branch=branch, repo_identifier=repo_identifier, root_folder=root_folder, file_path=file_path, commit_msg=commit_msg, last_object_id=last_object_id)

Delete a Pipeline

Deletes a Pipeline by Identifier

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
api_instance = harness_python_sdk.PipelineApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
pipeline_identifier = 'pipeline_identifier_example' # str | Pipeline Identifier
if_match = 'if_match_example' # str | Version of Entity to match (optional)
branch = 'branch_example' # str | Name of the branch. (optional)
repo_identifier = 'repo_identifier_example' # str | Git Sync Config Id. (optional)
root_folder = 'root_folder_example' # str | Path to the root folder of the Entity. (optional)
file_path = 'file_path_example' # str | File Path of the Entity. (optional)
commit_msg = 'commit_msg_example' # str | Commit Message to use for the merge commit. (optional)
last_object_id = 'last_object_id_example' # str | Last Object Id (optional)

try:
    # Delete a Pipeline
    api_response = api_instance.delete_pipeline(account_identifier, org_identifier, project_identifier, pipeline_identifier, if_match=if_match, branch=branch, repo_identifier=repo_identifier, root_folder=root_folder, file_path=file_path, commit_msg=commit_msg, last_object_id=last_object_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineApi->delete_pipeline: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **pipeline_identifier** | **str**| Pipeline Identifier | 
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

# **get_pipeline**
> ResponseDTOPMSPipelineResponse get_pipeline(account_identifier, org_identifier, project_identifier, pipeline_identifier, branch=branch, repo_identifier=repo_identifier, get_default_from_other_repo=get_default_from_other_repo, get_templates_resolved_pipeline=get_templates_resolved_pipeline, load_from_fallback_branch=load_from_fallback_branch, validate_async=validate_async, load_from_cache=load_from_cache)

Fetch a Pipeline

Returns a Pipeline by Identifier

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
api_instance = harness_python_sdk.PipelineApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
pipeline_identifier = 'pipeline_identifier_example' # str | Pipeline Identifier
branch = 'branch_example' # str | Name of the branch. (optional)
repo_identifier = 'repo_identifier_example' # str | Git Sync Config Id. (optional)
get_default_from_other_repo = true # bool | if true, return all the default entities (optional)
get_templates_resolved_pipeline = false # bool | This is a boolean value. If true, returns Templates resolved Pipeline YAML in the response else returns null. (optional) (default to false)
load_from_fallback_branch = false # bool |  (optional) (default to false)
validate_async = false # bool |  (optional) (default to false)
load_from_cache = 'false' # str |  (optional) (default to false)

try:
    # Fetch a Pipeline
    api_response = api_instance.get_pipeline(account_identifier, org_identifier, project_identifier, pipeline_identifier, branch=branch, repo_identifier=repo_identifier, get_default_from_other_repo=get_default_from_other_repo, get_templates_resolved_pipeline=get_templates_resolved_pipeline, load_from_fallback_branch=load_from_fallback_branch, validate_async=validate_async, load_from_cache=load_from_cache)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineApi->get_pipeline: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **pipeline_identifier** | **str**| Pipeline Identifier | 
 **branch** | **str**| Name of the branch. | [optional] 
 **repo_identifier** | **str**| Git Sync Config Id. | [optional] 
 **get_default_from_other_repo** | **bool**| if true, return all the default entities | [optional] 
 **get_templates_resolved_pipeline** | **bool**| This is a boolean value. If true, returns Templates resolved Pipeline YAML in the response else returns null. | [optional] [default to false]
 **load_from_fallback_branch** | **bool**|  | [optional] [default to false]
 **validate_async** | **bool**|  | [optional] [default to false]
 **load_from_cache** | **str**|  | [optional] [default to false]

### Return type

[**ResponseDTOPMSPipelineResponse**](ResponseDTOPMSPipelineResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pipeline_list**
> ResponseDTOPagePMSPipelineSummaryResponse get_pipeline_list(account_identifier, org_identifier, project_identifier, body=body, page=page, size=size, sort=sort, search_term=search_term, module=module, filter_identifier=filter_identifier, branch=branch, repo_identifier=repo_identifier, get_default_from_other_repo=get_default_from_other_repo, get_distinct_from_branches=get_distinct_from_branches)

List Pipelines

Returns List of Pipelines in the Given Project

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
api_instance = harness_python_sdk.PipelineApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
body = harness_python_sdk.PipelineFilterProperties() # PipelineFilterProperties | This is the body for the filter properties for listing pipelines. (optional)
page = 0 # int | Page Index of the results to fetch.Default Value: 0 (optional) (default to 0)
size = 25 # int | Results per page (optional) (default to 25)
sort = ['sort_example'] # list[str] | Sort criteria for the elements. (optional)
search_term = 'search_term_example' # str | Search term to filter out pipelines based on pipeline name, identifier, tags. (optional)
module = 'module_example' # str |  (optional)
filter_identifier = 'filter_identifier_example' # str |  (optional)
branch = 'branch_example' # str | Name of the branch. (optional)
repo_identifier = 'repo_identifier_example' # str | Git Sync Config Id. (optional)
get_default_from_other_repo = true # bool | if true, return all the default entities (optional)
get_distinct_from_branches = true # bool | Boolean flag to get distinct pipelines from all branches. (optional)

try:
    # List Pipelines
    api_response = api_instance.get_pipeline_list(account_identifier, org_identifier, project_identifier, body=body, page=page, size=size, sort=sort, search_term=search_term, module=module, filter_identifier=filter_identifier, branch=branch, repo_identifier=repo_identifier, get_default_from_other_repo=get_default_from_other_repo, get_distinct_from_branches=get_distinct_from_branches)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineApi->get_pipeline_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **body** | [**PipelineFilterProperties**](PipelineFilterProperties.md)| This is the body for the filter properties for listing pipelines. | [optional] 
 **page** | **int**| Page Index of the results to fetch.Default Value: 0 | [optional] [default to 0]
 **size** | **int**| Results per page | [optional] [default to 25]
 **sort** | [**list[str]**](str.md)| Sort criteria for the elements. | [optional] 
 **search_term** | **str**| Search term to filter out pipelines based on pipeline name, identifier, tags. | [optional] 
 **module** | **str**|  | [optional] 
 **filter_identifier** | **str**|  | [optional] 
 **branch** | **str**| Name of the branch. | [optional] 
 **repo_identifier** | **str**| Git Sync Config Id. | [optional] 
 **get_default_from_other_repo** | **bool**| if true, return all the default entities | [optional] 
 **get_distinct_from_branches** | **bool**| Boolean flag to get distinct pipelines from all branches. | [optional] 

### Return type

[**ResponseDTOPagePMSPipelineSummaryResponse**](ResponseDTOPagePMSPipelineSummaryResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pipeline_summary**
> ResponseDTOPMSPipelineSummaryResponse get_pipeline_summary(account_identifier, org_identifier, project_identifier, pipeline_identifier, branch=branch, repo_identifier=repo_identifier, get_default_from_other_repo=get_default_from_other_repo, load_from_fallback_branch=load_from_fallback_branch, load_from_cache=load_from_cache)

Fetch Pipeline Summary

Returns Pipeline Summary by Identifier

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
api_instance = harness_python_sdk.PipelineApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
pipeline_identifier = 'pipeline_identifier_example' # str | Pipeline Identifier
branch = 'branch_example' # str | Name of the branch. (optional)
repo_identifier = 'repo_identifier_example' # str | Git Sync Config Id. (optional)
get_default_from_other_repo = true # bool | if true, return all the default entities (optional)
load_from_fallback_branch = false # bool |  (optional) (default to false)
load_from_cache = 'false' # str |  (optional) (default to false)

try:
    # Fetch Pipeline Summary
    api_response = api_instance.get_pipeline_summary(account_identifier, org_identifier, project_identifier, pipeline_identifier, branch=branch, repo_identifier=repo_identifier, get_default_from_other_repo=get_default_from_other_repo, load_from_fallback_branch=load_from_fallback_branch, load_from_cache=load_from_cache)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineApi->get_pipeline_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **pipeline_identifier** | **str**| Pipeline Identifier | 
 **branch** | **str**| Name of the branch. | [optional] 
 **repo_identifier** | **str**| Git Sync Config Id. | [optional] 
 **get_default_from_other_repo** | **bool**| if true, return all the default entities | [optional] 
 **load_from_fallback_branch** | **bool**|  | [optional] [default to false]
 **load_from_cache** | **str**|  | [optional] [default to false]

### Return type

[**ResponseDTOPMSPipelineSummaryResponse**](ResponseDTOPMSPipelineSummaryResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_pipeline**
> ResponseDTOPipelineSaveResponse import_pipeline(account_identifier, org_identifier, project_identifier, pipeline_identifier, body=body, connector_ref=connector_ref, repo_name=repo_name, branch=branch, file_path=file_path, is_force_import=is_force_import)

Import and Create Pipeline from Git Repository

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
api_instance = harness_python_sdk.PipelineApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
pipeline_identifier = 'pipeline_identifier_example' # str | Pipeline Identifier
body = harness_python_sdk.PipelineImportRequest() # PipelineImportRequest |  (optional)
connector_ref = 'connector_ref_example' # str | Identifier of Connector needed for CRUD operations on the respective Entity (optional)
repo_name = 'repo_name_example' # str | Name of the repository. (optional)
branch = 'branch_example' # str | Name of the branch. (optional)
file_path = 'file_path_example' # str | File Path of the Entity. (optional)
is_force_import = false # bool | isForceImport (optional) (default to false)

try:
    # Import and Create Pipeline from Git Repository
    api_response = api_instance.import_pipeline(account_identifier, org_identifier, project_identifier, pipeline_identifier, body=body, connector_ref=connector_ref, repo_name=repo_name, branch=branch, file_path=file_path, is_force_import=is_force_import)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineApi->import_pipeline: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **pipeline_identifier** | **str**| Pipeline Identifier | 
 **body** | [**PipelineImportRequest**](PipelineImportRequest.md)|  | [optional] 
 **connector_ref** | **str**| Identifier of Connector needed for CRUD operations on the respective Entity | [optional] 
 **repo_name** | **str**| Name of the repository. | [optional] 
 **branch** | **str**| Name of the branch. | [optional] 
 **file_path** | **str**| File Path of the Entity. | [optional] 
 **is_force_import** | **bool**| isForceImport | [optional] [default to false]

### Return type

[**ResponseDTOPipelineSaveResponse**](ResponseDTOPipelineSaveResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_pipeline**
> ResponseDTOString post_pipeline(body, account_identifier, org_identifier, project_identifier, branch=branch, repo_identifier=repo_identifier, root_folder=root_folder, file_path=file_path, commit_msg=commit_msg, is_new_branch=is_new_branch, base_branch=base_branch, connector_ref=connector_ref, store_type=store_type, repo_name=repo_name)

Create a Pipeline

Creates a Pipeline

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
api_instance = harness_python_sdk.PipelineApi(harness_python_sdk.ApiClient(configuration))
body = 'body_example' # str | Pipeline YAML
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
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
    # Create a Pipeline
    api_response = api_instance.post_pipeline(body, account_identifier, org_identifier, project_identifier, branch=branch, repo_identifier=repo_identifier, root_folder=root_folder, file_path=file_path, commit_msg=commit_msg, is_new_branch=is_new_branch, base_branch=base_branch, connector_ref=connector_ref, store_type=store_type, repo_name=repo_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineApi->post_pipeline: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| Pipeline YAML | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
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

[**ResponseDTOString**](ResponseDTOString.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_pipeline_v2**
> ResponseDTOPipelineSaveResponse post_pipeline_v2(body, account_identifier, org_identifier, project_identifier, branch=branch, repo_identifier=repo_identifier, root_folder=root_folder, file_path=file_path, commit_msg=commit_msg, is_new_branch=is_new_branch, base_branch=base_branch, connector_ref=connector_ref, store_type=store_type, repo_name=repo_name, public=public)

Create a Pipeline

Creates a Pipeline

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
api_instance = harness_python_sdk.PipelineApi(harness_python_sdk.ApiClient(configuration))
body = '{   \"summary\" : \"Sample Create Pipeline YAML\",   \"description\" : \"Sample Pipeline YAML with One Build Stage and One Deploy Stage\",   \"value\" : \"pipeline:\\n    name: Sample Pipeline\\n    identifier: Sample_Pipeline\\n    allowStageExecutions: false\\n    projectIdentifier: Temp\\n    orgIdentifier: default\\n    tags: {}\\n    stages:\\n        - stage:\\n              name: Sample Stage\\n              identifier: Sample_Stage\\n              description: \\\"\\\"\\n              type: Approval\\n              spec:\\n                  execution:\\n                      steps:\\n                          - step:\\n                                name: Approval Step\\n                                identifier: Approval_Step\\n                                type: HarnessApproval\\n                                timeout: 1d\\n                                spec:\\n                                    approvalMessage: |-\\n                                        Please review the following information\\n                                        and approve the pipeline progression\\n                                    includePipelineExecutionHistory: true\\n                                    approvers:\\n                                        minimumCount: 1\\n                                        disallowPipelineExecutor: false\\n                                        userGroups: <+input>\\n                                    approverInputs: []\\n                          - step:\\n                                type: ShellScript\\n                                name: ShellScript Step\\n                                identifier: ShellScript_Step\\n                                spec:\\n                                    shell: Bash\\n                                    onDelegate: true\\n                                    source:\\n                                        type: Inline\\n                                        spec:\\n                                            script: <+input>\\n                                    environmentVariables: []\\n                                    outputVariables: []\\n                                    executionTarget: {}\\n                                timeout: 10m\\n              tags: {}\\n        - stage:\\n              name: Sample Deploy Stage\\n              identifier: Sample_Deploy_Stage\\n              description: \\\"\\\"\\n              type: Deployment\\n              spec:\\n                  serviceConfig:\\n                      serviceRef: <+input>\\n                      serviceDefinition:\\n                          spec:\\n                              variables: []\\n                          type: Kubernetes\\n                  infrastructure:\\n                      environmentRef: <+input>\\n                      infrastructureDefinition:\\n                          type: KubernetesDirect\\n                          spec:\\n                              connectorRef: <+input>\\n                              namespace: <+input>\\n                              releaseName: release-<+INFRA_KEY>\\n                      allowSimultaneousDeployments: false\\n                  execution:\\n                      steps:\\n                          - step:\\n                                name: Rollout Deployment\\n                                identifier: rolloutDeployment\\n                                type: K8sRollingDeploy\\n                                timeout: 10m\\n                                spec:\\n                                    skipDryRun: false\\n                      rollbackSteps:\\n                          - step:\\n                                name: Rollback Rollout Deployment\\n                                identifier: rollbackRolloutDeployment\\n                                type: K8sRollingRollback\\n                                timeout: 10m\\n                                spec: {}\\n              tags: {}\\n              failureStrategies:\\n                  - onFailure:\\n                        errors:\\n                            - AllErrors\\n                        action:\\n                            type: StageRollback\\n\" }' # str | Pipeline YAML
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
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
public = false # bool |  (optional) (default to false)

try:
    # Create a Pipeline
    api_response = api_instance.post_pipeline_v2(body, account_identifier, org_identifier, project_identifier, branch=branch, repo_identifier=repo_identifier, root_folder=root_folder, file_path=file_path, commit_msg=commit_msg, is_new_branch=is_new_branch, base_branch=base_branch, connector_ref=connector_ref, store_type=store_type, repo_name=repo_name, public=public)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineApi->post_pipeline_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| Pipeline YAML | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
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
 **public** | **bool**|  | [optional] [default to false]

### Return type

[**ResponseDTOPipelineSaveResponse**](ResponseDTOPipelineSaveResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pipeline**
> ResponseDTOString update_pipeline(body, account_identifier, org_identifier, project_identifier, pipeline_identifier, if_match=if_match, branch=branch, repo_identifier=repo_identifier, root_folder=root_folder, file_path=file_path, commit_msg=commit_msg, last_object_id=last_object_id, resolved_conflict_commit_id=resolved_conflict_commit_id, base_branch=base_branch, connector_ref=connector_ref, is_new_branch=is_new_branch)

Update a Pipeline

Updates a Pipeline by Identifier

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
api_instance = harness_python_sdk.PipelineApi(harness_python_sdk.ApiClient(configuration))
body = 'body_example' # str | Pipeline YAML to be updated
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
pipeline_identifier = 'pipeline_identifier_example' # str | Pipeline Identifier
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
    # Update a Pipeline
    api_response = api_instance.update_pipeline(body, account_identifier, org_identifier, project_identifier, pipeline_identifier, if_match=if_match, branch=branch, repo_identifier=repo_identifier, root_folder=root_folder, file_path=file_path, commit_msg=commit_msg, last_object_id=last_object_id, resolved_conflict_commit_id=resolved_conflict_commit_id, base_branch=base_branch, connector_ref=connector_ref, is_new_branch=is_new_branch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineApi->update_pipeline: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| Pipeline YAML to be updated | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **pipeline_identifier** | **str**| Pipeline Identifier | 
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

[**ResponseDTOString**](ResponseDTOString.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pipeline_git_details**
> ResponseDTOPMSGitUpdateResponse update_pipeline_git_details(account_identifier, org_identifier, project_identifier, pipeline_identifier, connector_ref=connector_ref, repo_name=repo_name, file_path=file_path)

Update git-metadata in remote pipeline Entity

Update git-metadata in remote pipeline and returns the identifier of updated pipeline

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
api_instance = harness_python_sdk.PipelineApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
pipeline_identifier = 'pipeline_identifier_example' # str | Pipeline Identifier
connector_ref = 'connector_ref_example' # str | Identifier of Connector needed for CRUD operations on the respective Entity (optional)
repo_name = 'repo_name_example' # str | Name of the repository. (optional)
file_path = 'file_path_example' # str | File Path of the Entity. (optional)

try:
    # Update git-metadata in remote pipeline Entity
    api_response = api_instance.update_pipeline_git_details(account_identifier, org_identifier, project_identifier, pipeline_identifier, connector_ref=connector_ref, repo_name=repo_name, file_path=file_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineApi->update_pipeline_git_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **pipeline_identifier** | **str**| Pipeline Identifier | 
 **connector_ref** | **str**| Identifier of Connector needed for CRUD operations on the respective Entity | [optional] 
 **repo_name** | **str**| Name of the repository. | [optional] 
 **file_path** | **str**| File Path of the Entity. | [optional] 

### Return type

[**ResponseDTOPMSGitUpdateResponse**](ResponseDTOPMSGitUpdateResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pipeline_v2**
> ResponseDTOPipelineSaveResponse update_pipeline_v2(body, account_identifier, org_identifier, project_identifier, pipeline_identifier, if_match=if_match, branch=branch, repo_identifier=repo_identifier, root_folder=root_folder, file_path=file_path, commit_msg=commit_msg, last_object_id=last_object_id, resolved_conflict_commit_id=resolved_conflict_commit_id, base_branch=base_branch, connector_ref=connector_ref, is_new_branch=is_new_branch, public=public)

Update a Pipeline

Updates a Pipeline by Identifier

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
api_instance = harness_python_sdk.PipelineApi(harness_python_sdk.ApiClient(configuration))
body = '{   \"summary\" : \"Sample Update Pipeline YAML\",   \"description\" : \"Sample Pipeline YAML with One Build Stage and One Deploy Stage\",   \"value\" : \"pipeline:\\n    name: Sample Pipeline\\n    identifier: Sample_Pipeline\\n    allowStageExecutions: false\\n    projectIdentifier: Temp\\n    orgIdentifier: default\\n    tags: {}\\n    stages:\\n        - stage:\\n              name: Sample Stage\\n              identifier: Sample_Stage\\n              description: \\\"\\\"\\n              type: Approval\\n              spec:\\n                  execution:\\n                      steps:\\n                          - step:\\n                                name: Approval Step\\n                                identifier: Approval_Step\\n                                type: HarnessApproval\\n                                timeout: 1d\\n                                spec:\\n                                    approvalMessage: |-\\n                                        Please review the following information\\n                                        and approve the pipeline progression\\n                                    includePipelineExecutionHistory: true\\n                                    approvers:\\n                                        minimumCount: 1\\n                                        disallowPipelineExecutor: false\\n                                        userGroups: <+input>\\n                                    approverInputs: []\\n                          - step:\\n                                type: ShellScript\\n                                name: ShellScript Step\\n                                identifier: ShellScript_Step\\n                                spec:\\n                                    shell: Bash\\n                                    onDelegate: true\\n                                    source:\\n                                        type: Inline\\n                                        spec:\\n                                            script: <+input>\\n                                    environmentVariables: []\\n                                    outputVariables: []\\n                                    executionTarget: {}\\n                                timeout: 10m\\n              tags: {}\\n        - stage:\\n              name: Sample Deploy Stage\\n              identifier: Sample_Deploy_Stage\\n              description: \\\"\\\"\\n              type: Deployment\\n              spec:\\n                  serviceConfig:\\n                      serviceRef: <+input>\\n                      serviceDefinition:\\n                          spec:\\n                              variables: []\\n                          type: Kubernetes\\n                  infrastructure:\\n                      environmentRef: <+input>\\n                      infrastructureDefinition:\\n                          type: KubernetesDirect\\n                          spec:\\n                              connectorRef: <+input>\\n                              namespace: <+input>\\n                              releaseName: release-<+INFRA_KEY>\\n                      allowSimultaneousDeployments: false\\n                  execution:\\n                      steps:\\n                          - step:\\n                                name: Rollout Deployment\\n                                identifier: rolloutDeployment\\n                                type: K8sRollingDeploy\\n                                timeout: 10m\\n                                spec:\\n                                    skipDryRun: false\\n                      rollbackSteps:\\n                          - step:\\n                                name: Rollback Rollout Deployment\\n                                identifier: rollbackRolloutDeployment\\n                                type: K8sRollingRollback\\n                                timeout: 10m\\n                                spec: {}\\n              tags: {}\\n              failureStrategies:\\n                  - onFailure:\\n                        errors:\\n                            - AllErrors\\n                        action:\\n                            type: StageRollback\\n\" }' # str | Pipeline YAML to be updated
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
pipeline_identifier = 'pipeline_identifier_example' # str | Pipeline Identifier
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
public = false # bool |  (optional) (default to false)

try:
    # Update a Pipeline
    api_response = api_instance.update_pipeline_v2(body, account_identifier, org_identifier, project_identifier, pipeline_identifier, if_match=if_match, branch=branch, repo_identifier=repo_identifier, root_folder=root_folder, file_path=file_path, commit_msg=commit_msg, last_object_id=last_object_id, resolved_conflict_commit_id=resolved_conflict_commit_id, base_branch=base_branch, connector_ref=connector_ref, is_new_branch=is_new_branch, public=public)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineApi->update_pipeline_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| Pipeline YAML to be updated | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **pipeline_identifier** | **str**| Pipeline Identifier | 
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
 **public** | **bool**|  | [optional] [default to false]

### Return type

[**ResponseDTOPipelineSaveResponse**](ResponseDTOPipelineSaveResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

