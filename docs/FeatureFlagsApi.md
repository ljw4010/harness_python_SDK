# harness_python_sdk.FeatureFlagsApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_feature_flag**](FeatureFlagsApi.md#create_feature_flag) | **POST** /cf/admin/features | Creates a Feature Flag
[**delete_feature_flag**](FeatureFlagsApi.md#delete_feature_flag) | **DELETE** /cf/admin/features/{identifier} | Delete a Feature Flag
[**get_all_features**](FeatureFlagsApi.md#get_all_features) | **GET** /cf/admin/features | Returns all Feature Flags for the project
[**get_dependent_features**](FeatureFlagsApi.md#get_dependent_features) | **GET** /cf/admin/features/{identifier}/dependants | Return a list of dependant flags
[**get_feature_flag**](FeatureFlagsApi.md#get_feature_flag) | **GET** /cf/admin/features/{identifier} | Returns a Feature Flag
[**patch_feature**](FeatureFlagsApi.md#patch_feature) | **PATCH** /cf/admin/features/{identifier} | Updates a Feature Flag
[**restore_feature_flag**](FeatureFlagsApi.md#restore_feature_flag) | **POST** /cf/admin/features/{identifier}/restore | Restore a Feature Flag

# **create_feature_flag**
> FeatureResponseMetadata create_feature_flag(account_identifier, org_identifier, body=body)

Creates a Feature Flag

Creates a Feature Flag in the Project

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
api_instance = harness_python_sdk.FeatureFlagsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier
org_identifier = 'org_identifier_example' # str | Organization Identifier
body = NULL # object |  (optional)

try:
    # Creates a Feature Flag
    api_response = api_instance.create_feature_flag(account_identifier, org_identifier, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeatureFlagsApi->create_feature_flag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier | 
 **org_identifier** | **str**| Organization Identifier | 
 **body** | [**object**](object.md)|  | [optional] 

### Return type

[**FeatureResponseMetadata**](FeatureResponseMetadata.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_feature_flag**
> delete_feature_flag(identifier, account_identifier, org_identifier, project_identifier, commit_msg=commit_msg, force_delete=force_delete)

Delete a Feature Flag

Delete Feature Flag for the given identifier and account ID

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
api_instance = harness_python_sdk.FeatureFlagsApi(harness_python_sdk.ApiClient(configuration))
identifier = 'identifier_example' # str | Unique identifier for the object in the API.
account_identifier = 'account_identifier_example' # str | Account Identifier
org_identifier = 'org_identifier_example' # str | Organization Identifier
project_identifier = 'project_identifier_example' # str | The Project identifier
commit_msg = 'commit_msg_example' # str | Git commit message (optional)
force_delete = true # bool | Permanently deletes the the feature flag (optional)

try:
    # Delete a Feature Flag
    api_instance.delete_feature_flag(identifier, account_identifier, org_identifier, project_identifier, commit_msg=commit_msg, force_delete=force_delete)
except ApiException as e:
    print("Exception when calling FeatureFlagsApi->delete_feature_flag: %s\n" % e)
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

# **get_all_features**
> Features get_all_features(account_identifier, org_identifier, project_identifier, environment_identifier=environment_identifier, page_number=page_number, page_size=page_size, sort_order=sort_order, sort_by_field=sort_by_field, name=name, identifier=identifier, archived=archived, kind=kind, target_identifier=target_identifier, target_identifier_filter=target_identifier_filter, metrics=metrics, feature_identifiers=feature_identifiers, excluded_features=excluded_features, status=status, lifetime=lifetime, enabled=enabled, flag_counts=flag_counts, summary=summary, tags=tags)

Returns all Feature Flags for the project

Returns all the Feature Flag details for the given project

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
api_instance = harness_python_sdk.FeatureFlagsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier
org_identifier = 'org_identifier_example' # str | Organization Identifier
project_identifier = 'project_identifier_example' # str | The Project identifier
environment_identifier = 'environment_identifier_example' # str | Environment (optional)
page_number = 56 # int | PageNumber (optional)
page_size = 56 # int | PageSize (optional)
sort_order = 'sort_order_example' # str | SortOrder (optional)
sort_by_field = 'sort_by_field_example' # str | SortByField (optional)
name = 'name_example' # str | Name of the field (optional)
identifier = 'identifier_example' # str | Identifier of the field (optional)
archived = true # bool | Status of the feature flag (optional)
kind = 'kind_example' # str | Kind of the feature flag (optional)
target_identifier = 'target_identifier_example' # str | Identifier of a target (optional)
target_identifier_filter = 'target_identifier_filter_example' # str | Identifier of the target to filter on (optional)
metrics = true # bool | Parameter to indicate if metrics data is requested in response (optional)
feature_identifiers = 'feature_identifiers_example' # str | Comma separated identifiers for multiple Features (optional)
excluded_features = 'excluded_features_example' # str | Comma separated identifiers to exclude from the response (optional)
status = 'status_example' # str | Filter for flags based on their status (active,never-requested,recently-accessed,potentially-stale) (optional)
lifetime = 'lifetime_example' # str | Filter for flags based on their lifetime (permanent/temporary) (optional)
enabled = true # bool | Filter for flags based on if they are enabled or disabled (optional)
flag_counts = true # bool | Returns counts for the different types of flags e.g num active, potentially-stale, recently-accessed etc (optional)
summary = true # bool | Returns summary info on flags if set to true (optional)
tags = 'tags_example' # str | Filter for flags based on their tag values supplied as comma separated list (optional)

try:
    # Returns all Feature Flags for the project
    api_response = api_instance.get_all_features(account_identifier, org_identifier, project_identifier, environment_identifier=environment_identifier, page_number=page_number, page_size=page_size, sort_order=sort_order, sort_by_field=sort_by_field, name=name, identifier=identifier, archived=archived, kind=kind, target_identifier=target_identifier, target_identifier_filter=target_identifier_filter, metrics=metrics, feature_identifiers=feature_identifiers, excluded_features=excluded_features, status=status, lifetime=lifetime, enabled=enabled, flag_counts=flag_counts, summary=summary, tags=tags)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeatureFlagsApi->get_all_features: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier | 
 **org_identifier** | **str**| Organization Identifier | 
 **project_identifier** | **str**| The Project identifier | 
 **environment_identifier** | **str**| Environment | [optional] 
 **page_number** | **int**| PageNumber | [optional] 
 **page_size** | **int**| PageSize | [optional] 
 **sort_order** | **str**| SortOrder | [optional] 
 **sort_by_field** | **str**| SortByField | [optional] 
 **name** | **str**| Name of the field | [optional] 
 **identifier** | **str**| Identifier of the field | [optional] 
 **archived** | **bool**| Status of the feature flag | [optional] 
 **kind** | **str**| Kind of the feature flag | [optional] 
 **target_identifier** | **str**| Identifier of a target | [optional] 
 **target_identifier_filter** | **str**| Identifier of the target to filter on | [optional] 
 **metrics** | **bool**| Parameter to indicate if metrics data is requested in response | [optional] 
 **feature_identifiers** | **str**| Comma separated identifiers for multiple Features | [optional] 
 **excluded_features** | **str**| Comma separated identifiers to exclude from the response | [optional] 
 **status** | **str**| Filter for flags based on their status (active,never-requested,recently-accessed,potentially-stale) | [optional] 
 **lifetime** | **str**| Filter for flags based on their lifetime (permanent/temporary) | [optional] 
 **enabled** | **bool**| Filter for flags based on if they are enabled or disabled | [optional] 
 **flag_counts** | **bool**| Returns counts for the different types of flags e.g num active, potentially-stale, recently-accessed etc | [optional] 
 **summary** | **bool**| Returns summary info on flags if set to true | [optional] 
 **tags** | **str**| Filter for flags based on their tag values supplied as comma separated list | [optional] 

### Return type

[**Features**](Features.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dependent_features**
> Features get_dependent_features(identifier, account_identifier, org_identifier, project_identifier, environment_identifier=environment_identifier, page_number=page_number, page_size=page_size, sort_order=sort_order, sort_by_field=sort_by_field, name=name, archived=archived, kind=kind, target_identifier=target_identifier, target_identifier_filter=target_identifier_filter, metrics=metrics, feature_identifiers=feature_identifiers, excluded_features=excluded_features, status=status, lifetime=lifetime, enabled=enabled, flag_counts=flag_counts, summary=summary, tags=tags)

Return a list of dependant flags

Given identifier return list all the flags which depend on it.

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
api_instance = harness_python_sdk.FeatureFlagsApi(harness_python_sdk.ApiClient(configuration))
identifier = 'identifier_example' # str | Unique identifier for the object in the API.
account_identifier = 'account_identifier_example' # str | Account Identifier
org_identifier = 'org_identifier_example' # str | Organization Identifier
project_identifier = 'project_identifier_example' # str | The Project identifier
environment_identifier = 'environment_identifier_example' # str | Environment (optional)
page_number = 56 # int | PageNumber (optional)
page_size = 56 # int | PageSize (optional)
sort_order = 'sort_order_example' # str | SortOrder (optional)
sort_by_field = 'sort_by_field_example' # str | SortByField (optional)
name = 'name_example' # str | Name of the field (optional)
archived = true # bool | Status of the feature flag (optional)
kind = 'kind_example' # str | Kind of the feature flag (optional)
target_identifier = 'target_identifier_example' # str | Identifier of a target (optional)
target_identifier_filter = 'target_identifier_filter_example' # str | Identifier of the target to filter on (optional)
metrics = true # bool | Parameter to indicate if metrics data is requested in response (optional)
feature_identifiers = 'feature_identifiers_example' # str | Comma separated identifiers for multiple Features (optional)
excluded_features = 'excluded_features_example' # str | Comma separated identifiers to exclude from the response (optional)
status = 'status_example' # str | Filter for flags based on their status (active,never-requested,recently-accessed,potentially-stale) (optional)
lifetime = 'lifetime_example' # str | Filter for flags based on their lifetime (permanent/temporary) (optional)
enabled = true # bool | Filter for flags based on if they are enabled or disabled (optional)
flag_counts = true # bool | Returns counts for the different types of flags e.g num active, potentially-stale, recently-accessed etc (optional)
summary = true # bool | Returns summary info on flags if set to true (optional)
tags = 'tags_example' # str | Filter for flags based on their tag values supplied as comma separated list (optional)

try:
    # Return a list of dependant flags
    api_response = api_instance.get_dependent_features(identifier, account_identifier, org_identifier, project_identifier, environment_identifier=environment_identifier, page_number=page_number, page_size=page_size, sort_order=sort_order, sort_by_field=sort_by_field, name=name, archived=archived, kind=kind, target_identifier=target_identifier, target_identifier_filter=target_identifier_filter, metrics=metrics, feature_identifiers=feature_identifiers, excluded_features=excluded_features, status=status, lifetime=lifetime, enabled=enabled, flag_counts=flag_counts, summary=summary, tags=tags)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeatureFlagsApi->get_dependent_features: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Unique identifier for the object in the API. | 
 **account_identifier** | **str**| Account Identifier | 
 **org_identifier** | **str**| Organization Identifier | 
 **project_identifier** | **str**| The Project identifier | 
 **environment_identifier** | **str**| Environment | [optional] 
 **page_number** | **int**| PageNumber | [optional] 
 **page_size** | **int**| PageSize | [optional] 
 **sort_order** | **str**| SortOrder | [optional] 
 **sort_by_field** | **str**| SortByField | [optional] 
 **name** | **str**| Name of the field | [optional] 
 **archived** | **bool**| Status of the feature flag | [optional] 
 **kind** | **str**| Kind of the feature flag | [optional] 
 **target_identifier** | **str**| Identifier of a target | [optional] 
 **target_identifier_filter** | **str**| Identifier of the target to filter on | [optional] 
 **metrics** | **bool**| Parameter to indicate if metrics data is requested in response | [optional] 
 **feature_identifiers** | **str**| Comma separated identifiers for multiple Features | [optional] 
 **excluded_features** | **str**| Comma separated identifiers to exclude from the response | [optional] 
 **status** | **str**| Filter for flags based on their status (active,never-requested,recently-accessed,potentially-stale) | [optional] 
 **lifetime** | **str**| Filter for flags based on their lifetime (permanent/temporary) | [optional] 
 **enabled** | **bool**| Filter for flags based on if they are enabled or disabled | [optional] 
 **flag_counts** | **bool**| Returns counts for the different types of flags e.g num active, potentially-stale, recently-accessed etc | [optional] 
 **summary** | **bool**| Returns summary info on flags if set to true | [optional] 
 **tags** | **str**| Filter for flags based on their tag values supplied as comma separated list | [optional] 

### Return type

[**Features**](Features.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_feature_flag**
> Feature get_feature_flag(identifier, account_identifier, org_identifier, project_identifier, environment_identifier=environment_identifier, metrics=metrics, archived=archived)

Returns a Feature Flag

Returns details such as Variation name, identifier etc for the given Feature Flag

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
api_instance = harness_python_sdk.FeatureFlagsApi(harness_python_sdk.ApiClient(configuration))
identifier = 'identifier_example' # str | Unique identifier for the object in the API.
account_identifier = 'account_identifier_example' # str | Account Identifier
org_identifier = 'org_identifier_example' # str | Organization Identifier
project_identifier = 'project_identifier_example' # str | The Project identifier
environment_identifier = 'environment_identifier_example' # str | Environment (optional)
metrics = true # bool | Parameter to indicate if metrics data is requested in response (optional)
archived = true # bool | Status of the feature flag (optional)

try:
    # Returns a Feature Flag
    api_response = api_instance.get_feature_flag(identifier, account_identifier, org_identifier, project_identifier, environment_identifier=environment_identifier, metrics=metrics, archived=archived)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeatureFlagsApi->get_feature_flag: %s\n" % e)
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

# **patch_feature**
> FeatureResponseMetadata patch_feature(account_identifier, org_identifier, project_identifier, identifier, body=body, environment_identifier=environment_identifier)

Updates a Feature Flag

This operation is used to modify a Feature Flag.  The request body can include one or more instructions that can modify flag attributes such as the state (off|on), the variations that are returned and serving rules. For example if you want to turn a flag off you can use this opeartion and send the setFeatureFlagState  {   \"kind\": \"setFeatureFlagState\",   \"parameters\": {     \"state\": \"off\"   } } 

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
api_instance = harness_python_sdk.FeatureFlagsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier
org_identifier = 'org_identifier_example' # str | Organization Identifier
project_identifier = 'project_identifier_example' # str | The Project identifier
identifier = 'identifier_example' # str | Unique identifier for the object in the API.
body = harness_python_sdk.GitSyncPatchOperation() # GitSyncPatchOperation |  (optional)
environment_identifier = 'environment_identifier_example' # str | Environment (optional)

try:
    # Updates a Feature Flag
    api_response = api_instance.patch_feature(account_identifier, org_identifier, project_identifier, identifier, body=body, environment_identifier=environment_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeatureFlagsApi->patch_feature: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier | 
 **org_identifier** | **str**| Organization Identifier | 
 **project_identifier** | **str**| The Project identifier | 
 **identifier** | **str**| Unique identifier for the object in the API. | 
 **body** | [**GitSyncPatchOperation**](GitSyncPatchOperation.md)|  | [optional] 
 **environment_identifier** | **str**| Environment | [optional] 

### Return type

[**FeatureResponseMetadata**](FeatureResponseMetadata.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_feature_flag**
> restore_feature_flag(identifier, account_identifier, org_identifier, project_identifier, commit_msg=commit_msg)

Restore a Feature Flag

Restore Feature Flag for the given identifier and account ID

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
api_instance = harness_python_sdk.FeatureFlagsApi(harness_python_sdk.ApiClient(configuration))
identifier = 'identifier_example' # str | Unique identifier for the object in the API.
account_identifier = 'account_identifier_example' # str | Account Identifier
org_identifier = 'org_identifier_example' # str | Organization Identifier
project_identifier = 'project_identifier_example' # str | The Project identifier
commit_msg = 'commit_msg_example' # str | Git commit message (optional)

try:
    # Restore a Feature Flag
    api_instance.restore_feature_flag(identifier, account_identifier, org_identifier, project_identifier, commit_msg=commit_msg)
except ApiException as e:
    print("Exception when calling FeatureFlagsApi->restore_feature_flag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Unique identifier for the object in the API. | 
 **account_identifier** | **str**| Account Identifier | 
 **org_identifier** | **str**| Organization Identifier | 
 **project_identifier** | **str**| The Project identifier | 
 **commit_msg** | **str**| Git commit message | [optional] 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

