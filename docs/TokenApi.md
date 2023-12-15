# swagger_client.TokenApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_token**](TokenApi.md#create_token) | **POST** /ng/api/token | Create a Token
[**delete_token**](TokenApi.md#delete_token) | **DELETE** /ng/api/token/{identifier} | Delete a Token
[**list_aggregated_tokens**](TokenApi.md#list_aggregated_tokens) | **GET** /ng/api/token/aggregate | List all Tokens
[**rotate_token**](TokenApi.md#rotate_token) | **POST** /ng/api/token/rotate/{identifier} | Rotate a Token
[**update_token**](TokenApi.md#update_token) | **PUT** /ng/api/token/{identifier} | Update a Token
[**validate_token**](TokenApi.md#validate_token) | **POST** /ng/api/token/validate | Validate a Token

# **create_token**
> ResponseDTOString create_token(account_identifier, body=body)

Create a Token

Creates a Token for the given API Key Type.

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
api_instance = swagger_client.TokenApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
body = swagger_client.Token() # Token |  (optional)

try:
    # Create a Token
    api_response = api_instance.create_token(account_identifier, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->create_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **body** | [**Token**](Token.md)|  | [optional] 

### Return type

[**ResponseDTOString**](ResponseDTOString.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml, text/plain
 - **Accept**: application/json, application/yaml, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_token**
> ResponseDTOBoolean delete_token(identifier, account_identifier, api_key_type, parent_identifier, api_key_identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Delete a Token

Deletes a Token for the given API Key Type.

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
api_instance = swagger_client.TokenApi(swagger_client.ApiClient(configuration))
identifier = 'identifier_example' # str | Token ID
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
api_key_type = 'api_key_type_example' # str | This is the API Key type like Personal Access Key or Service Account Key.
parent_identifier = 'parent_identifier_example' # str | ID of API key's Parent Service Account
api_key_identifier = 'api_key_identifier_example' # str | API key ID
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Delete a Token
    api_response = api_instance.delete_token(identifier, account_identifier, api_key_type, parent_identifier, api_key_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->delete_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Token ID | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **api_key_type** | **str**| This is the API Key type like Personal Access Key or Service Account Key. | 
 **parent_identifier** | **str**| ID of API key&#x27;s Parent Service Account | 
 **api_key_identifier** | **str**| API key ID | 
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

# **list_aggregated_tokens**
> ResponseDTOPageResponseTokenAggregate list_aggregated_tokens(account_identifier, api_key_type, org_identifier=org_identifier, project_identifier=project_identifier, parent_identifier=parent_identifier, api_key_identifier=api_key_identifier, identifiers=identifiers, page_index=page_index, page_size=page_size, sort_orders=sort_orders, page_token=page_token, search_term=search_term, include_only_active_tokens=include_only_active_tokens)

List all Tokens

Lists all the Tokens matching the given search criteria.

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
api_instance = swagger_client.TokenApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
api_key_type = 'api_key_type_example' # str | This is the API Key type like Personal Access Key or Service Account Key.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
parent_identifier = 'parent_identifier_example' # str | ID of API key's Parent Service Account (optional)
api_key_identifier = 'api_key_identifier_example' # str | API key ID (optional)
identifiers = ['identifiers_example'] # list[str] | This is the list of Token IDs. Details specific to these IDs would be fetched. (optional)
page_index = 0 # int | Page Index of the results to fetch.Default Value: 0 (optional) (default to 0)
page_size = 50 # int | Results per page(max 100)Default Value: 50 (optional) (default to 50)
sort_orders = [swagger_client.SortOrder()] # list[SortOrder] | Sort criteria for the elements. (optional)
page_token = 'page_token_example' # str | Page Token of the next results to fetch.Default Value: '' (optional)
search_term = 'search_term_example' # str | This would be used to filter Tokens. Any Token having the specified string in its Name, ID and Tag would be filtered. (optional)
include_only_active_tokens = true # bool | Boolean value to indicate whether to list only active tokens or all tokens. By default, all tokens will be listed. (optional)

try:
    # List all Tokens
    api_response = api_instance.list_aggregated_tokens(account_identifier, api_key_type, org_identifier=org_identifier, project_identifier=project_identifier, parent_identifier=parent_identifier, api_key_identifier=api_key_identifier, identifiers=identifiers, page_index=page_index, page_size=page_size, sort_orders=sort_orders, page_token=page_token, search_term=search_term, include_only_active_tokens=include_only_active_tokens)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->list_aggregated_tokens: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **api_key_type** | **str**| This is the API Key type like Personal Access Key or Service Account Key. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **parent_identifier** | **str**| ID of API key&#x27;s Parent Service Account | [optional] 
 **api_key_identifier** | **str**| API key ID | [optional] 
 **identifiers** | [**list[str]**](str.md)| This is the list of Token IDs. Details specific to these IDs would be fetched. | [optional] 
 **page_index** | **int**| Page Index of the results to fetch.Default Value: 0 | [optional] [default to 0]
 **page_size** | **int**| Results per page(max 100)Default Value: 50 | [optional] [default to 50]
 **sort_orders** | [**list[SortOrder]**](SortOrder.md)| Sort criteria for the elements. | [optional] 
 **page_token** | **str**| Page Token of the next results to fetch.Default Value: &#x27;&#x27; | [optional] 
 **search_term** | **str**| This would be used to filter Tokens. Any Token having the specified string in its Name, ID and Tag would be filtered. | [optional] 
 **include_only_active_tokens** | **bool**| Boolean value to indicate whether to list only active tokens or all tokens. By default, all tokens will be listed. | [optional] 

### Return type

[**ResponseDTOPageResponseTokenAggregate**](ResponseDTOPageResponseTokenAggregate.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rotate_token**
> ResponseDTOString rotate_token(identifier, account_identifier, api_key_type, parent_identifier, api_key_identifier, rotate_timestamp=rotate_timestamp, org_identifier=org_identifier, project_identifier=project_identifier)

Rotate a Token

Rotates a Token for the given API Key Type.

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
api_instance = swagger_client.TokenApi(swagger_client.ApiClient(configuration))
identifier = 'identifier_example' # str | Token Identifier
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
api_key_type = 'api_key_type_example' # str | This is the API Key type like Personal Access Key or Service Account Key.
parent_identifier = 'parent_identifier_example' # str | ID of API key's Parent Service Account
api_key_identifier = 'api_key_identifier_example' # str | API key ID
rotate_timestamp = 789 # int | Time stamp when the Token is to be rotated (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Rotate a Token
    api_response = api_instance.rotate_token(identifier, account_identifier, api_key_type, parent_identifier, api_key_identifier, rotate_timestamp=rotate_timestamp, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->rotate_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Token Identifier | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **api_key_type** | **str**| This is the API Key type like Personal Access Key or Service Account Key. | 
 **parent_identifier** | **str**| ID of API key&#x27;s Parent Service Account | 
 **api_key_identifier** | **str**| API key ID | 
 **rotate_timestamp** | **int**| Time stamp when the Token is to be rotated | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOString**](ResponseDTOString.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_token**
> ResponseDTOToken update_token(account_identifier, identifier, body=body)

Update a Token

Updates a Token for the given API Key Type.

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
api_instance = swagger_client.TokenApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
identifier = 'identifier_example' # str | Token ID
body = swagger_client.Token() # Token |  (optional)

try:
    # Update a Token
    api_response = api_instance.update_token(account_identifier, identifier, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->update_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **identifier** | **str**| Token ID | 
 **body** | [**Token**](Token.md)|  | [optional] 

### Return type

[**ResponseDTOToken**](ResponseDTOToken.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml, text/plain
 - **Accept**: application/json, application/yaml, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_token**
> ResponseDTOToken validate_token(body, account_identifier)

Validate a Token

Validate a Token for the given account.

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
api_instance = swagger_client.TokenApi(swagger_client.ApiClient(configuration))
body = 'body_example' # str | 
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Validate a Token
    api_response = api_instance.validate_token(body, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->validate_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)|  | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**ResponseDTOToken**](ResponseDTOToken.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml, text/plain
 - **Accept**: application/json, application/yaml, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

