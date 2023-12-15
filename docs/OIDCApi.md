# harness_python_sdk.OIDCApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_harness_open_id_config**](OIDCApi.md#get_harness_open_id_config) | **GET** /ng/api/oidc/account/{accountId}/.wellknown/jwks | Get the openid configuration for Harness
[**get_harness_open_id_config1**](OIDCApi.md#get_harness_open_id_config1) | **GET** /ng/api/oidc/account/{accountId}/.well-known/openid-configuration | Get the openid configuration for Harness

# **get_harness_open_id_config**
> JwksPublicKeysDTO get_harness_open_id_config(account_id)

Get the openid configuration for Harness

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
api_instance = harness_python_sdk.OIDCApi(harness_python_sdk.ApiClient(configuration))
account_id = 'account_id_example' # str | This is the accountIdentifier for the account for which the JWKS public key needs to be exposed.

try:
    # Get the openid configuration for Harness
    api_response = api_instance.get_harness_open_id_config(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OIDCApi->get_harness_open_id_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| This is the accountIdentifier for the account for which the JWKS public key needs to be exposed. | 

### Return type

[**JwksPublicKeysDTO**](JwksPublicKeysDTO.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_harness_open_id_config1**
> OidcConfiguration get_harness_open_id_config1(account_id)

Get the openid configuration for Harness

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
api_instance = harness_python_sdk.OIDCApi(harness_python_sdk.ApiClient(configuration))
account_id = 'account_id_example' # str | This is the accountIdentifier for the account for which the JWKS public key needs to be exposed.

try:
    # Get the openid configuration for Harness
    api_response = api_instance.get_harness_open_id_config1(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OIDCApi->get_harness_open_id_config1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| This is the accountIdentifier for the account for which the JWKS public key needs to be exposed. | 

### Return type

[**OidcConfiguration**](OidcConfiguration.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

