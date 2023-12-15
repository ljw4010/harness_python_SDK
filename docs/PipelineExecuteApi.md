# swagger_client.PipelineExecuteApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**handle_stage_interrupt**](PipelineExecuteApi.md#handle_stage_interrupt) | **PUT** /pipeline/api/pipeline/execute/interrupt/{planExecutionId}/{nodeExecutionId} | Handles the interrupt for a given stage in a pipeline
[**post_pipeline_execute_with_input_set_list**](PipelineExecuteApi.md#post_pipeline_execute_with_input_set_list) | **POST** /pipeline/api/pipeline/execute/{identifier}/inputSetList | Execute a Pipeline with Input Set References
[**post_pipeline_execute_with_input_set_yaml**](PipelineExecuteApi.md#post_pipeline_execute_with_input_set_yaml) | **POST** /pipeline/api/pipeline/execute/{identifier} | Execute a Pipeline with Runtime Input YAML
[**put_handle_interrupt**](PipelineExecuteApi.md#put_handle_interrupt) | **PUT** /pipeline/api/pipeline/execute/interrupt/{planExecutionId} | Execute an Interrupt
[**retry_history**](PipelineExecuteApi.md#retry_history) | **GET** /pipeline/api/pipeline/execute/retryHistory/{planExecutionId} | Retry History for a given execution
[**retry_pipeline**](PipelineExecuteApi.md#retry_pipeline) | **POST** /pipeline/api/pipeline/execute/retry/{identifier} | Retry a executed pipeline with inputSet pipeline yaml

# **handle_stage_interrupt**
> ResponseDTOInterruptResponse handle_stage_interrupt(account_identifier, org_identifier, project_identifier, interrupt_type, plan_execution_id, node_execution_id)

Handles the interrupt for a given stage in a pipeline

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
api_instance = swagger_client.PipelineExecuteApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
interrupt_type = 'interrupt_type_example' # str | The Interrupt type needed to be applied to the execution. Choose a value from the enum list.
plan_execution_id = 'plan_execution_id_example' # str | The Pipeline Execution Id on which the Interrupt needs to be applied.
node_execution_id = 'node_execution_id_example' # str | The runtime Id of the step/stage on which the Interrupt needs to be applied.

try:
    # Handles the interrupt for a given stage in a pipeline
    api_response = api_instance.handle_stage_interrupt(account_identifier, org_identifier, project_identifier, interrupt_type, plan_execution_id, node_execution_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineExecuteApi->handle_stage_interrupt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **interrupt_type** | **str**| The Interrupt type needed to be applied to the execution. Choose a value from the enum list. | 
 **plan_execution_id** | **str**| The Pipeline Execution Id on which the Interrupt needs to be applied. | 
 **node_execution_id** | **str**| The runtime Id of the step/stage on which the Interrupt needs to be applied. | 

### Return type

[**ResponseDTOInterruptResponse**](ResponseDTOInterruptResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_pipeline_execute_with_input_set_list**
> ResponseDTOPlanExecutionResponse post_pipeline_execute_with_input_set_list(body, account_identifier, org_identifier, project_identifier, identifier, module_type=module_type, branch=branch, repo_identifier=repo_identifier, get_default_from_other_repo=get_default_from_other_repo, use_fqnif_error=use_fqnif_error, notes_for_pipeline_execution=notes_for_pipeline_execution)

Execute a Pipeline with Input Set References

Execute a Pipeline with Input Set References

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
api_instance = swagger_client.PipelineExecuteApi(swagger_client.ApiClient(configuration))
body = swagger_client.MergeInputSetRequest() # MergeInputSetRequest | 
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
identifier = 'identifier_example' # str | Pipeline identifier for the entity. Identifier of the Pipeline to be executed
module_type = 'module_type_example' # str | Module type for the entity. If its from deployments,type will be CD , if its from build type will be CI (optional)
branch = 'branch_example' # str | Name of the branch. (optional)
repo_identifier = 'repo_identifier_example' # str | Git Sync Config Id. (optional)
get_default_from_other_repo = true # bool | if true, return all the default entities (optional)
use_fqnif_error = false # bool |  (optional) (default to false)
notes_for_pipeline_execution = '' # str | Notes of a pipeline execution (optional)

try:
    # Execute a Pipeline with Input Set References
    api_response = api_instance.post_pipeline_execute_with_input_set_list(body, account_identifier, org_identifier, project_identifier, identifier, module_type=module_type, branch=branch, repo_identifier=repo_identifier, get_default_from_other_repo=get_default_from_other_repo, use_fqnif_error=use_fqnif_error, notes_for_pipeline_execution=notes_for_pipeline_execution)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineExecuteApi->post_pipeline_execute_with_input_set_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MergeInputSetRequest**](MergeInputSetRequest.md)|  | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **identifier** | **str**| Pipeline identifier for the entity. Identifier of the Pipeline to be executed | 
 **module_type** | **str**| Module type for the entity. If its from deployments,type will be CD , if its from build type will be CI | [optional] 
 **branch** | **str**| Name of the branch. | [optional] 
 **repo_identifier** | **str**| Git Sync Config Id. | [optional] 
 **get_default_from_other_repo** | **bool**| if true, return all the default entities | [optional] 
 **use_fqnif_error** | **bool**|  | [optional] [default to false]
 **notes_for_pipeline_execution** | **str**| Notes of a pipeline execution | [optional] 

### Return type

[**ResponseDTOPlanExecutionResponse**](ResponseDTOPlanExecutionResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_pipeline_execute_with_input_set_yaml**
> ResponseDTOPlanExecutionResponse post_pipeline_execute_with_input_set_yaml(account_identifier, org_identifier, project_identifier, identifier, body=body, module_type=module_type, branch=branch, repo_identifier=repo_identifier, get_default_from_other_repo=get_default_from_other_repo, use_fqnif_error=use_fqnif_error, notify_only_user=notify_only_user, notes_for_pipeline_execution=notes_for_pipeline_execution)

Execute a Pipeline with Runtime Input YAML

Execute a Pipeline with Runtime Input YAML

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
api_instance = swagger_client.PipelineExecuteApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
identifier = 'identifier_example' # str | Pipeline identifier for the entity. Identifier of the Pipeline to be executed
body = '{   \"summary\" : \"Execute Pipeline with Runtime Input YAML\",   \"description\" : \"Execute Runtime Input YAML\",   \"value\" : \"pipeline:\\n  identifier: \\\"Sample_Pipeline\\\"\\n  stages:\\n      - stage:\\n          identifier: \\\"Sample_Stage\\\"\\n          type: \\\"Approval\\\"\\n          spec:\\n              execution:\\n                  steps:\\n                      - step:\\n                          identifier: \\\"Approval_Step\\\"\\n                          type: \\\"HarnessApproval\\\"\\n                          spec:\\n                            approvers:\\n                              userGroups: \\n                                - account._account_all_users:\\n                      - step:\\n                          identifier: \\\"Shellscript_Step\\\"\\n                          type: \\\"ShellScript\\\"\\n                          spec:\\n                            source:\\n                              type: \\\"Inline\\\"\\n                              spec:\\n                                script: \\\"exit 0\\\"\\n      - stage:\\n          identifier: \\\"Sample_Deploy_Stage\\\"\\n          type: \\\"Deployment\\\"\\n          spec:\\n            serviceConfig:\\n              serviceRef: \\\"service1\\\"\\n            infrastructure:\\n                environmentRef: \\\"env1\\\"\\n                infrastructureDefinition:\\n                              type: \\\"KubernetesDirect\\\"\\n                              spec:\\n                                connectorRef: \\\"KubernetesConnector>\\\"\\n                                namespace: \\\"default\\\"\\n\" }' # str | Enter Runtime Input YAML if the Pipeline contains Runtime Inputs. Template for this can be Fetched from /inputSets/template API. (optional)
module_type = 'module_type_example' # str | Module type for the entity. If its from deployments,type will be CD , if its from build type will be CI (optional)
branch = 'branch_example' # str | Name of the branch. (optional)
repo_identifier = 'repo_identifier_example' # str | Git Sync Config Id. (optional)
get_default_from_other_repo = true # bool | if true, return all the default entities (optional)
use_fqnif_error = false # bool |  (optional) (default to false)
notify_only_user = false # bool |  (optional) (default to false)
notes_for_pipeline_execution = '' # str | Notes of a pipeline execution (optional)

try:
    # Execute a Pipeline with Runtime Input YAML
    api_response = api_instance.post_pipeline_execute_with_input_set_yaml(account_identifier, org_identifier, project_identifier, identifier, body=body, module_type=module_type, branch=branch, repo_identifier=repo_identifier, get_default_from_other_repo=get_default_from_other_repo, use_fqnif_error=use_fqnif_error, notify_only_user=notify_only_user, notes_for_pipeline_execution=notes_for_pipeline_execution)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineExecuteApi->post_pipeline_execute_with_input_set_yaml: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **identifier** | **str**| Pipeline identifier for the entity. Identifier of the Pipeline to be executed | 
 **body** | [**str**](str.md)| Enter Runtime Input YAML if the Pipeline contains Runtime Inputs. Template for this can be Fetched from /inputSets/template API. | [optional] 
 **module_type** | **str**| Module type for the entity. If its from deployments,type will be CD , if its from build type will be CI | [optional] 
 **branch** | **str**| Name of the branch. | [optional] 
 **repo_identifier** | **str**| Git Sync Config Id. | [optional] 
 **get_default_from_other_repo** | **bool**| if true, return all the default entities | [optional] 
 **use_fqnif_error** | **bool**|  | [optional] [default to false]
 **notify_only_user** | **bool**|  | [optional] [default to false]
 **notes_for_pipeline_execution** | **str**| Notes of a pipeline execution | [optional] 

### Return type

[**ResponseDTOPlanExecutionResponse**](ResponseDTOPlanExecutionResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_handle_interrupt**
> ResponseDTOInterruptResponse put_handle_interrupt(account_identifier, org_identifier, project_identifier, interrupt_type, plan_execution_id)

Execute an Interrupt

Executes an Interrupt on a Given Execution

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
api_instance = swagger_client.PipelineExecuteApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
interrupt_type = 'interrupt_type_example' # str | The Interrupt type needed to be applied to the execution. Choose a value from the enum list.
plan_execution_id = 'plan_execution_id_example' # str | The Pipeline Execution Id on which the Interrupt needs to be applied.

try:
    # Execute an Interrupt
    api_response = api_instance.put_handle_interrupt(account_identifier, org_identifier, project_identifier, interrupt_type, plan_execution_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineExecuteApi->put_handle_interrupt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **interrupt_type** | **str**| The Interrupt type needed to be applied to the execution. Choose a value from the enum list. | 
 **plan_execution_id** | **str**| The Pipeline Execution Id on which the Interrupt needs to be applied. | 

### Return type

[**ResponseDTOInterruptResponse**](ResponseDTOInterruptResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retry_history**
> ResponseDTORetryHistoryResponse retry_history(account_identifier, org_identifier, project_identifier, pipeline_identifier, plan_execution_id)

Retry History for a given execution

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
api_instance = swagger_client.PipelineExecuteApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
pipeline_identifier = 'pipeline_identifier_example' # str | Pipeline Identifier
plan_execution_id = 'plan_execution_id_example' # str | planExecutionId of the execution of whose we need to find the retry history

try:
    # Retry History for a given execution
    api_response = api_instance.retry_history(account_identifier, org_identifier, project_identifier, pipeline_identifier, plan_execution_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineExecuteApi->retry_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **pipeline_identifier** | **str**| Pipeline Identifier | 
 **plan_execution_id** | **str**| planExecutionId of the execution of whose we need to find the retry history | 

### Return type

[**ResponseDTORetryHistoryResponse**](ResponseDTORetryHistoryResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retry_pipeline**
> ResponseDTOPlanExecutionResponse retry_pipeline(account_identifier, org_identifier, project_identifier, plan_execution_id, retry_stages, identifier, body=body, module_type=module_type, run_all_stages=run_all_stages, notes_for_pipeline_execution=notes_for_pipeline_execution)

Retry a executed pipeline with inputSet pipeline yaml

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
api_instance = swagger_client.PipelineExecuteApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
plan_execution_id = 'plan_execution_id_example' # str | This param contains the previous execution execution id. This is basically when we are rerunning a Pipeline.
retry_stages = ['retry_stages_example'] # list[str] | This param contains the identifier of stages from where to resume. It will be a list if we want to retry from parallel group 
identifier = 'identifier_example' # str | Pipeline Identifier
body = 'body_example' # str |  (optional)
module_type = 'module_type_example' # str | Module type for the entity. If its from deployments,type will be CD , if its from build type will be CI (optional)
run_all_stages = true # bool | This param provides an option to run only the failed stages when Pipeline fails at parallel group. By default, it will run all the stages in the failed parallel group. (optional) (default to true)
notes_for_pipeline_execution = '' # str | Notes of a pipeline execution (optional)

try:
    # Retry a executed pipeline with inputSet pipeline yaml
    api_response = api_instance.retry_pipeline(account_identifier, org_identifier, project_identifier, plan_execution_id, retry_stages, identifier, body=body, module_type=module_type, run_all_stages=run_all_stages, notes_for_pipeline_execution=notes_for_pipeline_execution)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineExecuteApi->retry_pipeline: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **plan_execution_id** | **str**| This param contains the previous execution execution id. This is basically when we are rerunning a Pipeline. | 
 **retry_stages** | [**list[str]**](str.md)| This param contains the identifier of stages from where to resume. It will be a list if we want to retry from parallel group  | 
 **identifier** | **str**| Pipeline Identifier | 
 **body** | [**str**](str.md)|  | [optional] 
 **module_type** | **str**| Module type for the entity. If its from deployments,type will be CD , if its from build type will be CI | [optional] 
 **run_all_stages** | **bool**| This param provides an option to run only the failed stages when Pipeline fails at parallel group. By default, it will run all the stages in the failed parallel group. | [optional] [default to true]
 **notes_for_pipeline_execution** | **str**| Notes of a pipeline execution | [optional] 

### Return type

[**ResponseDTOPlanExecutionResponse**](ResponseDTOPlanExecutionResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

