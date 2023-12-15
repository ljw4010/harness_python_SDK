# harness_python_sdk.CloudCostK8SConnectorsMetadataApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ccm_k8s_meta**](CloudCostK8SConnectorsMetadataApi.md#ccm_k8s_meta) | **POST** /ccm/api/ccmK8sMeta | Get CCM K8S Metadata

# **ccm_k8s_meta**
> ResponseDTOCcmK8sMetaInfoResponseDTO ccm_k8s_meta(body, account_identifier)

Get CCM K8S Metadata

Get CCM K8S Metadata 

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
api_instance = harness_python_sdk.CloudCostK8SConnectorsMetadataApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.CcmK8sMetaDTO() # CcmK8sMetaDTO | Request body containing Cost Access K8s connector identifiers
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Get CCM K8S Metadata
    api_response = api_instance.ccm_k8s_meta(body, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostK8SConnectorsMetadataApi->ccm_k8s_meta: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CcmK8sMetaDTO**](CcmK8sMetaDTO.md)| Request body containing Cost Access K8s connector identifiers | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**ResponseDTOCcmK8sMetaInfoResponseDTO**](ResponseDTOCcmK8sMetaInfoResponseDTO.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

