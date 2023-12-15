# harness_python_sdk.VariablesApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_variable**](VariablesApi.md#create_variable) | **POST** /ng/api/variables | Creates a Variable.
[**delete_variable**](VariablesApi.md#delete_variable) | **DELETE** /ng/api/variables/{identifier} | Deletes Variable by ID.
[**get_variable**](VariablesApi.md#get_variable) | **GET** /ng/api/variables/{identifier} | Get the Variable by scope identifiers and variable identifier.
[**get_variable_list**](VariablesApi.md#get_variable_list) | **GET** /ng/api/variables | Fetches the list of Variables.
[**update_variable**](VariablesApi.md#update_variable) | **PUT** /ng/api/variables | Updates the Variable.

# **create_variable**
> ResponseDTOVariableResponseDTO create_variable(body, account_identifier)

Creates a Variable.

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
api_instance = harness_python_sdk.VariablesApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.VariableRequestDTO() # VariableRequestDTO | Details of the Variable to create.
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Creates a Variable.
    api_response = api_instance.create_variable(body, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablesApi->create_variable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VariableRequestDTO**](VariableRequestDTO.md)| Details of the Variable to create. | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**ResponseDTOVariableResponseDTO**](ResponseDTOVariableResponseDTO.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_variable**
> ResponseDTOBoolean delete_variable(account_identifier, identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Deletes Variable by ID.

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
api_instance = harness_python_sdk.VariablesApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
identifier = 'identifier_example' # str | Variable ID
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Deletes Variable by ID.
    api_response = api_instance.delete_variable(account_identifier, identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablesApi->delete_variable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **identifier** | **str**| Variable ID | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOBoolean**](ResponseDTOBoolean.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_variable**
> ResponseDTOVariableResponseDTO get_variable(identifier, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Get the Variable by scope identifiers and variable identifier.

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
api_instance = harness_python_sdk.VariablesApi(harness_python_sdk.ApiClient(configuration))
identifier = 'identifier_example' # str | Variable ID
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Get the Variable by scope identifiers and variable identifier.
    api_response = api_instance.get_variable(identifier, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablesApi->get_variable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Variable ID | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOVariableResponseDTO**](ResponseDTOVariableResponseDTO.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_variable_list**
> ResponseDTOPageResponseVariableResponseDTO get_variable_list(account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, search_term=search_term, include_variables_from_every_sub_scope=include_variables_from_every_sub_scope, page_index=page_index, page_size=page_size, sort_orders=sort_orders, page_token=page_token)

Fetches the list of Variables.

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
api_instance = harness_python_sdk.VariablesApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
search_term = 'search_term_example' # str | This would be used to filter Variables. Any Variable having the specified string in its Name or ID would be filtered. (optional)
include_variables_from_every_sub_scope = false # bool | Specify whether or not to include all the Variables accessible at the scope. For eg if set as true, at the Project scope we will get org and account Variable also in the response. (optional) (default to false)
page_index = 0 # int | Page Index of the results to fetch.Default Value: 0 (optional) (default to 0)
page_size = 50 # int | Results per page(max 100)Default Value: 50 (optional) (default to 50)
sort_orders = [harness_python_sdk.SortOrder()] # list[SortOrder] | Sort criteria for the elements. (optional)
page_token = 'page_token_example' # str | Page Token of the next results to fetch.Default Value: '' (optional)

try:
    # Fetches the list of Variables.
    api_response = api_instance.get_variable_list(account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, search_term=search_term, include_variables_from_every_sub_scope=include_variables_from_every_sub_scope, page_index=page_index, page_size=page_size, sort_orders=sort_orders, page_token=page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablesApi->get_variable_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **search_term** | **str**| This would be used to filter Variables. Any Variable having the specified string in its Name or ID would be filtered. | [optional] 
 **include_variables_from_every_sub_scope** | **bool**| Specify whether or not to include all the Variables accessible at the scope. For eg if set as true, at the Project scope we will get org and account Variable also in the response. | [optional] [default to false]
 **page_index** | **int**| Page Index of the results to fetch.Default Value: 0 | [optional] [default to 0]
 **page_size** | **int**| Results per page(max 100)Default Value: 50 | [optional] [default to 50]
 **sort_orders** | [**list[SortOrder]**](SortOrder.md)| Sort criteria for the elements. | [optional] 
 **page_token** | **str**| Page Token of the next results to fetch.Default Value: &#x27;&#x27; | [optional] 

### Return type

[**ResponseDTOPageResponseVariableResponseDTO**](ResponseDTOPageResponseVariableResponseDTO.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_variable**
> ResponseDTOVariableResponseDTO update_variable(body, account_identifier)

Updates the Variable.

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
api_instance = harness_python_sdk.VariablesApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.VariableRequestDTO() # VariableRequestDTO | Details of the variable to update.
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Updates the Variable.
    api_response = api_instance.update_variable(body, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablesApi->update_variable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VariableRequestDTO**](VariableRequestDTO.md)| Details of the variable to update. | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**ResponseDTOVariableResponseDTO**](ResponseDTOVariableResponseDTO.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

