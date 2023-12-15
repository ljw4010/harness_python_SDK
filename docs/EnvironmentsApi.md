# harness_python_sdk.EnvironmentsApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_environment_v2**](EnvironmentsApi.md#create_environment_v2) | **POST** /ng/api/environmentsV2 | Create an Environment
[**delete_environment_v2**](EnvironmentsApi.md#delete_environment_v2) | **DELETE** /ng/api/environmentsV2/{environmentIdentifier} | Delete an Environment by identifier
[**delete_service_override**](EnvironmentsApi.md#delete_service_override) | **DELETE** /ng/api/environmentsV2/serviceOverrides | Delete a ServiceOverride entity
[**get_environment_access_list**](EnvironmentsApi.md#get_environment_access_list) | **GET** /ng/api/environmentsV2/list/access | Gets Environment Access list
[**get_environment_list**](EnvironmentsApi.md#get_environment_list) | **GET** /ng/api/environmentsV2 | Gets Environment list for a project
[**get_environment_v2**](EnvironmentsApi.md#get_environment_v2) | **GET** /ng/api/environmentsV2/{environmentIdentifier} | Gets an Environment by identifier
[**get_service_overrides_list**](EnvironmentsApi.md#get_service_overrides_list) | **GET** /ng/api/environmentsV2/serviceOverrides | Gets Service Overrides list
[**update_environment_v2**](EnvironmentsApi.md#update_environment_v2) | **PUT** /ng/api/environmentsV2 | Update an Environment by identifier
[**upsert_environment_v2**](EnvironmentsApi.md#upsert_environment_v2) | **PUT** /ng/api/environmentsV2/upsert | Upsert an Environment by identifier
[**upsert_service_override**](EnvironmentsApi.md#upsert_service_override) | **POST** /ng/api/environmentsV2/serviceOverrides | upsert a Service Override for an Environment

# **create_environment_v2**
> ResponseDTOEnvironmentResponse create_environment_v2(account_identifier, body=body)

Create an Environment

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
api_instance = harness_python_sdk.EnvironmentsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
body = harness_python_sdk.EnvironmentRequest() # EnvironmentRequest | Details of the Environment to be created (optional)

try:
    # Create an Environment
    api_response = api_instance.create_environment_v2(account_identifier, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentsApi->create_environment_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **body** | [**EnvironmentRequest**](EnvironmentRequest.md)| Details of the Environment to be created | [optional] 

### Return type

[**ResponseDTOEnvironmentResponse**](ResponseDTOEnvironmentResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_environment_v2**
> ResponseDTOBoolean delete_environment_v2(environment_identifier, account_identifier, if_match=if_match, org_identifier=org_identifier, project_identifier=project_identifier, force_delete=force_delete)

Delete an Environment by identifier

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
api_instance = harness_python_sdk.EnvironmentsApi(harness_python_sdk.ApiClient(configuration))
environment_identifier = 'environment_identifier_example' # str | Environment Identifier for the entity
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
if_match = 'if_match_example' # str |  (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
force_delete = false # bool | If true, the Entity will be forced delete, without checking any references/usages (optional) (default to false)

try:
    # Delete an Environment by identifier
    api_response = api_instance.delete_environment_v2(environment_identifier, account_identifier, if_match=if_match, org_identifier=org_identifier, project_identifier=project_identifier, force_delete=force_delete)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentsApi->delete_environment_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_identifier** | **str**| Environment Identifier for the entity | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **if_match** | **str**|  | [optional] 
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

# **delete_service_override**
> ResponseDTOBoolean delete_service_override(account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, environment_identifier=environment_identifier, service_identifier=service_identifier)

Delete a ServiceOverride entity

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
api_instance = harness_python_sdk.EnvironmentsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
environment_identifier = 'environment_identifier_example' # str | Environment Identifier for the Entity. (optional)
service_identifier = 'service_identifier_example' # str | Service Identifier for the Entity. (optional)

try:
    # Delete a ServiceOverride entity
    api_response = api_instance.delete_service_override(account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, environment_identifier=environment_identifier, service_identifier=service_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentsApi->delete_service_override: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **environment_identifier** | **str**| Environment Identifier for the Entity. | [optional] 
 **service_identifier** | **str**| Service Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOBoolean**](ResponseDTOBoolean.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_environment_access_list**
> ResponseDTOListEnvironmentResponse get_environment_access_list(account_identifier, page=page, size=size, org_identifier=org_identifier, project_identifier=project_identifier, search_term=search_term, env_identifiers=env_identifiers, env_group_identifier=env_group_identifier, sort=sort)

Gets Environment Access list

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
api_instance = harness_python_sdk.EnvironmentsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
page = 0 # int | page (optional) (default to 0)
size = 100 # int | size (optional) (default to 100)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
search_term = 'search_term_example' # str | The word to be searched and included in the list response (optional)
env_identifiers = ['env_identifiers_example'] # list[str] | List of EnvironmentIds (optional)
env_group_identifier = 'env_group_identifier_example' # str | Environment group identifier (optional)
sort = ['sort_example'] # list[str] | Specifies sorting criteria of the list. Like sorting based on the last updated entity, alphabetical sorting in an ascending or descending order (optional)

try:
    # Gets Environment Access list
    api_response = api_instance.get_environment_access_list(account_identifier, page=page, size=size, org_identifier=org_identifier, project_identifier=project_identifier, search_term=search_term, env_identifiers=env_identifiers, env_group_identifier=env_group_identifier, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentsApi->get_environment_access_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **page** | **int**| page | [optional] [default to 0]
 **size** | **int**| size | [optional] [default to 100]
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **search_term** | **str**| The word to be searched and included in the list response | [optional] 
 **env_identifiers** | [**list[str]**](str.md)| List of EnvironmentIds | [optional] 
 **env_group_identifier** | **str**| Environment group identifier | [optional] 
 **sort** | [**list[str]**](str.md)| Specifies sorting criteria of the list. Like sorting based on the last updated entity, alphabetical sorting in an ascending or descending order | [optional] 

### Return type

[**ResponseDTOListEnvironmentResponse**](ResponseDTOListEnvironmentResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_environment_list**
> ResponseDTOPageResponseEnvironmentResponse get_environment_list(account_identifier, page=page, size=size, org_identifier=org_identifier, project_identifier=project_identifier, search_term=search_term, env_identifiers=env_identifiers, sort=sort)

Gets Environment list for a project

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
api_instance = harness_python_sdk.EnvironmentsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
page = 0 # int | Page Index of the results to fetch.Default Value: 0 (optional) (default to 0)
size = 100 # int | Results per page (optional) (default to 100)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
search_term = 'search_term_example' # str | The word to be searched and included in the list response (optional)
env_identifiers = ['env_identifiers_example'] # list[str] | List of EnvironmentIds (optional)
sort = ['sort_example'] # list[str] | Specifies sorting criteria of the list. Like sorting based on the last updated entity, alphabetical sorting in an ascending or descending order (optional)

try:
    # Gets Environment list for a project
    api_response = api_instance.get_environment_list(account_identifier, page=page, size=size, org_identifier=org_identifier, project_identifier=project_identifier, search_term=search_term, env_identifiers=env_identifiers, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentsApi->get_environment_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **page** | **int**| Page Index of the results to fetch.Default Value: 0 | [optional] [default to 0]
 **size** | **int**| Results per page | [optional] [default to 100]
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **search_term** | **str**| The word to be searched and included in the list response | [optional] 
 **env_identifiers** | [**list[str]**](str.md)| List of EnvironmentIds | [optional] 
 **sort** | [**list[str]**](str.md)| Specifies sorting criteria of the list. Like sorting based on the last updated entity, alphabetical sorting in an ascending or descending order | [optional] 

### Return type

[**ResponseDTOPageResponseEnvironmentResponse**](ResponseDTOPageResponseEnvironmentResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_environment_v2**
> ResponseDTOEnvironmentResponse get_environment_v2(environment_identifier, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, deleted=deleted)

Gets an Environment by identifier

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
api_instance = harness_python_sdk.EnvironmentsApi(harness_python_sdk.ApiClient(configuration))
environment_identifier = 'environment_identifier_example' # str | Environment Identifier for the entity
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
deleted = false # bool | Specify whether Environment is deleted or not (optional) (default to false)

try:
    # Gets an Environment by identifier
    api_response = api_instance.get_environment_v2(environment_identifier, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, deleted=deleted)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentsApi->get_environment_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_identifier** | **str**| Environment Identifier for the entity | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **deleted** | **bool**| Specify whether Environment is deleted or not | [optional] [default to false]

### Return type

[**ResponseDTOEnvironmentResponse**](ResponseDTOEnvironmentResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_overrides_list**
> ResponseDTOPageResponseServiceOverrideResponse get_service_overrides_list(account_identifier, environment_identifier, page=page, size=size, org_identifier=org_identifier, project_identifier=project_identifier, service_identifier=service_identifier, sort=sort)

Gets Service Overrides list

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
api_instance = harness_python_sdk.EnvironmentsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
environment_identifier = 'environment_identifier_example' # str | Environment Identifier for the Entity.
page = 0 # int | Page Index of the results to fetch.Default Value: 0 (optional) (default to 0)
size = 500 # int | Results per page (optional) (default to 500)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
service_identifier = 'service_identifier_example' # str | Service Identifier for the Entity. (optional)
sort = ['sort_example'] # list[str] | Specifies the sorting criteria of the list. Like sorting based on the last updated entity, alphabetical sorting in an ascending or descending order (optional)

try:
    # Gets Service Overrides list
    api_response = api_instance.get_service_overrides_list(account_identifier, environment_identifier, page=page, size=size, org_identifier=org_identifier, project_identifier=project_identifier, service_identifier=service_identifier, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentsApi->get_service_overrides_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **environment_identifier** | **str**| Environment Identifier for the Entity. | 
 **page** | **int**| Page Index of the results to fetch.Default Value: 0 | [optional] [default to 0]
 **size** | **int**| Results per page | [optional] [default to 500]
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **service_identifier** | **str**| Service Identifier for the Entity. | [optional] 
 **sort** | [**list[str]**](str.md)| Specifies the sorting criteria of the list. Like sorting based on the last updated entity, alphabetical sorting in an ascending or descending order | [optional] 

### Return type

[**ResponseDTOPageResponseServiceOverrideResponse**](ResponseDTOPageResponseServiceOverrideResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_environment_v2**
> ResponseDTOEnvironmentResponse update_environment_v2(account_identifier, body=body, if_match=if_match)

Update an Environment by identifier

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
api_instance = harness_python_sdk.EnvironmentsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
body = harness_python_sdk.EnvironmentRequest() # EnvironmentRequest | Details of the Environment to be updated (optional)
if_match = 'if_match_example' # str |  (optional)

try:
    # Update an Environment by identifier
    api_response = api_instance.update_environment_v2(account_identifier, body=body, if_match=if_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentsApi->update_environment_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **body** | [**EnvironmentRequest**](EnvironmentRequest.md)| Details of the Environment to be updated | [optional] 
 **if_match** | **str**|  | [optional] 

### Return type

[**ResponseDTOEnvironmentResponse**](ResponseDTOEnvironmentResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_environment_v2**
> ResponseDTOEnvironmentResponse upsert_environment_v2(account_identifier, body=body, if_match=if_match)

Upsert an Environment by identifier

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
api_instance = harness_python_sdk.EnvironmentsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
body = harness_python_sdk.EnvironmentRequest() # EnvironmentRequest | Details of the Environment to be updated (optional)
if_match = 'if_match_example' # str |  (optional)

try:
    # Upsert an Environment by identifier
    api_response = api_instance.upsert_environment_v2(account_identifier, body=body, if_match=if_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentsApi->upsert_environment_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **body** | [**EnvironmentRequest**](EnvironmentRequest.md)| Details of the Environment to be updated | [optional] 
 **if_match** | **str**|  | [optional] 

### Return type

[**ResponseDTOEnvironmentResponse**](ResponseDTOEnvironmentResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_service_override**
> ResponseDTOServiceOverrideResponse upsert_service_override(account_identifier, body=body)

upsert a Service Override for an Environment

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
api_instance = harness_python_sdk.EnvironmentsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
body = harness_python_sdk.ServiceOverrideRequest() # ServiceOverrideRequest | Details of the Service Override to be upserted (optional)

try:
    # upsert a Service Override for an Environment
    api_response = api_instance.upsert_service_override(account_identifier, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentsApi->upsert_service_override: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **body** | [**ServiceOverrideRequest**](ServiceOverrideRequest.md)| Details of the Service Override to be upserted | [optional] 

### Return type

[**ResponseDTOServiceOverrideResponse**](ResponseDTOServiceOverrideResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

