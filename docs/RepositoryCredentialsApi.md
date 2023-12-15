# harness_python_sdk.RepositoryCredentialsApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**agent_repository_credentials_service_create_repository_credentials**](RepositoryCredentialsApi.md#agent_repository_credentials_service_create_repository_credentials) | **POST** /gitops/api/v1/agents/{agentIdentifier}/repocreds | Create creates a new repository credential
[**agent_repository_credentials_service_delete_repository_credentials**](RepositoryCredentialsApi.md#agent_repository_credentials_service_delete_repository_credentials) | **DELETE** /gitops/api/v1/agents/{agentIdentifier}/repocreds/{identifier} | Delete deletes a repository credential
[**agent_repository_credentials_service_get_credentials_for_repository_url**](RepositoryCredentialsApi.md#agent_repository_credentials_service_get_credentials_for_repository_url) | **POST** /gitops/api/v1/agents/{agentIdentifier}/repocreds/get | Get returns a repository credential given its url
[**agent_repository_credentials_service_get_repository_credentials**](RepositoryCredentialsApi.md#agent_repository_credentials_service_get_repository_credentials) | **GET** /gitops/api/v1/agents/{agentIdentifier}/repocreds/{identifier} | Get returns a repository credential given its identifier
[**agent_repository_credentials_service_list_repository_credentials**](RepositoryCredentialsApi.md#agent_repository_credentials_service_list_repository_credentials) | **POST** /gitops/api/v1/repocreds | List repository credentials
[**agent_repository_credentials_service_update_repository_credentials**](RepositoryCredentialsApi.md#agent_repository_credentials_service_update_repository_credentials) | **PUT** /gitops/api/v1/agents/{agentIdentifier}/repocreds/{identifier} | Update updates a repository credential

# **agent_repository_credentials_service_create_repository_credentials**
> Servicev1RepositoryCredentials agent_repository_credentials_service_create_repository_credentials(body, account_identifier, agent_identifier, org_identifier=org_identifier, project_identifier=project_identifier, identifier=identifier)

Create creates a new repository credential

Create creates a new repository credential.

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
api_instance = harness_python_sdk.RepositoryCredentialsApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.HrepocredsRepoCredsCreateRequest() # HrepocredsRepoCredsCreateRequest | 
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
agent_identifier = 'agent_identifier_example' # str | Agent identifier for entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
identifier = 'identifier_example' # str |  (optional)

try:
    # Create creates a new repository credential
    api_response = api_instance.agent_repository_credentials_service_create_repository_credentials(body, account_identifier, agent_identifier, org_identifier=org_identifier, project_identifier=project_identifier, identifier=identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryCredentialsApi->agent_repository_credentials_service_create_repository_credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HrepocredsRepoCredsCreateRequest**](HrepocredsRepoCredsCreateRequest.md)|  | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **agent_identifier** | **str**| Agent identifier for entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **identifier** | **str**|  | [optional] 

### Return type

[**Servicev1RepositoryCredentials**](Servicev1RepositoryCredentials.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_repository_credentials_service_delete_repository_credentials**
> HrepocredsRepoCredsResponse agent_repository_credentials_service_delete_repository_credentials(agent_identifier, identifier, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, query_url=query_url, query_repo_creds_type=query_repo_creds_type)

Delete deletes a repository credential

 Delete deletes a repository credential.

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
api_instance = harness_python_sdk.RepositoryCredentialsApi(harness_python_sdk.ApiClient(configuration))
agent_identifier = 'agent_identifier_example' # str | Agent identifier for entity.
identifier = 'identifier_example' # str | 
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity. (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
query_url = 'query_url_example' # str | Repo URL for query. (optional)
query_repo_creds_type = 'query_repo_creds_type_example' # str | RepoCreds type - git or helm. (optional)

try:
    # Delete deletes a repository credential
    api_response = api_instance.agent_repository_credentials_service_delete_repository_credentials(agent_identifier, identifier, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, query_url=query_url, query_repo_creds_type=query_repo_creds_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryCredentialsApi->agent_repository_credentials_service_delete_repository_credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_identifier** | **str**| Agent identifier for entity. | 
 **identifier** | **str**|  | 
 **account_identifier** | **str**| Account Identifier for the Entity. | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **query_url** | **str**| Repo URL for query. | [optional] 
 **query_repo_creds_type** | **str**| RepoCreds type - git or helm. | [optional] 

### Return type

[**HrepocredsRepoCredsResponse**](HrepocredsRepoCredsResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_repository_credentials_service_get_credentials_for_repository_url**
> Servicev1RepositoryCredentials agent_repository_credentials_service_get_credentials_for_repository_url(body, account_identifier, agent_identifier, org_identifier=org_identifier, project_identifier=project_identifier, identifier=identifier)

Get returns a repository credential given its url

Get returns a repository credential given its url.

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
api_instance = harness_python_sdk.RepositoryCredentialsApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.HrepocredsRepoCredsQuery() # HrepocredsRepoCredsQuery | 
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
agent_identifier = 'agent_identifier_example' # str | Agent identifier for entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
identifier = 'identifier_example' # str |  (optional)

try:
    # Get returns a repository credential given its url
    api_response = api_instance.agent_repository_credentials_service_get_credentials_for_repository_url(body, account_identifier, agent_identifier, org_identifier=org_identifier, project_identifier=project_identifier, identifier=identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryCredentialsApi->agent_repository_credentials_service_get_credentials_for_repository_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HrepocredsRepoCredsQuery**](HrepocredsRepoCredsQuery.md)|  | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **agent_identifier** | **str**| Agent identifier for entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **identifier** | **str**|  | [optional] 

### Return type

[**Servicev1RepositoryCredentials**](Servicev1RepositoryCredentials.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_repository_credentials_service_get_repository_credentials**
> Servicev1RepositoryCredentials agent_repository_credentials_service_get_repository_credentials(agent_identifier, identifier, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, query_url=query_url, query_repo_creds_type=query_repo_creds_type)

Get returns a repository credential given its identifier

Get returns a repository credential given its identifier.

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
api_instance = harness_python_sdk.RepositoryCredentialsApi(harness_python_sdk.ApiClient(configuration))
agent_identifier = 'agent_identifier_example' # str | Agent identifier for entity.
identifier = 'identifier_example' # str | 
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
query_url = 'query_url_example' # str | Repo URL for query. (optional)
query_repo_creds_type = 'query_repo_creds_type_example' # str | RepoCreds type - git or helm. (optional)

try:
    # Get returns a repository credential given its identifier
    api_response = api_instance.agent_repository_credentials_service_get_repository_credentials(agent_identifier, identifier, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, query_url=query_url, query_repo_creds_type=query_repo_creds_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryCredentialsApi->agent_repository_credentials_service_get_repository_credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_identifier** | **str**| Agent identifier for entity. | 
 **identifier** | **str**|  | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **query_url** | **str**| Repo URL for query. | [optional] 
 **query_repo_creds_type** | **str**| RepoCreds type - git or helm. | [optional] 

### Return type

[**Servicev1RepositoryCredentials**](Servicev1RepositoryCredentials.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_repository_credentials_service_list_repository_credentials**
> Servicev1RepositoryCredentialsList agent_repository_credentials_service_list_repository_credentials(body)

List repository credentials

List repository credentials.

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
api_instance = harness_python_sdk.RepositoryCredentialsApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.V1RepositoryCredentialsQuery() # V1RepositoryCredentialsQuery | 

try:
    # List repository credentials
    api_response = api_instance.agent_repository_credentials_service_list_repository_credentials(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryCredentialsApi->agent_repository_credentials_service_list_repository_credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1RepositoryCredentialsQuery**](V1RepositoryCredentialsQuery.md)|  | 

### Return type

[**Servicev1RepositoryCredentialsList**](Servicev1RepositoryCredentialsList.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_repository_credentials_service_update_repository_credentials**
> Servicev1RepositoryCredentials agent_repository_credentials_service_update_repository_credentials(body, agent_identifier, identifier, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Update updates a repository credential

Update updates a repository credential.

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
api_instance = harness_python_sdk.RepositoryCredentialsApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.HrepocredsRepoCredsUpdateRequest() # HrepocredsRepoCredsUpdateRequest | 
agent_identifier = 'agent_identifier_example' # str | Agent identifier for entity.
identifier = 'identifier_example' # str | 
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity. (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Update updates a repository credential
    api_response = api_instance.agent_repository_credentials_service_update_repository_credentials(body, agent_identifier, identifier, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryCredentialsApi->agent_repository_credentials_service_update_repository_credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HrepocredsRepoCredsUpdateRequest**](HrepocredsRepoCredsUpdateRequest.md)|  | 
 **agent_identifier** | **str**| Agent identifier for entity. | 
 **identifier** | **str**|  | 
 **account_identifier** | **str**| Account Identifier for the Entity. | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**Servicev1RepositoryCredentials**](Servicev1RepositoryCredentials.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

