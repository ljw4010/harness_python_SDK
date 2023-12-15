# swagger_client.AccountRancherInfrastructureApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_account_scoped_rancher_clusters_using_connector**](AccountRancherInfrastructureApi.md#list_account_scoped_rancher_clusters_using_connector) | **GET** /v1/rancher/connectors/{connector}/clusters | List rancher clusters using account level connector
[**list_account_scoped_rancher_clusters_using_env_and_infra**](AccountRancherInfrastructureApi.md#list_account_scoped_rancher_clusters_using_env_and_infra) | **GET** /v1/rancher/environments/{environment}/infrastructure-definitions/{infrastructure-definition}/clusters | List rancher clusters using account level env and infra def

# **list_account_scoped_rancher_clusters_using_connector**
> list[str] list_account_scoped_rancher_clusters_using_connector(connector, harness_account=harness_account, page=page, limit=limit, sort=sort, order=order)

List rancher clusters using account level connector

List rancher clusters using the given account level rancher connector

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
api_instance = swagger_client.AccountRancherInfrastructureApi(swagger_client.ApiClient(configuration))
connector = 'connector_example' # str | Identifier field of the scoped connector entity to be used for this operation.
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)
page = 0 # int | Pagination page number strategy: Specify the page number within the paginated collection related to the number of items in each page  (optional) (default to 0)
limit = 30 # int | Number of items to return per page. (optional) (default to 30)
sort = 'sort_example' # str | Parameter on the basis of which sorting is done. (optional)
order = 'order_example' # str | Order on the basis of which sorting is done. (optional)

try:
    # List rancher clusters using account level connector
    api_response = api_instance.list_account_scoped_rancher_clusters_using_connector(connector, harness_account=harness_account, page=page, limit=limit, sort=sort, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountRancherInfrastructureApi->list_account_scoped_rancher_clusters_using_connector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector** | **str**| Identifier field of the scoped connector entity to be used for this operation. | 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 
 **page** | **int**| Pagination page number strategy: Specify the page number within the paginated collection related to the number of items in each page  | [optional] [default to 0]
 **limit** | **int**| Number of items to return per page. | [optional] [default to 30]
 **sort** | **str**| Parameter on the basis of which sorting is done. | [optional] 
 **order** | **str**| Order on the basis of which sorting is done. | [optional] 

### Return type

**list[str]**

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_account_scoped_rancher_clusters_using_env_and_infra**
> list[str] list_account_scoped_rancher_clusters_using_env_and_infra(environment, infrastructure_definition, harness_account=harness_account, page=page, limit=limit, sort=sort, order=order)

List rancher clusters using account level env and infra def

List rancher clusters using the given account level environment and infrastructure definition.

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
api_instance = swagger_client.AccountRancherInfrastructureApi(swagger_client.ApiClient(configuration))
environment = 'environment_example' # str | Identifier field of the scoped environment entity to be used for the selected operation.
infrastructure_definition = 'infrastructure_definition_example' # str | Identifier field of the scoped infrastructure definition entity to be used in the selected operation.
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)
page = 0 # int | Pagination page number strategy: Specify the page number within the paginated collection related to the number of items in each page  (optional) (default to 0)
limit = 30 # int | Number of items to return per page. (optional) (default to 30)
sort = 'sort_example' # str | Parameter on the basis of which sorting is done. (optional)
order = 'order_example' # str | Order on the basis of which sorting is done. (optional)

try:
    # List rancher clusters using account level env and infra def
    api_response = api_instance.list_account_scoped_rancher_clusters_using_env_and_infra(environment, infrastructure_definition, harness_account=harness_account, page=page, limit=limit, sort=sort, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountRancherInfrastructureApi->list_account_scoped_rancher_clusters_using_env_and_infra: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **str**| Identifier field of the scoped environment entity to be used for the selected operation. | 
 **infrastructure_definition** | **str**| Identifier field of the scoped infrastructure definition entity to be used in the selected operation. | 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 
 **page** | **int**| Pagination page number strategy: Specify the page number within the paginated collection related to the number of items in each page  | [optional] [default to 0]
 **limit** | **int**| Number of items to return per page. | [optional] [default to 30]
 **sort** | **str**| Parameter on the basis of which sorting is done. | [optional] 
 **order** | **str**| Order on the basis of which sorting is done. | [optional] 

### Return type

**list[str]**

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

