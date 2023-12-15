# harness_python_sdk.AccountServicesApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_account_scoped_service**](AccountServicesApi.md#create_account_scoped_service) | **POST** /v1/services | Create a service
[**delete_account_scoped_service**](AccountServicesApi.md#delete_account_scoped_service) | **DELETE** /v1/services/{service} | Delete a service
[**get_account_scoped_service**](AccountServicesApi.md#get_account_scoped_service) | **GET** /v1/services/{service} | Retrieve a service
[**get_account_scoped_services**](AccountServicesApi.md#get_account_scoped_services) | **GET** /v1/services | List services
[**update_account_scoped_service**](AccountServicesApi.md#update_account_scoped_service) | **PUT** /v1/services/{service} | Update service

# **create_account_scoped_service**
> ServiceResponse create_account_scoped_service(body, harness_account=harness_account)

Create a service

Creates a service

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
api_instance = harness_python_sdk.AccountServicesApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.ServiceRequest() # ServiceRequest | Create Service request body
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)

try:
    # Create a service
    api_response = api_instance.create_account_scoped_service(body, harness_account=harness_account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountServicesApi->create_account_scoped_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ServiceRequest**](ServiceRequest.md)| Create Service request body | 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 

### Return type

[**ServiceResponse**](ServiceResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_account_scoped_service**
> ServiceResponse delete_account_scoped_service(service, harness_account=harness_account, force_delete=force_delete)

Delete a service

Deletes the requested service

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
api_instance = harness_python_sdk.AccountServicesApi(harness_python_sdk.ApiClient(configuration))
service = 'service_example' # str | Identifier field of the service the resource is scoped to
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)
force_delete = false # bool | Enable this field to force delete a template (optional) (default to false)

try:
    # Delete a service
    api_response = api_instance.delete_account_scoped_service(service, harness_account=harness_account, force_delete=force_delete)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountServicesApi->delete_account_scoped_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | **str**| Identifier field of the service the resource is scoped to | 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 
 **force_delete** | **bool**| Enable this field to force delete a template | [optional] [default to false]

### Return type

[**ServiceResponse**](ServiceResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_scoped_service**
> ServiceResponse get_account_scoped_service(service, harness_account=harness_account)

Retrieve a service

Retrieves the specified service

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
api_instance = harness_python_sdk.AccountServicesApi(harness_python_sdk.ApiClient(configuration))
service = 'service_example' # str | Identifier field of the service the resource is scoped to
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)

try:
    # Retrieve a service
    api_response = api_instance.get_account_scoped_service(service, harness_account=harness_account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountServicesApi->get_account_scoped_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | **str**| Identifier field of the service the resource is scoped to | 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 

### Return type

[**ServiceResponse**](ServiceResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_scoped_services**
> list[ServiceResponse] get_account_scoped_services(page=page, limit=limit, search_term=search_term, service_ids=service_ids, sort=sort, is_access_list=is_access_list, type=type, git_ops_enabled=git_ops_enabled, harness_account=harness_account, order=order)

List services

Returns a list of the services for which you have view permissions in the given project.

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
api_instance = harness_python_sdk.AccountServicesApi(harness_python_sdk.ApiClient(configuration))
page = 0 # int | Pagination page number strategy: Specify the page number within the paginated collection related to the number of items in each page  (optional) (default to 0)
limit = 30 # int | Number of items to return per page. (optional) (default to 30)
search_term = 'search_term_example' # str | This would be used to filter resources having attributes matching with search term. (optional)
service_ids = ['service_ids_example'] # list[str] | List of Service Identifiers (optional)
sort = 'sort_example' # str | Parameter on the basis of which sorting is done. (optional)
is_access_list = true # bool | Specifies whether the list is an access list. An access list is a list of services that you are permitted to use in a pipeline. (optional)
type = 'type_example' # str | Service Definition type (optional)
git_ops_enabled = true # bool | Enables you to use the service in Harness GitOps PR pipelines. (optional)
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)
order = 'order_example' # str | Order on the basis of which sorting is done. (optional)

try:
    # List services
    api_response = api_instance.get_account_scoped_services(page=page, limit=limit, search_term=search_term, service_ids=service_ids, sort=sort, is_access_list=is_access_list, type=type, git_ops_enabled=git_ops_enabled, harness_account=harness_account, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountServicesApi->get_account_scoped_services: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Pagination page number strategy: Specify the page number within the paginated collection related to the number of items in each page  | [optional] [default to 0]
 **limit** | **int**| Number of items to return per page. | [optional] [default to 30]
 **search_term** | **str**| This would be used to filter resources having attributes matching with search term. | [optional] 
 **service_ids** | [**list[str]**](str.md)| List of Service Identifiers | [optional] 
 **sort** | **str**| Parameter on the basis of which sorting is done. | [optional] 
 **is_access_list** | **bool**| Specifies whether the list is an access list. An access list is a list of services that you are permitted to use in a pipeline. | [optional] 
 **type** | **str**| Service Definition type | [optional] 
 **git_ops_enabled** | **bool**| Enables you to use the service in Harness GitOps PR pipelines. | [optional] 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 
 **order** | **str**| Order on the basis of which sorting is done. | [optional] 

### Return type

[**list[ServiceResponse]**](ServiceResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_account_scoped_service**
> ServiceResponse update_account_scoped_service(body, service, harness_account=harness_account)

Update service

Updates the specified service

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
api_instance = harness_python_sdk.AccountServicesApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.ServiceRequest() # ServiceRequest | Create Service request body
service = 'service_example' # str | Identifier field of the service the resource is scoped to
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)

try:
    # Update service
    api_response = api_instance.update_account_scoped_service(body, service, harness_account=harness_account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountServicesApi->update_account_scoped_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ServiceRequest**](ServiceRequest.md)| Create Service request body | 
 **service** | **str**| Identifier field of the service the resource is scoped to | 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 

### Return type

[**ServiceResponse**](ServiceResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

