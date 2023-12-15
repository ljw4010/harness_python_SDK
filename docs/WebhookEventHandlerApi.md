# swagger_client.WebhookEventHandlerApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**process_webhook_event**](WebhookEventHandlerApi.md#process_webhook_event) | **POST** /ng/api/webhook | Process event payload for webhook triggers.

# **process_webhook_event**
> ResponseDTOString process_webhook_event(body, account_identifier)

Process event payload for webhook triggers.

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
api_instance = swagger_client.WebhookEventHandlerApi(swagger_client.ApiClient(configuration))
body = 'body_example' # str | 
account_identifier = 'account_identifier_example' # str | 

try:
    # Process event payload for webhook triggers.
    api_response = api_instance.process_webhook_event(body, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookEventHandlerApi->process_webhook_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)|  | 
 **account_identifier** | **str**|  | 

### Return type

[**ResponseDTOString**](ResponseDTOString.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml, text/plain
 - **Accept**: application/json, application/yaml, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

