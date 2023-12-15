# harness_python_sdk.RuleEnforcementApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_rule_enforcement**](RuleEnforcementApi.md#add_rule_enforcement) | **POST** /ccm/api/governance/enforcement | Add a new rule Enforcement 
[**ccmget_execution_detail**](RuleEnforcementApi.md#ccmget_execution_detail) | **POST** /ccm/api/governance/execution/details | Fetch Rule Enforcement execution details for account
[**get_rule_enforcement**](RuleEnforcementApi.md#get_rule_enforcement) | **POST** /ccm/api/governance/enforcement/list | Fetch Rule Enforcements for account
[**get_rule_enforcement_count**](RuleEnforcementApi.md#get_rule_enforcement_count) | **POST** /ccm/api/governance/enforcement/count | Fetch Rule Enforcement count for account

# **add_rule_enforcement**
> ResponseDTORuleEnforcement add_rule_enforcement(body, account_identifier)

Add a new rule Enforcement 

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
api_instance = harness_python_sdk.RuleEnforcementApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.CreateRuleEnforcementDTO() # CreateRuleEnforcementDTO | Request body containing Rule Enforcement object
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Add a new rule Enforcement 
    api_response = api_instance.add_rule_enforcement(body, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RuleEnforcementApi->add_rule_enforcement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateRuleEnforcementDTO**](CreateRuleEnforcementDTO.md)| Request body containing Rule Enforcement object | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**ResponseDTORuleEnforcement**](ResponseDTORuleEnforcement.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml, text/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ccmget_execution_detail**
> ResponseDTOExecutionDetails ccmget_execution_detail(body, account_identifier)

Fetch Rule Enforcement execution details for account

execution Detail

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
api_instance = harness_python_sdk.RuleEnforcementApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.ExecutionDetailDTO() # ExecutionDetailDTO | Request body containing  Execution detail object
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Fetch Rule Enforcement execution details for account
    api_response = api_instance.ccmget_execution_detail(body, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RuleEnforcementApi->ccmget_execution_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExecutionDetailDTO**](ExecutionDetailDTO.md)| Request body containing  Execution detail object | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**ResponseDTOExecutionDetails**](ResponseDTOExecutionDetails.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rule_enforcement**
> ResponseDTOListRuleEnforcement get_rule_enforcement(body, account_identifier)

Fetch Rule Enforcements for account

Fetch Rule Enforcement 

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
api_instance = harness_python_sdk.RuleEnforcementApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.CreateRuleEnforcementDTO() # CreateRuleEnforcementDTO | Request body containing  Rule Enforcement  object
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Fetch Rule Enforcements for account
    api_response = api_instance.get_rule_enforcement(body, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RuleEnforcementApi->get_rule_enforcement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateRuleEnforcementDTO**](CreateRuleEnforcementDTO.md)| Request body containing  Rule Enforcement  object | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**ResponseDTOListRuleEnforcement**](ResponseDTOListRuleEnforcement.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rule_enforcement_count**
> ResponseDTOEnforcementCount get_rule_enforcement_count(body, account_identifier)

Fetch Rule Enforcement count for account

Fetch Rule Enforcement count

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
api_instance = harness_python_sdk.RuleEnforcementApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.EnforcementCountDTO() # EnforcementCountDTO | Request body containing  Rule Enforcement count object
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Fetch Rule Enforcement count for account
    api_response = api_instance.get_rule_enforcement_count(body, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RuleEnforcementApi->get_rule_enforcement_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EnforcementCountDTO**](EnforcementCountDTO.md)| Request body containing  Rule Enforcement count object | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**ResponseDTOEnforcementCount**](ResponseDTOEnforcementCount.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

