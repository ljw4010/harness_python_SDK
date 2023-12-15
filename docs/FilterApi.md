# harness_python_sdk.FilterApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ccmdelete_filter**](FilterApi.md#ccmdelete_filter) | **DELETE** /ccm/api/filters/{identifier} | Delete a Filter
[**ccmget_connector_list_v2**](FilterApi.md#ccmget_connector_list_v2) | **GET** /ccm/api/filters | List Filters
[**ccmget_filter**](FilterApi.md#ccmget_filter) | **GET** /ccm/api/filters/{identifier} | Return Filter Details
[**ccmpost_filter**](FilterApi.md#ccmpost_filter) | **POST** /ccm/api/filters | Create a Filter
[**ccmupdate_filter**](FilterApi.md#ccmupdate_filter) | **PUT** /ccm/api/filters | Update a Filter
[**delete_filter**](FilterApi.md#delete_filter) | **DELETE** /ng/api/filters/{identifier} | Delete a Filter
[**get_connector_list_v21**](FilterApi.md#get_connector_list_v21) | **GET** /ng/api/filters | List Filters
[**get_filter**](FilterApi.md#get_filter) | **GET** /ng/api/filters/{identifier} | Return Filter Details
[**pipelinedelete_filter**](FilterApi.md#pipelinedelete_filter) | **DELETE** /pipeline/api/filters/{identifier} | Delete a Filter
[**pipelineget_connector_list_v2**](FilterApi.md#pipelineget_connector_list_v2) | **GET** /pipeline/api/filters | List Filters
[**pipelineget_filter**](FilterApi.md#pipelineget_filter) | **GET** /pipeline/api/filters/{identifier} | Return Filter Details
[**pipelinepost_filter**](FilterApi.md#pipelinepost_filter) | **POST** /pipeline/api/filters | Create a Filter
[**pipelineupdate_filter**](FilterApi.md#pipelineupdate_filter) | **PUT** /pipeline/api/filters | Update a Filter
[**post_filter**](FilterApi.md#post_filter) | **POST** /ng/api/filters | Create a Filter
[**templatedelete_filter**](FilterApi.md#templatedelete_filter) | **DELETE** /template/api/filters/{identifier} | Delete a Filter
[**templateget_connector_list_v2**](FilterApi.md#templateget_connector_list_v2) | **GET** /template/api/filters | List Filters
[**templateget_filter**](FilterApi.md#templateget_filter) | **GET** /template/api/filters/{identifier} | Return Filter Details
[**templatepost_filter**](FilterApi.md#templatepost_filter) | **POST** /template/api/filters | Create a Filter
[**templateupdate_filter**](FilterApi.md#templateupdate_filter) | **PUT** /template/api/filters | Update a Filter
[**update_filter**](FilterApi.md#update_filter) | **PUT** /ng/api/filters | Update a Filter

# **ccmdelete_filter**
> ResponseDTOBoolean ccmdelete_filter(account_identifier, identifier, type, org_identifier=org_identifier, project_identifier=project_identifier)

Delete a Filter

Deletes a filter for the given ID.

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
api_instance = harness_python_sdk.FilterApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
identifier = 'identifier_example' # str | Filter Identifier
type = 'type_example' # str | Type of Filter
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Delete a Filter
    api_response = api_instance.ccmdelete_filter(account_identifier, identifier, type, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilterApi->ccmdelete_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **identifier** | **str**| Filter Identifier | 
 **type** | **str**| Type of Filter | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOBoolean**](ResponseDTOBoolean.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, text/yaml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ccmget_connector_list_v2**
> ResponseDTOPageResponseFilter ccmget_connector_list_v2(account_identifier, type, page_index=page_index, page_size=page_size, org_identifier=org_identifier, project_identifier=project_identifier)

List Filters

Lists Filters for the given criteria.

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
api_instance = harness_python_sdk.FilterApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
type = 'type_example' # str | Type of Filter
page_index = 0 # int | Page number of navigation. If left empty, default value of 0 is assumed. (optional) (default to 0)
page_size = 100 # int | Number of entries per page. If left empty, default value of 100 is assumed (optional) (default to 100)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # List Filters
    api_response = api_instance.ccmget_connector_list_v2(account_identifier, type, page_index=page_index, page_size=page_size, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilterApi->ccmget_connector_list_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **type** | **str**| Type of Filter | 
 **page_index** | **int**| Page number of navigation. If left empty, default value of 0 is assumed. | [optional] [default to 0]
 **page_size** | **int**| Number of entries per page. If left empty, default value of 100 is assumed | [optional] [default to 100]
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOPageResponseFilter**](ResponseDTOPageResponseFilter.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, text/yaml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ccmget_filter**
> ResponseDTOFilter ccmget_filter(account_identifier, identifier, type, org_identifier=org_identifier, project_identifier=project_identifier)

Return Filter Details

Returns the settings of a filter for the given ID.

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
api_instance = harness_python_sdk.FilterApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
identifier = 'identifier_example' # str | Filter Identifier
type = 'type_example' # str | Type of Filter
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Return Filter Details
    api_response = api_instance.ccmget_filter(account_identifier, identifier, type, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilterApi->ccmget_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **identifier** | **str**| Filter Identifier | 
 **type** | **str**| Type of Filter | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOFilter**](ResponseDTOFilter.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, text/yaml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ccmpost_filter**
> ResponseDTOFilter ccmpost_filter(body, account_identifier)

Create a Filter

Creates a Filter.

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
api_instance = harness_python_sdk.FilterApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.Filter() # Filter | Details of the Connector to create
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Create a Filter
    api_response = api_instance.ccmpost_filter(body, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilterApi->ccmpost_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Filter**](Filter.md)| Details of the Connector to create | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**ResponseDTOFilter**](ResponseDTOFilter.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, text/yaml, text/html, text/plain
 - **Accept**: application/json, application/yaml, text/yaml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ccmupdate_filter**
> ResponseDTOFilter ccmupdate_filter(body, account_identifier)

Update a Filter

Updates the filter for the given ID.

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
api_instance = harness_python_sdk.FilterApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.Filter() # Filter | This is the updated Filter. This should have all the fields not just the updated ones
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Update a Filter
    api_response = api_instance.ccmupdate_filter(body, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilterApi->ccmupdate_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Filter**](Filter.md)| This is the updated Filter. This should have all the fields not just the updated ones | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**ResponseDTOFilter**](ResponseDTOFilter.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, text/yaml, text/html, text/plain
 - **Accept**: application/json, application/yaml, text/yaml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_filter**
> ResponseDTOBoolean delete_filter(account_identifier, identifier, type, org_identifier=org_identifier, project_identifier=project_identifier)

Delete a Filter

Deletes a filter for the given ID.

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
api_instance = harness_python_sdk.FilterApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
identifier = 'identifier_example' # str | Filter Identifier
type = 'type_example' # str | Type of Filter
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Delete a Filter
    api_response = api_instance.delete_filter(account_identifier, identifier, type, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilterApi->delete_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **identifier** | **str**| Filter Identifier | 
 **type** | **str**| Type of Filter | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOBoolean**](ResponseDTOBoolean.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, text/yaml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connector_list_v21**
> ResponseDTOPageResponseFilter get_connector_list_v21(account_identifier, type, page_index=page_index, page_size=page_size, org_identifier=org_identifier, project_identifier=project_identifier)

List Filters

Lists Filters for the given criteria.

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
api_instance = harness_python_sdk.FilterApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
type = 'type_example' # str | Type of Filter
page_index = 0 # int | Page number of navigation. If left empty, default value of 0 is assumed. (optional) (default to 0)
page_size = 100 # int | Number of entries per page. If left empty, default value of 100 is assumed (optional) (default to 100)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # List Filters
    api_response = api_instance.get_connector_list_v21(account_identifier, type, page_index=page_index, page_size=page_size, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilterApi->get_connector_list_v21: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **type** | **str**| Type of Filter | 
 **page_index** | **int**| Page number of navigation. If left empty, default value of 0 is assumed. | [optional] [default to 0]
 **page_size** | **int**| Number of entries per page. If left empty, default value of 100 is assumed | [optional] [default to 100]
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOPageResponseFilter**](ResponseDTOPageResponseFilter.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, text/yaml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_filter**
> ResponseDTOFilter get_filter(account_identifier, identifier, type, org_identifier=org_identifier, project_identifier=project_identifier)

Return Filter Details

Returns the settings of a filter for the given ID.

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
api_instance = harness_python_sdk.FilterApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
identifier = 'identifier_example' # str | Filter Identifier
type = 'type_example' # str | Type of Filter
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Return Filter Details
    api_response = api_instance.get_filter(account_identifier, identifier, type, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilterApi->get_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **identifier** | **str**| Filter Identifier | 
 **type** | **str**| Type of Filter | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOFilter**](ResponseDTOFilter.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, text/yaml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipelinedelete_filter**
> ResponseDTOBoolean pipelinedelete_filter(account_identifier, identifier, type, org_identifier=org_identifier, project_identifier=project_identifier)

Delete a Filter

Deletes a filter for the given ID.

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
api_instance = harness_python_sdk.FilterApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
identifier = 'identifier_example' # str | Filter Identifier
type = 'type_example' # str | Type of Filter
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Delete a Filter
    api_response = api_instance.pipelinedelete_filter(account_identifier, identifier, type, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilterApi->pipelinedelete_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **identifier** | **str**| Filter Identifier | 
 **type** | **str**| Type of Filter | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOBoolean**](ResponseDTOBoolean.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, text/yaml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipelineget_connector_list_v2**
> ResponseDTOPageResponseFilter pipelineget_connector_list_v2(account_identifier, type, page_index=page_index, page_size=page_size, org_identifier=org_identifier, project_identifier=project_identifier)

List Filters

Lists Filters for the given criteria.

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
api_instance = harness_python_sdk.FilterApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
type = 'type_example' # str | Type of Filter
page_index = 0 # int | Page number of navigation. If left empty, default value of 0 is assumed. (optional) (default to 0)
page_size = 100 # int | Number of entries per page. If left empty, default value of 100 is assumed (optional) (default to 100)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # List Filters
    api_response = api_instance.pipelineget_connector_list_v2(account_identifier, type, page_index=page_index, page_size=page_size, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilterApi->pipelineget_connector_list_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **type** | **str**| Type of Filter | 
 **page_index** | **int**| Page number of navigation. If left empty, default value of 0 is assumed. | [optional] [default to 0]
 **page_size** | **int**| Number of entries per page. If left empty, default value of 100 is assumed | [optional] [default to 100]
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOPageResponseFilter**](ResponseDTOPageResponseFilter.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, text/yaml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipelineget_filter**
> ResponseDTOFilter pipelineget_filter(account_identifier, identifier, type, org_identifier=org_identifier, project_identifier=project_identifier)

Return Filter Details

Returns the settings of a filter for the given ID.

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
api_instance = harness_python_sdk.FilterApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
identifier = 'identifier_example' # str | Filter Identifier
type = 'type_example' # str | Type of Filter
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Return Filter Details
    api_response = api_instance.pipelineget_filter(account_identifier, identifier, type, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilterApi->pipelineget_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **identifier** | **str**| Filter Identifier | 
 **type** | **str**| Type of Filter | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOFilter**](ResponseDTOFilter.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, text/yaml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipelinepost_filter**
> ResponseDTOFilter pipelinepost_filter(body, account_identifier)

Create a Filter

Creates a Filter.

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
api_instance = harness_python_sdk.FilterApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.Filter() # Filter | Details of the Connector to create
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Create a Filter
    api_response = api_instance.pipelinepost_filter(body, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilterApi->pipelinepost_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Filter**](Filter.md)| Details of the Connector to create | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**ResponseDTOFilter**](ResponseDTOFilter.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, text/yaml, text/html, text/plain
 - **Accept**: application/json, application/yaml, text/yaml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipelineupdate_filter**
> ResponseDTOFilter pipelineupdate_filter(body, account_identifier)

Update a Filter

Updates the filter for the given ID.

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
api_instance = harness_python_sdk.FilterApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.Filter() # Filter | This is the updated Filter. This should have all the fields not just the updated ones
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Update a Filter
    api_response = api_instance.pipelineupdate_filter(body, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilterApi->pipelineupdate_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Filter**](Filter.md)| This is the updated Filter. This should have all the fields not just the updated ones | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**ResponseDTOFilter**](ResponseDTOFilter.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, text/yaml, text/html, text/plain
 - **Accept**: application/json, application/yaml, text/yaml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_filter**
> ResponseDTOFilter post_filter(body, account_identifier)

Create a Filter

Creates a Filter.

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
api_instance = harness_python_sdk.FilterApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.Filter() # Filter | Details of the Connector to create
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Create a Filter
    api_response = api_instance.post_filter(body, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilterApi->post_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Filter**](Filter.md)| Details of the Connector to create | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**ResponseDTOFilter**](ResponseDTOFilter.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, text/yaml, text/html, text/plain
 - **Accept**: application/json, application/yaml, text/yaml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templatedelete_filter**
> ResponseDTOBoolean templatedelete_filter(account_identifier, identifier, type, org_identifier=org_identifier, project_identifier=project_identifier)

Delete a Filter

Deletes a filter for the given ID.

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
api_instance = harness_python_sdk.FilterApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
identifier = 'identifier_example' # str | Filter Identifier
type = 'type_example' # str | Type of Filter
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Delete a Filter
    api_response = api_instance.templatedelete_filter(account_identifier, identifier, type, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilterApi->templatedelete_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **identifier** | **str**| Filter Identifier | 
 **type** | **str**| Type of Filter | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOBoolean**](ResponseDTOBoolean.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, text/yaml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templateget_connector_list_v2**
> ResponseDTOPageResponseFilter templateget_connector_list_v2(account_identifier, type, page_index=page_index, page_size=page_size, org_identifier=org_identifier, project_identifier=project_identifier)

List Filters

Lists Filters for the given criteria.

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
api_instance = harness_python_sdk.FilterApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
type = 'type_example' # str | Type of Filter
page_index = 0 # int | Page number of navigation. If left empty, default value of 0 is assumed. (optional) (default to 0)
page_size = 100 # int | Number of entries per page. If left empty, default value of 100 is assumed (optional) (default to 100)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # List Filters
    api_response = api_instance.templateget_connector_list_v2(account_identifier, type, page_index=page_index, page_size=page_size, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilterApi->templateget_connector_list_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **type** | **str**| Type of Filter | 
 **page_index** | **int**| Page number of navigation. If left empty, default value of 0 is assumed. | [optional] [default to 0]
 **page_size** | **int**| Number of entries per page. If left empty, default value of 100 is assumed | [optional] [default to 100]
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOPageResponseFilter**](ResponseDTOPageResponseFilter.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, text/yaml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templateget_filter**
> ResponseDTOFilter templateget_filter(account_identifier, identifier, type, org_identifier=org_identifier, project_identifier=project_identifier)

Return Filter Details

Returns the settings of a filter for the given ID.

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
api_instance = harness_python_sdk.FilterApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
identifier = 'identifier_example' # str | Filter Identifier
type = 'type_example' # str | Type of Filter
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Return Filter Details
    api_response = api_instance.templateget_filter(account_identifier, identifier, type, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilterApi->templateget_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **identifier** | **str**| Filter Identifier | 
 **type** | **str**| Type of Filter | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOFilter**](ResponseDTOFilter.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, text/yaml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templatepost_filter**
> ResponseDTOFilter templatepost_filter(body, account_identifier)

Create a Filter

Creates a Filter.

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
api_instance = harness_python_sdk.FilterApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.Filter() # Filter | Details of the Connector to create
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Create a Filter
    api_response = api_instance.templatepost_filter(body, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilterApi->templatepost_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Filter**](Filter.md)| Details of the Connector to create | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**ResponseDTOFilter**](ResponseDTOFilter.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, text/yaml, text/html, text/plain
 - **Accept**: application/json, application/yaml, text/yaml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templateupdate_filter**
> ResponseDTOFilter templateupdate_filter(body, account_identifier)

Update a Filter

Updates the filter for the given ID.

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
api_instance = harness_python_sdk.FilterApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.Filter() # Filter | This is the updated Filter. This should have all the fields not just the updated ones
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Update a Filter
    api_response = api_instance.templateupdate_filter(body, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilterApi->templateupdate_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Filter**](Filter.md)| This is the updated Filter. This should have all the fields not just the updated ones | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**ResponseDTOFilter**](ResponseDTOFilter.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, text/yaml, text/html, text/plain
 - **Accept**: application/json, application/yaml, text/yaml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_filter**
> ResponseDTOFilter update_filter(body, account_identifier)

Update a Filter

Updates the filter for the given ID.

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
api_instance = harness_python_sdk.FilterApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.Filter() # Filter | This is the updated Filter. This should have all the fields not just the updated ones
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Update a Filter
    api_response = api_instance.update_filter(body, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilterApi->update_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Filter**](Filter.md)| This is the updated Filter. This should have all the fields not just the updated ones | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**ResponseDTOFilter**](ResponseDTOFilter.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, text/yaml, text/html, text/plain
 - **Accept**: application/json, application/yaml, text/yaml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

