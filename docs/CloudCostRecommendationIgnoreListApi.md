# harness_python_sdk.CloudCostRecommendationIgnoreListApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_recommendations_ignore_list**](CloudCostRecommendationIgnoreListApi.md#add_recommendations_ignore_list) | **POST** /ccm/api/recommendation/ignore-list/add | Add resources to recommendations ignore list
[**get_recommendations_ignore_list**](CloudCostRecommendationIgnoreListApi.md#get_recommendations_ignore_list) | **GET** /ccm/api/recommendation/ignore-list | Get resources in recommendations ignore list
[**remove_recommendations_ignore_list**](CloudCostRecommendationIgnoreListApi.md#remove_recommendations_ignore_list) | **POST** /ccm/api/recommendation/ignore-list/remove | Remove resources from recommendations ignore list

# **add_recommendations_ignore_list**
> ResponseDTORecommendationsIgnoreList add_recommendations_ignore_list(body, account_identifier)

Add resources to recommendations ignore list

Add resources to recommendations ignore list

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
api_instance = harness_python_sdk.CloudCostRecommendationIgnoreListApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.RecommendationsIgnoreResourcesDTO() # RecommendationsIgnoreResourcesDTO | Request body containing IgnoreList
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Add resources to recommendations ignore list
    api_response = api_instance.add_recommendations_ignore_list(body, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostRecommendationIgnoreListApi->add_recommendations_ignore_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecommendationsIgnoreResourcesDTO**](RecommendationsIgnoreResourcesDTO.md)| Request body containing IgnoreList | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**ResponseDTORecommendationsIgnoreList**](ResponseDTORecommendationsIgnoreList.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recommendations_ignore_list**
> ResponseDTORecommendationsIgnoreList get_recommendations_ignore_list(account_identifier)

Get resources in recommendations ignore list

Get resources in recommendations ignore list

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
api_instance = harness_python_sdk.CloudCostRecommendationIgnoreListApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Get resources in recommendations ignore list
    api_response = api_instance.get_recommendations_ignore_list(account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostRecommendationIgnoreListApi->get_recommendations_ignore_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**ResponseDTORecommendationsIgnoreList**](ResponseDTORecommendationsIgnoreList.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_recommendations_ignore_list**
> ResponseDTORecommendationsIgnoreList remove_recommendations_ignore_list(body, account_identifier)

Remove resources from recommendations ignore list

Remove resources from recommendations ignore list

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
api_instance = harness_python_sdk.CloudCostRecommendationIgnoreListApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.RecommendationsIgnoreResourcesDTO() # RecommendationsIgnoreResourcesDTO | Request body containing IgnoreList
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Remove resources from recommendations ignore list
    api_response = api_instance.remove_recommendations_ignore_list(body, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostRecommendationIgnoreListApi->remove_recommendations_ignore_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecommendationsIgnoreResourcesDTO**](RecommendationsIgnoreResourcesDTO.md)| Request body containing IgnoreList | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**ResponseDTORecommendationsIgnoreList**](ResponseDTORecommendationsIgnoreList.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

