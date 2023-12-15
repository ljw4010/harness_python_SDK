# harness_python_sdk.CommitmentOrchestratorEventsAPIsApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**events_chart**](CommitmentOrchestratorEventsAPIsApi.md#events_chart) | **POST** /gateway/lw/api/accounts/{account_id}/v1/events/chart | List event logs

# **events_chart**
> EventsChartsSuccessResponse events_chart(account_identifier, start_date, end_date, account_id, body=body)

List event logs

Obtains list of events and the count of their occurences grouped by date

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
api_instance = harness_python_sdk.CommitmentOrchestratorEventsAPIsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity
start_date = 'start_date_example' # str | 
end_date = 'end_date_example' # str | 
account_id = 'account_id_example' # str | Account Identifier for the Entity
body = harness_python_sdk.EventsFilter() # EventsFilter | Optional filters (optional)

try:
    # List event logs
    api_response = api_instance.events_chart(account_identifier, start_date, end_date, account_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommitmentOrchestratorEventsAPIsApi->events_chart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity | 
 **start_date** | **str**|  | 
 **end_date** | **str**|  | 
 **account_id** | **str**| Account Identifier for the Entity | 
 **body** | [**EventsFilter**](EventsFilter.md)| Optional filters | [optional] 

### Return type

[**EventsChartsSuccessResponse**](EventsChartsSuccessResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

