# swagger_client.GitSyncApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_git_sync_config**](GitSyncApi.md#create_git_sync_config) | **POST** /ng/api/git-sync | Creates Git Sync Config in given scope
[**get_git_sync_config_list**](GitSyncApi.md#get_git_sync_config_list) | **GET** /ng/api/git-sync | Lists Git Sync Config for the given scope
[**is_git_sync_enabled**](GitSyncApi.md#is_git_sync_enabled) | **GET** /ng/api/git-sync/git-sync-enabled | Check whether Git Sync is enabled for given scope or not
[**update_default_folder**](GitSyncApi.md#update_default_folder) | **PUT** /ng/api/git-sync/{identifier}/folder/{folderIdentifier}/default | Update existing Git Sync Config default root folder by Identifier
[**update_git_sync_config**](GitSyncApi.md#update_git_sync_config) | **PUT** /ng/api/git-sync | Update existing Git Sync Config by Identifier

# **create_git_sync_config**
> GitSyncConfig create_git_sync_config(body, account_identifier)

Creates Git Sync Config in given scope

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
api_instance = swagger_client.GitSyncApi(swagger_client.ApiClient(configuration))
body = swagger_client.GitSyncConfig() # GitSyncConfig | Details of Git Sync Config
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Creates Git Sync Config in given scope
    api_response = api_instance.create_git_sync_config(body, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GitSyncApi->create_git_sync_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GitSyncConfig**](GitSyncConfig.md)| Details of Git Sync Config | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**GitSyncConfig**](GitSyncConfig.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, text/yaml, text/html, text/plain
 - **Accept**: application/json, application/yaml, text/yaml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_git_sync_config_list**
> list[GitSyncConfig] get_git_sync_config_list(account_identifier, project_identifier=project_identifier, org_identifier=org_identifier)

Lists Git Sync Config for the given scope

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
api_instance = swagger_client.GitSyncApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)

try:
    # Lists Git Sync Config for the given scope
    api_response = api_instance.get_git_sync_config_list(account_identifier, project_identifier=project_identifier, org_identifier=org_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GitSyncApi->get_git_sync_config_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 

### Return type

[**list[GitSyncConfig]**](GitSyncConfig.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, text/yaml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **is_git_sync_enabled**
> GitEnabled is_git_sync_enabled(account_identifier, project_identifier=project_identifier, org_identifier=org_identifier)

Check whether Git Sync is enabled for given scope or not

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
api_instance = swagger_client.GitSyncApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)

try:
    # Check whether Git Sync is enabled for given scope or not
    api_response = api_instance.is_git_sync_enabled(account_identifier, project_identifier=project_identifier, org_identifier=org_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GitSyncApi->is_git_sync_enabled: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 

### Return type

[**GitEnabled**](GitEnabled.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, text/yaml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_default_folder**
> GitSyncConfig update_default_folder(account_id, identifier, folder_identifier, project_id=project_id, organization_id=organization_id)

Update existing Git Sync Config default root folder by Identifier

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
api_instance = swagger_client.GitSyncApi(swagger_client.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier for the Entity.
identifier = 'identifier_example' # str | Git Sync Config Id.
folder_identifier = 'folder_identifier_example' # str | Folder Id
project_id = 'project_id_example' # str | Project Identifier for the Entity. (optional)
organization_id = 'organization_id_example' # str | Organization Identifier for the Entity. (optional)

try:
    # Update existing Git Sync Config default root folder by Identifier
    api_response = api_instance.update_default_folder(account_id, identifier, folder_identifier, project_id=project_id, organization_id=organization_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GitSyncApi->update_default_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier for the Entity. | 
 **identifier** | **str**| Git Sync Config Id. | 
 **folder_identifier** | **str**| Folder Id | 
 **project_id** | **str**| Project Identifier for the Entity. | [optional] 
 **organization_id** | **str**| Organization Identifier for the Entity. | [optional] 

### Return type

[**GitSyncConfig**](GitSyncConfig.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, text/yaml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_git_sync_config**
> GitSyncConfig update_git_sync_config(body, account_identifier)

Update existing Git Sync Config by Identifier

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
api_instance = swagger_client.GitSyncApi(swagger_client.ApiClient(configuration))
body = swagger_client.GitSyncConfig() # GitSyncConfig | Details of Git Sync Config
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Update existing Git Sync Config by Identifier
    api_response = api_instance.update_git_sync_config(body, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GitSyncApi->update_git_sync_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GitSyncConfig**](GitSyncConfig.md)| Details of Git Sync Config | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**GitSyncConfig**](GitSyncConfig.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, text/yaml, text/html, text/plain
 - **Accept**: application/json, application/yaml, text/yaml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

