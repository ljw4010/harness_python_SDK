# swagger_client.ConnectorsApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_connector**](ConnectorsApi.md#create_connector) | **POST** /ng/api/connectors | Create a Connector
[**delete_connector**](ConnectorsApi.md#delete_connector) | **DELETE** /ng/api/connectors/{identifier} | Delete a Connector
[**get_all_allowed_field_values**](ConnectorsApi.md#get_all_allowed_field_values) | **GET** /ng/api/connectors/fieldValues | List all the configured field values for the given Connector type.
[**get_ccmk8_s_connector_list**](ConnectorsApi.md#get_ccmk8_s_connector_list) | **POST** /ng/api/connectors/ccmK8sList | Fetches the list of CMC K8S Connectors corresponding to the request&#x27;s filter criteria.
[**get_ce_aws_template**](ConnectorsApi.md#get_ce_aws_template) | **POST** /ng/api/connectors/getceawstemplateurl | Get the Template URL of connector
[**get_connector**](ConnectorsApi.md#get_connector) | **GET** /ng/api/connectors/{identifier} | Return Connector details
[**get_connector_catalogue**](ConnectorsApi.md#get_connector_catalogue) | **GET** /ng/api/connectors/catalogue | Lists all Connectors for an account
[**get_connector_list**](ConnectorsApi.md#get_connector_list) | **GET** /ng/api/connectors | List all Connectors using filters
[**get_connector_list_v2**](ConnectorsApi.md#get_connector_list_v2) | **POST** /ng/api/connectors/listV2 | Fetches the list of Connectors corresponding to the request&#x27;s filter criteria.
[**get_connector_statistics**](ConnectorsApi.md#get_connector_statistics) | **GET** /ng/api/connectors/stats | Gets the connector&#x27;s statistics by Account Identifier, Project Identifier and Organization Identifier
[**get_test_connection_result**](ConnectorsApi.md#get_test_connection_result) | **POST** /ng/api/connectors/testConnection/{identifier} | Test Harness Connector connection with third-party tool
[**get_test_git_repo_connection_result**](ConnectorsApi.md#get_test_git_repo_connection_result) | **POST** /ng/api/connectors/testGitRepoConnection/{identifier} | Test Git Connector sync with repo
[**list_connector_by_fqn**](ConnectorsApi.md#list_connector_by_fqn) | **POST** /ng/api/connectors/listbyfqn | Get list of Connectors by FQN
[**update_connector**](ConnectorsApi.md#update_connector) | **PUT** /ng/api/connectors | Update a Connector
[**validate_the_identifier_is_unique**](ConnectorsApi.md#validate_the_identifier_is_unique) | **GET** /ng/api/connectors/validateUniqueIdentifier | Test a Harness Connector

# **create_connector**
> ResponseDTOConnectorResponse create_connector(body, account_identifier, branch=branch, repo_identifier=repo_identifier, root_folder=root_folder, file_path=file_path, commit_msg=commit_msg, is_new_branch=is_new_branch, base_branch=base_branch, connector_ref=connector_ref, store_type=store_type, repo_name=repo_name)

Create a Connector

Creates a new Harness Connector.

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
api_instance = swagger_client.ConnectorsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Connector2() # Connector2 | Details of the Connector to create
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
branch = 'branch_example' # str | Name of the branch. (optional)
repo_identifier = 'repo_identifier_example' # str | Git Sync Config Id. (optional)
root_folder = 'root_folder_example' # str | Path to the root folder of the Entity. (optional)
file_path = 'file_path_example' # str | File Path of the Entity. (optional)
commit_msg = 'commit_msg_example' # str | File Path of the Entity. (optional)
is_new_branch = false # bool | Checks the new branch (optional) (default to false)
base_branch = 'base_branch_example' # str | Name of the default branch. (optional)
connector_ref = 'connector_ref_example' # str | Identifier of Connector needed for CRUD operations on the respective Entity (optional)
store_type = 'store_type_example' # str | Tells whether the Entity is to be saved on Git or not (optional)
repo_name = 'repo_name_example' # str | Name of the repository. (optional)

try:
    # Create a Connector
    api_response = api_instance.create_connector(body, account_identifier, branch=branch, repo_identifier=repo_identifier, root_folder=root_folder, file_path=file_path, commit_msg=commit_msg, is_new_branch=is_new_branch, base_branch=base_branch, connector_ref=connector_ref, store_type=store_type, repo_name=repo_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectorsApi->create_connector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Connector2**](Connector2.md)| Details of the Connector to create | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **branch** | **str**| Name of the branch. | [optional] 
 **repo_identifier** | **str**| Git Sync Config Id. | [optional] 
 **root_folder** | **str**| Path to the root folder of the Entity. | [optional] 
 **file_path** | **str**| File Path of the Entity. | [optional] 
 **commit_msg** | **str**| File Path of the Entity. | [optional] 
 **is_new_branch** | **bool**| Checks the new branch | [optional] [default to false]
 **base_branch** | **str**| Name of the default branch. | [optional] 
 **connector_ref** | **str**| Identifier of Connector needed for CRUD operations on the respective Entity | [optional] 
 **store_type** | **str**| Tells whether the Entity is to be saved on Git or not | [optional] 
 **repo_name** | **str**| Name of the repository. | [optional] 

### Return type

[**ResponseDTOConnectorResponse**](ResponseDTOConnectorResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, text/yaml, text/html, text/plain
 - **Accept**: application/json, application/yaml, text/yaml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_connector**
> ResponseDTOBoolean delete_connector(account_identifier, identifier, org_identifier=org_identifier, project_identifier=project_identifier, branch=branch, repo_identifier=repo_identifier, root_folder=root_folder, file_path=file_path, commit_msg=commit_msg, last_object_id=last_object_id, force_delete=force_delete)

Delete a Connector

Deletes a Connector for the given ID.

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
api_instance = swagger_client.ConnectorsApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
identifier = 'identifier_example' # str | Connector ID
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
branch = 'branch_example' # str | Name of the branch. (optional)
repo_identifier = 'repo_identifier_example' # str | Git Sync Config Id. (optional)
root_folder = 'root_folder_example' # str | Path to the root folder of the Entity. (optional)
file_path = 'file_path_example' # str | File Path of the Entity. (optional)
commit_msg = 'commit_msg_example' # str | Commit Message to use for the merge commit. (optional)
last_object_id = 'last_object_id_example' # str | Last Object Id (optional)
force_delete = false # bool | If true, the Entity will be forced delete, without checking any references/usages (optional) (default to false)

try:
    # Delete a Connector
    api_response = api_instance.delete_connector(account_identifier, identifier, org_identifier=org_identifier, project_identifier=project_identifier, branch=branch, repo_identifier=repo_identifier, root_folder=root_folder, file_path=file_path, commit_msg=commit_msg, last_object_id=last_object_id, force_delete=force_delete)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectorsApi->delete_connector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **identifier** | **str**| Connector ID | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **branch** | **str**| Name of the branch. | [optional] 
 **repo_identifier** | **str**| Git Sync Config Id. | [optional] 
 **root_folder** | **str**| Path to the root folder of the Entity. | [optional] 
 **file_path** | **str**| File Path of the Entity. | [optional] 
 **commit_msg** | **str**| Commit Message to use for the merge commit. | [optional] 
 **last_object_id** | **str**| Last Object Id | [optional] 
 **force_delete** | **bool**| If true, the Entity will be forced delete, without checking any references/usages | [optional] [default to false]

### Return type

[**ResponseDTOBoolean**](ResponseDTOBoolean.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, text/yaml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_allowed_field_values**
> ResponseDTOFieldValues get_all_allowed_field_values(account_identifier, connector_type)

List all the configured field values for the given Connector type.

Returns all the configured field values for the given Connector type, which can be used during connector creation.

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
api_instance = swagger_client.ConnectorsApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
connector_type = 'connector_type_example' # str | Connector type

try:
    # List all the configured field values for the given Connector type.
    api_response = api_instance.get_all_allowed_field_values(account_identifier, connector_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectorsApi->get_all_allowed_field_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **connector_type** | **str**| Connector type | 

### Return type

[**ResponseDTOFieldValues**](ResponseDTOFieldValues.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, text/yaml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ccmk8_s_connector_list**
> ResponseDTOPageResponseCcmK8sConnectorResponse get_ccmk8_s_connector_list(body, account_identifier, search_term=search_term, org_identifier=org_identifier, project_identifier=project_identifier, filter_identifier=filter_identifier, include_all_connectors_available_at_scope=include_all_connectors_available_at_scope, branch=branch, repo_identifier=repo_identifier, get_default_from_other_repo=get_default_from_other_repo, get_distinct_from_branches=get_distinct_from_branches, page_index=page_index, page_size=page_size, sort_orders=sort_orders, page_token=page_token)

Fetches the list of CMC K8S Connectors corresponding to the request's filter criteria.

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
api_instance = swagger_client.ConnectorsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ConnectorFilterProperties() # ConnectorFilterProperties | Details of the filters applied
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
search_term = 'search_term_example' # str | This would be used to filter Connectors. Any Connector having the specified string in its Name, ID and Tag would be filtered. (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
filter_identifier = 'filter_identifier_example' # str |  (optional)
include_all_connectors_available_at_scope = true # bool | Specify whether or not to include all the Connectors accessible at the scope. For eg if set as true, at the Project scope we will get org and account Connector also in the response (optional)
branch = 'branch_example' # str | Name of the branch. (optional)
repo_identifier = 'repo_identifier_example' # str | Git Sync Config Id. (optional)
get_default_from_other_repo = true # bool | if true, return all the default entities (optional)
get_distinct_from_branches = true # bool | This when set to true along with GitSync enabled for the Connector, you can get one connector entity from each identifier. The connector entity can belong to any branch (optional)
page_index = 0 # int | Page Index of the results to fetch.Default Value: 0 (optional) (default to 0)
page_size = 50 # int | Results per page(max 100)Default Value: 50 (optional) (default to 50)
sort_orders = [swagger_client.SortOrder()] # list[SortOrder] | Sort criteria for the elements. (optional)
page_token = 'page_token_example' # str | Page Token of the next results to fetch.Default Value: '' (optional)

try:
    # Fetches the list of CMC K8S Connectors corresponding to the request's filter criteria.
    api_response = api_instance.get_ccmk8_s_connector_list(body, account_identifier, search_term=search_term, org_identifier=org_identifier, project_identifier=project_identifier, filter_identifier=filter_identifier, include_all_connectors_available_at_scope=include_all_connectors_available_at_scope, branch=branch, repo_identifier=repo_identifier, get_default_from_other_repo=get_default_from_other_repo, get_distinct_from_branches=get_distinct_from_branches, page_index=page_index, page_size=page_size, sort_orders=sort_orders, page_token=page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectorsApi->get_ccmk8_s_connector_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConnectorFilterProperties**](ConnectorFilterProperties.md)| Details of the filters applied | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **search_term** | **str**| This would be used to filter Connectors. Any Connector having the specified string in its Name, ID and Tag would be filtered. | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **filter_identifier** | **str**|  | [optional] 
 **include_all_connectors_available_at_scope** | **bool**| Specify whether or not to include all the Connectors accessible at the scope. For eg if set as true, at the Project scope we will get org and account Connector also in the response | [optional] 
 **branch** | **str**| Name of the branch. | [optional] 
 **repo_identifier** | **str**| Git Sync Config Id. | [optional] 
 **get_default_from_other_repo** | **bool**| if true, return all the default entities | [optional] 
 **get_distinct_from_branches** | **bool**| This when set to true along with GitSync enabled for the Connector, you can get one connector entity from each identifier. The connector entity can belong to any branch | [optional] 
 **page_index** | **int**| Page Index of the results to fetch.Default Value: 0 | [optional] [default to 0]
 **page_size** | **int**| Results per page(max 100)Default Value: 50 | [optional] [default to 50]
 **sort_orders** | [**list[SortOrder]**](SortOrder.md)| Sort criteria for the elements. | [optional] 
 **page_token** | **str**| Page Token of the next results to fetch.Default Value: &#x27;&#x27; | [optional] 

### Return type

[**ResponseDTOPageResponseCcmK8sConnectorResponse**](ResponseDTOPageResponseCcmK8sConnectorResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, text/yaml, text/html, text/plain
 - **Accept**: application/json, application/yaml, text/yaml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ce_aws_template**
> ResponseDTOString get_ce_aws_template(events_enabled=events_enabled, cur_enabled=cur_enabled, optimization_enabled=optimization_enabled)

Get the Template URL of connector

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
api_instance = swagger_client.ConnectorsApi(swagger_client.ApiClient(configuration))
events_enabled = true # bool | Specify whether or not to enable events (optional)
cur_enabled = true # bool | Specify whether or not to enable CUR (optional)
optimization_enabled = true # bool | Specify whether or not to enable optimization (optional)

try:
    # Get the Template URL of connector
    api_response = api_instance.get_ce_aws_template(events_enabled=events_enabled, cur_enabled=cur_enabled, optimization_enabled=optimization_enabled)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectorsApi->get_ce_aws_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **events_enabled** | **bool**| Specify whether or not to enable events | [optional] 
 **cur_enabled** | **bool**| Specify whether or not to enable CUR | [optional] 
 **optimization_enabled** | **bool**| Specify whether or not to enable optimization | [optional] 

### Return type

[**ResponseDTOString**](ResponseDTOString.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, text/yaml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connector**
> ResponseDTOConnectorResponse get_connector(account_identifier, identifier, org_identifier=org_identifier, project_identifier=project_identifier, branch=branch, repo_identifier=repo_identifier, get_default_from_other_repo=get_default_from_other_repo)

Return Connector details

Returns the Connector's details for the given Account and Connector ID.

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
api_instance = swagger_client.ConnectorsApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
identifier = 'identifier_example' # str | Connector Identifier
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
branch = 'branch_example' # str | Name of the branch. (optional)
repo_identifier = 'repo_identifier_example' # str | Git Sync Config Id. (optional)
get_default_from_other_repo = true # bool | if true, return all the default entities (optional)

try:
    # Return Connector details
    api_response = api_instance.get_connector(account_identifier, identifier, org_identifier=org_identifier, project_identifier=project_identifier, branch=branch, repo_identifier=repo_identifier, get_default_from_other_repo=get_default_from_other_repo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectorsApi->get_connector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **identifier** | **str**| Connector Identifier | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **branch** | **str**| Name of the branch. | [optional] 
 **repo_identifier** | **str**| Git Sync Config Id. | [optional] 
 **get_default_from_other_repo** | **bool**| if true, return all the default entities | [optional] 

### Return type

[**ResponseDTOConnectorResponse**](ResponseDTOConnectorResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, text/yaml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connector_catalogue**
> ResponseDTOConnectorCatalogueResponse get_connector_catalogue(account_identifier)

Lists all Connectors for an account

Lists all the Connectors for the given Account ID.

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
api_instance = swagger_client.ConnectorsApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Lists all Connectors for an account
    api_response = api_instance.get_connector_catalogue(account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectorsApi->get_connector_catalogue: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**ResponseDTOConnectorCatalogueResponse**](ResponseDTOConnectorCatalogueResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, text/yaml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connector_list**
> ResponseDTOPageResponseConnectorResponse get_connector_list(account_identifier, page_index=page_index, page_size=page_size, org_identifier=org_identifier, project_identifier=project_identifier, search_term=search_term, type=type, category=category, source_category=source_category, version=version, branch=branch, repo_identifier=repo_identifier, get_default_from_other_repo=get_default_from_other_repo)

List all Connectors using filters

Lists all the Connectors matching the specified filters.

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
api_instance = swagger_client.ConnectorsApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
page_index = 0 # int | Page number of navigation. By default, it is set to 0. (optional) (default to 0)
page_size = 100 # int | Number of entries per page.The default number of entries per page is 100, while the maximum number allowed is 1000. (optional) (default to 100)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
search_term = 'search_term_example' # str | This would be used to filter Connectors. Any Connector having the specified string in its Name, ID and Tag would be filtered. (optional)
type = 'type_example' # str | Filter Connectors by type (optional)
category = 'category_example' # str | Filter Connectors by category (optional)
source_category = 'source_category_example' # str | Filter Connectors by Source Category. Available Source Categories are CLOUD_PROVIDER, SECRET_MANAGER, CLOUD_COST, ARTIFACTORY, CODE_REPO,  MONITORING and TICKETING (optional)
version = 'version_example' # str |  (optional)
branch = 'branch_example' # str | Name of the branch. (optional)
repo_identifier = 'repo_identifier_example' # str | Git Sync Config Id. (optional)
get_default_from_other_repo = true # bool | if true, return all the default entities (optional)

try:
    # List all Connectors using filters
    api_response = api_instance.get_connector_list(account_identifier, page_index=page_index, page_size=page_size, org_identifier=org_identifier, project_identifier=project_identifier, search_term=search_term, type=type, category=category, source_category=source_category, version=version, branch=branch, repo_identifier=repo_identifier, get_default_from_other_repo=get_default_from_other_repo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectorsApi->get_connector_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **page_index** | **int**| Page number of navigation. By default, it is set to 0. | [optional] [default to 0]
 **page_size** | **int**| Number of entries per page.The default number of entries per page is 100, while the maximum number allowed is 1000. | [optional] [default to 100]
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **search_term** | **str**| This would be used to filter Connectors. Any Connector having the specified string in its Name, ID and Tag would be filtered. | [optional] 
 **type** | **str**| Filter Connectors by type | [optional] 
 **category** | **str**| Filter Connectors by category | [optional] 
 **source_category** | **str**| Filter Connectors by Source Category. Available Source Categories are CLOUD_PROVIDER, SECRET_MANAGER, CLOUD_COST, ARTIFACTORY, CODE_REPO,  MONITORING and TICKETING | [optional] 
 **version** | **str**|  | [optional] 
 **branch** | **str**| Name of the branch. | [optional] 
 **repo_identifier** | **str**| Git Sync Config Id. | [optional] 
 **get_default_from_other_repo** | **bool**| if true, return all the default entities | [optional] 

### Return type

[**ResponseDTOPageResponseConnectorResponse**](ResponseDTOPageResponseConnectorResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, text/yaml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connector_list_v2**
> ResponseDTOPageResponseConnectorResponse get_connector_list_v2(body, account_identifier, search_term=search_term, org_identifier=org_identifier, project_identifier=project_identifier, filter_identifier=filter_identifier, include_all_connectors_available_at_scope=include_all_connectors_available_at_scope, branch=branch, repo_identifier=repo_identifier, get_default_from_other_repo=get_default_from_other_repo, get_distinct_from_branches=get_distinct_from_branches, version=version, only_favorites=only_favorites, page_index=page_index, page_size=page_size, sort_orders=sort_orders, page_token=page_token)

Fetches the list of Connectors corresponding to the request's filter criteria.

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
api_instance = swagger_client.ConnectorsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ConnectorFilterProperties() # ConnectorFilterProperties | Details of the filters applied
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
search_term = 'search_term_example' # str | This would be used to filter Connectors. Any Connector having the specified string in its Name, ID and Tag would be filtered. (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
filter_identifier = 'filter_identifier_example' # str |  (optional)
include_all_connectors_available_at_scope = true # bool | Specify whether or not to include all the Connectors accessible at the scope. For eg if set as true, at the Project scope we will get org and account Connector also in the response (optional)
branch = 'branch_example' # str | Name of the branch. (optional)
repo_identifier = 'repo_identifier_example' # str | Git Sync Config Id. (optional)
get_default_from_other_repo = true # bool | if true, return all the default entities (optional)
get_distinct_from_branches = true # bool | This when set to true along with GitSync enabled for the Connector, you can get one connector entity from each identifier. The connector entity can belong to any branch (optional)
version = 'version_example' # str |  (optional)
only_favorites = false # bool |  (optional) (default to false)
page_index = 0 # int | Page Index of the results to fetch.Default Value: 0 (optional) (default to 0)
page_size = 50 # int | Results per page(max 100)Default Value: 50 (optional) (default to 50)
sort_orders = [swagger_client.SortOrder()] # list[SortOrder] | Sort criteria for the elements. (optional)
page_token = 'page_token_example' # str | Page Token of the next results to fetch.Default Value: '' (optional)

try:
    # Fetches the list of Connectors corresponding to the request's filter criteria.
    api_response = api_instance.get_connector_list_v2(body, account_identifier, search_term=search_term, org_identifier=org_identifier, project_identifier=project_identifier, filter_identifier=filter_identifier, include_all_connectors_available_at_scope=include_all_connectors_available_at_scope, branch=branch, repo_identifier=repo_identifier, get_default_from_other_repo=get_default_from_other_repo, get_distinct_from_branches=get_distinct_from_branches, version=version, only_favorites=only_favorites, page_index=page_index, page_size=page_size, sort_orders=sort_orders, page_token=page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectorsApi->get_connector_list_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConnectorFilterProperties**](ConnectorFilterProperties.md)| Details of the filters applied | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **search_term** | **str**| This would be used to filter Connectors. Any Connector having the specified string in its Name, ID and Tag would be filtered. | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **filter_identifier** | **str**|  | [optional] 
 **include_all_connectors_available_at_scope** | **bool**| Specify whether or not to include all the Connectors accessible at the scope. For eg if set as true, at the Project scope we will get org and account Connector also in the response | [optional] 
 **branch** | **str**| Name of the branch. | [optional] 
 **repo_identifier** | **str**| Git Sync Config Id. | [optional] 
 **get_default_from_other_repo** | **bool**| if true, return all the default entities | [optional] 
 **get_distinct_from_branches** | **bool**| This when set to true along with GitSync enabled for the Connector, you can get one connector entity from each identifier. The connector entity can belong to any branch | [optional] 
 **version** | **str**|  | [optional] 
 **only_favorites** | **bool**|  | [optional] [default to false]
 **page_index** | **int**| Page Index of the results to fetch.Default Value: 0 | [optional] [default to 0]
 **page_size** | **int**| Results per page(max 100)Default Value: 50 | [optional] [default to 50]
 **sort_orders** | [**list[SortOrder]**](SortOrder.md)| Sort criteria for the elements. | [optional] 
 **page_token** | **str**| Page Token of the next results to fetch.Default Value: &#x27;&#x27; | [optional] 

### Return type

[**ResponseDTOPageResponseConnectorResponse**](ResponseDTOPageResponseConnectorResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, text/yaml, text/html, text/plain
 - **Accept**: application/json, application/yaml, text/yaml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connector_statistics**
> ResponseDTOConnectorStatistics get_connector_statistics(account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, branch=branch, repo_identifier=repo_identifier, get_default_from_other_repo=get_default_from_other_repo)

Gets the connector's statistics by Account Identifier, Project Identifier and Organization Identifier

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
api_instance = swagger_client.ConnectorsApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
branch = 'branch_example' # str | Name of the branch. (optional)
repo_identifier = 'repo_identifier_example' # str | Git Sync Config Id. (optional)
get_default_from_other_repo = true # bool | if true, return all the default entities (optional)

try:
    # Gets the connector's statistics by Account Identifier, Project Identifier and Organization Identifier
    api_response = api_instance.get_connector_statistics(account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, branch=branch, repo_identifier=repo_identifier, get_default_from_other_repo=get_default_from_other_repo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectorsApi->get_connector_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **branch** | **str**| Name of the branch. | [optional] 
 **repo_identifier** | **str**| Git Sync Config Id. | [optional] 
 **get_default_from_other_repo** | **bool**| if true, return all the default entities | [optional] 

### Return type

[**ResponseDTOConnectorStatistics**](ResponseDTOConnectorStatistics.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, text/yaml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_connection_result**
> ResponseDTOConnectorValidationResult get_test_connection_result(account_identifier, identifier, org_identifier=org_identifier, project_identifier=project_identifier, branch=branch, repo_identifier=repo_identifier, get_default_from_other_repo=get_default_from_other_repo)

Test Harness Connector connection with third-party tool

Tests if a Harness Connector can successfully connect Harness to a third-party tool.

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
api_instance = swagger_client.ConnectorsApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
identifier = 'identifier_example' # str | Connector ID
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
branch = 'branch_example' # str | Name of the branch. (optional)
repo_identifier = 'repo_identifier_example' # str | Git Sync Config Id. (optional)
get_default_from_other_repo = true # bool | if true, return all the default entities (optional)

try:
    # Test Harness Connector connection with third-party tool
    api_response = api_instance.get_test_connection_result(account_identifier, identifier, org_identifier=org_identifier, project_identifier=project_identifier, branch=branch, repo_identifier=repo_identifier, get_default_from_other_repo=get_default_from_other_repo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectorsApi->get_test_connection_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **identifier** | **str**| Connector ID | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **branch** | **str**| Name of the branch. | [optional] 
 **repo_identifier** | **str**| Git Sync Config Id. | [optional] 
 **get_default_from_other_repo** | **bool**| if true, return all the default entities | [optional] 

### Return type

[**ResponseDTOConnectorValidationResult**](ResponseDTOConnectorValidationResult.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, text/yaml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_git_repo_connection_result**
> ResponseDTOConnectorValidationResult get_test_git_repo_connection_result(account_identifier, identifier, org_identifier=org_identifier, project_identifier=project_identifier, repo_url=repo_url)

Test Git Connector sync with repo

Tests if a Git Repo Connector can successfully connect Harness to a Git provider.

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
api_instance = swagger_client.ConnectorsApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
identifier = 'identifier_example' # str | Connector ID
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
repo_url = 'repo_url_example' # str | URL of the repository, specify only in the case of Account Type Git Connector (optional)

try:
    # Test Git Connector sync with repo
    api_response = api_instance.get_test_git_repo_connection_result(account_identifier, identifier, org_identifier=org_identifier, project_identifier=project_identifier, repo_url=repo_url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectorsApi->get_test_git_repo_connection_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **identifier** | **str**| Connector ID | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **repo_url** | **str**| URL of the repository, specify only in the case of Account Type Git Connector | [optional] 

### Return type

[**ResponseDTOConnectorValidationResult**](ResponseDTOConnectorValidationResult.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, text/yaml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_connector_by_fqn**
> ResponseDTOListConnectorResponse list_connector_by_fqn(body, account_identifier)

Get list of Connectors by FQN

Lists all Connectors for an Account by Fully Qualified Name (FQN).

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
api_instance = swagger_client.ConnectorsApi(swagger_client.ApiClient(configuration))
body = ['body_example'] # list[str] | A list of connectors' FQNs as strings. A maximum of 1000 characters is allowed.
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Get list of Connectors by FQN
    api_response = api_instance.list_connector_by_fqn(body, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectorsApi->list_connector_by_fqn: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)| A list of connectors&#x27; FQNs as strings. A maximum of 1000 characters is allowed. | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**ResponseDTOListConnectorResponse**](ResponseDTOListConnectorResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, text/yaml, text/html, text/plain
 - **Accept**: application/json, application/yaml, text/yaml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_connector**
> ResponseDTOConnectorResponse update_connector(body, account_identifier, branch=branch, repo_identifier=repo_identifier, root_folder=root_folder, file_path=file_path, commit_msg=commit_msg, last_object_id=last_object_id, resolved_conflict_commit_id=resolved_conflict_commit_id, base_branch=base_branch, connector_ref=connector_ref, is_new_branch=is_new_branch)

Update a Connector

Updates a Connector for the given ID.

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
api_instance = swagger_client.ConnectorsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Connector2() # Connector2 | This is the updated Connector. Please provide values for all fields, not just the fields you are updating
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
branch = 'branch_example' # str | Name of the branch. (optional)
repo_identifier = 'repo_identifier_example' # str | Git Sync Config Id. (optional)
root_folder = 'root_folder_example' # str | Path to the root folder of the Entity. (optional)
file_path = 'file_path_example' # str | Path to the root folder of the Entity. (optional)
commit_msg = 'commit_msg_example' # str | Commit Message to use for the merge commit. (optional)
last_object_id = 'last_object_id_example' # str | Its required field during update call request. It can be fetched from the response of GET API call for the entity (optional)
resolved_conflict_commit_id = 'resolved_conflict_commit_id_example' # str | If the entity is git-synced, this parameter represents the commit id against which file conflicts are resolved (optional)
base_branch = 'base_branch_example' # str | Name of the default branch. (optional)
connector_ref = 'connector_ref_example' # str | Identifier of Connector needed for CRUD operations on the respective Entity (optional)
is_new_branch = false # bool | Checks the new branch (optional) (default to false)

try:
    # Update a Connector
    api_response = api_instance.update_connector(body, account_identifier, branch=branch, repo_identifier=repo_identifier, root_folder=root_folder, file_path=file_path, commit_msg=commit_msg, last_object_id=last_object_id, resolved_conflict_commit_id=resolved_conflict_commit_id, base_branch=base_branch, connector_ref=connector_ref, is_new_branch=is_new_branch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectorsApi->update_connector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Connector2**](Connector2.md)| This is the updated Connector. Please provide values for all fields, not just the fields you are updating | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **branch** | **str**| Name of the branch. | [optional] 
 **repo_identifier** | **str**| Git Sync Config Id. | [optional] 
 **root_folder** | **str**| Path to the root folder of the Entity. | [optional] 
 **file_path** | **str**| Path to the root folder of the Entity. | [optional] 
 **commit_msg** | **str**| Commit Message to use for the merge commit. | [optional] 
 **last_object_id** | **str**| Its required field during update call request. It can be fetched from the response of GET API call for the entity | [optional] 
 **resolved_conflict_commit_id** | **str**| If the entity is git-synced, this parameter represents the commit id against which file conflicts are resolved | [optional] 
 **base_branch** | **str**| Name of the default branch. | [optional] 
 **connector_ref** | **str**| Identifier of Connector needed for CRUD operations on the respective Entity | [optional] 
 **is_new_branch** | **bool**| Checks the new branch | [optional] [default to false]

### Return type

[**ResponseDTOConnectorResponse**](ResponseDTOConnectorResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, text/yaml, text/html, text/plain
 - **Accept**: application/json, application/yaml, text/yaml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_the_identifier_is_unique**
> ResponseDTOBoolean validate_the_identifier_is_unique(account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, identifier=identifier)

Test a Harness Connector

Tests if a Connector can successfully connect Harness to a third-party tool using the an Account and Connector ID.

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
api_instance = swagger_client.ConnectorsApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
identifier = 'identifier_example' # str | Connector ID (optional)

try:
    # Test a Harness Connector
    api_response = api_instance.validate_the_identifier_is_unique(account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, identifier=identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectorsApi->validate_the_identifier_is_unique: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **identifier** | **str**| Connector ID | [optional] 

### Return type

[**ResponseDTOBoolean**](ResponseDTOBoolean.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, text/yaml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

