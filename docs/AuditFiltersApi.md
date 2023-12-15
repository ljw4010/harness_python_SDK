# swagger_client.AuditFiltersApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_audit_filter**](AuditFiltersApi.md#delete_audit_filter) | **DELETE** /audit/api/auditFilters/{identifier} | Delete a Filter of type Audit by identifier
[**get_audit_filter**](AuditFiltersApi.md#get_audit_filter) | **GET** /audit/api/auditFilters/{identifier} | Gets a Filter of type Audit by identifier
[**get_audit_filter_list**](AuditFiltersApi.md#get_audit_filter_list) | **GET** /audit/api/auditFilters | Get the list of Filters of type Audit satisfying the criteria (if any) in the request
[**post_audit_filter**](AuditFiltersApi.md#post_audit_filter) | **POST** /audit/api/auditFilters | Creates a Filter
[**update_audit_filter**](AuditFiltersApi.md#update_audit_filter) | **PUT** /audit/api/auditFilters | Updates the Filter of type Audit

# **delete_audit_filter**
> ResponseDTOBoolean delete_audit_filter(account_identifier, identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Delete a Filter of type Audit by identifier

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
api_instance = swagger_client.AuditFiltersApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
identifier = 'identifier_example' # str | Filter Identifier
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Delete a Filter of type Audit by identifier
    api_response = api_instance.delete_audit_filter(account_identifier, identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditFiltersApi->delete_audit_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **identifier** | **str**| Filter Identifier | 
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

# **get_audit_filter**
> ResponseDTOFilter get_audit_filter(account_identifier, identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Gets a Filter of type Audit by identifier

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
api_instance = swagger_client.AuditFiltersApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
identifier = 'identifier_example' # str | Filter Identifier
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Gets a Filter of type Audit by identifier
    api_response = api_instance.get_audit_filter(account_identifier, identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditFiltersApi->get_audit_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **identifier** | **str**| Filter Identifier | 
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

# **get_audit_filter_list**
> ResponseDTOPageResponseFilter get_audit_filter_list(account_identifier, page_index=page_index, page_size=page_size, org_identifier=org_identifier, project_identifier=project_identifier)

Get the list of Filters of type Audit satisfying the criteria (if any) in the request

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
api_instance = swagger_client.AuditFiltersApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
page_index = 0 # int | Page number of navigation. If left empty, default value of 0 is assumed (optional) (default to 0)
page_size = 100 # int | Number of entries per page. If left empty, default value of 100 is assumed (optional) (default to 100)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Get the list of Filters of type Audit satisfying the criteria (if any) in the request
    api_response = api_instance.get_audit_filter_list(account_identifier, page_index=page_index, page_size=page_size, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditFiltersApi->get_audit_filter_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **page_index** | **int**| Page number of navigation. If left empty, default value of 0 is assumed | [optional] [default to 0]
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

# **post_audit_filter**
> ResponseDTOFilter post_audit_filter(body, account_identifier)

Creates a Filter

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
api_instance = swagger_client.AuditFiltersApi(swagger_client.ApiClient(configuration))
body = swagger_client.Filter() # Filter | Details of the Filter to create
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Creates a Filter
    api_response = api_instance.post_audit_filter(body, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditFiltersApi->post_audit_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Filter**](Filter.md)| Details of the Filter to create | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**ResponseDTOFilter**](ResponseDTOFilter.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, text/yaml, text/html, text/plain
 - **Accept**: application/json, application/yaml, text/yaml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_audit_filter**
> ResponseDTOFilter update_audit_filter(body, account_identifier)

Updates the Filter of type Audit

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
api_instance = swagger_client.AuditFiltersApi(swagger_client.ApiClient(configuration))
body = swagger_client.Filter() # Filter | This is the updated Filter. This should have all the fields not just the updated ones
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Updates the Filter of type Audit
    api_response = api_instance.update_audit_filter(body, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditFiltersApi->update_audit_filter: %s\n" % e)
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

