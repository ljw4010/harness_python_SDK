# swagger_client.RolesApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_role**](RolesApi.md#delete_role) | **DELETE** /authz/api/roles/{identifier} | Delete Role
[**get_role**](RolesApi.md#get_role) | **GET** /authz/api/roles/{identifier} | Get Role
[**get_role_list**](RolesApi.md#get_role_list) | **GET** /authz/api/roles | List Roles
[**post_role**](RolesApi.md#post_role) | **POST** /authz/api/roles | Create Role
[**put_role**](RolesApi.md#put_role) | **PUT** /authz/api/roles/{identifier} | Update Role

# **delete_role**
> ResponseDTORoleResponse delete_role(identifier, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Delete Role

Delete a Custom Role in a scope

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
api_instance = swagger_client.RolesApi(swagger_client.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of the Role
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Delete Role
    api_response = api_instance.delete_role(identifier, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->delete_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of the Role | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTORoleResponse**](ResponseDTORoleResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role**
> ResponseDTORoleResponse get_role(identifier, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Get Role

Get a Role by identifier

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
api_instance = swagger_client.RolesApi(swagger_client.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of the Role
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Get Role
    api_response = api_instance.get_role(identifier, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->get_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of the Role | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTORoleResponse**](ResponseDTORoleResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_list**
> ResponseDTOPageResponseRoleWithPrincipalCountResponse get_role_list(account_identifier, page_index=page_index, page_size=page_size, sort_orders=sort_orders, page_token=page_token, org_identifier=org_identifier, project_identifier=project_identifier, search_term=search_term)

List Roles

List roles in the given scope

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
api_instance = swagger_client.RolesApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
page_index = 0 # int | Page Index of the results to fetch.Default Value: 0 (optional) (default to 0)
page_size = 50 # int | Results per page(max 100)Default Value: 50 (optional) (default to 50)
sort_orders = [swagger_client.SortOrder()] # list[SortOrder] | Sort criteria for the elements. (optional)
page_token = 'page_token_example' # str | Page Token of the next results to fetch.Default Value: '' (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
search_term = 'search_term_example' # str | Search roles by name/identifier (optional)

try:
    # List Roles
    api_response = api_instance.get_role_list(account_identifier, page_index=page_index, page_size=page_size, sort_orders=sort_orders, page_token=page_token, org_identifier=org_identifier, project_identifier=project_identifier, search_term=search_term)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->get_role_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **page_index** | **int**| Page Index of the results to fetch.Default Value: 0 | [optional] [default to 0]
 **page_size** | **int**| Results per page(max 100)Default Value: 50 | [optional] [default to 50]
 **sort_orders** | [**list[SortOrder]**](SortOrder.md)| Sort criteria for the elements. | [optional] 
 **page_token** | **str**| Page Token of the next results to fetch.Default Value: &#x27;&#x27; | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **search_term** | **str**| Search roles by name/identifier | [optional] 

### Return type

[**ResponseDTOPageResponseRoleWithPrincipalCountResponse**](ResponseDTOPageResponseRoleWithPrincipalCountResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_role**
> ResponseDTORoleResponse post_role(body, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Create Role

Create a Custom Role in a scope

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
api_instance = swagger_client.RolesApi(swagger_client.ApiClient(configuration))
body = swagger_client.Role() # Role | Role entity
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Create Role
    api_response = api_instance.post_role(body, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->post_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Role**](Role.md)| Role entity | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTORoleResponse**](ResponseDTORoleResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_role**
> ResponseDTORoleResponse put_role(body, account_identifier, identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Update Role

Update a Custom Role by identifier

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
api_instance = swagger_client.RolesApi(swagger_client.ApiClient(configuration))
body = swagger_client.Role() # Role | Updated Role entity
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
identifier = 'identifier_example' # str | Identifier of the Role
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Update Role
    api_response = api_instance.put_role(body, account_identifier, identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->put_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Role**](Role.md)| Updated Role entity | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **identifier** | **str**| Identifier of the Role | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTORoleResponse**](ResponseDTORoleResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

