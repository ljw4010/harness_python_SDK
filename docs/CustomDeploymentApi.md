# swagger_client.CustomDeploymentApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_custom_deployment_entity_references**](CustomDeploymentApi.md#get_custom_deployment_entity_references) | **POST** /ng/api/customDeployment/get-references | Gets Custom Deployment Entity References
[**get_custom_deployment_expression_variables**](CustomDeploymentApi.md#get_custom_deployment_expression_variables) | **POST** /ng/api/customDeployment/expression-variables | Gets Custom Deployment Expression Variables
[**get_custom_deployment_infra_variables**](CustomDeploymentApi.md#get_custom_deployment_infra_variables) | **GET** /ng/api/customDeployment/variables/{templateIdentifier} | Gets Infra Variables from a Custom Deployment Template by identifier
[**get_updated_yaml_for_infrastructure**](CustomDeploymentApi.md#get_updated_yaml_for_infrastructure) | **POST** /ng/api/customDeployment/get-updated-Yaml/{infraIdentifier} | Return the updated yaml for infrastructure based on Deployment template
[**validate_infrastructure_for_deployment_template**](CustomDeploymentApi.md#validate_infrastructure_for_deployment_template) | **GET** /ng/api/customDeployment/validate-infrastructure/{infraIdentifier} | This validates whether Infrastructure is valid or not

# **get_custom_deployment_entity_references**
> ResponseDTOListEntityDetailProtoDTO get_custom_deployment_entity_references(body, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Gets Custom Deployment Entity References

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
api_instance = swagger_client.CustomDeploymentApi(swagger_client.ApiClient(configuration))
body = swagger_client.CustomDeploymentYamlRequestDTO() # CustomDeploymentYamlRequestDTO | Custom Deployment Yaml Request DTO containing entityYaml
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Gets Custom Deployment Entity References
    api_response = api_instance.get_custom_deployment_entity_references(body, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomDeploymentApi->get_custom_deployment_entity_references: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CustomDeploymentYamlRequestDTO**](CustomDeploymentYamlRequestDTO.md)| Custom Deployment Yaml Request DTO containing entityYaml | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOListEntityDetailProtoDTO**](ResponseDTOListEntityDetailProtoDTO.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_deployment_expression_variables**
> ResponseDTOCustomDeploymentVariableResponseDTO get_custom_deployment_expression_variables(body)

Gets Custom Deployment Expression Variables

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
api_instance = swagger_client.CustomDeploymentApi(swagger_client.ApiClient(configuration))
body = swagger_client.CustomDeploymentYamlRequestDTO() # CustomDeploymentYamlRequestDTO | Custom Deployment Yaml Request DTO containing entityYaml

try:
    # Gets Custom Deployment Expression Variables
    api_response = api_instance.get_custom_deployment_expression_variables(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomDeploymentApi->get_custom_deployment_expression_variables: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CustomDeploymentYamlRequestDTO**](CustomDeploymentYamlRequestDTO.md)| Custom Deployment Yaml Request DTO containing entityYaml | 

### Return type

[**ResponseDTOCustomDeploymentVariableResponseDTO**](ResponseDTOCustomDeploymentVariableResponseDTO.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_deployment_infra_variables**
> ResponseDTOString get_custom_deployment_infra_variables(account_identifier, template_identifier, org_identifier=org_identifier, project_identifier=project_identifier, version_label=version_label, deleted=deleted)

Gets Infra Variables from a Custom Deployment Template by identifier

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
api_instance = swagger_client.CustomDeploymentApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
template_identifier = 'template_identifier_example' # str | Custom Deployment Identifier for the entity
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
version_label = 'version_label_example' # str | Version Label (optional)
deleted = false # bool | Specifies whether Template is deleted or not (optional) (default to false)

try:
    # Gets Infra Variables from a Custom Deployment Template by identifier
    api_response = api_instance.get_custom_deployment_infra_variables(account_identifier, template_identifier, org_identifier=org_identifier, project_identifier=project_identifier, version_label=version_label, deleted=deleted)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomDeploymentApi->get_custom_deployment_infra_variables: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **template_identifier** | **str**| Custom Deployment Identifier for the entity | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **version_label** | **str**| Version Label | [optional] 
 **deleted** | **bool**| Specifies whether Template is deleted or not | [optional] [default to false]

### Return type

[**ResponseDTOString**](ResponseDTOString.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_updated_yaml_for_infrastructure**
> ResponseDTOCustomDeploymentRefreshYamlDTO get_updated_yaml_for_infrastructure(body, account_identifier, infra_identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Return the updated yaml for infrastructure based on Deployment template

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
api_instance = swagger_client.CustomDeploymentApi(swagger_client.ApiClient(configuration))
body = swagger_client.CustomDeploymentYamlDTO() # CustomDeploymentYamlDTO | YAML
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
infra_identifier = 'infra_identifier_example' # str | Infrastructure Identifier for the entity
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Return the updated yaml for infrastructure based on Deployment template
    api_response = api_instance.get_updated_yaml_for_infrastructure(body, account_identifier, infra_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomDeploymentApi->get_updated_yaml_for_infrastructure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CustomDeploymentYamlDTO**](CustomDeploymentYamlDTO.md)| YAML | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **infra_identifier** | **str**| Infrastructure Identifier for the entity | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOCustomDeploymentRefreshYamlDTO**](ResponseDTOCustomDeploymentRefreshYamlDTO.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_infrastructure_for_deployment_template**
> ResponseDTOCustomDeploymentInfraResponseDTO validate_infrastructure_for_deployment_template(account_identifier, infra_identifier, org_identifier=org_identifier, project_identifier=project_identifier, env_identifier=env_identifier)

This validates whether Infrastructure is valid or not

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
api_instance = swagger_client.CustomDeploymentApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
infra_identifier = 'infra_identifier_example' # str | Infrastructure Identifier for the entity
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
env_identifier = 'env_identifier_example' # str | Environment Identifier for the entity (optional)

try:
    # This validates whether Infrastructure is valid or not
    api_response = api_instance.validate_infrastructure_for_deployment_template(account_identifier, infra_identifier, org_identifier=org_identifier, project_identifier=project_identifier, env_identifier=env_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomDeploymentApi->validate_infrastructure_for_deployment_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **infra_identifier** | **str**| Infrastructure Identifier for the entity | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **env_identifier** | **str**| Environment Identifier for the entity | [optional] 

### Return type

[**ResponseDTOCustomDeploymentInfraResponseDTO**](ResponseDTOCustomDeploymentInfraResponseDTO.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

