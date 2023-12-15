# harness_python_sdk.AgentsApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**agent_service_for_server_create**](AgentsApi.md#agent_service_for_server_create) | **POST** /gitops/api/v1/agents | 
[**agent_service_for_server_delete**](AgentsApi.md#agent_service_for_server_delete) | **DELETE** /gitops/api/v1/agents/{identifier} | 
[**agent_service_for_server_get**](AgentsApi.md#agent_service_for_server_get) | **GET** /gitops/api/v1/agents/{identifier} | 
[**agent_service_for_server_get_deploy_yaml**](AgentsApi.md#agent_service_for_server_get_deploy_yaml) | **GET** /gitops/api/v1/agents/{agentIdentifier}/deploy.yaml | 
[**agent_service_for_server_list**](AgentsApi.md#agent_service_for_server_list) | **GET** /gitops/api/v1/agents | 
[**agent_service_for_server_regenerate_credentials**](AgentsApi.md#agent_service_for_server_regenerate_credentials) | **POST** /gitops/api/v1/agents/{identifier}/credentials | 
[**agent_service_for_server_unique**](AgentsApi.md#agent_service_for_server_unique) | **GET** /gitops/api/v1/agents/{identifier}/unique | 
[**agent_service_for_server_update**](AgentsApi.md#agent_service_for_server_update) | **PUT** /gitops/api/v1/agents/{agent.identifier} | 

# **agent_service_for_server_create**
> V1Agent agent_service_for_server_create(body)



Create agent.

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
api_instance = harness_python_sdk.AgentsApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.V1Agent() # V1Agent | 

try:
    api_response = api_instance.agent_service_for_server_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentsApi->agent_service_for_server_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Agent**](V1Agent.md)|  | 

### Return type

[**V1Agent**](V1Agent.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_service_for_server_delete**
> V1Agent agent_service_for_server_delete(identifier, account_identifier=account_identifier, project_identifier=project_identifier, org_identifier=org_identifier, name=name, type=type, tags=tags, search_term=search_term, page_size=page_size, page_index=page_index, scope=scope)



Delete agents.

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
api_instance = harness_python_sdk.AgentsApi(harness_python_sdk.ApiClient(configuration))
identifier = 'identifier_example' # str | 
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
name = 'name_example' # str |  (optional)
type = 'AGENT_TYPE_UNSET' # str |  (optional) (default to AGENT_TYPE_UNSET)
tags = ['tags_example'] # list[str] |  (optional)
search_term = 'search_term_example' # str |  (optional)
page_size = 56 # int |  (optional)
page_index = 56 # int |  (optional)
scope = 'AGENT_SCOPE_UNSET' # str |  (optional) (default to AGENT_SCOPE_UNSET)

try:
    api_response = api_instance.agent_service_for_server_delete(identifier, account_identifier=account_identifier, project_identifier=project_identifier, org_identifier=org_identifier, name=name, type=type, tags=tags, search_term=search_term, page_size=page_size, page_index=page_index, scope=scope)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentsApi->agent_service_for_server_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**|  | 
 **account_identifier** | **str**| Account Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **name** | **str**|  | [optional] 
 **type** | **str**|  | [optional] [default to AGENT_TYPE_UNSET]
 **tags** | [**list[str]**](str.md)|  | [optional] 
 **search_term** | **str**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **page_index** | **int**|  | [optional] 
 **scope** | **str**|  | [optional] [default to AGENT_SCOPE_UNSET]

### Return type

[**V1Agent**](V1Agent.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_service_for_server_get**
> V1Agent agent_service_for_server_get(identifier, account_identifier, project_identifier=project_identifier, org_identifier=org_identifier, name=name, type=type, tags=tags, search_term=search_term, page_size=page_size, page_index=page_index, scope=scope)



Get agents.

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
api_instance = harness_python_sdk.AgentsApi(harness_python_sdk.ApiClient(configuration))
identifier = 'identifier_example' # str | 
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
name = 'name_example' # str |  (optional)
type = 'AGENT_TYPE_UNSET' # str |  (optional) (default to AGENT_TYPE_UNSET)
tags = ['tags_example'] # list[str] |  (optional)
search_term = 'search_term_example' # str |  (optional)
page_size = 56 # int |  (optional)
page_index = 56 # int |  (optional)
scope = 'AGENT_SCOPE_UNSET' # str |  (optional) (default to AGENT_SCOPE_UNSET)

try:
    api_response = api_instance.agent_service_for_server_get(identifier, account_identifier, project_identifier=project_identifier, org_identifier=org_identifier, name=name, type=type, tags=tags, search_term=search_term, page_size=page_size, page_index=page_index, scope=scope)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentsApi->agent_service_for_server_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**|  | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **name** | **str**|  | [optional] 
 **type** | **str**|  | [optional] [default to AGENT_TYPE_UNSET]
 **tags** | [**list[str]**](str.md)|  | [optional] 
 **search_term** | **str**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **page_index** | **int**|  | [optional] 
 **scope** | **str**|  | [optional] [default to AGENT_SCOPE_UNSET]

### Return type

[**V1Agent**](V1Agent.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_service_for_server_get_deploy_yaml**
> str agent_service_for_server_get_deploy_yaml(agent_identifier, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, namespace=namespace)



GetDeployYaml returns depoyment yamls for agents.

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
api_instance = harness_python_sdk.AgentsApi(harness_python_sdk.ApiClient(configuration))
agent_identifier = 'agent_identifier_example' # str | Agent identifier for entity.
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
namespace = 'namespace_example' # str |  (optional)

try:
    api_response = api_instance.agent_service_for_server_get_deploy_yaml(agent_identifier, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, namespace=namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentsApi->agent_service_for_server_get_deploy_yaml: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_identifier** | **str**| Agent identifier for entity. | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **namespace** | **str**|  | [optional] 

### Return type

**str**

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/x-yml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_service_for_server_list**
> V1AgentList agent_service_for_server_list(account_identifier, type, project_identifier=project_identifier, org_identifier=org_identifier, identifier=identifier, name=name, tags=tags, search_term=search_term, page_size=page_size, page_index=page_index, scope=scope)



List agents.

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
api_instance = harness_python_sdk.AgentsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
type = 'AGENT_TYPE_UNSET' # str | MANAGED_ARGO_PROVIDER (default to AGENT_TYPE_UNSET)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
identifier = 'identifier_example' # str |  (optional)
name = 'name_example' # str |  (optional)
tags = ['tags_example'] # list[str] |  (optional)
search_term = 'search_term_example' # str |  (optional)
page_size = 56 # int |  (optional)
page_index = 56 # int |  (optional)
scope = 'AGENT_SCOPE_UNSET' # str |  (optional) (default to AGENT_SCOPE_UNSET)

try:
    api_response = api_instance.agent_service_for_server_list(account_identifier, type, project_identifier=project_identifier, org_identifier=org_identifier, identifier=identifier, name=name, tags=tags, search_term=search_term, page_size=page_size, page_index=page_index, scope=scope)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentsApi->agent_service_for_server_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **type** | **str**| MANAGED_ARGO_PROVIDER | [default to AGENT_TYPE_UNSET]
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **identifier** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **tags** | [**list[str]**](str.md)|  | [optional] 
 **search_term** | **str**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **page_index** | **int**|  | [optional] 
 **scope** | **str**|  | [optional] [default to AGENT_SCOPE_UNSET]

### Return type

[**V1AgentList**](V1AgentList.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_service_for_server_regenerate_credentials**
> V1Agent agent_service_for_server_regenerate_credentials(identifier, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)



Regenerate credentials for agents.

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
api_instance = harness_python_sdk.AgentsApi(harness_python_sdk.ApiClient(configuration))
identifier = 'identifier_example' # str | 
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    api_response = api_instance.agent_service_for_server_regenerate_credentials(identifier, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentsApi->agent_service_for_server_regenerate_credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**|  | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**V1Agent**](V1Agent.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_service_for_server_unique**
> V1UniqueMessage agent_service_for_server_unique(identifier, account_identifier, project_identifier=project_identifier, org_identifier=org_identifier, name=name, type=type, tags=tags, search_term=search_term, page_size=page_size, page_index=page_index, scope=scope)



Unique returns unique agents.

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
api_instance = harness_python_sdk.AgentsApi(harness_python_sdk.ApiClient(configuration))
identifier = 'identifier_example' # str | 
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
name = 'name_example' # str |  (optional)
type = 'AGENT_TYPE_UNSET' # str |  (optional) (default to AGENT_TYPE_UNSET)
tags = ['tags_example'] # list[str] |  (optional)
search_term = 'search_term_example' # str |  (optional)
page_size = 56 # int |  (optional)
page_index = 56 # int |  (optional)
scope = 'AGENT_SCOPE_UNSET' # str |  (optional) (default to AGENT_SCOPE_UNSET)

try:
    api_response = api_instance.agent_service_for_server_unique(identifier, account_identifier, project_identifier=project_identifier, org_identifier=org_identifier, name=name, type=type, tags=tags, search_term=search_term, page_size=page_size, page_index=page_index, scope=scope)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentsApi->agent_service_for_server_unique: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**|  | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **name** | **str**|  | [optional] 
 **type** | **str**|  | [optional] [default to AGENT_TYPE_UNSET]
 **tags** | [**list[str]**](str.md)|  | [optional] 
 **search_term** | **str**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **page_index** | **int**|  | [optional] 
 **scope** | **str**|  | [optional] [default to AGENT_SCOPE_UNSET]

### Return type

[**V1UniqueMessage**](V1UniqueMessage.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_service_for_server_update**
> V1Agent agent_service_for_server_update(body, agent_identifier)



Update agents.

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
api_instance = harness_python_sdk.AgentsApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.V1Agent() # V1Agent | 
agent_identifier = 'agent_identifier_example' # str | The gitops-server generated ID for this gitops-agent

try:
    api_response = api_instance.agent_service_for_server_update(body, agent_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentsApi->agent_service_for_server_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Agent**](V1Agent.md)|  | 
 **agent_identifier** | **str**| The gitops-server generated ID for this gitops-agent | 

### Return type

[**V1Agent**](V1Agent.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

