# swagger_client.ServicesApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_service_v2**](ServicesApi.md#create_service_v2) | **POST** /ng/api/servicesV2 | Create a Service
[**create_services_v2**](ServicesApi.md#create_services_v2) | **POST** /ng/api/servicesV2/batch | Create Services
[**delete_service_v2**](ServicesApi.md#delete_service_v2) | **DELETE** /ng/api/servicesV2/{serviceIdentifier} | Delete a Service by identifier
[**get_service_access_list**](ServicesApi.md#get_service_access_list) | **GET** /ng/api/servicesV2/list/access | Gets Service Access list
[**get_service_list**](ServicesApi.md#get_service_list) | **GET** /ng/api/servicesV2 | Gets Service list
[**get_service_v2**](ServicesApi.md#get_service_v2) | **GET** /ng/api/servicesV2/{serviceIdentifier} | Gets a Service by identifier
[**hook_actions**](ServicesApi.md#hook_actions) | **GET** /ng/api/servicesV2/hooks/actions | Retrieving the list of actions available for service hooks
[**k8s_cmd_flags**](ServicesApi.md#k8s_cmd_flags) | **GET** /ng/api/servicesV2/k8s/command-flags | Retrieving the list of Kubernetes Command Options
[**kustomize_cmd_flags**](ServicesApi.md#kustomize_cmd_flags) | **GET** /ng/api/servicesV2/kustomize/command-flags | Retrieving the list of Kustomize Command Flags
[**update_service_v2**](ServicesApi.md#update_service_v2) | **PUT** /ng/api/servicesV2 | Update a Service by identifier
[**upsert_service_v2**](ServicesApi.md#upsert_service_v2) | **PUT** /ng/api/servicesV2/upsert | Upsert a Service by identifier

# **create_service_v2**
> ResponseDTOServiceResponse create_service_v2(body, account_identifier)

Create a Service

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
api_instance = swagger_client.ServicesApi(swagger_client.ApiClient(configuration))
body = swagger_client.ServiceRequest1() # ServiceRequest1 | Details of the Service to be created
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Create a Service
    api_response = api_instance.create_service_v2(body, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServicesApi->create_service_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ServiceRequest1**](ServiceRequest1.md)| Details of the Service to be created | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**ResponseDTOServiceResponse**](ResponseDTOServiceResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_services_v2**
> ResponseDTOPageResponseServiceResponse create_services_v2(account_identifier, body=body)

Create Services

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
api_instance = swagger_client.ServicesApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
body = [swagger_client.ServiceRequest1()] # list[ServiceRequest1] | Details of the Services to be created, maximum 1000 services can be created. (optional)

try:
    # Create Services
    api_response = api_instance.create_services_v2(account_identifier, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServicesApi->create_services_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **body** | [**list[ServiceRequest1]**](ServiceRequest1.md)| Details of the Services to be created, maximum 1000 services can be created. | [optional] 

### Return type

[**ResponseDTOPageResponseServiceResponse**](ResponseDTOPageResponseServiceResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_service_v2**
> ResponseDTOBoolean delete_service_v2(service_identifier, account_identifier, if_match=if_match, org_identifier=org_identifier, project_identifier=project_identifier, force_delete=force_delete)

Delete a Service by identifier

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
api_instance = swagger_client.ServicesApi(swagger_client.ApiClient(configuration))
service_identifier = 'service_identifier_example' # str | Service Identifier for the entity
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
if_match = 'if_match_example' # str |  (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
force_delete = false # bool | If true, the Entity will be forced delete, without checking any references/usages (optional) (default to false)

try:
    # Delete a Service by identifier
    api_response = api_instance.delete_service_v2(service_identifier, account_identifier, if_match=if_match, org_identifier=org_identifier, project_identifier=project_identifier, force_delete=force_delete)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServicesApi->delete_service_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_identifier** | **str**| Service Identifier for the entity | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **if_match** | **str**|  | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **force_delete** | **bool**| If true, the Entity will be forced delete, without checking any references/usages | [optional] [default to false]

### Return type

[**ResponseDTOBoolean**](ResponseDTOBoolean.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_access_list**
> ResponseDTOListServiceResponse get_service_access_list(account_identifier, page=page, size=size, org_identifier=org_identifier, project_identifier=project_identifier, search_term=search_term, service_identifiers=service_identifiers, sort=sort, type=type, git_ops_enabled=git_ops_enabled, deployment_template_identifier=deployment_template_identifier, version_label=version_label, deployment_metadata_yaml=deployment_metadata_yaml, include_all_services_accessible_at_scope=include_all_services_accessible_at_scope)

Gets Service Access list

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
api_instance = swagger_client.ServicesApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
page = 0 # int | Page Index of the results to fetch.Default Value: 0 (optional) (default to 0)
size = 100 # int | Results per page (optional) (default to 100)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
search_term = 'search_term_example' # str | The word to be searched and included in the list response (optional)
service_identifiers = ['service_identifiers_example'] # list[str] | List of ServicesIds (optional)
sort = ['sort_example'] # list[str] | Specifies the sorting criteria of the list. Like sorting based on the last updated entity, alphabetical sorting in an ascending or descending order (optional)
type = 'type_example' # str |  (optional)
git_ops_enabled = true # bool |  (optional)
deployment_template_identifier = 'deployment_template_identifier_example' # str | The Identifier of deployment template if infrastructure is of type custom deployment (optional)
version_label = 'version_label_example' # str | The version label of deployment template if infrastructure is of type custom deployment (optional)
deployment_metadata_yaml = 'deployment_metadata_yaml_example' # str |  (optional)
include_all_services_accessible_at_scope = false # bool | Specify true if all accessible Services are to be included (optional) (default to false)

try:
    # Gets Service Access list
    api_response = api_instance.get_service_access_list(account_identifier, page=page, size=size, org_identifier=org_identifier, project_identifier=project_identifier, search_term=search_term, service_identifiers=service_identifiers, sort=sort, type=type, git_ops_enabled=git_ops_enabled, deployment_template_identifier=deployment_template_identifier, version_label=version_label, deployment_metadata_yaml=deployment_metadata_yaml, include_all_services_accessible_at_scope=include_all_services_accessible_at_scope)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServicesApi->get_service_access_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **page** | **int**| Page Index of the results to fetch.Default Value: 0 | [optional] [default to 0]
 **size** | **int**| Results per page | [optional] [default to 100]
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **search_term** | **str**| The word to be searched and included in the list response | [optional] 
 **service_identifiers** | [**list[str]**](str.md)| List of ServicesIds | [optional] 
 **sort** | [**list[str]**](str.md)| Specifies the sorting criteria of the list. Like sorting based on the last updated entity, alphabetical sorting in an ascending or descending order | [optional] 
 **type** | **str**|  | [optional] 
 **git_ops_enabled** | **bool**|  | [optional] 
 **deployment_template_identifier** | **str**| The Identifier of deployment template if infrastructure is of type custom deployment | [optional] 
 **version_label** | **str**| The version label of deployment template if infrastructure is of type custom deployment | [optional] 
 **deployment_metadata_yaml** | **str**|  | [optional] 
 **include_all_services_accessible_at_scope** | **bool**| Specify true if all accessible Services are to be included | [optional] [default to false]

### Return type

[**ResponseDTOListServiceResponse**](ResponseDTOListServiceResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_list**
> ResponseDTOPageResponseServiceResponse get_service_list(account_identifier, page=page, size=size, org_identifier=org_identifier, project_identifier=project_identifier, search_term=search_term, service_identifiers=service_identifiers, sort=sort, type=type, git_ops_enabled=git_ops_enabled, deployment_template_identifier=deployment_template_identifier, version_label=version_label, include_all_services_accessible_at_scope=include_all_services_accessible_at_scope)

Gets Service list

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
api_instance = swagger_client.ServicesApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
page = 0 # int | Page Index of the results to fetch.Default Value: 0 (optional) (default to 0)
size = 100 # int | Results per page (optional) (default to 100)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
search_term = 'search_term_example' # str | The word to be searched and included in the list response (optional)
service_identifiers = ['service_identifiers_example'] # list[str] | List of ServicesIds (optional)
sort = ['sort_example'] # list[str] | Specifies the sorting criteria of the list. Like sorting based on the last updated entity, alphabetical sorting in an ascending or descending order (optional)
type = 'type_example' # str |  (optional)
git_ops_enabled = true # bool |  (optional)
deployment_template_identifier = 'deployment_template_identifier_example' # str | The Identifier of deployment template if infrastructure is of type custom deployment (optional)
version_label = 'version_label_example' # str | The version label of deployment template if infrastructure is of type custom deployment (optional)
include_all_services_accessible_at_scope = false # bool | Specify true if all accessible Services are to be included (optional) (default to false)

try:
    # Gets Service list
    api_response = api_instance.get_service_list(account_identifier, page=page, size=size, org_identifier=org_identifier, project_identifier=project_identifier, search_term=search_term, service_identifiers=service_identifiers, sort=sort, type=type, git_ops_enabled=git_ops_enabled, deployment_template_identifier=deployment_template_identifier, version_label=version_label, include_all_services_accessible_at_scope=include_all_services_accessible_at_scope)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServicesApi->get_service_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **page** | **int**| Page Index of the results to fetch.Default Value: 0 | [optional] [default to 0]
 **size** | **int**| Results per page | [optional] [default to 100]
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **search_term** | **str**| The word to be searched and included in the list response | [optional] 
 **service_identifiers** | [**list[str]**](str.md)| List of ServicesIds | [optional] 
 **sort** | [**list[str]**](str.md)| Specifies the sorting criteria of the list. Like sorting based on the last updated entity, alphabetical sorting in an ascending or descending order | [optional] 
 **type** | **str**|  | [optional] 
 **git_ops_enabled** | **bool**|  | [optional] 
 **deployment_template_identifier** | **str**| The Identifier of deployment template if infrastructure is of type custom deployment | [optional] 
 **version_label** | **str**| The version label of deployment template if infrastructure is of type custom deployment | [optional] 
 **include_all_services_accessible_at_scope** | **bool**| Specify true if all accessible Services are to be included | [optional] [default to false]

### Return type

[**ResponseDTOPageResponseServiceResponse**](ResponseDTOPageResponseServiceResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_v2**
> ResponseDTOServiceResponse get_service_v2(service_identifier, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, deleted=deleted)

Gets a Service by identifier

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
api_instance = swagger_client.ServicesApi(swagger_client.ApiClient(configuration))
service_identifier = 'service_identifier_example' # str | Service Identifier for the entity
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
deleted = false # bool | Specify whether Service is deleted or not (optional) (default to false)

try:
    # Gets a Service by identifier
    api_response = api_instance.get_service_v2(service_identifier, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, deleted=deleted)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServicesApi->get_service_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_identifier** | **str**| Service Identifier for the entity | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **deleted** | **bool**| Specify whether Service is deleted or not | [optional] [default to false]

### Return type

[**ResponseDTOServiceResponse**](ResponseDTOServiceResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hook_actions**
> ResponseDTOSetServiceHookAction hook_actions(service_spec_type)

Retrieving the list of actions available for service hooks

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
api_instance = swagger_client.ServicesApi(swagger_client.ApiClient(configuration))
service_spec_type = 'service_spec_type_example' # str | 

try:
    # Retrieving the list of actions available for service hooks
    api_response = api_instance.hook_actions(service_spec_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServicesApi->hook_actions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_spec_type** | **str**|  | 

### Return type

[**ResponseDTOSetServiceHookAction**](ResponseDTOSetServiceHookAction.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **k8s_cmd_flags**
> ResponseDTOSetK8sCommandFlagType k8s_cmd_flags(service_spec_type)

Retrieving the list of Kubernetes Command Options

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
api_instance = swagger_client.ServicesApi(swagger_client.ApiClient(configuration))
service_spec_type = 'service_spec_type_example' # str | 

try:
    # Retrieving the list of Kubernetes Command Options
    api_response = api_instance.k8s_cmd_flags(service_spec_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServicesApi->k8s_cmd_flags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_spec_type** | **str**|  | 

### Return type

[**ResponseDTOSetK8sCommandFlagType**](ResponseDTOSetK8sCommandFlagType.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kustomize_cmd_flags**
> ResponseDTOSetKustomizeCommandFlagType kustomize_cmd_flags()

Retrieving the list of Kustomize Command Flags

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
api_instance = swagger_client.ServicesApi(swagger_client.ApiClient(configuration))

try:
    # Retrieving the list of Kustomize Command Flags
    api_response = api_instance.kustomize_cmd_flags()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServicesApi->kustomize_cmd_flags: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResponseDTOSetKustomizeCommandFlagType**](ResponseDTOSetKustomizeCommandFlagType.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_service_v2**
> ResponseDTOServiceResponse update_service_v2(body, account_identifier, if_match=if_match)

Update a Service by identifier

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
api_instance = swagger_client.ServicesApi(swagger_client.ApiClient(configuration))
body = swagger_client.ServiceRequest1() # ServiceRequest1 | Details of the Service to be updated
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
if_match = 'if_match_example' # str |  (optional)

try:
    # Update a Service by identifier
    api_response = api_instance.update_service_v2(body, account_identifier, if_match=if_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServicesApi->update_service_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ServiceRequest1**](ServiceRequest1.md)| Details of the Service to be updated | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **if_match** | **str**|  | [optional] 

### Return type

[**ResponseDTOServiceResponse**](ResponseDTOServiceResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_service_v2**
> ResponseDTOServiceResponse upsert_service_v2(body, account_identifier, if_match=if_match)

Upsert a Service by identifier

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
api_instance = swagger_client.ServicesApi(swagger_client.ApiClient(configuration))
body = swagger_client.ServiceRequest1() # ServiceRequest1 | Details of the Service to be upserted
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
if_match = 'if_match_example' # str |  (optional)

try:
    # Upsert a Service by identifier
    api_response = api_instance.upsert_service_v2(body, account_identifier, if_match=if_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServicesApi->upsert_service_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ServiceRequest1**](ServiceRequest1.md)| Details of the Service to be upserted | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **if_match** | **str**|  | [optional] 

### Return type

[**ResponseDTOServiceResponse**](ResponseDTOServiceResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

