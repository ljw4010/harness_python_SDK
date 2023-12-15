# swagger_client.AccessControlListApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_access_control_list**](AccessControlListApi.md#get_access_control_list) | **POST** /authz/api/acl | Check Permission

# **get_access_control_list**
> ResponseDTOAccessCheckResponse get_access_control_list(body)

Check Permission

Check for permission on resource(s) for a principal

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
api_instance = swagger_client.AccessControlListApi(swagger_client.ApiClient(configuration))
body = swagger_client.AccessCheckRequest() # AccessCheckRequest | These are the checks to perform for Access Control.

try:
    # Check Permission
    api_response = api_instance.get_access_control_list(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessControlListApi->get_access_control_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccessCheckRequest**](AccessCheckRequest.md)| These are the checks to perform for Access Control. | 

### Return type

[**ResponseDTOAccessCheckResponse**](ResponseDTOAccessCheckResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

