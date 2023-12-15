# swagger_client.SourceCodeManagerApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_source_code_manager**](SourceCodeManagerApi.md#create_source_code_manager) | **POST** /ng/api/source-code-manager | Creates Source Code Manager
[**delete_source_code_manager**](SourceCodeManagerApi.md#delete_source_code_manager) | **DELETE** /ng/api/source-code-manager/{identifier} | Deletes the Source Code Manager corresponding to the specified Source Code Manager Id
[**get_source_code_managers**](SourceCodeManagerApi.md#get_source_code_managers) | **GET** /ng/api/source-code-manager | Lists Source Code Managers for the given account
[**update_source_code_manager**](SourceCodeManagerApi.md#update_source_code_manager) | **PUT** /ng/api/source-code-manager/{identifier} | Updates Source Code Manager Details with the given Source Code Manager Id

# **create_source_code_manager**
> ResponseDTOSourceCodeManager create_source_code_manager(body=body)

Creates Source Code Manager

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
api_instance = swagger_client.SourceCodeManagerApi(swagger_client.ApiClient(configuration))
body = swagger_client.SourceCodeManager() # SourceCodeManager | This contains details of Source Code Manager (optional)

try:
    # Creates Source Code Manager
    api_response = api_instance.create_source_code_manager(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceCodeManagerApi->create_source_code_manager: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SourceCodeManager**](SourceCodeManager.md)| This contains details of Source Code Manager | [optional] 

### Return type

[**ResponseDTOSourceCodeManager**](ResponseDTOSourceCodeManager.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_source_code_manager**
> ResponseDTOBoolean delete_source_code_manager(identifier, account_identifier)

Deletes the Source Code Manager corresponding to the specified Source Code Manager Id

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
api_instance = swagger_client.SourceCodeManagerApi(swagger_client.ApiClient(configuration))
identifier = 'identifier_example' # str | Source Code manager Identifier
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Deletes the Source Code Manager corresponding to the specified Source Code Manager Id
    api_response = api_instance.delete_source_code_manager(identifier, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceCodeManagerApi->delete_source_code_manager: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Source Code manager Identifier | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**ResponseDTOBoolean**](ResponseDTOBoolean.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_source_code_managers**
> ResponseDTOListSourceCodeManager get_source_code_managers(account_identifier)

Lists Source Code Managers for the given account

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
api_instance = swagger_client.SourceCodeManagerApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Lists Source Code Managers for the given account
    api_response = api_instance.get_source_code_managers(account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceCodeManagerApi->get_source_code_managers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**ResponseDTOListSourceCodeManager**](ResponseDTOListSourceCodeManager.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_source_code_manager**
> ResponseDTOSourceCodeManager update_source_code_manager(identifier, body=body)

Updates Source Code Manager Details with the given Source Code Manager Id

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
api_instance = swagger_client.SourceCodeManagerApi(swagger_client.ApiClient(configuration))
identifier = 'identifier_example' # str | Source Code manager Identifier
body = swagger_client.SourceCodeManager() # SourceCodeManager | This contains details of Source Code Manager (optional)

try:
    # Updates Source Code Manager Details with the given Source Code Manager Id
    api_response = api_instance.update_source_code_manager(identifier, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceCodeManagerApi->update_source_code_manager: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Source Code manager Identifier | 
 **body** | [**SourceCodeManager**](SourceCodeManager.md)| This contains details of Source Code Manager | [optional] 

### Return type

[**ResponseDTOSourceCodeManager**](ResponseDTOSourceCodeManager.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

