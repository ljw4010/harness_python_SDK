# swagger_client.TemplatesApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_template**](TemplatesApi.md#create_template) | **POST** /template/api/templates | Create a Template
[**delete_template_version**](TemplatesApi.md#delete_template_version) | **DELETE** /template/api/templates/{templateIdentifier}/{versionLabel} | Delete Template Version
[**get_refreshed_yaml**](TemplatesApi.md#get_refreshed_yaml) | **POST** /template/api/refresh-template/refreshed-yaml | Get YAML with updated Template Inputs
[**get_template**](TemplatesApi.md#get_template) | **GET** /template/api/templates/{templateIdentifier} | Get Template
[**get_template_input_set_yaml**](TemplatesApi.md#get_template_input_set_yaml) | **GET** /template/api/templates/templateInputs/{templateIdentifier} | Gets Template Input Set YAML
[**get_template_metadata_list**](TemplatesApi.md#get_template_metadata_list) | **POST** /template/api/templates/list-metadata | Gets all metadata of template list
[**move_template_configs**](TemplatesApi.md#move_template_configs) | **POST** /template/api/templates/move-config/{templateIdentifier} | Move Template YAML from inline to remote
[**templatevalidate_template_inputs**](TemplatesApi.md#templatevalidate_template_inputs) | **GET** /template/api/refresh-template/validate-template-inputs | Validate Template Inputs in a YAML
[**update_existing_template_version**](TemplatesApi.md#update_existing_template_version) | **PUT** /template/api/templates/update/{templateIdentifier}/{versionLabel} | Update Template Version
[**update_git_details**](TemplatesApi.md#update_git_details) | **POST** /template/api/templates/update/git-metadata/{templateIdentifier}/{versionLabel} | Update git metadata details for a remote template
[**update_stable_template**](TemplatesApi.md#update_stable_template) | **PUT** /template/api/templates/updateStableTemplate/{templateIdentifier}/{versionLabel} | Update Stable Template Version

# **create_template**
> ResponseDTOTemplateWrapperResponse create_template(body, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, branch=branch, repo_identifier=repo_identifier, root_folder=root_folder, file_path=file_path, commit_msg=commit_msg, is_new_branch=is_new_branch, base_branch=base_branch, connector_ref=connector_ref, store_type=store_type, repo_name=repo_name, set_default_template=set_default_template, comments=comments, is_new_template=is_new_template)

Create a Template

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: x-api-key
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TemplatesApi(swagger_client.ApiClient(configuration))
body = '{   \"summary\" : \"Sample Create Template YAML\",   \"description\" : \"Sample Template YAML\",   \"value\" : \"template:\\n  name: pipelineTemplate\\n  identifier: pipelineTemplate\\n  versionLabel: v1\\n  type: Pipeline\\n  projectIdentifier: TemplateDemo\\n  orgIdentifier: default\\n  tags: {}\\n  spec:\\n    stages:\\n      - stage:\\n          name: stage1\\n          identifier: stage1\\n          description: \\\"\\\"\\n          type: Deployment\\n          spec:\\n            deploymentType: Kubernetes\\n            service:\\n              serviceRef: <+input>\\n              serviceInputs: <+input>\\n            environment:\\n              environmentRef: <+input>\\n              deployToAll: false\\n              environmentInputs: <+input>\\n              infrastructureDefinitions: <+input>\\n            execution:\\n              steps:\\n                - step:\\n                    type: ShellScript\\n                    name: Shell Script_1\\n                    identifier: ShellScript_1\\n                    spec:\\n                      shell: Bash\\n                      onDelegate: true\\n                      source:\\n                        type: Inline\\n                        spec:\\n                          script: <+input>\\n                      environmentVariables: []\\n                      outputVariables: []\\n                    timeout: 10m\\n              rollbackSteps: []\\n          tags: {}\\n          failureStrategies:\\n            - onFailure:\\n                errors:\\n                  - AllErrors\\n                action:\\n                  type: StageRollback\\n\" }' # str | Template YAML
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
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
set_default_template = false # bool | Specify true if Default Template is to be set (optional) (default to false)
comments = 'comments_example' # str | Comments (optional)
is_new_template = false # bool | When isNewTemplate flag is set user will not be able to create a new version for an existing template (optional) (default to false)

try:
    # Create a Template
    api_response = api_instance.create_template(body, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, branch=branch, repo_identifier=repo_identifier, root_folder=root_folder, file_path=file_path, commit_msg=commit_msg, is_new_branch=is_new_branch, base_branch=base_branch, connector_ref=connector_ref, store_type=store_type, repo_name=repo_name, set_default_template=set_default_template, comments=comments, is_new_template=is_new_template)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->create_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| Template YAML | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
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
 **set_default_template** | **bool**| Specify true if Default Template is to be set | [optional] [default to false]
 **comments** | **str**| Comments | [optional] 
 **is_new_template** | **bool**| When isNewTemplate flag is set user will not be able to create a new version for an existing template | [optional] [default to false]

### Return type

[**ResponseDTOTemplateWrapperResponse**](ResponseDTOTemplateWrapperResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_template_version**
> ResponseDTOBoolean delete_template_version(account_identifier, template_identifier, version_label, if_match=if_match, org_identifier=org_identifier, project_identifier=project_identifier, branch=branch, repo_identifier=repo_identifier, root_folder=root_folder, file_path=file_path, commit_msg=commit_msg, last_object_id=last_object_id, comments=comments, force_delete=force_delete)

Delete Template Version

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: x-api-key
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TemplatesApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
template_identifier = 'template_identifier_example' # str | Template Identifier for the entity
version_label = 'version_label_example' # str | Version Label
if_match = 'if_match_example' # str |  (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
branch = 'branch_example' # str | Name of the branch. (optional)
repo_identifier = 'repo_identifier_example' # str | Git Sync Config Id. (optional)
root_folder = 'root_folder_example' # str | Path to the root folder of the Entity. (optional)
file_path = 'file_path_example' # str | File Path of the Entity. (optional)
commit_msg = 'commit_msg_example' # str | Commit Message to use for the merge commit. (optional)
last_object_id = 'last_object_id_example' # str | Last Object Id (optional)
comments = 'comments_example' # str |  (optional)
force_delete = false # bool | If true, the Entity will be forced delete, without checking any references/usages (optional) (default to false)

try:
    # Delete Template Version
    api_response = api_instance.delete_template_version(account_identifier, template_identifier, version_label, if_match=if_match, org_identifier=org_identifier, project_identifier=project_identifier, branch=branch, repo_identifier=repo_identifier, root_folder=root_folder, file_path=file_path, commit_msg=commit_msg, last_object_id=last_object_id, comments=comments, force_delete=force_delete)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->delete_template_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **template_identifier** | **str**| Template Identifier for the entity | 
 **version_label** | **str**| Version Label | 
 **if_match** | **str**|  | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **branch** | **str**| Name of the branch. | [optional] 
 **repo_identifier** | **str**| Git Sync Config Id. | [optional] 
 **root_folder** | **str**| Path to the root folder of the Entity. | [optional] 
 **file_path** | **str**| File Path of the Entity. | [optional] 
 **commit_msg** | **str**| Commit Message to use for the merge commit. | [optional] 
 **last_object_id** | **str**| Last Object Id | [optional] 
 **comments** | **str**|  | [optional] 
 **force_delete** | **bool**| If true, the Entity will be forced delete, without checking any references/usages | [optional] [default to false]

### Return type

[**ResponseDTOBoolean**](ResponseDTOBoolean.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_refreshed_yaml**
> ResponseDTORefreshResponse get_refreshed_yaml(body, account_identifier, load_from_cache=load_from_cache, org_identifier=org_identifier, project_identifier=project_identifier, branch=branch, repo_identifier=repo_identifier, get_default_from_other_repo=get_default_from_other_repo)

Get YAML with updated Template Inputs

Returns YAML with updated Template Inputs for a given YAML

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: x-api-key
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TemplatesApi(swagger_client.ApiClient(configuration))
body = swagger_client.RefreshRequestDTO() # RefreshRequestDTO | YAML
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
load_from_cache = 'false' # str |  (optional) (default to false)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
branch = 'branch_example' # str | Name of the branch. (optional)
repo_identifier = 'repo_identifier_example' # str | Git Sync Config Id. (optional)
get_default_from_other_repo = true # bool | if true, return all the default entities (optional)

try:
    # Get YAML with updated Template Inputs
    api_response = api_instance.get_refreshed_yaml(body, account_identifier, load_from_cache=load_from_cache, org_identifier=org_identifier, project_identifier=project_identifier, branch=branch, repo_identifier=repo_identifier, get_default_from_other_repo=get_default_from_other_repo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_refreshed_yaml: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RefreshRequestDTO**](RefreshRequestDTO.md)| YAML | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **load_from_cache** | **str**|  | [optional] [default to false]
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **branch** | **str**| Name of the branch. | [optional] 
 **repo_identifier** | **str**| Git Sync Config Id. | [optional] 
 **get_default_from_other_repo** | **bool**| if true, return all the default entities | [optional] 

### Return type

[**ResponseDTORefreshResponse**](ResponseDTORefreshResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template**
> ResponseDTOTemplateResponse get_template(account_identifier, template_identifier, org_identifier=org_identifier, project_identifier=project_identifier, version_label=version_label, deleted=deleted, branch=branch, repo_identifier=repo_identifier, get_default_from_other_repo=get_default_from_other_repo, load_from_cache=load_from_cache, load_from_fallback_branch=load_from_fallback_branch)

Get Template

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: x-api-key
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TemplatesApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
template_identifier = 'template_identifier_example' # str | Template Identifier for the entity
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
version_label = 'version_label_example' # str | Version Label (optional)
deleted = false # bool | Specifies whether Template is deleted or not (optional) (default to false)
branch = 'branch_example' # str | Name of the branch. (optional)
repo_identifier = 'repo_identifier_example' # str | Git Sync Config Id. (optional)
get_default_from_other_repo = true # bool | if true, return all the default entities (optional)
load_from_cache = 'false' # str |  (optional) (default to false)
load_from_fallback_branch = false # bool |  (optional) (default to false)

try:
    # Get Template
    api_response = api_instance.get_template(account_identifier, template_identifier, org_identifier=org_identifier, project_identifier=project_identifier, version_label=version_label, deleted=deleted, branch=branch, repo_identifier=repo_identifier, get_default_from_other_repo=get_default_from_other_repo, load_from_cache=load_from_cache, load_from_fallback_branch=load_from_fallback_branch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **template_identifier** | **str**| Template Identifier for the entity | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **version_label** | **str**| Version Label | [optional] 
 **deleted** | **bool**| Specifies whether Template is deleted or not | [optional] [default to false]
 **branch** | **str**| Name of the branch. | [optional] 
 **repo_identifier** | **str**| Git Sync Config Id. | [optional] 
 **get_default_from_other_repo** | **bool**| if true, return all the default entities | [optional] 
 **load_from_cache** | **str**|  | [optional] [default to false]
 **load_from_fallback_branch** | **bool**|  | [optional] [default to false]

### Return type

[**ResponseDTOTemplateResponse**](ResponseDTOTemplateResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template_input_set_yaml**
> ResponseDTOString get_template_input_set_yaml(account_identifier, template_identifier, version_label, org_identifier=org_identifier, project_identifier=project_identifier, load_from_cache=load_from_cache, branch=branch, repo_identifier=repo_identifier, get_default_from_other_repo=get_default_from_other_repo)

Gets Template Input Set YAML

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: x-api-key
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TemplatesApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
template_identifier = 'template_identifier_example' # str | Template Identifier for the entity
version_label = 'version_label_example' # str | Template Label
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
load_from_cache = 'false' # str |  (optional) (default to false)
branch = 'branch_example' # str | Name of the branch. (optional)
repo_identifier = 'repo_identifier_example' # str | Git Sync Config Id. (optional)
get_default_from_other_repo = true # bool | if true, return all the default entities (optional)

try:
    # Gets Template Input Set YAML
    api_response = api_instance.get_template_input_set_yaml(account_identifier, template_identifier, version_label, org_identifier=org_identifier, project_identifier=project_identifier, load_from_cache=load_from_cache, branch=branch, repo_identifier=repo_identifier, get_default_from_other_repo=get_default_from_other_repo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_template_input_set_yaml: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **template_identifier** | **str**| Template Identifier for the entity | 
 **version_label** | **str**| Template Label | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **load_from_cache** | **str**|  | [optional] [default to false]
 **branch** | **str**| Name of the branch. | [optional] 
 **repo_identifier** | **str**| Git Sync Config Id. | [optional] 
 **get_default_from_other_repo** | **bool**| if true, return all the default entities | [optional] 

### Return type

[**ResponseDTOString**](ResponseDTOString.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template_metadata_list**
> ResponseDTOPageTemplateMetadataSummaryResponse get_template_metadata_list(account_identifier, template_list_type, body=body, org_identifier=org_identifier, project_identifier=project_identifier, page=page, size=size, sort=sort, search_term=search_term, filter_identifier=filter_identifier, include_all_templates_available_at_scope=include_all_templates_available_at_scope, get_distinct_from_branches=get_distinct_from_branches)

Gets all metadata of template list

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: x-api-key
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TemplatesApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
template_list_type = 'template_list_type_example' # str | Template List Type
body = swagger_client.TemplateFilterProperties() # TemplateFilterProperties | This contains details of Template filters based on Template Types and Template Names  (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
page = 0 # int | Page Index of the results to fetch.Default Value: 0 (optional) (default to 0)
size = 25 # int | Results per page (optional) (default to 25)
sort = ['sort_example'] # list[str] | Specifies sorting criteria of the list. Like sorting based on the last updated entity, alphabetical sorting in an ascending or descending order (optional)
search_term = 'search_term_example' # str | The word to be searched and included in the list response (optional)
filter_identifier = 'filter_identifier_example' # str | Filter Identifier (optional)
include_all_templates_available_at_scope = true # bool | Specify true if all accessible Templates are to be included (optional)
get_distinct_from_branches = true # bool |  (optional)

try:
    # Gets all metadata of template list
    api_response = api_instance.get_template_metadata_list(account_identifier, template_list_type, body=body, org_identifier=org_identifier, project_identifier=project_identifier, page=page, size=size, sort=sort, search_term=search_term, filter_identifier=filter_identifier, include_all_templates_available_at_scope=include_all_templates_available_at_scope, get_distinct_from_branches=get_distinct_from_branches)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_template_metadata_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **template_list_type** | **str**| Template List Type | 
 **body** | [**TemplateFilterProperties**](TemplateFilterProperties.md)| This contains details of Template filters based on Template Types and Template Names  | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **page** | **int**| Page Index of the results to fetch.Default Value: 0 | [optional] [default to 0]
 **size** | **int**| Results per page | [optional] [default to 25]
 **sort** | [**list[str]**](str.md)| Specifies sorting criteria of the list. Like sorting based on the last updated entity, alphabetical sorting in an ascending or descending order | [optional] 
 **search_term** | **str**| The word to be searched and included in the list response | [optional] 
 **filter_identifier** | **str**| Filter Identifier | [optional] 
 **include_all_templates_available_at_scope** | **bool**| Specify true if all accessible Templates are to be included | [optional] 
 **get_distinct_from_branches** | **bool**|  | [optional] 

### Return type

[**ResponseDTOPageTemplateMetadataSummaryResponse**](ResponseDTOPageTemplateMetadataSummaryResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_template_configs**
> ResponseDTOTemplateMoveConfigResponse move_template_configs(account_identifier, template_identifier, version_label, org_identifier=org_identifier, project_identifier=project_identifier, connector_ref=connector_ref, repo_name=repo_name, branch=branch, file_path=file_path, commit_msg=commit_msg, is_new_branch=is_new_branch, base_branch=base_branch, move_config_type=move_config_type)

Move Template YAML from inline to remote

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: x-api-key
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TemplatesApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
template_identifier = 'template_identifier_example' # str | Template Identifier for the entity
version_label = 'version_label_example' # str | Version Label
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
connector_ref = 'connector_ref_example' # str | Identifier of Connector needed for CRUD operations on the respective Entity (optional)
repo_name = 'repo_name_example' # str | Name of the repository. (optional)
branch = 'branch_example' # str | Name of the branch. (optional)
file_path = 'file_path_example' # str | File Path of the Entity. (optional)
commit_msg = 'commit_msg_example' # str | File Path of the Entity. (optional)
is_new_branch = false # bool | Checks the new branch (optional) (default to false)
base_branch = 'base_branch_example' # str | Name of the default branch. (optional)
move_config_type = 'move_config_type_example' # str | Tells weather the entity has to be moved from inline to remote or remote to inline (optional)

try:
    # Move Template YAML from inline to remote
    api_response = api_instance.move_template_configs(account_identifier, template_identifier, version_label, org_identifier=org_identifier, project_identifier=project_identifier, connector_ref=connector_ref, repo_name=repo_name, branch=branch, file_path=file_path, commit_msg=commit_msg, is_new_branch=is_new_branch, base_branch=base_branch, move_config_type=move_config_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->move_template_configs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **template_identifier** | **str**| Template Identifier for the entity | 
 **version_label** | **str**| Version Label | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **connector_ref** | **str**| Identifier of Connector needed for CRUD operations on the respective Entity | [optional] 
 **repo_name** | **str**| Name of the repository. | [optional] 
 **branch** | **str**| Name of the branch. | [optional] 
 **file_path** | **str**| File Path of the Entity. | [optional] 
 **commit_msg** | **str**| File Path of the Entity. | [optional] 
 **is_new_branch** | **bool**| Checks the new branch | [optional] [default to false]
 **base_branch** | **str**| Name of the default branch. | [optional] 
 **move_config_type** | **str**| Tells weather the entity has to be moved from inline to remote or remote to inline | [optional] 

### Return type

[**ResponseDTOTemplateMoveConfigResponse**](ResponseDTOTemplateMoveConfigResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templatevalidate_template_inputs**
> TemplateResponseDTOValidateTemplateInputsResponseDTO templatevalidate_template_inputs(account_identifier, template_identifier, version_label, org_identifier=org_identifier, project_identifier=project_identifier, load_from_cache=load_from_cache, branch=branch, repo_identifier=repo_identifier, get_default_from_other_repo=get_default_from_other_repo)

Validate Template Inputs in a YAML

Validates the Template Inputs in a pipeline's YAML specification. If the Template Inputs are invalid, the operation returns an error summary.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: x-api-key
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TemplatesApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
template_identifier = 'template_identifier_example' # str | Template Identifier for the entity
version_label = 'version_label_example' # str | Template version
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
load_from_cache = 'false' # str |  (optional) (default to false)
branch = 'branch_example' # str | Name of the branch. (optional)
repo_identifier = 'repo_identifier_example' # str | Git Sync Config Id. (optional)
get_default_from_other_repo = true # bool | if true, return all the default entities (optional)

try:
    # Validate Template Inputs in a YAML
    api_response = api_instance.templatevalidate_template_inputs(account_identifier, template_identifier, version_label, org_identifier=org_identifier, project_identifier=project_identifier, load_from_cache=load_from_cache, branch=branch, repo_identifier=repo_identifier, get_default_from_other_repo=get_default_from_other_repo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->templatevalidate_template_inputs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **template_identifier** | **str**| Template Identifier for the entity | 
 **version_label** | **str**| Template version | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **load_from_cache** | **str**|  | [optional] [default to false]
 **branch** | **str**| Name of the branch. | [optional] 
 **repo_identifier** | **str**| Git Sync Config Id. | [optional] 
 **get_default_from_other_repo** | **bool**| if true, return all the default entities | [optional] 

### Return type

[**TemplateResponseDTOValidateTemplateInputsResponseDTO**](TemplateResponseDTOValidateTemplateInputsResponseDTO.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_existing_template_version**
> ResponseDTOTemplateWrapperResponse update_existing_template_version(body, account_identifier, template_identifier, version_label, if_match=if_match, org_identifier=org_identifier, project_identifier=project_identifier, branch=branch, repo_identifier=repo_identifier, root_folder=root_folder, file_path=file_path, commit_msg=commit_msg, last_object_id=last_object_id, resolved_conflict_commit_id=resolved_conflict_commit_id, base_branch=base_branch, connector_ref=connector_ref, is_new_branch=is_new_branch, set_default_template=set_default_template, comments=comments)

Update Template Version

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: x-api-key
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TemplatesApi(swagger_client.ApiClient(configuration))
body = '{   \"summary\" : \"Sample Update Template YAML\",   \"description\" : \"Sample Template YAML\",   \"value\" : \"template:\\n  name: pipelineTemplate\\n  identifier: pipelineTemplate\\n  versionLabel: v1\\n  type: Pipeline\\n  projectIdentifier: TemplateDemo\\n  orgIdentifier: default\\n  tags: {}\\n  spec:\\n    stages:\\n      - stage:\\n          name: stage1\\n          identifier: stage1\\n          description: \\\"\\\"\\n          type: Deployment\\n          spec:\\n            deploymentType: Kubernetes\\n            service:\\n              serviceRef: <+input>\\n              serviceInputs: <+input>\\n            environment:\\n              environmentRef: <+input>\\n              deployToAll: false\\n              environmentInputs: <+input>\\n              infrastructureDefinitions: <+input>\\n            execution:\\n              steps:\\n                - step:\\n                    type: ShellScript\\n                    name: Shell Script_1\\n                    identifier: ShellScript_1\\n                    spec:\\n                      shell: Bash\\n                      onDelegate: true\\n                      source:\\n                        type: Inline\\n                        spec:\\n                          script: <+input>\\n                      environmentVariables: []\\n                      outputVariables: []\\n                    timeout: 10m\\n              rollbackSteps: []\\n          tags: {}\\n          failureStrategies:\\n            - onFailure:\\n                errors:\\n                  - AllErrors\\n                action:\\n                  type: StageRollback\\n\" }' # str | Template YAML
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
template_identifier = 'template_identifier_example' # str | Template Identifier for the entity
version_label = 'version_label_example' # str | Version Label
if_match = 'if_match_example' # str |  (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
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
set_default_template = false # bool | Specify true if Default Template is to be set (optional) (default to false)
comments = 'comments_example' # str | Comments (optional)

try:
    # Update Template Version
    api_response = api_instance.update_existing_template_version(body, account_identifier, template_identifier, version_label, if_match=if_match, org_identifier=org_identifier, project_identifier=project_identifier, branch=branch, repo_identifier=repo_identifier, root_folder=root_folder, file_path=file_path, commit_msg=commit_msg, last_object_id=last_object_id, resolved_conflict_commit_id=resolved_conflict_commit_id, base_branch=base_branch, connector_ref=connector_ref, is_new_branch=is_new_branch, set_default_template=set_default_template, comments=comments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->update_existing_template_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| Template YAML | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **template_identifier** | **str**| Template Identifier for the entity | 
 **version_label** | **str**| Version Label | 
 **if_match** | **str**|  | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
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
 **set_default_template** | **bool**| Specify true if Default Template is to be set | [optional] [default to false]
 **comments** | **str**| Comments | [optional] 

### Return type

[**ResponseDTOTemplateWrapperResponse**](ResponseDTOTemplateWrapperResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_git_details**
> ResponseDTOTemplateUpdateGitDetailsResponse update_git_details(account_identifier, template_identifier, version_label, body=body, org_identifier=org_identifier, project_identifier=project_identifier)

Update git metadata details for a remote template

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: x-api-key
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TemplatesApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
template_identifier = 'template_identifier_example' # str | Template Identifier for the entity
version_label = 'version_label_example' # str | Version Label
body = swagger_client.TemplateUpdateGitDetailsRequest() # TemplateUpdateGitDetailsRequest | This contains details of Git Entity like Git Branch info to be updated (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Update git metadata details for a remote template
    api_response = api_instance.update_git_details(account_identifier, template_identifier, version_label, body=body, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->update_git_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **template_identifier** | **str**| Template Identifier for the entity | 
 **version_label** | **str**| Version Label | 
 **body** | [**TemplateUpdateGitDetailsRequest**](TemplateUpdateGitDetailsRequest.md)| This contains details of Git Entity like Git Branch info to be updated | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOTemplateUpdateGitDetailsResponse**](ResponseDTOTemplateUpdateGitDetailsResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_stable_template**
> ResponseDTOString update_stable_template(account_identifier, template_identifier, version_label, org_identifier=org_identifier, project_identifier=project_identifier, branch=branch, repo_identifier=repo_identifier, get_default_from_other_repo=get_default_from_other_repo, comments=comments)

Update Stable Template Version

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: x-api-key
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TemplatesApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
template_identifier = 'template_identifier_example' # str | Template Identifier for the entity
version_label = 'version_label_example' # str | Version Label
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
branch = 'branch_example' # str | Name of the branch. (optional)
repo_identifier = 'repo_identifier_example' # str | Git Sync Config Id. (optional)
get_default_from_other_repo = true # bool | if true, return all the default entities (optional)
comments = 'comments_example' # str | Comments (optional)

try:
    # Update Stable Template Version
    api_response = api_instance.update_stable_template(account_identifier, template_identifier, version_label, org_identifier=org_identifier, project_identifier=project_identifier, branch=branch, repo_identifier=repo_identifier, get_default_from_other_repo=get_default_from_other_repo, comments=comments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->update_stable_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **template_identifier** | **str**| Template Identifier for the entity | 
 **version_label** | **str**| Version Label | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **branch** | **str**| Name of the branch. | [optional] 
 **repo_identifier** | **str**| Git Sync Config Id. | [optional] 
 **get_default_from_other_repo** | **bool**| if true, return all the default entities | [optional] 
 **comments** | **str**| Comments | [optional] 

### Return type

[**ResponseDTOString**](ResponseDTOString.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

