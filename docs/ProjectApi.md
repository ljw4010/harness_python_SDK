# swagger_client.ProjectApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_project**](ProjectApi.md#delete_project) | **DELETE** /ng/api/projects/{identifier} | Delete a Project
[**get_project**](ProjectApi.md#get_project) | **GET** /ng/api/projects/{identifier} | List Project details
[**get_project_list**](ProjectApi.md#get_project_list) | **GET** /ng/api/projects | List all Projects for a user
[**get_project_list_with_multi_org_filter**](ProjectApi.md#get_project_list_with_multi_org_filter) | **GET** /ng/api/projects/list | List user&#x27;s project with support to filter by multiple organizations
[**post_project**](ProjectApi.md#post_project) | **POST** /ng/api/projects | Create a Project
[**put_project**](ProjectApi.md#put_project) | **PUT** /ng/api/projects/{identifier} | Update a Project

# **delete_project**
> ResponseDTOBoolean delete_project(identifier, account_identifier, if_match=if_match, org_identifier=org_identifier)

Delete a Project

Deletes a Project corresponding to the given ID.

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
api_instance = swagger_client.ProjectApi(swagger_client.ApiClient(configuration))
identifier = 'identifier_example' # str | Project Identifier for the Entity.
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
if_match = 'if_match_example' # str | Version number of Project (optional)
org_identifier = 'default' # str | This is the Organization Identifier for the Project. By default, the Default Organization's Identifier is considered. (optional) (default to default)

try:
    # Delete a Project
    api_response = api_instance.delete_project(identifier, account_identifier, if_match=if_match, org_identifier=org_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->delete_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Project Identifier for the Entity. | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **if_match** | **str**| Version number of Project | [optional] 
 **org_identifier** | **str**| This is the Organization Identifier for the Project. By default, the Default Organization&#x27;s Identifier is considered. | [optional] [default to default]

### Return type

[**ResponseDTOBoolean**](ResponseDTOBoolean.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project**
> ResponseDTOProjectResponse get_project(identifier, account_identifier, org_identifier=org_identifier)

List Project details

Lists a Project's details for the given ID.

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
api_instance = swagger_client.ProjectApi(swagger_client.ApiClient(configuration))
identifier = 'identifier_example' # str | Project Identifier for the Entity.
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'default' # str | Organization identifier for the project. If left empty, Default Organization is assumed (optional) (default to default)

try:
    # List Project details
    api_response = api_instance.get_project(identifier, account_identifier, org_identifier=org_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Project Identifier for the Entity. | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization identifier for the project. If left empty, Default Organization is assumed | [optional] [default to default]

### Return type

[**ResponseDTOProjectResponse**](ResponseDTOProjectResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_list**
> ResponseDTOPageResponseProjectResponse get_project_list(account_identifier, org_identifier=org_identifier, has_module=has_module, identifiers=identifiers, module_type=module_type, search_term=search_term, only_favorites=only_favorites, page_index=page_index, page_size=page_size, sort_orders=sort_orders, page_token=page_token)

List all Projects for a user

Lists all Projects the user is a member of by using the user's API key token.

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
api_instance = swagger_client.ProjectApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
has_module = true # bool | This boolean specifies whether to Filter Projects which has the Module of type passed in the module type parameter or to Filter Projects which does not has the Module of type passed in the module type parameter (optional) (default to true)
identifiers = ['identifiers_example'] # list[str] | This is the list of Project IDs. Details specific to these IDs would be fetched. (optional)
module_type = 'module_type_example' # str | Filter Projects by module type (optional)
search_term = 'search_term_example' # str | This would be used to filter Projects. Any Project having the specified string in its Name, ID and Tag would be filtered. (optional)
only_favorites = false # bool |  (optional) (default to false)
page_index = 0 # int | Page Index of the results to fetch.Default Value: 0 (optional) (default to 0)
page_size = 50 # int | Results per page(max 100)Default Value: 50 (optional) (default to 50)
sort_orders = [swagger_client.SortOrder()] # list[SortOrder] | Sort criteria for the elements. (optional)
page_token = 'page_token_example' # str | Page Token of the next results to fetch.Default Value: '' (optional)

try:
    # List all Projects for a user
    api_response = api_instance.get_project_list(account_identifier, org_identifier=org_identifier, has_module=has_module, identifiers=identifiers, module_type=module_type, search_term=search_term, only_favorites=only_favorites, page_index=page_index, page_size=page_size, sort_orders=sort_orders, page_token=page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_project_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **has_module** | **bool**| This boolean specifies whether to Filter Projects which has the Module of type passed in the module type parameter or to Filter Projects which does not has the Module of type passed in the module type parameter | [optional] [default to true]
 **identifiers** | [**list[str]**](str.md)| This is the list of Project IDs. Details specific to these IDs would be fetched. | [optional] 
 **module_type** | **str**| Filter Projects by module type | [optional] 
 **search_term** | **str**| This would be used to filter Projects. Any Project having the specified string in its Name, ID and Tag would be filtered. | [optional] 
 **only_favorites** | **bool**|  | [optional] [default to false]
 **page_index** | **int**| Page Index of the results to fetch.Default Value: 0 | [optional] [default to 0]
 **page_size** | **int**| Results per page(max 100)Default Value: 50 | [optional] [default to 50]
 **sort_orders** | [**list[SortOrder]**](SortOrder.md)| Sort criteria for the elements. | [optional] 
 **page_token** | **str**| Page Token of the next results to fetch.Default Value: &#x27;&#x27; | [optional] 

### Return type

[**ResponseDTOPageResponseProjectResponse**](ResponseDTOPageResponseProjectResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_list_with_multi_org_filter**
> ResponseDTOPageResponseProjectResponse get_project_list_with_multi_org_filter(account_identifier, org_identifiers=org_identifiers, has_module=has_module, identifiers=identifiers, module_type=module_type, search_term=search_term, only_favorites=only_favorites, page_index=page_index, page_size=page_size, sort_orders=sort_orders, page_token=page_token)

List user's project with support to filter by multiple organizations

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
api_instance = swagger_client.ProjectApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifiers = ['org_identifiers_example'] # list[str] | List of Organization Identifiers for the Entities. (optional)
has_module = true # bool | This boolean specifies whether to Filter Projects which has the Module of type passed in the module type parameter or to Filter Projects which does not has the Module of type passed in the module type parameter (optional) (default to true)
identifiers = ['identifiers_example'] # list[str] | This is the list of Project Identifiers. Details specific to these IDs would be fetched. (optional)
module_type = 'module_type_example' # str | Filter Projects by module type (optional)
search_term = 'search_term_example' # str | Filter Projects by searching for this word in Name, Id, and Tag (optional)
only_favorites = false # bool |  (optional) (default to false)
page_index = 0 # int | Page Index of the results to fetch.Default Value: 0 (optional) (default to 0)
page_size = 50 # int | Results per page(max 100)Default Value: 50 (optional) (default to 50)
sort_orders = [swagger_client.SortOrder()] # list[SortOrder] | Sort criteria for the elements. (optional)
page_token = 'page_token_example' # str | Page Token of the next results to fetch.Default Value: '' (optional)

try:
    # List user's project with support to filter by multiple organizations
    api_response = api_instance.get_project_list_with_multi_org_filter(account_identifier, org_identifiers=org_identifiers, has_module=has_module, identifiers=identifiers, module_type=module_type, search_term=search_term, only_favorites=only_favorites, page_index=page_index, page_size=page_size, sort_orders=sort_orders, page_token=page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_project_list_with_multi_org_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifiers** | [**list[str]**](str.md)| List of Organization Identifiers for the Entities. | [optional] 
 **has_module** | **bool**| This boolean specifies whether to Filter Projects which has the Module of type passed in the module type parameter or to Filter Projects which does not has the Module of type passed in the module type parameter | [optional] [default to true]
 **identifiers** | [**list[str]**](str.md)| This is the list of Project Identifiers. Details specific to these IDs would be fetched. | [optional] 
 **module_type** | **str**| Filter Projects by module type | [optional] 
 **search_term** | **str**| Filter Projects by searching for this word in Name, Id, and Tag | [optional] 
 **only_favorites** | **bool**|  | [optional] [default to false]
 **page_index** | **int**| Page Index of the results to fetch.Default Value: 0 | [optional] [default to 0]
 **page_size** | **int**| Results per page(max 100)Default Value: 50 | [optional] [default to 50]
 **sort_orders** | [**list[SortOrder]**](SortOrder.md)| Sort criteria for the elements. | [optional] 
 **page_token** | **str**| Page Token of the next results to fetch.Default Value: &#x27;&#x27; | [optional] 

### Return type

[**ResponseDTOPageResponseProjectResponse**](ResponseDTOPageResponseProjectResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_project**
> ResponseDTOProjectResponse post_project(body, account_identifier, org_identifier=org_identifier)

Create a Project

Creates a new Harness Project.

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
api_instance = swagger_client.ProjectApi(swagger_client.ApiClient(configuration))
body = swagger_client.ProjectRequest1() # ProjectRequest1 | Details of the Project to create
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'default' # str | Organization identifier for the Project. If left empty, the Project is created under Default Organization (optional) (default to default)

try:
    # Create a Project
    api_response = api_instance.post_project(body, account_identifier, org_identifier=org_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->post_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProjectRequest1**](ProjectRequest1.md)| Details of the Project to create | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization identifier for the Project. If left empty, the Project is created under Default Organization | [optional] [default to default]

### Return type

[**ResponseDTOProjectResponse**](ResponseDTOProjectResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_project**
> ResponseDTOProjectResponse put_project(body, account_identifier, identifier, if_match=if_match, org_identifier=org_identifier)

Update a Project

Updates Project details for the given ID.

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
api_instance = swagger_client.ProjectApi(swagger_client.ApiClient(configuration))
body = swagger_client.ProjectRequest1() # ProjectRequest1 | This is the updated Project. Please provide values for all fields, not just the fields you are updating
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
identifier = 'identifier_example' # str | Project Identifier for the Entity.
if_match = 'if_match_example' # str | Version number of Project (optional)
org_identifier = 'default' # str | Organization identifier for the Project. If left empty, Default Organization is assumed (optional) (default to default)

try:
    # Update a Project
    api_response = api_instance.put_project(body, account_identifier, identifier, if_match=if_match, org_identifier=org_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->put_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProjectRequest1**](ProjectRequest1.md)| This is the updated Project. Please provide values for all fields, not just the fields you are updating | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **identifier** | **str**| Project Identifier for the Entity. | 
 **if_match** | **str**| Version number of Project | [optional] 
 **org_identifier** | **str**| Organization identifier for the Project. If left empty, Default Organization is assumed | [optional] [default to default]

### Return type

[**ResponseDTOProjectResponse**](ResponseDTOProjectResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

