# swagger_client.ServiceLevelObjectiveApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_metric_graph_for_slo**](ServiceLevelObjectiveApi.md#get_metric_graph_for_slo) | **GET** /cv/api/v1/orgs/{org}/projects/{project}/metric-graph/{slo-identifier} | Get Metric Graph For SLO
[**list_slo**](ServiceLevelObjectiveApi.md#list_slo) | **GET** /cv/api/v1/orgs/{org}/projects/{project}/slo | List SLOs

# **get_metric_graph_for_slo**
> list[MetricGraph] get_metric_graph_for_slo(org, project, slo_identifier, start_time=start_time, end_time=end_time, harness_account=harness_account)

Get Metric Graph For SLO

Get Underlying Metrics Graph for SLO

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
api_instance = swagger_client.ServiceLevelObjectiveApi(swagger_client.ApiClient(configuration))
org = 'org_example' # str | Organization identifier
project = 'project_example' # str | Project identifier
slo_identifier = 'slo_identifier_example' # str | SLO identifier.
start_time = 789 # int | Start Time for the metric graphs.  (optional)
end_time = 789 # int | End Time for the metric graphs. (optional)
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)

try:
    # Get Metric Graph For SLO
    api_response = api_instance.get_metric_graph_for_slo(org, project, slo_identifier, start_time=start_time, end_time=end_time, harness_account=harness_account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceLevelObjectiveApi->get_metric_graph_for_slo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| Organization identifier | 
 **project** | **str**| Project identifier | 
 **slo_identifier** | **str**| SLO identifier. | 
 **start_time** | **int**| Start Time for the metric graphs.  | [optional] 
 **end_time** | **int**| End Time for the metric graphs. | [optional] 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 

### Return type

[**list[MetricGraph]**](MetricGraph.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_slo**
> list[SLOHealthListView] list_slo(org, project, harness_account=harness_account, page=page, limit=limit, composite_slo_identifier=composite_slo_identifier, monitored_service_identifier=monitored_service_identifier, user_journey_identifiers=user_journey_identifiers, filter=filter, slo_type=slo_type, env_identifiers=env_identifiers, target_types=target_types, error_budget_risks=error_budget_risks, evaluation_type=evaluation_type, child_resource=child_resource)

List SLOs

Returns a list of Service Level Objectives

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
api_instance = swagger_client.ServiceLevelObjectiveApi(swagger_client.ApiClient(configuration))
org = 'org_example' # str | Organization identifier
project = 'project_example' # str | Project identifier
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)
page = 0 # int | Pagination page number strategy: Specify the page number within the paginated collection related to the number of items on each page. (optional) (default to 0)
limit = 20 # int | Pagination: Number of items to return. (optional) (default to 20)
composite_slo_identifier = 'composite_slo_identifier_example' # str | Identifier for the Composite SLO for which underlying SLOs needs to be listed. (optional)
monitored_service_identifier = 'monitored_service_identifier_example' # str | For filtering on the basis of monitored service identifier (optional)
user_journey_identifiers = ['user_journey_identifiers_example'] # list[str] | List of User Journey identifiers on the basis of which the SLOs are filtered. (optional)
filter = 'filter_example' # str | SLO Name on the basis of which the SLOs are filtered. (optional)
slo_type = 'slo_type_example' # str | SLO Types on the basis of which the SLOs are filtered. (optional)
env_identifiers = ['env_identifiers_example'] # list[str] | Identifiers of Environments on the basis of which the SLOs are filtered. (optional)
target_types = ['target_types_example'] # list[str] | Target Types on the basis of which the SLOs are filtered. (optional)
error_budget_risks = ['error_budget_risks_example'] # list[str] | Error Budgets on the basis of which the SLOs are filtered. (optional)
evaluation_type = 'evaluation_type_example' # str | Evaluation Type on the basis of which the SLOs are filtered. (optional)
child_resource = false # bool | For filtering the simple slo&#x27;s on the basis of accountId. Set it to true for Account Level SLOs. (optional) (default to false)

try:
    # List SLOs
    api_response = api_instance.list_slo(org, project, harness_account=harness_account, page=page, limit=limit, composite_slo_identifier=composite_slo_identifier, monitored_service_identifier=monitored_service_identifier, user_journey_identifiers=user_journey_identifiers, filter=filter, slo_type=slo_type, env_identifiers=env_identifiers, target_types=target_types, error_budget_risks=error_budget_risks, evaluation_type=evaluation_type, child_resource=child_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceLevelObjectiveApi->list_slo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| Organization identifier | 
 **project** | **str**| Project identifier | 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 
 **page** | **int**| Pagination page number strategy: Specify the page number within the paginated collection related to the number of items on each page. | [optional] [default to 0]
 **limit** | **int**| Pagination: Number of items to return. | [optional] [default to 20]
 **composite_slo_identifier** | **str**| Identifier for the Composite SLO for which underlying SLOs needs to be listed. | [optional] 
 **monitored_service_identifier** | **str**| For filtering on the basis of monitored service identifier | [optional] 
 **user_journey_identifiers** | [**list[str]**](str.md)| List of User Journey identifiers on the basis of which the SLOs are filtered. | [optional] 
 **filter** | **str**| SLO Name on the basis of which the SLOs are filtered. | [optional] 
 **slo_type** | **str**| SLO Types on the basis of which the SLOs are filtered. | [optional] 
 **env_identifiers** | [**list[str]**](str.md)| Identifiers of Environments on the basis of which the SLOs are filtered. | [optional] 
 **target_types** | [**list[str]**](str.md)| Target Types on the basis of which the SLOs are filtered. | [optional] 
 **error_budget_risks** | [**list[str]**](str.md)| Error Budgets on the basis of which the SLOs are filtered. | [optional] 
 **evaluation_type** | **str**| Evaluation Type on the basis of which the SLOs are filtered. | [optional] 
 **child_resource** | **bool**| For filtering the simple slo&amp;#x27;s on the basis of accountId. Set it to true for Account Level SLOs. | [optional] [default to false]

### Return type

[**list[SLOHealthListView]**](SLOHealthListView.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

