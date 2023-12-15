# swagger_client.TargetGroupsApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_segment**](TargetGroupsApi.md#create_segment) | **POST** /cf/admin/segments | Creates a Target Group
[**delete_segment**](TargetGroupsApi.md#delete_segment) | **DELETE** /cf/admin/segments/{identifier} | Deletes a Target Group
[**get_all_segments**](TargetGroupsApi.md#get_all_segments) | **GET** /cf/admin/segments | Returns all Target Groups
[**get_available_flags_for_segment**](TargetGroupsApi.md#get_available_flags_for_segment) | **GET** /cf/admin/segments/{identifier}/available_flags | Returns Feature Flags that are available to be added to the given Target Group
[**get_segment**](TargetGroupsApi.md#get_segment) | **GET** /cf/admin/segments/{identifier} | Returns Target Group details for the given identifier
[**get_segment_flags**](TargetGroupsApi.md#get_segment_flags) | **GET** /cf/admin/segments/{identifier}/flags | Returns Feature Flags in a Target Group
[**patch_segment**](TargetGroupsApi.md#patch_segment) | **PATCH** /cf/admin/segments/{identifier} | Updates a Target Group

# **create_segment**
> create_segment(body, account_identifier, org_identifier)

Creates a Target Group

Creates a Target Group in the given Project

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
api_instance = swagger_client.TargetGroupsApi(swagger_client.ApiClient(configuration))
body = NULL # object | 
account_identifier = 'account_identifier_example' # str | Account Identifier
org_identifier = 'org_identifier_example' # str | Organization Identifier

try:
    # Creates a Target Group
    api_instance.create_segment(body, account_identifier, org_identifier)
except ApiException as e:
    print("Exception when calling TargetGroupsApi->create_segment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | 
 **account_identifier** | **str**| Account Identifier | 
 **org_identifier** | **str**| Organization Identifier | 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_segment**
> delete_segment(account_identifier, org_identifier, identifier, project_identifier, environment_identifier)

Deletes a Target Group

Deletes a Target Group for the given ID

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
api_instance = swagger_client.TargetGroupsApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier
org_identifier = 'org_identifier_example' # str | Organization Identifier
identifier = 'identifier_example' # str | Unique identifier for the object in the API.
project_identifier = 'project_identifier_example' # str | The Project identifier
environment_identifier = 'environment_identifier_example' # str | Environment Identifier

try:
    # Deletes a Target Group
    api_instance.delete_segment(account_identifier, org_identifier, identifier, project_identifier, environment_identifier)
except ApiException as e:
    print("Exception when calling TargetGroupsApi->delete_segment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier | 
 **org_identifier** | **str**| Organization Identifier | 
 **identifier** | **str**| Unique identifier for the object in the API. | 
 **project_identifier** | **str**| The Project identifier | 
 **environment_identifier** | **str**| Environment Identifier | 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_segments**
> Segments get_all_segments(account_identifier, org_identifier, environment_identifier, project_identifier, page_number=page_number, page_size=page_size, sort_order=sort_order, sort_by_field=sort_by_field, name=name, identifier=identifier)

Returns all Target Groups

Returns Target Group details for the given account

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
api_instance = swagger_client.TargetGroupsApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier
org_identifier = 'org_identifier_example' # str | Organization Identifier
environment_identifier = 'environment_identifier_example' # str | Environment Identifier
project_identifier = 'project_identifier_example' # str | The Project identifier
page_number = 56 # int | PageNumber (optional)
page_size = 56 # int | PageSize (optional)
sort_order = 'sort_order_example' # str | SortOrder (optional)
sort_by_field = 'sort_by_field_example' # str | SortByField (optional)
name = 'name_example' # str | Name of the field (optional)
identifier = 'identifier_example' # str | Identifier of the field (optional)

try:
    # Returns all Target Groups
    api_response = api_instance.get_all_segments(account_identifier, org_identifier, environment_identifier, project_identifier, page_number=page_number, page_size=page_size, sort_order=sort_order, sort_by_field=sort_by_field, name=name, identifier=identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetGroupsApi->get_all_segments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier | 
 **org_identifier** | **str**| Organization Identifier | 
 **environment_identifier** | **str**| Environment Identifier | 
 **project_identifier** | **str**| The Project identifier | 
 **page_number** | **int**| PageNumber | [optional] 
 **page_size** | **int**| PageSize | [optional] 
 **sort_order** | **str**| SortOrder | [optional] 
 **sort_by_field** | **str**| SortByField | [optional] 
 **name** | **str**| Name of the field | [optional] 
 **identifier** | **str**| Identifier of the field | [optional] 

### Return type

[**Segments**](Segments.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_flags_for_segment**
> FlagBasicInfos get_available_flags_for_segment(identifier, account_identifier, org_identifier, project_identifier, environment_identifier, page_number=page_number, page_size=page_size, sort_order=sort_order, sort_by_field=sort_by_field, flag_name_identifier=flag_name_identifier)

Returns Feature Flags that are available to be added to the given Target Group

Returns the list of Feature Flags that the Target Group can be added to.  This list will exclude any Feature Flag that the Target Group is already part of.

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
api_instance = swagger_client.TargetGroupsApi(swagger_client.ApiClient(configuration))
identifier = 'identifier_example' # str | Unique identifier for the object in the API.
account_identifier = 'account_identifier_example' # str | Account Identifier
org_identifier = 'org_identifier_example' # str | Organization Identifier
project_identifier = 'project_identifier_example' # str | The Project identifier
environment_identifier = 'environment_identifier_example' # str | Environment Identifier
page_number = 56 # int | PageNumber (optional)
page_size = 56 # int | PageSize (optional)
sort_order = 'sort_order_example' # str | SortOrder (optional)
sort_by_field = 'sort_by_field_example' # str | SortByField (optional)
flag_name_identifier = 'flag_name_identifier_example' # str | Identifier of the feature flag (optional)

try:
    # Returns Feature Flags that are available to be added to the given Target Group
    api_response = api_instance.get_available_flags_for_segment(identifier, account_identifier, org_identifier, project_identifier, environment_identifier, page_number=page_number, page_size=page_size, sort_order=sort_order, sort_by_field=sort_by_field, flag_name_identifier=flag_name_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetGroupsApi->get_available_flags_for_segment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Unique identifier for the object in the API. | 
 **account_identifier** | **str**| Account Identifier | 
 **org_identifier** | **str**| Organization Identifier | 
 **project_identifier** | **str**| The Project identifier | 
 **environment_identifier** | **str**| Environment Identifier | 
 **page_number** | **int**| PageNumber | [optional] 
 **page_size** | **int**| PageSize | [optional] 
 **sort_order** | **str**| SortOrder | [optional] 
 **sort_by_field** | **str**| SortByField | [optional] 
 **flag_name_identifier** | **str**| Identifier of the feature flag | [optional] 

### Return type

[**FlagBasicInfos**](FlagBasicInfos.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_segment**
> Segment get_segment(account_identifier, org_identifier, identifier, project_identifier, environment_identifier)

Returns Target Group details for the given identifier

Returns Target Group details for the given ID

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
api_instance = swagger_client.TargetGroupsApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier
org_identifier = 'org_identifier_example' # str | Organization Identifier
identifier = 'identifier_example' # str | Unique identifier for the object in the API.
project_identifier = 'project_identifier_example' # str | The Project identifier
environment_identifier = 'environment_identifier_example' # str | Environment Identifier

try:
    # Returns Target Group details for the given identifier
    api_response = api_instance.get_segment(account_identifier, org_identifier, identifier, project_identifier, environment_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetGroupsApi->get_segment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier | 
 **org_identifier** | **str**| Organization Identifier | 
 **identifier** | **str**| Unique identifier for the object in the API. | 
 **project_identifier** | **str**| The Project identifier | 
 **environment_identifier** | **str**| Environment Identifier | 

### Return type

[**Segment**](Segment.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_segment_flags**
> list[SegmentFlag] get_segment_flags(account_identifier, org_identifier, identifier, project_identifier, environment_identifier)

Returns Feature Flags in a Target Group

Returns the details of a Feature Flag in a Target Group for the given identifier

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
api_instance = swagger_client.TargetGroupsApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier
org_identifier = 'org_identifier_example' # str | Organization Identifier
identifier = 'identifier_example' # str | Unique identifier for the object in the API.
project_identifier = 'project_identifier_example' # str | The Project identifier
environment_identifier = 'environment_identifier_example' # str | Environment Identifier

try:
    # Returns Feature Flags in a Target Group
    api_response = api_instance.get_segment_flags(account_identifier, org_identifier, identifier, project_identifier, environment_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetGroupsApi->get_segment_flags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier | 
 **org_identifier** | **str**| Organization Identifier | 
 **identifier** | **str**| Unique identifier for the object in the API. | 
 **project_identifier** | **str**| The Project identifier | 
 **environment_identifier** | **str**| Environment Identifier | 

### Return type

[**list[SegmentFlag]**](SegmentFlag.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_segment**
> Segment patch_segment(account_identifier, org_identifier, project_identifier, environment_identifier, identifier, body=body)

Updates a Target Group

Updates a Target Group for the given identifier

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
api_instance = swagger_client.TargetGroupsApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier
org_identifier = 'org_identifier_example' # str | Organization Identifier
project_identifier = 'project_identifier_example' # str | The Project identifier
environment_identifier = 'environment_identifier_example' # str | Environment Identifier
identifier = 'identifier_example' # str | Unique identifier for the object in the API.
body = swagger_client.GitSyncPatchOperation() # GitSyncPatchOperation |  (optional)

try:
    # Updates a Target Group
    api_response = api_instance.patch_segment(account_identifier, org_identifier, project_identifier, environment_identifier, identifier, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetGroupsApi->patch_segment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier | 
 **org_identifier** | **str**| Organization Identifier | 
 **project_identifier** | **str**| The Project identifier | 
 **environment_identifier** | **str**| Environment Identifier | 
 **identifier** | **str**| Unique identifier for the object in the API. | 
 **body** | [**GitSyncPatchOperation**](GitSyncPatchOperation.md)|  | [optional] 

### Return type

[**Segment**](Segment.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

