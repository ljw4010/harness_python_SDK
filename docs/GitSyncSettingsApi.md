# swagger_client.GitSyncSettingsApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_git_sync_setting**](GitSyncSettingsApi.md#create_git_sync_setting) | **POST** /ng/api/git-sync-settings | Creates Git Sync Setting in a scope
[**get_git_sync_settings**](GitSyncSettingsApi.md#get_git_sync_settings) | **GET** /ng/api/git-sync-settings | Get Git Sync Setting for the given scope
[**update_git_sync_setting**](GitSyncSettingsApi.md#update_git_sync_setting) | **PUT** /ng/api/git-sync-settings | This updates the existing Git Sync settings within the scope. Only changing Connectivity Mode is allowed

# **create_git_sync_setting**
> ResponseDTOGitSyncSettings create_git_sync_setting(body, account_identifier)

Creates Git Sync Setting in a scope

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
api_instance = swagger_client.GitSyncSettingsApi(swagger_client.ApiClient(configuration))
body = swagger_client.GitSyncSettings() # GitSyncSettings | This contains details of Git Sync settings like - (scope, executionOnDelegate)
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Creates Git Sync Setting in a scope
    api_response = api_instance.create_git_sync_setting(body, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GitSyncSettingsApi->create_git_sync_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GitSyncSettings**](GitSyncSettings.md)| This contains details of Git Sync settings like - (scope, executionOnDelegate) | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**ResponseDTOGitSyncSettings**](ResponseDTOGitSyncSettings.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, text/yaml, text/html
 - **Accept**: application/json, application/yaml, text/yaml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_git_sync_settings**
> ResponseDTOGitSyncSettings get_git_sync_settings(account_identifier, project_identifier=project_identifier, org_identifier=org_identifier)

Get Git Sync Setting for the given scope

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
api_instance = swagger_client.GitSyncSettingsApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)

try:
    # Get Git Sync Setting for the given scope
    api_response = api_instance.get_git_sync_settings(account_identifier, project_identifier=project_identifier, org_identifier=org_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GitSyncSettingsApi->get_git_sync_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOGitSyncSettings**](ResponseDTOGitSyncSettings.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, text/yaml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_git_sync_setting**
> ResponseDTOGitSyncSettings update_git_sync_setting(body, account_identifier)

This updates the existing Git Sync settings within the scope. Only changing Connectivity Mode is allowed

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
api_instance = swagger_client.GitSyncSettingsApi(swagger_client.ApiClient(configuration))
body = swagger_client.GitSyncSettings() # GitSyncSettings | This contains details of Git Sync Settings
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # This updates the existing Git Sync settings within the scope. Only changing Connectivity Mode is allowed
    api_response = api_instance.update_git_sync_setting(body, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GitSyncSettingsApi->update_git_sync_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GitSyncSettings**](GitSyncSettings.md)| This contains details of Git Sync Settings | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**ResponseDTOGitSyncSettings**](ResponseDTOGitSyncSettings.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, text/yaml, text/html
 - **Accept**: application/json, application/yaml, text/yaml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

