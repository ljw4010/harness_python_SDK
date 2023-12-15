# harness_python_sdk.ApprovalsApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_harness_approval_activity**](ApprovalsApi.md#add_harness_approval_activity) | **POST** /pipeline/api/approvals/{approvalInstanceId}/harness/activity | Approve or Reject a Pipeline Execution
[**get_approval_instances_by_execution_id**](ApprovalsApi.md#get_approval_instances_by_execution_id) | **GET** /v1/orgs/{org}/projects/{project}/approvals/execution/{execution-id} | Gets Approval Instances by Execution Id

# **add_harness_approval_activity**
> ResponseDTOApprovalInstanceResponse add_harness_approval_activity(body, approval_instance_id, account_identifier=account_identifier)

Approve or Reject a Pipeline Execution

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
api_instance = harness_python_sdk.ApprovalsApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.HarnessApprovalActivityRequest() # HarnessApprovalActivityRequest | Details of approval activity
approval_instance_id = 'approval_instance_id_example' # str | Approval Identifier for the entity
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity. (optional)

try:
    # Approve or Reject a Pipeline Execution
    api_response = api_instance.add_harness_approval_activity(body, approval_instance_id, account_identifier=account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApprovalsApi->add_harness_approval_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HarnessApprovalActivityRequest**](HarnessApprovalActivityRequest.md)| Details of approval activity | 
 **approval_instance_id** | **str**| Approval Identifier for the entity | 
 **account_identifier** | **str**| Account Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOApprovalInstanceResponse**](ResponseDTOApprovalInstanceResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_approval_instances_by_execution_id**
> list[ApprovalInstanceResponseBody] get_approval_instances_by_execution_id(org, project, execution_id, harness_account=harness_account, approval_status=approval_status, approval_type=approval_type, node_execution_id=node_execution_id)

Gets Approval Instances by Execution Id

Gets Approval Instances by Execution Id [Beta]

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
api_instance = harness_python_sdk.ApprovalsApi(harness_python_sdk.ApiClient(configuration))
org = 'org_example' # str | Organization identifier
project = 'project_example' # str | Project identifier
execution_id = 'execution_id_example' # str | Pipeline Execution identifier
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)
approval_status = 'approval_status_example' # str | This filters approval instances based on status (optional)
approval_type = 'approval_type_example' # str | This filters approval instances based on type (optional)
node_execution_id = 'node_execution_id_example' # str | This filters approval instances based on runtime identifier of the step (optional)

try:
    # Gets Approval Instances by Execution Id
    api_response = api_instance.get_approval_instances_by_execution_id(org, project, execution_id, harness_account=harness_account, approval_status=approval_status, approval_type=approval_type, node_execution_id=node_execution_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApprovalsApi->get_approval_instances_by_execution_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| Organization identifier | 
 **project** | **str**| Project identifier | 
 **execution_id** | **str**| Pipeline Execution identifier | 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 
 **approval_status** | **str**| This filters approval instances based on status | [optional] 
 **approval_type** | **str**| This filters approval instances based on type | [optional] 
 **node_execution_id** | **str**| This filters approval instances based on runtime identifier of the step | [optional] 

### Return type

[**list[ApprovalInstanceResponseBody]**](ApprovalInstanceResponseBody.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

