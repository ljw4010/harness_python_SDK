# harness_python_sdk.TasApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_tas_organizations**](TasApi.md#get_tas_organizations) | **GET** /ng/api/tas/organizations | Return the Tas organizations
[**get_tas_spaces**](TasApi.md#get_tas_spaces) | **GET** /ng/api/tas/space | Return the Tas spaces
[**get_tas_spaces_v2**](TasApi.md#get_tas_spaces_v2) | **GET** /ng/api/tas/v2/space | Return the Tas spaces

# **get_tas_organizations**
> ResponseDTOListString get_tas_organizations(account_identifier, connector_ref=connector_ref, org_identifier=org_identifier, project_identifier=project_identifier, env_id=env_id, infra_definition_id=infra_definition_id)

Return the Tas organizations

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
api_instance = harness_python_sdk.TasApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | 
connector_ref = 'connector_ref_example' # str | Identifier for tas connector (optional)
org_identifier = 'org_identifier_example' # str |  (optional)
project_identifier = 'project_identifier_example' # str |  (optional)
env_id = 'env_id_example' # str | Environment Identifier for the Entity. (optional)
infra_definition_id = 'infra_definition_id_example' # str | Infrastructure Definition Identifier for the Entity. (optional)

try:
    # Return the Tas organizations
    api_response = api_instance.get_tas_organizations(account_identifier, connector_ref=connector_ref, org_identifier=org_identifier, project_identifier=project_identifier, env_id=env_id, infra_definition_id=infra_definition_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasApi->get_tas_organizations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**|  | 
 **connector_ref** | **str**| Identifier for tas connector | [optional] 
 **org_identifier** | **str**|  | [optional] 
 **project_identifier** | **str**|  | [optional] 
 **env_id** | **str**| Environment Identifier for the Entity. | [optional] 
 **infra_definition_id** | **str**| Infrastructure Definition Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOListString**](ResponseDTOListString.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tas_spaces**
> ResponseDTOListString get_tas_spaces(connector_ref, organization, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Return the Tas spaces

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
api_instance = harness_python_sdk.TasApi(harness_python_sdk.ApiClient(configuration))
connector_ref = 'connector_ref_example' # str | Identifier for tas connector
organization = 'organization_example' # str | organization for tas
account_identifier = 'account_identifier_example' # str | 
org_identifier = 'org_identifier_example' # str |  (optional)
project_identifier = 'project_identifier_example' # str |  (optional)

try:
    # Return the Tas spaces
    api_response = api_instance.get_tas_spaces(connector_ref, organization, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasApi->get_tas_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_ref** | **str**| Identifier for tas connector | 
 **organization** | **str**| organization for tas | 
 **account_identifier** | **str**|  | 
 **org_identifier** | **str**|  | [optional] 
 **project_identifier** | **str**|  | [optional] 

### Return type

[**ResponseDTOListString**](ResponseDTOListString.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tas_spaces_v2**
> ResponseDTOListString get_tas_spaces_v2(account_identifier, env_id, infra_definition_id, org_identifier=org_identifier, project_identifier=project_identifier, organization=organization)

Return the Tas spaces

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
api_instance = harness_python_sdk.TasApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | 
env_id = 'env_id_example' # str | Environment Identifier for the Entity.
infra_definition_id = 'infra_definition_id_example' # str | Infrastructure Definition Identifier for the Entity.
org_identifier = 'org_identifier_example' # str |  (optional)
project_identifier = 'project_identifier_example' # str |  (optional)
organization = 'organization_example' # str |  (optional)

try:
    # Return the Tas spaces
    api_response = api_instance.get_tas_spaces_v2(account_identifier, env_id, infra_definition_id, org_identifier=org_identifier, project_identifier=project_identifier, organization=organization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasApi->get_tas_spaces_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**|  | 
 **env_id** | **str**| Environment Identifier for the Entity. | 
 **infra_definition_id** | **str**| Infrastructure Definition Identifier for the Entity. | 
 **org_identifier** | **str**|  | [optional] 
 **project_identifier** | **str**|  | [optional] 
 **organization** | **str**|  | [optional] 

### Return type

[**ResponseDTOListString**](ResponseDTOListString.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

