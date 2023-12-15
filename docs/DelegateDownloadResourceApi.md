# harness_python_sdk.DelegateDownloadResourceApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_docker_delegate_yaml**](DelegateDownloadResourceApi.md#download_docker_delegate_yaml) | **POST** /ng/api/download-delegates/docker | Downloads a docker delegate yaml file.
[**download_kubernetes_delegate_yaml**](DelegateDownloadResourceApi.md#download_kubernetes_delegate_yaml) | **POST** /ng/api/download-delegates/kubernetes | Downloads a kubernetes delegate yaml file.

# **download_docker_delegate_yaml**
> download_docker_delegate_yaml(body, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Downloads a docker delegate yaml file.

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
api_instance = harness_python_sdk.DelegateDownloadResourceApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.DelegateDownloadRequest() # DelegateDownloadRequest | Parameters needed for downloading docker delegate yaml
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Downloads a docker delegate yaml file.
    api_instance.download_docker_delegate_yaml(body, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
except ApiException as e:
    print("Exception when calling DelegateDownloadResourceApi->download_docker_delegate_yaml: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DelegateDownloadRequest**](DelegateDownloadRequest.md)| Parameters needed for downloading docker delegate yaml | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_kubernetes_delegate_yaml**
> download_kubernetes_delegate_yaml(body, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Downloads a kubernetes delegate yaml file.

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
api_instance = harness_python_sdk.DelegateDownloadResourceApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.DelegateDownloadRequest() # DelegateDownloadRequest | Parameters needed for downloading kubernetes delegate yaml
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Downloads a kubernetes delegate yaml file.
    api_instance.download_kubernetes_delegate_yaml(body, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
except ApiException as e:
    print("Exception when calling DelegateDownloadResourceApi->download_kubernetes_delegate_yaml: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DelegateDownloadRequest**](DelegateDownloadRequest.md)| Parameters needed for downloading kubernetes delegate yaml | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

