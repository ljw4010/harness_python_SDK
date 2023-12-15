# swagger_client.DashboardAggregatesApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dashboard_service_recent_deployments**](DashboardAggregatesApi.md#dashboard_service_recent_deployments) | **POST** /gitops/api/v1/dashboard/activity | Returns aggregate statistics of recent deployments
[**dashboard_service_top_application_phase_stats**](DashboardAggregatesApi.md#dashboard_service_top_application_phase_stats) | **GET** /gitops/api/v1/dashboard/topapps | List phase status counts for top 5 most deployed apps

# **dashboard_service_recent_deployments**
> V1RecentDeploymentsDetailsList dashboard_service_recent_deployments(body)

Returns aggregate statistics of recent deployments

Returns aggregate statistics of recent deployments

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
api_instance = swagger_client.DashboardAggregatesApi(swagger_client.ApiClient(configuration))
body = swagger_client.V1RecentDeploymentQuery() # V1RecentDeploymentQuery | 

try:
    # Returns aggregate statistics of recent deployments
    api_response = api_instance.dashboard_service_recent_deployments(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardAggregatesApi->dashboard_service_recent_deployments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1RecentDeploymentQuery**](V1RecentDeploymentQuery.md)|  | 

### Return type

[**V1RecentDeploymentsDetailsList**](V1RecentDeploymentsDetailsList.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_service_top_application_phase_stats**
> V1TopApplicationPhaseStatsList dashboard_service_top_application_phase_stats(project_identifier, org_identifier, account_identifier, end_time, start_time, limit=limit)

List phase status counts for top 5 most deployed apps

List phase status counts for top 5 most deployed apps

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
api_instance = swagger_client.DashboardAggregatesApi(swagger_client.ApiClient(configuration))
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
end_time = 56 # int | 
start_time = 56 # int | 
limit = 56 # int |  (optional)

try:
    # List phase status counts for top 5 most deployed apps
    api_response = api_instance.dashboard_service_top_application_phase_stats(project_identifier, org_identifier, account_identifier, end_time, start_time, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardAggregatesApi->dashboard_service_top_application_phase_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **end_time** | **int**|  | 
 **start_time** | **int**|  | 
 **limit** | **int**|  | [optional] 

### Return type

[**V1TopApplicationPhaseStatsList**](V1TopApplicationPhaseStatsList.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

