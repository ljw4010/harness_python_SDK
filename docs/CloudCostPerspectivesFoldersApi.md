# swagger_client.CloudCostPerspectivesFoldersApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_perspective_folder**](CloudCostPerspectivesFoldersApi.md#create_perspective_folder) | **POST** /ccm/api/perspectiveFolders/create | Create a Perspective folder
[**delete_folder**](CloudCostPerspectivesFoldersApi.md#delete_folder) | **DELETE** /ccm/api/perspectiveFolders/{folderId} | Delete a folder
[**get_all_folder_perspectives**](CloudCostPerspectivesFoldersApi.md#get_all_folder_perspectives) | **GET** /ccm/api/perspectiveFolders/{folderId}/perspectives | Return details of all the Perspectives
[**get_folders**](CloudCostPerspectivesFoldersApi.md#get_folders) | **GET** /ccm/api/perspectiveFolders | Fetch folders for an account
[**move_perspectives**](CloudCostPerspectivesFoldersApi.md#move_perspectives) | **POST** /ccm/api/perspectiveFolders/movePerspectives | Move a Perspective
[**update_folder**](CloudCostPerspectivesFoldersApi.md#update_folder) | **PUT** /ccm/api/perspectiveFolders | Update a folder

# **create_perspective_folder**
> ResponseDTOCEViewFolder create_perspective_folder(body, account_identifier)

Create a Perspective folder

Create a Perspective Folder.

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
api_instance = swagger_client.CloudCostPerspectivesFoldersApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreatePerspectiveFolderDTO() # CreatePerspectiveFolderDTO | Request body containing Perspective's CEViewFolder object
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Create a Perspective folder
    api_response = api_instance.create_perspective_folder(body, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostPerspectivesFoldersApi->create_perspective_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreatePerspectiveFolderDTO**](CreatePerspectiveFolderDTO.md)| Request body containing Perspective&#x27;s CEViewFolder object | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**ResponseDTOCEViewFolder**](ResponseDTOCEViewFolder.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_folder**
> ResponseDTOBoolean delete_folder(account_identifier, folder_id)

Delete a folder

Delete a Folder for the given Folder ID.

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
api_instance = swagger_client.CloudCostPerspectivesFoldersApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
folder_id = 'folder_id_example' # str | Unique identifier for the Perspective folder

try:
    # Delete a folder
    api_response = api_instance.delete_folder(account_identifier, folder_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostPerspectivesFoldersApi->delete_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **folder_id** | **str**| Unique identifier for the Perspective folder | 

### Return type

[**ResponseDTOBoolean**](ResponseDTOBoolean.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_folder_perspectives**
> ResponseDTOListPerspective get_all_folder_perspectives(account_identifier, folder_id)

Return details of all the Perspectives

Return details of all the Perspectives for the given account ID and folder

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
api_instance = swagger_client.CloudCostPerspectivesFoldersApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
folder_id = 'folder_id_example' # str | Unique identifier for folder

try:
    # Return details of all the Perspectives
    api_response = api_instance.get_all_folder_perspectives(account_identifier, folder_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostPerspectivesFoldersApi->get_all_folder_perspectives: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **folder_id** | **str**| Unique identifier for folder | 

### Return type

[**ResponseDTOListPerspective**](ResponseDTOListPerspective.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folders**
> ResponseDTOListCEViewFolder get_folders(account_identifier, folder_name_pattern=folder_name_pattern)

Fetch folders for an account

Fetch folders given an accountId

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
api_instance = swagger_client.CloudCostPerspectivesFoldersApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
folder_name_pattern = 'folder_name_pattern_example' # str | Search by folder name pattern (optional)

try:
    # Fetch folders for an account
    api_response = api_instance.get_folders(account_identifier, folder_name_pattern=folder_name_pattern)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostPerspectivesFoldersApi->get_folders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **folder_name_pattern** | **str**| Search by folder name pattern | [optional] 

### Return type

[**ResponseDTOListCEViewFolder**](ResponseDTOListCEViewFolder.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_perspectives**
> ResponseDTOListCEView move_perspectives(body, account_identifier)

Move a Perspective

Move a perspective from a folder to another.

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
api_instance = swagger_client.CloudCostPerspectivesFoldersApi(swagger_client.ApiClient(configuration))
body = swagger_client.MovePerspectiveDTO() # MovePerspectiveDTO | Request body containing perspectiveIds to be moved and newFolderId
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Move a Perspective
    api_response = api_instance.move_perspectives(body, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostPerspectivesFoldersApi->move_perspectives: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MovePerspectiveDTO**](MovePerspectiveDTO.md)| Request body containing perspectiveIds to be moved and newFolderId | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**ResponseDTOListCEView**](ResponseDTOListCEView.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_folder**
> ResponseDTOCEViewFolder update_folder(body, account_identifier)

Update a folder

Update a folder

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
api_instance = swagger_client.CloudCostPerspectivesFoldersApi(swagger_client.ApiClient(configuration))
body = swagger_client.CEViewFolder() # CEViewFolder | Request body containing ceViewFolder object
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Update a folder
    api_response = api_instance.update_folder(body, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostPerspectivesFoldersApi->update_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CEViewFolder**](CEViewFolder.md)| Request body containing ceViewFolder object | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**ResponseDTOCEViewFolder**](ResponseDTOCEViewFolder.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

