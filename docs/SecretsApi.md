# harness_python_sdk.SecretsApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_secret_v2**](SecretsApi.md#delete_secret_v2) | **DELETE** /ng/api/v2/secrets/{identifier} | Deletes Secret by ID and Scope
[**get_secret_v2**](SecretsApi.md#get_secret_v2) | **GET** /ng/api/v2/secrets/{identifier} | Get the Secret by ID and Scope
[**list_secrets_v2**](SecretsApi.md#list_secrets_v2) | **GET** /ng/api/v2/secrets | Fetches the list of Secrets corresponding to the request&#x27;s filter criteria.
[**list_secrets_v3**](SecretsApi.md#list_secrets_v3) | **POST** /ng/api/v2/secrets/list | Fetches the list of Secrets corresponding to the request&#x27;s filter criteria.
[**post_secret**](SecretsApi.md#post_secret) | **POST** /ng/api/v2/secrets | Creates a Secret at given Scope
[**post_secret_file_v2**](SecretsApi.md#post_secret_file_v2) | **POST** /ng/api/v2/secrets/files | Creates a Secret File
[**post_secret_via_yaml**](SecretsApi.md#post_secret_via_yaml) | **POST** /ng/api/v2/secrets/yaml | Creates a secret via YAML
[**put_secret**](SecretsApi.md#put_secret) | **PUT** /ng/api/v2/secrets/{identifier} | Updates the Secret by ID and Scope
[**put_secret_file_v2**](SecretsApi.md#put_secret_file_v2) | **PUT** /ng/api/v2/secrets/files/{identifier} | Updates the Secret file by ID and Scope
[**put_secret_via_yaml**](SecretsApi.md#put_secret_via_yaml) | **PUT** /ng/api/v2/secrets/{identifier}/yaml | Updates the Secret by ID and Scope via YAML
[**validate_secret**](SecretsApi.md#validate_secret) | **POST** /ng/api/v2/secrets/validate | Validates Secret with the provided ID and Scope
[**validate_secret_identifier_is_unique**](SecretsApi.md#validate_secret_identifier_is_unique) | **GET** /ng/api/v2/secrets/validateUniqueIdentifier/{identifier} | Checks whether the identifier is unique or not

# **delete_secret_v2**
> ResponseDTOBoolean delete_secret_v2(identifier, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, force_delete=force_delete)

Deletes Secret by ID and Scope

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
api_instance = harness_python_sdk.SecretsApi(harness_python_sdk.ApiClient(configuration))
identifier = 'identifier_example' # str | Secret ID
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
force_delete = false # bool | If true, the Entity will be forced delete, without checking any references/usages (optional) (default to false)

try:
    # Deletes Secret by ID and Scope
    api_response = api_instance.delete_secret_v2(identifier, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, force_delete=force_delete)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecretsApi->delete_secret_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Secret ID | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **force_delete** | **bool**| If true, the Entity will be forced delete, without checking any references/usages | [optional] [default to false]

### Return type

[**ResponseDTOBoolean**](ResponseDTOBoolean.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_secret_v2**
> ResponseDTOSecretResponse get_secret_v2(identifier, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Get the Secret by ID and Scope

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
api_instance = harness_python_sdk.SecretsApi(harness_python_sdk.ApiClient(configuration))
identifier = 'identifier_example' # str | Secret ID
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Get the Secret by ID and Scope
    api_response = api_instance.get_secret_v2(identifier, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecretsApi->get_secret_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Secret ID | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOSecretResponse**](ResponseDTOSecretResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_secrets_v2**
> ResponseDTOPageResponseSecretResponse list_secrets_v2(account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, identifiers=identifiers, type=type, search_term=search_term, types=types, source_category=source_category, include_secrets_from_every_sub_scope=include_secrets_from_every_sub_scope, include_all_secrets_accessible_at_scope=include_all_secrets_accessible_at_scope, page_index=page_index, page_size=page_size, sort_orders=sort_orders, page_token=page_token)

Fetches the list of Secrets corresponding to the request's filter criteria.

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
api_instance = harness_python_sdk.SecretsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
identifiers = ['identifiers_example'] # list[str] | This is the list of Secret IDs. Details specific to these IDs would be fetched. (optional)
type = 'type_example' # str | Type of Secret whether it is SecretFile, SecretText or SSH key (optional)
search_term = 'search_term_example' # str | Filter Secrets based on name, Identifier and tags by this search term (optional)
types = ['types_example'] # list[str] | Add multiple secret types like SecretFile, SecretText or SSH key to criteria (optional)
source_category = 'source_category_example' # str | Source Category like CLOUD_PROVIDER, SECRET_MANAGER, CLOUD_COST, ARTIFACTORY, CODE_REPO, MONITORING or TICKETING (optional)
include_secrets_from_every_sub_scope = false # bool | Specify whether or not to include secrets from all the sub-scopes of the given Scope (optional) (default to false)
include_all_secrets_accessible_at_scope = false # bool | Specify whether or not to include all the Secrets accessible at the scope. For eg if set as true, at the Project scope we will get org and account Secrets also in the response (optional) (default to false)
page_index = 0 # int | Page Index of the results to fetch.Default Value: 0 (optional) (default to 0)
page_size = 50 # int | Results per page(max 100)Default Value: 50 (optional) (default to 50)
sort_orders = [harness_python_sdk.SortOrder()] # list[SortOrder] | Sort criteria for the elements. (optional)
page_token = 'page_token_example' # str | Page Token of the next results to fetch.Default Value: '' (optional)

try:
    # Fetches the list of Secrets corresponding to the request's filter criteria.
    api_response = api_instance.list_secrets_v2(account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, identifiers=identifiers, type=type, search_term=search_term, types=types, source_category=source_category, include_secrets_from_every_sub_scope=include_secrets_from_every_sub_scope, include_all_secrets_accessible_at_scope=include_all_secrets_accessible_at_scope, page_index=page_index, page_size=page_size, sort_orders=sort_orders, page_token=page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecretsApi->list_secrets_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **identifiers** | [**list[str]**](str.md)| This is the list of Secret IDs. Details specific to these IDs would be fetched. | [optional] 
 **type** | **str**| Type of Secret whether it is SecretFile, SecretText or SSH key | [optional] 
 **search_term** | **str**| Filter Secrets based on name, Identifier and tags by this search term | [optional] 
 **types** | [**list[str]**](str.md)| Add multiple secret types like SecretFile, SecretText or SSH key to criteria | [optional] 
 **source_category** | **str**| Source Category like CLOUD_PROVIDER, SECRET_MANAGER, CLOUD_COST, ARTIFACTORY, CODE_REPO, MONITORING or TICKETING | [optional] 
 **include_secrets_from_every_sub_scope** | **bool**| Specify whether or not to include secrets from all the sub-scopes of the given Scope | [optional] [default to false]
 **include_all_secrets_accessible_at_scope** | **bool**| Specify whether or not to include all the Secrets accessible at the scope. For eg if set as true, at the Project scope we will get org and account Secrets also in the response | [optional] [default to false]
 **page_index** | **int**| Page Index of the results to fetch.Default Value: 0 | [optional] [default to 0]
 **page_size** | **int**| Results per page(max 100)Default Value: 50 | [optional] [default to 50]
 **sort_orders** | [**list[SortOrder]**](SortOrder.md)| Sort criteria for the elements. | [optional] 
 **page_token** | **str**| Page Token of the next results to fetch.Default Value: &#x27;&#x27; | [optional] 

### Return type

[**ResponseDTOPageResponseSecretResponse**](ResponseDTOPageResponseSecretResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_secrets_v3**
> ResponseDTOPageResponseSecretResponse list_secrets_v3(account_identifier, body=body, org_identifier=org_identifier, project_identifier=project_identifier, page_index=page_index, page_size=page_size, sort_orders=sort_orders, page_token=page_token)

Fetches the list of Secrets corresponding to the request's filter criteria.

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
api_instance = harness_python_sdk.SecretsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
body = harness_python_sdk.SecretResourceFilter() # SecretResourceFilter |  (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
page_index = 0 # int | Page Index of the results to fetch.Default Value: 0 (optional) (default to 0)
page_size = 50 # int | Results per page(max 100)Default Value: 50 (optional) (default to 50)
sort_orders = [harness_python_sdk.SortOrder()] # list[SortOrder] | Sort criteria for the elements. (optional)
page_token = 'page_token_example' # str | Page Token of the next results to fetch.Default Value: '' (optional)

try:
    # Fetches the list of Secrets corresponding to the request's filter criteria.
    api_response = api_instance.list_secrets_v3(account_identifier, body=body, org_identifier=org_identifier, project_identifier=project_identifier, page_index=page_index, page_size=page_size, sort_orders=sort_orders, page_token=page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecretsApi->list_secrets_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **body** | [**SecretResourceFilter**](SecretResourceFilter.md)|  | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **page_index** | **int**| Page Index of the results to fetch.Default Value: 0 | [optional] [default to 0]
 **page_size** | **int**| Results per page(max 100)Default Value: 50 | [optional] [default to 50]
 **sort_orders** | [**list[SortOrder]**](SortOrder.md)| Sort criteria for the elements. | [optional] 
 **page_token** | **str**| Page Token of the next results to fetch.Default Value: &#x27;&#x27; | [optional] 

### Return type

[**ResponseDTOPageResponseSecretResponse**](ResponseDTOPageResponseSecretResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_secret**
> ResponseDTOSecretResponse post_secret(body, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, private_secret=private_secret)

Creates a Secret at given Scope

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
api_instance = harness_python_sdk.SecretsApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.SecretRequestWrapper() # SecretRequestWrapper | Details required to create the Secret
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
private_secret = false # bool | This is a boolean value to specify if the Secret is Private. The default value is False. (optional) (default to false)

try:
    # Creates a Secret at given Scope
    api_response = api_instance.post_secret(body, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, private_secret=private_secret)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecretsApi->post_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SecretRequestWrapper**](SecretRequestWrapper.md)| Details required to create the Secret | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **private_secret** | **bool**| This is a boolean value to specify if the Secret is Private. The default value is False. | [optional] [default to false]

### Return type

[**ResponseDTOSecretResponse**](ResponseDTOSecretResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_secret_file_v2**
> ResponseDTOSecretResponse post_secret_file_v2(account_identifier, file=file, spec=spec, org_identifier=org_identifier, project_identifier=project_identifier, private_secret=private_secret)

Creates a Secret File

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
api_instance = harness_python_sdk.SecretsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
file = NULL # object |  (optional)
spec = 'spec_example' # str |  (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
private_secret = false # bool | This is a boolean value to specify if the Secret is Private. The default value is False. (optional) (default to false)

try:
    # Creates a Secret File
    api_response = api_instance.post_secret_file_v2(account_identifier, file=file, spec=spec, org_identifier=org_identifier, project_identifier=project_identifier, private_secret=private_secret)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecretsApi->post_secret_file_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **file** | [**object**](.md)|  | [optional] 
 **spec** | **str**|  | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **private_secret** | **bool**| This is a boolean value to specify if the Secret is Private. The default value is False. | [optional] [default to false]

### Return type

[**ResponseDTOSecretResponse**](ResponseDTOSecretResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_secret_via_yaml**
> ResponseDTOSecretResponse post_secret_via_yaml(body, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, private_secret=private_secret)

Creates a secret via YAML

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
api_instance = harness_python_sdk.SecretsApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.SecretRequestWrapper() # SecretRequestWrapper | Details required to create the Secret
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
private_secret = false # bool | This is a boolean value to specify if the Secret is Private. The default value is False. (optional) (default to false)

try:
    # Creates a secret via YAML
    api_response = api_instance.post_secret_via_yaml(body, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, private_secret=private_secret)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecretsApi->post_secret_via_yaml: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SecretRequestWrapper**](SecretRequestWrapper.md)| Details required to create the Secret | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **private_secret** | **bool**| This is a boolean value to specify if the Secret is Private. The default value is False. | [optional] [default to false]

### Return type

[**ResponseDTOSecretResponse**](ResponseDTOSecretResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_secret**
> ResponseDTOSecretResponse put_secret(account_identifier, identifier, body=body, org_identifier=org_identifier, project_identifier=project_identifier)

Updates the Secret by ID and Scope

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
api_instance = harness_python_sdk.SecretsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
identifier = 'identifier_example' # str | Secret ID
body = harness_python_sdk.SecretRequestWrapper() # SecretRequestWrapper |  (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Updates the Secret by ID and Scope
    api_response = api_instance.put_secret(account_identifier, identifier, body=body, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecretsApi->put_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **identifier** | **str**| Secret ID | 
 **body** | [**SecretRequestWrapper**](SecretRequestWrapper.md)|  | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOSecretResponse**](ResponseDTOSecretResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_secret_file_v2**
> ResponseDTOSecretResponse put_secret_file_v2(account_identifier, identifier, file=file, spec=spec, org_identifier=org_identifier, project_identifier=project_identifier)

Updates the Secret file by ID and Scope

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
api_instance = harness_python_sdk.SecretsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
identifier = 'identifier_example' # str | Secret ID
file = NULL # object |  (optional)
spec = 'spec_example' # str |  (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Updates the Secret file by ID and Scope
    api_response = api_instance.put_secret_file_v2(account_identifier, identifier, file=file, spec=spec, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecretsApi->put_secret_file_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **identifier** | **str**| Secret ID | 
 **file** | [**object**](.md)|  | [optional] 
 **spec** | **str**|  | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOSecretResponse**](ResponseDTOSecretResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_secret_via_yaml**
> ResponseDTOSecretResponse put_secret_via_yaml(body, account_identifier, identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Updates the Secret by ID and Scope via YAML

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
api_instance = harness_python_sdk.SecretsApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.SecretRequestWrapper() # SecretRequestWrapper | Details of Secret to create
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
identifier = 'identifier_example' # str | Secret ID
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Updates the Secret by ID and Scope via YAML
    api_response = api_instance.put_secret_via_yaml(body, account_identifier, identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecretsApi->put_secret_via_yaml: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SecretRequestWrapper**](SecretRequestWrapper.md)| Details of Secret to create | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **identifier** | **str**| Secret ID | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOSecretResponse**](ResponseDTOSecretResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_secret**
> ResponseDTOSecretValidationResult validate_secret(body, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, identifier=identifier)

Validates Secret with the provided ID and Scope

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
api_instance = harness_python_sdk.SecretsApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.SecretValidationMetaData() # SecretValidationMetaData | Details of the Secret type
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
identifier = 'identifier_example' # str | Secret ID (optional)

try:
    # Validates Secret with the provided ID and Scope
    api_response = api_instance.validate_secret(body, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, identifier=identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecretsApi->validate_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SecretValidationMetaData**](SecretValidationMetaData.md)| Details of the Secret type | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **identifier** | **str**| Secret ID | [optional] 

### Return type

[**ResponseDTOSecretValidationResult**](ResponseDTOSecretValidationResult.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_secret_identifier_is_unique**
> ResponseDTOBoolean validate_secret_identifier_is_unique(identifier, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Checks whether the identifier is unique or not

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
api_instance = harness_python_sdk.SecretsApi(harness_python_sdk.ApiClient(configuration))
identifier = 'identifier_example' # str | Secret Identifier
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Checks whether the identifier is unique or not
    api_response = api_instance.validate_secret_identifier_is_unique(identifier, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecretsApi->validate_secret_identifier_is_unique: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Secret Identifier | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOBoolean**](ResponseDTOBoolean.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

