# harness_python_sdk.ApiKeyApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_api_key**](ApiKeyApi.md#create_api_key) | **POST** /ng/api/apikey | Creates an API key
[**delete_api_key**](ApiKeyApi.md#delete_api_key) | **DELETE** /ng/api/apikey/{identifier} | Deletes the API Key corresponding to the provided ID.
[**get_aggregated_api_key**](ApiKeyApi.md#get_aggregated_api_key) | **GET** /ng/api/apikey/aggregate/{identifier} | Fetches the API Keys details corresponding to the provided ID and Scope.
[**list_api_keys**](ApiKeyApi.md#list_api_keys) | **GET** /ng/api/apikey/aggregate | Fetches the list of Aggregated API Keys corresponding to the request&#x27;s filter criteria.
[**list_api_keys1**](ApiKeyApi.md#list_api_keys1) | **GET** /ng/api/apikey | Fetches the list of API Keys corresponding to the request&#x27;s filter criteria.
[**update_api_key**](ApiKeyApi.md#update_api_key) | **PUT** /ng/api/apikey/{identifier} | Updates API Key for the provided ID

# **create_api_key**
> ResponseDTOApiKey create_api_key(account_identifier, body=body)

Creates an API key

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
api_instance = harness_python_sdk.ApiKeyApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
body = harness_python_sdk.ApiKey() # ApiKey |  (optional)

try:
    # Creates an API key
    api_response = api_instance.create_api_key(account_identifier, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiKeyApi->create_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **body** | [**ApiKey**](ApiKey.md)|  | [optional] 

### Return type

[**ResponseDTOApiKey**](ResponseDTOApiKey.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml, text/plain
 - **Accept**: application/json, application/yaml, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_api_key**
> ResponseDTOBoolean delete_api_key(account_identifier, api_key_type, parent_identifier, identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Deletes the API Key corresponding to the provided ID.

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
api_instance = harness_python_sdk.ApiKeyApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
api_key_type = 'api_key_type_example' # str | This is the API Key type like Personal Access Key or Service Account Key.
parent_identifier = 'parent_identifier_example' # str | Id of API key's Parent Service Account
identifier = 'identifier_example' # str | This is the API key ID
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Deletes the API Key corresponding to the provided ID.
    api_response = api_instance.delete_api_key(account_identifier, api_key_type, parent_identifier, identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiKeyApi->delete_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **api_key_type** | **str**| This is the API Key type like Personal Access Key or Service Account Key. | 
 **parent_identifier** | **str**| Id of API key&#x27;s Parent Service Account | 
 **identifier** | **str**| This is the API key ID | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOBoolean**](ResponseDTOBoolean.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aggregated_api_key**
> ResponseDTOApiKeyAggregate get_aggregated_api_key(account_identifier, api_key_type, parent_identifier, identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Fetches the API Keys details corresponding to the provided ID and Scope.

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
api_instance = harness_python_sdk.ApiKeyApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
api_key_type = 'api_key_type_example' # str | This is the API Key type like Personal Access Key or Service Account Key.
parent_identifier = 'parent_identifier_example' # str | ID of API key's Parent Service Account
identifier = 'identifier_example' # str | This is the API key ID
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Fetches the API Keys details corresponding to the provided ID and Scope.
    api_response = api_instance.get_aggregated_api_key(account_identifier, api_key_type, parent_identifier, identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiKeyApi->get_aggregated_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **api_key_type** | **str**| This is the API Key type like Personal Access Key or Service Account Key. | 
 **parent_identifier** | **str**| ID of API key&#x27;s Parent Service Account | 
 **identifier** | **str**| This is the API key ID | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOApiKeyAggregate**](ResponseDTOApiKeyAggregate.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_api_keys**
> ResponseDTOPageResponseApiKeyAggregate list_api_keys(account_identifier, api_key_type, parent_identifier, org_identifier=org_identifier, project_identifier=project_identifier, identifiers=identifiers, page_index=page_index, page_size=page_size, sort_orders=sort_orders, page_token=page_token, search_term=search_term)

Fetches the list of Aggregated API Keys corresponding to the request's filter criteria.

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
api_instance = harness_python_sdk.ApiKeyApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
api_key_type = 'api_key_type_example' # str | This is the API Key type like Personal Access Key or Service Account Key.
parent_identifier = 'parent_identifier_example' # str | ID of API key's Parent Service Account
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
identifiers = ['identifiers_example'] # list[str] | This is the list of API Key IDs. Details specific to these IDs would be fetched. (optional)
page_index = 0 # int | Page Index of the results to fetch.Default Value: 0 (optional) (default to 0)
page_size = 50 # int | Results per page(max 100)Default Value: 50 (optional) (default to 50)
sort_orders = [harness_python_sdk.SortOrder()] # list[SortOrder] | Sort criteria for the elements. (optional)
page_token = 'page_token_example' # str | Page Token of the next results to fetch.Default Value: '' (optional)
search_term = 'search_term_example' # str | This would be used to filter API keys. Any API key having the specified string in its Name, ID and Tag would be filtered. (optional)

try:
    # Fetches the list of Aggregated API Keys corresponding to the request's filter criteria.
    api_response = api_instance.list_api_keys(account_identifier, api_key_type, parent_identifier, org_identifier=org_identifier, project_identifier=project_identifier, identifiers=identifiers, page_index=page_index, page_size=page_size, sort_orders=sort_orders, page_token=page_token, search_term=search_term)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiKeyApi->list_api_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **api_key_type** | **str**| This is the API Key type like Personal Access Key or Service Account Key. | 
 **parent_identifier** | **str**| ID of API key&#x27;s Parent Service Account | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **identifiers** | [**list[str]**](str.md)| This is the list of API Key IDs. Details specific to these IDs would be fetched. | [optional] 
 **page_index** | **int**| Page Index of the results to fetch.Default Value: 0 | [optional] [default to 0]
 **page_size** | **int**| Results per page(max 100)Default Value: 50 | [optional] [default to 50]
 **sort_orders** | [**list[SortOrder]**](SortOrder.md)| Sort criteria for the elements. | [optional] 
 **page_token** | **str**| Page Token of the next results to fetch.Default Value: &#x27;&#x27; | [optional] 
 **search_term** | **str**| This would be used to filter API keys. Any API key having the specified string in its Name, ID and Tag would be filtered. | [optional] 

### Return type

[**ResponseDTOPageResponseApiKeyAggregate**](ResponseDTOPageResponseApiKeyAggregate.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_api_keys1**
> ResponseDTOListApiKey list_api_keys1(account_identifier, api_key_type, parent_identifier, org_identifier=org_identifier, project_identifier=project_identifier, identifiers=identifiers)

Fetches the list of API Keys corresponding to the request's filter criteria.

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
api_instance = harness_python_sdk.ApiKeyApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
api_key_type = 'api_key_type_example' # str | This is the API Key type like Personal Access Key or Service Account Key.
parent_identifier = 'parent_identifier_example' # str | ID of API key's Parent Service Account
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
identifiers = ['identifiers_example'] # list[str] | This is the list of API Key IDs. Details specific to these IDs would be fetched. (optional)

try:
    # Fetches the list of API Keys corresponding to the request's filter criteria.
    api_response = api_instance.list_api_keys1(account_identifier, api_key_type, parent_identifier, org_identifier=org_identifier, project_identifier=project_identifier, identifiers=identifiers)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiKeyApi->list_api_keys1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **api_key_type** | **str**| This is the API Key type like Personal Access Key or Service Account Key. | 
 **parent_identifier** | **str**| ID of API key&#x27;s Parent Service Account | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **identifiers** | [**list[str]**](str.md)| This is the list of API Key IDs. Details specific to these IDs would be fetched. | [optional] 

### Return type

[**ResponseDTOListApiKey**](ResponseDTOListApiKey.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_api_key**
> ResponseDTOApiKey update_api_key(identifier, body=body)

Updates API Key for the provided ID

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
api_instance = harness_python_sdk.ApiKeyApi(harness_python_sdk.ApiClient(configuration))
identifier = 'identifier_example' # str | This is the API key ID
body = harness_python_sdk.ApiKey() # ApiKey |  (optional)

try:
    # Updates API Key for the provided ID
    api_response = api_instance.update_api_key(identifier, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiKeyApi->update_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| This is the API key ID | 
 **body** | [**ApiKey**](ApiKey.md)|  | [optional] 

### Return type

[**ResponseDTOApiKey**](ResponseDTOApiKey.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml, text/plain
 - **Accept**: application/json, application/yaml, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

