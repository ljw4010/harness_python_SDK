# swagger_client.ApplicationApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**application_service_list_apps**](ApplicationApi.md#application_service_list_apps) | **POST** /gitops/api/v1/applications | 

# **application_service_list_apps**
> Servicev1Applicationlist application_service_list_apps(body)



List returns list of apps

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
api_instance = swagger_client.ApplicationApi(swagger_client.ApiClient(configuration))
body = swagger_client.Servicev1ApplicationQuery() # Servicev1ApplicationQuery | 

try:
    api_response = api_instance.application_service_list_apps(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->application_service_list_apps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Servicev1ApplicationQuery**](Servicev1ApplicationQuery.md)|  | 

### Return type

[**Servicev1Applicationlist**](Servicev1Applicationlist.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

