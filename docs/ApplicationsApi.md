# harness_python_sdk.ApplicationsApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**agent_application_service_create**](ApplicationsApi.md#agent_application_service_create) | **POST** /gitops/api/v1/agents/{agentIdentifier}/applications | Create creates an application
[**agent_application_service_delete**](ApplicationsApi.md#agent_application_service_delete) | **DELETE** /gitops/api/v1/agents/{agentIdentifier}/applications/{request.name} | Delete deletes an application
[**agent_application_service_delete_resource**](ApplicationsApi.md#agent_application_service_delete_resource) | **DELETE** /gitops/api/v1/agents/{agentIdentifier}/applications/{request.name}/resource | DeleteResource deletes a single application resource
[**agent_application_service_get**](ApplicationsApi.md#agent_application_service_get) | **GET** /gitops/api/v1/agents/{agentIdentifier}/applications/{query.name} | Get returns an application by name
[**agent_application_service_get_application_sync_windows**](ApplicationsApi.md#agent_application_service_get_application_sync_windows) | **GET** /gitops/api/v1/agents/{agentIdentifier}/applications/{query.name}/syncwindows | Get returns sync windows of the application
[**agent_application_service_get_manifests**](ApplicationsApi.md#agent_application_service_get_manifests) | **GET** /gitops/api/v1/agents/{agentIdentifier}/applications/{query.name}/manifests | GetManifests returns application manifests
[**agent_application_service_get_resource**](ApplicationsApi.md#agent_application_service_get_resource) | **GET** /gitops/api/v1/agents/{agentIdentifier}/applications/{request.name}/resource | GetResource returns single application resource
[**agent_application_service_list**](ApplicationsApi.md#agent_application_service_list) | **GET** /gitops/api/v1/agents/{agentIdentifier}/applications | List returns list of applications for a specific agent
[**agent_application_service_list_resource_actions**](ApplicationsApi.md#agent_application_service_list_resource_actions) | **GET** /gitops/api/v1/agents/{agentIdentifier}/applications/{request.name}/resource/actions | ListResourceActions returns list of resource actions
[**agent_application_service_list_resource_events**](ApplicationsApi.md#agent_application_service_list_resource_events) | **GET** /gitops/api/v1/agents/{agentIdentifier}/applications/{query.name}/events | ListResourceEvents returns a list of event resources
[**agent_application_service_managed_resources**](ApplicationsApi.md#agent_application_service_managed_resources) | **GET** /gitops/api/v1/agents/{agentIdentifier}/applications/{query.applicationName}/managed-resources | ManagedResources returns list of managed resources
[**agent_application_service_patch**](ApplicationsApi.md#agent_application_service_patch) | **PATCH** /gitops/api/v1/agents/{agentIdentifier}/applications/{request.name} | Patch patch an application
[**agent_application_service_patch_resource**](ApplicationsApi.md#agent_application_service_patch_resource) | **POST** /gitops/api/v1/agents/{agentIdentifier}/applications/{request.name}/resource | PatchResource patch single application resource
[**agent_application_service_pod_logs**](ApplicationsApi.md#agent_application_service_pod_logs) | **GET** /gitops/api/v1/agents/{agentIdentifier}/applications/{query.name}/pods/{query.podName}/logs | PodLogs returns stream of log entries for the specified pod(s).
[**agent_application_service_pod_logs2**](ApplicationsApi.md#agent_application_service_pod_logs2) | **GET** /gitops/api/v1/agents/{agentIdentifier}/applications/{query.name}/logs | PodLogs returns stream of log entries for the specified pod(s).
[**agent_application_service_resource_tree**](ApplicationsApi.md#agent_application_service_resource_tree) | **GET** /gitops/api/v1/agents/{agentIdentifier}/applications/{query.name}/resource-tree | ResourceTree returns resource tree
[**agent_application_service_revision_metadata**](ApplicationsApi.md#agent_application_service_revision_metadata) | **GET** /gitops/api/v1/agents/{agentIdentifier}/applications/{query.name}/revisions/{query.revision}/metadata | Get the meta-data (author, date, tags, message) for a specific revision of the application
[**agent_application_service_rollback**](ApplicationsApi.md#agent_application_service_rollback) | **POST** /gitops/api/v1/agents/{agentIdentifier}/applications/{request.name}/rollback | Rollback syncs an application to its target state Harness Event type (rollback)
[**agent_application_service_run_resource_action**](ApplicationsApi.md#agent_application_service_run_resource_action) | **POST** /gitops/api/v1/agents/{agentIdentifier}/applications/{request.name}/resource/actions | RunResourceAction run resource action
[**agent_application_service_sync**](ApplicationsApi.md#agent_application_service_sync) | **POST** /gitops/api/v1/agents/{agentIdentifier}/applications/{request.name}/sync | Sync syncs an application to its target state Harness Event type (deploy)
[**agent_application_service_terminate_operation**](ApplicationsApi.md#agent_application_service_terminate_operation) | **DELETE** /gitops/api/v1/agents/{agentIdentifier}/applications/{request.name}/operation | TerminateOperation terminates the currently running operation
[**agent_application_service_update**](ApplicationsApi.md#agent_application_service_update) | **PUT** /gitops/api/v1/agents/{agentIdentifier}/applications/{request.application.metadata.name} | Update updates an application
[**agent_application_service_update_spec**](ApplicationsApi.md#agent_application_service_update_spec) | **PUT** /gitops/api/v1/agents/{agentIdentifier}/applications/{request.name}/spec | UpdateSpec updates an application spec
[**agent_application_service_watch**](ApplicationsApi.md#agent_application_service_watch) | **GET** /gitops/api/v1/agents/{agentIdentifier}/stream/applications | Watch returns stream of application change events
[**agent_application_service_watch_resource_tree**](ApplicationsApi.md#agent_application_service_watch_resource_tree) | **GET** /gitops/api/v1/agents/{agentIdentifier}/stream/applications/{query.applicationName}/resource-tree | WatchResourceTree returns stream of application resource tree
[**application_service_exists**](ApplicationsApi.md#application_service_exists) | **GET** /gitops/api/v1/applications/{name}/exists | Checks whether an app with the given name exists
[**application_service_list_app_sync**](ApplicationsApi.md#application_service_list_app_sync) | **POST** /gitops/api/v1/applications/sync | List returns list of application sync status

# **agent_application_service_create**
> Servicev1Application agent_application_service_create(body, agent_identifier, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, cluster_identifier=cluster_identifier, repo_identifier=repo_identifier)

Create creates an application

Creates application in project.

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
api_instance = harness_python_sdk.ApplicationsApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.ApplicationsApplicationCreateRequest() # ApplicationsApplicationCreateRequest | 
agent_identifier = 'agent_identifier_example' # str | Agent identifier for entity.
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity. (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
cluster_identifier = 'cluster_identifier_example' # str |  (optional)
repo_identifier = 'repo_identifier_example' # str |  (optional)

try:
    # Create creates an application
    api_response = api_instance.agent_application_service_create(body, agent_identifier, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, cluster_identifier=cluster_identifier, repo_identifier=repo_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->agent_application_service_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApplicationsApplicationCreateRequest**](ApplicationsApplicationCreateRequest.md)|  | 
 **agent_identifier** | **str**| Agent identifier for entity. | 
 **account_identifier** | **str**| Account Identifier for the Entity. | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **cluster_identifier** | **str**|  | [optional] 
 **repo_identifier** | **str**|  | [optional] 

### Return type

[**Servicev1Application**](Servicev1Application.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_application_service_delete**
> ApplicationsApplicationResponse agent_application_service_delete(agent_identifier, request_name, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, request_cascade=request_cascade, request_propagation_policy=request_propagation_policy, options_remove_existing_finalizers=options_remove_existing_finalizers)

Delete deletes an application

Delete deletes an application.

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
api_instance = harness_python_sdk.ApplicationsApi(harness_python_sdk.ApiClient(configuration))
agent_identifier = 'agent_identifier_example' # str | Agent identifier for entity.
request_name = 'request_name_example' # str | 
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity. (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
request_cascade = true # bool |  (optional)
request_propagation_policy = 'request_propagation_policy_example' # str |  (optional)
options_remove_existing_finalizers = true # bool |  (optional)

try:
    # Delete deletes an application
    api_response = api_instance.agent_application_service_delete(agent_identifier, request_name, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, request_cascade=request_cascade, request_propagation_policy=request_propagation_policy, options_remove_existing_finalizers=options_remove_existing_finalizers)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->agent_application_service_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_identifier** | **str**| Agent identifier for entity. | 
 **request_name** | **str**|  | 
 **account_identifier** | **str**| Account Identifier for the Entity. | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **request_cascade** | **bool**|  | [optional] 
 **request_propagation_policy** | **str**|  | [optional] 
 **options_remove_existing_finalizers** | **bool**|  | [optional] 

### Return type

[**ApplicationsApplicationResponse**](ApplicationsApplicationResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_application_service_delete_resource**
> ApplicationsApplicationResponse agent_application_service_delete_resource(agent_identifier, request_name, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, request_namespace=request_namespace, request_resource_name=request_resource_name, request_version=request_version, request_group=request_group, request_kind=request_kind, request_force=request_force, request_orphan=request_orphan)

DeleteResource deletes a single application resource

DeleteResource deletes a single application resource.

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
api_instance = harness_python_sdk.ApplicationsApi(harness_python_sdk.ApiClient(configuration))
agent_identifier = 'agent_identifier_example' # str | Agent identifier for entity.
request_name = 'request_name_example' # str | 
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity. (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
request_namespace = 'request_namespace_example' # str |  (optional)
request_resource_name = 'request_resource_name_example' # str |  (optional)
request_version = 'request_version_example' # str |  (optional)
request_group = 'request_group_example' # str |  (optional)
request_kind = 'request_kind_example' # str |  (optional)
request_force = true # bool |  (optional)
request_orphan = true # bool |  (optional)

try:
    # DeleteResource deletes a single application resource
    api_response = api_instance.agent_application_service_delete_resource(agent_identifier, request_name, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, request_namespace=request_namespace, request_resource_name=request_resource_name, request_version=request_version, request_group=request_group, request_kind=request_kind, request_force=request_force, request_orphan=request_orphan)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->agent_application_service_delete_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_identifier** | **str**| Agent identifier for entity. | 
 **request_name** | **str**|  | 
 **account_identifier** | **str**| Account Identifier for the Entity. | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **request_namespace** | **str**|  | [optional] 
 **request_resource_name** | **str**|  | [optional] 
 **request_version** | **str**|  | [optional] 
 **request_group** | **str**|  | [optional] 
 **request_kind** | **str**|  | [optional] 
 **request_force** | **bool**|  | [optional] 
 **request_orphan** | **bool**|  | [optional] 

### Return type

[**ApplicationsApplicationResponse**](ApplicationsApplicationResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_application_service_get**
> Servicev1Application agent_application_service_get(agent_identifier, query_name, account_identifier, org_identifier, project_identifier, query_refresh=query_refresh, query_project=query_project, query_resource_version=query_resource_version, query_selector=query_selector, query_repo=query_repo)

Get returns an application by name

 Get returns an application by name

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
api_instance = harness_python_sdk.ApplicationsApi(harness_python_sdk.ApiClient(configuration))
agent_identifier = 'agent_identifier_example' # str | Agent identifier for entity.
query_name = 'query_name_example' # str | the application's name
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
query_refresh = 'query_refresh_example' # str | forces application reconciliation if set to true. (optional)
query_project = ['query_project_example'] # list[str] | the project names to restrict returned list applications. (optional)
query_resource_version = 'query_resource_version_example' # str | when specified with a watch call, shows changes that occur after that particular version of a resource. (optional)
query_selector = 'query_selector_example' # str | the selector to to restrict returned list to applications only with matched labels. (optional)
query_repo = 'query_repo_example' # str | the repoURL to restrict returned list applications. (optional)

try:
    # Get returns an application by name
    api_response = api_instance.agent_application_service_get(agent_identifier, query_name, account_identifier, org_identifier, project_identifier, query_refresh=query_refresh, query_project=query_project, query_resource_version=query_resource_version, query_selector=query_selector, query_repo=query_repo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->agent_application_service_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_identifier** | **str**| Agent identifier for entity. | 
 **query_name** | **str**| the application&#x27;s name | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **query_refresh** | **str**| forces application reconciliation if set to true. | [optional] 
 **query_project** | [**list[str]**](str.md)| the project names to restrict returned list applications. | [optional] 
 **query_resource_version** | **str**| when specified with a watch call, shows changes that occur after that particular version of a resource. | [optional] 
 **query_selector** | **str**| the selector to to restrict returned list to applications only with matched labels. | [optional] 
 **query_repo** | **str**| the repoURL to restrict returned list applications. | [optional] 

### Return type

[**Servicev1Application**](Servicev1Application.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_application_service_get_application_sync_windows**
> ApplicationsApplicationSyncWindowsResponse agent_application_service_get_application_sync_windows(agent_identifier, query_name, account_identifier, org_identifier, project_identifier)

Get returns sync windows of the application

GetApplicationSyncWindows returns sync windows of the application.

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
api_instance = harness_python_sdk.ApplicationsApi(harness_python_sdk.ApiClient(configuration))
agent_identifier = 'agent_identifier_example' # str | Agent identifier for entity.
query_name = 'query_name_example' # str | 
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.

try:
    # Get returns sync windows of the application
    api_response = api_instance.agent_application_service_get_application_sync_windows(agent_identifier, query_name, account_identifier, org_identifier, project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->agent_application_service_get_application_sync_windows: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_identifier** | **str**| Agent identifier for entity. | 
 **query_name** | **str**|  | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 

### Return type

[**ApplicationsApplicationSyncWindowsResponse**](ApplicationsApplicationSyncWindowsResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_application_service_get_manifests**
> RepositoriesManifestResponse agent_application_service_get_manifests(agent_identifier, query_name, account_identifier, org_identifier, project_identifier, query_revision=query_revision)

GetManifests returns application manifests

GetManifests returns application manifests.

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
api_instance = harness_python_sdk.ApplicationsApi(harness_python_sdk.ApiClient(configuration))
agent_identifier = 'agent_identifier_example' # str | Agent identifier for entity.
query_name = 'query_name_example' # str | 
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
query_revision = 'query_revision_example' # str |  (optional)

try:
    # GetManifests returns application manifests
    api_response = api_instance.agent_application_service_get_manifests(agent_identifier, query_name, account_identifier, org_identifier, project_identifier, query_revision=query_revision)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->agent_application_service_get_manifests: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_identifier** | **str**| Agent identifier for entity. | 
 **query_name** | **str**|  | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **query_revision** | **str**|  | [optional] 

### Return type

[**RepositoriesManifestResponse**](RepositoriesManifestResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_application_service_get_resource**
> ApplicationsApplicationResourceResponse agent_application_service_get_resource(agent_identifier, request_name, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, request_namespace=request_namespace, request_resource_name=request_resource_name, request_version=request_version, request_group=request_group, request_kind=request_kind)

GetResource returns single application resource

GetResource returns single application resource.

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
api_instance = harness_python_sdk.ApplicationsApi(harness_python_sdk.ApiClient(configuration))
agent_identifier = 'agent_identifier_example' # str | Agent identifier for entity.
request_name = 'request_name_example' # str | 
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity. (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
request_namespace = 'request_namespace_example' # str |  (optional)
request_resource_name = 'request_resource_name_example' # str |  (optional)
request_version = 'request_version_example' # str |  (optional)
request_group = 'request_group_example' # str |  (optional)
request_kind = 'request_kind_example' # str |  (optional)

try:
    # GetResource returns single application resource
    api_response = api_instance.agent_application_service_get_resource(agent_identifier, request_name, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, request_namespace=request_namespace, request_resource_name=request_resource_name, request_version=request_version, request_group=request_group, request_kind=request_kind)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->agent_application_service_get_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_identifier** | **str**| Agent identifier for entity. | 
 **request_name** | **str**|  | 
 **account_identifier** | **str**| Account Identifier for the Entity. | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **request_namespace** | **str**|  | [optional] 
 **request_resource_name** | **str**|  | [optional] 
 **request_version** | **str**|  | [optional] 
 **request_group** | **str**|  | [optional] 
 **request_kind** | **str**|  | [optional] 

### Return type

[**ApplicationsApplicationResourceResponse**](ApplicationsApplicationResourceResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_application_service_list**
> ApplicationsApplicationList agent_application_service_list(agent_identifier, account_identifier, org_identifier, project_identifier, query_name=query_name, query_refresh=query_refresh, query_project=query_project, query_resource_version=query_resource_version, query_selector=query_selector, query_repo=query_repo)

List returns list of applications for a specific agent

List returns list of applications for a specific agent.

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
api_instance = harness_python_sdk.ApplicationsApi(harness_python_sdk.ApiClient(configuration))
agent_identifier = 'agent_identifier_example' # str | Agent identifier for entity.
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
query_name = 'query_name_example' # str | the application's name. (optional)
query_refresh = 'query_refresh_example' # str | forces application reconciliation if set to true. (optional)
query_project = ['query_project_example'] # list[str] | the project names to restrict returned list applications. (optional)
query_resource_version = 'query_resource_version_example' # str | when specified with a watch call, shows changes that occur after that particular version of a resource. (optional)
query_selector = 'query_selector_example' # str | the selector to to restrict returned list to applications only with matched labels. (optional)
query_repo = 'query_repo_example' # str | the repoURL to restrict returned list applications. (optional)

try:
    # List returns list of applications for a specific agent
    api_response = api_instance.agent_application_service_list(agent_identifier, account_identifier, org_identifier, project_identifier, query_name=query_name, query_refresh=query_refresh, query_project=query_project, query_resource_version=query_resource_version, query_selector=query_selector, query_repo=query_repo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->agent_application_service_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_identifier** | **str**| Agent identifier for entity. | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **query_name** | **str**| the application&#x27;s name. | [optional] 
 **query_refresh** | **str**| forces application reconciliation if set to true. | [optional] 
 **query_project** | [**list[str]**](str.md)| the project names to restrict returned list applications. | [optional] 
 **query_resource_version** | **str**| when specified with a watch call, shows changes that occur after that particular version of a resource. | [optional] 
 **query_selector** | **str**| the selector to to restrict returned list to applications only with matched labels. | [optional] 
 **query_repo** | **str**| the repoURL to restrict returned list applications. | [optional] 

### Return type

[**ApplicationsApplicationList**](ApplicationsApplicationList.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_application_service_list_resource_actions**
> ApplicationsResourceActionsListResponse agent_application_service_list_resource_actions(agent_identifier, request_name, account_identifier, org_identifier, project_identifier, request_namespace=request_namespace, request_resource_name=request_resource_name, request_version=request_version, request_group=request_group, request_kind=request_kind)

ListResourceActions returns list of resource actions

ListResourceActions returns list of resource actions.

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
api_instance = harness_python_sdk.ApplicationsApi(harness_python_sdk.ApiClient(configuration))
agent_identifier = 'agent_identifier_example' # str | Agent identifier for entity.
request_name = 'request_name_example' # str | 
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
request_namespace = 'request_namespace_example' # str |  (optional)
request_resource_name = 'request_resource_name_example' # str |  (optional)
request_version = 'request_version_example' # str |  (optional)
request_group = 'request_group_example' # str |  (optional)
request_kind = 'request_kind_example' # str |  (optional)

try:
    # ListResourceActions returns list of resource actions
    api_response = api_instance.agent_application_service_list_resource_actions(agent_identifier, request_name, account_identifier, org_identifier, project_identifier, request_namespace=request_namespace, request_resource_name=request_resource_name, request_version=request_version, request_group=request_group, request_kind=request_kind)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->agent_application_service_list_resource_actions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_identifier** | **str**| Agent identifier for entity. | 
 **request_name** | **str**|  | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **request_namespace** | **str**|  | [optional] 
 **request_resource_name** | **str**|  | [optional] 
 **request_version** | **str**|  | [optional] 
 **request_group** | **str**|  | [optional] 
 **request_kind** | **str**|  | [optional] 

### Return type

[**ApplicationsResourceActionsListResponse**](ApplicationsResourceActionsListResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_application_service_list_resource_events**
> V1EventList agent_application_service_list_resource_events(agent_identifier, query_name, account_identifier, org_identifier, project_identifier, query_resource_namespace=query_resource_namespace, query_resource_name=query_resource_name, query_resource_uid=query_resource_uid)

ListResourceEvents returns a list of event resources

ListResourceEvents returns list of event resources.

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
api_instance = harness_python_sdk.ApplicationsApi(harness_python_sdk.ApiClient(configuration))
agent_identifier = 'agent_identifier_example' # str | Agent identifier for entity.
query_name = 'query_name_example' # str | 
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
query_resource_namespace = 'query_resource_namespace_example' # str |  (optional)
query_resource_name = 'query_resource_name_example' # str |  (optional)
query_resource_uid = 'query_resource_uid_example' # str |  (optional)

try:
    # ListResourceEvents returns a list of event resources
    api_response = api_instance.agent_application_service_list_resource_events(agent_identifier, query_name, account_identifier, org_identifier, project_identifier, query_resource_namespace=query_resource_namespace, query_resource_name=query_resource_name, query_resource_uid=query_resource_uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->agent_application_service_list_resource_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_identifier** | **str**| Agent identifier for entity. | 
 **query_name** | **str**|  | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **query_resource_namespace** | **str**|  | [optional] 
 **query_resource_name** | **str**|  | [optional] 
 **query_resource_uid** | **str**|  | [optional] 

### Return type

[**V1EventList**](V1EventList.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_application_service_managed_resources**
> ApplicationsManagedResourcesResponse agent_application_service_managed_resources(agent_identifier, query_application_name, account_identifier, org_identifier, project_identifier, query_namespace=query_namespace, query_name=query_name, query_version=query_version, query_group=query_group, query_kind=query_kind)

ManagedResources returns list of managed resources

ManagedResources returns list of managed resources.

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
api_instance = harness_python_sdk.ApplicationsApi(harness_python_sdk.ApiClient(configuration))
agent_identifier = 'agent_identifier_example' # str | Agent identifier for entity.
query_application_name = 'query_application_name_example' # str | 
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
query_namespace = 'query_namespace_example' # str |  (optional)
query_name = 'query_name_example' # str |  (optional)
query_version = 'query_version_example' # str |  (optional)
query_group = 'query_group_example' # str |  (optional)
query_kind = 'query_kind_example' # str |  (optional)

try:
    # ManagedResources returns list of managed resources
    api_response = api_instance.agent_application_service_managed_resources(agent_identifier, query_application_name, account_identifier, org_identifier, project_identifier, query_namespace=query_namespace, query_name=query_name, query_version=query_version, query_group=query_group, query_kind=query_kind)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->agent_application_service_managed_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_identifier** | **str**| Agent identifier for entity. | 
 **query_application_name** | **str**|  | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **query_namespace** | **str**|  | [optional] 
 **query_name** | **str**|  | [optional] 
 **query_version** | **str**|  | [optional] 
 **query_group** | **str**|  | [optional] 
 **query_kind** | **str**|  | [optional] 

### Return type

[**ApplicationsManagedResourcesResponse**](ApplicationsManagedResourcesResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_application_service_patch**
> Servicev1Application agent_application_service_patch(body, agent_identifier, request_name)

Patch patch an application

Patch applys a patches to an application.

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
api_instance = harness_python_sdk.ApplicationsApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.Servicev1ApplicationPatchRequest() # Servicev1ApplicationPatchRequest | 
agent_identifier = 'agent_identifier_example' # str | Agent identifier for entity.
request_name = 'request_name_example' # str | 

try:
    # Patch patch an application
    api_response = api_instance.agent_application_service_patch(body, agent_identifier, request_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->agent_application_service_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Servicev1ApplicationPatchRequest**](Servicev1ApplicationPatchRequest.md)|  | 
 **agent_identifier** | **str**| Agent identifier for entity. | 
 **request_name** | **str**|  | 

### Return type

[**Servicev1Application**](Servicev1Application.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_application_service_patch_resource**
> ApplicationsApplicationResourceResponse agent_application_service_patch_resource(body, agent_identifier, request_name, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)

PatchResource patch single application resource

PatchResource patch single application resource.

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
api_instance = harness_python_sdk.ApplicationsApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.ApplicationsApplicationResourcePatchRequest() # ApplicationsApplicationResourcePatchRequest | 
agent_identifier = 'agent_identifier_example' # str | Agent identifier for entity.
request_name = 'request_name_example' # str | 
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity. (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # PatchResource patch single application resource
    api_response = api_instance.agent_application_service_patch_resource(body, agent_identifier, request_name, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->agent_application_service_patch_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApplicationsApplicationResourcePatchRequest**](ApplicationsApplicationResourcePatchRequest.md)|  | 
 **agent_identifier** | **str**| Agent identifier for entity. | 
 **request_name** | **str**|  | 
 **account_identifier** | **str**| Account Identifier for the Entity. | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ApplicationsApplicationResourceResponse**](ApplicationsApplicationResourceResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_application_service_pod_logs**
> StreamResultOfApplicationsLogEntry agent_application_service_pod_logs(agent_identifier, query_name, query_pod_name, account_identifier, org_identifier, project_identifier, query_namespace=query_namespace, query_container=query_container, query_since_seconds=query_since_seconds, query_since_time_seconds=query_since_time_seconds, query_since_time_nanos=query_since_time_nanos, query_tail_lines=query_tail_lines, query_follow=query_follow, query_until_time=query_until_time, query_filter=query_filter, query_kind=query_kind, query_group=query_group, query_resource_name=query_resource_name, query_previous=query_previous)

PodLogs returns stream of log entries for the specified pod(s).

PodLogs returns stream of log entries for the specified pod(s).

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
api_instance = harness_python_sdk.ApplicationsApi(harness_python_sdk.ApiClient(configuration))
agent_identifier = 'agent_identifier_example' # str | Agent identifier for entity.
query_name = 'query_name_example' # str | 
query_pod_name = 'query_pod_name_example' # str | 
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
query_namespace = 'query_namespace_example' # str |  (optional)
query_container = 'query_container_example' # str |  (optional)
query_since_seconds = 'query_since_seconds_example' # str |  (optional)
query_since_time_seconds = 'query_since_time_seconds_example' # str | Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be from 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z inclusive. (optional)
query_since_time_nanos = 56 # int | Non-negative fractions of a second at nanosecond resolution. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be from 0 to 999,999,999 inclusive. This field may be limited in precision depending on context. (optional)
query_tail_lines = 'query_tail_lines_example' # str |  (optional)
query_follow = true # bool |  (optional)
query_until_time = 'query_until_time_example' # str |  (optional)
query_filter = 'query_filter_example' # str |  (optional)
query_kind = 'query_kind_example' # str |  (optional)
query_group = 'query_group_example' # str |  (optional)
query_resource_name = 'query_resource_name_example' # str |  (optional)
query_previous = true # bool |  (optional)

try:
    # PodLogs returns stream of log entries for the specified pod(s).
    api_response = api_instance.agent_application_service_pod_logs(agent_identifier, query_name, query_pod_name, account_identifier, org_identifier, project_identifier, query_namespace=query_namespace, query_container=query_container, query_since_seconds=query_since_seconds, query_since_time_seconds=query_since_time_seconds, query_since_time_nanos=query_since_time_nanos, query_tail_lines=query_tail_lines, query_follow=query_follow, query_until_time=query_until_time, query_filter=query_filter, query_kind=query_kind, query_group=query_group, query_resource_name=query_resource_name, query_previous=query_previous)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->agent_application_service_pod_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_identifier** | **str**| Agent identifier for entity. | 
 **query_name** | **str**|  | 
 **query_pod_name** | **str**|  | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **query_namespace** | **str**|  | [optional] 
 **query_container** | **str**|  | [optional] 
 **query_since_seconds** | **str**|  | [optional] 
 **query_since_time_seconds** | **str**| Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be from 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z inclusive. | [optional] 
 **query_since_time_nanos** | **int**| Non-negative fractions of a second at nanosecond resolution. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be from 0 to 999,999,999 inclusive. This field may be limited in precision depending on context. | [optional] 
 **query_tail_lines** | **str**|  | [optional] 
 **query_follow** | **bool**|  | [optional] 
 **query_until_time** | **str**|  | [optional] 
 **query_filter** | **str**|  | [optional] 
 **query_kind** | **str**|  | [optional] 
 **query_group** | **str**|  | [optional] 
 **query_resource_name** | **str**|  | [optional] 
 **query_previous** | **bool**|  | [optional] 

### Return type

[**StreamResultOfApplicationsLogEntry**](StreamResultOfApplicationsLogEntry.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_application_service_pod_logs2**
> StreamResultOfApplicationsLogEntry agent_application_service_pod_logs2(agent_identifier, query_name, account_identifier, org_identifier, project_identifier, query_namespace=query_namespace, query_pod_name=query_pod_name, query_container=query_container, query_since_seconds=query_since_seconds, query_since_time_seconds=query_since_time_seconds, query_since_time_nanos=query_since_time_nanos, query_tail_lines=query_tail_lines, query_follow=query_follow, query_until_time=query_until_time, query_filter=query_filter, query_kind=query_kind, query_group=query_group, query_resource_name=query_resource_name, query_previous=query_previous)

PodLogs returns stream of log entries for the specified pod(s).

PodLogs returns stream of log entries for the specified pod(s).

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
api_instance = harness_python_sdk.ApplicationsApi(harness_python_sdk.ApiClient(configuration))
agent_identifier = 'agent_identifier_example' # str | Agent identifier for entity.
query_name = 'query_name_example' # str | 
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
query_namespace = 'query_namespace_example' # str |  (optional)
query_pod_name = 'query_pod_name_example' # str |  (optional)
query_container = 'query_container_example' # str |  (optional)
query_since_seconds = 'query_since_seconds_example' # str |  (optional)
query_since_time_seconds = 'query_since_time_seconds_example' # str | Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be from 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z inclusive. (optional)
query_since_time_nanos = 56 # int | Non-negative fractions of a second at nanosecond resolution. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be from 0 to 999,999,999 inclusive. This field may be limited in precision depending on context. (optional)
query_tail_lines = 'query_tail_lines_example' # str |  (optional)
query_follow = true # bool |  (optional)
query_until_time = 'query_until_time_example' # str |  (optional)
query_filter = 'query_filter_example' # str |  (optional)
query_kind = 'query_kind_example' # str |  (optional)
query_group = 'query_group_example' # str |  (optional)
query_resource_name = 'query_resource_name_example' # str |  (optional)
query_previous = true # bool |  (optional)

try:
    # PodLogs returns stream of log entries for the specified pod(s).
    api_response = api_instance.agent_application_service_pod_logs2(agent_identifier, query_name, account_identifier, org_identifier, project_identifier, query_namespace=query_namespace, query_pod_name=query_pod_name, query_container=query_container, query_since_seconds=query_since_seconds, query_since_time_seconds=query_since_time_seconds, query_since_time_nanos=query_since_time_nanos, query_tail_lines=query_tail_lines, query_follow=query_follow, query_until_time=query_until_time, query_filter=query_filter, query_kind=query_kind, query_group=query_group, query_resource_name=query_resource_name, query_previous=query_previous)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->agent_application_service_pod_logs2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_identifier** | **str**| Agent identifier for entity. | 
 **query_name** | **str**|  | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **query_namespace** | **str**|  | [optional] 
 **query_pod_name** | **str**|  | [optional] 
 **query_container** | **str**|  | [optional] 
 **query_since_seconds** | **str**|  | [optional] 
 **query_since_time_seconds** | **str**| Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be from 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z inclusive. | [optional] 
 **query_since_time_nanos** | **int**| Non-negative fractions of a second at nanosecond resolution. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be from 0 to 999,999,999 inclusive. This field may be limited in precision depending on context. | [optional] 
 **query_tail_lines** | **str**|  | [optional] 
 **query_follow** | **bool**|  | [optional] 
 **query_until_time** | **str**|  | [optional] 
 **query_filter** | **str**|  | [optional] 
 **query_kind** | **str**|  | [optional] 
 **query_group** | **str**|  | [optional] 
 **query_resource_name** | **str**|  | [optional] 
 **query_previous** | **bool**|  | [optional] 

### Return type

[**StreamResultOfApplicationsLogEntry**](StreamResultOfApplicationsLogEntry.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_application_service_resource_tree**
> ApplicationsApplicationTree agent_application_service_resource_tree(agent_identifier, query_name, account_identifier, org_identifier, project_identifier, query_application_name=query_application_name, query_namespace=query_namespace, query_version=query_version, query_group=query_group, query_kind=query_kind)

ResourceTree returns resource tree

ResourceTree returns resource tree.

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
api_instance = harness_python_sdk.ApplicationsApi(harness_python_sdk.ApiClient(configuration))
agent_identifier = 'agent_identifier_example' # str | Agent identifier for entity.
query_name = 'query_name_example' # str | 
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
query_application_name = 'query_application_name_example' # str |  (optional)
query_namespace = 'query_namespace_example' # str |  (optional)
query_version = 'query_version_example' # str |  (optional)
query_group = 'query_group_example' # str |  (optional)
query_kind = 'query_kind_example' # str |  (optional)

try:
    # ResourceTree returns resource tree
    api_response = api_instance.agent_application_service_resource_tree(agent_identifier, query_name, account_identifier, org_identifier, project_identifier, query_application_name=query_application_name, query_namespace=query_namespace, query_version=query_version, query_group=query_group, query_kind=query_kind)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->agent_application_service_resource_tree: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_identifier** | **str**| Agent identifier for entity. | 
 **query_name** | **str**|  | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **query_application_name** | **str**|  | [optional] 
 **query_namespace** | **str**|  | [optional] 
 **query_version** | **str**|  | [optional] 
 **query_group** | **str**|  | [optional] 
 **query_kind** | **str**|  | [optional] 

### Return type

[**ApplicationsApplicationTree**](ApplicationsApplicationTree.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_application_service_revision_metadata**
> RepositoriesRevisionMetadata agent_application_service_revision_metadata(agent_identifier, query_name, query_revision, account_identifier, org_identifier, project_identifier)

Get the meta-data (author, date, tags, message) for a specific revision of the application

RevisionMetadata returns metadata for a specific revision of the application.

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
api_instance = harness_python_sdk.ApplicationsApi(harness_python_sdk.ApiClient(configuration))
agent_identifier = 'agent_identifier_example' # str | Agent identifier for entity.
query_name = 'query_name_example' # str | the application's name
query_revision = 'query_revision_example' # str | the revision of the app
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.

try:
    # Get the meta-data (author, date, tags, message) for a specific revision of the application
    api_response = api_instance.agent_application_service_revision_metadata(agent_identifier, query_name, query_revision, account_identifier, org_identifier, project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->agent_application_service_revision_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_identifier** | **str**| Agent identifier for entity. | 
 **query_name** | **str**| the application&#x27;s name | 
 **query_revision** | **str**| the revision of the app | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 

### Return type

[**RepositoriesRevisionMetadata**](RepositoriesRevisionMetadata.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_application_service_rollback**
> Servicev1Application agent_application_service_rollback(body, account_identifier, org_identifier, project_identifier, agent_identifier, request_name)

Rollback syncs an application to its target state Harness Event type (rollback)

Rollback syncs an application to its target state Harness Event type (rollback).

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
api_instance = harness_python_sdk.ApplicationsApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.ApplicationsApplicationRollbackRequest() # ApplicationsApplicationRollbackRequest | 
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
agent_identifier = 'agent_identifier_example' # str | Agent identifier for entity.
request_name = 'request_name_example' # str | 

try:
    # Rollback syncs an application to its target state Harness Event type (rollback)
    api_response = api_instance.agent_application_service_rollback(body, account_identifier, org_identifier, project_identifier, agent_identifier, request_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->agent_application_service_rollback: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApplicationsApplicationRollbackRequest**](ApplicationsApplicationRollbackRequest.md)|  | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **agent_identifier** | **str**| Agent identifier for entity. | 
 **request_name** | **str**|  | 

### Return type

[**Servicev1Application**](Servicev1Application.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_application_service_run_resource_action**
> ApplicationsApplicationResponse agent_application_service_run_resource_action(body, agent_identifier, request_name, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)

RunResourceAction run resource action

RunResourceAction run resource action.

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
api_instance = harness_python_sdk.ApplicationsApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.ApplicationsResourceActionRunRequest() # ApplicationsResourceActionRunRequest | 
agent_identifier = 'agent_identifier_example' # str | Agent identifier for entity.
request_name = 'request_name_example' # str | 
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity. (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # RunResourceAction run resource action
    api_response = api_instance.agent_application_service_run_resource_action(body, agent_identifier, request_name, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->agent_application_service_run_resource_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApplicationsResourceActionRunRequest**](ApplicationsResourceActionRunRequest.md)|  | 
 **agent_identifier** | **str**| Agent identifier for entity. | 
 **request_name** | **str**|  | 
 **account_identifier** | **str**| Account Identifier for the Entity. | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ApplicationsApplicationResponse**](ApplicationsApplicationResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_application_service_sync**
> Servicev1Application agent_application_service_sync(body, account_identifier, org_identifier, project_identifier, agent_identifier, request_name)

Sync syncs an application to its target state Harness Event type (deploy)

Delete deletes an application.

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
api_instance = harness_python_sdk.ApplicationsApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.ApplicationsApplicationSyncRequest() # ApplicationsApplicationSyncRequest | 
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
agent_identifier = 'agent_identifier_example' # str | Agent identifier for entity.
request_name = 'request_name_example' # str | 

try:
    # Sync syncs an application to its target state Harness Event type (deploy)
    api_response = api_instance.agent_application_service_sync(body, account_identifier, org_identifier, project_identifier, agent_identifier, request_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->agent_application_service_sync: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApplicationsApplicationSyncRequest**](ApplicationsApplicationSyncRequest.md)|  | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **agent_identifier** | **str**| Agent identifier for entity. | 
 **request_name** | **str**|  | 

### Return type

[**Servicev1Application**](Servicev1Application.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_application_service_terminate_operation**
> ApplicationsOperationTerminateResponse agent_application_service_terminate_operation(agent_identifier, request_name, account_identifier, org_identifier, project_identifier)

TerminateOperation terminates the currently running operation

TerminateOperation terminates the currently running operation.

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
api_instance = harness_python_sdk.ApplicationsApi(harness_python_sdk.ApiClient(configuration))
agent_identifier = 'agent_identifier_example' # str | Agent identifier for entity.
request_name = 'request_name_example' # str | 
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.

try:
    # TerminateOperation terminates the currently running operation
    api_response = api_instance.agent_application_service_terminate_operation(agent_identifier, request_name, account_identifier, org_identifier, project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->agent_application_service_terminate_operation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_identifier** | **str**| Agent identifier for entity. | 
 **request_name** | **str**|  | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 

### Return type

[**ApplicationsOperationTerminateResponse**](ApplicationsOperationTerminateResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_application_service_update**
> Servicev1Application agent_application_service_update(body, account_identifier, org_identifier, project_identifier, agent_identifier, request_application_metadata_name, cluster_identifier=cluster_identifier, repo_identifier=repo_identifier)

Update updates an application

Update updates an application.

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
api_instance = harness_python_sdk.ApplicationsApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.ApplicationsApplicationUpdateRequest() # ApplicationsApplicationUpdateRequest | 
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
agent_identifier = 'agent_identifier_example' # str | Agent identifier for entity.
request_application_metadata_name = 'request_application_metadata_name_example' # str | Name must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names +optional
cluster_identifier = 'cluster_identifier_example' # str |  (optional)
repo_identifier = 'repo_identifier_example' # str |  (optional)

try:
    # Update updates an application
    api_response = api_instance.agent_application_service_update(body, account_identifier, org_identifier, project_identifier, agent_identifier, request_application_metadata_name, cluster_identifier=cluster_identifier, repo_identifier=repo_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->agent_application_service_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApplicationsApplicationUpdateRequest**](ApplicationsApplicationUpdateRequest.md)|  | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **agent_identifier** | **str**| Agent identifier for entity. | 
 **request_application_metadata_name** | **str**| Name must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names +optional | 
 **cluster_identifier** | **str**|  | [optional] 
 **repo_identifier** | **str**|  | [optional] 

### Return type

[**Servicev1Application**](Servicev1Application.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_application_service_update_spec**
> ApplicationsApplicationSpec agent_application_service_update_spec(body, account_identifier, org_identifier, project_identifier, agent_identifier, request_name)

UpdateSpec updates an application spec

UpdateSpec updates an application spec.

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
api_instance = harness_python_sdk.ApplicationsApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.ApplicationsApplicationUpdateSpecRequest() # ApplicationsApplicationUpdateSpecRequest | 
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
agent_identifier = 'agent_identifier_example' # str | Agent identifier for entity.
request_name = 'request_name_example' # str | 

try:
    # UpdateSpec updates an application spec
    api_response = api_instance.agent_application_service_update_spec(body, account_identifier, org_identifier, project_identifier, agent_identifier, request_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->agent_application_service_update_spec: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApplicationsApplicationUpdateSpecRequest**](ApplicationsApplicationUpdateSpecRequest.md)|  | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **agent_identifier** | **str**| Agent identifier for entity. | 
 **request_name** | **str**|  | 

### Return type

[**ApplicationsApplicationSpec**](ApplicationsApplicationSpec.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_application_service_watch**
> StreamResultOfApplicationsApplicationWatchEvent agent_application_service_watch(agent_identifier, account_identifier, org_identifier, project_identifier, query_name, query_refresh=query_refresh, query_project=query_project, query_resource_version=query_resource_version, query_selector=query_selector, query_repo=query_repo)

Watch returns stream of application change events

Watch returns stream of application change events.

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
api_instance = harness_python_sdk.ApplicationsApi(harness_python_sdk.ApiClient(configuration))
agent_identifier = 'agent_identifier_example' # str | Agent identifier for entity.
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
query_name = 'query_name_example' # str | the application's name.
query_refresh = 'query_refresh_example' # str | forces application reconciliation if set to true. (optional)
query_project = ['query_project_example'] # list[str] | the project names to restrict returned list applications. (optional)
query_resource_version = 'query_resource_version_example' # str | when specified with a watch call, shows changes that occur after that particular version of a resource. (optional)
query_selector = 'query_selector_example' # str | the selector to to restrict returned list to applications only with matched labels. (optional)
query_repo = 'query_repo_example' # str | the repoURL to restrict returned list applications. (optional)

try:
    # Watch returns stream of application change events
    api_response = api_instance.agent_application_service_watch(agent_identifier, account_identifier, org_identifier, project_identifier, query_name, query_refresh=query_refresh, query_project=query_project, query_resource_version=query_resource_version, query_selector=query_selector, query_repo=query_repo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->agent_application_service_watch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_identifier** | **str**| Agent identifier for entity. | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **query_name** | **str**| the application&#x27;s name. | 
 **query_refresh** | **str**| forces application reconciliation if set to true. | [optional] 
 **query_project** | [**list[str]**](str.md)| the project names to restrict returned list applications. | [optional] 
 **query_resource_version** | **str**| when specified with a watch call, shows changes that occur after that particular version of a resource. | [optional] 
 **query_selector** | **str**| the selector to to restrict returned list to applications only with matched labels. | [optional] 
 **query_repo** | **str**| the repoURL to restrict returned list applications. | [optional] 

### Return type

[**StreamResultOfApplicationsApplicationWatchEvent**](StreamResultOfApplicationsApplicationWatchEvent.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_application_service_watch_resource_tree**
> StreamResultOfApplicationsApplicationTree agent_application_service_watch_resource_tree(agent_identifier, query_application_name, account_identifier, org_identifier, project_identifier, query_namespace=query_namespace, query_name=query_name, query_version=query_version, query_group=query_group, query_kind=query_kind)

WatchResourceTree returns stream of application resource tree

WatchResourceTree returns stream of application resource tree.

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
api_instance = harness_python_sdk.ApplicationsApi(harness_python_sdk.ApiClient(configuration))
agent_identifier = 'agent_identifier_example' # str | Agent identifier for entity.
query_application_name = 'query_application_name_example' # str | 
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
query_namespace = 'query_namespace_example' # str |  (optional)
query_name = 'query_name_example' # str |  (optional)
query_version = 'query_version_example' # str |  (optional)
query_group = 'query_group_example' # str |  (optional)
query_kind = 'query_kind_example' # str |  (optional)

try:
    # WatchResourceTree returns stream of application resource tree
    api_response = api_instance.agent_application_service_watch_resource_tree(agent_identifier, query_application_name, account_identifier, org_identifier, project_identifier, query_namespace=query_namespace, query_name=query_name, query_version=query_version, query_group=query_group, query_kind=query_kind)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->agent_application_service_watch_resource_tree: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_identifier** | **str**| Agent identifier for entity. | 
 **query_application_name** | **str**|  | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **query_namespace** | **str**|  | [optional] 
 **query_name** | **str**|  | [optional] 
 **query_version** | **str**|  | [optional] 
 **query_group** | **str**|  | [optional] 
 **query_kind** | **str**|  | [optional] 

### Return type

[**StreamResultOfApplicationsApplicationTree**](StreamResultOfApplicationsApplicationTree.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_service_exists**
> bool application_service_exists(name, account_identifier, org_identifier, project_identifier, agent_identifier=agent_identifier)

Checks whether an app with the given name exists

Checks whether an app with the given name exists

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
api_instance = harness_python_sdk.ApplicationsApi(harness_python_sdk.ApiClient(configuration))
name = 'name_example' # str | 
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
agent_identifier = 'agent_identifier_example' # str | Agent identifier for entity. (optional)

try:
    # Checks whether an app with the given name exists
    api_response = api_instance.application_service_exists(name, account_identifier, org_identifier, project_identifier, agent_identifier=agent_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->application_service_exists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **agent_identifier** | **str**| Agent identifier for entity. | [optional] 

### Return type

**bool**

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_service_list_app_sync**
> V1ApplicationSyncStatuslist application_service_list_app_sync(body)

List returns list of application sync status

List returns list of application sync status

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
api_instance = harness_python_sdk.ApplicationsApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.V1ApplicationSyncStatusQuery() # V1ApplicationSyncStatusQuery | 

try:
    # List returns list of application sync status
    api_response = api_instance.application_service_list_app_sync(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->application_service_list_app_sync: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1ApplicationSyncStatusQuery**](V1ApplicationSyncStatusQuery.md)|  | 

### Return type

[**V1ApplicationSyncStatuslist**](V1ApplicationSyncStatuslist.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

