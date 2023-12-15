# swagger_client.DelegateTokenResourceApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_delegate_token**](DelegateTokenResourceApi.md#create_delegate_token) | **POST** /ng/api/delegate-token-ng | Creates Delegate Token.
[**get_delegate_groups_using_token**](DelegateTokenResourceApi.md#get_delegate_groups_using_token) | **GET** /ng/api/delegate-token-ng/delegate-groups | Lists delegate groups that are using the specified delegate token.
[**get_delegate_tokens**](DelegateTokenResourceApi.md#get_delegate_tokens) | **GET** /ng/api/delegate-token-ng | Retrieves Delegate Tokens by Account, Organization, Project and status.
[**revoke_delegate_token**](DelegateTokenResourceApi.md#revoke_delegate_token) | **PUT** /ng/api/delegate-token-ng | Revokes Delegate Token.

# **create_delegate_token**
> RestResponseDelegateTokenDetails create_delegate_token(account_identifier, token_name, org_identifier=org_identifier, project_identifier=project_identifier, revoke_after=revoke_after)

Creates Delegate Token.

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
api_instance = swagger_client.DelegateTokenResourceApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
token_name = 'token_name_example' # str | Delegate Token name
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
revoke_after = 789 # int | Epoch time in milliseconds after which the token will be marked as revoked. There can be a delay of upto one hour from the epoch value provided and actual revoking of the token. (optional)

try:
    # Creates Delegate Token.
    api_response = api_instance.create_delegate_token(account_identifier, token_name, org_identifier=org_identifier, project_identifier=project_identifier, revoke_after=revoke_after)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DelegateTokenResourceApi->create_delegate_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **token_name** | **str**| Delegate Token name | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **revoke_after** | **int**| Epoch time in milliseconds after which the token will be marked as revoked. There can be a delay of upto one hour from the epoch value provided and actual revoking of the token. | [optional] 

### Return type

[**RestResponseDelegateTokenDetails**](RestResponseDelegateTokenDetails.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_delegate_groups_using_token**
> RestResponseDelegateGroupListing get_delegate_groups_using_token(account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, delegate_token_name=delegate_token_name)

Lists delegate groups that are using the specified delegate token.

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
api_instance = swagger_client.DelegateTokenResourceApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
delegate_token_name = 'delegate_token_name_example' # str | Delegate Token name (optional)

try:
    # Lists delegate groups that are using the specified delegate token.
    api_response = api_instance.get_delegate_groups_using_token(account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, delegate_token_name=delegate_token_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DelegateTokenResourceApi->get_delegate_groups_using_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **delegate_token_name** | **str**| Delegate Token name | [optional] 

### Return type

[**RestResponseDelegateGroupListing**](RestResponseDelegateGroupListing.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_delegate_tokens**
> RestResponseListDelegateTokenDetails get_delegate_tokens(account_identifier, name=name, org_identifier=org_identifier, project_identifier=project_identifier, status=status)

Retrieves Delegate Tokens by Account, Organization, Project and status.

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
api_instance = swagger_client.DelegateTokenResourceApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
name = 'name_example' # str | Name of Delegate Token (ACTIVE or REVOKED). (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
status = 'status_example' # str | Status of Delegate Token (ACTIVE or REVOKED). If left empty both active and revoked tokens will be retrieved (optional)

try:
    # Retrieves Delegate Tokens by Account, Organization, Project and status.
    api_response = api_instance.get_delegate_tokens(account_identifier, name=name, org_identifier=org_identifier, project_identifier=project_identifier, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DelegateTokenResourceApi->get_delegate_tokens: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **name** | **str**| Name of Delegate Token (ACTIVE or REVOKED). | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **status** | **str**| Status of Delegate Token (ACTIVE or REVOKED). If left empty both active and revoked tokens will be retrieved | [optional] 

### Return type

[**RestResponseListDelegateTokenDetails**](RestResponseListDelegateTokenDetails.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_delegate_token**
> RestResponseDelegateTokenDetails revoke_delegate_token(account_identifier, token_name, org_identifier=org_identifier, project_identifier=project_identifier)

Revokes Delegate Token.

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
api_instance = swagger_client.DelegateTokenResourceApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
token_name = 'token_name_example' # str | Delegate Token name
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Revokes Delegate Token.
    api_response = api_instance.revoke_delegate_token(account_identifier, token_name, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DelegateTokenResourceApi->revoke_delegate_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **token_name** | **str**| Delegate Token name | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**RestResponseDelegateTokenDetails**](RestResponseDelegateTokenDetails.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

