# swagger_client.PolicysetsApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**policysets_create**](PolicysetsApi.md#policysets_create) | **POST** /pm/api/v1/policysets | 
[**policysets_delete**](PolicysetsApi.md#policysets_delete) | **DELETE** /pm/api/v1/policysets/{identifier} | 
[**policysets_find**](PolicysetsApi.md#policysets_find) | **GET** /pm/api/v1/policysets/{identifier} | 
[**policysets_list**](PolicysetsApi.md#policysets_list) | **GET** /pm/api/v1/policysets | 
[**policysets_update**](PolicysetsApi.md#policysets_update) | **PATCH** /pm/api/v1/policysets/{identifier} | 

# **policysets_create**
> PolicyManagementPolicySet policysets_create(body, x_api_key=x_api_key, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)



Create a policy set

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
api_instance = swagger_client.PolicysetsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateRequestBody2() # CreateRequestBody2 | 
x_api_key = 'x_api_key_example' # str | Harness PAT key used to perform authorization (optional)
account_identifier = '' # str | Harness account ID (optional)
org_identifier = '' # str | Harness organization ID (optional)
project_identifier = '' # str | Harness project ID (optional)

try:
    api_response = api_instance.policysets_create(body, x_api_key=x_api_key, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicysetsApi->policysets_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateRequestBody2**](CreateRequestBody2.md)|  | 
 **x_api_key** | **str**| Harness PAT key used to perform authorization | [optional] 
 **account_identifier** | **str**| Harness account ID | [optional] 
 **org_identifier** | **str**| Harness organization ID | [optional] 
 **project_identifier** | **str**| Harness project ID | [optional] 

### Return type

[**PolicyManagementPolicySet**](PolicyManagementPolicySet.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/vnd.goa.error

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **policysets_delete**
> policysets_delete(identifier, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, x_api_key=x_api_key)



Delete a policy set by identifier

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
api_instance = swagger_client.PolicysetsApi(swagger_client.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of the policy set
account_identifier = '' # str | Harness account ID (optional)
org_identifier = '' # str | Harness organization ID (optional)
project_identifier = '' # str | Harness project ID (optional)
x_api_key = 'x_api_key_example' # str | Harness PAT key used to perform authorization (optional)

try:
    api_instance.policysets_delete(identifier, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, x_api_key=x_api_key)
except ApiException as e:
    print("Exception when calling PolicysetsApi->policysets_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of the policy set | 
 **account_identifier** | **str**| Harness account ID | [optional] 
 **org_identifier** | **str**| Harness organization ID | [optional] 
 **project_identifier** | **str**| Harness project ID | [optional] 
 **x_api_key** | **str**| Harness PAT key used to perform authorization | [optional] 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.goa.error

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **policysets_find**
> PolicyManagementPolicySet policysets_find(identifier, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, x_api_key=x_api_key)



Find a policy set by identifier

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
api_instance = swagger_client.PolicysetsApi(swagger_client.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of the policy set to retrieve
account_identifier = '' # str | Harness account ID (optional)
org_identifier = '' # str | Harness organization ID (optional)
project_identifier = '' # str | Harness project ID (optional)
x_api_key = 'x_api_key_example' # str | Harness PAT key used to perform authorization (optional)

try:
    api_response = api_instance.policysets_find(identifier, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, x_api_key=x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicysetsApi->policysets_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of the policy set to retrieve | 
 **account_identifier** | **str**| Harness account ID | [optional] 
 **org_identifier** | **str**| Harness organization ID | [optional] 
 **project_identifier** | **str**| Harness project ID | [optional] 
 **x_api_key** | **str**| Harness PAT key used to perform authorization | [optional] 

### Return type

[**PolicyManagementPolicySet**](PolicyManagementPolicySet.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.goa.error

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **policysets_list**
> list[PolicyManagementPolicySet] policysets_list(account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, per_page=per_page, page=page, search_term=search_term, sort=sort, type=type, action=action, x_api_key=x_api_key)



List all policy sets

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
api_instance = swagger_client.PolicysetsApi(swagger_client.ApiClient(configuration))
account_identifier = '' # str | Harness account ID (optional)
org_identifier = '' # str | Harness organization ID (optional)
project_identifier = '' # str | Harness project ID (optional)
per_page = 50 # int | Number of results per page (optional) (default to 50)
page = 0 # int | Page number (starting from 0) (optional) (default to 0)
search_term = '' # str | Filter results by partial name match (optional)
sort = 'name,ASC' # str | Sort order for results (optional) (default to name,ASC)
type = 'type_example' # str | Filter results by type (optional)
action = 'action_example' # str | Filter results by action (optional)
x_api_key = 'x_api_key_example' # str | Harness PAT key used to perform authorization (optional)

try:
    api_response = api_instance.policysets_list(account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, per_page=per_page, page=page, search_term=search_term, sort=sort, type=type, action=action, x_api_key=x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicysetsApi->policysets_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Harness account ID | [optional] 
 **org_identifier** | **str**| Harness organization ID | [optional] 
 **project_identifier** | **str**| Harness project ID | [optional] 
 **per_page** | **int**| Number of results per page | [optional] [default to 50]
 **page** | **int**| Page number (starting from 0) | [optional] [default to 0]
 **search_term** | **str**| Filter results by partial name match | [optional] 
 **sort** | **str**| Sort order for results | [optional] [default to name,ASC]
 **type** | **str**| Filter results by type | [optional] 
 **action** | **str**| Filter results by action | [optional] 
 **x_api_key** | **str**| Harness PAT key used to perform authorization | [optional] 

### Return type

[**list[PolicyManagementPolicySet]**](PolicyManagementPolicySet.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.goa.error

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **policysets_update**
> policysets_update(body, identifier, x_api_key=x_api_key, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)



Update a policy set by identifier

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
api_instance = swagger_client.PolicysetsApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateRequestBody2() # UpdateRequestBody2 | 
identifier = 'identifier_example' # str | Identifier of the policy set
x_api_key = 'x_api_key_example' # str | Harness PAT key used to perform authorization (optional)
account_identifier = '' # str | Harness account ID (optional)
org_identifier = '' # str | Harness organization ID (optional)
project_identifier = '' # str | Harness project ID (optional)

try:
    api_instance.policysets_update(body, identifier, x_api_key=x_api_key, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
except ApiException as e:
    print("Exception when calling PolicysetsApi->policysets_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateRequestBody2**](UpdateRequestBody2.md)|  | 
 **identifier** | **str**| Identifier of the policy set | 
 **x_api_key** | **str**| Harness PAT key used to perform authorization | [optional] 
 **account_identifier** | **str**| Harness account ID | [optional] 
 **org_identifier** | **str**| Harness organization ID | [optional] 
 **project_identifier** | **str**| Harness project ID | [optional] 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.goa.error

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

