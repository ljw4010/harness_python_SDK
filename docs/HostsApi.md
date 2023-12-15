# harness_python_sdk.HostsApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**filter_hosts_by_connector**](HostsApi.md#filter_hosts_by_connector) | **POST** /ng/api/hosts/filter | Gets the list of hosts filtered by accountIdentifier and connectorIdentifier
[**validate_hosts1**](HostsApi.md#validate_hosts1) | **POST** /ng/api/hosts/validate | Validates hosts connectivity credentials

# **filter_hosts_by_connector**
> ResponseDTOPageResponseHostDTO filter_hosts_by_connector(account_identifier, body=body, page_index=page_index, page_size=page_size, sort_orders=sort_orders, page_token=page_token, org_identifier=org_identifier, project_identifier=project_identifier, identifier=identifier)

Gets the list of hosts filtered by accountIdentifier and connectorIdentifier

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
api_instance = harness_python_sdk.HostsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
body = harness_python_sdk.HostFilterDTO() # HostFilterDTO | Details of the filters applied (optional)
page_index = 0 # int | Page Index of the results to fetch.Default Value: 0 (optional) (default to 0)
page_size = 50 # int | Results per page(max 100)Default Value: 50 (optional) (default to 50)
sort_orders = [harness_python_sdk.SortOrder()] # list[SortOrder] | Sort criteria for the elements. (optional)
page_token = 'page_token_example' # str | Page Token of the next results to fetch.Default Value: '' (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
identifier = 'identifier_example' # str | Connector Identifier (optional)

try:
    # Gets the list of hosts filtered by accountIdentifier and connectorIdentifier
    api_response = api_instance.filter_hosts_by_connector(account_identifier, body=body, page_index=page_index, page_size=page_size, sort_orders=sort_orders, page_token=page_token, org_identifier=org_identifier, project_identifier=project_identifier, identifier=identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostsApi->filter_hosts_by_connector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **body** | [**HostFilterDTO**](HostFilterDTO.md)| Details of the filters applied | [optional] 
 **page_index** | **int**| Page Index of the results to fetch.Default Value: 0 | [optional] [default to 0]
 **page_size** | **int**| Results per page(max 100)Default Value: 50 | [optional] [default to 50]
 **sort_orders** | [**list[SortOrder]**](SortOrder.md)| Sort criteria for the elements. | [optional] 
 **page_token** | **str**| Page Token of the next results to fetch.Default Value: &#x27;&#x27; | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **identifier** | **str**| Connector Identifier | [optional] 

### Return type

[**ResponseDTOPageResponseHostDTO**](ResponseDTOPageResponseHostDTO.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, text/yaml, text/html, text/plain
 - **Accept**: application/json, application/yaml, text/yaml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_hosts1**
> ResponseDTOListHostValidationDTO validate_hosts1(body, account_identifier, identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Validates hosts connectivity credentials

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
api_instance = harness_python_sdk.HostsApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.HostValidationParams() # HostValidationParams | List of SSH or WinRm hosts to validate, and Delegate tags (optional)
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
identifier = 'identifier_example' # str | Secret Identifier
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Validates hosts connectivity credentials
    api_response = api_instance.validate_hosts1(body, account_identifier, identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostsApi->validate_hosts1: %s\n" % e)
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
 - **Accept**: application/json, application/yaml, text/yaml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

