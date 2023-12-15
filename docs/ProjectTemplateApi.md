# swagger_client.ProjectTemplateApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_templates_project**](ProjectTemplateApi.md#create_templates_project) | **POST** /v1/orgs/{org}/projects/{project}/templates | Create Template
[**delete_template_project**](ProjectTemplateApi.md#delete_template_project) | **DELETE** /v1/orgs/{org}/projects/{project}/templates/{template}/versions/{version} | Delete Template
[**get_template_project**](ProjectTemplateApi.md#get_template_project) | **GET** /v1/orgs/{org}/projects/{project}/templates/{template}/versions/{version} | Retrieve a Template
[**get_template_stable_project**](ProjectTemplateApi.md#get_template_stable_project) | **GET** /v1/orgs/{org}/projects/{project}/templates/{template} | Get Stable Template
[**get_templates_list_project**](ProjectTemplateApi.md#get_templates_list_project) | **GET** /v1/orgs/{org}/projects/{project}/templates | Get Templates List
[**import_template_project**](ProjectTemplateApi.md#import_template_project) | **POST** /v1/orgs/{org}/projects/{project}/templates/{template}/import | Import Template
[**update_template_project**](ProjectTemplateApi.md#update_template_project) | **PUT** /v1/orgs/{org}/projects/{project}/templates/{template}/versions/{version} | Update Template
[**update_template_stable_project**](ProjectTemplateApi.md#update_template_stable_project) | **PUT** /v1/orgs/{org}/projects/{project}/templates/{template}/versions/{version}/stable | Update Stable Template

# **create_templates_project**
> TemplateResponse create_templates_project(org, project, body=body, harness_account=harness_account)

Create Template

Creates a Template in the Project scope.

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
api_instance = swagger_client.ProjectTemplateApi(swagger_client.ApiClient(configuration))
org = 'org_example' # str | Organization Identifier
project = 'project_example' # str | Project Identifier
body = swagger_client.TemplateCreateRequestBody() # TemplateCreateRequestBody | Templates Create Request Body (optional)
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)

try:
    # Create Template
    api_response = api_instance.create_templates_project(org, project, body=body, harness_account=harness_account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectTemplateApi->create_templates_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| Organization Identifier | 
 **project** | **str**| Project Identifier | 
 **body** | [**TemplateCreateRequestBody**](TemplateCreateRequestBody.md)| Templates Create Request Body | [optional] 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 

### Return type

[**TemplateResponse**](TemplateResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_template_project**
> delete_template_project(project, template, org, version, harness_account=harness_account, comments=comments, force_delete=force_delete)

Delete Template

Deletes particular version of Template at Project scope.

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
api_instance = swagger_client.ProjectTemplateApi(swagger_client.ApiClient(configuration))
project = 'project_example' # str | Project Identifier
template = 'template_example' # str | Template Identifier
org = 'org_example' # str | Organization Identifier
version = 'version_example' # str | Version Label for Template
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)
comments = 'comments_example' # str | Specify comment with respect to changes   (optional)
force_delete = false # bool | Enable this field to force delete a template (optional) (default to false)

try:
    # Delete Template
    api_instance.delete_template_project(project, template, org, version, harness_account=harness_account, comments=comments, force_delete=force_delete)
except ApiException as e:
    print("Exception when calling ProjectTemplateApi->delete_template_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project Identifier | 
 **template** | **str**| Template Identifier | 
 **org** | **str**| Organization Identifier | 
 **version** | **str**| Version Label for Template | 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 
 **comments** | **str**| Specify comment with respect to changes   | [optional] 
 **force_delete** | **bool**| Enable this field to force delete a template | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template_project**
> TemplateWithInputsResponse get_template_project(project, template, org, version, harness_account=harness_account, include_yaml=include_yaml, branch_name=branch_name, parent_entity_connector_ref=parent_entity_connector_ref, parent_entity_repo_name=parent_entity_repo_name, parent_entity_account_id=parent_entity_account_id, parent_entity_org_id=parent_entity_org_id, parent_entity_project_id=parent_entity_project_id)

Retrieve a Template

Retrieves particular version of Template at Project scope.

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
api_instance = swagger_client.ProjectTemplateApi(swagger_client.ApiClient(configuration))
project = 'project_example' # str | Project Identifier
template = 'template_example' # str | Template Identifier
org = 'org_example' # str | Organization Identifier
version = 'version_example' # str | Version Label for Template
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)
include_yaml = true # bool | Use it to get Template along with Input Set YAML (optional)
branch_name = 'branch_name_example' # str | Name of the branch (optional)
parent_entity_connector_ref = 'parent_entity_connector_ref_example' # str | Connector ref of parent template if its remote (optional)
parent_entity_repo_name = 'parent_entity_repo_name_example' # str | Repo name of parent template if its remote (optional)
parent_entity_account_id = 'parent_entity_account_id_example' # str | Account name of parent template if its remote (optional)
parent_entity_org_id = 'parent_entity_org_id_example' # str | Organization name of parent template if its remote (optional)
parent_entity_project_id = 'parent_entity_project_id_example' # str | Project name of parent entity if its remote (optional)

try:
    # Retrieve a Template
    api_response = api_instance.get_template_project(project, template, org, version, harness_account=harness_account, include_yaml=include_yaml, branch_name=branch_name, parent_entity_connector_ref=parent_entity_connector_ref, parent_entity_repo_name=parent_entity_repo_name, parent_entity_account_id=parent_entity_account_id, parent_entity_org_id=parent_entity_org_id, parent_entity_project_id=parent_entity_project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectTemplateApi->get_template_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project Identifier | 
 **template** | **str**| Template Identifier | 
 **org** | **str**| Organization Identifier | 
 **version** | **str**| Version Label for Template | 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 
 **include_yaml** | **bool**| Use it to get Template along with Input Set YAML | [optional] 
 **branch_name** | **str**| Name of the branch | [optional] 
 **parent_entity_connector_ref** | **str**| Connector ref of parent template if its remote | [optional] 
 **parent_entity_repo_name** | **str**| Repo name of parent template if its remote | [optional] 
 **parent_entity_account_id** | **str**| Account name of parent template if its remote | [optional] 
 **parent_entity_org_id** | **str**| Organization name of parent template if its remote | [optional] 
 **parent_entity_project_id** | **str**| Project name of parent entity if its remote | [optional] 

### Return type

[**TemplateWithInputsResponse**](TemplateWithInputsResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template_stable_project**
> TemplateWithInputsResponse get_template_stable_project(org, project, template, harness_account=harness_account, include_yaml=include_yaml, branch_name=branch_name, parent_entity_connector_ref=parent_entity_connector_ref, parent_entity_repo_name=parent_entity_repo_name, parent_entity_account_id=parent_entity_account_id, parent_entity_org_id=parent_entity_org_id, parent_entity_project_id=parent_entity_project_id)

Get Stable Template

Retrieves stable version of Template at Project scope.

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
api_instance = swagger_client.ProjectTemplateApi(swagger_client.ApiClient(configuration))
org = 'org_example' # str | Organization Identifier
project = 'project_example' # str | Project Identifier
template = 'template_example' # str | Template Identifier
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)
include_yaml = true # bool | Use it to get Template along with Input Set YAML (optional)
branch_name = 'branch_name_example' # str | Name of the branch (optional)
parent_entity_connector_ref = 'parent_entity_connector_ref_example' # str | Connector ref of parent template if its remote (optional)
parent_entity_repo_name = 'parent_entity_repo_name_example' # str | Repo name of parent template if its remote (optional)
parent_entity_account_id = 'parent_entity_account_id_example' # str | Account name of parent template if its remote (optional)
parent_entity_org_id = 'parent_entity_org_id_example' # str | Organization name of parent template if its remote (optional)
parent_entity_project_id = 'parent_entity_project_id_example' # str | Project name of parent entity if its remote (optional)

try:
    # Get Stable Template
    api_response = api_instance.get_template_stable_project(org, project, template, harness_account=harness_account, include_yaml=include_yaml, branch_name=branch_name, parent_entity_connector_ref=parent_entity_connector_ref, parent_entity_repo_name=parent_entity_repo_name, parent_entity_account_id=parent_entity_account_id, parent_entity_org_id=parent_entity_org_id, parent_entity_project_id=parent_entity_project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectTemplateApi->get_template_stable_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| Organization Identifier | 
 **project** | **str**| Project Identifier | 
 **template** | **str**| Template Identifier | 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 
 **include_yaml** | **bool**| Use it to get Template along with Input Set YAML | [optional] 
 **branch_name** | **str**| Name of the branch | [optional] 
 **parent_entity_connector_ref** | **str**| Connector ref of parent template if its remote | [optional] 
 **parent_entity_repo_name** | **str**| Repo name of parent template if its remote | [optional] 
 **parent_entity_account_id** | **str**| Account name of parent template if its remote | [optional] 
 **parent_entity_org_id** | **str**| Organization name of parent template if its remote | [optional] 
 **parent_entity_project_id** | **str**| Project name of parent entity if its remote | [optional] 

### Return type

[**TemplateWithInputsResponse**](TemplateWithInputsResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_templates_list_project**
> TemplateMetaDataList get_templates_list_project(org, project, harness_account=harness_account, page=page, limit=limit, sort=sort, order=order, search_term=search_term, type=type, recursive=recursive, names=names, identifiers=identifiers, description=description, entity_types=entity_types, child_types=child_types)

Get Templates List

Retrieves list of Template with meta-data at Project scope.

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
api_instance = swagger_client.ProjectTemplateApi(swagger_client.ApiClient(configuration))
org = 'org_example' # str | Organization Identifier
project = 'project_example' # str | Project Identifier
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)
page = 0 # int | Pagination page number strategy: Specify the page number within the paginated collection related to the number of items in each page  (optional) (default to 0)
limit = 30 # int | Pagination: Number of items to return (optional) (default to 30)
sort = 'sort_example' # str | Parameter on the basis of which sorting is done. (optional)
order = 'order_example' # str | Order on the basis of which sorting is done. (optional)
search_term = 'search_term_example' # str | This would be used to filter resources having attributes matching with search term. (optional)
type = 'type_example' # str | Template List Type (optional)
recursive = false # bool | Specify true if all accessible Templates are to be included (optional) (default to false)
names = ['names_example'] # list[str] | Template names for filtering (optional)
identifiers = ['identifiers_example'] # list[str] | Template Ids for Filtering (optional)
description = 'description_example' # str | Filter properties description (optional)
entity_types = ['entity_types_example'] # list[str] | Type of Template (optional)
child_types = ['child_types_example'] # list[str] | Child types describe the type of Step or stage (optional)

try:
    # Get Templates List
    api_response = api_instance.get_templates_list_project(org, project, harness_account=harness_account, page=page, limit=limit, sort=sort, order=order, search_term=search_term, type=type, recursive=recursive, names=names, identifiers=identifiers, description=description, entity_types=entity_types, child_types=child_types)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectTemplateApi->get_templates_list_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| Organization Identifier | 
 **project** | **str**| Project Identifier | 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 
 **page** | **int**| Pagination page number strategy: Specify the page number within the paginated collection related to the number of items in each page  | [optional] [default to 0]
 **limit** | **int**| Pagination: Number of items to return | [optional] [default to 30]
 **sort** | **str**| Parameter on the basis of which sorting is done. | [optional] 
 **order** | **str**| Order on the basis of which sorting is done. | [optional] 
 **search_term** | **str**| This would be used to filter resources having attributes matching with search term. | [optional] 
 **type** | **str**| Template List Type | [optional] 
 **recursive** | **bool**| Specify true if all accessible Templates are to be included | [optional] [default to false]
 **names** | [**list[str]**](str.md)| Template names for filtering | [optional] 
 **identifiers** | [**list[str]**](str.md)| Template Ids for Filtering | [optional] 
 **description** | **str**| Filter properties description | [optional] 
 **entity_types** | [**list[str]**](str.md)| Type of Template | [optional] 
 **child_types** | [**list[str]**](str.md)| Child types describe the type of Step or stage | [optional] 

### Return type

[**TemplateMetaDataList**](TemplateMetaDataList.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_template_project**
> TemplateImportResponseBody import_template_project(org, project, template, body=body, harness_account=harness_account)

Import Template

Import template at a project level

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
api_instance = swagger_client.ProjectTemplateApi(swagger_client.ApiClient(configuration))
org = 'org_example' # str | Organization Identifier
project = 'project_example' # str | Project Identifier
template = 'template_example' # str | Template Identifier
body = swagger_client.TemplateImportRequestBody() # TemplateImportRequestBody |  (optional)
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)

try:
    # Import Template
    api_response = api_instance.import_template_project(org, project, template, body=body, harness_account=harness_account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectTemplateApi->import_template_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| Organization Identifier | 
 **project** | **str**| Project Identifier | 
 **template** | **str**| Template Identifier | 
 **body** | [**TemplateImportRequestBody**](TemplateImportRequestBody.md)|  | [optional] 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 

### Return type

[**TemplateImportResponseBody**](TemplateImportResponseBody.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_template_project**
> TemplateResponse update_template_project(project, template, org, version, body=body, harness_account=harness_account)

Update Template

Updates particular version of Template at Project scope.

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
api_instance = swagger_client.ProjectTemplateApi(swagger_client.ApiClient(configuration))
project = 'project_example' # str | Project Identifier
template = 'template_example' # str | Template Identifier
org = 'org_example' # str | Organization Identifier
version = 'version_example' # str | Version Label for Template
body = swagger_client.TemplateUpdateRequestBody() # TemplateUpdateRequestBody | Templates Update Request Body (optional)
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)

try:
    # Update Template
    api_response = api_instance.update_template_project(project, template, org, version, body=body, harness_account=harness_account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectTemplateApi->update_template_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project Identifier | 
 **template** | **str**| Template Identifier | 
 **org** | **str**| Organization Identifier | 
 **version** | **str**| Version Label for Template | 
 **body** | [**TemplateUpdateRequestBody**](TemplateUpdateRequestBody.md)| Templates Update Request Body | [optional] 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 

### Return type

[**TemplateResponse**](TemplateResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_template_stable_project**
> TemplateUpdateStableResponse update_template_stable_project(org, project, template, version, body=body, harness_account=harness_account)

Update Stable Template

Updates the stable version of Template at Project scope.

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
api_instance = swagger_client.ProjectTemplateApi(swagger_client.ApiClient(configuration))
org = 'org_example' # str | Organization Identifier
project = 'project_example' # str | Project Identifier
template = 'template_example' # str | Template Identifier
version = 'version_example' # str | Version Label for Template
body = swagger_client.GitFindDetails() # GitFindDetails | Templates Fetch Request Body (optional)
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)

try:
    # Update Stable Template
    api_response = api_instance.update_template_stable_project(org, project, template, version, body=body, harness_account=harness_account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectTemplateApi->update_template_stable_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| Organization Identifier | 
 **project** | **str**| Project Identifier | 
 **template** | **str**| Template Identifier | 
 **version** | **str**| Version Label for Template | 
 **body** | [**GitFindDetails**](GitFindDetails.md)| Templates Fetch Request Body | [optional] 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 

### Return type

[**TemplateUpdateStableResponse**](TemplateUpdateStableResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

