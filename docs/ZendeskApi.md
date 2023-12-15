# swagger_client.ZendeskApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_zendesk_ticket**](ZendeskApi.md#create_zendesk_ticket) | **POST** /resourcegroup/api/zendesk | create zendesk ticket for given user
[**get_coveo_token**](ZendeskApi.md#get_coveo_token) | **GET** /resourcegroup/api/zendesk/token | get short live token for Coveo

# **create_zendesk_ticket**
> ResponseDTOZendeskResponseDTO create_zendesk_ticket(email_id, ticket_type, priority, subject, body=body)

create zendesk ticket for given user

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
api_instance = swagger_client.ZendeskApi(swagger_client.ApiClient(configuration))
email_id = 'email_id_example' # str | emailId for user creating ticket
ticket_type = 'ticket_type_example' # str | type of the ticket 
priority = 'priority_example' # str | priority of the ticket
subject = 'subject_example' # str | subject of the ticket
body = swagger_client.ApiZendeskBody() # ApiZendeskBody |  (optional)

try:
    # create zendesk ticket for given user
    api_response = api_instance.create_zendesk_ticket(email_id, ticket_type, priority, subject, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZendeskApi->create_zendesk_ticket: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_id** | **str**| emailId for user creating ticket | 
 **ticket_type** | **str**| type of the ticket  | 
 **priority** | **str**| priority of the ticket | 
 **subject** | **str**| subject of the ticket | 
 **body** | [**ApiZendeskBody**](ApiZendeskBody.md)|  | [optional] 

### Return type

[**ResponseDTOZendeskResponseDTO**](ResponseDTOZendeskResponseDTO.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_coveo_token**
> ResponseDTOCoveoResponseDTO get_coveo_token()

get short live token for Coveo

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
api_instance = swagger_client.ZendeskApi(swagger_client.ApiClient(configuration))

try:
    # get short live token for Coveo
    api_response = api_instance.get_coveo_token()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZendeskApi->get_coveo_token: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResponseDTOCoveoResponseDTO**](ResponseDTOCoveoResponseDTO.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

