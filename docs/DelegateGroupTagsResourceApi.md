# swagger_client.DelegateGroupTagsResourceApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_tags_to_delegate_group**](DelegateGroupTagsResourceApi.md#add_tags_to_delegate_group) | **POST** /ng/api/delegate-group-tags/{groupIdentifier} | Add given list of tags to the Delegate group
[**delete_tags_from_delegate_group**](DelegateGroupTagsResourceApi.md#delete_tags_from_delegate_group) | **DELETE** /ng/api/delegate-group-tags/{groupIdentifier} | Deletes all tags from the Delegate group
[**list_delegate_groups_using_tags**](DelegateGroupTagsResourceApi.md#list_delegate_groups_using_tags) | **POST** /ng/api/delegate-group-tags/delegate-groups | List delegate groups that are having mentioned tags.
[**list_tags_for_delegate_group**](DelegateGroupTagsResourceApi.md#list_tags_for_delegate_group) | **GET** /ng/api/delegate-group-tags/{groupIdentifier} | Retrieves list of tags attached with Delegate group
[**update_tags_of_delegate_group**](DelegateGroupTagsResourceApi.md#update_tags_of_delegate_group) | **PUT** /ng/api/delegate-group-tags/{groupIdentifier} | Clears all existing tags with delegate group and attach given set of tags to delegate group.

# **add_tags_to_delegate_group**
> RestResponseDelegateGroupDTO add_tags_to_delegate_group(body, account_identifier, group_identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Add given list of tags to the Delegate group

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
api_instance = swagger_client.DelegateGroupTagsResourceApi(swagger_client.ApiClient(configuration))
body = swagger_client.DelegateGroupTags() # DelegateGroupTags | Set of tags
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
group_identifier = 'group_identifier_example' # str | Delegate Group Identifier
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Add given list of tags to the Delegate group
    api_response = api_instance.add_tags_to_delegate_group(body, account_identifier, group_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DelegateGroupTagsResourceApi->add_tags_to_delegate_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DelegateGroupTags**](DelegateGroupTags.md)| Set of tags | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **group_identifier** | **str**| Delegate Group Identifier | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**RestResponseDelegateGroupDTO**](RestResponseDelegateGroupDTO.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tags_from_delegate_group**
> RestResponseDelegateGroupDTO delete_tags_from_delegate_group(account_identifier, group_identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Deletes all tags from the Delegate group

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
api_instance = swagger_client.DelegateGroupTagsResourceApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
group_identifier = 'group_identifier_example' # str | Delegate Group Identifier
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Deletes all tags from the Delegate group
    api_response = api_instance.delete_tags_from_delegate_group(account_identifier, group_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DelegateGroupTagsResourceApi->delete_tags_from_delegate_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **group_identifier** | **str**| Delegate Group Identifier | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**RestResponseDelegateGroupDTO**](RestResponseDelegateGroupDTO.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_delegate_groups_using_tags**
> RestResponseListDelegateGroupDTO list_delegate_groups_using_tags(body, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)

List delegate groups that are having mentioned tags.

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
api_instance = swagger_client.DelegateGroupTagsResourceApi(swagger_client.ApiClient(configuration))
body = swagger_client.DelegateGroupTags() # DelegateGroupTags | Set of tags
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # List delegate groups that are having mentioned tags.
    api_response = api_instance.list_delegate_groups_using_tags(body, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DelegateGroupTagsResourceApi->list_delegate_groups_using_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DelegateGroupTags**](DelegateGroupTags.md)| Set of tags | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**RestResponseListDelegateGroupDTO**](RestResponseListDelegateGroupDTO.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tags_for_delegate_group**
> RestResponseDelegateGroupDTO list_tags_for_delegate_group(account_identifier, group_identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Retrieves list of tags attached with Delegate group

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
api_instance = swagger_client.DelegateGroupTagsResourceApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
group_identifier = 'group_identifier_example' # str | Delegate Group Identifier
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Retrieves list of tags attached with Delegate group
    api_response = api_instance.list_tags_for_delegate_group(account_identifier, group_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DelegateGroupTagsResourceApi->list_tags_for_delegate_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **group_identifier** | **str**| Delegate Group Identifier | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**RestResponseDelegateGroupDTO**](RestResponseDelegateGroupDTO.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tags_of_delegate_group**
> RestResponseDelegateGroupDTO update_tags_of_delegate_group(body, account_identifier, group_identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Clears all existing tags with delegate group and attach given set of tags to delegate group.

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
api_instance = swagger_client.DelegateGroupTagsResourceApi(swagger_client.ApiClient(configuration))
body = swagger_client.DelegateGroupTags() # DelegateGroupTags | Set of tags
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
group_identifier = 'group_identifier_example' # str | Delegate Group Identifier
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Clears all existing tags with delegate group and attach given set of tags to delegate group.
    api_response = api_instance.update_tags_of_delegate_group(body, account_identifier, group_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DelegateGroupTagsResourceApi->update_tags_of_delegate_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DelegateGroupTags**](DelegateGroupTags.md)| Set of tags | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **group_identifier** | **str**| Delegate Group Identifier | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**RestResponseDelegateGroupDTO**](RestResponseDelegateGroupDTO.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

