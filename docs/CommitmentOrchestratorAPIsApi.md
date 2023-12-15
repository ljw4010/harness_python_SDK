# swagger_client.CommitmentOrchestratorAPIsApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**event_logs**](CommitmentOrchestratorAPIsApi.md#event_logs) | **POST** /gateway/lw/api/accounts/{account_id}/v1/events/logs | List event logs

# **event_logs**
> EventLogsSuccessResponse event_logs(body, account_identifier, start_date, end_date, account_id)

List event logs

Obtains list of event logs generated as part of commitment orchestration

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
api_instance = swagger_client.CommitmentOrchestratorAPIsApi(swagger_client.ApiClient(configuration))
body = swagger_client.PaginationInput() # PaginationInput | Input for Pagination
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity
start_date = 'start_date_example' # str | 
end_date = 'end_date_example' # str | 
account_id = 'account_id_example' # str | Account Identifier for the Entity

try:
    # List event logs
    api_response = api_instance.event_logs(body, account_identifier, start_date, end_date, account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommitmentOrchestratorAPIsApi->event_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PaginationInput**](PaginationInput.md)| Input for Pagination | 
 **account_identifier** | **str**| Account Identifier for the Entity | 
 **start_date** | **str**|  | 
 **end_date** | **str**|  | 
 **account_id** | **str**| Account Identifier for the Entity | 

### Return type

[**EventLogsSuccessResponse**](EventLogsSuccessResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

