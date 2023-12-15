# swagger_client.ServiceAccountApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_service_account**](ServiceAccountApi.md#create_service_account) | **POST** /ng/api/serviceaccount | Create a Service Account
[**delete_service_account**](ServiceAccountApi.md#delete_service_account) | **DELETE** /ng/api/serviceaccount/{identifier} | Delete a Service Account
[**get_aggregated_service_account**](ServiceAccountApi.md#get_aggregated_service_account) | **GET** /ng/api/serviceaccount/aggregate/{identifier} | Get Service Account In Scope
[**list_aggregated_service_accounts**](ServiceAccountApi.md#list_aggregated_service_accounts) | **GET** /ng/api/serviceaccount/aggregate | List aggregated Service Accounts
[**list_service_account**](ServiceAccountApi.md#list_service_account) | **GET** /ng/api/serviceaccount | Get Service Accounts
[**update_service_account**](ServiceAccountApi.md#update_service_account) | **PUT** /ng/api/serviceaccount/{identifier} | Update a Service Account

# **create_service_account**
> ResponseDTOServiceAccount create_service_account(body, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Create a Service Account

Creates a new Service Account.

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
api_instance = swagger_client.ServiceAccountApi(swagger_client.ApiClient(configuration))
body = swagger_client.ServiceAccount() # ServiceAccount | Details required to create Service Account
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Create a Service Account
    api_response = api_instance.create_service_account(body, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceAccountApi->create_service_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ServiceAccount**](ServiceAccount.md)| Details required to create Service Account | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOServiceAccount**](ResponseDTOServiceAccount.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml, text/plain
 - **Accept**: application/json, application/yaml, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_service_account**
> ResponseDTOBoolean delete_service_account(account_identifier, identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Delete a Service Account

Deletes a Service Account corresponding to the given Service Account ID.

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
api_instance = swagger_client.ServiceAccountApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
identifier = 'identifier_example' # str | Service Account ID
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Delete a Service Account
    api_response = api_instance.delete_service_account(account_identifier, identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceAccountApi->delete_service_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **identifier** | **str**| Service Account ID | 
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

# **get_aggregated_service_account**
> ResponseDTOServiceAccountAggregate get_aggregated_service_account(account_identifier, identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Get Service Account In Scope

Gets the list of Service Accounts in the given scope.

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
api_instance = swagger_client.ServiceAccountApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
identifier = 'identifier_example' # str | Service Account IDr
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Get Service Account In Scope
    api_response = api_instance.get_aggregated_service_account(account_identifier, identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceAccountApi->get_aggregated_service_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **identifier** | **str**| Service Account IDr | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOServiceAccountAggregate**](ResponseDTOServiceAccountAggregate.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_aggregated_service_accounts**
> ResponseDTOPageResponseServiceAccountAggregate list_aggregated_service_accounts(account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, identifiers=identifiers, page_index=page_index, page_size=page_size, sort_orders=sort_orders, page_token=page_token, search_term=search_term)

List aggregated Service Accounts

Fetches the list of Aggregated Service Accounts corresponding to the request's filter criteria.

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
api_instance = swagger_client.ServiceAccountApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
identifiers = ['identifiers_example'] # list[str] | This is the list of Service Account IDs. Details specific to these IDs would be fetched. (optional)
page_index = 0 # int | Page Index of the results to fetch.Default Value: 0 (optional) (default to 0)
page_size = 50 # int | Results per page(max 100)Default Value: 50 (optional) (default to 50)
sort_orders = [swagger_client.SortOrder()] # list[SortOrder] | Sort criteria for the elements. (optional)
page_token = 'page_token_example' # str | Page Token of the next results to fetch.Default Value: '' (optional)
search_term = 'search_term_example' # str | This would be used to filter Service Accounts. Any Service Account having the specified string in its Name, ID and Tag would be filtered. (optional)

try:
    # List aggregated Service Accounts
    api_response = api_instance.list_aggregated_service_accounts(account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, identifiers=identifiers, page_index=page_index, page_size=page_size, sort_orders=sort_orders, page_token=page_token, search_term=search_term)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceAccountApi->list_aggregated_service_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **identifiers** | [**list[str]**](str.md)| This is the list of Service Account IDs. Details specific to these IDs would be fetched. | [optional] 
 **page_index** | **int**| Page Index of the results to fetch.Default Value: 0 | [optional] [default to 0]
 **page_size** | **int**| Results per page(max 100)Default Value: 50 | [optional] [default to 50]
 **sort_orders** | [**list[SortOrder]**](SortOrder.md)| Sort criteria for the elements. | [optional] 
 **page_token** | **str**| Page Token of the next results to fetch.Default Value: &#x27;&#x27; | [optional] 
 **search_term** | **str**| This would be used to filter Service Accounts. Any Service Account having the specified string in its Name, ID and Tag would be filtered. | [optional] 

### Return type

[**ResponseDTOPageResponseServiceAccountAggregate**](ResponseDTOPageResponseServiceAccountAggregate.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_service_account**
> ResponseDTOListServiceAccount list_service_account(account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, identifiers=identifiers)

Get Service Accounts

Fetches list of Service Accounts for the given filter criteria.

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
api_instance = swagger_client.ServiceAccountApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
identifiers = ['identifiers_example'] # list[str] | This is the list of Service Account IDs. Details specific to these IDs would be fetched. (optional)

try:
    # Get Service Accounts
    api_response = api_instance.list_service_account(account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, identifiers=identifiers)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceAccountApi->list_service_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **identifiers** | [**list[str]**](str.md)| This is the list of Service Account IDs. Details specific to these IDs would be fetched. | [optional] 

### Return type

[**ResponseDTOListServiceAccount**](ResponseDTOListServiceAccount.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_service_account**
> ResponseDTOServiceAccount update_service_account(body, account_identifier, identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Update a Service Account

Updates details of the Service Account for the given Service Account ID.

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
api_instance = swagger_client.ServiceAccountApi(swagger_client.ApiClient(configuration))
body = swagger_client.ServiceAccount() # ServiceAccount | Details of the updated Service Account
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
identifier = 'identifier_example' # str | Service Account ID
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Update a Service Account
    api_response = api_instance.update_service_account(body, account_identifier, identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceAccountApi->update_service_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ServiceAccount**](ServiceAccount.md)| Details of the updated Service Account | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **identifier** | **str**| Service Account ID | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOServiceAccount**](ResponseDTOServiceAccount.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml, text/plain
 - **Accept**: application/json, application/yaml, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

