# swagger_client.AuditApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_audit_event_list**](AuditApi.md#get_audit_event_list) | **POST** /audit/api/audits/list | List Audit Events

# **get_audit_event_list**
> ResponseDTOPageResponseAuditEvent get_audit_event_list(account_identifier, body=body, page_index=page_index, page_size=page_size, sort_orders=sort_orders, page_token=page_token)

List Audit Events

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
api_instance = swagger_client.AuditApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
body = swagger_client.AuditFilterProperties() # AuditFilterProperties | This has the filter attributes for listing Audit Events (optional)
page_index = 0 # int | Page Index of the results to fetch.Default Value: 0 (optional) (default to 0)
page_size = 50 # int | Results per page(max 100)Default Value: 50 (optional) (default to 50)
sort_orders = [swagger_client.SortOrder()] # list[SortOrder] | Sort criteria for the elements. (optional)
page_token = 'page_token_example' # str | Page Token of the next results to fetch.Default Value: '' (optional)

try:
    # List Audit Events
    api_response = api_instance.get_audit_event_list(account_identifier, body=body, page_index=page_index, page_size=page_size, sort_orders=sort_orders, page_token=page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditApi->get_audit_event_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **body** | [**AuditFilterProperties**](AuditFilterProperties.md)| This has the filter attributes for listing Audit Events | [optional] 
 **page_index** | **int**| Page Index of the results to fetch.Default Value: 0 | [optional] [default to 0]
 **page_size** | **int**| Results per page(max 100)Default Value: 50 | [optional] [default to 50]
 **sort_orders** | [**list[SortOrder]**](SortOrder.md)| Sort criteria for the elements. | [optional] 
 **page_token** | **str**| Page Token of the next results to fetch.Default Value: &#x27;&#x27; | [optional] 

### Return type

[**ResponseDTOPageResponseAuditEvent**](ResponseDTOPageResponseAuditEvent.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

