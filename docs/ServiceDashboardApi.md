# harness_python_sdk.ServiceDashboardApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pipeline_execution_count**](ServiceDashboardApi.md#pipeline_execution_count) | **GET** /ng/api/dashboard/getPipelineExecutionCount | Get pipeline execution count for a service with grouping support on artifact and deployment status

# **pipeline_execution_count**
> ResponseDTOPipelineExecutionCountInfo pipeline_execution_count(account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, service_id=service_id, start_time=start_time, end_time=end_time, artifact_path=artifact_path, artifact_version=artifact_version, artifact=artifact, status=status)

Get pipeline execution count for a service with grouping support on artifact and deployment status

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
api_instance = harness_python_sdk.ServiceDashboardApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
service_id = 'service_id_example' # str | Service Identifier for the Entity. (optional)
start_time = 789 # int | Start Time of the Interval for the Entity. (optional)
end_time = 789 # int | End Time of the Interval for the Entity. (optional)
artifact_path = 'artifact_path_example' # str | Image/ArtifactPath of the Artifact (optional)
artifact_version = 'artifact_version_example' # str | Version of the Artifact (optional)
artifact = 'artifact_example' # str | Fully Qualified Name of the Artifact (artifactPath:artifactVersion). For eg. in case of docker it would be imagePath:tag (optional)
status = 'status_example' # str | Deployment status (optional)

try:
    # Get pipeline execution count for a service with grouping support on artifact and deployment status
    api_response = api_instance.pipeline_execution_count(account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, service_id=service_id, start_time=start_time, end_time=end_time, artifact_path=artifact_path, artifact_version=artifact_version, artifact=artifact, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceDashboardApi->pipeline_execution_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **service_id** | **str**| Service Identifier for the Entity. | [optional] 
 **start_time** | **int**| Start Time of the Interval for the Entity. | [optional] 
 **end_time** | **int**| End Time of the Interval for the Entity. | [optional] 
 **artifact_path** | **str**| Image/ArtifactPath of the Artifact | [optional] 
 **artifact_version** | **str**| Version of the Artifact | [optional] 
 **artifact** | **str**| Fully Qualified Name of the Artifact (artifactPath:artifactVersion). For eg. in case of docker it would be imagePath:tag | [optional] 
 **status** | **str**| Deployment status | [optional] 

### Return type

[**ResponseDTOPipelineExecutionCountInfo**](ResponseDTOPipelineExecutionCountInfo.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

