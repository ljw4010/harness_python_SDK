# harness_python_sdk.OrganizationResourceGroupsApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_resource_group_org**](OrganizationResourceGroupsApi.md#create_resource_group_org) | **POST** /v1/orgs/{org}/resource-groups | Create a Resource Group
[**delete_resource_group_org**](OrganizationResourceGroupsApi.md#delete_resource_group_org) | **DELETE** /v1/orgs/{org}/resource-groups/{resource-group} | Delete a Resource Group
[**get_resource_group_org**](OrganizationResourceGroupsApi.md#get_resource_group_org) | **GET** /v1/orgs/{org}/resource-groups/{resource-group} | Retrieve a Resource Group
[**list_resource_groups_org**](OrganizationResourceGroupsApi.md#list_resource_groups_org) | **GET** /v1/orgs/{org}/resource-groups | List Resource Groups
[**update_resource_group_org**](OrganizationResourceGroupsApi.md#update_resource_group_org) | **PUT** /v1/orgs/{org}/resource-groups/{resource-group} | Update a Resource Group

# **create_resource_group_org**
> ResourceGroupsResponse create_resource_group_org(body, org, harness_account=harness_account)

Create a Resource Group

Creates a custom Resource Group in the Organization scope.

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
api_instance = harness_python_sdk.OrganizationResourceGroupsApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.CreateResourceGroupRequest() # CreateResourceGroupRequest | Resource Group request body
org = 'org_example' # str | Organization identifier
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)

try:
    # Create a Resource Group
    api_response = api_instance.create_resource_group_org(body, org, harness_account=harness_account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationResourceGroupsApi->create_resource_group_org: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateResourceGroupRequest**](CreateResourceGroupRequest.md)| Resource Group request body | 
 **org** | **str**| Organization identifier | 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 

### Return type

[**ResourceGroupsResponse**](ResourceGroupsResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_resource_group_org**
> ResourceGroupsResponse delete_resource_group_org(org, resource_group, harness_account=harness_account)

Delete a Resource Group

Deletes a custom Resource Group from Organization scope.

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
api_instance = harness_python_sdk.OrganizationResourceGroupsApi(harness_python_sdk.ApiClient(configuration))
org = 'org_example' # str | Organization identifier
resource_group = 'resource_group_example' # str | Resource Group identifier
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)

try:
    # Delete a Resource Group
    api_response = api_instance.delete_resource_group_org(org, resource_group, harness_account=harness_account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationResourceGroupsApi->delete_resource_group_org: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| Organization identifier | 
 **resource_group** | **str**| Resource Group identifier | 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 

### Return type

[**ResourceGroupsResponse**](ResourceGroupsResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_group_org**
> ResourceGroupsResponse get_resource_group_org(org, resource_group, harness_account=harness_account)

Retrieve a Resource Group

Retrieves a Resource Group from Organization scope.

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
api_instance = harness_python_sdk.OrganizationResourceGroupsApi(harness_python_sdk.ApiClient(configuration))
org = 'org_example' # str | Organization identifier
resource_group = 'resource_group_example' # str | Resource Group identifier
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)

try:
    # Retrieve a Resource Group
    api_response = api_instance.get_resource_group_org(org, resource_group, harness_account=harness_account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationResourceGroupsApi->get_resource_group_org: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| Organization identifier | 
 **resource_group** | **str**| Resource Group identifier | 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 

### Return type

[**ResourceGroupsResponse**](ResourceGroupsResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_resource_groups_org**
> list[ResourceGroupsResponse] list_resource_groups_org(org, page=page, limit=limit, search_term=search_term, harness_account=harness_account, sort=sort, order=order)

List Resource Groups

Returns a list of Resource Groups present in the Organization scope.

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
api_instance = harness_python_sdk.OrganizationResourceGroupsApi(harness_python_sdk.ApiClient(configuration))
org = 'org_example' # str | Organization identifier
page = 0 # int | Pagination page number strategy: Specify the page number within the paginated collection related to the number of items on each page. (optional) (default to 0)
limit = 30 # int | Pagination: Number of items to return. (optional) (default to 30)
search_term = 'search_term_example' # str | This would be used to filter resources having attributes matching the search term. (optional)
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)
sort = 'sort_example' # str | Parameter on the basis of which sorting is done. (optional)
order = 'order_example' # str | Order on the basis of which sorting is done. (optional)

try:
    # List Resource Groups
    api_response = api_instance.list_resource_groups_org(org, page=page, limit=limit, search_term=search_term, harness_account=harness_account, sort=sort, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationResourceGroupsApi->list_resource_groups_org: %s\n" % e)
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

[**list[ResourceGroupsResponse]**](ResourceGroupsResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_resource_group_org**
> ResourceGroupsResponse update_resource_group_org(body, org, resource_group, harness_account=harness_account)

Update a Resource Group

Updates a Resource Group from Organization scope.

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
api_instance = harness_python_sdk.OrganizationResourceGroupsApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.CreateResourceGroupRequest() # CreateResourceGroupRequest | Resource Group request body
org = 'org_example' # str | Organization identifier
resource_group = 'resource_group_example' # str | Resource Group identifier
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)

try:
    # Update a Resource Group
    api_response = api_instance.update_resource_group_org(body, org, resource_group, harness_account=harness_account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationResourceGroupsApi->update_resource_group_org: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateResourceGroupRequest**](CreateResourceGroupRequest.md)| Resource Group request body | 
 **org** | **str**| Organization identifier | 
 **resource_group** | **str**| Resource Group identifier | 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 

### Return type

[**ResourceGroupsResponse**](ResourceGroupsResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

