# harness_python_sdk.TriggersEventsApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**polled_response_trigger_identifier**](TriggersEventsApi.md#polled_response_trigger_identifier) | **GET** /pipeline/api/triggers/eventHistory/polledResponse/{triggerIdentifier} | Get all the polled response for a given trigger
[**trigger_event_history_build_source_type**](TriggersEventsApi.md#trigger_event_history_build_source_type) | **GET** /pipeline/api/triggers/eventHistory/artifact-manifest-info | Get artifact and manifest trigger event history based on build source type
[**trigger_event_history_new**](TriggersEventsApi.md#trigger_event_history_new) | **GET** /pipeline/api/triggers/eventHistory/{triggerIdentifier} | Get event history for a trigger
[**trigger_history_event_correlation**](TriggersEventsApi.md#trigger_history_event_correlation) | **GET** /pipeline/api/triggers/eventHistory/eventCorrelation/{eventCorrelationId} | Get Trigger history event correlation
[**trigger_history_event_correlation_v2**](TriggersEventsApi.md#trigger_history_event_correlation_v2) | **GET** /pipeline/api/triggers/eventHistory/v2/eventCorrelation/{eventCorrelationId} | Get Trigger history event correlation V2

# **polled_response_trigger_identifier**
> ResponseDTOPollingInfoForTriggers polled_response_trigger_identifier(account_identifier, org_identifier, project_identifier, target_identifier, trigger_identifier)

Get all the polled response for a given trigger

Get all the polled response for a given trigger

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
api_instance = harness_python_sdk.TriggersEventsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | 
org_identifier = 'org_identifier_example' # str | 
project_identifier = 'project_identifier_example' # str | 
target_identifier = 'target_identifier_example' # str | Identifier of the target pipeline under which trigger resides
trigger_identifier = 'trigger_identifier_example' # str | 

try:
    # Get all the polled response for a given trigger
    api_response = api_instance.polled_response_trigger_identifier(account_identifier, org_identifier, project_identifier, target_identifier, trigger_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TriggersEventsApi->polled_response_trigger_identifier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**|  | 
 **org_identifier** | **str**|  | 
 **project_identifier** | **str**|  | 
 **target_identifier** | **str**| Identifier of the target pipeline under which trigger resides | 
 **trigger_identifier** | **str**|  | 

### Return type

[**ResponseDTOPollingInfoForTriggers**](ResponseDTOPollingInfoForTriggers.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trigger_event_history_build_source_type**
> ResponseDTOPageNGTriggerEventHistoryDTO trigger_event_history_build_source_type(account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, target_identifier=target_identifier, artifact_type=artifact_type, search_term=search_term, page=page, size=size, sort=sort)

Get artifact and manifest trigger event history based on build source type

Get artifact and manifest trigger event history based on build source type

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
api_instance = harness_python_sdk.TriggersEventsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | 
org_identifier = 'org_identifier_example' # str |  (optional)
project_identifier = 'project_identifier_example' # str |  (optional)
target_identifier = 'target_identifier_example' # str | Identifier of the target pipeline under which trigger resides (optional)
artifact_type = 'artifact_type_example' # str | Type of artifact source (optional)
search_term = 'search_term_example' # str | Search term to filter out pipelines based on pipeline name, identifier, tags. (optional)
page = 0 # int | Page Index of the results to fetch.Default Value: 0 (optional) (default to 0)
size = 10 # int | Results per page (optional) (default to 10)
sort = ['sort_example'] # list[str] | Sort criteria for the elements. (optional)

try:
    # Get artifact and manifest trigger event history based on build source type
    api_response = api_instance.trigger_event_history_build_source_type(account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, target_identifier=target_identifier, artifact_type=artifact_type, search_term=search_term, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TriggersEventsApi->trigger_event_history_build_source_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**|  | 
 **org_identifier** | **str**|  | [optional] 
 **project_identifier** | **str**|  | [optional] 
 **target_identifier** | **str**| Identifier of the target pipeline under which trigger resides | [optional] 
 **artifact_type** | **str**| Type of artifact source | [optional] 
 **search_term** | **str**| Search term to filter out pipelines based on pipeline name, identifier, tags. | [optional] 
 **page** | **int**| Page Index of the results to fetch.Default Value: 0 | [optional] [default to 0]
 **size** | **int**| Results per page | [optional] [default to 10]
 **sort** | [**list[str]**](str.md)| Sort criteria for the elements. | [optional] 

### Return type

[**ResponseDTOPageNGTriggerEventHistoryDTO**](ResponseDTOPageNGTriggerEventHistoryDTO.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trigger_event_history_new**
> ResponseDTOPageNGTriggerEventHistoryDTO trigger_event_history_new(account_identifier, org_identifier, project_identifier, target_identifier, trigger_identifier, search_term=search_term, page=page, size=size, sort=sort)

Get event history for a trigger

Get event history for a trigger

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
api_instance = harness_python_sdk.TriggersEventsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | 
org_identifier = 'org_identifier_example' # str | 
project_identifier = 'project_identifier_example' # str | 
target_identifier = 'target_identifier_example' # str | Identifier of the target pipeline under which trigger resides
trigger_identifier = 'trigger_identifier_example' # str | 
search_term = 'search_term_example' # str | Search term to filter out pipelines based on pipeline name, identifier, tags. (optional)
page = 0 # int | Page Index of the results to fetch.Default Value: 0 (optional) (default to 0)
size = 10 # int | Results per page (optional) (default to 10)
sort = ['sort_example'] # list[str] | Sort criteria for the elements. (optional)

try:
    # Get event history for a trigger
    api_response = api_instance.trigger_event_history_new(account_identifier, org_identifier, project_identifier, target_identifier, trigger_identifier, search_term=search_term, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TriggersEventsApi->trigger_event_history_new: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**|  | 
 **org_identifier** | **str**|  | 
 **project_identifier** | **str**|  | 
 **target_identifier** | **str**| Identifier of the target pipeline under which trigger resides | 
 **trigger_identifier** | **str**|  | 
 **search_term** | **str**| Search term to filter out pipelines based on pipeline name, identifier, tags. | [optional] 
 **page** | **int**| Page Index of the results to fetch.Default Value: 0 | [optional] [default to 0]
 **size** | **int**| Results per page | [optional] [default to 10]
 **sort** | [**list[str]**](str.md)| Sort criteria for the elements. | [optional] 

### Return type

[**ResponseDTOPageNGTriggerEventHistoryDTO**](ResponseDTOPageNGTriggerEventHistoryDTO.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trigger_history_event_correlation**
> ResponseDTOPageNGTriggerEventHistoryBaseDTO trigger_history_event_correlation(account_identifier, event_correlation_id, page=page, size=size, sort=sort)

Get Trigger history event correlation

Get Trigger history event correlation

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
api_instance = harness_python_sdk.TriggersEventsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | 
event_correlation_id = 'event_correlation_id_example' # str | 
page = 0 # int | Page Index of the results to fetch.Default Value: 0 (optional) (default to 0)
size = 10 # int | Results per page (optional) (default to 10)
sort = ['sort_example'] # list[str] | Sort criteria for the elements. (optional)

try:
    # Get Trigger history event correlation
    api_response = api_instance.trigger_history_event_correlation(account_identifier, event_correlation_id, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TriggersEventsApi->trigger_history_event_correlation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**|  | 
 **event_correlation_id** | **str**|  | 
 **page** | **int**| Page Index of the results to fetch.Default Value: 0 | [optional] [default to 0]
 **size** | **int**| Results per page | [optional] [default to 10]
 **sort** | [**list[str]**](str.md)| Sort criteria for the elements. | [optional] 

### Return type

[**ResponseDTOPageNGTriggerEventHistoryBaseDTO**](ResponseDTOPageNGTriggerEventHistoryBaseDTO.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trigger_history_event_correlation_v2**
> ResponseDTOPageNGTriggerEventHistoryDTO trigger_history_event_correlation_v2(account_identifier, event_correlation_id, page=page, size=size, sort=sort)

Get Trigger history event correlation V2

Get Trigger history event correlation V2

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
api_instance = harness_python_sdk.TriggersEventsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | 
event_correlation_id = 'event_correlation_id_example' # str | 
page = 0 # int | Page Index of the results to fetch.Default Value: 0 (optional) (default to 0)
size = 10 # int | Results per page (optional) (default to 10)
sort = ['sort_example'] # list[str] | Sort criteria for the elements. (optional)

try:
    # Get Trigger history event correlation V2
    api_response = api_instance.trigger_history_event_correlation_v2(account_identifier, event_correlation_id, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TriggersEventsApi->trigger_history_event_correlation_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**|  | 
 **event_correlation_id** | **str**|  | 
 **page** | **int**| Page Index of the results to fetch.Default Value: 0 | [optional] [default to 0]
 **size** | **int**| Results per page | [optional] [default to 10]
 **sort** | [**list[str]**](str.md)| Sort criteria for the elements. | [optional] 

### Return type

[**ResponseDTOPageNGTriggerEventHistoryDTO**](ResponseDTOPageNGTriggerEventHistoryDTO.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

