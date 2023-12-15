# harness_python_sdk.NextgenLdapApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_ldap_authentication_test**](NextgenLdapApi.md#post_ldap_authentication_test) | **POST** /ng/api/ldap/ldap-login-test | Test LDAP authentication
[**search_ldap_groups**](NextgenLdapApi.md#search_ldap_groups) | **GET** /ng/api/ldap/{ldapId}/search/group | Return Ldap groups matching name

# **post_ldap_authentication_test**
> RestResponseLdapResponse post_ldap_authentication_test(account_identifier, email=email, password=password, org_identifier=org_identifier, project_identifier=project_identifier)

Test LDAP authentication

Tests LDAP authentication for the given Account ID, with a valid test email and password

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
api_instance = harness_python_sdk.NextgenLdapApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
email = 'email_example' # str |  (optional)
password = 'password_example' # str |  (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Test LDAP authentication
    api_response = api_instance.post_ldap_authentication_test(account_identifier, email=email, password=password, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NextgenLdapApi->post_ldap_authentication_test: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **email** | **str**|  | [optional] 
 **password** | **str**|  | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**RestResponseLdapResponse**](RestResponseLdapResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_ldap_groups**
> RestResponseCollectionLdapGroupResponse search_ldap_groups(ldap_id, account_identifier, name, org_identifier=org_identifier, project_identifier=project_identifier)

Return Ldap groups matching name

Returns all userGroups for the configured Ldap in the account matching a given name.

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
api_instance = harness_python_sdk.NextgenLdapApi(harness_python_sdk.ApiClient(configuration))
ldap_id = 'ldap_id_example' # str | Ldap setting id
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
name = 'name_example' # str | 
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Return Ldap groups matching name
    api_response = api_instance.search_ldap_groups(ldap_id, account_identifier, name, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NextgenLdapApi->search_ldap_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ldap_id** | **str**| Ldap setting id | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **name** | **str**|  | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**RestResponseCollectionLdapGroupResponse**](RestResponseCollectionLdapGroupResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

