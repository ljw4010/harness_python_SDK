# swagger_client.APIKeysApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_api_key**](APIKeysApi.md#add_api_key) | **POST** /cf/admin/apikey | Creates an API key for the given Environment
[**delete_api_key**](APIKeysApi.md#delete_api_key) | **DELETE** /cf/admin/apikey/{identifier} | Deletes an API Key
[**get_all_api_keys**](APIKeysApi.md#get_all_api_keys) | **GET** /cf/admin/apikey | Returns API Keys for an Environment
[**get_api_key**](APIKeysApi.md#get_api_key) | **GET** /cf/admin/apikey/{identifier} | Returns API keys
[**update_api_key**](APIKeysApi.md#update_api_key) | **PUT** /cf/admin/apikey/{identifier} | Updates an API Key

# **add_api_key**
> CfApiKey add_api_key(account_identifier, org_identifier, environment_identifier, project_identifier, body=body)

Creates an API key for the given Environment

Creates an API key for the given Environment

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
api_instance = swagger_client.APIKeysApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier
org_identifier = 'org_identifier_example' # str | Organization Identifier
environment_identifier = 'environment_identifier_example' # str | Environment Identifier
project_identifier = 'project_identifier_example' # str | The Project identifier
body = NULL # object |  (optional)

try:
    # Creates an API key for the given Environment
    api_response = api_instance.add_api_key(account_identifier, org_identifier, environment_identifier, project_identifier, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIKeysApi->add_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier | 
 **org_identifier** | **str**| Organization Identifier | 
 **environment_identifier** | **str**| Environment Identifier | 
 **project_identifier** | **str**| The Project identifier | 
 **body** | [**object**](object.md)|  | [optional] 

### Return type

[**CfApiKey**](CfApiKey.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_api_key**
> delete_api_key(identifier, project_identifier, environment_identifier, account_identifier, org_identifier)

Deletes an API Key

Deletes an API key for the given identifier

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
api_instance = swagger_client.APIKeysApi(swagger_client.ApiClient(configuration))
identifier = 'identifier_example' # str | Unique identifier for the object in the API.
project_identifier = 'project_identifier_example' # str | The Project identifier
environment_identifier = 'environment_identifier_example' # str | Environment Identifier
account_identifier = 'account_identifier_example' # str | Account Identifier
org_identifier = 'org_identifier_example' # str | Organization Identifier

try:
    # Deletes an API Key
    api_instance.delete_api_key(identifier, project_identifier, environment_identifier, account_identifier, org_identifier)
except ApiException as e:
    print("Exception when calling APIKeysApi->delete_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Unique identifier for the object in the API. | 
 **project_identifier** | **str**| The Project identifier | 
 **environment_identifier** | **str**| Environment Identifier | 
 **account_identifier** | **str**| Account Identifier | 
 **org_identifier** | **str**| Organization Identifier | 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_api_keys**
> ApiKeys get_all_api_keys(account_identifier, org_identifier, project_identifier, environment_identifier, page_number=page_number, page_size=page_size)

Returns API Keys for an Environment

Returns all the API Keys for an Environment

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
api_instance = swagger_client.APIKeysApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier
org_identifier = 'org_identifier_example' # str | Organization Identifier
project_identifier = 'project_identifier_example' # str | The Project identifier
environment_identifier = 'environment_identifier_example' # str | Environment Identifier
page_number = 56 # int | PageNumber (optional)
page_size = 56 # int | PageSize (optional)

try:
    # Returns API Keys for an Environment
    api_response = api_instance.get_all_api_keys(account_identifier, org_identifier, project_identifier, environment_identifier, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIKeysApi->get_all_api_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier | 
 **org_identifier** | **str**| Organization Identifier | 
 **project_identifier** | **str**| The Project identifier | 
 **environment_identifier** | **str**| Environment Identifier | 
 **page_number** | **int**| PageNumber | [optional] 
 **page_size** | **int**| PageSize | [optional] 

### Return type

[**ApiKeys**](ApiKeys.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_key**
> CfApiKey get_api_key(identifier, project_identifier, environment_identifier, account_identifier, org_identifier)

Returns API keys

Returns all the API Keys for the given identifier

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
api_instance = swagger_client.APIKeysApi(swagger_client.ApiClient(configuration))
identifier = 'identifier_example' # str | Unique identifier for the object in the API.
project_identifier = 'project_identifier_example' # str | The Project identifier
environment_identifier = 'environment_identifier_example' # str | Environment Identifier
account_identifier = 'account_identifier_example' # str | Account Identifier
org_identifier = 'org_identifier_example' # str | Organization Identifier

try:
    # Returns API keys
    api_response = api_instance.get_api_key(identifier, project_identifier, environment_identifier, account_identifier, org_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIKeysApi->get_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Unique identifier for the object in the API. | 
 **project_identifier** | **str**| The Project identifier | 
 **environment_identifier** | **str**| Environment Identifier | 
 **account_identifier** | **str**| Account Identifier | 
 **org_identifier** | **str**| Organization Identifier | 

### Return type

[**CfApiKey**](CfApiKey.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_api_key**
> update_api_key(project_identifier, environment_identifier, account_identifier, org_identifier, identifier, body=body)

Updates an API Key

Updates an API key for the given identifier

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
api_instance = swagger_client.APIKeysApi(swagger_client.ApiClient(configuration))
project_identifier = 'project_identifier_example' # str | The Project identifier
environment_identifier = 'environment_identifier_example' # str | Environment Identifier
account_identifier = 'account_identifier_example' # str | Account Identifier
org_identifier = 'org_identifier_example' # str | Organization Identifier
identifier = 'identifier_example' # str | Unique identifier for the object in the API.
body = NULL # object |  (optional)

try:
    # Updates an API Key
    api_instance.update_api_key(project_identifier, environment_identifier, account_identifier, org_identifier, identifier, body=body)
except ApiException as e:
    print("Exception when calling APIKeysApi->update_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_identifier** | **str**| The Project identifier | 
 **environment_identifier** | **str**| Environment Identifier | 
 **account_identifier** | **str**| Account Identifier | 
 **org_identifier** | **str**| Organization Identifier | 
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

