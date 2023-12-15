# harness_python_sdk.SrmNotificationApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_notification_rule_data**](SrmNotificationApi.md#delete_notification_rule_data) | **DELETE** /cv/api/notification-rule/{identifier} | 
[**get_notification_rule_data**](SrmNotificationApi.md#get_notification_rule_data) | **GET** /cv/api/notification-rule/{identifier} | 
[**get_notification_rule_data1**](SrmNotificationApi.md#get_notification_rule_data1) | **GET** /cv/api/notification-rule | 
[**save_notification_rule_data**](SrmNotificationApi.md#save_notification_rule_data) | **POST** /cv/api/notification-rule | 
[**update_notification_rule_data**](SrmNotificationApi.md#update_notification_rule_data) | **PUT** /cv/api/notification-rule/{identifier} | 

# **delete_notification_rule_data**
> delete_notification_rule_data(account_id, identifier, org_identifier=org_identifier, project_identifier=project_identifier)



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
api_instance = harness_python_sdk.SrmNotificationApi(harness_python_sdk.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier for the Entity.
identifier = 'identifier_example' # str | 
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    api_instance.delete_notification_rule_data(account_id, identifier, org_identifier=org_identifier, project_identifier=project_identifier)
except ApiException as e:
    print("Exception when calling SrmNotificationApi->delete_notification_rule_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier for the Entity. | 
 **identifier** | **str**|  | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notification_rule_data**
> get_notification_rule_data(account_id, identifier, org_identifier=org_identifier, project_identifier=project_identifier)



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
api_instance = harness_python_sdk.SrmNotificationApi(harness_python_sdk.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier for the Entity.
identifier = 'identifier_example' # str | 
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    api_instance.get_notification_rule_data(account_id, identifier, org_identifier=org_identifier, project_identifier=project_identifier)
except ApiException as e:
    print("Exception when calling SrmNotificationApi->get_notification_rule_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier for the Entity. | 
 **identifier** | **str**|  | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notification_rule_data1**
> get_notification_rule_data1(account_id, page_number, page_size, org_identifier=org_identifier, project_identifier=project_identifier, notification_rule_identifiers=notification_rule_identifiers)



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
api_instance = harness_python_sdk.SrmNotificationApi(harness_python_sdk.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier for the Entity.
page_number = 56 # int | 
page_size = 56 # int | 
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
notification_rule_identifiers = ['notification_rule_identifiers_example'] # list[str] |  (optional)

try:
    api_instance.get_notification_rule_data1(account_id, page_number, page_size, org_identifier=org_identifier, project_identifier=project_identifier, notification_rule_identifiers=notification_rule_identifiers)
except ApiException as e:
    print("Exception when calling SrmNotificationApi->get_notification_rule_data1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier for the Entity. | 
 **page_number** | **int**|  | 
 **page_size** | **int**|  | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **notification_rule_identifiers** | [**list[str]**](str.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_notification_rule_data**
> save_notification_rule_data(account_id, body=body)



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
api_instance = harness_python_sdk.SrmNotificationApi(harness_python_sdk.ApiClient(configuration))
account_id = 'account_id_example' # str | 
body = harness_python_sdk.NotificationRule() # NotificationRule |  (optional)

try:
    api_instance.save_notification_rule_data(account_id, body=body)
except ApiException as e:
    print("Exception when calling SrmNotificationApi->save_notification_rule_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **body** | [**NotificationRule**](NotificationRule.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_notification_rule_data**
> update_notification_rule_data(account_id, identifier, body=body, org_identifier=org_identifier, project_identifier=project_identifier)



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
api_instance = harness_python_sdk.SrmNotificationApi(harness_python_sdk.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier for the Entity.
identifier = 'identifier_example' # str | 
body = harness_python_sdk.NotificationRule() # NotificationRule |  (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    api_instance.update_notification_rule_data(account_id, identifier, body=body, org_identifier=org_identifier, project_identifier=project_identifier)
except ApiException as e:
    print("Exception when calling SrmNotificationApi->update_notification_rule_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier for the Entity. | 
 **identifier** | **str**|  | 
 **body** | [**NotificationRule**](NotificationRule.md)|  | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

