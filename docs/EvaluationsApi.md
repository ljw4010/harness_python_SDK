# swagger_client.EvaluationsApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**evaluations_find**](EvaluationsApi.md#evaluations_find) | **GET** /pm/api/v1/evaluations/{id} | 
[**evaluations_list**](EvaluationsApi.md#evaluations_list) | **GET** /pm/api/v1/evaluations | 

# **evaluations_find**
> Evaluation evaluations_find(id, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, x_api_key=x_api_key)



Find an evaluation by ID

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
api_instance = swagger_client.EvaluationsApi(swagger_client.ApiClient(configuration))
id = 789 # int | The ID of the evaluation to retrieve
account_identifier = '' # str | Harness account ID (optional)
org_identifier = '' # str | Harness organization ID (optional)
project_identifier = '' # str | Harness project ID (optional)
x_api_key = 'x_api_key_example' # str | Harness PAT key used to perform authorization (optional)

try:
    api_response = api_instance.evaluations_find(id, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, x_api_key=x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EvaluationsApi->evaluations_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the evaluation to retrieve | 
 **account_identifier** | **str**| Harness account ID | [optional] 
 **org_identifier** | **str**| Harness organization ID | [optional] 
 **project_identifier** | **str**| Harness project ID | [optional] 
 **x_api_key** | **str**| Harness PAT key used to perform authorization | [optional] 

### Return type

[**Evaluation**](Evaluation.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.goa.error

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **evaluations_list**
> list[Evaluation] evaluations_list(account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, per_page=per_page, page=page, entity=entity, type=type, action=action, last_seen=last_seen, created_date_from=created_date_from, created_date_to=created_date_to, status=status, include_child_scopes=include_child_scopes, x_api_key=x_api_key)



List evaluations

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
api_instance = swagger_client.EvaluationsApi(swagger_client.ApiClient(configuration))
account_identifier = '' # str | Harness account ID (optional)
org_identifier = '' # str | Harness organization ID (optional)
project_identifier = '' # str | Harness project ID (optional)
per_page = 50 # int | Number of results per page (optional) (default to 50)
page = 0 # int | Page number (starting from 0) (optional) (default to 0)
entity = 'entity_example' # str | Filter by the entity associated with the evaluation (optional)
type = 'type_example' # str | Filter by the type associated with the evaluation (optional)
action = 'action_example' # str | Filter by the action associated with the evaluation (optional)
last_seen = 789 # int | Retrieve results starting after this last-seen result (optional)
created_date_from = 789 # int | Retrieve results created from this date (optional)
created_date_to = 789 # int | Retrieve results created up to this date (optional)
status = 'status_example' # str | Retrieve results with these statuses (optional)
include_child_scopes = false # bool | When true, evaluations from child scopes will be inculded in the results (optional) (default to false)
x_api_key = 'x_api_key_example' # str | Harness PAT key used to perform authorization (optional)

try:
    api_response = api_instance.evaluations_list(account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, per_page=per_page, page=page, entity=entity, type=type, action=action, last_seen=last_seen, created_date_from=created_date_from, created_date_to=created_date_to, status=status, include_child_scopes=include_child_scopes, x_api_key=x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EvaluationsApi->evaluations_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Harness account ID | [optional] 
 **org_identifier** | **str**| Harness organization ID | [optional] 
 **project_identifier** | **str**| Harness project ID | [optional] 
 **per_page** | **int**| Number of results per page | [optional] [default to 50]
 **page** | **int**| Page number (starting from 0) | [optional] [default to 0]
 **entity** | **str**| Filter by the entity associated with the evaluation | [optional] 
 **type** | **str**| Filter by the type associated with the evaluation | [optional] 
 **action** | **str**| Filter by the action associated with the evaluation | [optional] 
 **last_seen** | **int**| Retrieve results starting after this last-seen result | [optional] 
 **created_date_from** | **int**| Retrieve results created from this date | [optional] 
 **created_date_to** | **int**| Retrieve results created up to this date | [optional] 
 **status** | **str**| Retrieve results with these statuses | [optional] 
 **include_child_scopes** | **bool**| When true, evaluations from child scopes will be inculded in the results | [optional] [default to false]
 **x_api_key** | **str**| Harness PAT key used to perform authorization | [optional] 

### Return type

[**list[Evaluation]**](Evaluation.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.goa.error

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

