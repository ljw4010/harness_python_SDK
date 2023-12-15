# swagger_client.GlobalTemplatesApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_global_template_input_set_yaml**](GlobalTemplatesApi.md#get_global_template_input_set_yaml) | **GET** /template/api/globalTemplates/inputs/{globalTemplateIdentifier} | Gets Global Template Input Set YAML

# **get_global_template_input_set_yaml**
> ResponseDTOString get_global_template_input_set_yaml(account_identifier, global_template_identifier, version_label, load_from_cache=load_from_cache)

Gets Global Template Input Set YAML

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
api_instance = swagger_client.GlobalTemplatesApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
global_template_identifier = 'global_template_identifier_example' # str | Template Identifier for the entity
version_label = 'version_label_example' # str | Template Label
load_from_cache = 'false' # str |  (optional) (default to false)

try:
    # Gets Global Template Input Set YAML
    api_response = api_instance.get_global_template_input_set_yaml(account_identifier, global_template_identifier, version_label, load_from_cache=load_from_cache)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GlobalTemplatesApi->get_global_template_input_set_yaml: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **global_template_identifier** | **str**| Template Identifier for the entity | 
 **version_label** | **str**| Template Label | 
 **load_from_cache** | **str**|  | [optional] [default to false]

### Return type

[**ResponseDTOString**](ResponseDTOString.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

