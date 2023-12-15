# harness_python_sdk.AidaApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**aida_analyze**](AidaApi.md#aida_analyze) | **POST** /pm/api/v1/aida/analyze | 
[**aida_generate**](AidaApi.md#aida_generate) | **POST** /pm/api/v1/aida/generate | 

# **aida_analyze**
> AnalyzeResponse aida_analyze(body, x_api_key=x_api_key, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)



Describe Policy On Basis of rego

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
api_instance = harness_python_sdk.AidaApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.AnalyzeRequestBody() # AnalyzeRequestBody | 
x_api_key = 'x_api_key_example' # str | Harness PAT key used to perform authorization (optional)
account_identifier = '' # str | Harness account ID (optional)
org_identifier = '' # str | Harness organization ID (optional)
project_identifier = '' # str | Harness project ID (optional)

try:
    api_response = api_instance.aida_analyze(body, x_api_key=x_api_key, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AidaApi->aida_analyze: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AnalyzeRequestBody**](AnalyzeRequestBody.md)|  | 
 **x_api_key** | **str**| Harness PAT key used to perform authorization | [optional] 
 **account_identifier** | **str**| Harness account ID | [optional] 
 **org_identifier** | **str**| Harness organization ID | [optional] 
 **project_identifier** | **str**| Harness project ID | [optional] 

### Return type

[**AnalyzeResponse**](AnalyzeResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/vnd.goa.error

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aida_generate**
> PolicySample aida_generate(body, x_api_key=x_api_key, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)



Generate Policy On Basis of free Text

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
api_instance = harness_python_sdk.AidaApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.GenerateRequestBody() # GenerateRequestBody | 
x_api_key = 'x_api_key_example' # str | Harness PAT key used to perform authorization (optional)
account_identifier = '' # str | Harness account ID (optional)
org_identifier = '' # str | Harness organization ID (optional)
project_identifier = '' # str | Harness project ID (optional)

try:
    api_response = api_instance.aida_generate(body, x_api_key=x_api_key, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AidaApi->aida_generate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GenerateRequestBody**](GenerateRequestBody.md)|  | 
 **x_api_key** | **str**| Harness PAT key used to perform authorization | [optional] 
 **account_identifier** | **str**| Harness account ID | [optional] 
 **org_identifier** | **str**| Harness organization ID | [optional] 
 **project_identifier** | **str**| Harness project ID | [optional] 

### Return type

[**PolicySample**](PolicySample.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/vnd.goa.error

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

