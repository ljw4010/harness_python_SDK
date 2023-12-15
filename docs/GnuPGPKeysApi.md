# swagger_client.GnuPGPKeysApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**agent_gpg_key_service_create**](GnuPGPKeysApi.md#agent_gpg_key_service_create) | **POST** /gitops/api/v1/agents/{agentIdentifier}/gpgkeys | Create one or more GPG public keys in the server&#x27;s configuration
[**agent_gpg_key_service_delete**](GnuPGPKeysApi.md#agent_gpg_key_service_delete) | **DELETE** /gitops/api/v1/agents/{agentIdentifier}/gpgkeys/{query.keyID} | Delete specified GPG public key from the server&#x27;s configuration
[**agent_gpg_key_service_get**](GnuPGPKeysApi.md#agent_gpg_key_service_get) | **GET** /gitops/api/v1/agents/{agentIdentifier}/gpgkeys/{query.keyID} | Get information about specified GPG public key from the server

# **agent_gpg_key_service_create**
> GpgkeysGnuPGPublicKeyCreateResponse agent_gpg_key_service_create(body, agent_identifier, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Create one or more GPG public keys in the server's configuration

Create one or more GPG public keys in the server's configuration.

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
api_instance = swagger_client.GnuPGPKeysApi(swagger_client.ApiClient(configuration))
body = swagger_client.GpgkeysGnuPGPublicKeyCreateRequest() # GpgkeysGnuPGPublicKeyCreateRequest | 
agent_identifier = 'agent_identifier_example' # str | Agent identifier for entity.
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity. (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Create one or more GPG public keys in the server's configuration
    api_response = api_instance.agent_gpg_key_service_create(body, agent_identifier, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GnuPGPKeysApi->agent_gpg_key_service_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GpgkeysGnuPGPublicKeyCreateRequest**](GpgkeysGnuPGPublicKeyCreateRequest.md)|  | 
 **agent_identifier** | **str**| Agent identifier for entity. | 
 **account_identifier** | **str**| Account Identifier for the Entity. | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**GpgkeysGnuPGPublicKeyCreateResponse**](GpgkeysGnuPGPublicKeyCreateResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_gpg_key_service_delete**
> GpgkeysGnuPGPublicKeyResponse agent_gpg_key_service_delete(agent_identifier, query_key_id, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Delete specified GPG public key from the server's configuration

Delete specified GPG public key from the server's configuration.

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
api_instance = swagger_client.GnuPGPKeysApi(swagger_client.ApiClient(configuration))
agent_identifier = 'agent_identifier_example' # str | Agent identifier for entity.
query_key_id = 'query_key_id_example' # str | The GPG key ID to query for
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity. (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Delete specified GPG public key from the server's configuration
    api_response = api_instance.agent_gpg_key_service_delete(agent_identifier, query_key_id, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GnuPGPKeysApi->agent_gpg_key_service_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_identifier** | **str**| Agent identifier for entity. | 
 **query_key_id** | **str**| The GPG key ID to query for | 
 **account_identifier** | **str**| Account Identifier for the Entity. | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**GpgkeysGnuPGPublicKeyResponse**](GpgkeysGnuPGPublicKeyResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_gpg_key_service_get**
> GpgkeysGnuPGPublicKey agent_gpg_key_service_get(agent_identifier, query_key_id, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Get information about specified GPG public key from the server

Get information about specified GPG public key from the server.

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
api_instance = swagger_client.GnuPGPKeysApi(swagger_client.ApiClient(configuration))
agent_identifier = 'agent_identifier_example' # str | Agent identifier for entity.
query_key_id = 'query_key_id_example' # str | The GPG key ID to query for
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Get information about specified GPG public key from the server
    api_response = api_instance.agent_gpg_key_service_get(agent_identifier, query_key_id, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GnuPGPKeysApi->agent_gpg_key_service_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_identifier** | **str**| Agent identifier for entity. | 
 **query_key_id** | **str**| The GPG key ID to query for | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**GpgkeysGnuPGPublicKey**](GpgkeysGnuPGPublicKey.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

