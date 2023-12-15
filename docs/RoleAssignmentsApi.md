# harness_python_sdk.RoleAssignmentsApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_delete_role_assignment**](RoleAssignmentsApi.md#bulk_delete_role_assignment) | **POST** /authz/api/roleassignments/delete/batch | Bulk Delete Role Assignment
[**delete_role_assignment**](RoleAssignmentsApi.md#delete_role_assignment) | **DELETE** /authz/api/roleassignments/{identifier} | Delete Role Assignment
[**get_filtered_role_assignment_by_scope_list**](RoleAssignmentsApi.md#get_filtered_role_assignment_by_scope_list) | **POST** /authz/api/roleassignments/v2/filter | List Role Assignments by scope filter
[**get_filtered_role_assignment_list**](RoleAssignmentsApi.md#get_filtered_role_assignment_list) | **POST** /authz/api/roleassignments/filter | List Role Assignments by filter
[**get_role_assignment**](RoleAssignmentsApi.md#get_role_assignment) | **GET** /authz/api/roleassignments/{identifier} | Get Role Assignment
[**get_role_assignment_aggregate_list**](RoleAssignmentsApi.md#get_role_assignment_aggregate_list) | **POST** /authz/api/roleassignments/aggregate | List Aggregated Role Assignments by filter
[**get_role_assignment_list**](RoleAssignmentsApi.md#get_role_assignment_list) | **GET** /authz/api/roleassignments | List Role Assignments
[**post_role_assignment**](RoleAssignmentsApi.md#post_role_assignment) | **POST** /authz/api/roleassignments | Create Role Assignment
[**post_role_assignments**](RoleAssignmentsApi.md#post_role_assignments) | **POST** /authz/api/roleassignments/multi | Create Role Assignments
[**validate_role_assignment**](RoleAssignmentsApi.md#validate_role_assignment) | **POST** /authz/api/roleassignments/validate | Validate Role Assignment

# **bulk_delete_role_assignment**
> ResponseDTORoleAssignmentDeleteResponseDTO bulk_delete_role_assignment(body, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Bulk Delete Role Assignment

Bulk delete role assignments by identifiers

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
api_instance = harness_python_sdk.RoleAssignmentsApi(harness_python_sdk.ApiClient(configuration))
body = ['body_example'] # list[str] | List of role assigment identifiers to be deleted
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Bulk Delete Role Assignment
    api_response = api_instance.bulk_delete_role_assignment(body, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleAssignmentsApi->bulk_delete_role_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)| List of role assigment identifiers to be deleted | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTORoleAssignmentDeleteResponseDTO**](ResponseDTORoleAssignmentDeleteResponseDTO.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_role_assignment**
> ResponseDTORoleAssignmentResponse delete_role_assignment(account_identifier, identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Delete Role Assignment

Delete an existing role assignment by identifier

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
api_instance = harness_python_sdk.RoleAssignmentsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
identifier = 'identifier_example' # str | Identifier for role assignment
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Delete Role Assignment
    api_response = api_instance.delete_role_assignment(account_identifier, identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleAssignmentsApi->delete_role_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **identifier** | **str**| Identifier for role assignment | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTORoleAssignmentResponse**](ResponseDTORoleAssignmentResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_filtered_role_assignment_by_scope_list**
> ResponseDTOPageResponseRoleAssignmentAggregate get_filtered_role_assignment_by_scope_list(account_identifier, body=body, page_index=page_index, page_size=page_size, sort_orders=sort_orders, page_token=page_token, org_identifier=org_identifier, project_identifier=project_identifier)

List Role Assignments by scope filter

List role assignments in the scope according to the given filter

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
api_instance = harness_python_sdk.RoleAssignmentsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
body = harness_python_sdk.RoleAssignmentFilterV2() # RoleAssignmentFilterV2 |  (optional)
page_index = 0 # int | Page Index of the results to fetch.Default Value: 0 (optional) (default to 0)
page_size = 50 # int | Results per page(max 100)Default Value: 50 (optional) (default to 50)
sort_orders = [harness_python_sdk.SortOrder()] # list[SortOrder] | Sort criteria for the elements. (optional)
page_token = 'page_token_example' # str | Page Token of the next results to fetch.Default Value: '' (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # List Role Assignments by scope filter
    api_response = api_instance.get_filtered_role_assignment_by_scope_list(account_identifier, body=body, page_index=page_index, page_size=page_size, sort_orders=sort_orders, page_token=page_token, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleAssignmentsApi->get_filtered_role_assignment_by_scope_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **body** | [**RoleAssignmentFilterV2**](RoleAssignmentFilterV2.md)|  | [optional] 
 **page_index** | **int**| Page Index of the results to fetch.Default Value: 0 | [optional] [default to 0]
 **page_size** | **int**| Results per page(max 100)Default Value: 50 | [optional] [default to 50]
 **sort_orders** | [**list[SortOrder]**](SortOrder.md)| Sort criteria for the elements. | [optional] 
 **page_token** | **str**| Page Token of the next results to fetch.Default Value: &#x27;&#x27; | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOPageResponseRoleAssignmentAggregate**](ResponseDTOPageResponseRoleAssignmentAggregate.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_filtered_role_assignment_list**
> ResponseDTOPageResponseRoleAssignmentResponse get_filtered_role_assignment_list(body, account_identifier, page_index=page_index, page_size=page_size, sort_orders=sort_orders, page_token=page_token, org_identifier=org_identifier, project_identifier=project_identifier)

List Role Assignments by filter

List role assignments in the scope according to the given filter

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
api_instance = harness_python_sdk.RoleAssignmentsApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.RoleAssignmentFilter() # RoleAssignmentFilter | Filter role assignments based on multiple parameters.
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
page_index = 0 # int | Page Index of the results to fetch.Default Value: 0 (optional) (default to 0)
page_size = 50 # int | Results per page(max 100)Default Value: 50 (optional) (default to 50)
sort_orders = [harness_python_sdk.SortOrder()] # list[SortOrder] | Sort criteria for the elements. (optional)
page_token = 'page_token_example' # str | Page Token of the next results to fetch.Default Value: '' (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # List Role Assignments by filter
    api_response = api_instance.get_filtered_role_assignment_list(body, account_identifier, page_index=page_index, page_size=page_size, sort_orders=sort_orders, page_token=page_token, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleAssignmentsApi->get_filtered_role_assignment_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RoleAssignmentFilter**](RoleAssignmentFilter.md)| Filter role assignments based on multiple parameters. | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **page_index** | **int**| Page Index of the results to fetch.Default Value: 0 | [optional] [default to 0]
 **page_size** | **int**| Results per page(max 100)Default Value: 50 | [optional] [default to 50]
 **sort_orders** | [**list[SortOrder]**](SortOrder.md)| Sort criteria for the elements. | [optional] 
 **page_token** | **str**| Page Token of the next results to fetch.Default Value: &#x27;&#x27; | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOPageResponseRoleAssignmentResponse**](ResponseDTOPageResponseRoleAssignmentResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_assignment**
> ResponseDTORoleAssignmentResponse get_role_assignment(account_identifier, identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Get Role Assignment

Get an existing role assignment by identifier

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
api_instance = harness_python_sdk.RoleAssignmentsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
identifier = 'identifier_example' # str | Identifier for role assignment
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Get Role Assignment
    api_response = api_instance.get_role_assignment(account_identifier, identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleAssignmentsApi->get_role_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **identifier** | **str**| Identifier for role assignment | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTORoleAssignmentResponse**](ResponseDTORoleAssignmentResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_assignment_aggregate_list**
> ResponseDTORoleAssignmentAggregateResponse get_role_assignment_aggregate_list(body, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)

List Aggregated Role Assignments by filter

List role assignments in the scope according to the given filter with added metadata

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
api_instance = harness_python_sdk.RoleAssignmentsApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.RoleAssignmentFilter() # RoleAssignmentFilter | Filter role assignments based on multiple parameters.
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # List Aggregated Role Assignments by filter
    api_response = api_instance.get_role_assignment_aggregate_list(body, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleAssignmentsApi->get_role_assignment_aggregate_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RoleAssignmentFilter**](RoleAssignmentFilter.md)| Filter role assignments based on multiple parameters. | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTORoleAssignmentAggregateResponse**](ResponseDTORoleAssignmentAggregateResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_assignment_list**
> ResponseDTOPageResponseRoleAssignmentResponse get_role_assignment_list(account_identifier, page_index=page_index, page_size=page_size, sort_orders=sort_orders, page_token=page_token, org_identifier=org_identifier, project_identifier=project_identifier)

List Role Assignments

List role assignments in the given scope

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
api_instance = harness_python_sdk.RoleAssignmentsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
page_index = 0 # int | Page Index of the results to fetch.Default Value: 0 (optional) (default to 0)
page_size = 50 # int | Results per page(max 100)Default Value: 50 (optional) (default to 50)
sort_orders = [harness_python_sdk.SortOrder()] # list[SortOrder] | Sort criteria for the elements. (optional)
page_token = 'page_token_example' # str | Page Token of the next results to fetch.Default Value: '' (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # List Role Assignments
    api_response = api_instance.get_role_assignment_list(account_identifier, page_index=page_index, page_size=page_size, sort_orders=sort_orders, page_token=page_token, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleAssignmentsApi->get_role_assignment_list: %s\n" % e)
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

### Return type

[**ResponseDTOPageResponseRoleAssignmentResponse**](ResponseDTOPageResponseRoleAssignmentResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_role_assignment**
> ResponseDTORoleAssignmentResponse post_role_assignment(body, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Create Role Assignment

Creates role assignment within the specified scope.

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
api_instance = harness_python_sdk.RoleAssignmentsApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.AuthzRoleAssignment() # AuthzRoleAssignment | These are details for the role assignment to create.
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Create Role Assignment
    api_response = api_instance.post_role_assignment(body, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleAssignmentsApi->post_role_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthzRoleAssignment**](AuthzRoleAssignment.md)| These are details for the role assignment to create. | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTORoleAssignmentResponse**](ResponseDTORoleAssignmentResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_role_assignments**
> ResponseDTOListRoleAssignmentResponse post_role_assignments(body, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Create Role Assignments

Create multiple role assignments in a scope. Returns all successfully created role assignments. Ignores failures and duplicates.

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
api_instance = harness_python_sdk.RoleAssignmentsApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.RoleAssignmentCreateRequest() # RoleAssignmentCreateRequest | List of role assignments to create
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Create Role Assignments
    api_response = api_instance.post_role_assignments(body, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleAssignmentsApi->post_role_assignments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RoleAssignmentCreateRequest**](RoleAssignmentCreateRequest.md)| List of role assignments to create | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOListRoleAssignmentResponse**](ResponseDTOListRoleAssignmentResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_role_assignment**
> ResponseDTORoleAssignmentValidationResponse validate_role_assignment(body, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Validate Role Assignment

Check whether a proposed role assignment is valid.

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
api_instance = harness_python_sdk.RoleAssignmentsApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.RoleAssignmentValidationRequest() # RoleAssignmentValidationRequest | This is the details of the role assignment for validation.
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Validate Role Assignment
    api_response = api_instance.validate_role_assignment(body, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleAssignmentsApi->validate_role_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RoleAssignmentValidationRequest**](RoleAssignmentValidationRequest.md)| This is the details of the role assignment for validation. | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTORoleAssignmentValidationResponse**](ResponseDTORoleAssignmentValidationResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

