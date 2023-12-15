# swagger_client.InviteApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_invite**](InviteApi.md#delete_invite) | **DELETE** /ng/api/invites/{inviteId} | Delete Invite
[**get_invite**](InviteApi.md#get_invite) | **GET** /ng/api/invites/invite | Get Invite
[**get_invites**](InviteApi.md#get_invites) | **GET** /ng/api/invites | List Invites
[**get_pending_users_aggregated**](InviteApi.md#get_pending_users_aggregated) | **POST** /ng/api/invites/aggregate | Get pending users
[**update_invite**](InviteApi.md#update_invite) | **PUT** /ng/api/invites/{inviteId} | Resend invite

# **delete_invite**
> ResponseDTOOptionalInvite delete_invite(account_identifier, invite_id)

Delete Invite

Delete an Invite by Identifier

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
api_instance = swagger_client.InviteApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
invite_id = 'invite_id_example' # str | Invite Id

try:
    # Delete Invite
    api_response = api_instance.delete_invite(account_identifier, invite_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InviteApi->delete_invite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **invite_id** | **str**| Invite Id | 

### Return type

[**ResponseDTOOptionalInvite**](ResponseDTOOptionalInvite.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invite**
> ResponseDTOInvite get_invite(account_identifier, invite_id=invite_id, jwttoken=jwttoken)

Get Invite

Gets an Invite by either Invite Id or JwtToken

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
api_instance = swagger_client.InviteApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
invite_id = 'invite_id_example' # str | Invitation Id (optional)
jwttoken = 'jwttoken_example' # str | JWT Token (optional)

try:
    # Get Invite
    api_response = api_instance.get_invite(account_identifier, invite_id=invite_id, jwttoken=jwttoken)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InviteApi->get_invite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **invite_id** | **str**| Invitation Id | [optional] 
 **jwttoken** | **str**| JWT Token | [optional] 

### Return type

[**ResponseDTOInvite**](ResponseDTOInvite.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, text/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invites**
> ResponseDTOPageResponseInvite get_invites(account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, page_index=page_index, page_size=page_size, sort_orders=sort_orders, page_token=page_token)

List Invites

List all the Invites for a Project or Organization

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
api_instance = swagger_client.InviteApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
page_index = 0 # int | Page Index of the results to fetch.Default Value: 0 (optional) (default to 0)
page_size = 50 # int | Results per page(max 100)Default Value: 50 (optional) (default to 50)
sort_orders = [swagger_client.SortOrder()] # list[SortOrder] | Sort criteria for the elements. (optional)
page_token = 'page_token_example' # str | Page Token of the next results to fetch.Default Value: '' (optional)

try:
    # List Invites
    api_response = api_instance.get_invites(account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, page_index=page_index, page_size=page_size, sort_orders=sort_orders, page_token=page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InviteApi->get_invites: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **page_index** | **int**| Page Index of the results to fetch.Default Value: 0 | [optional] [default to 0]
 **page_size** | **int**| Results per page(max 100)Default Value: 50 | [optional] [default to 50]
 **sort_orders** | [**list[SortOrder]**](SortOrder.md)| Sort criteria for the elements. | [optional] 
 **page_token** | **str**| Page Token of the next results to fetch.Default Value: &#x27;&#x27; | [optional] 

### Return type

[**ResponseDTOPageResponseInvite**](ResponseDTOPageResponseInvite.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, text/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pending_users_aggregated**
> ResponseDTOPageResponseInvite get_pending_users_aggregated(account_identifier, body=body, org_identifier=org_identifier, project_identifier=project_identifier, search_term=search_term, page_index=page_index, page_size=page_size, sort_orders=sort_orders, page_token=page_token)

Get pending users

List of all the pending users in a scope

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
api_instance = swagger_client.InviteApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
body = swagger_client.ACLAggregateFilter() # ACLAggregateFilter |  (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
search_term = 'search_term_example' # str | Search term (optional)
page_index = 0 # int | Page Index of the results to fetch.Default Value: 0 (optional) (default to 0)
page_size = 50 # int | Results per page(max 100)Default Value: 50 (optional) (default to 50)
sort_orders = [swagger_client.SortOrder()] # list[SortOrder] | Sort criteria for the elements. (optional)
page_token = 'page_token_example' # str | Page Token of the next results to fetch.Default Value: '' (optional)

try:
    # Get pending users
    api_response = api_instance.get_pending_users_aggregated(account_identifier, body=body, org_identifier=org_identifier, project_identifier=project_identifier, search_term=search_term, page_index=page_index, page_size=page_size, sort_orders=sort_orders, page_token=page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InviteApi->get_pending_users_aggregated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **body** | [**ACLAggregateFilter**](ACLAggregateFilter.md)|  | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **search_term** | **str**| Search term | [optional] 
 **page_index** | **int**| Page Index of the results to fetch.Default Value: 0 | [optional] [default to 0]
 **page_size** | **int**| Results per page(max 100)Default Value: 50 | [optional] [default to 50]
 **sort_orders** | [**list[SortOrder]**](SortOrder.md)| Sort criteria for the elements. | [optional] 
 **page_token** | **str**| Page Token of the next results to fetch.Default Value: &#x27;&#x27; | [optional] 

### Return type

[**ResponseDTOPageResponseInvite**](ResponseDTOPageResponseInvite.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, text/yaml
 - **Accept**: application/json, application/yaml, text/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_invite**
> ResponseDTOOptionalInvite update_invite(body, account_identifier, invite_id)

Resend invite

Resend the invite email

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
api_instance = swagger_client.InviteApi(swagger_client.ApiClient(configuration))
body = swagger_client.Invite() # Invite | Details of the Updated Invite
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
invite_id = 'invite_id_example' # str | Invite id

try:
    # Resend invite
    api_response = api_instance.update_invite(body, account_identifier, invite_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InviteApi->update_invite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Invite**](Invite.md)| Details of the Updated Invite | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **invite_id** | **str**| Invite id | 

### Return type

[**ResponseDTOOptionalInvite**](ResponseDTOOptionalInvite.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, text/yaml
 - **Accept**: application/json, application/yaml, text/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

