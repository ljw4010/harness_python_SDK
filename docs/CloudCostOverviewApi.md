# swagger_client.CloudCostOverviewApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ccm_overview**](CloudCostOverviewApi.md#get_ccm_overview) | **GET** /ccm/api/overview | Fetch high level overview details about CCM feature.

# **get_ccm_overview**
> ResponseDTOCCMOverview get_ccm_overview(account_identifier, start_time, end_time, group_by)

Fetch high level overview details about CCM feature.

Fetch high level overview details about CCM feature.

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
api_instance = swagger_client.CloudCostOverviewApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
start_time = 789 # int | Start time of the period
end_time = 789 # int | End time of the period
group_by = 'group_by_example' # str | Group by period

try:
    # Fetch high level overview details about CCM feature.
    api_response = api_instance.get_ccm_overview(account_identifier, start_time, end_time, group_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostOverviewApi->get_ccm_overview: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **start_time** | **int**| Start time of the period | 
 **end_time** | **int**| End time of the period | 
 **group_by** | **str**| Group by period | 

### Return type

[**ResponseDTOCCMOverview**](ResponseDTOCCMOverview.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

