# swagger_client.ProjectServicesApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_service**](ProjectServicesApi.md#create_service) | **POST** /v1/orgs/{org}/projects/{project}/services | Create a Service
[**delete_service**](ProjectServicesApi.md#delete_service) | **DELETE** /v1/orgs/{org}/projects/{project}/services/{service} | Delete a Service
[**get_service**](ProjectServicesApi.md#get_service) | **GET** /v1/orgs/{org}/projects/{project}/services/{service} | Retrieve a service
[**get_services**](ProjectServicesApi.md#get_services) | **GET** /v1/orgs/{org}/projects/{project}/services | List Services
[**update_service**](ProjectServicesApi.md#update_service) | **PUT** /v1/orgs/{org}/projects/{project}/services/{service} | Update Service

# **create_service**
> ServiceResponse create_service(body, org, project, harness_account=harness_account)

Create a Service

Creates a service

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
api_instance = swagger_client.ProjectServicesApi(swagger_client.ApiClient(configuration))
body = swagger_client.ServiceRequest() # ServiceRequest | Create Service request body
org = 'org_example' # str | Identifier field of the organization the resource is scoped to
project = 'project_example' # str | Identifier field of the project the resource is scoped to
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)

try:
    # Create a Service
    api_response = api_instance.create_service(body, org, project, harness_account=harness_account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServicesApi->create_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ServiceRequest**](ServiceRequest.md)| Create Service request body | 
 **org** | **str**| Identifier field of the organization the resource is scoped to | 
 **project** | **str**| Identifier field of the project the resource is scoped to | 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 

### Return type

[**ServiceResponse**](ServiceResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_service**
> ServiceResponse delete_service(org, project, service, harness_account=harness_account, force_delete=force_delete)

Delete a Service

Deletes the requested service.

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
api_instance = swagger_client.ProjectServicesApi(swagger_client.ApiClient(configuration))
org = 'org_example' # str | Identifier field of the organization the resource is scoped to
project = 'project_example' # str | Identifier field of the project the resource is scoped to
service = 'service_example' # str | Identifier field of the service the resource is scoped to
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)
force_delete = false # bool | Enable this field to force delete a template (optional) (default to false)

try:
    # Delete a Service
    api_response = api_instance.delete_service(org, project, service, harness_account=harness_account, force_delete=force_delete)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServicesApi->delete_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| Identifier field of the organization the resource is scoped to | 
 **project** | **str**| Identifier field of the project the resource is scoped to | 
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

# **get_service**
> ServiceResponse get_service(org, project, service, harness_account=harness_account)

Retrieve a service

Retrieves the specified service

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
api_instance = swagger_client.ProjectServicesApi(swagger_client.ApiClient(configuration))
org = 'org_example' # str | Identifier field of the organization the resource is scoped to
project = 'project_example' # str | Identifier field of the project the resource is scoped to
service = 'service_example' # str | Identifier field of the service the resource is scoped to
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)

try:
    # Retrieve a service
    api_response = api_instance.get_service(org, project, service, harness_account=harness_account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServicesApi->get_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| Identifier field of the organization the resource is scoped to | 
 **project** | **str**| Identifier field of the project the resource is scoped to | 
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

# **get_services**
> list[ServiceResponse] get_services(org, project, page=page, limit=limit, search_term=search_term, service_ids=service_ids, sort=sort, is_access_list=is_access_list, type=type, git_ops_enabled=git_ops_enabled, harness_account=harness_account, order=order)

List Services

Returns a list of the services for which you have view permissions in the given project.

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
api_instance = swagger_client.ProjectServicesApi(swagger_client.ApiClient(configuration))
org = 'org_example' # str | Identifier field of the organization the resource is scoped to
project = 'project_example' # str | Identifier field of the project the resource is scoped to
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
    # List Services
    api_response = api_instance.get_services(org, project, page=page, limit=limit, search_term=search_term, service_ids=service_ids, sort=sort, is_access_list=is_access_list, type=type, git_ops_enabled=git_ops_enabled, harness_account=harness_account, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServicesApi->get_services: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| Identifier field of the organization the resource is scoped to | 
 **project** | **str**| Identifier field of the project the resource is scoped to | 
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

# **update_service**
> ServiceResponse update_service(body, org, project, service, harness_account=harness_account)

Update Service

Updates the specified service

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
api_instance = swagger_client.ProjectServicesApi(swagger_client.ApiClient(configuration))
body = swagger_client.ServiceRequest() # ServiceRequest | Create Service request body
org = 'org_example' # str | Identifier field of the organization the resource is scoped to
project = 'project_example' # str | Identifier field of the project the resource is scoped to
service = 'service_example' # str | Identifier field of the service the resource is scoped to
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)

try:
    # Update Service
    api_response = api_instance.update_service(body, org, project, service, harness_account=harness_account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServicesApi->update_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ServiceRequest**](ServiceRequest.md)| Create Service request body | 
 **org** | **str**| Identifier field of the organization the resource is scoped to | 
 **project** | **str**| Identifier field of the project the resource is scoped to | 
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

