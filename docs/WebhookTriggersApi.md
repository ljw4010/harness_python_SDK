# harness_python_sdk.WebhookTriggersApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_webhook_details**](WebhookTriggersApi.md#fetch_webhook_details) | **GET** /pipeline/api/webhook/triggerProcessingDetails | Gets webhook event processing details for input eventId.
[**fetch_webhook_execution_details**](WebhookTriggersApi.md#fetch_webhook_execution_details) | **GET** /pipeline/api/webhook/triggerExecutionDetails/{eventId} | Gets webhook event processing details for input eventId.
[**pipelineprocess_webhook_event**](WebhookTriggersApi.md#pipelineprocess_webhook_event) | **POST** /pipeline/api/webhook/trigger | Handles event payload for webhook triggers.
[**process_custom_webhook_event**](WebhookTriggersApi.md#process_custom_webhook_event) | **POST** /pipeline/api/webhook/custom | Handles event payload for custom webhook triggers.
[**process_custom_webhook_event_v2**](WebhookTriggersApi.md#process_custom_webhook_event_v2) | **POST** /pipeline/api/webhook/custom/v2 | Handles event payload for custom webhook triggers.
[**process_custom_webhook_event_v3**](WebhookTriggersApi.md#process_custom_webhook_event_v3) | **POST** /pipeline/api/webhook/custom/{webhookToken}/v3 | Handles event payload for custom webhook triggers.

# **fetch_webhook_details**
> ResponseDTOWebhookEventProcessingDetails fetch_webhook_details(account_identifier, event_id)

Gets webhook event processing details for input eventId.

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
api_instance = harness_python_sdk.WebhookTriggersApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | 
event_id = 'event_id_example' # str | 

try:
    # Gets webhook event processing details for input eventId.
    api_response = api_instance.fetch_webhook_details(account_identifier, event_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookTriggersApi->fetch_webhook_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**|  | 
 **event_id** | **str**|  | 

### Return type

[**ResponseDTOWebhookEventProcessingDetails**](ResponseDTOWebhookEventProcessingDetails.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_webhook_execution_details**
> ResponseDTOWebhookExecutionDetails fetch_webhook_execution_details(event_id, account_identifier)

Gets webhook event processing details for input eventId.

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
api_instance = harness_python_sdk.WebhookTriggersApi(harness_python_sdk.ApiClient(configuration))
event_id = 'event_id_example' # str | 
account_identifier = 'account_identifier_example' # str | 

try:
    # Gets webhook event processing details for input eventId.
    api_response = api_instance.fetch_webhook_execution_details(event_id, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookTriggersApi->fetch_webhook_execution_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **str**|  | 
 **account_identifier** | **str**|  | 

### Return type

[**ResponseDTOWebhookExecutionDetails**](ResponseDTOWebhookExecutionDetails.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipelineprocess_webhook_event**
> ResponseDTOString pipelineprocess_webhook_event(body, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Handles event payload for webhook triggers.

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
api_instance = harness_python_sdk.WebhookTriggersApi(harness_python_sdk.ApiClient(configuration))
body = 'body_example' # str | 
account_identifier = 'account_identifier_example' # str | 
org_identifier = 'org_identifier_example' # str |  (optional)
project_identifier = 'project_identifier_example' # str |  (optional)

try:
    # Handles event payload for webhook triggers.
    api_response = api_instance.pipelineprocess_webhook_event(body, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookTriggersApi->pipelineprocess_webhook_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)|  | 
 **account_identifier** | **str**|  | 
 **org_identifier** | **str**|  | [optional] 
 **project_identifier** | **str**|  | [optional] 

### Return type

[**ResponseDTOString**](ResponseDTOString.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml, text/plain
 - **Accept**: application/json, application/yaml, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_custom_webhook_event**
> ResponseDTOString process_custom_webhook_event(body, account_identifier, org_identifier, project_identifier, pipeline_identifier=pipeline_identifier, trigger_identifier=trigger_identifier)

Handles event payload for custom webhook triggers.

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
api_instance = harness_python_sdk.WebhookTriggersApi(harness_python_sdk.ApiClient(configuration))
body = 'body_example' # str | 
account_identifier = 'account_identifier_example' # str | 
org_identifier = 'org_identifier_example' # str | 
project_identifier = 'project_identifier_example' # str | 
pipeline_identifier = 'pipeline_identifier_example' # str |  (optional)
trigger_identifier = 'trigger_identifier_example' # str |  (optional)

try:
    # Handles event payload for custom webhook triggers.
    api_response = api_instance.process_custom_webhook_event(body, account_identifier, org_identifier, project_identifier, pipeline_identifier=pipeline_identifier, trigger_identifier=trigger_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookTriggersApi->process_custom_webhook_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)|  | 
 **account_identifier** | **str**|  | 
 **org_identifier** | **str**|  | 
 **project_identifier** | **str**|  | 
 **pipeline_identifier** | **str**|  | [optional] 
 **trigger_identifier** | **str**|  | [optional] 

### Return type

[**ResponseDTOString**](ResponseDTOString.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml, text/plain
 - **Accept**: application/json, application/yaml, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_custom_webhook_event_v2**
> ResponseDTONGProcessWebhookResponse process_custom_webhook_event_v2(body, account_identifier, org_identifier, project_identifier, pipeline_identifier=pipeline_identifier, trigger_identifier=trigger_identifier)

Handles event payload for custom webhook triggers.

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
api_instance = harness_python_sdk.WebhookTriggersApi(harness_python_sdk.ApiClient(configuration))
body = 'body_example' # str | Trigger Payload
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
pipeline_identifier = 'pipeline_identifier_example' # str | Pipeline Identifier (optional)
trigger_identifier = 'trigger_identifier_example' # str | Trigger Key (optional)

try:
    # Handles event payload for custom webhook triggers.
    api_response = api_instance.process_custom_webhook_event_v2(body, account_identifier, org_identifier, project_identifier, pipeline_identifier=pipeline_identifier, trigger_identifier=trigger_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookTriggersApi->process_custom_webhook_event_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| Trigger Payload | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **pipeline_identifier** | **str**| Pipeline Identifier | [optional] 
 **trigger_identifier** | **str**| Trigger Key | [optional] 

### Return type

[**ResponseDTONGProcessWebhookResponse**](ResponseDTONGProcessWebhookResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml, text/plain
 - **Accept**: application/json, application/yaml, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_custom_webhook_event_v3**
> ResponseDTONGProcessWebhookResponse process_custom_webhook_event_v3(body, account_identifier, org_identifier, project_identifier, webhook_token, pipeline_identifier=pipeline_identifier, trigger_identifier=trigger_identifier)

Handles event payload for custom webhook triggers.

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
api_instance = harness_python_sdk.WebhookTriggersApi(harness_python_sdk.ApiClient(configuration))
body = 'body_example' # str | Trigger Payload
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity.
webhook_token = 'webhook_token_example' # str | Custom Webhook token for custom webhook triggers
pipeline_identifier = 'pipeline_identifier_example' # str | Pipeline Identifier (optional)
trigger_identifier = 'trigger_identifier_example' # str | Trigger Key (optional)

try:
    # Handles event payload for custom webhook triggers.
    api_response = api_instance.process_custom_webhook_event_v3(body, account_identifier, org_identifier, project_identifier, webhook_token, pipeline_identifier=pipeline_identifier, trigger_identifier=trigger_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookTriggersApi->process_custom_webhook_event_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| Trigger Payload | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | 
 **webhook_token** | **str**| Custom Webhook token for custom webhook triggers | 
 **pipeline_identifier** | **str**| Pipeline Identifier | [optional] 
 **trigger_identifier** | **str**| Trigger Key | [optional] 

### Return type

[**ResponseDTONGProcessWebhookResponse**](ResponseDTONGProcessWebhookResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml, text/plain
 - **Accept**: application/json, application/yaml, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

