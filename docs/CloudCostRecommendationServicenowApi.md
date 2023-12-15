# harness_python_sdk.CloudCostRecommendationServicenowApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_recommendation_servicenow_ticket**](CloudCostRecommendationServicenowApi.md#create_recommendation_servicenow_ticket) | **POST** /ccm/api/recommendation/servicenow/create | Create servicenow ticket for recommendation

# **create_recommendation_servicenow_ticket**
> ResponseDTOCCMServiceNowDetails create_recommendation_servicenow_ticket(body, account_identifier)

Create servicenow ticket for recommendation

Create Servicenow ticket for recommendation

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
api_instance = harness_python_sdk.CloudCostRecommendationServicenowApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.CCMServiceNowCreateDTO() # CCMServiceNowCreateDTO | Request body containing CCMServiceNowDetails
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Create servicenow ticket for recommendation
    api_response = api_instance.create_recommendation_servicenow_ticket(body, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostRecommendationServicenowApi->create_recommendation_servicenow_ticket: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CCMServiceNowCreateDTO**](CCMServiceNowCreateDTO.md)| Request body containing CCMServiceNowDetails | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**ResponseDTOCCMServiceNowDetails**](ResponseDTOCCMServiceNowDetails.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

