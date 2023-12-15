# swagger_client.ReconcilerApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reconciler_service_collect_counts**](ReconcilerApi.md#reconciler_service_collect_counts) | **POST** /gitops/api/v1/agents/{agentIdentifier}/reconcile/counts | Returns number of entities that exist in the cluster on the agent. Filter can be used to count only global entities (with empty project) and those specified by the filter.
[**reconciler_service_import_data**](ReconcilerApi.md#reconciler_service_import_data) | **POST** /gitops/api/v1/agents/{agentIdentifier}/reconcile/import | Imports data from cluster via agent. There must be at least one project mapping in the database. Returns number of entities imported.

# **reconciler_service_collect_counts**
> ReconcilerReconcileCountsResponse reconciler_service_collect_counts(body, account_identifier, agent_identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Returns number of entities that exist in the cluster on the agent. Filter can be used to count only global entities (with empty project) and those specified by the filter.

Returns number of entities that exist in the cluster on the agent. Filter can be used to count only global entities (with empty project) and those specified by the filter.

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
api_instance = swagger_client.ReconcilerApi(swagger_client.ApiClient(configuration))
body = swagger_client.Servicev1ReconcilerFilter() # Servicev1ReconcilerFilter | 
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
agent_identifier = 'agent_identifier_example' # str | Agent identifier for entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Returns number of entities that exist in the cluster on the agent. Filter can be used to count only global entities (with empty project) and those specified by the filter.
    api_response = api_instance.reconciler_service_collect_counts(body, account_identifier, agent_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReconcilerApi->reconciler_service_collect_counts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Servicev1ReconcilerFilter**](Servicev1ReconcilerFilter.md)|  | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **agent_identifier** | **str**| Agent identifier for entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ReconcilerReconcileCountsResponse**](ReconcilerReconcileCountsResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reconciler_service_import_data**
> ReconcilerReconcileCountsResponse reconciler_service_import_data(body, account_identifier, agent_identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Imports data from cluster via agent. There must be at least one project mapping in the database. Returns number of entities imported.

Imports data from cluster via agent. There must be at least one project mapping in the database. Returns number of entities imported.

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
api_instance = swagger_client.ReconcilerApi(swagger_client.ApiClient(configuration))
body = swagger_client.Servicev1ReconcilerFilter() # Servicev1ReconcilerFilter | 
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
agent_identifier = 'agent_identifier_example' # str | Agent identifier for entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Imports data from cluster via agent. There must be at least one project mapping in the database. Returns number of entities imported.
    api_response = api_instance.reconciler_service_import_data(body, account_identifier, agent_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReconcilerApi->reconciler_service_import_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Servicev1ReconcilerFilter**](Servicev1ReconcilerFilter.md)|  | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **agent_identifier** | **str**| Agent identifier for entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ReconcilerReconcileCountsResponse**](ReconcilerReconcileCountsResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

