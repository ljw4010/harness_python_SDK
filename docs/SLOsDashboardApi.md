# harness_python_sdk.SLOsDashboardApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_secondary_event_details**](SLOsDashboardApi.md#get_secondary_event_details) | **GET** /cv/api/slo-dashboard/secondary-events-details | 
[**get_secondary_events**](SLOsDashboardApi.md#get_secondary_events) | **GET** /cv/api/slo-dashboard/secondary-events/{identifier} | 
[**get_service_level_objectives_risk_count**](SLOsDashboardApi.md#get_service_level_objectives_risk_count) | **GET** /cv/api/slo-dashboard/risk-count | Get all SLOs count by risk
[**get_slo_associated_environment_identifiers**](SLOsDashboardApi.md#get_slo_associated_environment_identifiers) | **GET** /cv/api/slo-dashboard/environment-identifiers | 
[**get_slo_associated_monitored_services**](SLOsDashboardApi.md#get_slo_associated_monitored_services) | **GET** /cv/api/slo-dashboard/monitored-services | 
[**get_slo_consumption_breakdown_view**](SLOsDashboardApi.md#get_slo_consumption_breakdown_view) | **GET** /cv/api/slo-dashboard/widget/{identifier}/consumption | Get SLO consumption breakdown
[**get_slo_details**](SLOsDashboardApi.md#get_slo_details) | **GET** /cv/api/slo-dashboard/widget/{identifier} | Get SLO dashboard details
[**get_slo_health_list_view**](SLOsDashboardApi.md#get_slo_health_list_view) | **GET** /cv/api/slo-dashboard/widgets/list | Get SLO list view
[**get_slo_health_list_view_v2**](SLOsDashboardApi.md#get_slo_health_list_view_v2) | **POST** /cv/api/slo-dashboard/widgets/list | Get SLO list view

# **get_secondary_event_details**
> get_secondary_event_details(account_id, secondary_event_type, identifiers)



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
api_instance = harness_python_sdk.SLOsDashboardApi(harness_python_sdk.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier for the Entity.
secondary_event_type = 'secondary_event_type_example' # str | 
identifiers = ['identifiers_example'] # list[str] | 

try:
    api_instance.get_secondary_event_details(account_id, secondary_event_type, identifiers)
except ApiException as e:
    print("Exception when calling SLOsDashboardApi->get_secondary_event_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier for the Entity. | 
 **secondary_event_type** | **str**|  | 
 **identifiers** | [**list[str]**](str.md)|  | 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_secondary_events**
> get_secondary_events(identifier, start_time, end_time, account_id, org_identifier=org_identifier, project_identifier=project_identifier)



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
api_instance = harness_python_sdk.SLOsDashboardApi(harness_python_sdk.ApiClient(configuration))
identifier = 'identifier_example' # str | SLO identifier for the entity
start_time = 789 # int | 
end_time = 789 # int | 
account_id = 'account_id_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    api_instance.get_secondary_events(identifier, start_time, end_time, account_id, org_identifier=org_identifier, project_identifier=project_identifier)
except ApiException as e:
    print("Exception when calling SLOsDashboardApi->get_secondary_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| SLO identifier for the entity | 
 **start_time** | **int**|  | 
 **end_time** | **int**|  | 
 **account_id** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_level_objectives_risk_count**
> ResponseDTOSLORiskCountResponse get_service_level_objectives_risk_count(account_id, org_identifier=org_identifier, project_identifier=project_identifier, user_journey_identifiers=user_journey_identifiers, monitored_service_identifier=monitored_service_identifier, target_types=target_types, error_budget_risks=error_budget_risks, filter=filter, slo_type=slo_type, evaluation_type=evaluation_type, env_identifiers=env_identifiers)

Get all SLOs count by risk

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
api_instance = harness_python_sdk.SLOsDashboardApi(harness_python_sdk.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
user_journey_identifiers = ['user_journey_identifiers_example'] # list[str] | For filtering on the basis of user journeys' identifiers (optional)
monitored_service_identifier = 'monitored_service_identifier_example' # str | For filtering on the basis of monitored services' identifiers (optional)
target_types = ['target_types_example'] # list[str] | For filtering on the basis of target types (optional)
error_budget_risks = ['error_budget_risks_example'] # list[str] | For filtering on the basis of error budget risks (optional)
filter = 'filter_example' # str | For filtering on the basis of name (optional)
slo_type = 'slo_type_example' # str | For filtering on the basis of SLO type (optional)
evaluation_type = 'evaluation_type_example' # str | For filtering on the basis of SLI Evaluation type (optional)
env_identifiers = ['env_identifiers_example'] # list[str] | For Filtering on the basis of environment identifiers (optional)

try:
    # Get all SLOs count by risk
    api_response = api_instance.get_service_level_objectives_risk_count(account_id, org_identifier=org_identifier, project_identifier=project_identifier, user_journey_identifiers=user_journey_identifiers, monitored_service_identifier=monitored_service_identifier, target_types=target_types, error_budget_risks=error_budget_risks, filter=filter, slo_type=slo_type, evaluation_type=evaluation_type, env_identifiers=env_identifiers)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SLOsDashboardApi->get_service_level_objectives_risk_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **user_journey_identifiers** | [**list[str]**](str.md)| For filtering on the basis of user journeys&#x27; identifiers | [optional] 
 **monitored_service_identifier** | **str**| For filtering on the basis of monitored services&#x27; identifiers | [optional] 
 **target_types** | [**list[str]**](str.md)| For filtering on the basis of target types | [optional] 
 **error_budget_risks** | [**list[str]**](str.md)| For filtering on the basis of error budget risks | [optional] 
 **filter** | **str**| For filtering on the basis of name | [optional] 
 **slo_type** | **str**| For filtering on the basis of SLO type | [optional] 
 **evaluation_type** | **str**| For filtering on the basis of SLI Evaluation type | [optional] 
 **env_identifiers** | [**list[str]**](str.md)| For Filtering on the basis of environment identifiers | [optional] 

### Return type

[**ResponseDTOSLORiskCountResponse**](ResponseDTOSLORiskCountResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_slo_associated_environment_identifiers**
> get_slo_associated_environment_identifiers(account_id, org_identifier=org_identifier, project_identifier=project_identifier, page_number=page_number, page_size=page_size)



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
api_instance = harness_python_sdk.SLOsDashboardApi(harness_python_sdk.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
page_number = 0 # int | Page Index of the results to fetch.Default Value: 0 (optional) (default to 0)
page_size = 10 # int | Results per page (optional) (default to 10)

try:
    api_instance.get_slo_associated_environment_identifiers(account_id, org_identifier=org_identifier, project_identifier=project_identifier, page_number=page_number, page_size=page_size)
except ApiException as e:
    print("Exception when calling SLOsDashboardApi->get_slo_associated_environment_identifiers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **page_number** | **int**| Page Index of the results to fetch.Default Value: 0 | [optional] [default to 0]
 **page_size** | **int**| Results per page | [optional] [default to 10]

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_slo_associated_monitored_services**
> get_slo_associated_monitored_services(account_id, org_identifier=org_identifier, project_identifier=project_identifier, page_number=page_number, page_size=page_size)



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
api_instance = harness_python_sdk.SLOsDashboardApi(harness_python_sdk.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
page_number = 0 # int | Page Index of the results to fetch.Default Value: 0 (optional) (default to 0)
page_size = 10 # int | Results per page (optional) (default to 10)

try:
    api_instance.get_slo_associated_monitored_services(account_id, org_identifier=org_identifier, project_identifier=project_identifier, page_number=page_number, page_size=page_size)
except ApiException as e:
    print("Exception when calling SLOsDashboardApi->get_slo_associated_monitored_services: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **page_number** | **int**| Page Index of the results to fetch.Default Value: 0 | [optional] [default to 0]
 **page_size** | **int**| Results per page | [optional] [default to 10]

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_slo_consumption_breakdown_view**
> ResponseDTOPageResponseSLOConsumptionBreakdown get_slo_consumption_breakdown_view(identifier, start_time, end_time, account_id, org_identifier=org_identifier, project_identifier=project_identifier)

Get SLO consumption breakdown

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
api_instance = harness_python_sdk.SLOsDashboardApi(harness_python_sdk.ApiClient(configuration))
identifier = 'identifier_example' # str | SLO identifier for the entity
start_time = 789 # int | 
end_time = 789 # int | 
account_id = 'account_id_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Get SLO consumption breakdown
    api_response = api_instance.get_slo_consumption_breakdown_view(identifier, start_time, end_time, account_id, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SLOsDashboardApi->get_slo_consumption_breakdown_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| SLO identifier for the entity | 
 **start_time** | **int**|  | 
 **end_time** | **int**|  | 
 **account_id** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOPageResponseSLOConsumptionBreakdown**](ResponseDTOPageResponseSLOConsumptionBreakdown.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_slo_details**
> ResponseDTOSLODashboardDetail get_slo_details(identifier, account_id, start_time=start_time, end_time=end_time, org_identifier=org_identifier, project_identifier=project_identifier)

Get SLO dashboard details

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
api_instance = harness_python_sdk.SLOsDashboardApi(harness_python_sdk.ApiClient(configuration))
identifier = 'identifier_example' # str | SLO identifier for the entity
account_id = 'account_id_example' # str | Account Identifier for the Entity.
start_time = 789 # int |  (optional)
end_time = 789 # int |  (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Get SLO dashboard details
    api_response = api_instance.get_slo_details(identifier, account_id, start_time=start_time, end_time=end_time, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SLOsDashboardApi->get_slo_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| SLO identifier for the entity | 
 **account_id** | **str**| Account Identifier for the Entity. | 
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOSLODashboardDetail**](ResponseDTOSLODashboardDetail.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_slo_health_list_view**
> ResponseDTOPageResponseSLOHealthListView get_slo_health_list_view(account_id, org_identifier=org_identifier, project_identifier=project_identifier, user_journey_identifiers=user_journey_identifiers, monitored_service_identifier=monitored_service_identifier, target_types=target_types, error_budget_risks=error_budget_risks, filter=filter, slo_type=slo_type, evaluation_type=evaluation_type, env_identifiers=env_identifiers, page_number=page_number, page_size=page_size)

Get SLO list view

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
api_instance = harness_python_sdk.SLOsDashboardApi(harness_python_sdk.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
user_journey_identifiers = ['user_journey_identifiers_example'] # list[str] | For filtering on the basis of user journeys' identifiers (optional)
monitored_service_identifier = 'monitored_service_identifier_example' # str | For filtering on the basis of monitored services' identifiers (optional)
target_types = ['target_types_example'] # list[str] | For filtering on the basis of target types (optional)
error_budget_risks = ['error_budget_risks_example'] # list[str] | For filtering on the basis of error budget risks (optional)
filter = 'filter_example' # str | For filtering on the basis of name (optional)
slo_type = 'slo_type_example' # str | For filtering on the basis of SLO type (optional)
evaluation_type = 'evaluation_type_example' # str | For filtering on the basis of SLI Evaluation type (optional)
env_identifiers = ['env_identifiers_example'] # list[str] | For Filtering on the basis of environment identifiers (optional)
page_number = 0 # int | Page Index of the results to fetch.Default Value: 0 (optional) (default to 0)
page_size = 10 # int | Results per page (optional) (default to 10)

try:
    # Get SLO list view
    api_response = api_instance.get_slo_health_list_view(account_id, org_identifier=org_identifier, project_identifier=project_identifier, user_journey_identifiers=user_journey_identifiers, monitored_service_identifier=monitored_service_identifier, target_types=target_types, error_budget_risks=error_budget_risks, filter=filter, slo_type=slo_type, evaluation_type=evaluation_type, env_identifiers=env_identifiers, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SLOsDashboardApi->get_slo_health_list_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **user_journey_identifiers** | [**list[str]**](str.md)| For filtering on the basis of user journeys&#x27; identifiers | [optional] 
 **monitored_service_identifier** | **str**| For filtering on the basis of monitored services&#x27; identifiers | [optional] 
 **target_types** | [**list[str]**](str.md)| For filtering on the basis of target types | [optional] 
 **error_budget_risks** | [**list[str]**](str.md)| For filtering on the basis of error budget risks | [optional] 
 **filter** | **str**| For filtering on the basis of name | [optional] 
 **slo_type** | **str**| For filtering on the basis of SLO type | [optional] 
 **evaluation_type** | **str**| For filtering on the basis of SLI Evaluation type | [optional] 
 **env_identifiers** | [**list[str]**](str.md)| For Filtering on the basis of environment identifiers | [optional] 
 **page_number** | **int**| Page Index of the results to fetch.Default Value: 0 | [optional] [default to 0]
 **page_size** | **int**| Results per page | [optional] [default to 10]

### Return type

[**ResponseDTOPageResponseSLOHealthListView**](ResponseDTOPageResponseSLOHealthListView.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_slo_health_list_view_v2**
> ResponseDTOPageResponseSLOHealthListView get_slo_health_list_view_v2(account_id, body=body, org_identifier=org_identifier, project_identifier=project_identifier, page_number=page_number, page_size=page_size)

Get SLO list view

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
api_instance = harness_python_sdk.SLOsDashboardApi(harness_python_sdk.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier for the Entity.
body = harness_python_sdk.SLODashboardApiFilter() # SLODashboardApiFilter |  (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
page_number = 0 # int | Page Index of the results to fetch.Default Value: 0 (optional) (default to 0)
page_size = 10 # int | Results per page (optional) (default to 10)

try:
    # Get SLO list view
    api_response = api_instance.get_slo_health_list_view_v2(account_id, body=body, org_identifier=org_identifier, project_identifier=project_identifier, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SLOsDashboardApi->get_slo_health_list_view_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier for the Entity. | 
 **body** | [**SLODashboardApiFilter**](SLODashboardApiFilter.md)|  | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **page_number** | **int**| Page Index of the results to fetch.Default Value: 0 | [optional] [default to 0]
 **page_size** | **int**| Results per page | [optional] [default to 10]

### Return type

[**ResponseDTOPageResponseSLOHealthListView**](ResponseDTOPageResponseSLOHealthListView.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

