# harness_python_sdk.AgentMTLSEndpointManagementApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_agent_mtls_endpoint_domain_prefix_availability**](AgentMTLSEndpointManagementApi.md#check_agent_mtls_endpoint_domain_prefix_availability) | **GET** /ng/api/agent/mtls/check-availability | Checks whether a given agent mTLS endpoint domain prefix is available.
[**create_agent_mtls_endpoint_for_account**](AgentMTLSEndpointManagementApi.md#create_agent_mtls_endpoint_for_account) | **POST** /ng/api/agent/mtls/endpoint | Creates the agent mTLS endpoint for an account.
[**delete_agent_mtls_endpoint_for_account**](AgentMTLSEndpointManagementApi.md#delete_agent_mtls_endpoint_for_account) | **DELETE** /ng/api/agent/mtls/endpoint | Removes the agent mTLS endpoint for an account.
[**get_agent_mtls_endpoint_for_account**](AgentMTLSEndpointManagementApi.md#get_agent_mtls_endpoint_for_account) | **GET** /ng/api/agent/mtls/endpoint | Gets the agent mTLS endpoint for an account.
[**patch_agent_mtls_endpoint_for_account**](AgentMTLSEndpointManagementApi.md#patch_agent_mtls_endpoint_for_account) | **PATCH** /ng/api/agent/mtls/endpoint | Updates selected properties of the existing agent mTLS endpoint for an account.
[**update_agent_mtls_endpoint_for_account**](AgentMTLSEndpointManagementApi.md#update_agent_mtls_endpoint_for_account) | **PUT** /ng/api/agent/mtls/endpoint | Updates the existing agent mTLS endpoint for an account.

# **check_agent_mtls_endpoint_domain_prefix_availability**
> RestResponseBoolean check_agent_mtls_endpoint_domain_prefix_availability(account_identifier, domain_prefix)

Checks whether a given agent mTLS endpoint domain prefix is available.

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
api_instance = harness_python_sdk.AgentMTLSEndpointManagementApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
domain_prefix = 'domain_prefix_example' # str | The domain prefix to check.

try:
    # Checks whether a given agent mTLS endpoint domain prefix is available.
    api_response = api_instance.check_agent_mtls_endpoint_domain_prefix_availability(account_identifier, domain_prefix)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentMTLSEndpointManagementApi->check_agent_mtls_endpoint_domain_prefix_availability: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **domain_prefix** | **str**| The domain prefix to check. | 

### Return type

[**RestResponseBoolean**](RestResponseBoolean.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_agent_mtls_endpoint_for_account**
> RestResponseAgentMtlsEndpointDetails create_agent_mtls_endpoint_for_account(body, account_identifier)

Creates the agent mTLS endpoint for an account.

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
api_instance = harness_python_sdk.AgentMTLSEndpointManagementApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.AgentMtlsEndpointRequest() # AgentMtlsEndpointRequest | The details of the agent mTLS endpoint to create.
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Creates the agent mTLS endpoint for an account.
    api_response = api_instance.create_agent_mtls_endpoint_for_account(body, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentMTLSEndpointManagementApi->create_agent_mtls_endpoint_for_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AgentMtlsEndpointRequest**](AgentMtlsEndpointRequest.md)| The details of the agent mTLS endpoint to create. | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**RestResponseAgentMtlsEndpointDetails**](RestResponseAgentMtlsEndpointDetails.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_agent_mtls_endpoint_for_account**
> RestResponseBoolean delete_agent_mtls_endpoint_for_account(account_identifier)

Removes the agent mTLS endpoint for an account.

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
api_instance = harness_python_sdk.AgentMTLSEndpointManagementApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Removes the agent mTLS endpoint for an account.
    api_response = api_instance.delete_agent_mtls_endpoint_for_account(account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentMTLSEndpointManagementApi->delete_agent_mtls_endpoint_for_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**RestResponseBoolean**](RestResponseBoolean.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_mtls_endpoint_for_account**
> RestResponseAgentMtlsEndpointDetails get_agent_mtls_endpoint_for_account(account_identifier)

Gets the agent mTLS endpoint for an account.

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
api_instance = harness_python_sdk.AgentMTLSEndpointManagementApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Gets the agent mTLS endpoint for an account.
    api_response = api_instance.get_agent_mtls_endpoint_for_account(account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentMTLSEndpointManagementApi->get_agent_mtls_endpoint_for_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**RestResponseAgentMtlsEndpointDetails**](RestResponseAgentMtlsEndpointDetails.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_agent_mtls_endpoint_for_account**
> RestResponseAgentMtlsEndpointDetails patch_agent_mtls_endpoint_for_account(body, account_identifier)

Updates selected properties of the existing agent mTLS endpoint for an account.

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
api_instance = harness_python_sdk.AgentMTLSEndpointManagementApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.AgentMtlsEndpointRequest() # AgentMtlsEndpointRequest | A subset of the details to update for the agent mTLS endpoint.
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Updates selected properties of the existing agent mTLS endpoint for an account.
    api_response = api_instance.patch_agent_mtls_endpoint_for_account(body, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentMTLSEndpointManagementApi->patch_agent_mtls_endpoint_for_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AgentMtlsEndpointRequest**](AgentMtlsEndpointRequest.md)| A subset of the details to update for the agent mTLS endpoint. | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**RestResponseAgentMtlsEndpointDetails**](RestResponseAgentMtlsEndpointDetails.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_agent_mtls_endpoint_for_account**
> RestResponseAgentMtlsEndpointDetails update_agent_mtls_endpoint_for_account(body, account_identifier)

Updates the existing agent mTLS endpoint for an account.

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
api_instance = harness_python_sdk.AgentMTLSEndpointManagementApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.AgentMtlsEndpointRequest() # AgentMtlsEndpointRequest | The details to update for the agent mTLS endpoint.
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Updates the existing agent mTLS endpoint for an account.
    api_response = api_instance.update_agent_mtls_endpoint_for_account(body, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentMTLSEndpointManagementApi->update_agent_mtls_endpoint_for_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AgentMtlsEndpointRequest**](AgentMtlsEndpointRequest.md)| The details to update for the agent mTLS endpoint. | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**RestResponseAgentMtlsEndpointDetails**](RestResponseAgentMtlsEndpointDetails.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

