# swagger_client.AiEngineApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_prompt_resources**](AiEngineApi.md#get_prompt_resources) | **GET** /ccm/api/governance/promptResources | Get supported prompt resources
[**get_prompt_rules**](AiEngineApi.md#get_prompt_rules) | **GET** /ccm/api/governance/promptRules | Get sample prompt governance rules

# **get_prompt_resources**
> ResponseDTOSetString get_prompt_resources(account_identifier, cloud_provider)

Get supported prompt resources

Get supported prompt resources for a given cloud provider

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
api_instance = swagger_client.AiEngineApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
cloud_provider = 'cloud_provider_example' # str | Cloud Provider

try:
    # Get supported prompt resources
    api_response = api_instance.get_prompt_resources(account_identifier, cloud_provider)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AiEngineApi->get_prompt_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **cloud_provider** | **str**| Cloud Provider | 

### Return type

[**ResponseDTOSetString**](ResponseDTOSetString.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_prompt_rules**
> ResponseDTOListGovernancePromptRule get_prompt_rules(account_identifier, cloud_provider, resource_type=resource_type)

Get sample prompt governance rules

Get sample prompt rules for given cloud provider and resource type

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
api_instance = swagger_client.AiEngineApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
cloud_provider = 'cloud_provider_example' # str | Cloud Provider
resource_type = 'resource_type_example' # str | Resource Type (optional)

try:
    # Get sample prompt governance rules
    api_response = api_instance.get_prompt_rules(account_identifier, cloud_provider, resource_type=resource_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AiEngineApi->get_prompt_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **cloud_provider** | **str**| Cloud Provider | 
 **resource_type** | **str**| Resource Type | [optional] 

### Return type

[**ResponseDTOListGovernancePromptRule**](ResponseDTOListGovernancePromptRule.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

