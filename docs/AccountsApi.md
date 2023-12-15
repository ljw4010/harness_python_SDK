# harness_python_sdk.AccountsApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account_ng**](AccountsApi.md#get_account_ng) | **GET** /ng/api/accounts/{accountIdentifier} | Gets an account
[**is_immutable_delegate_enabled**](AccountsApi.md#is_immutable_delegate_enabled) | **GET** /ng/api/accounts/{accountIdentifier}/immutable-delegate-enabled | Checks if immutable delegate is enabled for account
[**update_account_default_experience_ng**](AccountsApi.md#update_account_default_experience_ng) | **PUT** /ng/api/accounts/{accountIdentifier}/default-experience | Update Default Experience
[**update_account_name_ng**](AccountsApi.md#update_account_name_ng) | **PUT** /ng/api/accounts/{accountIdentifier}/name | Update Account Name

# **get_account_ng**
> ResponseDTOAccount get_account_ng(account_identifier)

Gets an account

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
api_instance = harness_python_sdk.AccountsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Gets an account
    api_response = api_instance.get_account_ng(account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_account_ng: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**ResponseDTOAccount**](ResponseDTOAccount.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **is_immutable_delegate_enabled**
> ResponseDTOBoolean is_immutable_delegate_enabled(account_identifier)

Checks if immutable delegate is enabled for account

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
api_instance = harness_python_sdk.AccountsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Checks if immutable delegate is enabled for account
    api_response = api_instance.is_immutable_delegate_enabled(account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->is_immutable_delegate_enabled: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**ResponseDTOBoolean**](ResponseDTOBoolean.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_account_default_experience_ng**
> ResponseDTOAccount update_account_default_experience_ng(body, account_identifier)

Update Default Experience

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
api_instance = harness_python_sdk.AccountsApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.Account() # Account | This is details of the Account. DefaultExperience is mandatory
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Update Default Experience
    api_response = api_instance.update_account_default_experience_ng(body, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->update_account_default_experience_ng: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Account**](Account.md)| This is details of the Account. DefaultExperience is mandatory | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**ResponseDTOAccount**](ResponseDTOAccount.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_account_name_ng**
> ResponseDTOAccount update_account_name_ng(body, account_identifier)

Update Account Name

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
api_instance = harness_python_sdk.AccountsApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.Account() # Account | This is details of the Account. Name is mandatory.
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Update Account Name
    api_response = api_instance.update_account_name_ng(body, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->update_account_name_ng: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Account**](Account.md)| This is details of the Account. Name is mandatory. | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**ResponseDTOAccount**](ResponseDTOAccount.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

