# swagger_client.CertificatesApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**certificate_service_list_certs**](CertificatesApi.md#certificate_service_list_certs) | **GET** /gitops/api/v1/certificates | List returns list of certificates

# **certificate_service_list_certs**
> V1Certificatelist certificate_service_list_certs(account_identifier, project_identifier=project_identifier, org_identifier=org_identifier, name=name, search_term=search_term, page_size=page_size, page_index=page_index, agent_identifier=agent_identifier)

List returns list of certificates

List returns list of certificates

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
api_instance = swagger_client.CertificatesApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
name = 'name_example' # str |  (optional)
search_term = 'search_term_example' # str |  (optional)
page_size = 56 # int |  (optional)
page_index = 56 # int |  (optional)
agent_identifier = 'agent_identifier_example' # str | Agent identifier for entity. (optional)

try:
    # List returns list of certificates
    api_response = api_instance.certificate_service_list_certs(account_identifier, project_identifier=project_identifier, org_identifier=org_identifier, name=name, search_term=search_term, page_size=page_size, page_index=page_index, agent_identifier=agent_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CertificatesApi->certificate_service_list_certs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **name** | **str**|  | [optional] 
 **search_term** | **str**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **page_index** | **int**|  | [optional] 
 **agent_identifier** | **str**| Agent identifier for entity. | [optional] 

### Return type

[**V1Certificatelist**](V1Certificatelist.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

