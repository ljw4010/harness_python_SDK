# harness_python_sdk.CloudCostBIDashboardsApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_bi_dashboards**](CloudCostBIDashboardsApi.md#list_bi_dashboards) | **GET** /ccm/api/bi-dashboards | List all the BI Dashboards for CCM

# **list_bi_dashboards**
> ResponseDTOListBIDashboardSummary list_bi_dashboards(account_identifier)

List all the BI Dashboards for CCM

List all the Cloud Cost BI Dashboards.

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
api_instance = harness_python_sdk.CloudCostBIDashboardsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # List all the BI Dashboards for CCM
    api_response = api_instance.list_bi_dashboards(account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostBIDashboardsApi->list_bi_dashboards: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**ResponseDTOListBIDashboardSummary**](ResponseDTOListBIDashboardSummary.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

