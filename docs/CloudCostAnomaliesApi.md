# harness_python_sdk.CloudCostAnomaliesApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**anomaly_filter_values**](CloudCostAnomaliesApi.md#anomaly_filter_values) | **POST** /ccm/api/anomaly/filter-values | Returns the list of distinct values for all the specified Anomaly fields.
[**get_anomalies_summary**](CloudCostAnomaliesApi.md#get_anomalies_summary) | **POST** /ccm/api/anomaly/summary | List Anomalies
[**list_anomalies**](CloudCostAnomaliesApi.md#list_anomalies) | **POST** /ccm/api/anomaly | List Anomalies
[**list_perspective_anomalies**](CloudCostAnomaliesApi.md#list_perspective_anomalies) | **POST** /ccm/api/anomaly/perspective/{perspectiveId} | List Anomalies for Perspective
[**report_anomaly_feedback**](CloudCostAnomaliesApi.md#report_anomaly_feedback) | **PUT** /ccm/api/anomaly/feedback | Report Anomaly feedback

# **anomaly_filter_values**
> ResponseDTOListFilterStats anomaly_filter_values(body, account_identifier)

Returns the list of distinct values for all the specified Anomaly fields.

Returns the list of distinct values for all the specified Anomaly fields.

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
api_instance = harness_python_sdk.CloudCostAnomaliesApi(harness_python_sdk.ApiClient(configuration))
body = ['body_example'] # list[str] | List of Anomaly columns whose unique values will be fetched
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Returns the list of distinct values for all the specified Anomaly fields.
    api_response = api_instance.anomaly_filter_values(body, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostAnomaliesApi->anomaly_filter_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)| List of Anomaly columns whose unique values will be fetched | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**ResponseDTOListFilterStats**](ResponseDTOListFilterStats.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_anomalies_summary**
> ResponseDTOListAnomalySummary get_anomalies_summary(account_identifier, body=body)

List Anomalies

Fetch the result of anomaly query

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
api_instance = harness_python_sdk.CloudCostAnomaliesApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
body = harness_python_sdk.AnomalyFilterProperties() # AnomalyFilterProperties | Anomaly Filter Properties (optional)

try:
    # List Anomalies
    api_response = api_instance.get_anomalies_summary(account_identifier, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostAnomaliesApi->get_anomalies_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **body** | [**AnomalyFilterProperties**](AnomalyFilterProperties.md)| Anomaly Filter Properties | [optional] 

### Return type

[**ResponseDTOListAnomalySummary**](ResponseDTOListAnomalySummary.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_anomalies**
> ResponseDTOListAnomalyData list_anomalies(account_identifier, body=body)

List Anomalies

Fetch the list of anomalies reported according to the filters applied

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
api_instance = harness_python_sdk.CloudCostAnomaliesApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
body = harness_python_sdk.AnomalyFilterProperties() # AnomalyFilterProperties | Anomaly Filter Properties (optional)

try:
    # List Anomalies
    api_response = api_instance.list_anomalies(account_identifier, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostAnomaliesApi->list_anomalies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **body** | [**AnomalyFilterProperties**](AnomalyFilterProperties.md)| Anomaly Filter Properties | [optional] 

### Return type

[**ResponseDTOListAnomalyData**](ResponseDTOListAnomalyData.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_perspective_anomalies**
> ResponseDTOListPerspectiveAnomalyData list_perspective_anomalies(body, account_identifier, perspective_id)

List Anomalies for Perspective

Fetch anomalies for perspective

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
api_instance = harness_python_sdk.CloudCostAnomaliesApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.PerspectiveQueryDTO() # PerspectiveQueryDTO | Perspective Query
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
perspective_id = 'perspective_id_example' # str | Unique identifier for perspective

try:
    # List Anomalies for Perspective
    api_response = api_instance.list_perspective_anomalies(body, account_identifier, perspective_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostAnomaliesApi->list_perspective_anomalies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PerspectiveQueryDTO**](PerspectiveQueryDTO.md)| Perspective Query | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **perspective_id** | **str**| Unique identifier for perspective | 

### Return type

[**ResponseDTOListPerspectiveAnomalyData**](ResponseDTOListPerspectiveAnomalyData.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **report_anomaly_feedback**
> ResponseDTOBoolean report_anomaly_feedback(body, account_identifier, anomaly_id)

Report Anomaly feedback

Mark an anomaly as true/false anomaly

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
api_instance = harness_python_sdk.CloudCostAnomaliesApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.AnomalyFeedback() # AnomalyFeedback | Feedback
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
anomaly_id = 'anomaly_id_example' # str | Unique identifier for perspective

try:
    # Report Anomaly feedback
    api_response = api_instance.report_anomaly_feedback(body, account_identifier, anomaly_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostAnomaliesApi->report_anomaly_feedback: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AnomalyFeedback**](AnomalyFeedback.md)| Feedback | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **anomaly_id** | **str**| Unique identifier for perspective | 

### Return type

[**ResponseDTOBoolean**](ResponseDTOBoolean.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

