# harness_python_sdk.EULAApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sign_eula**](EULAApi.md#sign_eula) | **POST** /v1/eula/sign | Sign an End User License Agreement
[**validate_eula_sign**](EULAApi.md#validate_eula_sign) | **GET** v1/eula/validate-sign | Validate specified agreement is signed or not

# **sign_eula**
> EulaSignResponse sign_eula(body=body, harness_account=harness_account)

Sign an End User License Agreement

Sign an End User License Agreement.

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
api_instance = harness_python_sdk.EULAApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.EulaSignRequest() # EulaSignRequest |  (optional)
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)

try:
    # Sign an End User License Agreement
    api_response = api_instance.sign_eula(body=body, harness_account=harness_account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EULAApi->sign_eula: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EulaSignRequest**](EulaSignRequest.md)|  | [optional] 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 

### Return type

[**EulaSignResponse**](EulaSignResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_eula_sign**
> EulaSignResponse validate_eula_sign(agreement_type, harness_account=harness_account)

Validate specified agreement is signed or not

Check whether End User License Agreement has been signed for specified agreement type.

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
api_instance = harness_python_sdk.EULAApi(harness_python_sdk.ApiClient(configuration))
agreement_type = 'agreement_type_example' # str | Type of Agreements.
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)

try:
    # Validate specified agreement is signed or not
    api_response = api_instance.validate_eula_sign(agreement_type, harness_account=harness_account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EULAApi->validate_eula_sign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agreement_type** | **str**| Type of Agreements. | 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 

### Return type

[**EulaSignResponse**](EulaSignResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

