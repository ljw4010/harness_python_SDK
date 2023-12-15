# harness_python_sdk.CloudCostDetailsApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cluster_data**](CloudCostDetailsApi.md#cluster_data) | **POST** /ccm/api/costdetails/clusterData | Returns cluster data in a tabular format
[**costdetailoverview**](CloudCostDetailsApi.md#costdetailoverview) | **POST** /ccm/api/costdetails/overview | Returns an overview of the cost
[**costdetailtabular**](CloudCostDetailsApi.md#costdetailtabular) | **POST** /ccm/api/costdetails/tabularformat | Returns cost details in a tabular format
[**costdetailttimeseries**](CloudCostDetailsApi.md#costdetailttimeseries) | **POST** /ccm/api/costdetails/timeseriesformat | Returns cost details in a time series format

# **cluster_data**
> ResponseDTOListClusterCostDetails cluster_data(body, account_identifier, start_time=start_time, end_time=end_time)

Returns cluster data in a tabular format

Returns cluster data based on the specified query parameters.

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
api_instance = harness_python_sdk.CloudCostDetailsApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.ClusterCostDetailsQueryParams() # ClusterCostDetailsQueryParams | Cost details query parameters.
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
start_time = 'start_time_example' # str | Start time of the cost details. Should use org.joda.time.DateTime parsable format. Example, '2022-01-31', '2022-01-31T07:54Z' or '2022-01-31T07:54:51.264Z'.  Defaults to Today - 7days (optional)
end_time = 'end_time_example' # str | End time of the cost details. Should use org.joda.time.DateTime parsable format. Example, '2022-01-31', '2022-01-31T07:54Z' or '2022-01-31T07:54:51.264Z'.  Defaults to Today (optional)

try:
    # Returns cluster data in a tabular format
    api_response = api_instance.cluster_data(body, account_identifier, start_time=start_time, end_time=end_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostDetailsApi->cluster_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClusterCostDetailsQueryParams**](ClusterCostDetailsQueryParams.md)| Cost details query parameters. | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **start_time** | **str**| Start time of the cost details. Should use org.joda.time.DateTime parsable format. Example, &#x27;2022-01-31&#x27;, &#x27;2022-01-31T07:54Z&#x27; or &#x27;2022-01-31T07:54:51.264Z&#x27;.  Defaults to Today - 7days | [optional] 
 **end_time** | **str**| End time of the cost details. Should use org.joda.time.DateTime parsable format. Example, &#x27;2022-01-31&#x27;, &#x27;2022-01-31T07:54Z&#x27; or &#x27;2022-01-31T07:54:51.264Z&#x27;.  Defaults to Today | [optional] 

### Return type

[**ResponseDTOListClusterCostDetails**](ResponseDTOListClusterCostDetails.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **costdetailoverview**
> ResponseDTOCostOverview costdetailoverview(account_identifier, perspective_id, body=body, start_time=start_time, end_time=end_time)

Returns an overview of the cost

Returns total cost, cost trend, and the time period based on the specified query parameters.

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
api_instance = harness_python_sdk.CloudCostDetailsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
perspective_id = 'perspective_id_example' # str | Perspective identifier of the cost details
body = harness_python_sdk.CostDetailsQueryParams() # CostDetailsQueryParams | Cost details query parameters. (optional)
start_time = 'start_time_example' # str | Start time of the cost details. Should use org.joda.time.DateTime parsable format. Example, '2022-01-31', '2022-01-31T07:54Z' or '2022-01-31T07:54:51.264Z'.  Defaults to Today - 7days (optional)
end_time = 'end_time_example' # str | End time of the cost details. Should use org.joda.time.DateTime parsable format. Example, '2022-01-31', '2022-01-31T07:54Z' or '2022-01-31T07:54:51.264Z'.  Defaults to Today (optional)

try:
    # Returns an overview of the cost
    api_response = api_instance.costdetailoverview(account_identifier, perspective_id, body=body, start_time=start_time, end_time=end_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostDetailsApi->costdetailoverview: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **perspective_id** | **str**| Perspective identifier of the cost details | 
 **body** | [**CostDetailsQueryParams**](CostDetailsQueryParams.md)| Cost details query parameters. | [optional] 
 **start_time** | **str**| Start time of the cost details. Should use org.joda.time.DateTime parsable format. Example, &#x27;2022-01-31&#x27;, &#x27;2022-01-31T07:54Z&#x27; or &#x27;2022-01-31T07:54:51.264Z&#x27;.  Defaults to Today - 7days | [optional] 
 **end_time** | **str**| End time of the cost details. Should use org.joda.time.DateTime parsable format. Example, &#x27;2022-01-31&#x27;, &#x27;2022-01-31T07:54Z&#x27; or &#x27;2022-01-31T07:54:51.264Z&#x27;.  Defaults to Today | [optional] 

### Return type

[**ResponseDTOCostOverview**](ResponseDTOCostOverview.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **costdetailtabular**
> ResponseDTOPerspectiveEntityStatsData costdetailtabular(body, account_identifier, perspective_id, start_time=start_time, end_time=end_time)

Returns cost details in a tabular format

Returns cost details in a tabular format based on the specified query parameters.

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
api_instance = harness_python_sdk.CloudCostDetailsApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.CostDetailsQueryParams() # CostDetailsQueryParams | Cost details query parameters.
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
perspective_id = 'perspective_id_example' # str | Perspective identifier of the cost details
start_time = 'start_time_example' # str | Start time of the cost details. Should use org.joda.time.DateTime parsable format. Example, '2022-01-31', '2022-01-31T07:54Z' or '2022-01-31T07:54:51.264Z'.  Defaults to Today - 7days (optional)
end_time = 'end_time_example' # str | End time of the cost details. Should use org.joda.time.DateTime parsable format. Example, '2022-01-31', '2022-01-31T07:54Z' or '2022-01-31T07:54:51.264Z'.  Defaults to Today (optional)

try:
    # Returns cost details in a tabular format
    api_response = api_instance.costdetailtabular(body, account_identifier, perspective_id, start_time=start_time, end_time=end_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostDetailsApi->costdetailtabular: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CostDetailsQueryParams**](CostDetailsQueryParams.md)| Cost details query parameters. | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **perspective_id** | **str**| Perspective identifier of the cost details | 
 **start_time** | **str**| Start time of the cost details. Should use org.joda.time.DateTime parsable format. Example, &#x27;2022-01-31&#x27;, &#x27;2022-01-31T07:54Z&#x27; or &#x27;2022-01-31T07:54:51.264Z&#x27;.  Defaults to Today - 7days | [optional] 
 **end_time** | **str**| End time of the cost details. Should use org.joda.time.DateTime parsable format. Example, &#x27;2022-01-31&#x27;, &#x27;2022-01-31T07:54Z&#x27; or &#x27;2022-01-31T07:54:51.264Z&#x27;.  Defaults to Today | [optional] 

### Return type

[**ResponseDTOPerspectiveEntityStatsData**](ResponseDTOPerspectiveEntityStatsData.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **costdetailttimeseries**
> ResponseDTOPerspectiveTimeSeriesData costdetailttimeseries(body, account_identifier, perspective_id, start_time=start_time, end_time=end_time)

Returns cost details in a time series format

Returns cost details in a time series format based on the specified query parameters.

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
api_instance = harness_python_sdk.CloudCostDetailsApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.CostDetailsQueryParams() # CostDetailsQueryParams | Cost details query parameters.
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
perspective_id = 'perspective_id_example' # str | Perspective identifier of the cost details
start_time = 'start_time_example' # str | Start time of the cost details. Should use org.joda.time.DateTime parsable format. Example, '2022-01-31', '2022-01-31T07:54Z' or '2022-01-31T07:54:51.264Z'.  Defaults to Today - 7days (optional)
end_time = 'end_time_example' # str | End time of the cost details. Should use org.joda.time.DateTime parsable format. Example, '2022-01-31', '2022-01-31T07:54Z' or '2022-01-31T07:54:51.264Z'.  Defaults to Today (optional)

try:
    # Returns cost details in a time series format
    api_response = api_instance.costdetailttimeseries(body, account_identifier, perspective_id, start_time=start_time, end_time=end_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostDetailsApi->costdetailttimeseries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CostDetailsQueryParams**](CostDetailsQueryParams.md)| Cost details query parameters. | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **perspective_id** | **str**| Perspective identifier of the cost details | 
 **start_time** | **str**| Start time of the cost details. Should use org.joda.time.DateTime parsable format. Example, &#x27;2022-01-31&#x27;, &#x27;2022-01-31T07:54Z&#x27; or &#x27;2022-01-31T07:54:51.264Z&#x27;.  Defaults to Today - 7days | [optional] 
 **end_time** | **str**| End time of the cost details. Should use org.joda.time.DateTime parsable format. Example, &#x27;2022-01-31&#x27;, &#x27;2022-01-31T07:54Z&#x27; or &#x27;2022-01-31T07:54:51.264Z&#x27;.  Defaults to Today | [optional] 

### Return type

[**ResponseDTOPerspectiveTimeSeriesData**](ResponseDTOPerspectiveTimeSeriesData.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

