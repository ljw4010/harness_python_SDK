# swagger_client.EvaluateApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**evaluate_evaluate**](EvaluateApi.md#evaluate_evaluate) | **POST** /pm/api/v1/evaluate | 

# **evaluate_evaluate**
> EvaluatedPolicy evaluate_evaluate(body, x_api_key=x_api_key, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)



Evaluate arbitrary rego

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
api_instance = swagger_client.EvaluateApi(swagger_client.ApiClient(configuration))
body = swagger_client.EvaluateRequestBody() # EvaluateRequestBody | 
x_api_key = 'x_api_key_example' # str | Harness PAT key used to perform authorization (optional)
account_identifier = '' # str | Harness account ID (optional)
org_identifier = '' # str | Harness organization ID (optional)
project_identifier = '' # str | Harness project ID (optional)

try:
    api_response = api_instance.evaluate_evaluate(body, x_api_key=x_api_key, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EvaluateApi->evaluate_evaluate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EvaluateRequestBody**](EvaluateRequestBody.md)|  | 
 **x_api_key** | **str**| Harness PAT key used to perform authorization | [optional] 
 **account_identifier** | **str**| Harness account ID | [optional] 
 **org_identifier** | **str**| Harness organization ID | [optional] 
 **project_identifier** | **str**| Harness project ID | [optional] 

### Return type

[**EvaluatedPolicy**](EvaluatedPolicy.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/vnd.goa.error

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
