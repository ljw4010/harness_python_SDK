# harness_python_sdk.InfrastructuresApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_infrastructure**](InfrastructuresApi.md#create_infrastructure) | **POST** /ng/api/infrastructures | Create an Infrastructure in an Environment
[**delete_infrastructure**](InfrastructuresApi.md#delete_infrastructure) | **DELETE** /ng/api/infrastructures/{infraIdentifier} | Delete an Infrastructure by identifier
[**get_infrastructure**](InfrastructuresApi.md#get_infrastructure) | **GET** /ng/api/infrastructures/{infraIdentifier} | Gets an Infrastructure by identifier
[**get_infrastructure_list**](InfrastructuresApi.md#get_infrastructure_list) | **GET** /ng/api/infrastructures | Gets Infrastructure list
[**update_infrastructure**](InfrastructuresApi.md#update_infrastructure) | **PUT** /ng/api/infrastructures | Update an Infrastructure by identifier

# **create_infrastructure**
> ResponseDTOInfrastructureResponse create_infrastructure(body, account_identifier)

Create an Infrastructure in an Environment

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
api_instance = harness_python_sdk.InfrastructuresApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.InfrastructureRequest() # InfrastructureRequest | Details of the Infrastructure to be created
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Create an Infrastructure in an Environment
    api_response = api_instance.create_infrastructure(body, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfrastructuresApi->create_infrastructure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InfrastructureRequest**](InfrastructureRequest.md)| Details of the Infrastructure to be created | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**ResponseDTOInfrastructureResponse**](ResponseDTOInfrastructureResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_infrastructure**
> ResponseDTOBoolean delete_infrastructure(infra_identifier, account_identifier, environment_identifier, org_identifier=org_identifier, project_identifier=project_identifier, force_delete=force_delete)

Delete an Infrastructure by identifier

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
api_instance = harness_python_sdk.InfrastructuresApi(harness_python_sdk.ApiClient(configuration))
infra_identifier = 'infra_identifier_example' # str | Infrastructure Identifier for the entity
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
environment_identifier = 'environment_identifier_example' # str | Environment Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
force_delete = false # bool | If true, the Entity will be forced delete, without checking any references/usages (optional) (default to false)

try:
    # Delete an Infrastructure by identifier
    api_response = api_instance.delete_infrastructure(infra_identifier, account_identifier, environment_identifier, org_identifier=org_identifier, project_identifier=project_identifier, force_delete=force_delete)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfrastructuresApi->delete_infrastructure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **infra_identifier** | **str**| Infrastructure Identifier for the entity | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **environment_identifier** | **str**| Environment Identifier for the Entity. | 
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

# **get_infrastructure**
> ResponseDTOInfrastructureResponse get_infrastructure(infra_identifier, account_identifier, environment_identifier, org_identifier=org_identifier, project_identifier=project_identifier, deleted=deleted)

Gets an Infrastructure by identifier

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
api_instance = harness_python_sdk.InfrastructuresApi(harness_python_sdk.ApiClient(configuration))
infra_identifier = 'infra_identifier_example' # str | Infrastructure Identifier for the entity
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
environment_identifier = 'environment_identifier_example' # str | envId
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
deleted = false # bool | Specify whether Infrastructure is deleted or not (optional) (default to false)

try:
    # Gets an Infrastructure by identifier
    api_response = api_instance.get_infrastructure(infra_identifier, account_identifier, environment_identifier, org_identifier=org_identifier, project_identifier=project_identifier, deleted=deleted)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfrastructuresApi->get_infrastructure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **infra_identifier** | **str**| Infrastructure Identifier for the entity | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **environment_identifier** | **str**| envId | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **deleted** | **bool**| Specify whether Infrastructure is deleted or not | [optional] [default to false]

### Return type

[**ResponseDTOInfrastructureResponse**](ResponseDTOInfrastructureResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_infrastructure_list**
> ResponseDTOPageResponseInfrastructureResponse get_infrastructure_list(account_identifier, environment_identifier, page=page, size=size, org_identifier=org_identifier, project_identifier=project_identifier, search_term=search_term, infra_identifiers=infra_identifiers, deployment_type=deployment_type, deployment_template_identifier=deployment_template_identifier, version_label=version_label, sort=sort, service_refs=service_refs)

Gets Infrastructure list

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
api_instance = harness_python_sdk.InfrastructuresApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
environment_identifier = 'environment_identifier_example' # str | Environment Identifier for the Entity.
page = 0 # int | Page Index of the results to fetch.Default Value: 0 (optional) (default to 0)
size = 100 # int | Results per page (optional) (default to 100)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
search_term = 'search_term_example' # str | The word to be searched and included in the list response (optional)
infra_identifiers = ['infra_identifiers_example'] # list[str] | List of InfrastructureIds (optional)
deployment_type = 'deployment_type_example' # str |  (optional)
deployment_template_identifier = 'deployment_template_identifier_example' # str | The Identifier of deployment template if infrastructure is of type custom deployment (optional)
version_label = 'version_label_example' # str | The version label of deployment template if infrastructure is of type custom deployment (optional)
sort = ['sort_example'] # list[str] | Specifies the sorting criteria of the list. Like sorting based on the last updated entity, alphabetical sorting in an ascending or descending order (optional)
service_refs = ['service_refs_example'] # list[str] | list of service refs required to fetch infrastructures scoped to these service refs (optional)

try:
    # Gets Infrastructure list
    api_response = api_instance.get_infrastructure_list(account_identifier, environment_identifier, page=page, size=size, org_identifier=org_identifier, project_identifier=project_identifier, search_term=search_term, infra_identifiers=infra_identifiers, deployment_type=deployment_type, deployment_template_identifier=deployment_template_identifier, version_label=version_label, sort=sort, service_refs=service_refs)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfrastructuresApi->get_infrastructure_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **environment_identifier** | **str**| Environment Identifier for the Entity. | 
 **page** | **int**| Page Index of the results to fetch.Default Value: 0 | [optional] [default to 0]
 **size** | **int**| Results per page | [optional] [default to 100]
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **search_term** | **str**| The word to be searched and included in the list response | [optional] 
 **infra_identifiers** | [**list[str]**](str.md)| List of InfrastructureIds | [optional] 
 **deployment_type** | **str**|  | [optional] 
 **deployment_template_identifier** | **str**| The Identifier of deployment template if infrastructure is of type custom deployment | [optional] 
 **version_label** | **str**| The version label of deployment template if infrastructure is of type custom deployment | [optional] 
 **sort** | [**list[str]**](str.md)| Specifies the sorting criteria of the list. Like sorting based on the last updated entity, alphabetical sorting in an ascending or descending order | [optional] 
 **service_refs** | [**list[str]**](str.md)| list of service refs required to fetch infrastructures scoped to these service refs | [optional] 

### Return type

[**ResponseDTOPageResponseInfrastructureResponse**](ResponseDTOPageResponseInfrastructureResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_infrastructure**
> ResponseDTOInfrastructureResponse update_infrastructure(body, account_identifier)

Update an Infrastructure by identifier

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
api_instance = harness_python_sdk.InfrastructuresApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.InfrastructureRequest() # InfrastructureRequest | Details of the Infrastructure to be updated
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Update an Infrastructure by identifier
    api_response = api_instance.update_infrastructure(body, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfrastructuresApi->update_infrastructure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InfrastructureRequest**](InfrastructureRequest.md)| Details of the Infrastructure to be updated | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**ResponseDTOInfrastructureResponse**](ResponseDTOInfrastructureResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

