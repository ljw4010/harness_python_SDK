# swagger_client.PipelineRefreshApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**validate_template_inputs**](PipelineRefreshApi.md#validate_template_inputs) | **GET** /pipeline/api/refresh-template/validate-template-inputs | Validates template inputs in a pipeline&#x27;s YAML specification.

# **validate_template_inputs**
> ResponseDTOValidateTemplateInputsResponseDTO validate_template_inputs(account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, identifier=identifier, load_from_cache=load_from_cache, branch=branch, repo_identifier=repo_identifier, get_default_from_other_repo=get_default_from_other_repo)

Validates template inputs in a pipeline's YAML specification.

Validates the template inputs in a pipeline's YAML specification. If the template inputs are invalid, the operation returns an error summary.

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
api_instance = swagger_client.PipelineRefreshApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
identifier = 'identifier_example' # str |  (optional)
load_from_cache = 'false' # str |  (optional) (default to false)
branch = 'branch_example' # str | Name of the branch. (optional)
repo_identifier = 'repo_identifier_example' # str | Git Sync Config Id. (optional)
get_default_from_other_repo = true # bool | if true, return all the default entities (optional)

try:
    # Validates template inputs in a pipeline's YAML specification.
    api_response = api_instance.validate_template_inputs(account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, identifier=identifier, load_from_cache=load_from_cache, branch=branch, repo_identifier=repo_identifier, get_default_from_other_repo=get_default_from_other_repo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelineRefreshApi->validate_template_inputs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **identifier** | **str**|  | [optional] 
 **load_from_cache** | **str**|  | [optional] [default to false]
 **branch** | **str**| Name of the branch. | [optional] 
 **repo_identifier** | **str**| Git Sync Config Id. | [optional] 
 **get_default_from_other_repo** | **bool**| if true, return all the default entities | [optional] 

### Return type

[**ResponseDTOValidateTemplateInputsResponseDTO**](ResponseDTOValidateTemplateInputsResponseDTO.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

