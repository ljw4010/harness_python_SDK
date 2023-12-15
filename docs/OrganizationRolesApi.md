# swagger_client.OrganizationRolesApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_role_org**](OrganizationRolesApi.md#create_role_org) | **POST** /v1/orgs/{org}/roles | Create a Role
[**delete_role_org**](OrganizationRolesApi.md#delete_role_org) | **DELETE** /v1/orgs/{org}/roles/{role} | Delete a Role
[**get_role_org**](OrganizationRolesApi.md#get_role_org) | **GET** /v1/orgs/{org}/roles/{role} | Retrieve a Role
[**list_roles_org**](OrganizationRolesApi.md#list_roles_org) | **GET** /v1/orgs/{org}/roles | List Roles
[**update_role_org**](OrganizationRolesApi.md#update_role_org) | **PUT** /v1/orgs/{org}/roles/{role} | Update a Role

# **create_role_org**
> RolesResponse create_role_org(body, org, harness_account=harness_account)

Create a Role

Creates a custom Role in the Organization scope.

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
api_instance = swagger_client.OrganizationRolesApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateRoleRequest() # CreateRoleRequest | Role Request body
org = 'org_example' # str | Organization identifier
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)

try:
    # Create a Role
    api_response = api_instance.create_role_org(body, org, harness_account=harness_account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationRolesApi->create_role_org: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateRoleRequest**](CreateRoleRequest.md)| Role Request body | 
 **org** | **str**| Organization identifier | 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 

### Return type

[**RolesResponse**](RolesResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_role_org**
> RolesResponse delete_role_org(org, role, harness_account=harness_account)

Delete a Role

Deletes a custom Role from Organization scope.

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
api_instance = swagger_client.OrganizationRolesApi(swagger_client.ApiClient(configuration))
org = 'org_example' # str | Organization identifier
role = 'role_example' # str | Role identifier
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)

try:
    # Delete a Role
    api_response = api_instance.delete_role_org(org, role, harness_account=harness_account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationRolesApi->delete_role_org: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| Organization identifier | 
 **role** | **str**| Role identifier | 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 

### Return type

[**RolesResponse**](RolesResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_org**
> RolesResponse get_role_org(org, role, harness_account=harness_account)

Retrieve a Role

Retrieves a Role from Organization scope.

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
api_instance = swagger_client.OrganizationRolesApi(swagger_client.ApiClient(configuration))
org = 'org_example' # str | Organization identifier
role = 'role_example' # str | Role identifier
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)

try:
    # Retrieve a Role
    api_response = api_instance.get_role_org(org, role, harness_account=harness_account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationRolesApi->get_role_org: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| Organization identifier | 
 **role** | **str**| Role identifier | 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 

### Return type

[**RolesResponse**](RolesResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_roles_org**
> list[RolesResponse] list_roles_org(org, page=page, limit=limit, search_term=search_term, harness_account=harness_account, sort=sort, order=order)

List Roles

Returns a list of Roles present in the Organization scope.

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
api_instance = swagger_client.OrganizationRolesApi(swagger_client.ApiClient(configuration))
org = 'org_example' # str | Organization identifier
page = 0 # int | Pagination page number strategy: Specify the page number within the paginated collection related to the number of items on each page. (optional) (default to 0)
limit = 30 # int | Pagination: Number of items to return. (optional) (default to 30)
search_term = 'search_term_example' # str | This would be used to filter resources having attributes matching the search term. (optional)
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)
sort = 'sort_example' # str | Parameter on the basis of which sorting is done. (optional)
order = 'order_example' # str | Order on the basis of which sorting is done. (optional)

try:
    # List Roles
    api_response = api_instance.list_roles_org(org, page=page, limit=limit, search_term=search_term, harness_account=harness_account, sort=sort, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationRolesApi->list_roles_org: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| Organization identifier | 
 **page** | **int**| Pagination page number strategy: Specify the page number within the paginated collection related to the number of items on each page. | [optional] [default to 0]
 **limit** | **int**| Pagination: Number of items to return. | [optional] [default to 30]
 **search_term** | **str**| This would be used to filter resources having attributes matching the search term. | [optional] 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 
 **sort** | **str**| Parameter on the basis of which sorting is done. | [optional] 
 **order** | **str**| Order on the basis of which sorting is done. | [optional] 

### Return type

[**list[RolesResponse]**](RolesResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_role_org**
> RolesResponse update_role_org(body, org, role, harness_account=harness_account)

Update a Role

Updates a Role from Organization scope.

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
api_instance = swagger_client.OrganizationRolesApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateRoleRequest() # CreateRoleRequest | Role Request body
org = 'org_example' # str | Organization identifier
role = 'role_example' # str | Role identifier
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)

try:
    # Update a Role
    api_response = api_instance.update_role_org(body, org, role, harness_account=harness_account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationRolesApi->update_role_org: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateRoleRequest**](CreateRoleRequest.md)| Role Request body | 
 **org** | **str**| Organization identifier | 
 **role** | **str**| Role identifier | 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 

### Return type

[**RolesResponse**](RolesResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

