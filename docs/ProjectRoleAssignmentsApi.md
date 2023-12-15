# harness_python_sdk.ProjectRoleAssignmentsApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project_scoped_role_assignments**](ProjectRoleAssignmentsApi.md#create_project_scoped_role_assignments) | **POST** /v1/orgs/{org}/projects/{project}/role-assignments | Create a role assignment
[**delete_project_scoped_role_assignment**](ProjectRoleAssignmentsApi.md#delete_project_scoped_role_assignment) | **DELETE** /v1/orgs/{org}/projects/{project}/role-assignments/{role-assignment} | Delete a role assignment
[**get_project_scoped_role_assignment**](ProjectRoleAssignmentsApi.md#get_project_scoped_role_assignment) | **GET** /v1/orgs/{org}/projects/{project}/role-assignments/{role-assignment} | Retrieve a role assignment
[**get_project_scoped_role_assignments**](ProjectRoleAssignmentsApi.md#get_project_scoped_role_assignments) | **GET** /v1/orgs/{org}/projects/{project}/role-assignments | List role assignments

# **create_project_scoped_role_assignments**
> RoleAssignmentResponse create_project_scoped_role_assignments(body, org, project, harness_account=harness_account)

Create a role assignment

Create a role assignment

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
api_instance = harness_python_sdk.ProjectRoleAssignmentsApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.RoleAssignment() # RoleAssignment | Role Request body
org = 'org_example' # str | Organization identifier
project = 'project_example' # str | Project identifier
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)

try:
    # Create a role assignment
    api_response = api_instance.create_project_scoped_role_assignments(body, org, project, harness_account=harness_account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectRoleAssignmentsApi->create_project_scoped_role_assignments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RoleAssignment**](RoleAssignment.md)| Role Request body | 
 **org** | **str**| Organization identifier | 
 **project** | **str**| Project identifier | 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 

### Return type

[**RoleAssignmentResponse**](RoleAssignmentResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project_scoped_role_assignment**
> RoleAssignmentResponse delete_project_scoped_role_assignment(role_assignment, org, project, harness_account=harness_account)

Delete a role assignment

Deletes the information of the role assignment with the matching role assignment identifier.

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
api_instance = harness_python_sdk.ProjectRoleAssignmentsApi(harness_python_sdk.ApiClient(configuration))
role_assignment = 'role_assignment_example' # str | Role assignment identifier
org = 'org_example' # str | Organization identifier
project = 'project_example' # str | Project identifier
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)

try:
    # Delete a role assignment
    api_response = api_instance.delete_project_scoped_role_assignment(role_assignment, org, project, harness_account=harness_account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectRoleAssignmentsApi->delete_project_scoped_role_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_assignment** | **str**| Role assignment identifier | 
 **org** | **str**| Organization identifier | 
 **project** | **str**| Project identifier | 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 

### Return type

[**RoleAssignmentResponse**](RoleAssignmentResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_scoped_role_assignment**
> RoleAssignmentResponse get_project_scoped_role_assignment(role_assignment, org, project, harness_account=harness_account)

Retrieve a role assignment

Retrieves the information of the role assignment with the matching role assignment identifier.

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
api_instance = harness_python_sdk.ProjectRoleAssignmentsApi(harness_python_sdk.ApiClient(configuration))
role_assignment = 'role_assignment_example' # str | Role assignment identifier
org = 'org_example' # str | Organization identifier
project = 'project_example' # str | Project identifier
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)

try:
    # Retrieve a role assignment
    api_response = api_instance.get_project_scoped_role_assignment(role_assignment, org, project, harness_account=harness_account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectRoleAssignmentsApi->get_project_scoped_role_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_assignment** | **str**| Role assignment identifier | 
 **org** | **str**| Organization identifier | 
 **project** | **str**| Project identifier | 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 

### Return type

[**RoleAssignmentResponse**](RoleAssignmentResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_scoped_role_assignments**
> list[RoleAssignmentResponse] get_project_scoped_role_assignments(org, project, harness_account=harness_account, page=page, limit=limit, sort=sort, order=order)

List role assignments

Retrieves the information of the role assignments

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
api_instance = harness_python_sdk.ProjectRoleAssignmentsApi(harness_python_sdk.ApiClient(configuration))
org = 'org_example' # str | Organization identifier
project = 'project_example' # str | Project identifier
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)
page = 0 # int | Pagination page number strategy: Specify the page number within the paginated collection related to the number of items on each page. (optional) (default to 0)
limit = 30 # int | Pagination: Number of items to return. (optional) (default to 30)
sort = 'sort_example' # str | Parameter on the basis of which sorting is done. (optional)
order = 'order_example' # str | Order on the basis of which sorting is done. (optional)

try:
    # List role assignments
    api_response = api_instance.get_project_scoped_role_assignments(org, project, harness_account=harness_account, page=page, limit=limit, sort=sort, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectRoleAssignmentsApi->get_project_scoped_role_assignments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| Organization identifier | 
 **project** | **str**| Project identifier | 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 
 **page** | **int**| Pagination page number strategy: Specify the page number within the paginated collection related to the number of items on each page. | [optional] [default to 0]
 **limit** | **int**| Pagination: Number of items to return. | [optional] [default to 30]
 **sort** | **str**| Parameter on the basis of which sorting is done. | [optional] 
 **order** | **str**| Order on the basis of which sorting is done. | [optional] 

### Return type

[**list[RoleAssignmentResponse]**](RoleAssignmentResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

