# harness_python_sdk.PipelineExecutionDetailsApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_execution_detail**](PipelineExecutionDetailsApi.md#get_execution_detail) | **GET** /pipeline/api/pipelines/execution/{planExecutionId} | Fetch Execution Details
[**get_execution_detail_v2**](PipelineExecutionDetailsApi.md#get_execution_detail_v2) | **GET** /pipeline/api/pipelines/execution/v2/{planExecutionId} | Fetch Execution Details
[**get_execution_sub_graph_for_node_execution**](PipelineExecutionDetailsApi.md#get_execution_sub_graph_for_node_execution) | **GET** /pipeline/api/pipelines/execution/subGraph/{planExecutionId}/{nodeExecutionId} | Fetch Execution SubGraph for a Given NodeExecution ID
[**get_inputset_yaml_v2**](PipelineExecutionDetailsApi.md#get_inputset_yaml_v2) | **GET** /pipeline/api/pipelines/execution/{planExecutionId}/inputsetV2 | Get the Input Set YAML used for given Plan Execution
[**get_list_of_execution_identifier**](PipelineExecutionDetailsApi.md#get_list_of_execution_identifier) | **POST** /pipeline/api/pipelines/execution/executionSummary | List Execution Identifier
[**get_list_of_executions**](PipelineExecutionDetailsApi.md#get_list_of_executions) | **POST** /pipeline/api/pipelines/execution/summary | List Executions
[**get_notes_for_execution**](PipelineExecutionDetailsApi.md#get_notes_for_execution) | **GET** /pipeline/api/pipelines/execution/{planExecutionId}/notes | Get Notes for a pipelineExecution
[**update_notes_for_execution**](PipelineExecutionDetailsApi.md#update_notes_for_execution) | **PUT** /pipeline/api/pipelines/execution/{planExecutionId}/notes | Updates Notes for a pipelineExecution

# **get_execution_detail**
> ResponseDTOPipelineExecutionDetail get_execution_detail(account_identifier, org_identifier, project_identifier, plan_execution_id, stage_node_id=stage_node_id, stage_node_execution_id=stage_node_execution_id)

Fetch Execution Details

Returns the Pipeline Execution Details for a Given PlanExecution ID

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
api_instance = harness_python_sdk.PipelineExecutionDetailsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
plan_execution_id = 'plan_execution_id_example' # str | Plan Execution Id for which we want to get the Execution details
stage_node_id = 'stage_node_id_example' # str | Stage Node Identifier for which Stage Graph needs to be Rendered (optional)
stage_node_execution_id = 'stage_node_execution_id_example' # str | Stage Node Execution ID for which Stage Graph needs to be Rendered. (Needed only when there are Multiple Runs for a Given Stage. It can be Extracted from LayoutNodeMap Field) (optional)

try:
    # Fetch Execution Details
    api_response = api_instance.get_execution_detail(account_identifier, org_identifier, project_identifier, plan_execution_id, stage_node_id=stage_node_id, stage_node_execution_id=stage_node_execution_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineExecutionDetailsApi->get_execution_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **plan_execution_id** | **str**| Plan Execution Id for which we want to get the Execution details | 
 **stage_node_id** | **str**| Stage Node Identifier for which Stage Graph needs to be Rendered | [optional] 
 **stage_node_execution_id** | **str**| Stage Node Execution ID for which Stage Graph needs to be Rendered. (Needed only when there are Multiple Runs for a Given Stage. It can be Extracted from LayoutNodeMap Field) | [optional] 

### Return type

[**ResponseDTOPipelineExecutionDetail**](ResponseDTOPipelineExecutionDetail.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_execution_detail_v2**
> ResponseDTOPipelineExecutionDetail get_execution_detail_v2(account_identifier, org_identifier, project_identifier, plan_execution_id, stage_node_id=stage_node_id, stage_node_execution_id=stage_node_execution_id, child_stage_node_id=child_stage_node_id, render_full_bottom_graph=render_full_bottom_graph)

Fetch Execution Details

Returns the Pipeline Execution Details for a Given PlanExecution ID

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
api_instance = harness_python_sdk.PipelineExecutionDetailsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
plan_execution_id = 'plan_execution_id_example' # str | Plan Execution Id for which we want to get the Execution details
stage_node_id = 'stage_node_id_example' # str | Stage Node Identifier for which Stage Graph needs to be Rendered (optional)
stage_node_execution_id = 'stage_node_execution_id_example' # str | Stage Node Execution ID for which Stage Graph needs to be Rendered. (Needed only when there are Multiple Runs for a Given Stage. It can be Extracted from LayoutNodeMap Field) (optional)
child_stage_node_id = 'child_stage_node_id_example' # str | Stage Node Execution ID for which Stage Graph needs to be Rendered. (Needed only when there are Multiple Runs for a Given Stage. It can be Extracted from LayoutNodeMap Field) (optional)
render_full_bottom_graph = true # bool | Generate Graph for all the Stages including Steps in each Stage (optional)

try:
    # Fetch Execution Details
    api_response = api_instance.get_execution_detail_v2(account_identifier, org_identifier, project_identifier, plan_execution_id, stage_node_id=stage_node_id, stage_node_execution_id=stage_node_execution_id, child_stage_node_id=child_stage_node_id, render_full_bottom_graph=render_full_bottom_graph)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineExecutionDetailsApi->get_execution_detail_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **plan_execution_id** | **str**| Plan Execution Id for which we want to get the Execution details | 
 **stage_node_id** | **str**| Stage Node Identifier for which Stage Graph needs to be Rendered | [optional] 
 **stage_node_execution_id** | **str**| Stage Node Execution ID for which Stage Graph needs to be Rendered. (Needed only when there are Multiple Runs for a Given Stage. It can be Extracted from LayoutNodeMap Field) | [optional] 
 **child_stage_node_id** | **str**| Stage Node Execution ID for which Stage Graph needs to be Rendered. (Needed only when there are Multiple Runs for a Given Stage. It can be Extracted from LayoutNodeMap Field) | [optional] 
 **render_full_bottom_graph** | **bool**| Generate Graph for all the Stages including Steps in each Stage | [optional] 

### Return type

[**ResponseDTOPipelineExecutionDetail**](ResponseDTOPipelineExecutionDetail.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_execution_sub_graph_for_node_execution**
> ResponseDTONodeExecutionDetails get_execution_sub_graph_for_node_execution(account_identifier, org_identifier, project_identifier, node_execution_id, plan_execution_id)

Fetch Execution SubGraph for a Given NodeExecution ID

Returns the Pipeline Execution SubGraph for a Given NodeExecution ID

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
api_instance = harness_python_sdk.PipelineExecutionDetailsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
node_execution_id = 'node_execution_id_example' # str | Node Execution Id for which we want to get the Execution SubGraph
plan_execution_id = 'plan_execution_id_example' # str | Plan Execution Id for which we want to get the Execution details

try:
    # Fetch Execution SubGraph for a Given NodeExecution ID
    api_response = api_instance.get_execution_sub_graph_for_node_execution(account_identifier, org_identifier, project_identifier, node_execution_id, plan_execution_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineExecutionDetailsApi->get_execution_sub_graph_for_node_execution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **node_execution_id** | **str**| Node Execution Id for which we want to get the Execution SubGraph | 
 **plan_execution_id** | **str**| Plan Execution Id for which we want to get the Execution details | 

### Return type

[**ResponseDTONodeExecutionDetails**](ResponseDTONodeExecutionDetails.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inputset_yaml_v2**
> ResponseDTOInputSetTemplateResponse get_inputset_yaml_v2(account_identifier, org_identifier, project_identifier, plan_execution_id, resolve_expressions=resolve_expressions, resolve_expressions_type=resolve_expressions_type)

Get the Input Set YAML used for given Plan Execution

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
api_instance = harness_python_sdk.PipelineExecutionDetailsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
plan_execution_id = 'plan_execution_id_example' # str | Plan Execution Id for which we want to get the Input Set YAML
resolve_expressions = false # bool | A boolean that indicates whether or not expressions should be resolved in input set yaml  (optional) (default to false)
resolve_expressions_type = 'UNKNOWN' # str | Resolve Expressions Type indicates what kind of expressions should be resolved in input set yaml. The default value is UNKNOWN in which case no expressions will be resolvedChoose a value from the enum list: [RESOLVE_ALL_EXPRESSIONS, RESOLVE_TRIGGER_EXPRESSIONS, UNKNOWN] (optional) (default to UNKNOWN)

try:
    # Get the Input Set YAML used for given Plan Execution
    api_response = api_instance.get_inputset_yaml_v2(account_identifier, org_identifier, project_identifier, plan_execution_id, resolve_expressions=resolve_expressions, resolve_expressions_type=resolve_expressions_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineExecutionDetailsApi->get_inputset_yaml_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **plan_execution_id** | **str**| Plan Execution Id for which we want to get the Input Set YAML | 
 **resolve_expressions** | **bool**| A boolean that indicates whether or not expressions should be resolved in input set yaml  | [optional] [default to false]
 **resolve_expressions_type** | **str**| Resolve Expressions Type indicates what kind of expressions should be resolved in input set yaml. The default value is UNKNOWN in which case no expressions will be resolvedChoose a value from the enum list: [RESOLVE_ALL_EXPRESSIONS, RESOLVE_TRIGGER_EXPRESSIONS, UNKNOWN] | [optional] [default to UNKNOWN]

### Return type

[**ResponseDTOInputSetTemplateResponse**](ResponseDTOInputSetTemplateResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_of_execution_identifier**
> ResponseDTOPagePipelineExecutionIdentifierSummary get_list_of_execution_identifier(account_identifier, org_identifier, project_identifier, pipeline_identifier=pipeline_identifier, page=page, size=size, branch=branch, repo_identifier=repo_identifier, get_default_from_other_repo=get_default_from_other_repo)

List Execution Identifier

Returns a List of Pipeline Executions Identifier with Specific Filter

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
api_instance = harness_python_sdk.PipelineExecutionDetailsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
pipeline_identifier = 'pipeline_identifier_example' # str | Pipeline Identifier filter if exact pipelines needs to be filtered. (optional)
page = 0 # int | Page Index of the results to fetch.Default Value: 0 (optional) (default to 0)
size = 10 # int | Results per page (optional) (default to 10)
branch = 'branch_example' # str | Name of the branch. (optional)
repo_identifier = 'repo_identifier_example' # str | Git Sync Config Id. (optional)
get_default_from_other_repo = true # bool | if true, return all the default entities (optional)

try:
    # List Execution Identifier
    api_response = api_instance.get_list_of_execution_identifier(account_identifier, org_identifier, project_identifier, pipeline_identifier=pipeline_identifier, page=page, size=size, branch=branch, repo_identifier=repo_identifier, get_default_from_other_repo=get_default_from_other_repo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineExecutionDetailsApi->get_list_of_execution_identifier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **pipeline_identifier** | **str**| Pipeline Identifier filter if exact pipelines needs to be filtered. | [optional] 
 **page** | **int**| Page Index of the results to fetch.Default Value: 0 | [optional] [default to 0]
 **size** | **int**| Results per page | [optional] [default to 10]
 **branch** | **str**| Name of the branch. | [optional] 
 **repo_identifier** | **str**| Git Sync Config Id. | [optional] 
 **get_default_from_other_repo** | **bool**| if true, return all the default entities | [optional] 

### Return type

[**ResponseDTOPagePipelineExecutionIdentifierSummary**](ResponseDTOPagePipelineExecutionIdentifierSummary.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_of_executions**
> ResponseDTOPagePipelineExecutionSummary get_list_of_executions(account_identifier, org_identifier, project_identifier, body=body, search_term=search_term, pipeline_identifier=pipeline_identifier, page=page, size=size, sort=sort, filter_identifier=filter_identifier, show_all_executions=show_all_executions, module=module, status=status, my_deployments=my_deployments, branch=branch, repo_identifier=repo_identifier, get_default_from_other_repo=get_default_from_other_repo)

List Executions

Returns a List of Pipeline Executions with Specific Filter

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
api_instance = harness_python_sdk.PipelineExecutionDetailsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
body = harness_python_sdk.FilterProperties() # FilterProperties | Returns a List of Pipeline Executions with Specific Filters (optional)
search_term = 'search_term_example' # str | Search term to filter out pipelines based on pipeline name, identifier, tags. (optional)
pipeline_identifier = 'pipeline_identifier_example' # str | Pipeline Identifier filter if exact pipelines needs to be filtered. (optional)
page = 0 # int | Page Index of the results to fetch.Default Value: 0 (optional) (default to 0)
size = 10 # int | Results per page (optional) (default to 10)
sort = ['sort_example'] # list[str] | Sort criteria for the elements. (optional)
filter_identifier = 'filter_identifier_example' # str |  (optional)
show_all_executions = false # bool |  (optional) (default to false)
module = 'module_example' # str |  (optional)
status = ['status_example'] # list[str] |  (optional)
my_deployments = true # bool |  (optional)
branch = 'branch_example' # str | Name of the branch. (optional)
repo_identifier = 'repo_identifier_example' # str | Git Sync Config Id. (optional)
get_default_from_other_repo = true # bool | if true, return all the default entities (optional)

try:
    # List Executions
    api_response = api_instance.get_list_of_executions(account_identifier, org_identifier, project_identifier, body=body, search_term=search_term, pipeline_identifier=pipeline_identifier, page=page, size=size, sort=sort, filter_identifier=filter_identifier, show_all_executions=show_all_executions, module=module, status=status, my_deployments=my_deployments, branch=branch, repo_identifier=repo_identifier, get_default_from_other_repo=get_default_from_other_repo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineExecutionDetailsApi->get_list_of_executions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **body** | [**FilterProperties**](FilterProperties.md)| Returns a List of Pipeline Executions with Specific Filters | [optional] 
 **search_term** | **str**| Search term to filter out pipelines based on pipeline name, identifier, tags. | [optional] 
 **pipeline_identifier** | **str**| Pipeline Identifier filter if exact pipelines needs to be filtered. | [optional] 
 **page** | **int**| Page Index of the results to fetch.Default Value: 0 | [optional] [default to 0]
 **size** | **int**| Results per page | [optional] [default to 10]
 **sort** | [**list[str]**](str.md)| Sort criteria for the elements. | [optional] 
 **filter_identifier** | **str**|  | [optional] 
 **show_all_executions** | **bool**|  | [optional] [default to false]
 **module** | **str**|  | [optional] 
 **status** | [**list[str]**](str.md)|  | [optional] 
 **my_deployments** | **bool**|  | [optional] 
 **branch** | **str**| Name of the branch. | [optional] 
 **repo_identifier** | **str**| Git Sync Config Id. | [optional] 
 **get_default_from_other_repo** | **bool**| if true, return all the default entities | [optional] 

### Return type

[**ResponseDTOPagePipelineExecutionSummary**](ResponseDTOPagePipelineExecutionSummary.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notes_for_execution**
> ResponseDTOPipelineExecutionNotes get_notes_for_execution(account_identifier, plan_execution_id)

Get Notes for a pipelineExecution

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
api_instance = harness_python_sdk.PipelineExecutionDetailsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
plan_execution_id = 'plan_execution_id_example' # str | ExecutionId of the execution for which we want to get notes

try:
    # Get Notes for a pipelineExecution
    api_response = api_instance.get_notes_for_execution(account_identifier, plan_execution_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineExecutionDetailsApi->get_notes_for_execution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **plan_execution_id** | **str**| ExecutionId of the execution for which we want to get notes | 

### Return type

[**ResponseDTOPipelineExecutionNotes**](ResponseDTOPipelineExecutionNotes.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_notes_for_execution**
> ResponseDTOPipelineExecutionNotes update_notes_for_execution(account_identifier, org_identifier, project_identifier, notes_for_pipeline_execution, plan_execution_id)

Updates Notes for a pipelineExecution

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
api_instance = harness_python_sdk.PipelineExecutionDetailsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
notes_for_pipeline_execution = 'notes_for_pipeline_execution_example' # str | Notes of a Pipeline Execution
plan_execution_id = 'plan_execution_id_example' # str | ExecutionId of the execution for which we want to update notes

try:
    # Updates Notes for a pipelineExecution
    api_response = api_instance.update_notes_for_execution(account_identifier, org_identifier, project_identifier, notes_for_pipeline_execution, plan_execution_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineExecutionDetailsApi->update_notes_for_execution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **notes_for_pipeline_execution** | **str**| Notes of a Pipeline Execution | 
 **plan_execution_id** | **str**| ExecutionId of the execution for which we want to update notes | 

### Return type

[**ResponseDTOPipelineExecutionNotes**](ResponseDTOPipelineExecutionNotes.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

