# harness_python_sdk.GitFullSyncApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_git_full_sync_config**](GitFullSyncApi.md#create_git_full_sync_config) | **POST** /ng/api/git-full-sync/config | Create Configuration for Git Full Sync for the provided scope
[**get_git_full_sync_config**](GitFullSyncApi.md#get_git_full_sync_config) | **GET** /ng/api/git-full-sync/config | Fetch Configuration for Git Full Sync for the provided scope
[**list_full_sync_files**](GitFullSyncApi.md#list_full_sync_files) | **POST** /ng/api/git-full-sync/files | List files in full sync along with their status
[**trigger_full_sync**](GitFullSyncApi.md#trigger_full_sync) | **POST** /ng/api/git-full-sync | Trigger Full Sync
[**update_git_full_sync_config**](GitFullSyncApi.md#update_git_full_sync_config) | **PUT** /ng/api/git-full-sync/config | Update Configuration for Git Full Sync for the provided scope

# **create_git_full_sync_config**
> ResponseDTOGitFullSyncConfig create_git_full_sync_config(account_identifier, body=body, org_identifier=org_identifier, project_identifier=project_identifier)

Create Configuration for Git Full Sync for the provided scope

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
api_instance = harness_python_sdk.GitFullSyncApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
body = harness_python_sdk.GitFullSyncConfigRequest() # GitFullSyncConfigRequest | Details of the Git Full sync Configuration (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Create Configuration for Git Full Sync for the provided scope
    api_response = api_instance.create_git_full_sync_config(account_identifier, body=body, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GitFullSyncApi->create_git_full_sync_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **body** | [**GitFullSyncConfigRequest**](GitFullSyncConfigRequest.md)| Details of the Git Full sync Configuration | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOGitFullSyncConfig**](ResponseDTOGitFullSyncConfig.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, text/yaml, text/html
 - **Accept**: application/json, application/yaml, text/yaml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_git_full_sync_config**
> ResponseDTOGitFullSyncConfig get_git_full_sync_config(account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Fetch Configuration for Git Full Sync for the provided scope

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
api_instance = harness_python_sdk.GitFullSyncApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Fetch Configuration for Git Full Sync for the provided scope
    api_response = api_instance.get_git_full_sync_config(account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GitFullSyncApi->get_git_full_sync_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOGitFullSyncConfig**](ResponseDTOGitFullSyncConfig.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, text/yaml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_full_sync_files**
> ResponseDTOPageResponseGitFullSyncEntityInfo list_full_sync_files(account_identifier, body=body, org_identifier=org_identifier, project_identifier=project_identifier, page_index=page_index, page_size=page_size, sort_orders=sort_orders, page_token=page_token, search_term=search_term)

List files in full sync along with their status

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
api_instance = harness_python_sdk.GitFullSyncApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
body = harness_python_sdk.GitFullSyncEntityInfoFilter() # GitFullSyncEntityInfoFilter | Entity Type and Sync Status (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
page_index = 0 # int | Page Index of the results to fetch.Default Value: 0 (optional) (default to 0)
page_size = 50 # int | Results per page(max 100)Default Value: 50 (optional) (default to 50)
sort_orders = [harness_python_sdk.SortOrder()] # list[SortOrder] | Sort criteria for the elements. (optional)
page_token = 'page_token_example' # str | Page Token of the next results to fetch.Default Value: '' (optional)
search_term = 'search_term_example' # str | Search Term. (optional)

try:
    # List files in full sync along with their status
    api_response = api_instance.list_full_sync_files(account_identifier, body=body, org_identifier=org_identifier, project_identifier=project_identifier, page_index=page_index, page_size=page_size, sort_orders=sort_orders, page_token=page_token, search_term=search_term)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GitFullSyncApi->list_full_sync_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **body** | [**GitFullSyncEntityInfoFilter**](GitFullSyncEntityInfoFilter.md)| Entity Type and Sync Status | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **page_index** | **int**| Page Index of the results to fetch.Default Value: 0 | [optional] [default to 0]
 **page_size** | **int**| Results per page(max 100)Default Value: 50 | [optional] [default to 50]
 **sort_orders** | [**list[SortOrder]**](SortOrder.md)| Sort criteria for the elements. | [optional] 
 **page_token** | **str**| Page Token of the next results to fetch.Default Value: &#x27;&#x27; | [optional] 
 **search_term** | **str**| Search Term. | [optional] 

### Return type

[**ResponseDTOPageResponseGitFullSyncEntityInfo**](ResponseDTOPageResponseGitFullSyncEntityInfo.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, text/yaml, text/html
 - **Accept**: application/json, application/yaml, text/yaml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trigger_full_sync**
> ResponseDTOTriggerGitFullSyncResponse trigger_full_sync(account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Trigger Full Sync

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
api_instance = harness_python_sdk.GitFullSyncApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Trigger Full Sync
    api_response = api_instance.trigger_full_sync(account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GitFullSyncApi->trigger_full_sync: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOTriggerGitFullSyncResponse**](ResponseDTOTriggerGitFullSyncResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, text/yaml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_git_full_sync_config**
> ResponseDTOGitFullSyncConfig update_git_full_sync_config(account_identifier, body=body, org_identifier=org_identifier, project_identifier=project_identifier)

Update Configuration for Git Full Sync for the provided scope

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
api_instance = harness_python_sdk.GitFullSyncApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
body = harness_python_sdk.GitFullSyncConfigRequest() # GitFullSyncConfigRequest | Details of the Git Full sync Configuration (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Update Configuration for Git Full Sync for the provided scope
    api_response = api_instance.update_git_full_sync_config(account_identifier, body=body, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GitFullSyncApi->update_git_full_sync_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **body** | [**GitFullSyncConfigRequest**](GitFullSyncConfigRequest.md)| Details of the Git Full sync Configuration | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOGitFullSyncConfig**](ResponseDTOGitFullSyncConfig.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, text/yaml, text/html
 - **Accept**: application/json, application/yaml, text/yaml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

