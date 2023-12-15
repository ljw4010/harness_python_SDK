# harness_python_sdk.UserGroupApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**copy_user_group**](UserGroupApi.md#copy_user_group) | **PUT** /ng/api/user-groups/copy | Copy User Group
[**delete_member**](UserGroupApi.md#delete_member) | **DELETE** /ng/api/user-groups/{identifier}/member/{userIdentifier} | Remove user from User Group
[**delete_user_group**](UserGroupApi.md#delete_user_group) | **DELETE** /ng/api/user-groups/{identifier} | Delete a User Group in an account/org/project
[**get_batch_users_group_list**](UserGroupApi.md#get_batch_users_group_list) | **POST** /ng/api/user-groups/batch | List User Groups by filter
[**get_filtered_user_groups_list**](UserGroupApi.md#get_filtered_user_groups_list) | **POST** /ng/api/user-groups/filter | Get filtered User Groups
[**get_inheriting_child_scope_list**](UserGroupApi.md#get_inheriting_child_scope_list) | **GET** /ng/api/user-groups/{identifier}/scopes | Get Inheriting Child Scopes
[**get_member**](UserGroupApi.md#get_member) | **GET** /ng/api/user-groups/{identifier}/member/{userIdentifier} | Check user membership
[**get_user_group**](UserGroupApi.md#get_user_group) | **GET** /ng/api/user-groups/{identifier} | Get User Group
[**get_user_group_list**](UserGroupApi.md#get_user_group_list) | **GET** /ng/api/user-groups | List the User Groups in an account/org/project
[**get_user_list_in_user_group**](UserGroupApi.md#get_user_list_in_user_group) | **POST** /ng/api/user-groups/{identifier}/users | List users in User Group
[**link_user_group_to_ldap**](UserGroupApi.md#link_user_group_to_ldap) | **PUT** /ng/api/user-groups/{userGroupId}/link/ldap/{ldapId} | Link LDAP Group to the User Group to an account/org/project
[**link_user_group_to_saml**](UserGroupApi.md#link_user_group_to_saml) | **PUT** /ng/api/user-groups/{userGroupId}/link/saml/{samlId} | Link SAML Group to the User Group in an account/org/project
[**post_user_group**](UserGroupApi.md#post_user_group) | **POST** /ng/api/user-groups | Create User Group
[**post_user_group_v2**](UserGroupApi.md#post_user_group_v2) | **POST** /ng/api/v2/user-groups | Create User Group
[**put_member**](UserGroupApi.md#put_member) | **PUT** /ng/api/user-groups/{identifier}/member/{userIdentifier} | Add user to User Group
[**put_user_group**](UserGroupApi.md#put_user_group) | **PUT** /ng/api/user-groups | Update User Group
[**put_user_group_v2**](UserGroupApi.md#put_user_group_v2) | **PUT** /ng/api/v2/user-groups | Update User Group
[**unlink_user_groupfrom_sso**](UserGroupApi.md#unlink_user_groupfrom_sso) | **PUT** /ng/api/user-groups/{userGroupId}/unlink | Unlink SSO Group from the User Group in an account/org/project

# **copy_user_group**
> ResponseDTOBoolean copy_user_group(body, account_identifier, group_identifier)

Copy User Group

Copy a User Group in an account/org/project

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
api_instance = harness_python_sdk.UserGroupApi(harness_python_sdk.ApiClient(configuration))
body = [harness_python_sdk.Scope1()] # list[Scope1] | List of scopes
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
group_identifier = 'group_identifier_example' # str | groupIdentifier

try:
    # Copy User Group
    api_response = api_instance.copy_user_group(body, account_identifier, group_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGroupApi->copy_user_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[Scope1]**](Scope1.md)| List of scopes | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **group_identifier** | **str**| groupIdentifier | 

### Return type

[**ResponseDTOBoolean**](ResponseDTOBoolean.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_member**
> ResponseDTOUserGroup delete_member(account_identifier, identifier, user_identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Remove user from User Group

Remove a user from the user group in an account/org/project

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
api_instance = harness_python_sdk.UserGroupApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
identifier = 'identifier_example' # str | Identifier of the user group
user_identifier = 'user_identifier_example' # str | Identifier of the user
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Remove user from User Group
    api_response = api_instance.delete_member(account_identifier, identifier, user_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGroupApi->delete_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **identifier** | **str**| Identifier of the user group | 
 **user_identifier** | **str**| Identifier of the user | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOUserGroup**](ResponseDTOUserGroup.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_group**
> ResponseDTOUserGroup delete_user_group(account_identifier, identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Delete a User Group in an account/org/project

Delete User Group

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
api_instance = harness_python_sdk.UserGroupApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
identifier = 'identifier_example' # str | Identifier of the user group
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Delete a User Group in an account/org/project
    api_response = api_instance.delete_user_group(account_identifier, identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGroupApi->delete_user_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **identifier** | **str**| Identifier of the user group | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOUserGroup**](ResponseDTOUserGroup.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_batch_users_group_list**
> ResponseDTOListUserGroup get_batch_users_group_list(body, account_identifier)

List User Groups by filter

List the User Groups selected by a filter in an account/org/project. This api supports maximum of 10K User Group in response.

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
api_instance = harness_python_sdk.UserGroupApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.UserGroupFilter() # UserGroupFilter | User Group Filter
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # List User Groups by filter
    api_response = api_instance.get_batch_users_group_list(body, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGroupApi->get_batch_users_group_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserGroupFilter**](UserGroupFilter.md)| User Group Filter | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**ResponseDTOListUserGroup**](ResponseDTOListUserGroup.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_filtered_user_groups_list**
> ResponseDTOPageResponseUserGroup get_filtered_user_groups_list(body, account_identifier, page_index=page_index, page_size=page_size, sort_orders=sort_orders, page_token=page_token)

Get filtered User Groups

List the User Groups selected by a filter in an account/org/project

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
api_instance = harness_python_sdk.UserGroupApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.UserGroupFilter() # UserGroupFilter | User Group Filter
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
page_index = 0 # int | Page Index of the results to fetch.Default Value: 0 (optional) (default to 0)
page_size = 50 # int | Results per page(max 100)Default Value: 50 (optional) (default to 50)
sort_orders = [harness_python_sdk.SortOrder()] # list[SortOrder] | Sort criteria for the elements. (optional)
page_token = 'page_token_example' # str | Page Token of the next results to fetch.Default Value: '' (optional)

try:
    # Get filtered User Groups
    api_response = api_instance.get_filtered_user_groups_list(body, account_identifier, page_index=page_index, page_size=page_size, sort_orders=sort_orders, page_token=page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGroupApi->get_filtered_user_groups_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserGroupFilter**](UserGroupFilter.md)| User Group Filter | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **page_index** | **int**| Page Index of the results to fetch.Default Value: 0 | [optional] [default to 0]
 **page_size** | **int**| Results per page(max 100)Default Value: 50 | [optional] [default to 50]
 **sort_orders** | [**list[SortOrder]**](SortOrder.md)| Sort criteria for the elements. | [optional] 
 **page_token** | **str**| Page Token of the next results to fetch.Default Value: &#x27;&#x27; | [optional] 

### Return type

[**ResponseDTOPageResponseUserGroup**](ResponseDTOPageResponseUserGroup.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inheriting_child_scope_list**
> ResponseDTOListScopeName get_inheriting_child_scope_list(identifier, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Get Inheriting Child Scopes

List the Child Scopes inheriting this User Group

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
api_instance = harness_python_sdk.UserGroupApi(harness_python_sdk.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of the user group
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Get Inheriting Child Scopes
    api_response = api_instance.get_inheriting_child_scope_list(identifier, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGroupApi->get_inheriting_child_scope_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of the user group | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOListScopeName**](ResponseDTOListScopeName.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_member**
> ResponseDTOBoolean get_member(account_identifier, identifier, user_identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Check user membership

Check if the user is part of the user group in an account/org/project

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
api_instance = harness_python_sdk.UserGroupApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
identifier = 'identifier_example' # str | Identifier of the user group
user_identifier = 'user_identifier_example' # str | Identifier of the user
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Check user membership
    api_response = api_instance.get_member(account_identifier, identifier, user_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGroupApi->get_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **identifier** | **str**| Identifier of the user group | 
 **user_identifier** | **str**| Identifier of the user | 
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

# **get_user_group**
> ResponseDTOUserGroup get_user_group(account_identifier, identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Get User Group

Get a User Group in an account/org/project

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
api_instance = harness_python_sdk.UserGroupApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
identifier = 'identifier_example' # str | Identifier of the user group
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Get User Group
    api_response = api_instance.get_user_group(account_identifier, identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGroupApi->get_user_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **identifier** | **str**| Identifier of the user group | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOUserGroup**](ResponseDTOUserGroup.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_group_list**
> ResponseDTOPageResponseUserGroup get_user_group_list(account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, search_term=search_term, filter_type=filter_type, page_index=page_index, page_size=page_size, sort_orders=sort_orders, page_token=page_token)

List the User Groups in an account/org/project

List User Groups

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
api_instance = harness_python_sdk.UserGroupApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
search_term = 'search_term_example' # str | Search filter which matches by user group name/identifier (optional)
filter_type = 'EXCLUDE_INHERITED_GROUPS' # str |  (optional) (default to EXCLUDE_INHERITED_GROUPS)
page_index = 0 # int | Page Index of the results to fetch.Default Value: 0 (optional) (default to 0)
page_size = 50 # int | Results per page(max 100)Default Value: 50 (optional) (default to 50)
sort_orders = [harness_python_sdk.SortOrder()] # list[SortOrder] | Sort criteria for the elements. (optional)
page_token = 'page_token_example' # str | Page Token of the next results to fetch.Default Value: '' (optional)

try:
    # List the User Groups in an account/org/project
    api_response = api_instance.get_user_group_list(account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, search_term=search_term, filter_type=filter_type, page_index=page_index, page_size=page_size, sort_orders=sort_orders, page_token=page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGroupApi->get_user_group_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **search_term** | **str**| Search filter which matches by user group name/identifier | [optional] 
 **filter_type** | **str**|  | [optional] [default to EXCLUDE_INHERITED_GROUPS]
 **page_index** | **int**| Page Index of the results to fetch.Default Value: 0 | [optional] [default to 0]
 **page_size** | **int**| Results per page(max 100)Default Value: 50 | [optional] [default to 50]
 **sort_orders** | [**list[SortOrder]**](SortOrder.md)| Sort criteria for the elements. | [optional] 
 **page_token** | **str**| Page Token of the next results to fetch.Default Value: &#x27;&#x27; | [optional] 

### Return type

[**ResponseDTOPageResponseUserGroup**](ResponseDTOPageResponseUserGroup.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_list_in_user_group**
> ResponseDTOPageResponseUserMetadata get_user_list_in_user_group(account_identifier, identifier, body=body, org_identifier=org_identifier, project_identifier=project_identifier, page_index=page_index, page_size=page_size, sort_orders=sort_orders, page_token=page_token)

List users in User Group

List the users in a User Group in an account/org/project

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
api_instance = harness_python_sdk.UserGroupApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
identifier = 'identifier_example' # str | Identifier of the user group
body = harness_python_sdk.UserFilter() # UserFilter | Filter users based on multiple parameters (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
page_index = 0 # int | Page Index of the results to fetch.Default Value: 0 (optional) (default to 0)
page_size = 50 # int | Results per page(max 100)Default Value: 50 (optional) (default to 50)
sort_orders = [harness_python_sdk.SortOrder()] # list[SortOrder] | Sort criteria for the elements. (optional)
page_token = 'page_token_example' # str | Page Token of the next results to fetch.Default Value: '' (optional)

try:
    # List users in User Group
    api_response = api_instance.get_user_list_in_user_group(account_identifier, identifier, body=body, org_identifier=org_identifier, project_identifier=project_identifier, page_index=page_index, page_size=page_size, sort_orders=sort_orders, page_token=page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGroupApi->get_user_list_in_user_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **identifier** | **str**| Identifier of the user group | 
 **body** | [**UserFilter**](UserFilter.md)| Filter users based on multiple parameters | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **page_index** | **int**| Page Index of the results to fetch.Default Value: 0 | [optional] [default to 0]
 **page_size** | **int**| Results per page(max 100)Default Value: 50 | [optional] [default to 50]
 **sort_orders** | [**list[SortOrder]**](SortOrder.md)| Sort criteria for the elements. | [optional] 
 **page_token** | **str**| Page Token of the next results to fetch.Default Value: &#x27;&#x27; | [optional] 

### Return type

[**ResponseDTOPageResponseUserMetadata**](ResponseDTOPageResponseUserMetadata.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_user_group_to_ldap**
> RestResponseUserGroup link_user_group_to_ldap(body, account_identifier, user_group_id, ldap_id, org_identifier=org_identifier, project_identifier=project_identifier)

Link LDAP Group to the User Group to an account/org/project

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
api_instance = harness_python_sdk.UserGroupApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.LdapLinkGroupRequest() # LdapLinkGroupRequest | LDAP Link Group Request
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
user_group_id = 'user_group_id_example' # str | Identifier of the user group
ldap_id = 'ldap_id_example' # str | LDAP entity identifier
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Link LDAP Group to the User Group to an account/org/project
    api_response = api_instance.link_user_group_to_ldap(body, account_identifier, user_group_id, ldap_id, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGroupApi->link_user_group_to_ldap: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LdapLinkGroupRequest**](LdapLinkGroupRequest.md)| LDAP Link Group Request | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **user_group_id** | **str**| Identifier of the user group | 
 **ldap_id** | **str**| LDAP entity identifier | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**RestResponseUserGroup**](RestResponseUserGroup.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_user_group_to_saml**
> RestResponseUserGroup link_user_group_to_saml(body, account_identifier, user_group_id, saml_id, org_identifier=org_identifier, project_identifier=project_identifier)

Link SAML Group to the User Group in an account/org/project

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
api_instance = harness_python_sdk.UserGroupApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.SamlLinkGroupRequest() # SamlLinkGroupRequest | Saml Link Group Request
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
user_group_id = 'user_group_id_example' # str | Identifier of the user group
saml_id = 'saml_id_example' # str | Saml Group entity identifier
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Link SAML Group to the User Group in an account/org/project
    api_response = api_instance.link_user_group_to_saml(body, account_identifier, user_group_id, saml_id, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGroupApi->link_user_group_to_saml: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SamlLinkGroupRequest**](SamlLinkGroupRequest.md)| Saml Link Group Request | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **user_group_id** | **str**| Identifier of the user group | 
 **saml_id** | **str**| Saml Group entity identifier | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**RestResponseUserGroup**](RestResponseUserGroup.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_user_group**
> ResponseDTOUserGroup post_user_group(body, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Create User Group

Create a User Group in an account/org/project

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
api_instance = harness_python_sdk.UserGroupApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.UserGroup() # UserGroup | User Group entity to be created
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Create User Group
    api_response = api_instance.post_user_group(body, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGroupApi->post_user_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserGroup**](UserGroup.md)| User Group entity to be created | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOUserGroup**](ResponseDTOUserGroup.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_user_group_v2**
> ResponseDTOUserGroupResponseV2 post_user_group_v2(body, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Create User Group

Create a User Group in an account/org/project

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
api_instance = harness_python_sdk.UserGroupApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.UserGroupRequestV2() # UserGroupRequestV2 | User Group entity to be created
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Create User Group
    api_response = api_instance.post_user_group_v2(body, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGroupApi->post_user_group_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserGroupRequestV2**](UserGroupRequestV2.md)| User Group entity to be created | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOUserGroupResponseV2**](ResponseDTOUserGroupResponseV2.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_member**
> ResponseDTOUserGroup put_member(account_identifier, identifier, user_identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Add user to User Group

Add a user to the user group in an account/org/project

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
api_instance = harness_python_sdk.UserGroupApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
identifier = 'identifier_example' # str | Identifier of the user group
user_identifier = 'user_identifier_example' # str | Identifier of the user
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Add user to User Group
    api_response = api_instance.put_member(account_identifier, identifier, user_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGroupApi->put_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **identifier** | **str**| Identifier of the user group | 
 **user_identifier** | **str**| Identifier of the user | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOUserGroup**](ResponseDTOUserGroup.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_user_group**
> ResponseDTOUserGroup put_user_group(body, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Update User Group

Update a User Group in an account/org/project

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
api_instance = harness_python_sdk.UserGroupApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.UserGroup() # UserGroup | User Group entity with the updates
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Update User Group
    api_response = api_instance.put_user_group(body, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGroupApi->put_user_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserGroup**](UserGroup.md)| User Group entity with the updates | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOUserGroup**](ResponseDTOUserGroup.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_user_group_v2**
> ResponseDTOUserGroupResponseV2 put_user_group_v2(body, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Update User Group

Update a User Group in an account/org/project

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
api_instance = harness_python_sdk.UserGroupApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.UserGroupRequestV2() # UserGroupRequestV2 | User Group entity with the updates
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Update User Group
    api_response = api_instance.put_user_group_v2(body, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGroupApi->put_user_group_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserGroupRequestV2**](UserGroupRequestV2.md)| User Group entity with the updates | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOUserGroupResponseV2**](ResponseDTOUserGroupResponseV2.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unlink_user_groupfrom_sso**
> RestResponseUserGroup unlink_user_groupfrom_sso(user_group_id, account_identifier, retain_members=retain_members, org_identifier=org_identifier, project_identifier=project_identifier)

Unlink SSO Group from the User Group in an account/org/project

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
api_instance = harness_python_sdk.UserGroupApi(harness_python_sdk.ApiClient(configuration))
user_group_id = 'user_group_id_example' # str | Identifier of the user group
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
retain_members = true # bool | Retain currently synced members of the user group (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Unlink SSO Group from the User Group in an account/org/project
    api_response = api_instance.unlink_user_groupfrom_sso(user_group_id, account_identifier, retain_members=retain_members, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGroupApi->unlink_user_groupfrom_sso: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_group_id** | **str**| Identifier of the user group | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **retain_members** | **bool**| Retain currently synced members of the user group | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**RestResponseUserGroup**](RestResponseUserGroup.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

