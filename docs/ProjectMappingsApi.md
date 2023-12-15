# harness_python_sdk.ProjectMappingsApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_project_mapping_service_create**](ProjectMappingsApi.md#app_project_mapping_service_create) | **POST** /gitops/api/v1/agents/{agentIdentifier}/appprojectsmapping | CreateAppProjectMapping creates a new mapping between Harness Project and argo project
[**app_project_mapping_service_delete**](ProjectMappingsApi.md#app_project_mapping_service_delete) | **DELETE** /gitops/api/v1/agents/{agentIdentifier}/appprojectsmapping/{name} | Delete an argo project to harness project mapping
[**app_project_mapping_service_get_app_project_mapping_list**](ProjectMappingsApi.md#app_project_mapping_service_get_app_project_mapping_list) | **GET** /gitops/api/v1/appprojectsmapping | 
[**app_project_mapping_service_get_app_project_mapping_list_by_agent**](ProjectMappingsApi.md#app_project_mapping_service_get_app_project_mapping_list_by_agent) | **GET** /gitops/api/v1/agents/{agentIdentifier}/appprojectsmapping | 

# **app_project_mapping_service_create**
> V1Empty app_project_mapping_service_create(body, agent_identifier, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)

CreateAppProjectMapping creates a new mapping between Harness Project and argo project

Creates Harness-Argo project mappings.

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
api_instance = harness_python_sdk.ProjectMappingsApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.Servicev1AppProjectMapping() # Servicev1AppProjectMapping | 
agent_identifier = 'agent_identifier_example' # str | Agent identifier for entity.
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity. (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # CreateAppProjectMapping creates a new mapping between Harness Project and argo project
    api_response = api_instance.app_project_mapping_service_create(body, agent_identifier, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectMappingsApi->app_project_mapping_service_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Servicev1AppProjectMapping**](Servicev1AppProjectMapping.md)|  | 
 **agent_identifier** | **str**| Agent identifier for entity. | 
 **account_identifier** | **str**| Account Identifier for the Entity. | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**V1Empty**](V1Empty.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_project_mapping_service_delete**
> V1Empty app_project_mapping_service_delete(agent_identifier, name, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Delete an argo project to harness project mapping

Delete Harness-Argo project mappings.

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
api_instance = harness_python_sdk.ProjectMappingsApi(harness_python_sdk.ApiClient(configuration))
agent_identifier = 'agent_identifier_example' # str | Agent identifier for entity.
name = 'name_example' # str | 
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Delete an argo project to harness project mapping
    api_response = api_instance.app_project_mapping_service_delete(agent_identifier, name, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectMappingsApi->app_project_mapping_service_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_identifier** | **str**| Agent identifier for entity. | 
 **name** | **str**|  | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**V1Empty**](V1Empty.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_project_mapping_service_get_app_project_mapping_list**
> Servicev1AppProjectMapping app_project_mapping_service_get_app_project_mapping_list(agent_identifier, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)



Retrieves Harness-Argo project mappings list.

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
api_instance = harness_python_sdk.ProjectMappingsApi(harness_python_sdk.ApiClient(configuration))
agent_identifier = 'agent_identifier_example' # str | Agent identifier for entity.
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity. (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    api_response = api_instance.app_project_mapping_service_get_app_project_mapping_list(agent_identifier, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectMappingsApi->app_project_mapping_service_get_app_project_mapping_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_identifier** | **str**| Agent identifier for entity. | 
 **account_identifier** | **str**| Account Identifier for the Entity. | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**Servicev1AppProjectMapping**](Servicev1AppProjectMapping.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_project_mapping_service_get_app_project_mapping_list_by_agent**
> Servicev1AppProjectMapping app_project_mapping_service_get_app_project_mapping_list_by_agent(agent_identifier, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)



Retrieves Harness-Argo project mappings list by agent.

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
api_instance = harness_python_sdk.ProjectMappingsApi(harness_python_sdk.ApiClient(configuration))
agent_identifier = 'agent_identifier_example' # str | Agent identifier for entity.
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    api_response = api_instance.app_project_mapping_service_get_app_project_mapping_list_by_agent(agent_identifier, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectMappingsApi->app_project_mapping_service_get_app_project_mapping_list_by_agent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_identifier** | **str**| Agent identifier for entity. | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**Servicev1AppProjectMapping**](Servicev1AppProjectMapping.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

