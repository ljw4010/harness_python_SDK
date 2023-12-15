# harness_python_sdk.ProxyApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_proxy_key**](ProxyApi.md#create_proxy_key) | **POST** /cf/admin/proxy/keys | Creates a Proxy Key in the account &amp; org
[**delete_proxy_key**](ProxyApi.md#delete_proxy_key) | **DELETE** /cf/admin/proxy/keys/{identifier} | Deletes a ProxyKey
[**get_proxy_key**](ProxyApi.md#get_proxy_key) | **GET** /cf/admin/proxy/keys/{identifier} | Returns a ProxyKey
[**get_proxy_keys**](ProxyApi.md#get_proxy_keys) | **GET** /cf/admin/proxy/keys | Returns all Proxy keys in an account
[**patch_proxy_key**](ProxyApi.md#patch_proxy_key) | **PATCH** /cf/admin/proxy/keys/{identifier} | Updates a Proxy Key in the account &amp; org
[**update_proxy_key**](ProxyApi.md#update_proxy_key) | **PUT** /cf/admin/proxy/keys/{identifier} | Updates a Proxy Key in the account &amp; org

# **create_proxy_key**
> InlineResponse201 create_proxy_key(account_identifier, body=body)

Creates a Proxy Key in the account & org

Creates a Proxy Key in the account & org

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
api_instance = harness_python_sdk.ProxyApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier
body = NULL # object |  (optional)

try:
    # Creates a Proxy Key in the account & org
    api_response = api_instance.create_proxy_key(account_identifier, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProxyApi->create_proxy_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier | 
 **body** | [**object**](object.md)|  | [optional] 

### Return type

[**InlineResponse201**](InlineResponse201.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_proxy_key**
> delete_proxy_key(account_identifier, identifier)

Deletes a ProxyKey

Deletes a ProxyKey

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
api_instance = harness_python_sdk.ProxyApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier
identifier = 'identifier_example' # str | Unique identifier for the object in the API.

try:
    # Deletes a ProxyKey
    api_instance.delete_proxy_key(account_identifier, identifier)
except ApiException as e:
    print("Exception when calling ProxyApi->delete_proxy_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier | 
 **identifier** | **str**| Unique identifier for the object in the API. | 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_proxy_key**
> InlineResponse200 get_proxy_key(account_identifier, identifier)

Returns a ProxyKey

Returns a ProxyKey

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
api_instance = harness_python_sdk.ProxyApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier
identifier = 'identifier_example' # str | Unique identifier for the object in the API.

try:
    # Returns a ProxyKey
    api_response = api_instance.get_proxy_key(account_identifier, identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProxyApi->get_proxy_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier | 
 **identifier** | **str**| Unique identifier for the object in the API. | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_proxy_keys**
> ProxyKeys get_proxy_keys(account_identifier, name=name, sort_order=sort_order, sort_by_field=sort_by_field, page_number=page_number, page_size=page_size)

Returns all Proxy keys in an account

Returns all the Proxy keys in an account

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
api_instance = harness_python_sdk.ProxyApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier
name = 'name_example' # str | Name of the field (optional)
sort_order = 'sort_order_example' # str | SortOrder (optional)
sort_by_field = 'sort_by_field_example' # str | SortByField (optional)
page_number = 56 # int | PageNumber (optional)
page_size = 56 # int | PageSize (optional)

try:
    # Returns all Proxy keys in an account
    api_response = api_instance.get_proxy_keys(account_identifier, name=name, sort_order=sort_order, sort_by_field=sort_by_field, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProxyApi->get_proxy_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier | 
 **name** | **str**| Name of the field | [optional] 
 **sort_order** | **str**| SortOrder | [optional] 
 **sort_by_field** | **str**| SortByField | [optional] 
 **page_number** | **int**| PageNumber | [optional] 
 **page_size** | **int**| PageSize | [optional] 

### Return type

[**ProxyKeys**](ProxyKeys.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_proxy_key**
> InlineResponse201 patch_proxy_key(account_identifier, identifier, body=body)

Updates a Proxy Key in the account & org

Operation is currently used (but not limited to) to rotate ProxyKey

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
api_instance = harness_python_sdk.ProxyApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier
identifier = 'identifier_example' # str | Unique identifier for the object in the API.
body = harness_python_sdk.ProxyKeyInstruction() # ProxyKeyInstruction |  (optional)

try:
    # Updates a Proxy Key in the account & org
    api_response = api_instance.patch_proxy_key(account_identifier, identifier, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProxyApi->patch_proxy_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier | 
 **identifier** | **str**| Unique identifier for the object in the API. | 
 **body** | [**ProxyKeyInstruction**](ProxyKeyInstruction.md)|  | [optional] 

### Return type

[**InlineResponse201**](InlineResponse201.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_proxy_key**
> update_proxy_key(account_identifier, identifier, body=body)

Updates a Proxy Key in the account & org

This operation is used to modify which environments a ProxyKey has access to. The requet body can include one or more instructions that can assign or unassign environmnets to the ProxyKey 

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
api_instance = harness_python_sdk.ProxyApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier
identifier = 'identifier_example' # str | Unique identifier for the object in the API.
body = NULL # object |  (optional)

try:
    # Updates a Proxy Key in the account & org
    api_instance.update_proxy_key(account_identifier, identifier, body=body)
except ApiException as e:
    print("Exception when calling ProxyApi->update_proxy_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier | 
 **identifier** | **str**| Unique identifier for the object in the API. | 
 **body** | [**object**](object.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

