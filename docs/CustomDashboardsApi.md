# swagger_client.CustomDashboardsApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_dashboard_data**](CustomDashboardsApi.md#get_dashboard_data) | **GET** /dashboard/api/dashboards/{dashboard_id}/download | Download data within a Dashboard

# **get_dashboard_data**
> DashboardDownloadResponse get_dashboard_data(dashboard_id, file_type, filters=filters)

Download data within a Dashboard

Download the data of all tiles within a Dashboard.

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
api_instance = swagger_client.CustomDashboardsApi(swagger_client.ApiClient(configuration))
dashboard_id = 'dashboard_id_example' # str | 
file_type = 'file_type_example' # str | 
filters = 'filters_example' # str |  (optional)

try:
    # Download data within a Dashboard
    api_response = api_instance.get_dashboard_data(dashboard_id, file_type, filters=filters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomDashboardsApi->get_dashboard_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **str**|  | 
 **file_type** | **str**|  | 
 **filters** | **str**|  | [optional] 

### Return type

[**DashboardDownloadResponse**](DashboardDownloadResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

