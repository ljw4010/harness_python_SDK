# harness_python_sdk.MonitoredServicesApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_default_monitored_service**](MonitoredServicesApi.md#create_default_monitored_service) | **POST** /cv/api/monitored-service/create-default | 
[**cvget_anomalies_summary**](MonitoredServicesApi.md#cvget_anomalies_summary) | **GET** /cv/api/monitored-service/{identifier}/anomaliesCount | 
[**delete_monitored_service**](MonitoredServicesApi.md#delete_monitored_service) | **DELETE** /cv/api/monitored-service/{identifier} | Delete monitored service data
[**get_all_monitored_services_with_health_sources**](MonitoredServicesApi.md#get_all_monitored_services_with_health_sources) | **GET** /cv/api/monitored-service/all/time-series-health-sources | 
[**get_count_of_services**](MonitoredServicesApi.md#get_count_of_services) | **GET** /cv/api/monitored-service/count-of-services | 
[**get_environments**](MonitoredServicesApi.md#get_environments) | **GET** /cv/api/monitored-service/environments | 
[**get_health_sources**](MonitoredServicesApi.md#get_health_sources) | **GET** /cv/api/monitored-service/health-sources | 
[**get_health_sources_for_monitored_service_identifier**](MonitoredServicesApi.md#get_health_sources_for_monitored_service_identifier) | **GET** /cv/api/monitored-service/{monitoredServiceIdentifier}/health-sources | 
[**get_list**](MonitoredServicesApi.md#get_list) | **GET** /cv/api/monitored-service/list | 
[**get_list_v2**](MonitoredServicesApi.md#get_list_v2) | **GET** /cv/api/monitored-service/platform/list | 
[**get_monitored_service**](MonitoredServicesApi.md#get_monitored_service) | **GET** /cv/api/monitored-service/{identifier} | Get monitored service data
[**get_monitored_service_change_details**](MonitoredServicesApi.md#get_monitored_service_change_details) | **GET** /cv/api/monitored-service/{monitoredServiceIdentifier}/change-details | 
[**get_monitored_service_details**](MonitoredServicesApi.md#get_monitored_service_details) | **GET** /cv/api/monitored-service/{monitoredServiceIdentifier}/service-details | 
[**get_monitored_service_details1**](MonitoredServicesApi.md#get_monitored_service_details1) | **GET** /cv/api/monitored-service/service-details | 
[**get_monitored_service_from_service_and_environment**](MonitoredServicesApi.md#get_monitored_service_from_service_and_environment) | **GET** /cv/api/monitored-service/service-environment | 
[**get_monitored_service_logs**](MonitoredServicesApi.md#get_monitored_service_logs) | **GET** /cv/api/monitored-service/{monitoredServiceIdentifier}/logs | 
[**get_monitored_service_score**](MonitoredServicesApi.md#get_monitored_service_score) | **GET** /cv/api/monitored-service/{identifier}/scores | 
[**get_ms_secondary_events**](MonitoredServicesApi.md#get_ms_secondary_events) | **GET** /cv/api/monitored-service/{identifier}/secondary-events | 
[**get_ms_secondary_events_details**](MonitoredServicesApi.md#get_ms_secondary_events_details) | **GET** /cv/api/monitored-service/secondary-events-details | 
[**get_notification_rules_for_monitored_service**](MonitoredServicesApi.md#get_notification_rules_for_monitored_service) | **GET** /cv/api/monitored-service/{identifier}/notification-rules | Get notification rules for MonitoredService
[**get_over_all_health_score**](MonitoredServicesApi.md#get_over_all_health_score) | **GET** /cv/api/monitored-service/{identifier}/overall-health-score | 
[**get_services**](MonitoredServicesApi.md#get_services) | **GET** /cv/api/monitored-service/services | 
[**get_slo_metrics**](MonitoredServicesApi.md#get_slo_metrics) | **GET** /cv/api/monitored-service/{monitoredServiceIdentifier}/health-source/{healthSourceIdentifier}/slo-metrics | 
[**list**](MonitoredServicesApi.md#list) | **GET** /cv/api/monitored-service | 
[**save_monitored_service**](MonitoredServicesApi.md#save_monitored_service) | **POST** /cv/api/monitored-service | Saves monitored service data
[**save_monitored_service_from_template_input**](MonitoredServicesApi.md#save_monitored_service_from_template_input) | **POST** /cv/api/monitored-service/template-input | Saves monitored service from template input
[**save_monitored_service_from_yaml**](MonitoredServicesApi.md#save_monitored_service_from_yaml) | **POST** /cv/api/monitored-service/yaml | 
[**set_health_monitoring_flag**](MonitoredServicesApi.md#set_health_monitoring_flag) | **PUT** /cv/api/monitored-service/{identifier}/health-monitoring-flag | 
[**update_monitored_service**](MonitoredServicesApi.md#update_monitored_service) | **PUT** /cv/api/monitored-service/{identifier} | Updates monitored service data
[**update_monitored_service_from_template_input**](MonitoredServicesApi.md#update_monitored_service_from_template_input) | **PUT** /cv/api/monitored-service/{identifier}/template-input | Update monitored service from yaml or template
[**update_monitored_service_from_yaml**](MonitoredServicesApi.md#update_monitored_service_from_yaml) | **PUT** /cv/api/monitored-service/{identifier}/yaml | 
[**yaml_template**](MonitoredServicesApi.md#yaml_template) | **GET** /cv/api/monitored-service/yaml-template | 

# **create_default_monitored_service**
> create_default_monitored_service(account_id, org_identifier, project_identifier, environment_identifier, service_identifier)



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
api_instance = harness_python_sdk.MonitoredServicesApi(harness_python_sdk.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
environment_identifier = 'environment_identifier_example' # str | 
service_identifier = 'service_identifier_example' # str | 

try:
    api_instance.create_default_monitored_service(account_id, org_identifier, project_identifier, environment_identifier, service_identifier)
except ApiException as e:
    print("Exception when calling MonitoredServicesApi->create_default_monitored_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **environment_identifier** | **str**|  | 
 **service_identifier** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cvget_anomalies_summary**
> cvget_anomalies_summary(account_id, org_identifier, project_identifier, identifier, start_time, end_time)



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
api_instance = harness_python_sdk.MonitoredServicesApi(harness_python_sdk.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
identifier = 'identifier_example' # str | 
start_time = 789 # int | 
end_time = 789 # int | 

try:
    api_instance.cvget_anomalies_summary(account_id, org_identifier, project_identifier, identifier, start_time, end_time)
except ApiException as e:
    print("Exception when calling MonitoredServicesApi->cvget_anomalies_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **identifier** | **str**|  | 
 **start_time** | **int**|  | 
 **end_time** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_monitored_service**
> CvRestResponseBoolean delete_monitored_service(account_id, org_identifier, project_identifier, identifier)

Delete monitored service data

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
api_instance = harness_python_sdk.MonitoredServicesApi(harness_python_sdk.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
identifier = 'identifier_example' # str | Identifier for the Entity.

try:
    # Delete monitored service data
    api_response = api_instance.delete_monitored_service(account_id, org_identifier, project_identifier, identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitoredServicesApi->delete_monitored_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **identifier** | **str**| Identifier for the Entity. | 

### Return type

[**CvRestResponseBoolean**](CvRestResponseBoolean.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_monitored_services_with_health_sources**
> get_all_monitored_services_with_health_sources(account_id, org_identifier, project_identifier)



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
api_instance = harness_python_sdk.MonitoredServicesApi(harness_python_sdk.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.

try:
    api_instance.get_all_monitored_services_with_health_sources(account_id, org_identifier, project_identifier)
except ApiException as e:
    print("Exception when calling MonitoredServicesApi->get_all_monitored_services_with_health_sources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_count_of_services**
> get_count_of_services(account_id, org_identifier, project_identifier, environment_identifier=environment_identifier, filter=filter)



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
api_instance = harness_python_sdk.MonitoredServicesApi(harness_python_sdk.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
environment_identifier = 'environment_identifier_example' # str |  (optional)
filter = 'filter_example' # str |  (optional)

try:
    api_instance.get_count_of_services(account_id, org_identifier, project_identifier, environment_identifier=environment_identifier, filter=filter)
except ApiException as e:
    print("Exception when calling MonitoredServicesApi->get_count_of_services: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **environment_identifier** | **str**|  | [optional] 
 **filter** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_environments**
> get_environments(account_id, org_identifier, project_identifier)



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
api_instance = harness_python_sdk.MonitoredServicesApi(harness_python_sdk.ApiClient(configuration))
account_id = 'account_id_example' # str | 
org_identifier = 'org_identifier_example' # str | 
project_identifier = 'project_identifier_example' # str | 

try:
    api_instance.get_environments(account_id, org_identifier, project_identifier)
except ApiException as e:
    print("Exception when calling MonitoredServicesApi->get_environments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **org_identifier** | **str**|  | 
 **project_identifier** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_health_sources**
> get_health_sources(account_id, org_identifier, project_identifier, service_identifier, environment_identifier)



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
api_instance = harness_python_sdk.MonitoredServicesApi(harness_python_sdk.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
service_identifier = 'service_identifier_example' # str | 
environment_identifier = 'environment_identifier_example' # str | 

try:
    api_instance.get_health_sources(account_id, org_identifier, project_identifier, service_identifier, environment_identifier)
except ApiException as e:
    print("Exception when calling MonitoredServicesApi->get_health_sources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **service_identifier** | **str**|  | 
 **environment_identifier** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_health_sources_for_monitored_service_identifier**
> get_health_sources_for_monitored_service_identifier(account_id, org_identifier, project_identifier, monitored_service_identifier)



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
api_instance = harness_python_sdk.MonitoredServicesApi(harness_python_sdk.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
monitored_service_identifier = 'monitored_service_identifier_example' # str | 

try:
    api_instance.get_health_sources_for_monitored_service_identifier(account_id, org_identifier, project_identifier, monitored_service_identifier)
except ApiException as e:
    print("Exception when calling MonitoredServicesApi->get_health_sources_for_monitored_service_identifier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **monitored_service_identifier** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list**
> get_list(account_id, org_identifier, project_identifier, offset, page_size, environment_identifier=environment_identifier, environment_identifiers=environment_identifiers, filter=filter)



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
api_instance = harness_python_sdk.MonitoredServicesApi(harness_python_sdk.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
offset = 56 # int | 
page_size = 56 # int | 
environment_identifier = 'environment_identifier_example' # str |  (optional)
environment_identifiers = ['environment_identifiers_example'] # list[str] |  (optional)
filter = 'filter_example' # str |  (optional)

try:
    api_instance.get_list(account_id, org_identifier, project_identifier, offset, page_size, environment_identifier=environment_identifier, environment_identifiers=environment_identifiers, filter=filter)
except ApiException as e:
    print("Exception when calling MonitoredServicesApi->get_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **offset** | **int**|  | 
 **page_size** | **int**|  | 
 **environment_identifier** | **str**|  | [optional] 
 **environment_identifiers** | [**list[str]**](str.md)|  | [optional] 
 **filter** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_v2**
> get_list_v2(account_id, org_identifier, project_identifier, offset, page_size, environment_identifiers=environment_identifiers, filter=filter, monitored_service_type=monitored_service_type, hide_not_configured_services=hide_not_configured_services)



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
api_instance = harness_python_sdk.MonitoredServicesApi(harness_python_sdk.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
offset = 56 # int | 
page_size = 56 # int | 
environment_identifiers = ['environment_identifiers_example'] # list[str] |  (optional)
filter = 'filter_example' # str |  (optional)
monitored_service_type = 'monitored_service_type_example' # str |  (optional)
hide_not_configured_services = true # bool |  (optional)

try:
    api_instance.get_list_v2(account_id, org_identifier, project_identifier, offset, page_size, environment_identifiers=environment_identifiers, filter=filter, monitored_service_type=monitored_service_type, hide_not_configured_services=hide_not_configured_services)
except ApiException as e:
    print("Exception when calling MonitoredServicesApi->get_list_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **offset** | **int**|  | 
 **page_size** | **int**|  | 
 **environment_identifiers** | [**list[str]**](str.md)|  | [optional] 
 **filter** | **str**|  | [optional] 
 **monitored_service_type** | **str**|  | [optional] 
 **hide_not_configured_services** | **bool**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_monitored_service**
> ResponseDTOMonitoredServiceResponse get_monitored_service(identifier, account_id, org_identifier, project_identifier)

Get monitored service data

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
api_instance = harness_python_sdk.MonitoredServicesApi(harness_python_sdk.ApiClient(configuration))
identifier = 'identifier_example' # str | 
account_id = 'account_id_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.

try:
    # Get monitored service data
    api_response = api_instance.get_monitored_service(identifier, account_id, org_identifier, project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitoredServicesApi->get_monitored_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**|  | 
 **account_id** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 

### Return type

[**ResponseDTOMonitoredServiceResponse**](ResponseDTOMonitoredServiceResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_monitored_service_change_details**
> get_monitored_service_change_details(account_id, org_identifier, project_identifier, monitored_service_identifier, slo_identifiers=slo_identifiers, start_time=start_time, end_time=end_time)



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
api_instance = harness_python_sdk.MonitoredServicesApi(harness_python_sdk.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
monitored_service_identifier = 'monitored_service_identifier_example' # str | 
slo_identifiers = ['slo_identifiers_example'] # list[str] |  (optional)
start_time = 789 # int |  (optional)
end_time = 789 # int |  (optional)

try:
    api_instance.get_monitored_service_change_details(account_id, org_identifier, project_identifier, monitored_service_identifier, slo_identifiers=slo_identifiers, start_time=start_time, end_time=end_time)
except ApiException as e:
    print("Exception when calling MonitoredServicesApi->get_monitored_service_change_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **monitored_service_identifier** | **str**|  | 
 **slo_identifiers** | [**list[str]**](str.md)|  | [optional] 
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_monitored_service_details**
> get_monitored_service_details(account_id, org_identifier, project_identifier, monitored_service_identifier)



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
api_instance = harness_python_sdk.MonitoredServicesApi(harness_python_sdk.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
monitored_service_identifier = 'monitored_service_identifier_example' # str | 

try:
    api_instance.get_monitored_service_details(account_id, org_identifier, project_identifier, monitored_service_identifier)
except ApiException as e:
    print("Exception when calling MonitoredServicesApi->get_monitored_service_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **monitored_service_identifier** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_monitored_service_details1**
> get_monitored_service_details1(account_id, service_identifier, environment_identifier, org_identifier=org_identifier, project_identifier=project_identifier)



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
api_instance = harness_python_sdk.MonitoredServicesApi(harness_python_sdk.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier for the Entity.
service_identifier = 'service_identifier_example' # str | 
environment_identifier = 'environment_identifier_example' # str | 
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    api_instance.get_monitored_service_details1(account_id, service_identifier, environment_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
except ApiException as e:
    print("Exception when calling MonitoredServicesApi->get_monitored_service_details1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier for the Entity. | 
 **service_identifier** | **str**|  | 
 **environment_identifier** | **str**|  | 
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

# **get_monitored_service_from_service_and_environment**
> get_monitored_service_from_service_and_environment(account_id, org_identifier, project_identifier, service_identifier, environment_identifier)



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
api_instance = harness_python_sdk.MonitoredServicesApi(harness_python_sdk.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
service_identifier = 'service_identifier_example' # str | 
environment_identifier = 'environment_identifier_example' # str | 

try:
    api_instance.get_monitored_service_from_service_and_environment(account_id, org_identifier, project_identifier, service_identifier, environment_identifier)
except ApiException as e:
    print("Exception when calling MonitoredServicesApi->get_monitored_service_from_service_and_environment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **service_identifier** | **str**|  | 
 **environment_identifier** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_monitored_service_logs**
> get_monitored_service_logs(account_id, org_identifier, project_identifier, monitored_service_identifier, log_type, start_time, end_time, error_logs_only=error_logs_only, health_sources=health_sources, page_number=page_number, page_size=page_size)



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
api_instance = harness_python_sdk.MonitoredServicesApi(harness_python_sdk.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
monitored_service_identifier = 'monitored_service_identifier_example' # str | 
log_type = 'log_type_example' # str | 
start_time = 789 # int | 
end_time = 789 # int | 
error_logs_only = true # bool |  (optional)
health_sources = ['health_sources_example'] # list[str] |  (optional)
page_number = 0 # int | Page Index of the results to fetch.Default Value: 0 (optional) (default to 0)
page_size = 10 # int | Results per page (optional) (default to 10)

try:
    api_instance.get_monitored_service_logs(account_id, org_identifier, project_identifier, monitored_service_identifier, log_type, start_time, end_time, error_logs_only=error_logs_only, health_sources=health_sources, page_number=page_number, page_size=page_size)
except ApiException as e:
    print("Exception when calling MonitoredServicesApi->get_monitored_service_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **monitored_service_identifier** | **str**|  | 
 **log_type** | **str**|  | 
 **start_time** | **int**|  | 
 **end_time** | **int**|  | 
 **error_logs_only** | **bool**|  | [optional] 
 **health_sources** | [**list[str]**](str.md)|  | [optional] 
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

# **get_monitored_service_score**
> get_monitored_service_score(account_id, org_identifier, project_identifier, identifier)



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
api_instance = harness_python_sdk.MonitoredServicesApi(harness_python_sdk.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
identifier = 'identifier_example' # str | 

try:
    api_instance.get_monitored_service_score(account_id, org_identifier, project_identifier, identifier)
except ApiException as e:
    print("Exception when calling MonitoredServicesApi->get_monitored_service_score: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **identifier** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ms_secondary_events**
> get_ms_secondary_events(account_id, identifier, start_time, end_time, org_identifier=org_identifier, project_identifier=project_identifier)



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
api_instance = harness_python_sdk.MonitoredServicesApi(harness_python_sdk.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier for the Entity.
identifier = 'identifier_example' # str | 
start_time = 789 # int | 
end_time = 789 # int | 
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    api_instance.get_ms_secondary_events(account_id, identifier, start_time, end_time, org_identifier=org_identifier, project_identifier=project_identifier)
except ApiException as e:
    print("Exception when calling MonitoredServicesApi->get_ms_secondary_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier for the Entity. | 
 **identifier** | **str**|  | 
 **start_time** | **int**|  | 
 **end_time** | **int**|  | 
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

# **get_ms_secondary_events_details**
> get_ms_secondary_events_details(account_id, secondary_event_type, identifiers)



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
api_instance = harness_python_sdk.MonitoredServicesApi(harness_python_sdk.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier for the Entity.
secondary_event_type = 'secondary_event_type_example' # str | 
identifiers = ['identifiers_example'] # list[str] | 

try:
    api_instance.get_ms_secondary_events_details(account_id, secondary_event_type, identifiers)
except ApiException as e:
    print("Exception when calling MonitoredServicesApi->get_ms_secondary_events_details: %s\n" % e)
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

# **get_notification_rules_for_monitored_service**
> ResponseDTOPageResponseNotificationRuleResponse get_notification_rules_for_monitored_service(account_id, org_identifier, project_identifier, identifier, page_number=page_number, page_size=page_size)

Get notification rules for MonitoredService

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
api_instance = harness_python_sdk.MonitoredServicesApi(harness_python_sdk.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
identifier = 'identifier_example' # str | Identifier for the Entity.
page_number = 0 # int | Page Index of the results to fetch.Default Value: 0 (optional) (default to 0)
page_size = 10 # int | Results per page (optional) (default to 10)

try:
    # Get notification rules for MonitoredService
    api_response = api_instance.get_notification_rules_for_monitored_service(account_id, org_identifier, project_identifier, identifier, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitoredServicesApi->get_notification_rules_for_monitored_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **identifier** | **str**| Identifier for the Entity. | 
 **page_number** | **int**| Page Index of the results to fetch.Default Value: 0 | [optional] [default to 0]
 **page_size** | **int**| Results per page | [optional] [default to 10]

### Return type

[**ResponseDTOPageResponseNotificationRuleResponse**](ResponseDTOPageResponseNotificationRuleResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_over_all_health_score**
> get_over_all_health_score(account_id, org_identifier, project_identifier, identifier, end_time, duration=duration, start_time=start_time)



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
api_instance = harness_python_sdk.MonitoredServicesApi(harness_python_sdk.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
identifier = 'identifier_example' # str | 
end_time = 789 # int | 
duration = 'duration_example' # str |  (optional)
start_time = 789 # int |  (optional)

try:
    api_instance.get_over_all_health_score(account_id, org_identifier, project_identifier, identifier, end_time, duration=duration, start_time=start_time)
except ApiException as e:
    print("Exception when calling MonitoredServicesApi->get_over_all_health_score: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **identifier** | **str**|  | 
 **end_time** | **int**|  | 
 **duration** | **str**|  | [optional] 
 **start_time** | **int**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_services**
> get_services(account_id, org_identifier, project_identifier)



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
api_instance = harness_python_sdk.MonitoredServicesApi(harness_python_sdk.ApiClient(configuration))
account_id = 'account_id_example' # str | 
org_identifier = 'org_identifier_example' # str | 
project_identifier = 'project_identifier_example' # str | 

try:
    api_instance.get_services(account_id, org_identifier, project_identifier)
except ApiException as e:
    print("Exception when calling MonitoredServicesApi->get_services: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **org_identifier** | **str**|  | 
 **project_identifier** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_slo_metrics**
> get_slo_metrics(account_id, org_identifier, project_identifier, monitored_service_identifier, health_source_identifier)



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
api_instance = harness_python_sdk.MonitoredServicesApi(harness_python_sdk.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
monitored_service_identifier = 'monitored_service_identifier_example' # str | 
health_source_identifier = 'health_source_identifier_example' # str | 

try:
    api_instance.get_slo_metrics(account_id, org_identifier, project_identifier, monitored_service_identifier, health_source_identifier)
except ApiException as e:
    print("Exception when calling MonitoredServicesApi->get_slo_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **monitored_service_identifier** | **str**|  | 
 **health_source_identifier** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> list(account_id, org_identifier, project_identifier, offset, page_size, services_at_risk_filter, environment_identifier=environment_identifier, environment_identifiers=environment_identifiers, service_identifier=service_identifier, filter=filter, monitored_service_type=monitored_service_type)



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
api_instance = harness_python_sdk.MonitoredServicesApi(harness_python_sdk.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
offset = 56 # int | 
page_size = 56 # int | 
services_at_risk_filter = true # bool | 
environment_identifier = 'environment_identifier_example' # str |  (optional)
environment_identifiers = ['environment_identifiers_example'] # list[str] |  (optional)
service_identifier = 'service_identifier_example' # str |  (optional)
filter = 'filter_example' # str |  (optional)
monitored_service_type = 'monitored_service_type_example' # str |  (optional)

try:
    api_instance.list(account_id, org_identifier, project_identifier, offset, page_size, services_at_risk_filter, environment_identifier=environment_identifier, environment_identifiers=environment_identifiers, service_identifier=service_identifier, filter=filter, monitored_service_type=monitored_service_type)
except ApiException as e:
    print("Exception when calling MonitoredServicesApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **offset** | **int**|  | 
 **page_size** | **int**|  | 
 **services_at_risk_filter** | **bool**|  | 
 **environment_identifier** | **str**|  | [optional] 
 **environment_identifiers** | [**list[str]**](str.md)|  | [optional] 
 **service_identifier** | **str**|  | [optional] 
 **filter** | **str**|  | [optional] 
 **monitored_service_type** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_monitored_service**
> RestResponseMonitoredServiceResponse save_monitored_service(body, account_id)

Saves monitored service data

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
api_instance = harness_python_sdk.MonitoredServicesApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.MonitoredService() # MonitoredService | 
account_id = 'account_id_example' # str | 

try:
    # Saves monitored service data
    api_response = api_instance.save_monitored_service(body, account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitoredServicesApi->save_monitored_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MonitoredService**](MonitoredService.md)|  | 
 **account_id** | **str**|  | 

### Return type

[**RestResponseMonitoredServiceResponse**](RestResponseMonitoredServiceResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_monitored_service_from_template_input**
> RestResponseMonitoredServiceResponse save_monitored_service_from_template_input(body, account_id, org_identifier, project_identifier)

Saves monitored service from template input

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
api_instance = harness_python_sdk.MonitoredServicesApi(harness_python_sdk.ApiClient(configuration))
body = 'body_example' # str | Template input yaml for the monitored service creation from given template
account_id = 'account_id_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.

try:
    # Saves monitored service from template input
    api_response = api_instance.save_monitored_service_from_template_input(body, account_id, org_identifier, project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitoredServicesApi->save_monitored_service_from_template_input: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| Template input yaml for the monitored service creation from given template | 
 **account_id** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 

### Return type

[**RestResponseMonitoredServiceResponse**](RestResponseMonitoredServiceResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_monitored_service_from_yaml**
> save_monitored_service_from_yaml(body, account_id, org_identifier, project_identifier)



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
api_instance = harness_python_sdk.MonitoredServicesApi(harness_python_sdk.ApiClient(configuration))
body = 'body_example' # str | 
account_id = 'account_id_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.

try:
    api_instance.save_monitored_service_from_yaml(body, account_id, org_identifier, project_identifier)
except ApiException as e:
    print("Exception when calling MonitoredServicesApi->save_monitored_service_from_yaml: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)|  | 
 **account_id** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_health_monitoring_flag**
> set_health_monitoring_flag(account_id, org_identifier, project_identifier, identifier, enable)



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
api_instance = harness_python_sdk.MonitoredServicesApi(harness_python_sdk.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
identifier = 'identifier_example' # str | 
enable = true # bool | 

try:
    api_instance.set_health_monitoring_flag(account_id, org_identifier, project_identifier, identifier, enable)
except ApiException as e:
    print("Exception when calling MonitoredServicesApi->set_health_monitoring_flag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **identifier** | **str**|  | 
 **enable** | **bool**|  | 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_monitored_service**
> RestResponseMonitoredServiceResponse update_monitored_service(body, account_id, identifier)

Updates monitored service data

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
api_instance = harness_python_sdk.MonitoredServicesApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.MonitoredService() # MonitoredService | 
account_id = 'account_id_example' # str | Account Identifier for the Entity.
identifier = 'identifier_example' # str | Identifier for the Entity.

try:
    # Updates monitored service data
    api_response = api_instance.update_monitored_service(body, account_id, identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitoredServicesApi->update_monitored_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MonitoredService**](MonitoredService.md)|  | 
 **account_id** | **str**| Account Identifier for the Entity. | 
 **identifier** | **str**| Identifier for the Entity. | 

### Return type

[**RestResponseMonitoredServiceResponse**](RestResponseMonitoredServiceResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_monitored_service_from_template_input**
> RestResponseMonitoredServiceResponse update_monitored_service_from_template_input(body, account_id, org_identifier, project_identifier, identifier)

Update monitored service from yaml or template

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
api_instance = harness_python_sdk.MonitoredServicesApi(harness_python_sdk.ApiClient(configuration))
body = 'body_example' # str | Template input yaml for the monitored service creation from given template
account_id = 'account_id_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
identifier = 'identifier_example' # str | Identifier for the Entity.

try:
    # Update monitored service from yaml or template
    api_response = api_instance.update_monitored_service_from_template_input(body, account_id, org_identifier, project_identifier, identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitoredServicesApi->update_monitored_service_from_template_input: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| Template input yaml for the monitored service creation from given template | 
 **account_id** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **identifier** | **str**| Identifier for the Entity. | 

### Return type

[**RestResponseMonitoredServiceResponse**](RestResponseMonitoredServiceResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_monitored_service_from_yaml**
> update_monitored_service_from_yaml(body, account_id, org_identifier, project_identifier, identifier)



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
api_instance = harness_python_sdk.MonitoredServicesApi(harness_python_sdk.ApiClient(configuration))
body = 'body_example' # str | 
account_id = 'account_id_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
identifier = 'identifier_example' # str | 

try:
    api_instance.update_monitored_service_from_yaml(body, account_id, org_identifier, project_identifier, identifier)
except ApiException as e:
    print("Exception when calling MonitoredServicesApi->update_monitored_service_from_yaml: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)|  | 
 **account_id** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **identifier** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **yaml_template**
> yaml_template(account_id, org_identifier, project_identifier, type=type)



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
api_instance = harness_python_sdk.MonitoredServicesApi(harness_python_sdk.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
type = 'type_example' # str |  (optional)

try:
    api_instance.yaml_template(account_id, org_identifier, project_identifier, type=type)
except ApiException as e:
    print("Exception when calling MonitoredServicesApi->yaml_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **type** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

