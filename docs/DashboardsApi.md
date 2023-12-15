# swagger_client.DashboardsApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dashboard_service_get_dashboard_overview**](DashboardsApi.md#dashboard_service_get_dashboard_overview) | **GET** /gitops/api/v1/dashboard/overview | GetDashboradOverview gets dashboard overview
[**dashboard_service_recently_created_counts**](DashboardsApi.md#dashboard_service_recently_created_counts) | **GET** /gitops/api/v1/dashboard/counts | List count of Cluster, Repos and Apps created within a time series

# **dashboard_service_get_dashboard_overview**
> V1DashboardOverview dashboard_service_get_dashboard_overview(project_identifier, org_identifier, account_identifier, agent_identifier=agent_identifier)

GetDashboradOverview gets dashboard overview

Gets dashboard overview

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
api_instance = swagger_client.DashboardsApi(swagger_client.ApiClient(configuration))
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
agent_identifier = 'agent_identifier_example' # str | Agent identifier for entity. (optional)

try:
    # GetDashboradOverview gets dashboard overview
    api_response = api_instance.dashboard_service_get_dashboard_overview(project_identifier, org_identifier, account_identifier, agent_identifier=agent_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->dashboard_service_get_dashboard_overview: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **agent_identifier** | **str**| Agent identifier for entity. | [optional] 

### Return type

[**V1DashboardOverview**](V1DashboardOverview.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_service_recently_created_counts**
> V1RecentlyCreatedOverview dashboard_service_recently_created_counts(project_identifier, org_identifier, account_identifier, end_time, start_time)

List count of Cluster, Repos and Apps created within a time series

List count of Cluster, Repos and Apps created within a time series.

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
api_instance = swagger_client.DashboardsApi(swagger_client.ApiClient(configuration))
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
end_time = 56 # int | 
start_time = 56 # int | 

try:
    # List count of Cluster, Repos and Apps created within a time series
    api_response = api_instance.dashboard_service_recently_created_counts(project_identifier, org_identifier, account_identifier, end_time, start_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->dashboard_service_recently_created_counts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **end_time** | **int**|  | 
 **start_time** | **int**|  | 

### Return type

[**V1RecentlyCreatedOverview**](V1RecentlyCreatedOverview.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

