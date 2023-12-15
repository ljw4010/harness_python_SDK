# swagger_client.GoogleSecretManagerConnectorApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_gcp_regions**](GoogleSecretManagerConnectorApi.md#get_gcp_regions) | **GET** /ng/api/google-secret-manager-connector/gcp-regions | Get list of GCP Regions

# **get_gcp_regions**
> ResponseDTOListString get_gcp_regions()

Get list of GCP Regions

Lists all GCP Regions

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
api_instance = swagger_client.GoogleSecretManagerConnectorApi(swagger_client.ApiClient(configuration))

try:
    # Get list of GCP Regions
    api_response = api_instance.get_gcp_regions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GoogleSecretManagerConnectorApi->get_gcp_regions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResponseDTOListString**](ResponseDTOListString.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, text/yaml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

