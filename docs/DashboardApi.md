# harness_python_sdk.DashboardApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dashboard_metrics**](DashboardApi.md#dashboard_metrics) | **GET** /pm/api/v1/dashboard | 

# **dashboard_metrics**
> DashboardMetrics dashboard_metrics(range=range, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, x_api_key=x_api_key)



Get metrics about policies, policy sets and evaluations

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
api_instance = harness_python_sdk.DashboardApi(harness_python_sdk.ApiClient(configuration))
range = '30d' # str | The time period over which to aggregate dashboard data. Can be: 24 hours, 7 days or 30 days (optional) (default to 30d)
account_identifier = '' # str | Harness account ID (optional)
org_identifier = '' # str | Harness organization ID (optional)
project_identifier = '' # str | Harness project ID (optional)
x_api_key = 'x_api_key_example' # str | Harness PAT key used to perform authorization (optional)

try:
    api_response = api_instance.dashboard_metrics(range=range, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, x_api_key=x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->dashboard_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **range** | **str**| The time period over which to aggregate dashboard data. Can be: 24 hours, 7 days or 30 days | [optional] [default to 30d]
 **account_identifier** | **str**| Harness account ID | [optional] 
 **org_identifier** | **str**| Harness organization ID | [optional] 
 **project_identifier** | **str**| Harness project ID | [optional] 
 **x_api_key** | **str**| Harness PAT key used to perform authorization | [optional] 

### Return type

[**DashboardMetrics**](DashboardMetrics.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.goa.error

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

