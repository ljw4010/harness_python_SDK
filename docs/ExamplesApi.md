# swagger_client.ExamplesApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**examples_list**](ExamplesApi.md#examples_list) | **GET** /pm/api/v1/examples | 

# **examples_list**
> list[PolicyExample] examples_list(account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, x_api_key=x_api_key)



list examples

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
api_instance = swagger_client.ExamplesApi(swagger_client.ApiClient(configuration))
account_identifier = '' # str | Harness account ID (optional)
org_identifier = '' # str | Harness organization ID (optional)
project_identifier = '' # str | Harness project ID (optional)
x_api_key = 'x_api_key_example' # str | Harness PAT key used to perform authorization (optional)

try:
    api_response = api_instance.examples_list(account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, x_api_key=x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExamplesApi->examples_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Harness account ID | [optional] 
 **org_identifier** | **str**| Harness organization ID | [optional] 
 **project_identifier** | **str**| Harness project ID | [optional] 
 **x_api_key** | **str**| Harness PAT key used to perform authorization | [optional] 

### Return type

[**list[PolicyExample]**](PolicyExample.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.goa.error

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

