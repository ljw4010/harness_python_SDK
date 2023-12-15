# harness_python_sdk.RepositoryCertificatesApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**agent_certificate_service_create**](RepositoryCertificatesApi.md#agent_certificate_service_create) | **POST** /gitops/api/v1/agents/{agentIdentifier}/certificates | Creates repository certificates on the server
[**agent_certificate_service_delete**](RepositoryCertificatesApi.md#agent_certificate_service_delete) | **DELETE** /gitops/api/v1/agents/{agentIdentifier}/certificates | Delete the certificates that match the RepositoryCertificateQuery
[**agent_certificate_service_list**](RepositoryCertificatesApi.md#agent_certificate_service_list) | **GET** /gitops/api/v1/agents/{agentIdentifier}/certificates | List all available repository certificates

# **agent_certificate_service_create**
> CertificatesRepositoryCertificateList agent_certificate_service_create(body, agent_identifier, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Creates repository certificates on the server

Create repository certificates.

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
api_instance = harness_python_sdk.RepositoryCertificatesApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.CertificateRepositoryCertificateCreateRequest() # CertificateRepositoryCertificateCreateRequest | 
agent_identifier = 'agent_identifier_example' # str | Agent identifier for entity.
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity. (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Creates repository certificates on the server
    api_response = api_instance.agent_certificate_service_create(body, agent_identifier, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryCertificatesApi->agent_certificate_service_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CertificateRepositoryCertificateCreateRequest**](CertificateRepositoryCertificateCreateRequest.md)|  | 
 **agent_identifier** | **str**| Agent identifier for entity. | 
 **account_identifier** | **str**| Account Identifier for the Entity. | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**CertificatesRepositoryCertificateList**](CertificatesRepositoryCertificateList.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_certificate_service_delete**
> CertificatesRepositoryCertificateList agent_certificate_service_delete(agent_identifier, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, query_host_name_pattern=query_host_name_pattern, query_cert_type=query_cert_type, query_cert_sub_type=query_cert_sub_type)

Delete the certificates that match the RepositoryCertificateQuery

Delete repository certificates.

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
api_instance = harness_python_sdk.RepositoryCertificatesApi(harness_python_sdk.ApiClient(configuration))
agent_identifier = 'agent_identifier_example' # str | Agent identifier for entity.
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity. (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str |  (optional)
query_host_name_pattern = 'query_host_name_pattern_example' # str | A file-glob pattern (not regular expression) the host name has to match. (optional)
query_cert_type = 'query_cert_type_example' # str | The type of the certificate to match (ssh or https). (optional)
query_cert_sub_type = 'query_cert_sub_type_example' # str | The sub type of the certificate to match (protocol dependent, usually only used for ssh certs). (optional)

try:
    # Delete the certificates that match the RepositoryCertificateQuery
    api_response = api_instance.agent_certificate_service_delete(agent_identifier, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, query_host_name_pattern=query_host_name_pattern, query_cert_type=query_cert_type, query_cert_sub_type=query_cert_sub_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryCertificatesApi->agent_certificate_service_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_identifier** | **str**| Agent identifier for entity. | 
 **account_identifier** | **str**| Account Identifier for the Entity. | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**|  | [optional] 
 **query_host_name_pattern** | **str**| A file-glob pattern (not regular expression) the host name has to match. | [optional] 
 **query_cert_type** | **str**| The type of the certificate to match (ssh or https). | [optional] 
 **query_cert_sub_type** | **str**| The sub type of the certificate to match (protocol dependent, usually only used for ssh certs). | [optional] 

### Return type

[**CertificatesRepositoryCertificateList**](CertificatesRepositoryCertificateList.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_certificate_service_list**
> CertificatesRepositoryCertificateList agent_certificate_service_list(agent_identifier, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, query_host_name_pattern=query_host_name_pattern, query_cert_type=query_cert_type, query_cert_sub_type=query_cert_sub_type)

List all available repository certificates

List repository certificates.

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
api_instance = harness_python_sdk.RepositoryCertificatesApi(harness_python_sdk.ApiClient(configuration))
agent_identifier = 'agent_identifier_example' # str | Agent identifier for entity.
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str |  (optional)
query_host_name_pattern = 'query_host_name_pattern_example' # str | A file-glob pattern (not regular expression) the host name has to match. (optional)
query_cert_type = 'query_cert_type_example' # str | The type of the certificate to match (ssh or https). (optional)
query_cert_sub_type = 'query_cert_sub_type_example' # str | The sub type of the certificate to match (protocol dependent, usually only used for ssh certs). (optional)

try:
    # List all available repository certificates
    api_response = api_instance.agent_certificate_service_list(agent_identifier, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, query_host_name_pattern=query_host_name_pattern, query_cert_type=query_cert_type, query_cert_sub_type=query_cert_sub_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryCertificatesApi->agent_certificate_service_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_identifier** | **str**| Agent identifier for entity. | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**|  | [optional] 
 **query_host_name_pattern** | **str**| A file-glob pattern (not regular expression) the host name has to match. | [optional] 
 **query_cert_type** | **str**| The type of the certificate to match (ssh or https). | [optional] 
 **query_cert_sub_type** | **str**| The sub type of the certificate to match (protocol dependent, usually only used for ssh certs). | [optional] 

### Return type

[**CertificatesRepositoryCertificateList**](CertificatesRepositoryCertificateList.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

