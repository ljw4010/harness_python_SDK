# swagger_client.PipelineDashboardApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_pipeline_execution**](PipelineDashboardApi.md#get_pipeline_execution) | **GET** /pipeline/api/pipelines/pipelineExecution | Fetch Execution Details for an Interval

# **get_pipeline_execution**
> ResponseDTODashboardPipelineExecution get_pipeline_execution(account_identifier, org_identifier, project_identifier, pipeline_identifier, module_info, start_time, end_time)

Fetch Execution Details for an Interval

Returns Pipeline Execution Details for a Given Interval (Presented in Day Wise Format)

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
api_instance = swagger_client.PipelineDashboardApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
pipeline_identifier = 'pipeline_identifier_example' # str | Pipeline Identifier
module_info = 'module_info_example' # str | The module from which execution was triggered.
start_time = 789 # int | Start Date Epoch time in ms
end_time = 789 # int | End Date Epoch time in ms

try:
    # Fetch Execution Details for an Interval
    api_response = api_instance.get_pipeline_execution(account_identifier, org_identifier, project_identifier, pipeline_identifier, module_info, start_time, end_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineDashboardApi->get_pipeline_execution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **pipeline_identifier** | **str**| Pipeline Identifier | 
 **module_info** | **str**| The module from which execution was triggered. | 
 **start_time** | **int**| Start Date Epoch time in ms | 
 **end_time** | **int**| End Date Epoch time in ms | 

### Return type

[**ResponseDTODashboardPipelineExecution**](ResponseDTODashboardPipelineExecution.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

