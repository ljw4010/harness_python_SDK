# harness_python_sdk.SecretManagersApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_metadata**](SecretManagersApi.md#get_metadata) | **POST** /ng/api/secret-managers/meta-data | Gets the metadata of Secret Manager

# **get_metadata**
> ResponseDTOSecretManagerMetadataDTO get_metadata(body, account_identifier)

Gets the metadata of Secret Manager

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
api_instance = harness_python_sdk.SecretManagersApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.SecretManagerMetadataRequest() # SecretManagerMetadataRequest | Details required for the creation of the Secret Manager
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Gets the metadata of Secret Manager
    api_response = api_instance.get_metadata(body, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecretManagersApi->get_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SecretManagerMetadataRequest**](SecretManagerMetadataRequest.md)| Details required for the creation of the Secret Manager | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**ResponseDTOSecretManagerMetadataDTO**](ResponseDTOSecretManagerMetadataDTO.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

