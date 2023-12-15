# harness_python_sdk.DowntimeApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_downtime_data**](DowntimeApi.md#delete_downtime_data) | **DELETE** /cv/api/account/{accountIdentifier}/org/{orgIdentifier}/project/{projectIdentifier}/downtime/identifier/{identifier} | 
[**get_associated_monitored_services**](DowntimeApi.md#get_associated_monitored_services) | **GET** /cv/api/account/{accountIdentifier}/org/{orgIdentifier}/project/{projectIdentifier}/downtime/monitored-services/{identifier} | 
[**get_downtime**](DowntimeApi.md#get_downtime) | **GET** /cv/api/account/{accountIdentifier}/org/{orgIdentifier}/project/{projectIdentifier}/downtime/identifier/{identifier} | 
[**get_downtime_associated_monitored_services**](DowntimeApi.md#get_downtime_associated_monitored_services) | **GET** /cv/api/account/{accountIdentifier}/org/{orgIdentifier}/project/{projectIdentifier}/downtime/monitored-services | 
[**get_history**](DowntimeApi.md#get_history) | **GET** /cv/api/account/{accountIdentifier}/org/{orgIdentifier}/project/{projectIdentifier}/downtime/history | 
[**list_downtimes**](DowntimeApi.md#list_downtimes) | **GET** /cv/api/account/{accountIdentifier}/org/{orgIdentifier}/project/{projectIdentifier}/downtime/list | 
[**save_downtime**](DowntimeApi.md#save_downtime) | **POST** /cv/api/account/{accountIdentifier}/org/{orgIdentifier}/project/{projectIdentifier}/downtime | 
[**update_downtime_data**](DowntimeApi.md#update_downtime_data) | **PUT** /cv/api/account/{accountIdentifier}/org/{orgIdentifier}/project/{projectIdentifier}/downtime/identifier/{identifier} | 
[**update_downtime_enabled**](DowntimeApi.md#update_downtime_enabled) | **PUT** /cv/api/account/{accountIdentifier}/org/{orgIdentifier}/project/{projectIdentifier}/downtime/flag/{identifier} | 

# **delete_downtime_data**
> delete_downtime_data(identifier, account_identifier, org_identifier, project_identifier)



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
api_instance = harness_python_sdk.DowntimeApi(harness_python_sdk.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier for the Entity.
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.

try:
    api_instance.delete_downtime_data(identifier, account_identifier, org_identifier, project_identifier)
except ApiException as e:
    print("Exception when calling DowntimeApi->delete_downtime_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier for the Entity. | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_associated_monitored_services**
> get_associated_monitored_services(identifier, account_identifier, org_identifier, project_identifier)



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
api_instance = harness_python_sdk.DowntimeApi(harness_python_sdk.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier for the Entity.
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.

try:
    api_instance.get_associated_monitored_services(identifier, account_identifier, org_identifier, project_identifier)
except ApiException as e:
    print("Exception when calling DowntimeApi->get_associated_monitored_services: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier for the Entity. | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_downtime**
> get_downtime(identifier, account_identifier, org_identifier, project_identifier)



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
api_instance = harness_python_sdk.DowntimeApi(harness_python_sdk.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier for the Entity.
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.

try:
    api_instance.get_downtime(identifier, account_identifier, org_identifier, project_identifier)
except ApiException as e:
    print("Exception when calling DowntimeApi->get_downtime: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier for the Entity. | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_downtime_associated_monitored_services**
> get_downtime_associated_monitored_services(account_identifier, org_identifier, project_identifier, page_number=page_number, page_size=page_size)



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
api_instance = harness_python_sdk.DowntimeApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
page_number = 0 # int | Page Index of the results to fetch.Default Value: 0 (optional) (default to 0)
page_size = 10 # int | Results per page (optional) (default to 10)

try:
    api_instance.get_downtime_associated_monitored_services(account_identifier, org_identifier, project_identifier, page_number=page_number, page_size=page_size)
except ApiException as e:
    print("Exception when calling DowntimeApi->get_downtime_associated_monitored_services: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **page_number** | **int**| Page Index of the results to fetch.Default Value: 0 | [optional] [default to 0]
 **page_size** | **int**| Results per page | [optional] [default to 10]

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_history**
> get_history(account_identifier, org_identifier, project_identifier, page_number=page_number, page_size=page_size, monitored_service_identifier=monitored_service_identifier, filter=filter)



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
api_instance = harness_python_sdk.DowntimeApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
page_number = 0 # int | Page Index of the results to fetch.Default Value: 0 (optional) (default to 0)
page_size = 10 # int | Results per page (optional) (default to 10)
monitored_service_identifier = 'monitored_service_identifier_example' # str | For filtering on the basis of monitored services' identifiers (optional)
filter = 'filter_example' # str | For filtering on the basis of name (optional)

try:
    api_instance.get_history(account_identifier, org_identifier, project_identifier, page_number=page_number, page_size=page_size, monitored_service_identifier=monitored_service_identifier, filter=filter)
except ApiException as e:
    print("Exception when calling DowntimeApi->get_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **page_number** | **int**| Page Index of the results to fetch.Default Value: 0 | [optional] [default to 0]
 **page_size** | **int**| Results per page | [optional] [default to 10]
 **monitored_service_identifier** | **str**| For filtering on the basis of monitored services&#x27; identifiers | [optional] 
 **filter** | **str**| For filtering on the basis of name | [optional] 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_downtimes**
> list_downtimes(account_identifier, org_identifier, project_identifier, page_number=page_number, page_size=page_size, monitored_service_identifier=monitored_service_identifier, filter=filter)



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
api_instance = harness_python_sdk.DowntimeApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
page_number = 0 # int | Page Index of the results to fetch.Default Value: 0 (optional) (default to 0)
page_size = 10 # int | Results per page (optional) (default to 10)
monitored_service_identifier = 'monitored_service_identifier_example' # str | For filtering on the basis of monitored services' identifiers (optional)
filter = 'filter_example' # str | For filtering on the basis of name (optional)

try:
    api_instance.list_downtimes(account_identifier, org_identifier, project_identifier, page_number=page_number, page_size=page_size, monitored_service_identifier=monitored_service_identifier, filter=filter)
except ApiException as e:
    print("Exception when calling DowntimeApi->list_downtimes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **page_number** | **int**| Page Index of the results to fetch.Default Value: 0 | [optional] [default to 0]
 **page_size** | **int**| Results per page | [optional] [default to 10]
 **monitored_service_identifier** | **str**| For filtering on the basis of monitored services&#x27; identifiers | [optional] 
 **filter** | **str**| For filtering on the basis of name | [optional] 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_downtime**
> save_downtime(body, account_identifier, org_identifier, project_identifier)



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
api_instance = harness_python_sdk.DowntimeApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.Downtime() # Downtime | Details of the Downtime to be saved
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.

try:
    api_instance.save_downtime(body, account_identifier, org_identifier, project_identifier)
except ApiException as e:
    print("Exception when calling DowntimeApi->save_downtime: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Downtime**](Downtime.md)| Details of the Downtime to be saved | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_downtime_data**
> update_downtime_data(body, identifier, account_identifier, org_identifier, project_identifier)



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
api_instance = harness_python_sdk.DowntimeApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.Downtime() # Downtime | Details of the Downtime to be updated
identifier = 'identifier_example' # str | Identifier for the Entity.
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.

try:
    api_instance.update_downtime_data(body, identifier, account_identifier, org_identifier, project_identifier)
except ApiException as e:
    print("Exception when calling DowntimeApi->update_downtime_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Downtime**](Downtime.md)| Details of the Downtime to be updated | 
 **identifier** | **str**| Identifier for the Entity. | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_downtime_enabled**
> update_downtime_enabled(identifier, account_identifier, org_identifier, project_identifier, enable)



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
api_instance = harness_python_sdk.DowntimeApi(harness_python_sdk.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier for the Entity.
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
enable = true # bool | 

try:
    api_instance.update_downtime_enabled(identifier, account_identifier, org_identifier, project_identifier, enable)
except ApiException as e:
    print("Exception when calling DowntimeApi->update_downtime_enabled: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier for the Entity. | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **enable** | **bool**|  | 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

