# swagger_client.RepositoriesApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**agent_repository_service_create_repository**](RepositoriesApi.md#agent_repository_service_create_repository) | **POST** /gitops/api/v1/agents/{agentIdentifier}/repositories | CreateRepository creates a new repository configuration
[**agent_repository_service_delete_repository**](RepositoriesApi.md#agent_repository_service_delete_repository) | **DELETE** /gitops/api/v1/agents/{agentIdentifier}/repositories/{identifier} | DeleteRepository deletes a repository from the configuration
[**agent_repository_service_get**](RepositoriesApi.md#agent_repository_service_get) | **GET** /gitops/api/v1/agents/{agentIdentifier}/repositories/{identifier} | Get returns a repository or its credentials
[**agent_repository_service_get_app_details**](RepositoriesApi.md#agent_repository_service_get_app_details) | **GET** /gitops/api/v1/agents/{agentIdentifier}/repositories/{identifier}/appdetails | GetAppDetails returns application details by given path
[**agent_repository_service_get_helm_charts**](RepositoriesApi.md#agent_repository_service_get_helm_charts) | **GET** /gitops/api/v1/agents/{agentIdentifier}/repositories/{identifier}/helmcharts | GetHelmCharts returns list of helm charts in the specified repository
[**agent_repository_service_list_apps**](RepositoriesApi.md#agent_repository_service_list_apps) | **GET** /gitops/api/v1/agents/{agentIdentifier}/repositories/{identifier}/apps | ListApps returns list of apps in the repo
[**agent_repository_service_list_refs**](RepositoriesApi.md#agent_repository_service_list_refs) | **GET** /gitops/api/v1/agents/{agentIdentifier}/repositories/{identifier}/refs | Returns a list of refs (e.g. branches and tags) in the repo
[**agent_repository_service_list_repositories**](RepositoriesApi.md#agent_repository_service_list_repositories) | **GET** /gitops/api/v1/agents/{agentIdentifier}/repositories | ListRepositories gets a list of all configured repositories
[**agent_repository_service_update_repository**](RepositoriesApi.md#agent_repository_service_update_repository) | **PUT** /gitops/api/v1/agents/{agentIdentifier}/repositories/{identifier} | UpdateRepository updates a repository configuration
[**agent_repository_service_validate_access**](RepositoriesApi.md#agent_repository_service_validate_access) | **POST** /gitops/api/v1/agents/{agentIdentifier}/repositories/validate | ValidateAccess gets connection state for a repository
[**repository_service_exists**](RepositoriesApi.md#repository_service_exists) | **GET** /gitops/api/v1/repositories/exists | Checks whether a repository with the given name exists
[**repository_service_list_repositories**](RepositoriesApi.md#repository_service_list_repositories) | **POST** /gitops/api/v1/repositories | List returns list of Repositories

# **agent_repository_service_create_repository**
> Servicev1Repository agent_repository_service_create_repository(body, agent_identifier, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, identifier=identifier, repo_creds_id=repo_creds_id)

CreateRepository creates a new repository configuration

CreateRepository creates a new repository configuration.

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
api_instance = swagger_client.RepositoriesApi(swagger_client.ApiClient(configuration))
body = swagger_client.RepositoriesRepoCreateRequest() # RepositoriesRepoCreateRequest | 
agent_identifier = 'agent_identifier_example' # str | Agent identifier for entity.
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity. (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
identifier = 'identifier_example' # str |  (optional)
repo_creds_id = 'repo_creds_id_example' # str |  (optional)

try:
    # CreateRepository creates a new repository configuration
    api_response = api_instance.agent_repository_service_create_repository(body, agent_identifier, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, identifier=identifier, repo_creds_id=repo_creds_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->agent_repository_service_create_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RepositoriesRepoCreateRequest**](RepositoriesRepoCreateRequest.md)|  | 
 **agent_identifier** | **str**| Agent identifier for entity. | 
 **account_identifier** | **str**| Account Identifier for the Entity. | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **identifier** | **str**|  | [optional] 
 **repo_creds_id** | **str**|  | [optional] 

### Return type

[**Servicev1Repository**](Servicev1Repository.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_repository_service_delete_repository**
> RepositoriesRepoResponse agent_repository_service_delete_repository(agent_identifier, identifier, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, query_repo=query_repo, query_force_refresh=query_force_refresh, query_project=query_project)

DeleteRepository deletes a repository from the configuration

DeleteRepository deletes a repository from the configuration.

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
api_instance = swagger_client.RepositoriesApi(swagger_client.ApiClient(configuration))
agent_identifier = 'agent_identifier_example' # str | Agent identifier for entity.
identifier = 'identifier_example' # str | 
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity. (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
query_repo = 'query_repo_example' # str | Repo URL for query. (optional)
query_force_refresh = true # bool | Whether to force a cache refresh on repo's connection state. (optional)
query_project = 'query_project_example' # str | The associated project project. (optional)

try:
    # DeleteRepository deletes a repository from the configuration
    api_response = api_instance.agent_repository_service_delete_repository(agent_identifier, identifier, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, query_repo=query_repo, query_force_refresh=query_force_refresh, query_project=query_project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->agent_repository_service_delete_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_identifier** | **str**| Agent identifier for entity. | 
 **identifier** | **str**|  | 
 **account_identifier** | **str**| Account Identifier for the Entity. | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **query_repo** | **str**| Repo URL for query. | [optional] 
 **query_force_refresh** | **bool**| Whether to force a cache refresh on repo&#x27;s connection state. | [optional] 
 **query_project** | **str**| The associated project project. | [optional] 

### Return type

[**RepositoriesRepoResponse**](RepositoriesRepoResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_repository_service_get**
> Servicev1Repository agent_repository_service_get(agent_identifier, identifier, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, query_repo=query_repo, query_force_refresh=query_force_refresh, query_project=query_project)

Get returns a repository or its credentials

Get returns a repository or its credentials.

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
api_instance = swagger_client.RepositoriesApi(swagger_client.ApiClient(configuration))
agent_identifier = 'agent_identifier_example' # str | Agent identifier for entity.
identifier = 'identifier_example' # str | 
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
query_repo = 'query_repo_example' # str | Repo URL for query. (optional)
query_force_refresh = true # bool | Whether to force a cache refresh on repo's connection state. (optional)
query_project = 'query_project_example' # str | The associated project project. (optional)

try:
    # Get returns a repository or its credentials
    api_response = api_instance.agent_repository_service_get(agent_identifier, identifier, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, query_repo=query_repo, query_force_refresh=query_force_refresh, query_project=query_project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->agent_repository_service_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_identifier** | **str**| Agent identifier for entity. | 
 **identifier** | **str**|  | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **query_repo** | **str**| Repo URL for query. | [optional] 
 **query_force_refresh** | **bool**| Whether to force a cache refresh on repo&#x27;s connection state. | [optional] 
 **query_project** | **str**| The associated project project. | [optional] 

### Return type

[**Servicev1Repository**](Servicev1Repository.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_repository_service_get_app_details**
> RepositoriesRepoAppDetailsResponse agent_repository_service_get_app_details(agent_identifier, identifier, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, query_source_repo_url=query_source_repo_url, query_source_path=query_source_path, query_source_target_revision=query_source_target_revision, query_source_helm_value_files=query_source_helm_value_files, query_source_helm_release_name=query_source_helm_release_name, query_source_helm_values=query_source_helm_values, query_source_helm_version=query_source_helm_version, query_source_helm_pass_credentials=query_source_helm_pass_credentials, query_source_kustomize_name_prefix=query_source_kustomize_name_prefix, query_source_kustomize_name_suffix=query_source_kustomize_name_suffix, query_source_kustomize_images=query_source_kustomize_images, query_source_kustomize_version=query_source_kustomize_version, query_source_kustomize_force_common_labels=query_source_kustomize_force_common_labels, query_source_kustomize_force_common_annotations=query_source_kustomize_force_common_annotations, query_source_ksonnet_environment=query_source_ksonnet_environment, query_source_directory_recurse=query_source_directory_recurse, query_source_directory_jsonnet_libs=query_source_directory_jsonnet_libs, query_source_directory_exclude=query_source_directory_exclude, query_source_directory_include=query_source_directory_include, query_source_plugin_name=query_source_plugin_name, query_source_chart=query_source_chart, query_app_name=query_app_name, query_app_project=query_app_project)

GetAppDetails returns application details by given path

GetAppDetails returns application details by given path.

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
api_instance = swagger_client.RepositoriesApi(swagger_client.ApiClient(configuration))
agent_identifier = 'agent_identifier_example' # str | Agent identifier for entity.
identifier = 'identifier_example' # str | 
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
query_source_repo_url = 'query_source_repo_url_example' # str | RepoURL is the URL to the repository (Git or Helm) that contains the application manifests. (optional)
query_source_path = 'query_source_path_example' # str | Path is a directory path within the Git repository, and is only valid for applications sourced from Git. (optional)
query_source_target_revision = 'query_source_target_revision_example' # str | TargetRevision defines the revision of the source to sync the application to. In case of Git, this can be commit, tag, or branch. If omitted, will equal to HEAD. In case of Helm, this is a semver tag for the Chart's version. (optional)
query_source_helm_value_files = ['query_source_helm_value_files_example'] # list[str] | ValuesFiles is a list of Helm value files to use when generating a template. (optional)
query_source_helm_release_name = 'query_source_helm_release_name_example' # str | ReleaseName is the Helm release name to use. If omitted it will use the application name. (optional)
query_source_helm_values = 'query_source_helm_values_example' # str | Values specifies Helm values to be passed to helm template, typically defined as a block. (optional)
query_source_helm_version = 'query_source_helm_version_example' # str | Version is the Helm version to use for templating (either \"2\" or \"3\"). (optional)
query_source_helm_pass_credentials = true # bool | PassCredentials pass credentials to all domains (Helm's --pass-credentials). (optional)
query_source_kustomize_name_prefix = 'query_source_kustomize_name_prefix_example' # str | NamePrefix is a prefix appended to resources for Kustomize apps. (optional)
query_source_kustomize_name_suffix = 'query_source_kustomize_name_suffix_example' # str | NameSuffix is a suffix appended to resources for Kustomize apps. (optional)
query_source_kustomize_images = ['query_source_kustomize_images_example'] # list[str] | Images is a list of Kustomize image override specifications. (optional)
query_source_kustomize_version = 'query_source_kustomize_version_example' # str | Version controls which version of Kustomize to use for rendering manifests. (optional)
query_source_kustomize_force_common_labels = true # bool | ForceCommonLabels specifies whether to force applying common labels to resources for Kustomize apps. (optional)
query_source_kustomize_force_common_annotations = true # bool | ForceCommonAnnotations specifies whether to force applying common annotations to resources for Kustomize apps. (optional)
query_source_ksonnet_environment = 'query_source_ksonnet_environment_example' # str | Environment is a ksonnet application environment name. (optional)
query_source_directory_recurse = true # bool | Recurse specifies whether to scan a directory recursively for manifests. (optional)
query_source_directory_jsonnet_libs = ['query_source_directory_jsonnet_libs_example'] # list[str] | Additional library search dirs. (optional)
query_source_directory_exclude = 'query_source_directory_exclude_example' # str | Exclude contains a glob pattern to match paths against that should be explicitly excluded from being used during manifest generation. (optional)
query_source_directory_include = 'query_source_directory_include_example' # str | Include contains a glob pattern to match paths against that should be explicitly included during manifest generation. (optional)
query_source_plugin_name = 'query_source_plugin_name_example' # str |  (optional)
query_source_chart = 'query_source_chart_example' # str | Chart is a Helm chart name, and must be specified for applications sourced from a Helm repo. (optional)
query_app_name = 'query_app_name_example' # str |  (optional)
query_app_project = 'query_app_project_example' # str |  (optional)

try:
    # GetAppDetails returns application details by given path
    api_response = api_instance.agent_repository_service_get_app_details(agent_identifier, identifier, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, query_source_repo_url=query_source_repo_url, query_source_path=query_source_path, query_source_target_revision=query_source_target_revision, query_source_helm_value_files=query_source_helm_value_files, query_source_helm_release_name=query_source_helm_release_name, query_source_helm_values=query_source_helm_values, query_source_helm_version=query_source_helm_version, query_source_helm_pass_credentials=query_source_helm_pass_credentials, query_source_kustomize_name_prefix=query_source_kustomize_name_prefix, query_source_kustomize_name_suffix=query_source_kustomize_name_suffix, query_source_kustomize_images=query_source_kustomize_images, query_source_kustomize_version=query_source_kustomize_version, query_source_kustomize_force_common_labels=query_source_kustomize_force_common_labels, query_source_kustomize_force_common_annotations=query_source_kustomize_force_common_annotations, query_source_ksonnet_environment=query_source_ksonnet_environment, query_source_directory_recurse=query_source_directory_recurse, query_source_directory_jsonnet_libs=query_source_directory_jsonnet_libs, query_source_directory_exclude=query_source_directory_exclude, query_source_directory_include=query_source_directory_include, query_source_plugin_name=query_source_plugin_name, query_source_chart=query_source_chart, query_app_name=query_app_name, query_app_project=query_app_project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->agent_repository_service_get_app_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_identifier** | **str**| Agent identifier for entity. | 
 **identifier** | **str**|  | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **query_source_repo_url** | **str**| RepoURL is the URL to the repository (Git or Helm) that contains the application manifests. | [optional] 
 **query_source_path** | **str**| Path is a directory path within the Git repository, and is only valid for applications sourced from Git. | [optional] 
 **query_source_target_revision** | **str**| TargetRevision defines the revision of the source to sync the application to. In case of Git, this can be commit, tag, or branch. If omitted, will equal to HEAD. In case of Helm, this is a semver tag for the Chart&#x27;s version. | [optional] 
 **query_source_helm_value_files** | [**list[str]**](str.md)| ValuesFiles is a list of Helm value files to use when generating a template. | [optional] 
 **query_source_helm_release_name** | **str**| ReleaseName is the Helm release name to use. If omitted it will use the application name. | [optional] 
 **query_source_helm_values** | **str**| Values specifies Helm values to be passed to helm template, typically defined as a block. | [optional] 
 **query_source_helm_version** | **str**| Version is the Helm version to use for templating (either \&quot;2\&quot; or \&quot;3\&quot;). | [optional] 
 **query_source_helm_pass_credentials** | **bool**| PassCredentials pass credentials to all domains (Helm&#x27;s --pass-credentials). | [optional] 
 **query_source_kustomize_name_prefix** | **str**| NamePrefix is a prefix appended to resources for Kustomize apps. | [optional] 
 **query_source_kustomize_name_suffix** | **str**| NameSuffix is a suffix appended to resources for Kustomize apps. | [optional] 
 **query_source_kustomize_images** | [**list[str]**](str.md)| Images is a list of Kustomize image override specifications. | [optional] 
 **query_source_kustomize_version** | **str**| Version controls which version of Kustomize to use for rendering manifests. | [optional] 
 **query_source_kustomize_force_common_labels** | **bool**| ForceCommonLabels specifies whether to force applying common labels to resources for Kustomize apps. | [optional] 
 **query_source_kustomize_force_common_annotations** | **bool**| ForceCommonAnnotations specifies whether to force applying common annotations to resources for Kustomize apps. | [optional] 
 **query_source_ksonnet_environment** | **str**| Environment is a ksonnet application environment name. | [optional] 
 **query_source_directory_recurse** | **bool**| Recurse specifies whether to scan a directory recursively for manifests. | [optional] 
 **query_source_directory_jsonnet_libs** | [**list[str]**](str.md)| Additional library search dirs. | [optional] 
 **query_source_directory_exclude** | **str**| Exclude contains a glob pattern to match paths against that should be explicitly excluded from being used during manifest generation. | [optional] 
 **query_source_directory_include** | **str**| Include contains a glob pattern to match paths against that should be explicitly included during manifest generation. | [optional] 
 **query_source_plugin_name** | **str**|  | [optional] 
 **query_source_chart** | **str**| Chart is a Helm chart name, and must be specified for applications sourced from a Helm repo. | [optional] 
 **query_app_name** | **str**|  | [optional] 
 **query_app_project** | **str**|  | [optional] 

### Return type

[**RepositoriesRepoAppDetailsResponse**](RepositoriesRepoAppDetailsResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_repository_service_get_helm_charts**
> RepositoriesHelmChartsResponse agent_repository_service_get_helm_charts(agent_identifier, identifier, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, query_repo=query_repo, query_force_refresh=query_force_refresh, query_project=query_project)

GetHelmCharts returns list of helm charts in the specified repository

GetHelmCharts returns list of helm charts in the specified repository.

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
api_instance = swagger_client.RepositoriesApi(swagger_client.ApiClient(configuration))
agent_identifier = 'agent_identifier_example' # str | Agent identifier for entity.
identifier = 'identifier_example' # str | 
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
query_repo = 'query_repo_example' # str | Repo URL for query. (optional)
query_force_refresh = true # bool | Whether to force a cache refresh on repo's connection state. (optional)
query_project = 'query_project_example' # str | The associated project project. (optional)

try:
    # GetHelmCharts returns list of helm charts in the specified repository
    api_response = api_instance.agent_repository_service_get_helm_charts(agent_identifier, identifier, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, query_repo=query_repo, query_force_refresh=query_force_refresh, query_project=query_project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->agent_repository_service_get_helm_charts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_identifier** | **str**| Agent identifier for entity. | 
 **identifier** | **str**|  | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **query_repo** | **str**| Repo URL for query. | [optional] 
 **query_force_refresh** | **bool**| Whether to force a cache refresh on repo&#x27;s connection state. | [optional] 
 **query_project** | **str**| The associated project project. | [optional] 

### Return type

[**RepositoriesHelmChartsResponse**](RepositoriesHelmChartsResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_repository_service_list_apps**
> RepositoriesRepoAppsResponse agent_repository_service_list_apps(agent_identifier, identifier, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, query_repo=query_repo, query_revision=query_revision, query_app_name=query_app_name, query_app_project=query_app_project)

ListApps returns list of apps in the repo

ListApps returns list of apps in the repo.

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
api_instance = swagger_client.RepositoriesApi(swagger_client.ApiClient(configuration))
agent_identifier = 'agent_identifier_example' # str | Agent identifier for entity.
identifier = 'identifier_example' # str | 
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
query_repo = 'query_repo_example' # str |  (optional)
query_revision = 'query_revision_example' # str |  (optional)
query_app_name = 'query_app_name_example' # str |  (optional)
query_app_project = 'query_app_project_example' # str |  (optional)

try:
    # ListApps returns list of apps in the repo
    api_response = api_instance.agent_repository_service_list_apps(agent_identifier, identifier, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, query_repo=query_repo, query_revision=query_revision, query_app_name=query_app_name, query_app_project=query_app_project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->agent_repository_service_list_apps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_identifier** | **str**| Agent identifier for entity. | 
 **identifier** | **str**|  | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **query_repo** | **str**|  | [optional] 
 **query_revision** | **str**|  | [optional] 
 **query_app_name** | **str**|  | [optional] 
 **query_app_project** | **str**|  | [optional] 

### Return type

[**RepositoriesRepoAppsResponse**](RepositoriesRepoAppsResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_repository_service_list_refs**
> RepositoriesRefs agent_repository_service_list_refs(agent_identifier, identifier, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, query_repo=query_repo, query_force_refresh=query_force_refresh, query_project=query_project)

Returns a list of refs (e.g. branches and tags) in the repo

Returns a list of refs (e.g. branches and tags) in the repo.

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
api_instance = swagger_client.RepositoriesApi(swagger_client.ApiClient(configuration))
agent_identifier = 'agent_identifier_example' # str | Agent identifier for entity.
identifier = 'identifier_example' # str | 
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
query_repo = 'query_repo_example' # str | Repo URL for query. (optional)
query_force_refresh = true # bool | Whether to force a cache refresh on repo's connection state. (optional)
query_project = 'query_project_example' # str | The associated project project. (optional)

try:
    # Returns a list of refs (e.g. branches and tags) in the repo
    api_response = api_instance.agent_repository_service_list_refs(agent_identifier, identifier, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, query_repo=query_repo, query_force_refresh=query_force_refresh, query_project=query_project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->agent_repository_service_list_refs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_identifier** | **str**| Agent identifier for entity. | 
 **identifier** | **str**|  | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **query_repo** | **str**| Repo URL for query. | [optional] 
 **query_force_refresh** | **bool**| Whether to force a cache refresh on repo&#x27;s connection state. | [optional] 
 **query_project** | **str**| The associated project project. | [optional] 

### Return type

[**RepositoriesRefs**](RepositoriesRefs.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_repository_service_list_repositories**
> RepositoriesRepositoryList agent_repository_service_list_repositories(agent_identifier, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, identifier=identifier, query_repo=query_repo, query_force_refresh=query_force_refresh, query_project=query_project)

ListRepositories gets a list of all configured repositories

ListRepositories gets a list of all configured repositories.

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
api_instance = swagger_client.RepositoriesApi(swagger_client.ApiClient(configuration))
agent_identifier = 'agent_identifier_example' # str | Agent identifier for entity.
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
identifier = 'identifier_example' # str |  (optional)
query_repo = 'query_repo_example' # str | Repo URL for query. (optional)
query_force_refresh = true # bool | Whether to force a cache refresh on repo's connection state. (optional)
query_project = 'query_project_example' # str | The associated project project. (optional)

try:
    # ListRepositories gets a list of all configured repositories
    api_response = api_instance.agent_repository_service_list_repositories(agent_identifier, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, identifier=identifier, query_repo=query_repo, query_force_refresh=query_force_refresh, query_project=query_project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->agent_repository_service_list_repositories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_identifier** | **str**| Agent identifier for entity. | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **identifier** | **str**|  | [optional] 
 **query_repo** | **str**| Repo URL for query. | [optional] 
 **query_force_refresh** | **bool**| Whether to force a cache refresh on repo&#x27;s connection state. | [optional] 
 **query_project** | **str**| The associated project project. | [optional] 

### Return type

[**RepositoriesRepositoryList**](RepositoriesRepositoryList.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_repository_service_update_repository**
> Servicev1Repository agent_repository_service_update_repository(body, agent_identifier, identifier, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)

UpdateRepository updates a repository configuration

UpdateRepository updates a repository configuration.

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
api_instance = swagger_client.RepositoriesApi(swagger_client.ApiClient(configuration))
body = swagger_client.RepositoriesRepoUpdateRequest() # RepositoriesRepoUpdateRequest | 
agent_identifier = 'agent_identifier_example' # str | Agent identifier for entity.
identifier = 'identifier_example' # str | 
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity. (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # UpdateRepository updates a repository configuration
    api_response = api_instance.agent_repository_service_update_repository(body, agent_identifier, identifier, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->agent_repository_service_update_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RepositoriesRepoUpdateRequest**](RepositoriesRepoUpdateRequest.md)|  | 
 **agent_identifier** | **str**| Agent identifier for entity. | 
 **identifier** | **str**|  | 
 **account_identifier** | **str**| Account Identifier for the Entity. | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**Servicev1Repository**](Servicev1Repository.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_repository_service_validate_access**
> CommonsConnectionState agent_repository_service_validate_access(body, account_identifier, agent_identifier, org_identifier=org_identifier, project_identifier=project_identifier, identifier=identifier)

ValidateAccess gets connection state for a repository

ValidateAccess gets connection state for a repository.

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
api_instance = swagger_client.RepositoriesApi(swagger_client.ApiClient(configuration))
body = swagger_client.RepositoriesRepoAccessQuery() # RepositoriesRepoAccessQuery | 
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
agent_identifier = 'agent_identifier_example' # str | Agent identifier for entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
identifier = 'identifier_example' # str |  (optional)

try:
    # ValidateAccess gets connection state for a repository
    api_response = api_instance.agent_repository_service_validate_access(body, account_identifier, agent_identifier, org_identifier=org_identifier, project_identifier=project_identifier, identifier=identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->agent_repository_service_validate_access: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RepositoriesRepoAccessQuery**](RepositoriesRepoAccessQuery.md)|  | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **agent_identifier** | **str**| Agent identifier for entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **identifier** | **str**|  | [optional] 

### Return type

[**CommonsConnectionState**](CommonsConnectionState.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repository_service_exists**
> bool repository_service_exists(account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, agent_identifier=agent_identifier, url=url)

Checks whether a repository with the given name exists

Checks whether a repository with the given name exists.

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
api_instance = swagger_client.RepositoriesApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
agent_identifier = 'agent_identifier_example' # str | Agent identifier for entity. (optional)
url = 'url_example' # str |  (optional)

try:
    # Checks whether a repository with the given name exists
    api_response = api_instance.repository_service_exists(account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, agent_identifier=agent_identifier, url=url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->repository_service_exists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **agent_identifier** | **str**| Agent identifier for entity. | [optional] 
 **url** | **str**|  | [optional] 

### Return type

**bool**

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repository_service_list_repositories**
> V1Repositorylist repository_service_list_repositories(body)

List returns list of Repositories

List returns list of Repositories

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
api_instance = swagger_client.RepositoriesApi(swagger_client.ApiClient(configuration))
body = swagger_client.V1RepositoryQuery() # V1RepositoryQuery | 

try:
    # List returns list of Repositories
    api_response = api_instance.repository_service_list_repositories(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->repository_service_list_repositories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1RepositoryQuery**](V1RepositoryQuery.md)|  | 

### Return type

[**V1Repositorylist**](V1Repositorylist.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

