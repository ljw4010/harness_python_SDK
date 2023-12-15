# harness_python_sdk.CannyApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_canny_post**](CannyApi.md#create_canny_post) | **POST** /ng/api/canny/post | create Canny Post for given user
[**get_canny_boards**](CannyApi.md#get_canny_boards) | **GET** /ng/api/canny/boards | Get a list of boards available on Canny

# **create_canny_post**
> ResponseDTOCannyResponse create_canny_post(account_identifier, body=body)

create Canny Post for given user

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
api_instance = harness_python_sdk.CannyApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
body = harness_python_sdk.CannyPostBody() # CannyPostBody |  (optional)

try:
    # create Canny Post for given user
    api_response = api_instance.create_canny_post(account_identifier, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CannyApi->create_canny_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **body** | [**CannyPostBody**](CannyPostBody.md)|  | [optional] 

### Return type

[**ResponseDTOCannyResponse**](ResponseDTOCannyResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_canny_boards**
> ResponseDTOCannyBoardsResponse get_canny_boards(account_identifier)

Get a list of boards available on Canny

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
api_instance = harness_python_sdk.CannyApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Get a list of boards available on Canny
    api_response = api_instance.get_canny_boards(account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CannyApi->get_canny_boards: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**ResponseDTOCannyBoardsResponse**](ResponseDTOCannyBoardsResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

