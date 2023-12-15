# swagger_client.AccountSettingApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account_setting**](AccountSettingApi.md#get_account_setting) | **GET** /ng/api/account-setting | Get the AccountSetting by accountIdentifier
[**list_account_setting**](AccountSettingApi.md#list_account_setting) | **GET** /ng/api/account-setting/list | Get the AccountSetting by accountIdentifier
[**update_account_setting**](AccountSettingApi.md#update_account_setting) | **PUT** /ng/api/account-setting | Updates account settings

# **get_account_setting**
> ResponseDTOAccountSettingResponse get_account_setting(account_identifier, type, org_identifier=org_identifier, project_identifier=project_identifier)

Get the AccountSetting by accountIdentifier

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
api_instance = swagger_client.AccountSettingApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
type = 'type_example' # str | 
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Get the AccountSetting by accountIdentifier
    api_response = api_instance.get_account_setting(account_identifier, type, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountSettingApi->get_account_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **type** | **str**|  | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOAccountSettingResponse**](ResponseDTOAccountSettingResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, text/yaml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_account_setting**
> ResponseDTOListAccountSettings list_account_setting(account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, type=type)

Get the AccountSetting by accountIdentifier

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
api_instance = swagger_client.AccountSettingApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
type = 'type_example' # str |  (optional)

try:
    # Get the AccountSetting by accountIdentifier
    api_response = api_instance.list_account_setting(account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountSettingApi->list_account_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **type** | **str**|  | [optional] 

### Return type

[**ResponseDTOListAccountSettings**](ResponseDTOListAccountSettings.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, text/yaml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_account_setting**
> ResponseDTOAccountSettingResponse update_account_setting(body, account_identifier)

Updates account settings

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
api_instance = swagger_client.AccountSettingApi(swagger_client.ApiClient(configuration))
body = swagger_client.AccountSettings() # AccountSettings | Details of the AccountSetting to create
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Updates account settings
    api_response = api_instance.update_account_setting(body, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountSettingApi->update_account_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccountSettings**](AccountSettings.md)| Details of the AccountSetting to create | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**ResponseDTOAccountSettingResponse**](ResponseDTOAccountSettingResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, text/yaml, text/html, text/plain
 - **Accept**: application/json, application/yaml, text/yaml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

