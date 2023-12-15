# swagger_client.NGSLOsApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_slo_data_ng**](NGSLOsApi.md#delete_slo_data_ng) | **DELETE** /cv/api/account/{accountIdentifier}/org/{orgIdentifier}/project/{projectIdentifier}/slo/v2/identifier/{identifier} | Delete SLO data
[**get_onboarding_graph_ng**](NGSLOsApi.md#get_onboarding_graph_ng) | **POST** /cv/api/account/{accountIdentifier}/org/{orgIdentifier}/project/{projectIdentifier}/slo/v2/composite-slo/onboarding-graph | Get onBoarding graph for composite slo
[**get_service_level_objective_ng**](NGSLOsApi.md#get_service_level_objective_ng) | **GET** /cv/api/account/{accountIdentifier}/org/{orgIdentifier}/project/{projectIdentifier}/slo/v2/identifier/{identifier} | Get SLO data
[**get_service_level_objectives_ng**](NGSLOsApi.md#get_service_level_objectives_ng) | **GET** /cv/api/account/{accountIdentifier}/org/{orgIdentifier}/project/{projectIdentifier}/slo/v2 | Get all SLOs
[**get_slo_health_list_view_ng**](NGSLOsApi.md#get_slo_health_list_view_ng) | **POST** /cv/api/account/{accountIdentifier}/org/{orgIdentifier}/project/{projectIdentifier}/slo/v2/status-list | Get SLO list view
[**save_slo_data_ng**](NGSLOsApi.md#save_slo_data_ng) | **POST** /cv/api/account/{accountIdentifier}/org/{orgIdentifier}/project/{projectIdentifier}/slo/v2 | Saves SLO data
[**update_slo_data_ng**](NGSLOsApi.md#update_slo_data_ng) | **PUT** /cv/api/account/{accountIdentifier}/org/{orgIdentifier}/project/{projectIdentifier}/slo/v2/identifier/{identifier} | Update SLO data

# **delete_slo_data_ng**
> CvRestResponseBoolean delete_slo_data_ng(identifier, account_identifier, org_identifier, project_identifier)

Delete SLO data

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
api_instance = swagger_client.NGSLOsApi(swagger_client.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier for the Entity.
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.

try:
    # Delete SLO data
    api_response = api_instance.delete_slo_data_ng(identifier, account_identifier, org_identifier, project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NGSLOsApi->delete_slo_data_ng: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier for the Entity. | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 

### Return type

[**CvRestResponseBoolean**](CvRestResponseBoolean.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_onboarding_graph_ng**
> RestResponseTimeGraphResponse get_onboarding_graph_ng(body, account_identifier, org_identifier, project_identifier)

Get onBoarding graph for composite slo

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
api_instance = swagger_client.NGSLOsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CompositeServiceLevelObjectiveSpec() # CompositeServiceLevelObjectiveSpec | Composite SLO spec which consists of list of SLO details
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.

try:
    # Get onBoarding graph for composite slo
    api_response = api_instance.get_onboarding_graph_ng(body, account_identifier, org_identifier, project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NGSLOsApi->get_onboarding_graph_ng: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CompositeServiceLevelObjectiveSpec**](CompositeServiceLevelObjectiveSpec.md)| Composite SLO spec which consists of list of SLO details | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 

### Return type

[**RestResponseTimeGraphResponse**](RestResponseTimeGraphResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_level_objective_ng**
> RestResponseServiceLevelObjectiveV2Response get_service_level_objective_ng(identifier, account_identifier, org_identifier, project_identifier)

Get SLO data

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
api_instance = swagger_client.NGSLOsApi(swagger_client.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier for the Entity.
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.

try:
    # Get SLO data
    api_response = api_instance.get_service_level_objective_ng(identifier, account_identifier, org_identifier, project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NGSLOsApi->get_service_level_objective_ng: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier for the Entity. | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 

### Return type

[**RestResponseServiceLevelObjectiveV2Response**](RestResponseServiceLevelObjectiveV2Response.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_level_objectives_ng**
> ResponseDTOPageResponseServiceLevelObjectiveV2Response get_service_level_objectives_ng(account_identifier, org_identifier, project_identifier, offset, page_size, user_journeys=user_journeys, identifiers=identifiers, target_types=target_types, error_budget_risks=error_budget_risks)

Get all SLOs

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
api_instance = swagger_client.NGSLOsApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
offset = 56 # int | Page Index of the results to fetch.Default Value: 0
page_size = 56 # int | Results per page
user_journeys = ['user_journeys_example'] # list[str] |  (optional)
identifiers = ['identifiers_example'] # list[str] |  (optional)
target_types = ['target_types_example'] # list[str] |  (optional)
error_budget_risks = ['error_budget_risks_example'] # list[str] |  (optional)

try:
    # Get all SLOs
    api_response = api_instance.get_service_level_objectives_ng(account_identifier, org_identifier, project_identifier, offset, page_size, user_journeys=user_journeys, identifiers=identifiers, target_types=target_types, error_budget_risks=error_budget_risks)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NGSLOsApi->get_service_level_objectives_ng: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **offset** | **int**| Page Index of the results to fetch.Default Value: 0 | 
 **page_size** | **int**| Results per page | 
 **user_journeys** | [**list[str]**](str.md)|  | [optional] 
 **identifiers** | [**list[str]**](str.md)|  | [optional] 
 **target_types** | [**list[str]**](str.md)|  | [optional] 
 **error_budget_risks** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**ResponseDTOPageResponseServiceLevelObjectiveV2Response**](ResponseDTOPageResponseServiceLevelObjectiveV2Response.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_slo_health_list_view_ng**
> ResponseDTOPageResponseSLOHealthListView get_slo_health_list_view_ng(account_identifier, org_identifier, project_identifier, body=body, page_number=page_number, page_size=page_size)

Get SLO list view

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
api_instance = swagger_client.NGSLOsApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
body = swagger_client.SLODashboardApiFilter() # SLODashboardApiFilter |  (optional)
page_number = 0 # int | Page Index of the results to fetch.Default Value: 0 (optional) (default to 0)
page_size = 10 # int | Results per page (optional) (default to 10)

try:
    # Get SLO list view
    api_response = api_instance.get_slo_health_list_view_ng(account_identifier, org_identifier, project_identifier, body=body, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NGSLOsApi->get_slo_health_list_view_ng: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **body** | [**SLODashboardApiFilter**](SLODashboardApiFilter.md)|  | [optional] 
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

# **save_slo_data_ng**
> RestResponseServiceLevelObjectiveV2Response save_slo_data_ng(body, account_identifier, org_identifier, project_identifier)

Saves SLO data

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
api_instance = swagger_client.NGSLOsApi(swagger_client.ApiClient(configuration))
body = swagger_client.AbstractServiceLevelObjective() # AbstractServiceLevelObjective | Details of the SLO to be saved
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.

try:
    # Saves SLO data
    api_response = api_instance.save_slo_data_ng(body, account_identifier, org_identifier, project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NGSLOsApi->save_slo_data_ng: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AbstractServiceLevelObjective**](AbstractServiceLevelObjective.md)| Details of the SLO to be saved | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 

### Return type

[**RestResponseServiceLevelObjectiveV2Response**](RestResponseServiceLevelObjectiveV2Response.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_slo_data_ng**
> RestResponseServiceLevelObjectiveV2Response update_slo_data_ng(body, identifier, account_identifier, org_identifier, project_identifier)

Update SLO data

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
api_instance = swagger_client.NGSLOsApi(swagger_client.ApiClient(configuration))
body = swagger_client.AbstractServiceLevelObjective() # AbstractServiceLevelObjective | Details of the SLO to be updated
identifier = 'identifier_example' # str | Identifier for the Entity.
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.

try:
    # Update SLO data
    api_response = api_instance.update_slo_data_ng(body, identifier, account_identifier, org_identifier, project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NGSLOsApi->update_slo_data_ng: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AbstractServiceLevelObjective**](AbstractServiceLevelObjective.md)| Details of the SLO to be updated | 
 **identifier** | **str**| Identifier for the Entity. | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 

### Return type

[**RestResponseServiceLevelObjectiveV2Response**](RestResponseServiceLevelObjectiveV2Response.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

