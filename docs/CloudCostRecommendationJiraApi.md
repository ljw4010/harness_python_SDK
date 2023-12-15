# harness_python_sdk.CloudCostRecommendationJiraApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_recommendation_jira**](CloudCostRecommendationJiraApi.md#create_recommendation_jira) | **POST** /ccm/api/recommendation/jira/create | Create jira for recommendation

# **create_recommendation_jira**
> ResponseDTOCCMJiraDetails create_recommendation_jira(body, account_identifier)

Create jira for recommendation

Create jira for recommendation

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
api_instance = harness_python_sdk.CloudCostRecommendationJiraApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.CCMJiraCreateDTO() # CCMJiraCreateDTO | Request body containing CCMJiraDetails
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Create jira for recommendation
    api_response = api_instance.create_recommendation_jira(body, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostRecommendationJiraApi->create_recommendation_jira: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CCMJiraCreateDTO**](CCMJiraCreateDTO.md)| Request body containing CCMJiraDetails | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**ResponseDTOCCMJiraDetails**](ResponseDTOCCMJiraDetails.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

