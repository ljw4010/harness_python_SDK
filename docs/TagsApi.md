# swagger_client.TagsApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tag**](TagsApi.md#create_tag) | **POST** /cf/admin/tags | Creates a Tag
[**delete_tag**](TagsApi.md#delete_tag) | **DELETE** /cf/admin/tags/{identifier} | Delete a Tag
[**get_all_tags**](TagsApi.md#get_all_tags) | **GET** /cf/admin/tags | Returns all Tags
[**get_tag**](TagsApi.md#get_tag) | **GET** /cf/admin/tags/{identifier} | Returns a Tag

# **create_tag**
> TagResponseMetadata create_tag(body, account_identifier, org_identifier, project_identifier)

Creates a Tag

Create Tags for the given identifier

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
api_instance = swagger_client.TagsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Tag() # Tag | 
account_identifier = 'account_identifier_example' # str | Account Identifier
org_identifier = 'org_identifier_example' # str | Organization Identifier
project_identifier = 'project_identifier_example' # str | The Project identifier

try:
    # Creates a Tag
    api_response = api_instance.create_tag(body, account_identifier, org_identifier, project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->create_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Tag**](Tag.md)|  | 
 **account_identifier** | **str**| Account Identifier | 
 **org_identifier** | **str**| Organization Identifier | 
 **project_identifier** | **str**| The Project identifier | 

### Return type

[**TagResponseMetadata**](TagResponseMetadata.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tag**
> delete_tag(identifier, account_identifier, org_identifier, project_identifier, commit_msg=commit_msg, force_delete=force_delete)

Delete a Tag

Delete Tag for the given identifier and account ID

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
api_instance = swagger_client.TagsApi(swagger_client.ApiClient(configuration))
identifier = 'identifier_example' # str | Unique identifier for the object in the API.
account_identifier = 'account_identifier_example' # str | Account Identifier
org_identifier = 'org_identifier_example' # str | Organization Identifier
project_identifier = 'project_identifier_example' # str | The Project identifier
commit_msg = 'commit_msg_example' # str | Git commit message (optional)
force_delete = true # bool | Permanently deletes the the feature flag (optional)

try:
    # Delete a Tag
    api_instance.delete_tag(identifier, account_identifier, org_identifier, project_identifier, commit_msg=commit_msg, force_delete=force_delete)
except ApiException as e:
    print("Exception when calling TagsApi->delete_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Unique identifier for the object in the API. | 
 **account_identifier** | **str**| Account Identifier | 
 **org_identifier** | **str**| Organization Identifier | 
 **project_identifier** | **str**| The Project identifier | 
 **commit_msg** | **str**| Git commit message | [optional] 
 **force_delete** | **bool**| Permanently deletes the the feature flag | [optional] 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_tags**
> Tags get_all_tags(account_identifier, org_identifier, project_identifier, environment_identifier, page_number=page_number, page_size=page_size, sort_order=sort_order, sort_by_field=sort_by_field, tag_identifier_filter=tag_identifier_filter)

Returns all Tags

Returns all the Tags for the given Account ID

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
api_instance = swagger_client.TagsApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier
org_identifier = 'org_identifier_example' # str | Organization Identifier
project_identifier = 'project_identifier_example' # str | The Project identifier
environment_identifier = 'environment_identifier_example' # str | Environment Identifier
page_number = 56 # int | PageNumber (optional)
page_size = 56 # int | PageSize (optional)
sort_order = 'sort_order_example' # str | SortOrder (optional)
sort_by_field = 'sort_by_field_example' # str | SortByField (optional)
tag_identifier_filter = 'tag_identifier_filter_example' # str | Partial Search of Tag Identifiers to filter on (optional)

try:
    # Returns all Tags
    api_response = api_instance.get_all_tags(account_identifier, org_identifier, project_identifier, environment_identifier, page_number=page_number, page_size=page_size, sort_order=sort_order, sort_by_field=sort_by_field, tag_identifier_filter=tag_identifier_filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->get_all_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier | 
 **org_identifier** | **str**| Organization Identifier | 
 **project_identifier** | **str**| The Project identifier | 
 **environment_identifier** | **str**| Environment Identifier | 
 **page_number** | **int**| PageNumber | [optional] 
 **page_size** | **int**| PageSize | [optional] 
 **sort_order** | **str**| SortOrder | [optional] 
 **sort_by_field** | **str**| SortByField | [optional] 
 **tag_identifier_filter** | **str**| Partial Search of Tag Identifiers to filter on | [optional] 

### Return type

[**Tags**](Tags.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tag**
> Feature get_tag(identifier, account_identifier, org_identifier, project_identifier, environment_identifier=environment_identifier, metrics=metrics, archived=archived)

Returns a Tag

Returns details such as identifier,Associated Feature Flag etc for the given Tag

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
api_instance = swagger_client.TagsApi(swagger_client.ApiClient(configuration))
identifier = 'identifier_example' # str | Unique identifier for the object in the API.
account_identifier = 'account_identifier_example' # str | Account Identifier
org_identifier = 'org_identifier_example' # str | Organization Identifier
project_identifier = 'project_identifier_example' # str | The Project identifier
environment_identifier = 'environment_identifier_example' # str | Environment (optional)
metrics = true # bool | Parameter to indicate if metrics data is requested in response (optional)
archived = true # bool | Status of the feature flag (optional)

try:
    # Returns a Tag
    api_response = api_instance.get_tag(identifier, account_identifier, org_identifier, project_identifier, environment_identifier=environment_identifier, metrics=metrics, archived=archived)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->get_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Unique identifier for the object in the API. | 
 **account_identifier** | **str**| Account Identifier | 
 **org_identifier** | **str**| Organization Identifier | 
 **project_identifier** | **str**| The Project identifier | 
 **environment_identifier** | **str**| Environment | [optional] 
 **metrics** | **bool**| Parameter to indicate if metrics data is requested in response | [optional] 
 **archived** | **bool**| Status of the feature flag | [optional] 

### Return type

[**Feature**](Feature.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

