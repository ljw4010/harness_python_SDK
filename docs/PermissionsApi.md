# swagger_client.PermissionsApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_permission_list**](PermissionsApi.md#get_permission_list) | **GET** /authz/api/permissions | List Permissions
[**get_permission_resource_types_list**](PermissionsApi.md#get_permission_resource_types_list) | **GET** /authz/api/permissions/resourcetypes | List Resource Types

# **get_permission_list**
> ResponseDTOListPermissionResponse get_permission_list(account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, scope_filter_disabled=scope_filter_disabled)

List Permissions

Get all permissions in a scope or all permissions in the system

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
api_instance = swagger_client.PermissionsApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
scope_filter_disabled = true # bool | This is to enable or disable filtering by scope. The default value is false. If the value is true, all the permissions in the system are fetched. (optional)

try:
    # List Permissions
    api_response = api_instance.get_permission_list(account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, scope_filter_disabled=scope_filter_disabled)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionsApi->get_permission_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **scope_filter_disabled** | **bool**| This is to enable or disable filtering by scope. The default value is false. If the value is true, all the permissions in the system are fetched. | [optional] 

### Return type

[**ResponseDTOListPermissionResponse**](ResponseDTOListPermissionResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_permission_resource_types_list**
> ResponseDTOSetString get_permission_resource_types_list(account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, scope_filter_disabled=scope_filter_disabled)

List Resource Types

Get all resource types for permissions in a scope or in the system.

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
api_instance = swagger_client.PermissionsApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
scope_filter_disabled = true # bool | This is to enable or disable filtering by scope. The default value is false. If the value is true, all the permissions in the system are fetched. (optional)

try:
    # List Resource Types
    api_response = api_instance.get_permission_resource_types_list(account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, scope_filter_disabled=scope_filter_disabled)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionsApi->get_permission_resource_types_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **scope_filter_disabled** | **bool**| This is to enable or disable filtering by scope. The default value is false. If the value is true, all the permissions in the system are fetched. | [optional] 

### Return type

[**ResponseDTOSetString**](ResponseDTOSetString.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

