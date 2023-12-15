# swagger_client.CommitmentOrchestratorSetupAPIsApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_masters**](CommitmentOrchestratorSetupAPIsApi.md#list_masters) | **POST** /gateway/lw/api/accounts/{account_id}/v1/setup/listMasterAccounts | List master accounts for commitment Setup
[**list_setups**](CommitmentOrchestratorSetupAPIsApi.md#list_setups) | **GET** /gateway/lw/api/accounts/{account_id}/v1/setup/list | List of commitment Setups
[**setup_validate**](CommitmentOrchestratorSetupAPIsApi.md#setup_validate) | **POST** /gateway/lw/api/accounts/{account_id}/v1/setup/validate | Validate commitment Setup

# **list_masters**
> ListMasterSuccessResponse list_masters(account_id, account_identifier)

List master accounts for commitment Setup

Lists master accounts available for commitment orchestrator setup

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
api_instance = swagger_client.CommitmentOrchestratorSetupAPIsApi(swagger_client.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier for the Entity
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity

try:
    # List master accounts for commitment Setup
    api_response = api_instance.list_masters(account_id, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommitmentOrchestratorSetupAPIsApi->list_masters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier for the Entity | 
 **account_identifier** | **str**| Account Identifier for the Entity | 

### Return type

[**ListMasterSuccessResponse**](ListMasterSuccessResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_setups**
> ListSetupsSuccessResponse list_setups(account_id, account_identifier)

List of commitment Setups

Lists setups available for commitment orchestrator

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
api_instance = swagger_client.CommitmentOrchestratorSetupAPIsApi(swagger_client.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier for the Entity
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity

try:
    # List of commitment Setups
    api_response = api_instance.list_setups(account_id, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommitmentOrchestratorSetupAPIsApi->list_setups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier for the Entity | 
 **account_identifier** | **str**| Account Identifier for the Entity | 

### Return type

[**ListSetupsSuccessResponse**](ListSetupsSuccessResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_validate**
> SetupValidateSuccessResponse setup_validate(account_identifier, cloud_account_id, account_id, body=body)

Validate commitment Setup

Obtains maximum allowed configuration values for Savings Plans given a target total coverage

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
api_instance = swagger_client.CommitmentOrchestratorSetupAPIsApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity
cloud_account_id = 'cloud_account_id_example' # str | 
account_id = 'account_id_example' # str | Account Identifier for the Entity
body = swagger_client.AutoCUDConfig() # AutoCUDConfig | Configured setup values (optional)

try:
    # Validate commitment Setup
    api_response = api_instance.setup_validate(account_identifier, cloud_account_id, account_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommitmentOrchestratorSetupAPIsApi->setup_validate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity | 
 **cloud_account_id** | **str**|  | 
 **account_id** | **str**| Account Identifier for the Entity | 
 **body** | [**AutoCUDConfig**](AutoCUDConfig.md)| Configured setup values | [optional] 

### Return type

[**SetupValidateSuccessResponse**](SetupValidateSuccessResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

