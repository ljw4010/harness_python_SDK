# harness_python_sdk.OrgSecretApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_org_scoped_secret**](OrgSecretApi.md#create_org_scoped_secret) | **POST** /v1/orgs/{org}/secrets | Create a secret
[**delete_org_scoped_secret**](OrgSecretApi.md#delete_org_scoped_secret) | **DELETE** /v1/orgs/{org}/secrets/{secret} | Delete a secret
[**get_org_scoped_secret**](OrgSecretApi.md#get_org_scoped_secret) | **GET** /v1/orgs/{org}/secrets/{secret} | Retrieve a secret
[**get_org_scoped_secrets**](OrgSecretApi.md#get_org_scoped_secrets) | **GET** /v1/orgs/{org}/secrets | List secrets
[**update_org_scoped_secret**](OrgSecretApi.md#update_org_scoped_secret) | **PUT** /v1/orgs/{org}/secrets/{secret} | Update a secret
[**validate_org_secret_ref**](OrgSecretApi.md#validate_org_secret_ref) | **POST** /v1/orgs/{org}/secrets/validate-secret-ref | Validate secret reference

# **create_org_scoped_secret**
> SecretResponse create_org_scoped_secret(body, org, harness_account=harness_account, private_secret=private_secret)

Create a secret

Creates a new secret

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
api_instance = harness_python_sdk.OrgSecretApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.SecretRequest() # SecretRequest | 
org = 'org_example' # str | Identifier field of the organization the resource is scoped to
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)
private_secret = false # bool | This would be used to define secret as private. (optional) (default to false)

try:
    # Create a secret
    api_response = api_instance.create_org_scoped_secret(body, org, harness_account=harness_account, private_secret=private_secret)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgSecretApi->create_org_scoped_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SecretRequest**](SecretRequest.md)|  | 
 **org** | **str**| Identifier field of the organization the resource is scoped to | 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 
 **private_secret** | **bool**| This would be used to define secret as private. | [optional] [default to false]

### Return type

[**SecretResponse**](SecretResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml, multipart/form-data
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_org_scoped_secret**
> SecretResponse delete_org_scoped_secret(org, secret, harness_account=harness_account)

Delete a secret

Deletes the information of the secret with the matching secret identifier.

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
api_instance = harness_python_sdk.OrgSecretApi(harness_python_sdk.ApiClient(configuration))
org = 'org_example' # str | Identifier field of the organization the resource is scoped to
secret = 'secret_example' # str | Identifier field of the secret
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)

try:
    # Delete a secret
    api_response = api_instance.delete_org_scoped_secret(org, secret, harness_account=harness_account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgSecretApi->delete_org_scoped_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| Identifier field of the organization the resource is scoped to | 
 **secret** | **str**| Identifier field of the secret | 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 

### Return type

[**SecretResponse**](SecretResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_org_scoped_secret**
> SecretResponse get_org_scoped_secret(org, secret, harness_account=harness_account)

Retrieve a secret

Retrieves the information of the secret.

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
api_instance = harness_python_sdk.OrgSecretApi(harness_python_sdk.ApiClient(configuration))
org = 'org_example' # str | Identifier field of the organization the resource is scoped to
secret = 'secret_example' # str | Identifier field of the secret
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)

try:
    # Retrieve a secret
    api_response = api_instance.get_org_scoped_secret(org, secret, harness_account=harness_account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgSecretApi->get_org_scoped_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| Identifier field of the organization the resource is scoped to | 
 **secret** | **str**| Identifier field of the secret | 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 

### Return type

[**SecretResponse**](SecretResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_org_scoped_secrets**
> list[SecretResponse] get_org_scoped_secrets(org, secret=secret, type=type, recursive=recursive, search_term=search_term, page=page, limit=limit, harness_account=harness_account, sort=sort, order=order)

List secrets

Retrieves the information of the secrets.

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
api_instance = harness_python_sdk.OrgSecretApi(harness_python_sdk.ApiClient(configuration))
org = 'org_example' # str | Identifier field of the organization the resource is scoped to
secret = ['secret_example'] # list[str] | Identifier field of secrets (optional)
type = ['type_example'] # list[str] | Secret types on which the filter will be applied (optional)
recursive = false # bool | Expand current scope to include all child scopes  (optional) (default to false)
search_term = 'search_term_example' # str | This would be used to filter resources having attributes matching with search term. (optional)
page = 0 # int | Pagination page number strategy: Specify the page number within the paginated collection related to the number of items in each page  (optional) (default to 0)
limit = 30 # int | Number of items to return per page. (optional) (default to 30)
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)
sort = 'sort_example' # str | Parameter on the basis of which sorting is done. (optional)
order = 'order_example' # str | Order on the basis of which sorting is done. (optional)

try:
    # List secrets
    api_response = api_instance.get_org_scoped_secrets(org, secret=secret, type=type, recursive=recursive, search_term=search_term, page=page, limit=limit, harness_account=harness_account, sort=sort, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgSecretApi->get_org_scoped_secrets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| Identifier field of the organization the resource is scoped to | 
 **secret** | [**list[str]**](str.md)| Identifier field of secrets | [optional] 
 **type** | [**list[str]**](str.md)| Secret types on which the filter will be applied | [optional] 
 **recursive** | **bool**| Expand current scope to include all child scopes  | [optional] [default to false]
 **search_term** | **str**| This would be used to filter resources having attributes matching with search term. | [optional] 
 **page** | **int**| Pagination page number strategy: Specify the page number within the paginated collection related to the number of items in each page  | [optional] [default to 0]
 **limit** | **int**| Number of items to return per page. | [optional] [default to 30]
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 
 **sort** | **str**| Parameter on the basis of which sorting is done. | [optional] 
 **order** | **str**| Order on the basis of which sorting is done. | [optional] 

### Return type

[**list[SecretResponse]**](SecretResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_org_scoped_secret**
> SecretResponse update_org_scoped_secret(body, org, secret, harness_account=harness_account)

Update a secret

Updates the information of the secret with the matching secret identifier.

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
api_instance = harness_python_sdk.OrgSecretApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.SecretRequest() # SecretRequest | 
org = 'org_example' # str | Identifier field of the organization the resource is scoped to
secret = 'secret_example' # str | Identifier field of the secret
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)

try:
    # Update a secret
    api_response = api_instance.update_org_scoped_secret(body, org, secret, harness_account=harness_account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgSecretApi->update_org_scoped_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SecretRequest**](SecretRequest.md)|  | 
 **org** | **str**| Identifier field of the organization the resource is scoped to | 
 **secret** | **str**| Identifier field of the secret | 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 

### Return type

[**SecretResponse**](SecretResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml, multipart/form-data
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_org_secret_ref**
> SecretValidationResponse validate_org_secret_ref(org, body=body, harness_account=harness_account)

Validate secret reference

Validates if the secret at the secretManager path can be referenced

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
api_instance = harness_python_sdk.OrgSecretApi(harness_python_sdk.ApiClient(configuration))
org = 'org_example' # str | Identifier field of the organization the resource is scoped to
body = harness_python_sdk.SecretRequest() # SecretRequest | Details of the secret reference (optional)
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)

try:
    # Validate secret reference
    api_response = api_instance.validate_org_secret_ref(org, body=body, harness_account=harness_account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgSecretApi->validate_org_secret_ref: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| Identifier field of the organization the resource is scoped to | 
 **body** | [**SecretRequest**](SecretRequest.md)| Details of the secret reference | [optional] 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 

### Return type

[**SecretValidationResponse**](SecretValidationResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

