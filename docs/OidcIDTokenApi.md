# harness_python_sdk.OidcIDTokenApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_oidc_id_token_for_gcp**](OidcIDTokenApi.md#generate_oidc_id_token_for_gcp) | **POST** /ng/api/oidc/id-token/gcp | Generates an OIDC ID Token for GCP

# **generate_oidc_id_token_for_gcp**
> ResponseDTOString generate_oidc_id_token_for_gcp(body)

Generates an OIDC ID Token for GCP

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
api_instance = harness_python_sdk.OidcIDTokenApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.GcpOidcTokenRequest() # GcpOidcTokenRequest | Details of GCP Workload Identity

try:
    # Generates an OIDC ID Token for GCP
    api_response = api_instance.generate_oidc_id_token_for_gcp(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OidcIDTokenApi->generate_oidc_id_token_for_gcp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GcpOidcTokenRequest**](GcpOidcTokenRequest.md)| Details of GCP Workload Identity | 

### Return type

[**ResponseDTOString**](ResponseDTOString.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

