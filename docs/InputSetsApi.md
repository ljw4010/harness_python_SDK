# harness_python_sdk.InputSetsApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_input_set**](InputSetsApi.md#create_input_set) | **POST** /v1/orgs/{org}/projects/{project}/input-sets | Create an Input Set
[**delete_input_set**](InputSetsApi.md#delete_input_set) | **DELETE** /v1/orgs/{org}/projects/{project}/input-sets/{input-set} | Delete an Input Set
[**get_input_set**](InputSetsApi.md#get_input_set) | **GET** /v1/orgs/{org}/projects/{project}/input-sets/{input-set} | Retrieve an Input Set
[**import_input_set_from_git**](InputSetsApi.md#import_input_set_from_git) | **POST** /v1/orgs/{org}/projects/{project}/input-sets/{input-set}/import | Get Input Set YAML from Git Repository
[**input_sets_move_config**](InputSetsApi.md#input_sets_move_config) | **POST** /v1/orgs/{org}/projects/{project}/input-sets/{input-set}/move-config | Move InputSet YAML from inline to remote
[**list_input_sets**](InputSetsApi.md#list_input_sets) | **GET** /v1/orgs/{org}/projects/{project}/input-sets | List Input Sets
[**update_input_set**](InputSetsApi.md#update_input_set) | **PUT** /v1/orgs/{org}/projects/{project}/input-sets/{input-set} | Update an Input Set
[**update_input_set_git_metadata**](InputSetsApi.md#update_input_set_git_metadata) | **PUT** /v1/orgs/{org}/projects/{project}/input-sets/{input-set}/git-metadata | Update GitMetadata for Remote InputSet

# **create_input_set**
> InputSetResponseBody create_input_set(body, pipeline, org, project, harness_account=harness_account)

Create an Input Set

Creates an Input Set for a Pipeline.

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
api_instance = harness_python_sdk.InputSetsApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.InputSetCreateRequestBody() # InputSetCreateRequestBody | Input Set create request body.
pipeline = 'pipeline_example' # str | Pipeline identifier for the Input Set.
org = 'org_example' # str | Organization identifier
project = 'project_example' # str | Project identifier
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)

try:
    # Create an Input Set
    api_response = api_instance.create_input_set(body, pipeline, org, project, harness_account=harness_account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InputSetsApi->create_input_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InputSetCreateRequestBody**](InputSetCreateRequestBody.md)| Input Set create request body. | 
 **pipeline** | **str**| Pipeline identifier for the Input Set. | 
 **org** | **str**| Organization identifier | 
 **project** | **str**| Project identifier | 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 

### Return type

[**InputSetResponseBody**](InputSetResponseBody.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_input_set**
> delete_input_set(org, project, input_set, pipeline, harness_account=harness_account)

Delete an Input Set

Deletes an Input Set for a Pipeline.

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
api_instance = harness_python_sdk.InputSetsApi(harness_python_sdk.ApiClient(configuration))
org = 'org_example' # str | Organization identifier
project = 'project_example' # str | Project identifier
input_set = 'input_set_example' # str | Input Set identifier
pipeline = 'pipeline_example' # str | Pipeline identifier for the Input Set.
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)

try:
    # Delete an Input Set
    api_instance.delete_input_set(org, project, input_set, pipeline, harness_account=harness_account)
except ApiException as e:
    print("Exception when calling InputSetsApi->delete_input_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| Organization identifier | 
 **project** | **str**| Project identifier | 
 **input_set** | **str**| Input Set identifier | 
 **pipeline** | **str**| Pipeline identifier for the Input Set. | 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_input_set**
> InputSetResponseBody get_input_set(org, project, input_set, pipeline, harness_account=harness_account, branch_name=branch_name, parent_entity_connector_ref=parent_entity_connector_ref, parent_entity_repo_name=parent_entity_repo_name, load_from_fallback_branch=load_from_fallback_branch, load_from_cache=load_from_cache)

Retrieve an Input Set

Retrieves an Input Set for a Pipeline.

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
api_instance = harness_python_sdk.InputSetsApi(harness_python_sdk.ApiClient(configuration))
org = 'org_example' # str | Organization identifier
project = 'project_example' # str | Project identifier
input_set = 'input_set_example' # str | Input Set identifier
pipeline = 'pipeline_example' # str | Pipeline identifier for the Input Set.
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)
branch_name = 'branch_name_example' # str | Name of the branch (for Git Experience). (optional)
parent_entity_connector_ref = 'parent_entity_connector_ref_example' # str | Connector reference for Parent Entity (Pipeline). (optional)
parent_entity_repo_name = 'parent_entity_repo_name_example' # str | Repository name for Parent Entity (Pipeline). (optional)
load_from_fallback_branch = false # bool | Flag to load the pipeline from the created non default branch (optional) (default to false)
load_from_cache = 'false' # str | Specifies whether the remote pipeline should be loaded from Git or Git cache. (optional) (default to false)

try:
    # Retrieve an Input Set
    api_response = api_instance.get_input_set(org, project, input_set, pipeline, harness_account=harness_account, branch_name=branch_name, parent_entity_connector_ref=parent_entity_connector_ref, parent_entity_repo_name=parent_entity_repo_name, load_from_fallback_branch=load_from_fallback_branch, load_from_cache=load_from_cache)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InputSetsApi->get_input_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| Organization identifier | 
 **project** | **str**| Project identifier | 
 **input_set** | **str**| Input Set identifier | 
 **pipeline** | **str**| Pipeline identifier for the Input Set. | 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 
 **branch_name** | **str**| Name of the branch (for Git Experience). | [optional] 
 **parent_entity_connector_ref** | **str**| Connector reference for Parent Entity (Pipeline). | [optional] 
 **parent_entity_repo_name** | **str**| Repository name for Parent Entity (Pipeline). | [optional] 
 **load_from_fallback_branch** | **bool**| Flag to load the pipeline from the created non default branch | [optional] [default to false]
 **load_from_cache** | **str**| Specifies whether the remote pipeline should be loaded from Git or Git cache. | [optional] [default to false]

### Return type

[**InputSetResponseBody**](InputSetResponseBody.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_input_set_from_git**
> InputSetImportResponseBody import_input_set_from_git(pipeline, org, project, input_set, body=body, harness_account=harness_account)

Get Input Set YAML from Git Repository

Fetches InputSet YAML from Git Repository and saves a record for it in Harness

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
api_instance = harness_python_sdk.InputSetsApi(harness_python_sdk.ApiClient(configuration))
pipeline = 'pipeline_example' # str | Pipeline identifier for the Input Set.
org = 'org_example' # str | Organization identifier
project = 'project_example' # str | Project identifier
input_set = 'input_set_example' # str | Input Set identifier
body = harness_python_sdk.InputSetImportRequestBody() # InputSetImportRequestBody | Input Set import request body (optional)
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)

try:
    # Get Input Set YAML from Git Repository
    api_response = api_instance.import_input_set_from_git(pipeline, org, project, input_set, body=body, harness_account=harness_account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InputSetsApi->import_input_set_from_git: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline** | **str**| Pipeline identifier for the Input Set. | 
 **org** | **str**| Organization identifier | 
 **project** | **str**| Project identifier | 
 **input_set** | **str**| Input Set identifier | 
 **body** | [**InputSetImportRequestBody**](InputSetImportRequestBody.md)| Input Set import request body | [optional] 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 

### Return type

[**InputSetImportResponseBody**](InputSetImportResponseBody.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **input_sets_move_config**
> InputSetMoveConfigResponseBody input_sets_move_config(org, project, input_set, body=body, harness_account=harness_account)

Move InputSet YAML from inline to remote

Creates a remote entity by fetching the input set YAML from Harness.

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
api_instance = harness_python_sdk.InputSetsApi(harness_python_sdk.ApiClient(configuration))
org = 'org_example' # str | Organization identifier
project = 'project_example' # str | Project identifier
input_set = 'input_set_example' # str | Input Set identifier
body = harness_python_sdk.InputSetMoveConfigRequestBody() # InputSetMoveConfigRequestBody |  (optional)
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)

try:
    # Move InputSet YAML from inline to remote
    api_response = api_instance.input_sets_move_config(org, project, input_set, body=body, harness_account=harness_account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InputSetsApi->input_sets_move_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| Organization identifier | 
 **project** | **str**| Project identifier | 
 **input_set** | **str**| Input Set identifier | 
 **body** | [**InputSetMoveConfigRequestBody**](InputSetMoveConfigRequestBody.md)|  | [optional] 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 

### Return type

[**InputSetMoveConfigResponseBody**](InputSetMoveConfigResponseBody.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_input_sets**
> list[InputSetResponseBody] list_input_sets(org, project, pipeline, harness_account=harness_account, page=page, limit=limit, search_term=search_term, sort=sort, order=order)

List Input Sets

Returns a List of Input Sets for a Pipeline.

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
api_instance = harness_python_sdk.InputSetsApi(harness_python_sdk.ApiClient(configuration))
org = 'org_example' # str | Organization identifier
project = 'project_example' # str | Project identifier
pipeline = 'pipeline_example' # str | Pipeline identifier for the Input Set.
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)
page = 0 # int | Pagination page number strategy: Specify the page number within the paginated collection related to the number of items on each page. (optional) (default to 0)
limit = 30 # int | Pagination: Number of items to return. (optional) (default to 30)
search_term = 'search_term_example' # str | This would be used to filter resources having attributes matching the search term. (optional)
sort = 'sort_example' # str | Parameter on the basis of which sorting is done. (optional)
order = 'order_example' # str | Order on the basis of which sorting is done. (optional)

try:
    # List Input Sets
    api_response = api_instance.list_input_sets(org, project, pipeline, harness_account=harness_account, page=page, limit=limit, search_term=search_term, sort=sort, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InputSetsApi->list_input_sets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| Organization identifier | 
 **project** | **str**| Project identifier | 
 **pipeline** | **str**| Pipeline identifier for the Input Set. | 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 
 **page** | **int**| Pagination page number strategy: Specify the page number within the paginated collection related to the number of items on each page. | [optional] [default to 0]
 **limit** | **int**| Pagination: Number of items to return. | [optional] [default to 30]
 **search_term** | **str**| This would be used to filter resources having attributes matching the search term. | [optional] 
 **sort** | **str**| Parameter on the basis of which sorting is done. | [optional] 
 **order** | **str**| Order on the basis of which sorting is done. | [optional] 

### Return type

[**list[InputSetResponseBody]**](InputSetResponseBody.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_input_set**
> InputSetResponseBody update_input_set(body, pipeline, org, project, input_set, harness_account=harness_account)

Update an Input Set

Updates an Input Set for a Pipeline.

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
api_instance = harness_python_sdk.InputSetsApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.InputSetUpdateRequestBody() # InputSetUpdateRequestBody | Input Set update request body
pipeline = 'pipeline_example' # str | Pipeline identifier for the Input Set.
org = 'org_example' # str | Organization identifier
project = 'project_example' # str | Project identifier
input_set = 'input_set_example' # str | Input Set identifier
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)

try:
    # Update an Input Set
    api_response = api_instance.update_input_set(body, pipeline, org, project, input_set, harness_account=harness_account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InputSetsApi->update_input_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InputSetUpdateRequestBody**](InputSetUpdateRequestBody.md)| Input Set update request body | 
 **pipeline** | **str**| Pipeline identifier for the Input Set. | 
 **org** | **str**| Organization identifier | 
 **project** | **str**| Project identifier | 
 **input_set** | **str**| Input Set identifier | 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 

### Return type

[**InputSetResponseBody**](InputSetResponseBody.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_input_set_git_metadata**
> GitMetadataUpdateResponseBody update_input_set_git_metadata(pipeline, org, project, input_set, body=body, harness_account=harness_account)

Update GitMetadata for Remote InputSet

Update git-metadata in remote inputSet and return the updated inputSet

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
api_instance = harness_python_sdk.InputSetsApi(harness_python_sdk.ApiClient(configuration))
pipeline = 'pipeline_example' # str | Pipeline identifier for the Input Set.
org = 'org_example' # str | Organization identifier
project = 'project_example' # str | Project identifier
input_set = 'input_set_example' # str | Input Set identifier
body = harness_python_sdk.GitMetadataUpdateRequestBody() # GitMetadataUpdateRequestBody |  (optional)
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)

try:
    # Update GitMetadata for Remote InputSet
    api_response = api_instance.update_input_set_git_metadata(pipeline, org, project, input_set, body=body, harness_account=harness_account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InputSetsApi->update_input_set_git_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline** | **str**| Pipeline identifier for the Input Set. | 
 **org** | **str**| Organization identifier | 
 **project** | **str**| Project identifier | 
 **input_set** | **str**| Input Set identifier | 
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

