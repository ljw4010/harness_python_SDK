# swagger_client.FreezeCRUDApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_freeze**](FreezeCRUDApi.md#create_freeze) | **POST** /ng/api/freeze | Create a Freeze
[**create_global_freeze**](FreezeCRUDApi.md#create_global_freeze) | **POST** /ng/api/freeze/manageGlobalFreeze | Create Global Freeze
[**delete_freeze**](FreezeCRUDApi.md#delete_freeze) | **DELETE** /ng/api/freeze/{freezeIdentifier} | Delete a Freeze
[**delete_many_freezes**](FreezeCRUDApi.md#delete_many_freezes) | **POST** /ng/api/freeze/delete | Delete many Freezes
[**get_freeze**](FreezeCRUDApi.md#get_freeze) | **GET** /ng/api/freeze/{freezeIdentifier} | Get a Freeze
[**get_freeze_list**](FreezeCRUDApi.md#get_freeze_list) | **POST** /ng/api/freeze/list | Gets Freeze list
[**get_frozen_execution_details**](FreezeCRUDApi.md#get_frozen_execution_details) | **GET** /ng/api/freeze/getFrozenExecutionDetails | Get list of freeze acted on a frozen execution
[**get_global_freeze**](FreezeCRUDApi.md#get_global_freeze) | **GET** /ng/api/freeze/getGlobalFreeze | Get Global Freeze Yaml
[**update_freeze**](FreezeCRUDApi.md#update_freeze) | **PUT** /ng/api/freeze/{freezeIdentifier} | Updates a Freeze
[**update_freeze_status**](FreezeCRUDApi.md#update_freeze_status) | **POST** /ng/api/freeze/updateFreezeStatus | Update the status of Freeze to active or inactive

# **create_freeze**
> ResponseDTOFreezeResponse create_freeze(body, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Create a Freeze

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
api_instance = swagger_client.FreezeCRUDApi(swagger_client.ApiClient(configuration))
body = '{   \"summary\" : \"Sample Create Freeze YAML\",   \"description\" : \"Sample Freeze YAML\",   \"value\" : \"freeze:\\n  name: Sample Freeze\\n  identifier: Sample_Freeze\\n  entityConfigs:\\n    - name: Rule 1\\n      entities:\\n        - type: Service\\n          filterType: All\\n        - type: EnvType\\n          filterType: All\\n  status: Disabled\\n  orgIdentifier: org1\\n  projectIdentifier: Project1\\n  windows:\\n    - timeZone: Asia/Calcutta\\n      startTime: 2023-02-20 11:28 AM\\n      duration: 30m\" }' # str | Freeze YAML
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Create a Freeze
    api_response = api_instance.create_freeze(body, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FreezeCRUDApi->create_freeze: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| Freeze YAML | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOFreezeResponse**](ResponseDTOFreezeResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_global_freeze**
> ResponseDTOFreezeResponse create_global_freeze(body, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Create Global Freeze

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
api_instance = swagger_client.FreezeCRUDApi(swagger_client.ApiClient(configuration))
body = 'body_example' # str | Freeze YAML
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Create Global Freeze
    api_response = api_instance.create_global_freeze(body, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FreezeCRUDApi->create_global_freeze: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| Freeze YAML | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOFreezeResponse**](ResponseDTOFreezeResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_freeze**
> delete_freeze(account_identifier, freeze_identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Delete a Freeze

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
api_instance = swagger_client.FreezeCRUDApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
freeze_identifier = 'freeze_identifier_example' # str | Freeze Identifier.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Delete a Freeze
    api_instance.delete_freeze(account_identifier, freeze_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
except ApiException as e:
    print("Exception when calling FreezeCRUDApi->delete_freeze: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **freeze_identifier** | **str**| Freeze Identifier. | 
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

# **delete_many_freezes**
> ResponseDTOFreezeResponseWrapperDTO delete_many_freezes(account_identifier, body=body, org_identifier=org_identifier, project_identifier=project_identifier)

Delete many Freezes

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
api_instance = swagger_client.FreezeCRUDApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
body = ['body_example'] # list[str] | List of Freeze Identifiers (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Delete many Freezes
    api_response = api_instance.delete_many_freezes(account_identifier, body=body, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FreezeCRUDApi->delete_many_freezes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **body** | [**list[str]**](str.md)| List of Freeze Identifiers | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOFreezeResponseWrapperDTO**](ResponseDTOFreezeResponseWrapperDTO.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_freeze**
> ResponseDTOFreezeDetailedResponse get_freeze(account_identifier, freeze_identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Get a Freeze

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
api_instance = swagger_client.FreezeCRUDApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
freeze_identifier = 'freeze_identifier_example' # str | Freeze Identifier.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Get a Freeze
    api_response = api_instance.get_freeze(account_identifier, freeze_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FreezeCRUDApi->get_freeze: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **freeze_identifier** | **str**| Freeze Identifier. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOFreezeDetailedResponse**](ResponseDTOFreezeDetailedResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_freeze_list**
> ResponseDTOPageResponseFreezeSummaryResponse get_freeze_list(account_identifier, body=body, page=page, size=size, org_identifier=org_identifier, project_identifier=project_identifier)

Gets Freeze list

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
api_instance = swagger_client.FreezeCRUDApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
body = swagger_client.FreezeFilterPropertiesDTO() # FreezeFilterPropertiesDTO | This contains details of Freeze filters (optional)
page = 0 # int | Page Index of the results to fetch.Default Value: 0 (optional) (default to 0)
size = 10 # int | Results per page (optional) (default to 10)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Gets Freeze list
    api_response = api_instance.get_freeze_list(account_identifier, body=body, page=page, size=size, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FreezeCRUDApi->get_freeze_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **body** | [**FreezeFilterPropertiesDTO**](FreezeFilterPropertiesDTO.md)| This contains details of Freeze filters | [optional] 
 **page** | **int**| Page Index of the results to fetch.Default Value: 0 | [optional] [default to 0]
 **size** | **int**| Results per page | [optional] [default to 10]
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOPageResponseFreezeSummaryResponse**](ResponseDTOPageResponseFreezeSummaryResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_frozen_execution_details**
> ResponseDTOFrozenExecutionDetails get_frozen_execution_details(account_identifier, org_identifier, project_identifier, plan_execution_id)

Get list of freeze acted on a frozen execution

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
api_instance = swagger_client.FreezeCRUDApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
plan_execution_id = 'plan_execution_id_example' # str | 

try:
    # Get list of freeze acted on a frozen execution
    api_response = api_instance.get_frozen_execution_details(account_identifier, org_identifier, project_identifier, plan_execution_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FreezeCRUDApi->get_frozen_execution_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **plan_execution_id** | **str**|  | 

### Return type

[**ResponseDTOFrozenExecutionDetails**](ResponseDTOFrozenExecutionDetails.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_global_freeze**
> ResponseDTOFreezeDetailedResponse get_global_freeze(account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Get Global Freeze Yaml

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
api_instance = swagger_client.FreezeCRUDApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Get Global Freeze Yaml
    api_response = api_instance.get_global_freeze(account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FreezeCRUDApi->get_global_freeze: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOFreezeDetailedResponse**](ResponseDTOFreezeDetailedResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_freeze**
> ResponseDTOFreezeResponse update_freeze(body, account_identifier, freeze_identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Updates a Freeze

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
api_instance = swagger_client.FreezeCRUDApi(swagger_client.ApiClient(configuration))
body = '{   \"summary\" : \"Sample Update Freeze YAML\",   \"description\" : \"Sample Freeze YAML\",   \"value\" : \"freeze:\\n  name: Sample Freeze\\n  identifier: Sample_Freeze\\n  entityConfigs:\\n    - name: Rule 1\\n      entities:\\n        - type: Service\\n          filterType: All\\n        - type: EnvType\\n          filterType: All\\n  status: Disabled\\n  orgIdentifier: org1\\n  projectIdentifier: project1\\n  windows:\\n    - timeZone: Asia/Calcutta\\n      startTime: 2023-02-20 11:28 AM\\n      duration: 33m\\n  description: \\\"\\\"\" }' # str | Freeze YAML
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
freeze_identifier = 'freeze_identifier_example' # str | Freeze Identifier.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Updates a Freeze
    api_response = api_instance.update_freeze(body, account_identifier, freeze_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FreezeCRUDApi->update_freeze: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| Freeze YAML | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **freeze_identifier** | **str**| Freeze Identifier. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOFreezeResponse**](ResponseDTOFreezeResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_freeze_status**
> ResponseDTOFreezeResponseWrapperDTO update_freeze_status(account_identifier, status, body=body, org_identifier=org_identifier, project_identifier=project_identifier)

Update the status of Freeze to active or inactive

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
api_instance = swagger_client.FreezeCRUDApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
status = 'status_example' # str | Freeze YAML
body = ['body_example'] # list[str] | Comma seperated List of Freeze Identifiers (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Update the status of Freeze to active or inactive
    api_response = api_instance.update_freeze_status(account_identifier, status, body=body, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FreezeCRUDApi->update_freeze_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **status** | **str**| Freeze YAML | 
 **body** | [**list[str]**](str.md)| Comma seperated List of Freeze Identifiers | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOFreezeResponseWrapperDTO**](ResponseDTOFreezeResponseWrapperDTO.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

