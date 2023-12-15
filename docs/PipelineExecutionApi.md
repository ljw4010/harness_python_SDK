# swagger_client.PipelineExecutionApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**execute_pipeline**](PipelineExecutionApi.md#execute_pipeline) | **POST** /v1/orgs/{org}/projects/{project}/pipelines/{pipeline}/execute | Execute Pipeline

# **execute_pipeline**
> PipelineExecuteResponseBody execute_pipeline(org, project, pipeline, body=body, harness_account=harness_account, module=module, use_fqn_if_error_response=use_fqn_if_error_response, notify_only_user=notify_only_user, notes=notes)

Execute Pipeline

Pipeline Execution API

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
api_instance = swagger_client.PipelineExecutionApi(swagger_client.ApiClient(configuration))
org = 'org_example' # str | Organization identifier
project = 'project_example' # str | Project identifier
pipeline = 'pipeline_example' # str | Pipeline identifier
body = swagger_client.PipelineExecuteBody() # PipelineExecuteBody |  (optional)
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)
module = 'module_example' # str |  (optional)
use_fqn_if_error_response = false # bool |  (optional) (default to false)
notify_only_user = false # bool |  (optional) (default to false)
notes = 'notes_example' # str |  (optional)

try:
    # Execute Pipeline
    api_response = api_instance.execute_pipeline(org, project, pipeline, body=body, harness_account=harness_account, module=module, use_fqn_if_error_response=use_fqn_if_error_response, notify_only_user=notify_only_user, notes=notes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineExecutionApi->execute_pipeline: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| Organization identifier | 
 **project** | **str**| Project identifier | 
 **pipeline** | **str**| Pipeline identifier | 
 **body** | [**PipelineExecuteBody**](PipelineExecuteBody.md)|  | [optional] 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 
 **module** | **str**|  | [optional] 
 **use_fqn_if_error_response** | **bool**|  | [optional] [default to false]
 **notify_only_user** | **bool**|  | [optional] [default to false]
 **notes** | **str**|  | [optional] 

### Return type

[**PipelineExecuteResponseBody**](PipelineExecuteResponseBody.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

