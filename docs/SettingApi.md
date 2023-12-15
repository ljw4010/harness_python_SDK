# swagger_client.SettingApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_setting_value**](SettingApi.md#get_setting_value) | **GET** /ng/api/settings/{identifier} | Get a setting value by identifier
[**get_settings_list**](SettingApi.md#get_settings_list) | **GET** /ng/api/settings | Get list of settings under the specified category
[**update_setting_value**](SettingApi.md#update_setting_value) | **PUT** /ng/api/settings | Update settings

# **get_setting_value**
> ResponseDTOSettingValueResponseDTO get_setting_value(identifier, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Get a setting value by identifier

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
api_instance = swagger_client.SettingApi(swagger_client.ApiClient(configuration))
identifier = 'identifier_example' # str | This is the Identifier of the Entity
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Get a setting value by identifier
    api_response = api_instance.get_setting_value(identifier, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingApi->get_setting_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| This is the Identifier of the Entity | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOSettingValueResponseDTO**](ResponseDTOSettingValueResponseDTO.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_settings_list**
> ResponseDTOListSettingResponseDTO get_settings_list(account_identifier, category, org_identifier=org_identifier, project_identifier=project_identifier, group=group, include_parent_scopes=include_parent_scopes)

Get list of settings under the specified category

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
api_instance = swagger_client.SettingApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
category = 'category_example' # str | Category of the Setting.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
group = 'group_example' # str | Group Id of the setting (optional)
include_parent_scopes = true # bool | Flag to include the settings which only exist at the parent scopes (optional)

try:
    # Get list of settings under the specified category
    api_response = api_instance.get_settings_list(account_identifier, category, org_identifier=org_identifier, project_identifier=project_identifier, group=group, include_parent_scopes=include_parent_scopes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingApi->get_settings_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **category** | **str**| Category of the Setting. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **group** | **str**| Group Id of the setting | [optional] 
 **include_parent_scopes** | **bool**| Flag to include the settings which only exist at the parent scopes | [optional] 

### Return type

[**ResponseDTOListSettingResponseDTO**](ResponseDTOListSettingResponseDTO.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_setting_value**
> ResponseDTOListSettingUpdateResponseDTO update_setting_value(account_identifier, body=body, org_identifier=org_identifier, project_identifier=project_identifier)

Update settings

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
api_instance = swagger_client.SettingApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
body = [swagger_client.SettingRequestDTO()] # list[SettingRequestDTO] | List of update requests for settings (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Update settings
    api_response = api_instance.update_setting_value(account_identifier, body=body, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingApi->update_setting_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **body** | [**list[SettingRequestDTO]**](SettingRequestDTO.md)| List of update requests for settings | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOListSettingUpdateResponseDTO**](ResponseDTOListSettingUpdateResponseDTO.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

