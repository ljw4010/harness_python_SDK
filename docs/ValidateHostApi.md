# swagger_client.ValidateHostApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**validate_hosts**](ValidateHostApi.md#validate_hosts) | **POST** /ng/api/host-validation | Validates hosts connectivity credentials

# **validate_hosts**
> ResponseDTOListHostValidationDTO validate_hosts(body, account_identifier, identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Validates hosts connectivity credentials

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
api_instance = swagger_client.ValidateHostApi(swagger_client.ApiClient(configuration))
body = swagger_client.HostValidationParams() # HostValidationParams | List of SSH or WinRm hosts to validate, and Delegate tags (optional)
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
identifier = 'identifier_example' # str | Secret Identifier
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Validates hosts connectivity credentials
    api_response = api_instance.validate_hosts(body, account_identifier, identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ValidateHostApi->validate_hosts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HostValidationParams**](HostValidationParams.md)| List of SSH or WinRm hosts to validate, and Delegate tags (optional) | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **identifier** | **str**| Secret Identifier | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOListHostValidationDTO**](ResponseDTOListHostValidationDTO.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

