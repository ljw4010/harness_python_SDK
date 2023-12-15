# harness_python_sdk.CloudCostRecommendationsApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_recommendation_state**](CloudCostRecommendationsApi.md#change_recommendation_state) | **POST** /ccm/api/recommendation/overview/change-state | Return void
[**list_recommendations**](CloudCostRecommendationsApi.md#list_recommendations) | **POST** /ccm/api/recommendation/overview/list | Return the list of Recommendations
[**recommendation_filter_values**](CloudCostRecommendationsApi.md#recommendation_filter_values) | **POST** /ccm/api/recommendation/overview/filter-values | Return the list of filter values for the Recommendations
[**recommendation_stats**](CloudCostRecommendationsApi.md#recommendation_stats) | **POST** /ccm/api/recommendation/overview/stats | Return Recommendations statistics
[**recommendations_count**](CloudCostRecommendationsApi.md#recommendations_count) | **POST** /ccm/api/recommendation/overview/count | Return the number of Recommendations

# **change_recommendation_state**
> ResponseDTOVoid change_recommendation_state(account_identifier, recommendation_id, state)

Return void

Mark recommendation as applied/open

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
api_instance = harness_python_sdk.CloudCostRecommendationsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
recommendation_id = 'recommendation_id_example' # str | 
state = 'state_example' # str | 

try:
    # Return void
    api_response = api_instance.change_recommendation_state(account_identifier, recommendation_id, state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostRecommendationsApi->change_recommendation_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **recommendation_id** | **str**|  | 
 **state** | **str**|  | 

### Return type

[**ResponseDTOVoid**](ResponseDTOVoid.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_recommendations**
> ResponseDTORecommendations list_recommendations(body, account_identifier)

Return the list of Recommendations

Returns the list of Cloud Cost Recommendations for the specified filters.

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
api_instance = harness_python_sdk.CloudCostRecommendationsApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.CCMRecommendationFilterProperties() # CCMRecommendationFilterProperties | CCM Recommendations filter body.
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Return the list of Recommendations
    api_response = api_instance.list_recommendations(body, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostRecommendationsApi->list_recommendations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CCMRecommendationFilterProperties**](CCMRecommendationFilterProperties.md)| CCM Recommendations filter body. | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**ResponseDTORecommendations**](ResponseDTORecommendations.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recommendation_filter_values**
> ResponseDTOListFilterStats recommendation_filter_values(body, account_identifier)

Return the list of filter values for the Recommendations

Returns the list of filter values for all the specified filters.

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
api_instance = harness_python_sdk.CloudCostRecommendationsApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.FilterValues() # FilterValues | Recommendation Filter Values Body.
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Return the list of filter values for the Recommendations
    api_response = api_instance.recommendation_filter_values(body, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostRecommendationsApi->recommendation_filter_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FilterValues**](FilterValues.md)| Recommendation Filter Values Body. | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**ResponseDTOListFilterStats**](ResponseDTOListFilterStats.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recommendation_stats**
> ResponseDTORecommendationOverviewStats recommendation_stats(body, account_identifier)

Return Recommendations statistics

Returns the Cloud Cost Recommendations statistics for the specified filters.

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
api_instance = harness_python_sdk.CloudCostRecommendationsApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.CCMRecommendationFilterProperties() # CCMRecommendationFilterProperties | CCM Recommendations filter body.
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Return Recommendations statistics
    api_response = api_instance.recommendation_stats(body, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostRecommendationsApi->recommendation_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CCMRecommendationFilterProperties**](CCMRecommendationFilterProperties.md)| CCM Recommendations filter body. | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**ResponseDTORecommendationOverviewStats**](ResponseDTORecommendationOverviewStats.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recommendations_count**
> ResponseDTOInteger recommendations_count(body, account_identifier)

Return the number of Recommendations

Returns the total number of Cloud Cost Recommendations based on the specified filters.

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
api_instance = harness_python_sdk.CloudCostRecommendationsApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.CCMRecommendationFilterProperties() # CCMRecommendationFilterProperties | CCM Recommendations filter body.
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Return the number of Recommendations
    api_response = api_instance.recommendations_count(body, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostRecommendationsApi->recommendations_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CCMRecommendationFilterProperties**](CCMRecommendationFilterProperties.md)| CCM Recommendations filter body. | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**ResponseDTOInteger**](ResponseDTOInteger.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

