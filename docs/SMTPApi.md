# swagger_client.SMTPApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_smtp_config**](SMTPApi.md#create_smtp_config) | **POST** /ng/api/smtpConfig | Creates SMTP config
[**delete_smtp_config**](SMTPApi.md#delete_smtp_config) | **DELETE** /ng/api/smtpConfig/{identifier} | Delete Smtp Config by identifier
[**get_smtp_config**](SMTPApi.md#get_smtp_config) | **GET** /ng/api/smtpConfig | Gets Smtp config by accountId
[**update_smtp**](SMTPApi.md#update_smtp) | **PUT** /ng/api/smtpConfig | Updates the Smtp Config
[**validate_connectivity**](SMTPApi.md#validate_connectivity) | **POST** /ng/api/smtpConfig/validate-connectivity | Tests the config&#x27;s connectivity by sending a test email
[**validate_name**](SMTPApi.md#validate_name) | **POST** /ng/api/smtpConfig/validateName | Checks whether other connectors exist with the same name

# **create_smtp_config**
> ResponseDTONgSmtp create_smtp_config(body, account_identifier)

Creates SMTP config

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
api_instance = swagger_client.SMTPApi(swagger_client.ApiClient(configuration))
body = swagger_client.NgSmtp() # NgSmtp | 
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Creates SMTP config
    api_response = api_instance.create_smtp_config(body, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMTPApi->create_smtp_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NgSmtp**](NgSmtp.md)|  | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**ResponseDTONgSmtp**](ResponseDTONgSmtp.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_smtp_config**
> ResponseDTOBoolean delete_smtp_config(identifier, account_identifier)

Delete Smtp Config by identifier

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
api_instance = swagger_client.SMTPApi(swagger_client.ApiClient(configuration))
identifier = 'identifier_example' # str | Config identifier
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Delete Smtp Config by identifier
    api_response = api_instance.delete_smtp_config(identifier, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMTPApi->delete_smtp_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Config identifier | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**ResponseDTOBoolean**](ResponseDTOBoolean.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_smtp_config**
> ResponseDTONgSmtp get_smtp_config(account_id=account_id)

Gets Smtp config by accountId

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
api_instance = swagger_client.SMTPApi(swagger_client.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier for the Entity. (optional)

try:
    # Gets Smtp config by accountId
    api_response = api_instance.get_smtp_config(account_id=account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMTPApi->get_smtp_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTONgSmtp**](ResponseDTONgSmtp.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_smtp**
> ResponseDTONgSmtp update_smtp(body, account_identifier)

Updates the Smtp Config

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
api_instance = swagger_client.SMTPApi(swagger_client.ApiClient(configuration))
body = swagger_client.NgSmtp() # NgSmtp | 
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Updates the Smtp Config
    api_response = api_instance.update_smtp(body, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMTPApi->update_smtp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NgSmtp**](NgSmtp.md)|  | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**ResponseDTONgSmtp**](ResponseDTONgSmtp.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_connectivity**
> ResponseDTOValidationResult validate_connectivity(identifier, account_id, to, subject, body)

Tests the config's connectivity by sending a test email

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
api_instance = swagger_client.SMTPApi(swagger_client.ApiClient(configuration))
identifier = 'identifier_example' # str | Attribute uuid
account_id = 'account_id_example' # str | Account Identifier for the Entity.
to = 'to_example' # str | 
subject = 'subject_example' # str | 
body = 'body_example' # str | 

try:
    # Tests the config's connectivity by sending a test email
    api_response = api_instance.validate_connectivity(identifier, account_id, to, subject, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMTPApi->validate_connectivity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Attribute uuid | 
 **account_id** | **str**| Account Identifier for the Entity. | 
 **to** | **str**|  | 
 **subject** | **str**|  | 
 **body** | **str**|  | 

### Return type

[**ResponseDTOValidationResult**](ResponseDTOValidationResult.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_name**
> ResponseDTOValidationResult validate_name(account_id, name=name)

Checks whether other connectors exist with the same name

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
api_instance = swagger_client.SMTPApi(swagger_client.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier for the Entity.
name = 'name_example' # str | The name of Config (optional)

try:
    # Checks whether other connectors exist with the same name
    api_response = api_instance.validate_name(account_id, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMTPApi->validate_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier for the Entity. | 
 **name** | **str**| The name of Config | [optional] 

### Return type

[**ResponseDTOValidationResult**](ResponseDTOValidationResult.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

