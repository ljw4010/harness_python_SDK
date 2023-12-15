# harness_python_sdk.CloudCostAutoStoppingRulesApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_auto_stopping_resources**](CloudCostAutoStoppingRulesApi.md#all_auto_stopping_resources) | **GET** /gateway/lw/api/accounts/{account_id}/autostopping/rules/{rule_id}/resources | List all the resources for an AutoStopping Rule
[**auto_stopping_rule_details**](CloudCostAutoStoppingRulesApi.md#auto_stopping_rule_details) | **GET** /gateway/lw/api/accounts/{account_id}/autostopping/rules/{rule_id} | Return AutoStopping Rule details
[**cool_down_autostopping_rule**](CloudCostAutoStoppingRulesApi.md#cool_down_autostopping_rule) | **POST** /gateway/lw/api/accounts/{account_id}/autostopping/rules/{rule_id}/cooldown | Cool down an AutoStopping Rule
[**cumulative_auto_stopping_savings**](CloudCostAutoStoppingRulesApi.md#cumulative_auto_stopping_savings) | **GET** /gateway/lw/api/accounts/{account_id}/autostopping/rules/savings/cumulative | Return cumulative savings for all the AutoStopping Rules
[**delete_auto_stopping_rule**](CloudCostAutoStoppingRulesApi.md#delete_auto_stopping_rule) | **DELETE** /gateway/lw/api/accounts/{account_id}/autostopping/rules/{rule_id} | Delete an AutoStopping Rule
[**get_auto_stopping_cool_down_meta**](CloudCostAutoStoppingRulesApi.md#get_auto_stopping_cool_down_meta) | **GET** /gateway/lw/api/accounts/{account_id}/autostopping/rules/{rule_id}/cooldown_meta | Return metadata of cool down of an AutoStopping Rule
[**get_auto_stopping_diagnostics**](CloudCostAutoStoppingRulesApi.md#get_auto_stopping_diagnostics) | **GET** /gateway/lw/api/accounts/{account_id}/autostopping/rules/{rule_id}/diagnostics | Return diagnostics result of an AutoStopping Rule
[**health_of_auto_stopping_rule**](CloudCostAutoStoppingRulesApi.md#health_of_auto_stopping_rule) | **GET** /gateway/lw/api/accounts/{account_id}/autostopping/rules/{rule_id}/health | Return health status of an AutoStopping Rule
[**list_auto_stopping_rules**](CloudCostAutoStoppingRulesApi.md#list_auto_stopping_rules) | **GET** /gateway/lw/api/accounts/{account_id}/autostopping/rules | List AutoStopping Rules
[**savings_from_auto_stopping_rule**](CloudCostAutoStoppingRulesApi.md#savings_from_auto_stopping_rule) | **GET** /gateway/lw/api/accounts/{account_id}/autostopping/rules/{rule_id}/savings | Return savings details for an AutoStopping Rule
[**toggle_autostopping_rule**](CloudCostAutoStoppingRulesApi.md#toggle_autostopping_rule) | **PUT** /gateway/lw/api/accounts/{account_id}/autostopping/rules/{rule_id}/toggle_state | Disable/Enable an Autostopping Rule
[**update_auto_stopping_rule**](CloudCostAutoStoppingRulesApi.md#update_auto_stopping_rule) | **POST** /gateway/lw/api/accounts/{account_id}/autostopping/rules | Create an AutoStopping Rule

# **all_auto_stopping_resources**
> AllResourcesOfAccountResponse all_auto_stopping_resources(account_id, cloud_account_id, region, rule_id, account_identifier)

List all the resources for an AutoStopping Rule

Lists all the resources for an AutoStopping Rule for the given identifier.

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
api_instance = harness_python_sdk.CloudCostAutoStoppingRulesApi(harness_python_sdk.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier for the Entity
cloud_account_id = 'cloud_account_id_example' # str | Connector ID
region = 'region_example' # str | Cloud region where resources belong to
rule_id = 1.2 # float | ID of the AutoStopping Rule for which you need to list the resources
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity

try:
    # List all the resources for an AutoStopping Rule
    api_response = api_instance.all_auto_stopping_resources(account_id, cloud_account_id, region, rule_id, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostAutoStoppingRulesApi->all_auto_stopping_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier for the Entity | 
 **cloud_account_id** | **str**| Connector ID | 
 **region** | **str**| Cloud region where resources belong to | 
 **rule_id** | **float**| ID of the AutoStopping Rule for which you need to list the resources | 
 **account_identifier** | **str**| Account Identifier for the Entity | 

### Return type

[**AllResourcesOfAccountResponse**](AllResourcesOfAccountResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auto_stopping_rule_details**
> InlineResponse2001 auto_stopping_rule_details(account_id, rule_id, account_identifier)

Return AutoStopping Rule details

Returns details of an AutoStopping Rule for the given identifier.

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
api_instance = harness_python_sdk.CloudCostAutoStoppingRulesApi(harness_python_sdk.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier for the Entity
rule_id = 1.2 # float | ID of the AutoStopping Rule for which you need to fetch the details
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity

try:
    # Return AutoStopping Rule details
    api_response = api_instance.auto_stopping_rule_details(account_id, rule_id, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostAutoStoppingRulesApi->auto_stopping_rule_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier for the Entity | 
 **rule_id** | **float**| ID of the AutoStopping Rule for which you need to fetch the details | 
 **account_identifier** | **str**| Account Identifier for the Entity | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cool_down_autostopping_rule**
> str cool_down_autostopping_rule(body, account_identifier, account_id, rule_id)

Cool down an AutoStopping Rule

Cool down resources under an Autostopping rule

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
api_instance = harness_python_sdk.CloudCostAutoStoppingRulesApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.CoolDownOption() # CoolDownOption | Cool Down Options
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity
account_id = 'account_id_example' # str | Account Identifier for the Entity
rule_id = 1.2 # float | ID of the AutoStopping rule for which you need to fetch the diagnostics details

try:
    # Cool down an AutoStopping Rule
    api_response = api_instance.cool_down_autostopping_rule(body, account_identifier, account_id, rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostAutoStoppingRulesApi->cool_down_autostopping_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CoolDownOption**](CoolDownOption.md)| Cool Down Options | 
 **account_identifier** | **str**| Account Identifier for the Entity | 
 **account_id** | **str**| Account Identifier for the Entity | 
 **rule_id** | **float**| ID of the AutoStopping rule for which you need to fetch the diagnostics details | 

### Return type

**str**

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cumulative_auto_stopping_savings**
> CumulativeSavingsResponse cumulative_auto_stopping_savings(account_id, account_identifier)

Return cumulative savings for all the AutoStopping Rules

Returns cumulative savings for all the AutoStopping Rules.

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
api_instance = harness_python_sdk.CloudCostAutoStoppingRulesApi(harness_python_sdk.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier for the Entity
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity

try:
    # Return cumulative savings for all the AutoStopping Rules
    api_response = api_instance.cumulative_auto_stopping_savings(account_id, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostAutoStoppingRulesApi->cumulative_auto_stopping_savings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier for the Entity | 
 **account_identifier** | **str**| Account Identifier for the Entity | 

### Return type

[**CumulativeSavingsResponse**](CumulativeSavingsResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_auto_stopping_rule**
> delete_auto_stopping_rule(rule_id, account_id, account_identifier)

Delete an AutoStopping Rule

Deletes an AutoStopping Rule for the given identifier.

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
api_instance = harness_python_sdk.CloudCostAutoStoppingRulesApi(harness_python_sdk.ApiClient(configuration))
rule_id = 1.2 # float | ID of the AutoStopping Rule that you want to delete
account_id = 'account_id_example' # str | Account Identifier for the Entity
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity

try:
    # Delete an AutoStopping Rule
    api_instance.delete_auto_stopping_rule(rule_id, account_id, account_identifier)
except ApiException as e:
    print("Exception when calling CloudCostAutoStoppingRulesApi->delete_auto_stopping_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **float**| ID of the AutoStopping Rule that you want to delete | 
 **account_id** | **str**| Account Identifier for the Entity | 
 **account_identifier** | **str**| Account Identifier for the Entity | 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auto_stopping_cool_down_meta**
> CoolDownMetaSuccessResponse get_auto_stopping_cool_down_meta(account_id, rule_id, account_identifier)

Return metadata of cool down of an AutoStopping Rule

Return metadata of cool down of an AutoStopping Rule

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
api_instance = harness_python_sdk.CloudCostAutoStoppingRulesApi(harness_python_sdk.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier for the Entity
rule_id = 1.2 # float | ID of the AutoStopping rule for which you need to fetch the diagnostics details
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity

try:
    # Return metadata of cool down of an AutoStopping Rule
    api_response = api_instance.get_auto_stopping_cool_down_meta(account_id, rule_id, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostAutoStoppingRulesApi->get_auto_stopping_cool_down_meta: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier for the Entity | 
 **rule_id** | **float**| ID of the AutoStopping rule for which you need to fetch the diagnostics details | 
 **account_identifier** | **str**| Account Identifier for the Entity | 

### Return type

[**CoolDownMetaSuccessResponse**](CoolDownMetaSuccessResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auto_stopping_diagnostics**
> ServiceDiagnosticsResponse get_auto_stopping_diagnostics(account_id, rule_id, account_identifier)

Return diagnostics result of an AutoStopping Rule

Returns the diagnostics result of an AutoStopping rule for the given identifier.

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
api_instance = harness_python_sdk.CloudCostAutoStoppingRulesApi(harness_python_sdk.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier for the Entity
rule_id = 1.2 # float | ID of the AutoStopping rule for which you need to fetch the diagnostics details
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity

try:
    # Return diagnostics result of an AutoStopping Rule
    api_response = api_instance.get_auto_stopping_diagnostics(account_id, rule_id, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostAutoStoppingRulesApi->get_auto_stopping_diagnostics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier for the Entity | 
 **rule_id** | **float**| ID of the AutoStopping rule for which you need to fetch the diagnostics details | 
 **account_identifier** | **str**| Account Identifier for the Entity | 

### Return type

[**ServiceDiagnosticsResponse**](ServiceDiagnosticsResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **health_of_auto_stopping_rule**
> ServiceHealthResponse health_of_auto_stopping_rule(account_id, rule_id, account_identifier)

Return health status of an AutoStopping Rule

Returns health status of an AutoStopping Rule for the given identifier.

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
api_instance = harness_python_sdk.CloudCostAutoStoppingRulesApi(harness_python_sdk.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier for the Entity
rule_id = 1.2 # float | ID of the AutoStopping Rule for which you need to fetch the health status
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity

try:
    # Return health status of an AutoStopping Rule
    api_response = api_instance.health_of_auto_stopping_rule(account_id, rule_id, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostAutoStoppingRulesApi->health_of_auto_stopping_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier for the Entity | 
 **rule_id** | **float**| ID of the AutoStopping Rule for which you need to fetch the health status | 
 **account_identifier** | **str**| Account Identifier for the Entity | 

### Return type

[**ServiceHealthResponse**](ServiceHealthResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_auto_stopping_rules**
> ServicesResponse list_auto_stopping_rules(account_id, account_identifier, dry_run=dry_run)

List AutoStopping Rules

Lists all the AutoStopping rules separated by comma-separated strings.

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
api_instance = harness_python_sdk.CloudCostAutoStoppingRulesApi(harness_python_sdk.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier for the Entity
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity
dry_run = false # bool | Flag which if enabled lists out only dry run rules. (optional) (default to false)

try:
    # List AutoStopping Rules
    api_response = api_instance.list_auto_stopping_rules(account_id, account_identifier, dry_run=dry_run)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostAutoStoppingRulesApi->list_auto_stopping_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier for the Entity | 
 **account_identifier** | **str**| Account Identifier for the Entity | 
 **dry_run** | **bool**| Flag which if enabled lists out only dry run rules. | [optional] [default to false]

### Return type

[**ServicesResponse**](ServicesResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **savings_from_auto_stopping_rule**
> object savings_from_auto_stopping_rule(account_id, rule_id, account_identifier, _from=_from, to=to, group_by=group_by)

Return savings details for an AutoStopping Rule

Returns savings details for an AutoStopping rule for the given identifier and the specified time duration.

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
api_instance = harness_python_sdk.CloudCostAutoStoppingRulesApi(harness_python_sdk.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier for the Entity
rule_id = 1.2 # float | ID of the AutoStopping Rule for which you want to fetch savings detail
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity
_from = '_from_example' # str | Start time for the computation of savings (optional)
to = 'to_example' # str | End time for the computation of savings (optional)
group_by = 'group_by_example' # str |  (optional)

try:
    # Return savings details for an AutoStopping Rule
    api_response = api_instance.savings_from_auto_stopping_rule(account_id, rule_id, account_identifier, _from=_from, to=to, group_by=group_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostAutoStoppingRulesApi->savings_from_auto_stopping_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier for the Entity | 
 **rule_id** | **float**| ID of the AutoStopping Rule for which you want to fetch savings detail | 
 **account_identifier** | **str**| Account Identifier for the Entity | 
 **_from** | **str**| Start time for the computation of savings | [optional] 
 **to** | **str**| End time for the computation of savings | [optional] 
 **group_by** | **str**|  | [optional] 

### Return type

**object**

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **toggle_autostopping_rule**
> ServicesResponse toggle_autostopping_rule(account_id, rule_id, disable, account_identifier)

Disable/Enable an Autostopping Rule

Disables or enables an Autostopping Rule for the given identifier.

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
api_instance = harness_python_sdk.CloudCostAutoStoppingRulesApi(harness_python_sdk.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier for the Entity
rule_id = 'rule_id_example' # str | ID of the AutoStopping rule to be enabled/disabled
disable = true # bool | 
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity

try:
    # Disable/Enable an Autostopping Rule
    api_response = api_instance.toggle_autostopping_rule(account_id, rule_id, disable, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostAutoStoppingRulesApi->toggle_autostopping_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier for the Entity | 
 **rule_id** | **str**| ID of the AutoStopping rule to be enabled/disabled | 
 **disable** | **bool**|  | 
 **account_identifier** | **str**| Account Identifier for the Entity | 

### Return type

[**ServicesResponse**](ServicesResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_auto_stopping_rule**
> LwServiceResponse update_auto_stopping_rule(body, account_identifier, account_id)

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
api_instance = harness_python_sdk.CloudCostAutoStoppingRulesApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.SaveServiceRequest() # SaveServiceRequest | Service definition of an AutoStopping rule
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity
account_id = 'account_id_example' # str | Account Identifier for the Entity

try:
    # Create an AutoStopping Rule
    api_response = api_instance.update_auto_stopping_rule(body, account_identifier, account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostAutoStoppingRulesApi->update_auto_stopping_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SaveServiceRequest**](SaveServiceRequest.md)| Service definition of an AutoStopping rule | 
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

