# swagger_client.PipelinesApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_pipeline**](PipelinesApi.md#create_pipeline) | **POST** /v1/orgs/{org}/projects/{project}/pipelines | Create a Pipeline
[**delete_pipeline**](PipelinesApi.md#delete_pipeline) | **DELETE** /v1/orgs/{org}/projects/{project}/pipelines/{pipeline} | Delete a Pipeline
[**get_pipeline**](PipelinesApi.md#get_pipeline) | **GET** /v1/orgs/{org}/projects/{project}/pipelines/{pipeline} | Retrieve a Pipeline
[**import_pipeline_from_git**](PipelinesApi.md#import_pipeline_from_git) | **POST** /v1/orgs/{org}/projects/{project}/pipelines/{pipeline}/import | Get Pipeline YAML from Git Repository
[**list_pipelines**](PipelinesApi.md#list_pipelines) | **GET** /v1/orgs/{org}/projects/{project}/pipelines | List Pipelines
[**move_config**](PipelinesApi.md#move_config) | **POST** /v1/orgs/{org}/projects/{project}/pipelines/{pipeline}/move-config | Move Pipeline YAML from inline to remote
[**update_pipeline**](PipelinesApi.md#update_pipeline) | **PUT** /v1/orgs/{org}/projects/{project}/pipelines/{pipeline} | Update a Pipeline
[**update_pipeline_git_metadata**](PipelinesApi.md#update_pipeline_git_metadata) | **PUT** /v1/orgs/{org}/projects/{project}/pipelines/{pipeline}/git-metadata | Update GitMetadata for Remote Pipelines

# **create_pipeline**
> PipelineCreateResponseBody create_pipeline(body, org, project, harness_account=harness_account)

Create a Pipeline

Creates a Pipeline.

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
api_instance = swagger_client.PipelinesApi(swagger_client.ApiClient(configuration))
body = swagger_client.PipelineCreateRequestBody() # PipelineCreateRequestBody | Pipeline request body
org = 'org_example' # str | Organization identifier
project = 'project_example' # str | Project identifier
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)

try:
    # Create a Pipeline
    api_response = api_instance.create_pipeline(body, org, project, harness_account=harness_account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelinesApi->create_pipeline: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PipelineCreateRequestBody**](PipelineCreateRequestBody.md)| Pipeline request body | 
 **org** | **str**| Organization identifier | 
 **project** | **str**| Project identifier | 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 

### Return type

[**PipelineCreateResponseBody**](PipelineCreateResponseBody.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pipeline**
> delete_pipeline(org, project, pipeline, harness_account=harness_account)

Delete a Pipeline

Deletes a Pipeline.

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
api_instance = swagger_client.PipelinesApi(swagger_client.ApiClient(configuration))
org = 'org_example' # str | Organization identifier
project = 'project_example' # str | Project identifier
pipeline = 'pipeline_example' # str | Pipeline identifier
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)

try:
    # Delete a Pipeline
    api_instance.delete_pipeline(org, project, pipeline, harness_account=harness_account)
except ApiException as e:
    print("Exception when calling PipelinesApi->delete_pipeline: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| Organization identifier | 
 **project** | **str**| Project identifier | 
 **pipeline** | **str**| Pipeline identifier | 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pipeline**
> PipelineGetResponseBody get_pipeline(org, project, pipeline, harness_account=harness_account, branch_name=branch_name, template_applied=template_applied, connector_ref=connector_ref, repo_name=repo_name, load_from_cache=load_from_cache, load_from_fallback_branch=load_from_fallback_branch, validate_async=validate_async)

Retrieve a Pipeline

Retrieves a Pipeline.

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
api_instance = swagger_client.PipelinesApi(swagger_client.ApiClient(configuration))
org = 'org_example' # str | Organization identifier
project = 'project_example' # str | Project identifier
pipeline = 'pipeline_example' # str | Pipeline identifier
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)
branch_name = 'branch_name_example' # str | Name of the branch (for Git Experience). (optional)
template_applied = false # bool | If true, returns Pipeline YAML with Templates applied on it. (optional) (default to false)
connector_ref = 'connector_ref_example' # str | Identifier of the Harness Connector used for CRUD operations on the Entity (for Git Experience). (optional)
repo_name = 'repo_name_example' # str | Name of the repository (for Git Experience). (optional)
load_from_cache = 'false' # str | Flag to enable loading the remote pipeline from git or git cache (optional) (default to false)
load_from_fallback_branch = false # bool | Flag to load the pipeline from the created non default branch (optional) (default to false)
validate_async = false # bool | Flag to tell whether to start an asynchronous validation process or not (optional) (default to false)

try:
    # Retrieve a Pipeline
    api_response = api_instance.get_pipeline(org, project, pipeline, harness_account=harness_account, branch_name=branch_name, template_applied=template_applied, connector_ref=connector_ref, repo_name=repo_name, load_from_cache=load_from_cache, load_from_fallback_branch=load_from_fallback_branch, validate_async=validate_async)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelinesApi->get_pipeline: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| Organization identifier | 
 **project** | **str**| Project identifier | 
 **pipeline** | **str**| Pipeline identifier | 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 
 **branch_name** | **str**| Name of the branch (for Git Experience). | [optional] 
 **template_applied** | **bool**| If true, returns Pipeline YAML with Templates applied on it. | [optional] [default to false]
 **connector_ref** | **str**| Identifier of the Harness Connector used for CRUD operations on the Entity (for Git Experience). | [optional] 
 **repo_name** | **str**| Name of the repository (for Git Experience). | [optional] 
 **load_from_cache** | **str**| Flag to enable loading the remote pipeline from git or git cache | [optional] [default to false]
 **load_from_fallback_branch** | **bool**| Flag to load the pipeline from the created non default branch | [optional] [default to false]
 **validate_async** | **bool**| Flag to tell whether to start an asynchronous validation process or not | [optional] [default to false]

### Return type

[**PipelineGetResponseBody**](PipelineGetResponseBody.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_pipeline_from_git**
> PipelineSaveResponseBody import_pipeline_from_git(org, project, pipeline, body=body, harness_account=harness_account)

Get Pipeline YAML from Git Repository

Fetches Pipeline YAML from Git Repository and saves a record for it in Harness

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
api_instance = swagger_client.PipelinesApi(swagger_client.ApiClient(configuration))
org = 'org_example' # str | Organization identifier
project = 'project_example' # str | Project identifier
pipeline = 'pipeline_example' # str | Pipeline identifier
body = swagger_client.PipelineImportRequestBody() # PipelineImportRequestBody | Pipeline import request body (optional)
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)

try:
    # Get Pipeline YAML from Git Repository
    api_response = api_instance.import_pipeline_from_git(org, project, pipeline, body=body, harness_account=harness_account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelinesApi->import_pipeline_from_git: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| Organization identifier | 
 **project** | **str**| Project identifier | 
 **pipeline** | **str**| Pipeline identifier | 
 **body** | [**PipelineImportRequestBody**](PipelineImportRequestBody.md)| Pipeline import request body | [optional] 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 

### Return type

[**PipelineSaveResponseBody**](PipelineSaveResponseBody.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_pipelines**
> list[PipelineListResponseBody] list_pipelines(org, project, harness_account=harness_account, page=page, limit=limit, search_term=search_term, sort=sort, order=order, module=module, filter_identifier=filter_identifier, pipeline_identifiers=pipeline_identifiers, name=name, description=description, tags=tags, service_names=service_names, env_names=env_names, deployment_type=deployment_type, repository=repository)

List Pipelines

Returns a list of Pipelines.

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
api_instance = swagger_client.PipelinesApi(swagger_client.ApiClient(configuration))
org = 'org_example' # str | Organization identifier
project = 'project_example' # str | Project identifier
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)
page = 0 # int | Pagination page number strategy: Specify the page number within the paginated collection related to the number of items on each page. (optional) (default to 0)
limit = 30 # int | Pagination: Number of items to return. (optional) (default to 30)
search_term = 'search_term_example' # str | This would be used to filter resources having attributes matching the search term. (optional)
sort = 'sort_example' # str | Parameter on the basis of which sorting is done. (optional)
order = 'order_example' # str | Order on the basis of which sorting is done. (optional)
module = 'module_example' # str | Harness module which is part of the Pipeline. (optional)
filter_identifier = 'filter_identifier_example' # str | Identifier of a saved Filter. (optional)
pipeline_identifiers = ['pipeline_identifiers_example'] # list[str] | List of Pipeline identifiers on the basis of which the Pipelines are filtered. (optional)
name = 'name_example' # str | Pipeline Name on the basis of which the Pipelines are filtered. (optional)
description = 'description_example' # str | Pipeline Description on the basis of which the Pipelines are filtered. (optional)
tags = ['tags_example'] # list[str] | Filter tags as a key:value pair. (optional)
service_names = ['service_names_example'] # list[str] | Service names on the basis of which the Pipelines are filtered. [CD] (optional)
env_names = ['env_names_example'] # list[str] | Names of Environments on the basis of which the Pipelines are filtered. [CD] (optional)
deployment_type = 'deployment_type_example' # str | Deployment type on the basis of which the Pipelines are filtered. [CD] (optional)
repository = 'repository_example' # str | Repository name on the basis of which the Pipelines are filtered. [CI] (optional)

try:
    # List Pipelines
    api_response = api_instance.list_pipelines(org, project, harness_account=harness_account, page=page, limit=limit, search_term=search_term, sort=sort, order=order, module=module, filter_identifier=filter_identifier, pipeline_identifiers=pipeline_identifiers, name=name, description=description, tags=tags, service_names=service_names, env_names=env_names, deployment_type=deployment_type, repository=repository)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelinesApi->list_pipelines: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| Organization identifier | 
 **project** | **str**| Project identifier | 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 
 **page** | **int**| Pagination page number strategy: Specify the page number within the paginated collection related to the number of items on each page. | [optional] [default to 0]
 **limit** | **int**| Pagination: Number of items to return. | [optional] [default to 30]
 **search_term** | **str**| This would be used to filter resources having attributes matching the search term. | [optional] 
 **sort** | **str**| Parameter on the basis of which sorting is done. | [optional] 
 **order** | **str**| Order on the basis of which sorting is done. | [optional] 
 **module** | **str**| Harness module which is part of the Pipeline. | [optional] 
 **filter_identifier** | **str**| Identifier of a saved Filter. | [optional] 
 **pipeline_identifiers** | [**list[str]**](str.md)| List of Pipeline identifiers on the basis of which the Pipelines are filtered. | [optional] 
 **name** | **str**| Pipeline Name on the basis of which the Pipelines are filtered. | [optional] 
 **description** | **str**| Pipeline Description on the basis of which the Pipelines are filtered. | [optional] 
 **tags** | [**list[str]**](str.md)| Filter tags as a key:value pair. | [optional] 
 **service_names** | [**list[str]**](str.md)| Service names on the basis of which the Pipelines are filtered. [CD] | [optional] 
 **env_names** | [**list[str]**](str.md)| Names of Environments on the basis of which the Pipelines are filtered. [CD] | [optional] 
 **deployment_type** | **str**| Deployment type on the basis of which the Pipelines are filtered. [CD] | [optional] 
 **repository** | **str**| Repository name on the basis of which the Pipelines are filtered. [CI] | [optional] 

### Return type

[**list[PipelineListResponseBody]**](PipelineListResponseBody.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_config**
> PipelineMoveConfigResponseBody move_config(org, project, pipeline, body=body, harness_account=harness_account)

Move Pipeline YAML from inline to remote

Creates a remote entity by fetching pipeline YAML from Harness.

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
api_instance = swagger_client.PipelinesApi(swagger_client.ApiClient(configuration))
org = 'org_example' # str | Organization identifier
project = 'project_example' # str | Project identifier
pipeline = 'pipeline_example' # str | Pipeline identifier
body = swagger_client.PipelineMoveConfigRequestBody() # PipelineMoveConfigRequestBody |  (optional)
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)

try:
    # Move Pipeline YAML from inline to remote
    api_response = api_instance.move_config(org, project, pipeline, body=body, harness_account=harness_account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelinesApi->move_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| Organization identifier | 
 **project** | **str**| Project identifier | 
 **pipeline** | **str**| Pipeline identifier | 
 **body** | [**PipelineMoveConfigRequestBody**](PipelineMoveConfigRequestBody.md)|  | [optional] 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 

### Return type

[**PipelineMoveConfigResponseBody**](PipelineMoveConfigResponseBody.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pipeline**
> PipelineCreateResponseBody update_pipeline(body, org, project, pipeline, harness_account=harness_account)

Update a Pipeline

Updates a Pipeline.

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
api_instance = swagger_client.PipelinesApi(swagger_client.ApiClient(configuration))
body = swagger_client.PipelineUpdateRequestBody() # PipelineUpdateRequestBody | Pipeline request body
org = 'org_example' # str | Organization identifier
project = 'project_example' # str | Project identifier
pipeline = 'pipeline_example' # str | Pipeline identifier
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)

try:
    # Update a Pipeline
    api_response = api_instance.update_pipeline(body, org, project, pipeline, harness_account=harness_account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelinesApi->update_pipeline: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PipelineUpdateRequestBody**](PipelineUpdateRequestBody.md)| Pipeline request body | 
 **org** | **str**| Organization identifier | 
 **project** | **str**| Project identifier | 
 **pipeline** | **str**| Pipeline identifier | 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 

### Return type

[**PipelineCreateResponseBody**](PipelineCreateResponseBody.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pipeline_git_metadata**
> GitMetadataUpdateResponseBody update_pipeline_git_metadata(org, project, pipeline, body=body, harness_account=harness_account)

Update GitMetadata for Remote Pipelines

Update git-metadata in remote pipeline

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
api_instance = swagger_client.PipelinesApi(swagger_client.ApiClient(configuration))
org = 'org_example' # str | Organization identifier
project = 'project_example' # str | Project identifier
pipeline = 'pipeline_example' # str | Pipeline identifier
body = swagger_client.GitMetadataUpdateRequestBody() # GitMetadataUpdateRequestBody |  (optional)
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)

try:
    # Update GitMetadata for Remote Pipelines
    api_response = api_instance.update_pipeline_git_metadata(org, project, pipeline, body=body, harness_account=harness_account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelinesApi->update_pipeline_git_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| Organization identifier | 
 **project** | **str**| Project identifier | 
 **pipeline** | **str**| Pipeline identifier | 
 **body** | [**GitMetadataUpdateRequestBody**](GitMetadataUpdateRequestBody.md)|  | [optional] 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 

### Return type

[**GitMetadataUpdateResponseBody**](GitMetadataUpdateResponseBody.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

