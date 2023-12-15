# swagger_client.TriggersApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_trigger**](TriggersApi.md#create_trigger) | **POST** /pipeline/api/triggers | Creates Trigger for triggering target pipeline identifier.
[**delete_trigger**](TriggersApi.md#delete_trigger) | **DELETE** /pipeline/api/triggers/{triggerIdentifier} | Deletes Trigger by identifier.
[**get_list_for_target**](TriggersApi.md#get_list_for_target) | **GET** /pipeline/api/triggers | Gets the paginated list of triggers for accountIdentifier, orgIdentifier, projectIdentifier, targetIdentifier.
[**get_trigger**](TriggersApi.md#get_trigger) | **GET** /pipeline/api/triggers/{triggerIdentifier} | Gets the trigger by accountIdentifier, orgIdentifier, projectIdentifier, targetIdentifier and triggerIdentifier.
[**get_trigger_catalog**](TriggersApi.md#get_trigger_catalog) | **GET** /pipeline/api/triggers/catalog | Lists all Triggers
[**get_trigger_details**](TriggersApi.md#get_trigger_details) | **GET** /pipeline/api/triggers/{triggerIdentifier}/details | Fetches Trigger details for a specific accountIdentifier, orgIdentifier, projectIdentifier, targetIdentifier, triggerIdentifier.
[**trigger_event_history**](TriggersApi.md#trigger_event_history) | **GET** /pipeline/api/triggers/{triggerIdentifier}/eventHistory | Get event history for a trigger
[**update_trigger**](TriggersApi.md#update_trigger) | **PUT** /pipeline/api/triggers/{triggerIdentifier} | Updates trigger for pipeline with target pipeline identifier.

# **create_trigger**
> ResponseDTONGTriggerResponse create_trigger(body, account_identifier, org_identifier, project_identifier, target_identifier, ignore_error=ignore_error, with_service_v2=with_service_v2)

Creates Trigger for triggering target pipeline identifier.

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
api_instance = swagger_client.TriggersApi(swagger_client.ApiClient(configuration))
body = '{   \"summary\" : \"Sample Create Trigger YAML\",   \"description\" : \"Sample Triggers YAML\",   \"value\" : \"trigger:\\n  name: Trigger\\n  identifier: Trigger\\n  enabled: true\\n  orgIdentifier: default\\n  projectIdentifier: Terraform_Provider\\n  pipelineIdentifier: Terraform_NG_Acc_Tests_With_Notifications\\n  source:\\n    type: Scheduled\\n    spec:\\n      type: Cron\\n      spec:\\n        expression: 0 8,20 * * *\\n  inputYaml: |\\n    pipeline:\\n      identifier: Terraform_NG_Acc_Tests_With_Notifications\\n      properties:\\n        ci:\\n          codebase:\\n            build:\\n              type: branch\\n              spec:\\n                branch: main\" }' # str | Triggers YAML
account_identifier = 'account_identifier_example' # str | 
org_identifier = 'org_identifier_example' # str | 
project_identifier = 'project_identifier_example' # str | 
target_identifier = 'target_identifier_example' # str | Identifier of the target pipeline
ignore_error = false # bool |  (optional) (default to false)
with_service_v2 = false # bool |  (optional) (default to false)

try:
    # Creates Trigger for triggering target pipeline identifier.
    api_response = api_instance.create_trigger(body, account_identifier, org_identifier, project_identifier, target_identifier, ignore_error=ignore_error, with_service_v2=with_service_v2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TriggersApi->create_trigger: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| Triggers YAML | 
 **account_identifier** | **str**|  | 
 **org_identifier** | **str**|  | 
 **project_identifier** | **str**|  | 
 **target_identifier** | **str**| Identifier of the target pipeline | 
 **ignore_error** | **bool**|  | [optional] [default to false]
 **with_service_v2** | **bool**|  | [optional] [default to false]

### Return type

[**ResponseDTONGTriggerResponse**](ResponseDTONGTriggerResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_trigger**
> ResponseDTOBoolean delete_trigger(account_identifier, org_identifier, project_identifier, target_identifier, trigger_identifier, if_match=if_match)

Deletes Trigger by identifier.

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
api_instance = swagger_client.TriggersApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | 
org_identifier = 'org_identifier_example' # str | 
project_identifier = 'project_identifier_example' # str | 
target_identifier = 'target_identifier_example' # str | Identifier of the target pipeline under which trigger resides.
trigger_identifier = 'trigger_identifier_example' # str | 
if_match = 'if_match_example' # str |  (optional)

try:
    # Deletes Trigger by identifier.
    api_response = api_instance.delete_trigger(account_identifier, org_identifier, project_identifier, target_identifier, trigger_identifier, if_match=if_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TriggersApi->delete_trigger: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**|  | 
 **org_identifier** | **str**|  | 
 **project_identifier** | **str**|  | 
 **target_identifier** | **str**| Identifier of the target pipeline under which trigger resides. | 
 **trigger_identifier** | **str**|  | 
 **if_match** | **str**|  | [optional] 

### Return type

[**ResponseDTOBoolean**](ResponseDTOBoolean.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_for_target**
> ResponseDTOPageResponseNGTriggerDetailsResponseDTO get_list_for_target(account_identifier, org_identifier, project_identifier, target_identifier, body=body, filter=filter, page=page, size=size, sort=sort, search_term=search_term)

Gets the paginated list of triggers for accountIdentifier, orgIdentifier, projectIdentifier, targetIdentifier.

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
api_instance = swagger_client.TriggersApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | 
org_identifier = 'org_identifier_example' # str | 
project_identifier = 'project_identifier_example' # str | 
target_identifier = 'target_identifier_example' # str | Identifier of the target pipeline
body = swagger_client.TriggerFilterProperties() # TriggerFilterProperties | This contains details of Trigger filters based on Trigger Types and Trigger Names  (optional)
filter = 'filter_example' # str |  (optional)
page = 0 # int |  (optional) (default to 0)
size = 25 # int |  (optional) (default to 25)
sort = ['sort_example'] # list[str] |  (optional)
search_term = 'search_term_example' # str |  (optional)

try:
    # Gets the paginated list of triggers for accountIdentifier, orgIdentifier, projectIdentifier, targetIdentifier.
    api_response = api_instance.get_list_for_target(account_identifier, org_identifier, project_identifier, target_identifier, body=body, filter=filter, page=page, size=size, sort=sort, search_term=search_term)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TriggersApi->get_list_for_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**|  | 
 **org_identifier** | **str**|  | 
 **project_identifier** | **str**|  | 
 **target_identifier** | **str**| Identifier of the target pipeline | 
 **body** | [**TriggerFilterProperties**](TriggerFilterProperties.md)| This contains details of Trigger filters based on Trigger Types and Trigger Names  | [optional] 
 **filter** | **str**|  | [optional] 
 **page** | **int**|  | [optional] [default to 0]
 **size** | **int**|  | [optional] [default to 25]
 **sort** | [**list[str]**](str.md)|  | [optional] 
 **search_term** | **str**|  | [optional] 

### Return type

[**ResponseDTOPageResponseNGTriggerDetailsResponseDTO**](ResponseDTOPageResponseNGTriggerDetailsResponseDTO.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trigger**
> ResponseDTONGTriggerResponse get_trigger(account_identifier, org_identifier, project_identifier, target_identifier, trigger_identifier)

Gets the trigger by accountIdentifier, orgIdentifier, projectIdentifier, targetIdentifier and triggerIdentifier.

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
api_instance = swagger_client.TriggersApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | 
org_identifier = 'org_identifier_example' # str | 
project_identifier = 'project_identifier_example' # str | 
target_identifier = 'target_identifier_example' # str | Identifier of the target pipeline under which trigger resides
trigger_identifier = 'trigger_identifier_example' # str | 

try:
    # Gets the trigger by accountIdentifier, orgIdentifier, projectIdentifier, targetIdentifier and triggerIdentifier.
    api_response = api_instance.get_trigger(account_identifier, org_identifier, project_identifier, target_identifier, trigger_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TriggersApi->get_trigger: %s\n" % e)
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

[**ResponseDTONGTriggerResponse**](ResponseDTONGTriggerResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trigger_catalog**
> ResponseDTOTriggerCatalogResponse get_trigger_catalog(account_identifier)

Lists all Triggers

Lists all the Triggers for the given Account ID.

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
api_instance = swagger_client.TriggersApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Lists all Triggers
    api_response = api_instance.get_trigger_catalog(account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TriggersApi->get_trigger_catalog: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**ResponseDTOTriggerCatalogResponse**](ResponseDTOTriggerCatalogResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trigger_details**
> ResponseDTONGTriggerDetailsResponseDTO get_trigger_details(account_identifier, org_identifier, project_identifier, trigger_identifier, target_identifier)

Fetches Trigger details for a specific accountIdentifier, orgIdentifier, projectIdentifier, targetIdentifier, triggerIdentifier.

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
api_instance = swagger_client.TriggersApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | 
org_identifier = 'org_identifier_example' # str | 
project_identifier = 'project_identifier_example' # str | 
trigger_identifier = 'trigger_identifier_example' # str | Identifier of the target pipeline
target_identifier = 'target_identifier_example' # str | 

try:
    # Fetches Trigger details for a specific accountIdentifier, orgIdentifier, projectIdentifier, targetIdentifier, triggerIdentifier.
    api_response = api_instance.get_trigger_details(account_identifier, org_identifier, project_identifier, trigger_identifier, target_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TriggersApi->get_trigger_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**|  | 
 **org_identifier** | **str**|  | 
 **project_identifier** | **str**|  | 
 **trigger_identifier** | **str**| Identifier of the target pipeline | 
 **target_identifier** | **str**|  | 

### Return type

[**ResponseDTONGTriggerDetailsResponseDTO**](ResponseDTONGTriggerDetailsResponseDTO.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trigger_event_history**
> ResponseDTOPageNGTriggerEventHistoryDTO trigger_event_history(account_identifier, org_identifier, project_identifier, target_identifier, trigger_identifier, search_term=search_term, page=page, size=size, sort=sort)

Get event history for a trigger

Get event history for a trigger

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
api_instance = swagger_client.TriggersApi(swagger_client.ApiClient(configuration))
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
    api_response = api_instance.trigger_event_history(account_identifier, org_identifier, project_identifier, target_identifier, trigger_identifier, search_term=search_term, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TriggersApi->trigger_event_history: %s\n" % e)
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

# **update_trigger**
> ResponseDTONGTriggerResponse update_trigger(body, account_identifier, org_identifier, project_identifier, target_identifier, trigger_identifier, if_match=if_match, ignore_error=ignore_error)

Updates trigger for pipeline with target pipeline identifier.

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
api_instance = swagger_client.TriggersApi(swagger_client.ApiClient(configuration))
body = '{   \"summary\" : \"Sample Update Trigger YAML\",   \"description\" : \"Sample Triggers YAML\",   \"value\" : \"trigger:\\n  name: Trigger\\n  identifier: Trigger\\n  enabled: true\\n  orgIdentifier: default\\n  projectIdentifier: Terraform_Provider\\n  pipelineIdentifier: Terraform_NG_Acc_Tests_With_Notifications\\n  source:\\n    type: Scheduled\\n    spec:\\n      type: Cron\\n      spec:\\n        expression: 0 8,20 * * *\\n  inputYaml: |\\n    pipeline:\\n      identifier: Terraform_NG_Acc_Tests_With_Notifications\\n      properties:\\n        ci:\\n          codebase:\\n            build:\\n              type: branch\\n              spec:\\n                branch: main\" }' # str | Triggers YAML
account_identifier = 'account_identifier_example' # str | 
org_identifier = 'org_identifier_example' # str | 
project_identifier = 'project_identifier_example' # str | 
target_identifier = 'target_identifier_example' # str | Identifier of the target pipeline under which trigger resides
trigger_identifier = 'trigger_identifier_example' # str | 
if_match = 'if_match_example' # str |  (optional)
ignore_error = false # bool |  (optional) (default to false)

try:
    # Updates trigger for pipeline with target pipeline identifier.
    api_response = api_instance.update_trigger(body, account_identifier, org_identifier, project_identifier, target_identifier, trigger_identifier, if_match=if_match, ignore_error=ignore_error)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TriggersApi->update_trigger: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| Triggers YAML | 
 **account_identifier** | **str**|  | 
 **org_identifier** | **str**|  | 
 **project_identifier** | **str**|  | 
 **target_identifier** | **str**| Identifier of the target pipeline under which trigger resides | 
 **trigger_identifier** | **str**|  | 
 **if_match** | **str**|  | [optional] 
 **ignore_error** | **bool**|  | [optional] [default to false]

### Return type

[**ResponseDTONGTriggerResponse**](ResponseDTONGTriggerResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

