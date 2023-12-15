# harness_python_sdk.AuthenticationSettingsApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ldap_settings**](AuthenticationSettingsApi.md#create_ldap_settings) | **POST** /ng/api/authentication-settings/ldap/settings | Create Ldap setting
[**delete_ldap_settings**](AuthenticationSettingsApi.md#delete_ldap_settings) | **DELETE** /ng/api/authentication-settings/ldap/settings | Delete Ldap settings
[**delete_saml_meta_data**](AuthenticationSettingsApi.md#delete_saml_meta_data) | **DELETE** /ng/api/authentication-settings/delete-saml-metadata | Delete SAML meta data
[**delete_saml_meta_data_for_saml_ssoid**](AuthenticationSettingsApi.md#delete_saml_meta_data_for_saml_ssoid) | **DELETE** /ng/api/authentication-settings/saml-metadata/{samlSSOId}/delete | Delete SAML meta data for given SAML sso id
[**enable_disable_authentication_for_saml_setting**](AuthenticationSettingsApi.md#enable_disable_authentication_for_saml_setting) | **PUT** /ng/api/authentication-settings/saml-metadata-upload/{samlSSOId}/authentication | Update authentication enabled or not for given SAML setting
[**get_authentication_settings**](AuthenticationSettingsApi.md#get_authentication_settings) | **GET** /ng/api/authentication-settings | Gets authentication settings for the given Account ID
[**get_authentication_settings_v2**](AuthenticationSettingsApi.md#get_authentication_settings_v2) | **GET** /ng/api/authentication-settings/v2 | Gets authentication settings version 2 for the given Account ID
[**get_ldap_settings**](AuthenticationSettingsApi.md#get_ldap_settings) | **GET** /ng/api/authentication-settings/ldap/settings | Return configured Ldap settings for the account
[**get_password_strength_settings**](AuthenticationSettingsApi.md#get_password_strength_settings) | **GET** /ng/api/authentication-settings/login-settings/password-strength | Get password strength
[**get_saml_login_test**](AuthenticationSettingsApi.md#get_saml_login_test) | **GET** /ng/api/authentication-settings/saml-login-test | Test SAML connectivity
[**get_saml_login_test_v2**](AuthenticationSettingsApi.md#get_saml_login_test_v2) | **GET** /ng/api/authentication-settings/saml-login-test/{samlSSOId} | Test SAML connectivity
[**remove_oauth_mechanism**](AuthenticationSettingsApi.md#remove_oauth_mechanism) | **DELETE** /ng/api/authentication-settings/oauth/remove-mechanism | Delete OAuth Setting
[**set_public_access**](AuthenticationSettingsApi.md#set_public_access) | **PUT** /ng/api/authentication-settings/public-access | Enable/disable public access at account level
[**set_session_timeout_at_account_level**](AuthenticationSettingsApi.md#set_session_timeout_at_account_level) | **PUT** /ng/api/authentication-settings/session-timeout-account-level | Set session timeout at account level
[**set_two_factor_auth_at_account_level**](AuthenticationSettingsApi.md#set_two_factor_auth_at_account_level) | **PUT** /ng/api/authentication-settings/two-factor-admin-override-settings | Set two factor authorization
[**update_auth_mechanism**](AuthenticationSettingsApi.md#update_auth_mechanism) | **PUT** /ng/api/authentication-settings/update-auth-mechanism | Update Auth mechanism
[**update_ldap_settings**](AuthenticationSettingsApi.md#update_ldap_settings) | **PUT** /ng/api/authentication-settings/ldap/settings | Updates Ldap setting
[**update_oauth_providers**](AuthenticationSettingsApi.md#update_oauth_providers) | **PUT** /ng/api/authentication-settings/oauth/update-providers | Update Oauth providers
[**update_saml_meta_data**](AuthenticationSettingsApi.md#update_saml_meta_data) | **PUT** /ng/api/authentication-settings/saml-metadata-upload | Update SAML metadata
[**update_saml_meta_data_for_saml_ssoid**](AuthenticationSettingsApi.md#update_saml_meta_data_for_saml_ssoid) | **PUT** /ng/api/authentication-settings/saml-metadata-upload/{samlSSOId} | Update SAML metadata for a given SAML SSO Id
[**update_whitelisted_domains**](AuthenticationSettingsApi.md#update_whitelisted_domains) | **PUT** /ng/api/authentication-settings/whitelisted-domains | Updates the whitelisted domains
[**upload_saml_meta_data**](AuthenticationSettingsApi.md#upload_saml_meta_data) | **POST** /ng/api/authentication-settings/saml-metadata-upload | Upload SAML metadata

# **create_ldap_settings**
> RestResponseLDAPSettings create_ldap_settings(body, account_identifier)

Create Ldap setting

Creates Ldap settings along with the user, group queries.

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
api_instance = harness_python_sdk.AuthenticationSettingsApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.LDAPSettings() # LDAPSettings | Create LdapSettings request body. Values for connection settings are needed, user and group settings can also be provided
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Create Ldap setting
    api_response = api_instance.create_ldap_settings(body, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationSettingsApi->create_ldap_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LDAPSettings**](LDAPSettings.md)| Create LdapSettings request body. Values for connection settings are needed, user and group settings can also be provided | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**RestResponseLDAPSettings**](RestResponseLDAPSettings.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ldap_settings**
> RestResponseBoolean delete_ldap_settings(account_identifier)

Delete Ldap settings

Delete configured Ldap settings on this account.

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
api_instance = harness_python_sdk.AuthenticationSettingsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Delete Ldap settings
    api_response = api_instance.delete_ldap_settings(account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationSettingsApi->delete_ldap_settings: %s\n" % e)
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

# **delete_saml_meta_data**
> RestResponseSSOConfig delete_saml_meta_data(account_identifier)

Delete SAML meta data

Deletes SAML metadata for the given Account ID.

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
api_instance = harness_python_sdk.AuthenticationSettingsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Delete SAML meta data
    api_response = api_instance.delete_saml_meta_data(account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationSettingsApi->delete_saml_meta_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**RestResponseSSOConfig**](RestResponseSSOConfig.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_saml_meta_data_for_saml_ssoid**
> RestResponseSSOConfig delete_saml_meta_data_for_saml_ssoid(account_identifier, saml_ssoid)

Delete SAML meta data for given SAML sso id

Deletes SAML metadata for the given Account and SAML sso id

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
api_instance = harness_python_sdk.AuthenticationSettingsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
saml_ssoid = 'saml_ssoid_example' # str | Saml Settings Identifier

try:
    # Delete SAML meta data for given SAML sso id
    api_response = api_instance.delete_saml_meta_data_for_saml_ssoid(account_identifier, saml_ssoid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationSettingsApi->delete_saml_meta_data_for_saml_ssoid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **saml_ssoid** | **str**| Saml Settings Identifier | 

### Return type

[**RestResponseSSOConfig**](RestResponseSSOConfig.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_disable_authentication_for_saml_setting**
> RestResponseBoolean enable_disable_authentication_for_saml_setting(account_identifier, enable, saml_ssoid)

Update authentication enabled or not for given SAML setting

Updates if authentication is enabled or not for given SAML setting in Account ID.

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
api_instance = harness_python_sdk.AuthenticationSettingsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
enable = true # bool |  (default to true)
saml_ssoid = 'saml_ssoid_example' # str | Saml Settings Identifier

try:
    # Update authentication enabled or not for given SAML setting
    api_response = api_instance.enable_disable_authentication_for_saml_setting(account_identifier, enable, saml_ssoid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationSettingsApi->enable_disable_authentication_for_saml_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **enable** | **bool**|  | [default to true]
 **saml_ssoid** | **str**| Saml Settings Identifier | 

### Return type

[**RestResponseBoolean**](RestResponseBoolean.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_authentication_settings**
> RestResponseAuthenticationSettingsResponse get_authentication_settings(account_identifier)

Gets authentication settings for the given Account ID

Gets authentication settings for the given Account ID.

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
api_instance = harness_python_sdk.AuthenticationSettingsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Gets authentication settings for the given Account ID
    api_response = api_instance.get_authentication_settings(account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationSettingsApi->get_authentication_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**RestResponseAuthenticationSettingsResponse**](RestResponseAuthenticationSettingsResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_authentication_settings_v2**
> RestResponseAuthenticationSettingsResponse get_authentication_settings_v2(account_identifier)

Gets authentication settings version 2 for the given Account ID

Gets authentication settings version 2 for the given Account ID.

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
api_instance = harness_python_sdk.AuthenticationSettingsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Gets authentication settings version 2 for the given Account ID
    api_response = api_instance.get_authentication_settings_v2(account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationSettingsApi->get_authentication_settings_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**RestResponseAuthenticationSettingsResponse**](RestResponseAuthenticationSettingsResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ldap_settings**
> RestResponseLDAPSettings get_ldap_settings(account_identifier)

Return configured Ldap settings for the account

Returns configured Ldap settings and its details for the account.

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
api_instance = harness_python_sdk.AuthenticationSettingsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Return configured Ldap settings for the account
    api_response = api_instance.get_ldap_settings(account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationSettingsApi->get_ldap_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**RestResponseLDAPSettings**](RestResponseLDAPSettings.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_password_strength_settings**
> RestResponsePasswordStrengthPolicy get_password_strength_settings(account_identifier)

Get password strength

Gets password strength for the given Account ID.

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
api_instance = harness_python_sdk.AuthenticationSettingsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Get password strength
    api_response = api_instance.get_password_strength_settings(account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationSettingsApi->get_password_strength_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**RestResponsePasswordStrengthPolicy**](RestResponsePasswordStrengthPolicy.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_saml_login_test**
> RestResponseLoginTypeResponse get_saml_login_test(account_id)

Test SAML connectivity

Tests SAML connectivity for the given Account ID.

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
api_instance = harness_python_sdk.AuthenticationSettingsApi(harness_python_sdk.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier for the Entity.

try:
    # Test SAML connectivity
    api_response = api_instance.get_saml_login_test(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationSettingsApi->get_saml_login_test: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier for the Entity. | 

### Return type

[**RestResponseLoginTypeResponse**](RestResponseLoginTypeResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_saml_login_test_v2**
> RestResponseLoginTypeResponse get_saml_login_test_v2(account_identifier, saml_ssoid)

Test SAML connectivity

Tests SAML connectivity for the given Account ID and SAML setting.

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
api_instance = harness_python_sdk.AuthenticationSettingsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
saml_ssoid = 'saml_ssoid_example' # str | Saml Settings Identifier

try:
    # Test SAML connectivity
    api_response = api_instance.get_saml_login_test_v2(account_identifier, saml_ssoid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationSettingsApi->get_saml_login_test_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **saml_ssoid** | **str**| Saml Settings Identifier | 

### Return type

[**RestResponseLoginTypeResponse**](RestResponseLoginTypeResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_oauth_mechanism**
> RestResponseBoolean remove_oauth_mechanism(account_identifier)

Delete OAuth Setting

Deletes OAuth settings for a given Account ID.

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
api_instance = harness_python_sdk.AuthenticationSettingsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Delete OAuth Setting
    api_response = api_instance.remove_oauth_mechanism(account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationSettingsApi->remove_oauth_mechanism: %s\n" % e)
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

# **set_public_access**
> RestResponseBoolean set_public_access(body, account_identifier)

Enable/disable public access at account level

Enable/disable public access for the given Account ID.

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
api_instance = harness_python_sdk.AuthenticationSettingsApi(harness_python_sdk.ApiClient(configuration))
body = True # bool | Information about the session timeout for all users of this account in minutes.
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Enable/disable public access at account level
    api_response = api_instance.set_public_access(body, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationSettingsApi->set_public_access: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**bool**](bool.md)| Information about the session timeout for all users of this account in minutes. | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**RestResponseBoolean**](RestResponseBoolean.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_session_timeout_at_account_level**
> RestResponseBoolean set_session_timeout_at_account_level(body, account_identifier)

Set session timeout at account level

Sets session timeout of all users for the given Account ID.

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
api_instance = harness_python_sdk.AuthenticationSettingsApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.SessionTimeoutSettings() # SessionTimeoutSettings | Information about the session timeout for all users of this account in minutes.
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Set session timeout at account level
    api_response = api_instance.set_session_timeout_at_account_level(body, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationSettingsApi->set_session_timeout_at_account_level: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SessionTimeoutSettings**](SessionTimeoutSettings.md)| Information about the session timeout for all users of this account in minutes. | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**RestResponseBoolean**](RestResponseBoolean.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_two_factor_auth_at_account_level**
> RestResponseBoolean set_two_factor_auth_at_account_level(body, account_identifier)

Set two factor authorization

Sets Two-Factor authorization for the given Account ID.

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
api_instance = harness_python_sdk.AuthenticationSettingsApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.TwoFactorAdminOverrideSettings() # TwoFactorAdminOverrideSettings | Boolean that specify whether or not to override two factor enabled setting
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Set two factor authorization
    api_response = api_instance.set_two_factor_auth_at_account_level(body, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationSettingsApi->set_two_factor_auth_at_account_level: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TwoFactorAdminOverrideSettings**](TwoFactorAdminOverrideSettings.md)| Boolean that specify whether or not to override two factor enabled setting | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**RestResponseBoolean**](RestResponseBoolean.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_auth_mechanism**
> RestResponseBoolean update_auth_mechanism(account_identifier, authentication_mechanism=authentication_mechanism)

Update Auth mechanism

Updates the authentication mechanism for the given Account ID.

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
api_instance = harness_python_sdk.AuthenticationSettingsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
authentication_mechanism = 'authentication_mechanism_example' # str | Type of Authentication Mechanism SSO or NON_SSO (optional)

try:
    # Update Auth mechanism
    api_response = api_instance.update_auth_mechanism(account_identifier, authentication_mechanism=authentication_mechanism)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationSettingsApi->update_auth_mechanism: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **authentication_mechanism** | **str**| Type of Authentication Mechanism SSO or NON_SSO | [optional] 

### Return type

[**RestResponseBoolean**](RestResponseBoolean.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ldap_settings**
> RestResponseLDAPSettings update_ldap_settings(body, account_identifier)

Updates Ldap setting

Updates configured Ldap settings along with the user, group queries.

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
api_instance = harness_python_sdk.AuthenticationSettingsApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.LDAPSettings() # LDAPSettings | This is the updated LdapSettings. Values for all fields is needed, not just the fields you are updating
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Updates Ldap setting
    api_response = api_instance.update_ldap_settings(body, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationSettingsApi->update_ldap_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LDAPSettings**](LDAPSettings.md)| This is the updated LdapSettings. Values for all fields is needed, not just the fields you are updating | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**RestResponseLDAPSettings**](RestResponseLDAPSettings.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_oauth_providers**
> RestResponseBoolean update_oauth_providers(body, account_identifier)

Update Oauth providers

Updates OAuth providers for the given Account ID.

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
api_instance = harness_python_sdk.AuthenticationSettingsApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.OAuthSettings() # OAuthSettings | This is the updated OAuthSettings. Please provide values for all fields, not just the fields you are updating
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Update Oauth providers
    api_response = api_instance.update_oauth_providers(body, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationSettingsApi->update_oauth_providers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OAuthSettings**](OAuthSettings.md)| This is the updated OAuthSettings. Please provide values for all fields, not just the fields you are updating | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**RestResponseBoolean**](RestResponseBoolean.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_saml_meta_data**
> RestResponseSSOConfig update_saml_meta_data(account_id, file=file, file_metadata=file_metadata, display_name=display_name, group_membership_attr=group_membership_attr, authorization_enabled=authorization_enabled, logout_url=logout_url, entity_identifier=entity_identifier, saml_provider_type=saml_provider_type, client_id=client_id, client_secret=client_secret, jit_enabled=jit_enabled, jit_validation_key=jit_validation_key, jit_validation_value=jit_validation_value)

Update SAML metadata

Updates SAML metadata of the SAML configuration configured for an account

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
api_instance = harness_python_sdk.AuthenticationSettingsApi(harness_python_sdk.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier for the Entity.
file = NULL # object |  (optional)
file_metadata = harness_python_sdk.FormDataContentDisposition() # FormDataContentDisposition |  (optional)
display_name = 'display_name_example' # str |  (optional)
group_membership_attr = 'group_membership_attr_example' # str |  (optional)
authorization_enabled = true # bool |  (optional)
logout_url = 'logout_url_example' # str |  (optional)
entity_identifier = 'entity_identifier_example' # str |  (optional)
saml_provider_type = 'saml_provider_type_example' # str |  (optional)
client_id = 'client_id_example' # str |  (optional)
client_secret = 'client_secret_example' # str |  (optional)
jit_enabled = true # bool |  (optional)
jit_validation_key = 'jit_validation_key_example' # str |  (optional)
jit_validation_value = 'jit_validation_value_example' # str |  (optional)

try:
    # Update SAML metadata
    api_response = api_instance.update_saml_meta_data(account_id, file=file, file_metadata=file_metadata, display_name=display_name, group_membership_attr=group_membership_attr, authorization_enabled=authorization_enabled, logout_url=logout_url, entity_identifier=entity_identifier, saml_provider_type=saml_provider_type, client_id=client_id, client_secret=client_secret, jit_enabled=jit_enabled, jit_validation_key=jit_validation_key, jit_validation_value=jit_validation_value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationSettingsApi->update_saml_meta_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier for the Entity. | 
 **file** | [**object**](.md)|  | [optional] 
 **file_metadata** | [**FormDataContentDisposition**](.md)|  | [optional] 
 **display_name** | **str**|  | [optional] 
 **group_membership_attr** | **str**|  | [optional] 
 **authorization_enabled** | **bool**|  | [optional] 
 **logout_url** | **str**|  | [optional] 
 **entity_identifier** | **str**|  | [optional] 
 **saml_provider_type** | **str**|  | [optional] 
 **client_id** | **str**|  | [optional] 
 **client_secret** | **str**|  | [optional] 
 **jit_enabled** | **bool**|  | [optional] 
 **jit_validation_key** | **str**|  | [optional] 
 **jit_validation_value** | **str**|  | [optional] 

### Return type

[**RestResponseSSOConfig**](RestResponseSSOConfig.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_saml_meta_data_for_saml_ssoid**
> RestResponseSSOConfig update_saml_meta_data_for_saml_ssoid(account_identifier, saml_ssoid, file=file, file_metadata=file_metadata, display_name=display_name, group_membership_attr=group_membership_attr, authorization_enabled=authorization_enabled, logout_url=logout_url, entity_identifier=entity_identifier, saml_provider_type=saml_provider_type, client_id=client_id, client_secret=client_secret, friendly_saml_name=friendly_saml_name, jit_enabled=jit_enabled, jit_validation_key=jit_validation_key, jit_validation_value=jit_validation_value)

Update SAML metadata for a given SAML SSO Id

Updates SAML metadata of the SAML configuration with given SSO Id, configured for an account

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
api_instance = harness_python_sdk.AuthenticationSettingsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
saml_ssoid = 'saml_ssoid_example' # str | Saml Settings Identifier
file = NULL # object |  (optional)
file_metadata = harness_python_sdk.FormDataContentDisposition() # FormDataContentDisposition |  (optional)
display_name = 'display_name_example' # str |  (optional)
group_membership_attr = 'group_membership_attr_example' # str |  (optional)
authorization_enabled = true # bool |  (optional)
logout_url = 'logout_url_example' # str |  (optional)
entity_identifier = 'entity_identifier_example' # str |  (optional)
saml_provider_type = 'saml_provider_type_example' # str |  (optional)
client_id = 'client_id_example' # str |  (optional)
client_secret = 'client_secret_example' # str |  (optional)
friendly_saml_name = 'friendly_saml_name_example' # str |  (optional)
jit_enabled = true # bool |  (optional)
jit_validation_key = 'jit_validation_key_example' # str |  (optional)
jit_validation_value = 'jit_validation_value_example' # str |  (optional)

try:
    # Update SAML metadata for a given SAML SSO Id
    api_response = api_instance.update_saml_meta_data_for_saml_ssoid(account_identifier, saml_ssoid, file=file, file_metadata=file_metadata, display_name=display_name, group_membership_attr=group_membership_attr, authorization_enabled=authorization_enabled, logout_url=logout_url, entity_identifier=entity_identifier, saml_provider_type=saml_provider_type, client_id=client_id, client_secret=client_secret, friendly_saml_name=friendly_saml_name, jit_enabled=jit_enabled, jit_validation_key=jit_validation_key, jit_validation_value=jit_validation_value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationSettingsApi->update_saml_meta_data_for_saml_ssoid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **saml_ssoid** | **str**| Saml Settings Identifier | 
 **file** | [**object**](.md)|  | [optional] 
 **file_metadata** | [**FormDataContentDisposition**](.md)|  | [optional] 
 **display_name** | **str**|  | [optional] 
 **group_membership_attr** | **str**|  | [optional] 
 **authorization_enabled** | **bool**|  | [optional] 
 **logout_url** | **str**|  | [optional] 
 **entity_identifier** | **str**|  | [optional] 
 **saml_provider_type** | **str**|  | [optional] 
 **client_id** | **str**|  | [optional] 
 **client_secret** | **str**|  | [optional] 
 **friendly_saml_name** | **str**|  | [optional] 
 **jit_enabled** | **bool**|  | [optional] 
 **jit_validation_key** | **str**|  | [optional] 
 **jit_validation_value** | **str**|  | [optional] 

### Return type

[**RestResponseSSOConfig**](RestResponseSSOConfig.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_whitelisted_domains**
> RestResponseBoolean update_whitelisted_domains(account_identifier, body=body)

Updates the whitelisted domains

Updates whitelisted domains configured for an account.

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
api_instance = harness_python_sdk.AuthenticationSettingsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
body = ['body_example'] # list[str] | Set of whitelisted domains and IPs for the account (optional)

try:
    # Updates the whitelisted domains
    api_response = api_instance.update_whitelisted_domains(account_identifier, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationSettingsApi->update_whitelisted_domains: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **body** | [**list[str]**](str.md)| Set of whitelisted domains and IPs for the account | [optional] 

### Return type

[**RestResponseBoolean**](RestResponseBoolean.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_saml_meta_data**
> RestResponseSSOConfig upload_saml_meta_data(account_id, file=file, file_metadata=file_metadata, display_name=display_name, group_membership_attr=group_membership_attr, authorization_enabled=authorization_enabled, logout_url=logout_url, entity_identifier=entity_identifier, saml_provider_type=saml_provider_type, client_id=client_id, client_secret=client_secret, friendly_saml_name=friendly_saml_name, jit_enabled=jit_enabled, jit_validation_key=jit_validation_key, jit_validation_value=jit_validation_value)

Upload SAML metadata

Updates the SAML metadata for the given Account ID.

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
api_instance = harness_python_sdk.AuthenticationSettingsApi(harness_python_sdk.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier for the Entity.
file = NULL # object |  (optional)
file_metadata = harness_python_sdk.FormDataContentDisposition() # FormDataContentDisposition |  (optional)
display_name = 'display_name_example' # str |  (optional)
group_membership_attr = 'group_membership_attr_example' # str |  (optional)
authorization_enabled = true # bool |  (optional)
logout_url = 'logout_url_example' # str |  (optional)
entity_identifier = 'entity_identifier_example' # str |  (optional)
saml_provider_type = 'saml_provider_type_example' # str |  (optional)
client_id = 'client_id_example' # str |  (optional)
client_secret = 'client_secret_example' # str |  (optional)
friendly_saml_name = 'friendly_saml_name_example' # str |  (optional)
jit_enabled = true # bool |  (optional)
jit_validation_key = 'jit_validation_key_example' # str |  (optional)
jit_validation_value = 'jit_validation_value_example' # str |  (optional)

try:
    # Upload SAML metadata
    api_response = api_instance.upload_saml_meta_data(account_id, file=file, file_metadata=file_metadata, display_name=display_name, group_membership_attr=group_membership_attr, authorization_enabled=authorization_enabled, logout_url=logout_url, entity_identifier=entity_identifier, saml_provider_type=saml_provider_type, client_id=client_id, client_secret=client_secret, friendly_saml_name=friendly_saml_name, jit_enabled=jit_enabled, jit_validation_key=jit_validation_key, jit_validation_value=jit_validation_value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationSettingsApi->upload_saml_meta_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier for the Entity. | 
 **file** | [**object**](.md)|  | [optional] 
 **file_metadata** | [**FormDataContentDisposition**](.md)|  | [optional] 
 **display_name** | **str**|  | [optional] 
 **group_membership_attr** | **str**|  | [optional] 
 **authorization_enabled** | **bool**|  | [optional] 
 **logout_url** | **str**|  | [optional] 
 **entity_identifier** | **str**|  | [optional] 
 **saml_provider_type** | **str**|  | [optional] 
 **client_id** | **str**|  | [optional] 
 **client_secret** | **str**|  | [optional] 
 **friendly_saml_name** | **str**|  | [optional] 
 **jit_enabled** | **bool**|  | [optional] 
 **jit_validation_key** | **str**|  | [optional] 
 **jit_validation_value** | **str**|  | [optional] 

### Return type

[**RestResponseSSOConfig**](RestResponseSSOConfig.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

