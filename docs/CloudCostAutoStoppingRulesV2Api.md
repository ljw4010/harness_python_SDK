# harness_python_sdk.CloudCostAutoStoppingRulesV2Api

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_auto_stopping_rule_v2**](CloudCostAutoStoppingRulesV2Api.md#create_auto_stopping_rule_v2) | **POST** /gateway/lw/api/accounts/{account_id}/autostopping/v2/rules | Create an AutoStopping Rule
[**update_auto_stopping_rule_v2**](CloudCostAutoStoppingRulesV2Api.md#update_auto_stopping_rule_v2) | **PUT** /gateway/lw/api/accounts/{account_id}/autostopping/v2/rules/{rule_id} | Update an existing AutoStopping Rule

# **create_auto_stopping_rule_v2**
> LwServiceResponse create_auto_stopping_rule_v2(body, account_identifier, account_id)

Create an AutoStopping Rule

Creates a new AutoStopping Rule.

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
api_instance = harness_python_sdk.CloudCostAutoStoppingRulesV2Api(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.SaveServiceRequestV2() # SaveServiceRequestV2 | Service definition of an AutoStopping rule
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity
account_id = 'account_id_example' # str | Account Identifier for the Entity

try:
    # Create an AutoStopping Rule
    api_response = api_instance.create_auto_stopping_rule_v2(body, account_identifier, account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostAutoStoppingRulesV2Api->create_auto_stopping_rule_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SaveServiceRequestV2**](SaveServiceRequestV2.md)| Service definition of an AutoStopping rule | 
 **account_identifier** | **str**| Account Identifier for the Entity | 
 **account_id** | **str**| Account Identifier for the Entity | 

### Return type

[**LwServiceResponse**](LwServiceResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_auto_stopping_rule_v2**
> LwServiceResponse update_auto_stopping_rule_v2(body, account_identifier, account_id, rule_id)

Update an existing AutoStopping Rule

Updates an existing AutoStopping Rule.

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
api_instance = harness_python_sdk.CloudCostAutoStoppingRulesV2Api(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.SaveServiceRequestV2() # SaveServiceRequestV2 | Service definition of an AutoStopping rule
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity
account_id = 'account_id_example' # str | Account Identifier for the Entity
rule_id = 'rule_id_example' # str | ID of the AutoStopping rule to be enabled/disabled

try:
    # Update an existing AutoStopping Rule
    api_response = api_instance.update_auto_stopping_rule_v2(body, account_identifier, account_id, rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostAutoStoppingRulesV2Api->update_auto_stopping_rule_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SaveServiceRequestV2**](SaveServiceRequestV2.md)| Service definition of an AutoStopping rule | 
 **account_identifier** | **str**| Account Identifier for the Entity | 
 **account_id** | **str**| Account Identifier for the Entity | 
 **rule_id** | **str**| ID of the AutoStopping rule to be enabled/disabled | 

### Return type

[**LwServiceResponse**](LwServiceResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

