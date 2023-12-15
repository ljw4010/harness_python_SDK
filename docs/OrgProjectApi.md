# harness_python_sdk.OrgProjectApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_org_scoped_project**](OrgProjectApi.md#create_org_scoped_project) | **POST** /v1/orgs/{org}/projects | Create a project
[**delete_org_scoped_project**](OrgProjectApi.md#delete_org_scoped_project) | **DELETE** /v1/orgs/{org}/projects/{project} | Delete a project
[**get_org_scoped_project**](OrgProjectApi.md#get_org_scoped_project) | **GET** /v1/orgs/{org}/projects/{project} | Retrieve a project
[**get_org_scoped_projects**](OrgProjectApi.md#get_org_scoped_projects) | **GET** /v1/orgs/{org}/projects | List projects
[**update_org_scoped_project**](OrgProjectApi.md#update_org_scoped_project) | **PUT** /v1/orgs/{org}/projects/{project} | Update a project

# **create_org_scoped_project**
> ProjectResponse create_org_scoped_project(body, org, harness_account=harness_account)

Create a project

Creates a new project

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
api_instance = harness_python_sdk.OrgProjectApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.CreateProjectRequest() # CreateProjectRequest | Post the necessary fields for the API to create a project.
org = 'org_example' # str | Identifier field of the organization the resource is scoped to
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)

try:
    # Create a project
    api_response = api_instance.create_org_scoped_project(body, org, harness_account=harness_account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgProjectApi->create_org_scoped_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateProjectRequest**](CreateProjectRequest.md)| Post the necessary fields for the API to create a project. | 
 **org** | **str**| Identifier field of the organization the resource is scoped to | 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 

### Return type

[**ProjectResponse**](ProjectResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_org_scoped_project**
> ProjectResponse delete_org_scoped_project(org, project, harness_account=harness_account)

Delete a project

Deletes the information of the project with the matching project identifier.

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
api_instance = harness_python_sdk.OrgProjectApi(harness_python_sdk.ApiClient(configuration))
org = 'org_example' # str | Identifier field of the organization the resource is scoped to
project = 'project_example' # str | Identifier field of the project the resource is scoped to
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)

try:
    # Delete a project
    api_response = api_instance.delete_org_scoped_project(org, project, harness_account=harness_account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgProjectApi->delete_org_scoped_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| Identifier field of the organization the resource is scoped to | 
 **project** | **str**| Identifier field of the project the resource is scoped to | 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 

### Return type

[**ProjectResponse**](ProjectResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_org_scoped_project**
> ProjectResponse get_org_scoped_project(org, project, harness_account=harness_account)

Retrieve a project

Retrieves the information of the project with the matching project identifier.

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
api_instance = harness_python_sdk.OrgProjectApi(harness_python_sdk.ApiClient(configuration))
org = 'org_example' # str | Identifier field of the organization the resource is scoped to
project = 'project_example' # str | Identifier field of the project the resource is scoped to
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)

try:
    # Retrieve a project
    api_response = api_instance.get_org_scoped_project(org, project, harness_account=harness_account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgProjectApi->get_org_scoped_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| Identifier field of the organization the resource is scoped to | 
 **project** | **str**| Identifier field of the project the resource is scoped to | 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 

### Return type

[**ProjectResponse**](ProjectResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_org_scoped_projects**
> list[ProjectResponse] get_org_scoped_projects(org, project=project, has_module=has_module, module_type=module_type, only_favorites=only_favorites, search_term=search_term, page=page, limit=limit, harness_account=harness_account, sort=sort, order=order)

List projects

Retrieves the information of the projects.

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
api_instance = harness_python_sdk.OrgProjectApi(harness_python_sdk.ApiClient(configuration))
org = 'org_example' # str | Identifier field of the organization the resource is scoped to
project = ['project_example'] # list[str] | Identifier field of the projects the resource is scoped to (optional)
has_module = true # bool | This boolean specifies whether to filter projects which has the module of type passed in the moduleType parameter or not (optional) (default to true)
module_type = 'module_type_example' # str | Project's module type (optional)
only_favorites = true # bool | Enable this field to fetch only the entities that are marked as favorites. (optional)
search_term = 'search_term_example' # str | This would be used to filter resources having attributes matching with search term. (optional)
page = 0 # int | Pagination page number strategy: Specify the page number within the paginated collection related to the number of items in each page  (optional) (default to 0)
limit = 30 # int | Number of items to return per page. (optional) (default to 30)
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)
sort = 'sort_example' # str | Parameter on the basis of which sorting is done. (optional)
order = 'order_example' # str | Order on the basis of which sorting is done. (optional)

try:
    # List projects
    api_response = api_instance.get_org_scoped_projects(org, project=project, has_module=has_module, module_type=module_type, only_favorites=only_favorites, search_term=search_term, page=page, limit=limit, harness_account=harness_account, sort=sort, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgProjectApi->get_org_scoped_projects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| Identifier field of the organization the resource is scoped to | 
 **project** | [**list[str]**](str.md)| Identifier field of the projects the resource is scoped to | [optional] 
 **has_module** | **bool**| This boolean specifies whether to filter projects which has the module of type passed in the moduleType parameter or not | [optional] [default to true]
 **module_type** | **str**| Project&#x27;s module type | [optional] 
 **only_favorites** | **bool**| Enable this field to fetch only the entities that are marked as favorites. | [optional] 
 **search_term** | **str**| This would be used to filter resources having attributes matching with search term. | [optional] 
 **page** | **int**| Pagination page number strategy: Specify the page number within the paginated collection related to the number of items in each page  | [optional] [default to 0]
 **limit** | **int**| Number of items to return per page. | [optional] [default to 30]
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 
 **sort** | **str**| Parameter on the basis of which sorting is done. | [optional] 
 **order** | **str**| Order on the basis of which sorting is done. | [optional] 

### Return type

[**list[ProjectResponse]**](ProjectResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_org_scoped_project**
> ProjectResponse update_org_scoped_project(body, org, project, harness_account=harness_account)

Update a project

Updates the information of the project with the matching project identifier.

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
api_instance = harness_python_sdk.OrgProjectApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.UpdateProjectRequest() # UpdateProjectRequest | Put the necessary fields for the API to update a Project.
org = 'org_example' # str | Identifier field of the organization the resource is scoped to
project = 'project_example' # str | Identifier field of the project the resource is scoped to
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)

try:
    # Update a project
    api_response = api_instance.update_org_scoped_project(body, org, project, harness_account=harness_account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgProjectApi->update_org_scoped_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateProjectRequest**](UpdateProjectRequest.md)| Put the necessary fields for the API to update a Project. | 
 **org** | **str**| Identifier field of the organization the resource is scoped to | 
 **project** | **str**| Identifier field of the project the resource is scoped to | 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 

### Return type

[**ProjectResponse**](ProjectResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

