# swagger_client.FilterResourceGroupsApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**filter_resource_groups**](FilterResourceGroupsApi.md#filter_resource_groups) | **POST** /v1/resource-groups/filter | Filter Resource Groups

# **filter_resource_groups**
> list[ResourceGroupsResponse] filter_resource_groups(body, harness_account=harness_account, page=page, limit=limit, sort=sort, order=order)

Filter Resource Groups

Returns a list of Resource Groups based on filter criteria.

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
api_instance = swagger_client.FilterResourceGroupsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ResourceGroupFilterRequestBody() # ResourceGroupFilterRequestBody | Filter Resource Group request body
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)
page = 0 # int | Pagination page number strategy: Specify the page number within the paginated collection related to the number of items on each page. (optional) (default to 0)
limit = 30 # int | Pagination: Number of items to return. (optional) (default to 30)
sort = 'sort_example' # str | Parameter on the basis of which sorting is done. (optional)
order = 'order_example' # str | Order on the basis of which sorting is done. (optional)

try:
    # Filter Resource Groups
    api_response = api_instance.filter_resource_groups(body, harness_account=harness_account, page=page, limit=limit, sort=sort, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilterResourceGroupsApi->filter_resource_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ResourceGroupFilterRequestBody**](ResourceGroupFilterRequestBody.md)| Filter Resource Group request body | 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 
 **page** | **int**| Pagination page number strategy: Specify the page number within the paginated collection related to the number of items on each page. | [optional] [default to 0]
 **limit** | **int**| Pagination: Number of items to return. | [optional] [default to 30]
 **sort** | **str**| Parameter on the basis of which sorting is done. | [optional] 
 **order** | **str**| Order on the basis of which sorting is done. | [optional] 

### Return type

[**list[ResourceGroupsResponse]**](ResourceGroupsResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

