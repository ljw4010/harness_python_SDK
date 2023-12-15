# swagger_client.IPAllowlistApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ip_allowlist_config**](IPAllowlistApi.md#create_ip_allowlist_config) | **POST** /v1/ip-allowlist | Create a IP Allowlist config
[**delete_ip_allowlist_config**](IPAllowlistApi.md#delete_ip_allowlist_config) | **DELETE** /v1/ip-allowlist/{ip-config-identifier} | Delete an IP Allowlist config
[**get_ip_allowlist_config**](IPAllowlistApi.md#get_ip_allowlist_config) | **GET** /v1/ip-allowlist/{ip-config-identifier} | Retrieve a IP Allowlist config
[**get_ip_allowlist_configs**](IPAllowlistApi.md#get_ip_allowlist_configs) | **GET** /v1/ip-allowlist | List IP Allowlist Configs
[**update_ip_allowlist_config**](IPAllowlistApi.md#update_ip_allowlist_config) | **PUT** /v1/ip-allowlist/{ip-config-identifier} | Update IP Allowlist config
[**validate_ip_address_allowlisted_or_not**](IPAllowlistApi.md#validate_ip_address_allowlisted_or_not) | **GET** /v1/ip-allowlist/validate/ip-address | Validate IP address lies in a specified range or not
[**validate_unique_ip_allowlist_config_identifier**](IPAllowlistApi.md#validate_unique_ip_allowlist_config_identifier) | **GET** /v1/ip-allowlist/validate-unique-identifier/{ip-config-identifier} | Validate unique IP Allowlist config identifier

# **create_ip_allowlist_config**
> IPAllowlistConfigResponse create_ip_allowlist_config(body=body, harness_account=harness_account)

Create a IP Allowlist config

Creates a new IP Allowlist config

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
api_instance = swagger_client.IPAllowlistApi(swagger_client.ApiClient(configuration))
body = swagger_client.IPAllowlistConfigRequest() # IPAllowlistConfigRequest |  (optional)
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)

try:
    # Create a IP Allowlist config
    api_response = api_instance.create_ip_allowlist_config(body=body, harness_account=harness_account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IPAllowlistApi->create_ip_allowlist_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IPAllowlistConfigRequest**](IPAllowlistConfigRequest.md)|  | [optional] 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 

### Return type

[**IPAllowlistConfigResponse**](IPAllowlistConfigResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ip_allowlist_config**
> delete_ip_allowlist_config(ip_config_identifier, harness_account=harness_account)

Delete an IP Allowlist config

Deletes the specified IP Allowlist config

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
api_instance = swagger_client.IPAllowlistApi(swagger_client.ApiClient(configuration))
ip_config_identifier = 'ip_config_identifier_example' # str | 
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)

try:
    # Delete an IP Allowlist config
    api_instance.delete_ip_allowlist_config(ip_config_identifier, harness_account=harness_account)
except ApiException as e:
    print("Exception when calling IPAllowlistApi->delete_ip_allowlist_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip_config_identifier** | **str**|  | 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ip_allowlist_config**
> IPAllowlistConfigResponse get_ip_allowlist_config(ip_config_identifier, harness_account=harness_account)

Retrieve a IP Allowlist config

Retrieves the specified IP Allowlist config

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
api_instance = swagger_client.IPAllowlistApi(swagger_client.ApiClient(configuration))
ip_config_identifier = 'ip_config_identifier_example' # str | 
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)

try:
    # Retrieve a IP Allowlist config
    api_response = api_instance.get_ip_allowlist_config(ip_config_identifier, harness_account=harness_account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IPAllowlistApi->get_ip_allowlist_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip_config_identifier** | **str**|  | 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 

### Return type

[**IPAllowlistConfigResponse**](IPAllowlistConfigResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ip_allowlist_configs**
> list[IPAllowlistConfigResponse] get_ip_allowlist_configs(search_term=search_term, page=page, limit=limit, harness_account=harness_account, sort=sort, order=order, allowed_source_type=allowed_source_type)

List IP Allowlist Configs

Retrieves the information of the IP Allowlist Config

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
api_instance = swagger_client.IPAllowlistApi(swagger_client.ApiClient(configuration))
search_term = 'search_term_example' # str | This would be used to filter resources having attributes matching with search term. (optional)
page = 0 # int | Pagination page number strategy: Specify the page number within the paginated collection related to the number of items in each page  (optional) (default to 0)
limit = 30 # int | Number of items to return per page. (optional) (default to 30)
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)
sort = 'sort_example' # str | Parameter on the basis of which sorting is done. (optional)
order = 'order_example' # str | Order on the basis of which sorting is done. (optional)
allowed_source_type = 'allowed_source_type_example' # str | This is to filter IP allowlist configs only blocked from UI or API (optional)

try:
    # List IP Allowlist Configs
    api_response = api_instance.get_ip_allowlist_configs(search_term=search_term, page=page, limit=limit, harness_account=harness_account, sort=sort, order=order, allowed_source_type=allowed_source_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IPAllowlistApi->get_ip_allowlist_configs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_term** | **str**| This would be used to filter resources having attributes matching with search term. | [optional] 
 **page** | **int**| Pagination page number strategy: Specify the page number within the paginated collection related to the number of items in each page  | [optional] [default to 0]
 **limit** | **int**| Number of items to return per page. | [optional] [default to 30]
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 
 **sort** | **str**| Parameter on the basis of which sorting is done. | [optional] 
 **order** | **str**| Order on the basis of which sorting is done. | [optional] 
 **allowed_source_type** | **str**| This is to filter IP allowlist configs only blocked from UI or API | [optional] 

### Return type

[**list[IPAllowlistConfigResponse]**](IPAllowlistConfigResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ip_allowlist_config**
> IPAllowlistConfigResponse update_ip_allowlist_config(ip_config_identifier, body=body, harness_account=harness_account)

Update IP Allowlist config

Updates the specified IP Allowlist config

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
api_instance = swagger_client.IPAllowlistApi(swagger_client.ApiClient(configuration))
ip_config_identifier = 'ip_config_identifier_example' # str | 
body = swagger_client.IPAllowlistConfigRequest() # IPAllowlistConfigRequest |  (optional)
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)

try:
    # Update IP Allowlist config
    api_response = api_instance.update_ip_allowlist_config(ip_config_identifier, body=body, harness_account=harness_account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IPAllowlistApi->update_ip_allowlist_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip_config_identifier** | **str**|  | 
 **body** | [**IPAllowlistConfigRequest**](IPAllowlistConfigRequest.md)|  | [optional] 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 

### Return type

[**IPAllowlistConfigResponse**](IPAllowlistConfigResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_ip_address_allowlisted_or_not**
> IPAllowlistConfigValidateResponse validate_ip_address_allowlisted_or_not(ip_address, harness_account=harness_account, custom_ip_address_block=custom_ip_address_block)

Validate IP address lies in a specified range or not

Checks whether the IP address is allowed or not. It also supports checking against a specific IP block range.

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
api_instance = swagger_client.IPAllowlistApi(swagger_client.ApiClient(configuration))
ip_address = 'ip_address_example' # str | This is the IP address that needs to be checked if allowed or not
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)
custom_ip_address_block = 'custom_ip_address_block_example' # str | This is the IP address or block of IP address against which we need to verify if a given IP address is allowed or not. If not passed we do the validation against the IP configs within Harness. (optional)

try:
    # Validate IP address lies in a specified range or not
    api_response = api_instance.validate_ip_address_allowlisted_or_not(ip_address, harness_account=harness_account, custom_ip_address_block=custom_ip_address_block)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IPAllowlistApi->validate_ip_address_allowlisted_or_not: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip_address** | **str**| This is the IP address that needs to be checked if allowed or not | 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 
 **custom_ip_address_block** | **str**| This is the IP address or block of IP address against which we need to verify if a given IP address is allowed or not. If not passed we do the validation against the IP configs within Harness. | [optional] 

### Return type

[**IPAllowlistConfigValidateResponse**](IPAllowlistConfigValidateResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_unique_ip_allowlist_config_identifier**
> bool validate_unique_ip_allowlist_config_identifier(ip_config_identifier, harness_account=harness_account)

Validate unique IP Allowlist config identifier

Checks whether the IP Allowlist config identifier is unique or not

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
api_instance = swagger_client.IPAllowlistApi(swagger_client.ApiClient(configuration))
ip_config_identifier = 'ip_config_identifier_example' # str | 
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)

try:
    # Validate unique IP Allowlist config identifier
    api_response = api_instance.validate_unique_ip_allowlist_config_identifier(ip_config_identifier, harness_account=harness_account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IPAllowlistApi->validate_unique_ip_allowlist_config_identifier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip_config_identifier** | **str**|  | 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 

### Return type

**bool**

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

