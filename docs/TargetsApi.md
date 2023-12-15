# harness_python_sdk.TargetsApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_target**](TargetsApi.md#create_target) | **POST** /cf/admin/targets | Creates a Target
[**delete_target**](TargetsApi.md#delete_target) | **DELETE** /cf/admin/targets/{identifier} | Deletes a Target
[**get_all_targets**](TargetsApi.md#get_all_targets) | **GET** /cf/admin/targets | Returns all Targets
[**get_target**](TargetsApi.md#get_target) | **GET** /cf/admin/targets/{identifier} | Returns details of a Target
[**get_target_segments**](TargetsApi.md#get_target_segments) | **GET** /cf/admin/targets/{identifier}/segments | Returns Target Groups for the given Target
[**modify_target**](TargetsApi.md#modify_target) | **PUT** /cf/admin/targets/{identifier} | Modifies a Target
[**patch_target**](TargetsApi.md#patch_target) | **PATCH** /cf/admin/targets/{identifier} | Updates a Target
[**upload_targets**](TargetsApi.md#upload_targets) | **POST** /cf/admin/targets/upload | Add Target details

# **create_target**
> create_target(body, account_identifier, org_identifier)

Creates a Target

Create Targets for the given identifier

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
api_instance = harness_python_sdk.TargetsApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.Target() # Target | 
account_identifier = 'account_identifier_example' # str | Account Identifier
org_identifier = 'org_identifier_example' # str | Organization Identifier

try:
    # Creates a Target
    api_instance.create_target(body, account_identifier, org_identifier)
except ApiException as e:
    print("Exception when calling TargetsApi->create_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Target**](Target.md)|  | 
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

# **delete_target**
> delete_target(identifier, account_identifier, org_identifier, project_identifier, environment_identifier)

Deletes a Target

Deletes a Target for the given identifier

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
api_instance = harness_python_sdk.TargetsApi(harness_python_sdk.ApiClient(configuration))
identifier = 'identifier_example' # str | Unique identifier for the object in the API.
account_identifier = 'account_identifier_example' # str | Account Identifier
org_identifier = 'org_identifier_example' # str | Organization Identifier
project_identifier = 'project_identifier_example' # str | The Project identifier
environment_identifier = 'environment_identifier_example' # str | Environment Identifier

try:
    # Deletes a Target
    api_instance.delete_target(identifier, account_identifier, org_identifier, project_identifier, environment_identifier)
except ApiException as e:
    print("Exception when calling TargetsApi->delete_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Unique identifier for the object in the API. | 
 **account_identifier** | **str**| Account Identifier | 
 **org_identifier** | **str**| Organization Identifier | 
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

# **get_all_targets**
> Targets get_all_targets(account_identifier, org_identifier, project_identifier, environment_identifier, page_number=page_number, page_size=page_size, sort_order=sort_order, sort_by_field=sort_by_field, target_name=target_name, target_identifier=target_identifier)

Returns all Targets

Returns all the Targets for the given Account ID

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
api_instance = harness_python_sdk.TargetsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier
org_identifier = 'org_identifier_example' # str | Organization Identifier
project_identifier = 'project_identifier_example' # str | The Project identifier
environment_identifier = 'environment_identifier_example' # str | Environment Identifier
page_number = 56 # int | PageNumber (optional)
page_size = 56 # int | PageSize (optional)
sort_order = 'sort_order_example' # str | SortOrder (optional)
sort_by_field = 'sort_by_field_example' # str | SortByField (optional)
target_name = 'target_name_example' # str | Name of the target (optional)
target_identifier = 'target_identifier_example' # str | Identifier of the target (optional)

try:
    # Returns all Targets
    api_response = api_instance.get_all_targets(account_identifier, org_identifier, project_identifier, environment_identifier, page_number=page_number, page_size=page_size, sort_order=sort_order, sort_by_field=sort_by_field, target_name=target_name, target_identifier=target_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetsApi->get_all_targets: %s\n" % e)
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
 **target_name** | **str**| Name of the target | [optional] 
 **target_identifier** | **str**| Identifier of the target | [optional] 

### Return type

[**Targets**](Targets.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_target**
> Target get_target(identifier, account_identifier, org_identifier, project_identifier, environment_identifier)

Returns details of a Target

Returns details of a Target for the given identifier

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
api_instance = harness_python_sdk.TargetsApi(harness_python_sdk.ApiClient(configuration))
identifier = 'identifier_example' # str | Unique identifier for the object in the API.
account_identifier = 'account_identifier_example' # str | Account Identifier
org_identifier = 'org_identifier_example' # str | Organization Identifier
project_identifier = 'project_identifier_example' # str | The Project identifier
environment_identifier = 'environment_identifier_example' # str | Environment Identifier

try:
    # Returns details of a Target
    api_response = api_instance.get_target(identifier, account_identifier, org_identifier, project_identifier, environment_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetsApi->get_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Unique identifier for the object in the API. | 
 **account_identifier** | **str**| Account Identifier | 
 **org_identifier** | **str**| Organization Identifier | 
 **project_identifier** | **str**| The Project identifier | 
 **environment_identifier** | **str**| Environment Identifier | 

### Return type

[**Target**](Target.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_target_segments**
> TargetDetail get_target_segments(identifier, account_identifier, org_identifier, project_identifier, environment_identifier)

Returns Target Groups for the given Target

Returns the Target Groups that the specified Target belongs to.

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
api_instance = harness_python_sdk.TargetsApi(harness_python_sdk.ApiClient(configuration))
identifier = 'identifier_example' # str | Unique identifier for the object in the API.
account_identifier = 'account_identifier_example' # str | Account Identifier
org_identifier = 'org_identifier_example' # str | Organization Identifier
project_identifier = 'project_identifier_example' # str | The Project identifier
environment_identifier = 'environment_identifier_example' # str | Environment Identifier

try:
    # Returns Target Groups for the given Target
    api_response = api_instance.get_target_segments(identifier, account_identifier, org_identifier, project_identifier, environment_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetsApi->get_target_segments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Unique identifier for the object in the API. | 
 **account_identifier** | **str**| Account Identifier | 
 **org_identifier** | **str**| Organization Identifier | 
 **project_identifier** | **str**| The Project identifier | 
 **environment_identifier** | **str**| Environment Identifier | 

### Return type

[**TargetDetail**](TargetDetail.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_target**
> Target modify_target(body, account_identifier, org_identifier, project_identifier, environment_identifier, identifier)

Modifies a Target

Modifies a Target for the given account identifier

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
api_instance = harness_python_sdk.TargetsApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.Target() # Target | 
account_identifier = 'account_identifier_example' # str | Account Identifier
org_identifier = 'org_identifier_example' # str | Organization Identifier
project_identifier = 'project_identifier_example' # str | The Project identifier
environment_identifier = 'environment_identifier_example' # str | Environment Identifier
identifier = 'identifier_example' # str | Unique identifier for the object in the API.

try:
    # Modifies a Target
    api_response = api_instance.modify_target(body, account_identifier, org_identifier, project_identifier, environment_identifier, identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetsApi->modify_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Target**](Target.md)|  | 
 **account_identifier** | **str**| Account Identifier | 
 **org_identifier** | **str**| Organization Identifier | 
 **project_identifier** | **str**| The Project identifier | 
 **environment_identifier** | **str**| Environment Identifier | 
 **identifier** | **str**| Unique identifier for the object in the API. | 

### Return type

[**Target**](Target.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_target**
> Target patch_target(account_identifier, org_identifier, project_identifier, environment_identifier, identifier, body=body)

Updates a Target

Updates a Target for the given identifier

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
api_instance = harness_python_sdk.TargetsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier
org_identifier = 'org_identifier_example' # str | Organization Identifier
project_identifier = 'project_identifier_example' # str | The Project identifier
environment_identifier = 'environment_identifier_example' # str | Environment Identifier
identifier = 'identifier_example' # str | Unique identifier for the object in the API.
body = harness_python_sdk.GitSyncPatchOperation() # GitSyncPatchOperation |  (optional)

try:
    # Updates a Target
    api_response = api_instance.patch_target(account_identifier, org_identifier, project_identifier, environment_identifier, identifier, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetsApi->patch_target: %s\n" % e)
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

[**Target**](Target.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_targets**
> upload_targets(account_identifier, org_identifier, project_identifier, environment_identifier, file_name=file_name)

Add Target details

Add targets by uploading a CSV file

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
api_instance = harness_python_sdk.TargetsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier
org_identifier = 'org_identifier_example' # str | Organization Identifier
project_identifier = 'project_identifier_example' # str | The Project identifier
environment_identifier = 'environment_identifier_example' # str | Environment Identifier
file_name = 'file_name_example' # str |  (optional)

try:
    # Add Target details
    api_instance.upload_targets(account_identifier, org_identifier, project_identifier, environment_identifier, file_name=file_name)
except ApiException as e:
    print("Exception when calling TargetsApi->upload_targets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier | 
 **org_identifier** | **str**| Organization Identifier | 
 **project_identifier** | **str**| The Project identifier | 
 **environment_identifier** | **str**| Environment Identifier | 
 **file_name** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

