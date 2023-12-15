# swagger_client.FileStoreApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](FileStoreApi.md#create) | **POST** /ng/api/file-store | Create Folder or File including content
[**create_via_yaml**](FileStoreApi.md#create_via_yaml) | **POST** /ng/api/file-store/yaml | Creates File or Folder metadata via YAML
[**delete_file**](FileStoreApi.md#delete_file) | **DELETE** /ng/api/file-store/{identifier} | Delete File or Folder by identifier
[**download_file**](FileStoreApi.md#download_file) | **GET** /ng/api/file-store/files/{identifier}/download | Download File
[**get_created_by_list**](FileStoreApi.md#get_created_by_list) | **GET** /ng/api/file-store/files/createdBy | Get list of created by user details
[**get_entity_types**](FileStoreApi.md#get_entity_types) | **GET** /ng/api/file-store/supported-entity-types | Get the list of supported entity types for files
[**get_file**](FileStoreApi.md#get_file) | **GET** /ng/api/file-store/{identifier} | Get the Folder or File metadata
[**get_file_content_using_scoped_file_path**](FileStoreApi.md#get_file_content_using_scoped_file_path) | **GET** /ng/api/file-store/files/{scopedFilePath}/content | Get file content of scopedFilePath
[**get_folder_nodes**](FileStoreApi.md#get_folder_nodes) | **POST** /ng/api/file-store/folder | Get folder nodes at first level, not including sub-nodes
[**get_referenced_by**](FileStoreApi.md#get_referenced_by) | **GET** /ng/api/file-store/{identifier}/referenced-by | Get list of entities where file is referenced by queried entity type
[**list_files_and_folders**](FileStoreApi.md#list_files_and_folders) | **GET** /ng/api/file-store | List Files and Folders metadata
[**list_files_with_filter**](FileStoreApi.md#list_files_with_filter) | **POST** /ng/api/file-store/files/filter | Get filtered list of Files or Folders
[**update**](FileStoreApi.md#update) | **PUT** /ng/api/file-store/{identifier} | Update Folder or File including content
[**update_via_yaml**](FileStoreApi.md#update_via_yaml) | **PUT** /ng/api/file-store/yaml/{identifier} | Update File or Folder metadata via YAML

# **create**
> ResponseDTOFile create(account_identifier, tags=tags, content=content, identifier=identifier, name=name, file_usage=file_usage, type=type, parent_identifier=parent_identifier, description=description, mime_type=mime_type, path=path, created_by=created_by, last_modified_by=last_modified_by, last_modified_at=last_modified_at, org_identifier=org_identifier, project_identifier=project_identifier)

Create Folder or File including content

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
api_instance = swagger_client.FileStoreApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
tags = 'tags_example' # str |  (optional)
content = NULL # object |  (optional)
identifier = 'identifier_example' # str |  (optional)
name = 'name_example' # str |  (optional)
file_usage = 'file_usage_example' # str |  (optional)
type = 'type_example' # str |  (optional)
parent_identifier = 'parent_identifier_example' # str |  (optional)
description = 'description_example' # str |  (optional)
mime_type = 'mime_type_example' # str |  (optional)
path = 'path_example' # str |  (optional)
created_by = swagger_client.EmbeddedUserDetailsDTO() # EmbeddedUserDetailsDTO |  (optional)
last_modified_by = swagger_client.EmbeddedUserDetailsDTO() # EmbeddedUserDetailsDTO |  (optional)
last_modified_at = 789 # int |  (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Create Folder or File including content
    api_response = api_instance.create(account_identifier, tags=tags, content=content, identifier=identifier, name=name, file_usage=file_usage, type=type, parent_identifier=parent_identifier, description=description, mime_type=mime_type, path=path, created_by=created_by, last_modified_by=last_modified_by, last_modified_at=last_modified_at, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileStoreApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **tags** | **str**|  | [optional] 
 **content** | [**object**](.md)|  | [optional] 
 **identifier** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **file_usage** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 
 **parent_identifier** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **mime_type** | **str**|  | [optional] 
 **path** | **str**|  | [optional] 
 **created_by** | [**EmbeddedUserDetailsDTO**](.md)|  | [optional] 
 **last_modified_by** | [**EmbeddedUserDetailsDTO**](.md)|  | [optional] 
 **last_modified_at** | **int**|  | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOFile**](ResponseDTOFile.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_via_yaml**
> ResponseDTOFile create_via_yaml(body, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Creates File or Folder metadata via YAML

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
api_instance = swagger_client.FileStoreApi(swagger_client.ApiClient(configuration))
body = swagger_client.FileStoreRequest() # FileStoreRequest | YAML definition of File or Folder
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Creates File or Folder metadata via YAML
    api_response = api_instance.create_via_yaml(body, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileStoreApi->create_via_yaml: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FileStoreRequest**](FileStoreRequest.md)| YAML definition of File or Folder | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOFile**](ResponseDTOFile.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_file**
> ResponseDTOBoolean delete_file(account_identifier, identifier, org_identifier=org_identifier, project_identifier=project_identifier, force_delete=force_delete)

Delete File or Folder by identifier

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
api_instance = swagger_client.FileStoreApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
identifier = 'identifier_example' # str | The file identifier
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
force_delete = false # bool | If true, the Entity will be forced delete, without checking any references/usages (optional) (default to false)

try:
    # Delete File or Folder by identifier
    api_response = api_instance.delete_file(account_identifier, identifier, org_identifier=org_identifier, project_identifier=project_identifier, force_delete=force_delete)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileStoreApi->delete_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **identifier** | **str**| The file identifier | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **force_delete** | **bool**| If true, the Entity will be forced delete, without checking any references/usages | [optional] [default to false]

### Return type

[**ResponseDTOBoolean**](ResponseDTOBoolean.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_file**
> download_file(identifier, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Download File

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
api_instance = swagger_client.FileStoreApi(swagger_client.ApiClient(configuration))
identifier = 'identifier_example' # str | The file identifier
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Download File
    api_instance.download_file(identifier, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
except ApiException as e:
    print("Exception when calling FileStoreApi->download_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| The file identifier | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_created_by_list**
> ResponseDTOSetEmbeddedUserDetailsDTO get_created_by_list(account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Get list of created by user details

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
api_instance = swagger_client.FileStoreApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity. (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Get list of created by user details
    api_response = api_instance.get_created_by_list(account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileStoreApi->get_created_by_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOSetEmbeddedUserDetailsDTO**](ResponseDTOSetEmbeddedUserDetailsDTO.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_types**
> ResponseDTOListEntityType get_entity_types(account_identifier)

Get the list of supported entity types for files

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
api_instance = swagger_client.FileStoreApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Get the list of supported entity types for files
    api_response = api_instance.get_entity_types(account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileStoreApi->get_entity_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**ResponseDTOListEntityType**](ResponseDTOListEntityType.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file**
> ResponseDTOFile get_file(identifier, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Get the Folder or File metadata

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
api_instance = swagger_client.FileStoreApi(swagger_client.ApiClient(configuration))
identifier = 'identifier_example' # str | The file identifier
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Get the Folder or File metadata
    api_response = api_instance.get_file(identifier, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileStoreApi->get_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| The file identifier | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOFile**](ResponseDTOFile.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_content_using_scoped_file_path**
> ResponseDTOString get_file_content_using_scoped_file_path(scoped_file_path, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Get file content of scopedFilePath

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
api_instance = swagger_client.FileStoreApi(swagger_client.ApiClient(configuration))
scoped_file_path = 'scoped_file_path_example' # str | The scoped file path reference
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity. (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Get file content of scopedFilePath
    api_response = api_instance.get_file_content_using_scoped_file_path(scoped_file_path, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileStoreApi->get_file_content_using_scoped_file_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scoped_file_path** | **str**| The scoped file path reference | 
 **account_identifier** | **str**| Account Identifier for the Entity. | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOString**](ResponseDTOString.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folder_nodes**
> ResponseDTOFolderNode get_folder_nodes(body, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, file_usage=file_usage)

Get folder nodes at first level, not including sub-nodes

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
api_instance = swagger_client.FileStoreApi(swagger_client.ApiClient(configuration))
body = swagger_client.FolderNode() # FolderNode | Folder node for which to return the list of nodes
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
file_usage = 'file_usage_example' # str | The file usage (optional)

try:
    # Get folder nodes at first level, not including sub-nodes
    api_response = api_instance.get_folder_nodes(body, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, file_usage=file_usage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileStoreApi->get_folder_nodes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FolderNode**](FolderNode.md)| Folder node for which to return the list of nodes | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **file_usage** | **str**| The file usage | [optional] 

### Return type

[**ResponseDTOFolderNode**](ResponseDTOFolderNode.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_referenced_by**
> ResponseDTOPageResponseEntitySetupUsage get_referenced_by(account_identifier, identifier, page_index=page_index, page_size=page_size, org_identifier=org_identifier, project_identifier=project_identifier, entity_type=entity_type, search_term=search_term)

Get list of entities where file is referenced by queried entity type

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
api_instance = swagger_client.FileStoreApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
identifier = 'identifier_example' # str | The file identifier
page_index = 0 # int | Page number of navigation. The default value is 0 (optional) (default to 0)
page_size = 100 # int | Number of entries per page. The default value is 100 (optional) (default to 100)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
entity_type = 'entity_type_example' # str | Entity type (optional)
search_term = 'search_term_example' # str |  (optional)

try:
    # Get list of entities where file is referenced by queried entity type
    api_response = api_instance.get_referenced_by(account_identifier, identifier, page_index=page_index, page_size=page_size, org_identifier=org_identifier, project_identifier=project_identifier, entity_type=entity_type, search_term=search_term)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileStoreApi->get_referenced_by: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **identifier** | **str**| The file identifier | 
 **page_index** | **int**| Page number of navigation. The default value is 0 | [optional] [default to 0]
 **page_size** | **int**| Number of entries per page. The default value is 100 | [optional] [default to 100]
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **entity_type** | **str**| Entity type | [optional] 
 **search_term** | **str**|  | [optional] 

### Return type

[**ResponseDTOPageResponseEntitySetupUsage**](ResponseDTOPageResponseEntitySetupUsage.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_files_and_folders**
> ResponseDTOPageFile list_files_and_folders(account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, identifiers=identifiers, search_term=search_term, page_index=page_index, page_size=page_size, sort_orders=sort_orders, page_token=page_token)

List Files and Folders metadata

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
api_instance = swagger_client.FileStoreApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
identifiers = ['identifiers_example'] # list[str] | This is the list of File IDs. Details specific to these IDs would be fetched. (optional)
search_term = 'search_term_example' # str | This will be used to filter files or folders. Any file or folder having the specified search term in its Name or Identifier will be filtered (optional)
page_index = 0 # int | Page Index of the results to fetch.Default Value: 0 (optional) (default to 0)
page_size = 50 # int | Results per page(max 100)Default Value: 50 (optional) (default to 50)
sort_orders = [swagger_client.SortOrder()] # list[SortOrder] | Sort criteria for the elements. (optional)
page_token = 'page_token_example' # str | Page Token of the next results to fetch.Default Value: '' (optional)

try:
    # List Files and Folders metadata
    api_response = api_instance.list_files_and_folders(account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, identifiers=identifiers, search_term=search_term, page_index=page_index, page_size=page_size, sort_orders=sort_orders, page_token=page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileStoreApi->list_files_and_folders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **identifiers** | [**list[str]**](str.md)| This is the list of File IDs. Details specific to these IDs would be fetched. | [optional] 
 **search_term** | **str**| This will be used to filter files or folders. Any file or folder having the specified search term in its Name or Identifier will be filtered | [optional] 
 **page_index** | **int**| Page Index of the results to fetch.Default Value: 0 | [optional] [default to 0]
 **page_size** | **int**| Results per page(max 100)Default Value: 50 | [optional] [default to 50]
 **sort_orders** | [**list[SortOrder]**](SortOrder.md)| Sort criteria for the elements. | [optional] 
 **page_token** | **str**| Page Token of the next results to fetch.Default Value: &#x27;&#x27; | [optional] 

### Return type

[**ResponseDTOPageFile**](ResponseDTOPageFile.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_files_with_filter**
> ResponseDTOPageFile list_files_with_filter(body=body, page_index=page_index, page_size=page_size, sort_orders=sort_orders, page_token=page_token, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, filter_identifier=filter_identifier, search_term=search_term)

Get filtered list of Files or Folders

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
api_instance = swagger_client.FileStoreApi(swagger_client.ApiClient(configuration))
body = swagger_client.FilesFilterPropertiesDTO() # FilesFilterPropertiesDTO | Details of the File filter properties to be applied (optional)
page_index = 0 # int | Page Index of the results to fetch.Default Value: 0 (optional) (default to 0)
page_size = 50 # int | Results per page(max 100)Default Value: 50 (optional) (default to 50)
sort_orders = [swagger_client.SortOrder()] # list[SortOrder] | Sort criteria for the elements. (optional)
page_token = 'page_token_example' # str | Page Token of the next results to fetch.Default Value: '' (optional)
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity. (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
filter_identifier = 'filter_identifier_example' # str | Filter identifier (optional)
search_term = 'search_term_example' # str | This will be used to filter files or folders. Any file or folder having the specified search term in its Name or Identifier will be filtered (optional)

try:
    # Get filtered list of Files or Folders
    api_response = api_instance.list_files_with_filter(body=body, page_index=page_index, page_size=page_size, sort_orders=sort_orders, page_token=page_token, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, filter_identifier=filter_identifier, search_term=search_term)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileStoreApi->list_files_with_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FilesFilterPropertiesDTO**](FilesFilterPropertiesDTO.md)| Details of the File filter properties to be applied | [optional] 
 **page_index** | **int**| Page Index of the results to fetch.Default Value: 0 | [optional] [default to 0]
 **page_size** | **int**| Results per page(max 100)Default Value: 50 | [optional] [default to 50]
 **sort_orders** | [**list[SortOrder]**](SortOrder.md)| Sort criteria for the elements. | [optional] 
 **page_token** | **str**| Page Token of the next results to fetch.Default Value: &#x27;&#x27; | [optional] 
 **account_identifier** | **str**| Account Identifier for the Entity. | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **filter_identifier** | **str**| Filter identifier | [optional] 
 **search_term** | **str**| This will be used to filter files or folders. Any file or folder having the specified search term in its Name or Identifier will be filtered | [optional] 

### Return type

[**ResponseDTOPageFile**](ResponseDTOPageFile.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> ResponseDTOFile update(account_identifier, identifier, tags=tags, identifier2=identifier2, name=name, file_usage=file_usage, type=type, parent_identifier=parent_identifier, description=description, mime_type=mime_type, path=path, created_by=created_by, last_modified_by=last_modified_by, last_modified_at=last_modified_at, content=content, org_identifier=org_identifier, project_identifier=project_identifier)

Update Folder or File including content

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
api_instance = swagger_client.FileStoreApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
identifier = 'identifier_example' # str | The file identifier
tags = 'tags_example' # str |  (optional)
identifier2 = 'identifier_example' # str |  (optional)
name = 'name_example' # str |  (optional)
file_usage = 'file_usage_example' # str |  (optional)
type = 'type_example' # str |  (optional)
parent_identifier = 'parent_identifier_example' # str |  (optional)
description = 'description_example' # str |  (optional)
mime_type = 'mime_type_example' # str |  (optional)
path = 'path_example' # str |  (optional)
created_by = swagger_client.EmbeddedUserDetailsDTO() # EmbeddedUserDetailsDTO |  (optional)
last_modified_by = swagger_client.EmbeddedUserDetailsDTO() # EmbeddedUserDetailsDTO |  (optional)
last_modified_at = 789 # int |  (optional)
content = NULL # object |  (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Update Folder or File including content
    api_response = api_instance.update(account_identifier, identifier, tags=tags, identifier2=identifier2, name=name, file_usage=file_usage, type=type, parent_identifier=parent_identifier, description=description, mime_type=mime_type, path=path, created_by=created_by, last_modified_by=last_modified_by, last_modified_at=last_modified_at, content=content, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileStoreApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **identifier** | **str**| The file identifier | 
 **tags** | **str**|  | [optional] 
 **identifier2** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **file_usage** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 
 **parent_identifier** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **mime_type** | **str**|  | [optional] 
 **path** | **str**|  | [optional] 
 **created_by** | [**EmbeddedUserDetailsDTO**](.md)|  | [optional] 
 **last_modified_by** | [**EmbeddedUserDetailsDTO**](.md)|  | [optional] 
 **last_modified_at** | **int**|  | [optional] 
 **content** | [**object**](.md)|  | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOFile**](ResponseDTOFile.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_via_yaml**
> ResponseDTOFile update_via_yaml(body, account_identifier, identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Update File or Folder metadata via YAML

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
api_instance = swagger_client.FileStoreApi(swagger_client.ApiClient(configuration))
body = swagger_client.FileStoreRequest() # FileStoreRequest | YAML definition of File or Folder
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
identifier = 'identifier_example' # str | The file identifier
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Update File or Folder metadata via YAML
    api_response = api_instance.update_via_yaml(body, account_identifier, identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileStoreApi->update_via_yaml: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FileStoreRequest**](FileStoreRequest.md)| YAML definition of File or Folder | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **identifier** | **str**| The file identifier | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOFile**](ResponseDTOFile.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

