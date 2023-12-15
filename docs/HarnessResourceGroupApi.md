# harness_python_sdk.HarnessResourceGroupApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_resource_group_v2**](HarnessResourceGroupApi.md#create_resource_group_v2) | **POST** /resourcegroup/api/v2/resourcegroup | Create Resource Group
[**delete_resource_group_v2**](HarnessResourceGroupApi.md#delete_resource_group_v2) | **DELETE** /resourcegroup/api/v2/resourcegroup/{identifier} | Delete Resource Group
[**get_filter_resource_group_list_v2**](HarnessResourceGroupApi.md#get_filter_resource_group_list_v2) | **POST** /resourcegroup/api/v2/resourcegroup/filter | List Resource Groups by filter
[**get_resource_group_list_v2**](HarnessResourceGroupApi.md#get_resource_group_list_v2) | **GET** /resourcegroup/api/v2/resourcegroup | List Resource Groups
[**get_resource_group_v2**](HarnessResourceGroupApi.md#get_resource_group_v2) | **GET** /resourcegroup/api/v2/resourcegroup/{identifier} | Get Resource Group
[**update_resource_group_v2**](HarnessResourceGroupApi.md#update_resource_group_v2) | **PUT** /resourcegroup/api/v2/resourcegroup/{identifier} | Update Resource Group

# **create_resource_group_v2**
> ResponseDTOResourceGroupV2Response create_resource_group_v2(body, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Create Resource Group

Create a resource group

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
api_instance = harness_python_sdk.HarnessResourceGroupApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.ResourceGroupV2Request() # ResourceGroupV2Request | This contains the details required to create a Resource Group
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Create Resource Group
    api_response = api_instance.create_resource_group_v2(body, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HarnessResourceGroupApi->create_resource_group_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ResourceGroupV2Request**](ResourceGroupV2Request.md)| This contains the details required to create a Resource Group | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOResourceGroupV2Response**](ResponseDTOResourceGroupV2Response.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_resource_group_v2**
> ResponseDTOBoolean delete_resource_group_v2(identifier, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Delete Resource Group

Delete a resource group

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
api_instance = harness_python_sdk.HarnessResourceGroupApi(harness_python_sdk.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier for the Entity.
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Delete Resource Group
    api_response = api_instance.delete_resource_group_v2(identifier, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HarnessResourceGroupApi->delete_resource_group_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier for the Entity. | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
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

# **get_filter_resource_group_list_v2**
> ResponseDTOPageResponseResourceGroupV2Response get_filter_resource_group_list_v2(body, account_identifier, page_index=page_index, page_size=page_size, sort_orders=sort_orders, page_token=page_token)

List Resource Groups by filter

This fetches a filtered list of Resource Groups

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
api_instance = harness_python_sdk.HarnessResourceGroupApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.ResourceGroupFilter() # ResourceGroupFilter | Filter Resource Groups based on multiple parameters
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
page_index = 0 # int | Page Index of the results to fetch.Default Value: 0 (optional) (default to 0)
page_size = 50 # int | Results per page(max 100)Default Value: 50 (optional) (default to 50)
sort_orders = [harness_python_sdk.SortOrder()] # list[SortOrder] | Sort criteria for the elements. (optional)
page_token = 'page_token_example' # str | Page Token of the next results to fetch.Default Value: '' (optional)

try:
    # List Resource Groups by filter
    api_response = api_instance.get_filter_resource_group_list_v2(body, account_identifier, page_index=page_index, page_size=page_size, sort_orders=sort_orders, page_token=page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HarnessResourceGroupApi->get_filter_resource_group_list_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ResourceGroupFilter**](ResourceGroupFilter.md)| Filter Resource Groups based on multiple parameters | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **page_index** | **int**| Page Index of the results to fetch.Default Value: 0 | [optional] [default to 0]
 **page_size** | **int**| Results per page(max 100)Default Value: 50 | [optional] [default to 50]
 **sort_orders** | [**list[SortOrder]**](SortOrder.md)| Sort criteria for the elements. | [optional] 
 **page_token** | **str**| Page Token of the next results to fetch.Default Value: &#x27;&#x27; | [optional] 

### Return type

[**ResponseDTOPageResponseResourceGroupV2Response**](ResponseDTOPageResponseResourceGroupV2Response.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_group_list_v2**
> ResponseDTOPageResponseResourceGroupV2Response get_resource_group_list_v2(account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, search_term=search_term, page_index=page_index, page_size=page_size, sort_orders=sort_orders, page_token=page_token)

List Resource Groups

Get list of resource groups

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
api_instance = harness_python_sdk.HarnessResourceGroupApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
search_term = 'search_term_example' # str | Details of all the resource groups having this string in their name or identifier will be returned. (optional)
page_index = 0 # int | Page Index of the results to fetch.Default Value: 0 (optional) (default to 0)
page_size = 50 # int | Results per page(max 100)Default Value: 50 (optional) (default to 50)
sort_orders = [harness_python_sdk.SortOrder()] # list[SortOrder] | Sort criteria for the elements. (optional)
page_token = 'page_token_example' # str | Page Token of the next results to fetch.Default Value: '' (optional)

try:
    # List Resource Groups
    api_response = api_instance.get_resource_group_list_v2(account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, search_term=search_term, page_index=page_index, page_size=page_size, sort_orders=sort_orders, page_token=page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HarnessResourceGroupApi->get_resource_group_list_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **search_term** | **str**| Details of all the resource groups having this string in their name or identifier will be returned. | [optional] 
 **page_index** | **int**| Page Index of the results to fetch.Default Value: 0 | [optional] [default to 0]
 **page_size** | **int**| Results per page(max 100)Default Value: 50 | [optional] [default to 50]
 **sort_orders** | [**list[SortOrder]**](SortOrder.md)| Sort criteria for the elements. | [optional] 
 **page_token** | **str**| Page Token of the next results to fetch.Default Value: &#x27;&#x27; | [optional] 

### Return type

[**ResponseDTOPageResponseResourceGroupV2Response**](ResponseDTOPageResponseResourceGroupV2Response.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_group_v2**
> ResponseDTOResourceGroupV2Response get_resource_group_v2(identifier, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Get Resource Group

Get a resource group by identifier

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
api_instance = harness_python_sdk.HarnessResourceGroupApi(harness_python_sdk.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier for the Entity.
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Get Resource Group
    api_response = api_instance.get_resource_group_v2(identifier, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HarnessResourceGroupApi->get_resource_group_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier for the Entity. | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOResourceGroupV2Response**](ResponseDTOResourceGroupV2Response.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_resource_group_v2**
> ResponseDTOResourceGroupV2Response update_resource_group_v2(body, account_identifier, identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Update Resource Group

Update a resource group

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
api_instance = harness_python_sdk.HarnessResourceGroupApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.ResourceGroupV2Request() # ResourceGroupV2Request | This contains the details required to create a Resource Group
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
identifier = 'identifier_example' # str | Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Update Resource Group
    api_response = api_instance.update_resource_group_v2(body, account_identifier, identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HarnessResourceGroupApi->update_resource_group_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ResourceGroupV2Request**](ResourceGroupV2Request.md)| This contains the details required to create a Resource Group | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **identifier** | **str**| Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOResourceGroupV2Response**](ResponseDTOResourceGroupV2Response.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

