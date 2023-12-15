# harness_python_sdk
The Harness Software Delivery Platform uses OpenAPI Specification v3.0. Harness constantly improves these APIs. Please be aware that some improvements could cause breaking changes. 
# Introduction     
The Harness API allows you to integrate and use all the services and modules we provide on the Harness Platform. If you use client-side SDKs, Harness functionality can be integrated with your client-side automation, helping you reduce manual efforts and deploy code faster.    
For more information about how Harness works, read our [documentation](https://developer.harness.io/docs/getting-started) or visit the [Harness Developer Hub](https://developer.harness.io/).  
## How it works    
The Harness API is a RESTful API that uses standard HTTP verbs. You can send requests in JSON, YAML, or form-data format. The format of the response matches the format of your request. You must send a single request at a time and ensure that you include your authentication key. For more information about this, go to [Authentication](#section/Introduction/Authentication).  
## Get started    
Before you start integrating, get to know our API better by reading the following topics:    
* [Harness key concepts](https://developer.harness.io/docs/getting-started/learn-harness-key-concepts/)
* [Authentication](#section/Introduction/Authentication)
* [Requests and responses](#section/Introduction/Requests-and-Responses)
* [Common Parameters](#section/Introduction/Common-Parameters-Beta)
* [Status Codes](#section/Introduction/Status-Codes)
* [Errors](#tag/Error-Response)
* [Versioning](#section/Introduction/Versioning-Beta)
* [Pagination](/#section/Introduction/Pagination-Beta)
The methods you need to integrate with depend on the functionality you want to use. Work with  your Harness Solutions Engineer to determine which methods you need.
## Authentication  
To authenticate with the Harness API, you need to:   
1. Generate an API token on the Harness Platform.
2. Send the API token you generate in the `x-api-key` header in each request.
### Generate an API token  
To generate an API token, complete the following steps:   
1. Go to the [Harness Platform](https://app.harness.io/).
2. On the left-hand navigation, click **My Profile**.
3. Click **+API Key**, enter a name for your key and then click **Save**.
4. Within the API Key tile, click **+Token**.
5. Enter a name for your token and click **Generate Token**.
**Important**: Make sure to save your token securely. Harness does not store the API token for future reference, so make sure to save your token securely before you leave the page.
### Send the API token in your requests  
Send the token you created in the Harness Platform in the x-api-key header. 
For example:   `x-api-key: YOUR_API_KEY_HERE`  
## Requests and Responses    
The structure for each request and response is outlined in the API documentation. We have examples in JSON and YAML for every request and response. You can use our online editor to test the examples.  
## Common Parameters [Beta]  
| Field Name | Type    | Default | Description    | 
|------------|---------|---------|----------------| 
| identifier | string  | none    | URL-friendly version of the name, used to identify a resource within it's scope and so needs to be unique within the scope. | 
| name       | string  | none    | Human-friendly name for the resource.| 
| org        | string  | none    | Limit to provided org identifiers. | 
| project    | string  | none    | Limit to provided project identifiers.| 
| description| string  | none    | More information about the specific resource.| 
| tags       | map[string]string  | none    | List of labels applied to the resource.| 
| order      | string  | desc    | Order to use when sorting the specified fields. Type: enum(asc,desc).| 
| sort       | string  | none    | Fields on which to sort. Note: Specify the fields that you want to use for sorting. When doing so, consider the operational overhead of sorting fields. | 
| limit      | int     | 30      | Pagination: Number of items to return.| 
| page       | int     | 1       | Pagination page number strategy: Specify the page number within the paginated collection related to the number of items in each page.                  | 
| created    | int64   | none    | Unix timestamp that shows when the resource was created (in milliseconds).                                                               | 
| updated    | int64   | none    | Unix timestamp that shows when the resource was last edited (in milliseconds).                                                           |   
## Status Codes    
Harness uses conventional HTTP status codes to indicate the status of an API request.    Generally, 2xx responses are reserved for success and 4xx status codes are reserved for failures. A 5xx response code indicates an error on the Harness server.    
| Error Code  | Description |   
|-------------|-------------|   
| 200         |     OK      |   
| 201         |   Created   |   
| 202         |   Accepted  |   
| 204         |  No Content |   
| 400         | Bad Request |   
| 401         | Unauthorized |   
| 403         | Forbidden |   | 412         
| Precondition Failed |   
| 415         | Unsupported Media Type |   
| 500         | Server Error |   

To view our error response structures, go [here](#tag/Error-Response).  
## Versioning [Beta]  
### Harness Version   
The current version of our Beta APIs is yet to be announced. The version number will use the date-header format and will be valid only for our Beta APIs.  
### Generation   
All our beta APIs are versioned as a Generation, and this version is included in the path to every API resource. For example, v1 beta APIs begin with `app.harness.io/v1/`, where v1 is the API Generation.    
The version number represents the core API and does not change frequently. The version number changes only if there is a significant departure from the basic underpinnings of the existing API. For example, when Harness performs a system-wide refactoring of core concepts or resources.  
## Pagination [Beta]  
We use pagination to place limits on the number of responses associated with list endpoints. Pagination is achieved by the use of limit query parameters. The limit defaults to 30. Its maximum value is 100.  
Following are the pagination headers supported in the response bodies of paginated APIs:   
1. X-Total-Elements : Indicates the total number of entries in a paginated response.
2. X-Page-Number : Indicates the page number currently returned for a paginated response.
3. X-Page-Size : Indicates the number of entries per page for a paginated response.  For example:    ``` X-Total-Elements : 30 X-Page-Number : 0 X-Page-Size : 10   ``` 

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0
- Package version: v1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen
For more information, please visit [https://harness.io/](https://harness.io/)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import harness_python_sdk 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import harness_python_sdk
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
api_instance = harness_python_sdk.APIKeysApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier
org_identifier = 'org_identifier_example' # str | Organization Identifier
environment_identifier = 'environment_identifier_example' # str | Environment Identifier
project_identifier = 'project_identifier_example' # str | The Project identifier
body = NULL # object |  (optional)

try:
    # Creates an API key for the given Environment
    api_response = api_instance.add_api_key(account_identifier, org_identifier, environment_identifier, project_identifier, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIKeysApi->add_api_key: %s\n" % e)

# Configure API key authorization: x-api-key
configuration = harness_python_sdk.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = harness_python_sdk.APIKeysApi(harness_python_sdk.ApiClient(configuration))
identifier = 'identifier_example' # str | Unique identifier for the object in the API.
project_identifier = 'project_identifier_example' # str | The Project identifier
environment_identifier = 'environment_identifier_example' # str | Environment Identifier
account_identifier = 'account_identifier_example' # str | Account Identifier
org_identifier = 'org_identifier_example' # str | Organization Identifier

try:
    # Deletes an API Key
    api_instance.delete_api_key(identifier, project_identifier, environment_identifier, account_identifier, org_identifier)
except ApiException as e:
    print("Exception when calling APIKeysApi->delete_api_key: %s\n" % e)

# Configure API key authorization: x-api-key
configuration = harness_python_sdk.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = harness_python_sdk.APIKeysApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier
org_identifier = 'org_identifier_example' # str | Organization Identifier
project_identifier = 'project_identifier_example' # str | The Project identifier
environment_identifier = 'environment_identifier_example' # str | Environment Identifier
page_number = 56 # int | PageNumber (optional)
page_size = 56 # int | PageSize (optional)

try:
    # Returns API Keys for an Environment
    api_response = api_instance.get_all_api_keys(account_identifier, org_identifier, project_identifier, environment_identifier, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIKeysApi->get_all_api_keys: %s\n" % e)

# Configure API key authorization: x-api-key
configuration = harness_python_sdk.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = harness_python_sdk.APIKeysApi(harness_python_sdk.ApiClient(configuration))
identifier = 'identifier_example' # str | Unique identifier for the object in the API.
project_identifier = 'project_identifier_example' # str | The Project identifier
environment_identifier = 'environment_identifier_example' # str | Environment Identifier
account_identifier = 'account_identifier_example' # str | Account Identifier
org_identifier = 'org_identifier_example' # str | Organization Identifier

try:
    # Returns API keys
    api_response = api_instance.get_api_key(identifier, project_identifier, environment_identifier, account_identifier, org_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIKeysApi->get_api_key: %s\n" % e)

# Configure API key authorization: x-api-key
configuration = harness_python_sdk.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = harness_python_sdk.APIKeysApi(harness_python_sdk.ApiClient(configuration))
project_identifier = 'project_identifier_example' # str | The Project identifier
environment_identifier = 'environment_identifier_example' # str | Environment Identifier
account_identifier = 'account_identifier_example' # str | Account Identifier
org_identifier = 'org_identifier_example' # str | Organization Identifier
identifier = 'identifier_example' # str | Unique identifier for the object in the API.
body = NULL # object |  (optional)

try:
    # Updates an API Key
    api_instance.update_api_key(project_identifier, environment_identifier, account_identifier, org_identifier, identifier, body=body)
except ApiException as e:
    print("Exception when calling APIKeysApi->update_api_key: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://app.harness.io*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*APIKeysApi* | [**add_api_key**](docs/APIKeysApi.md#add_api_key) | **POST** /cf/admin/apikey | Creates an API key for the given Environment
*APIKeysApi* | [**delete_api_key**](docs/APIKeysApi.md#delete_api_key) | **DELETE** /cf/admin/apikey/{identifier} | Deletes an API Key
*APIKeysApi* | [**get_all_api_keys**](docs/APIKeysApi.md#get_all_api_keys) | **GET** /cf/admin/apikey | Returns API Keys for an Environment
*APIKeysApi* | [**get_api_key**](docs/APIKeysApi.md#get_api_key) | **GET** /cf/admin/apikey/{identifier} | Returns API keys
*APIKeysApi* | [**update_api_key**](docs/APIKeysApi.md#update_api_key) | **PUT** /cf/admin/apikey/{identifier} | Updates an API Key
*AccessControlListApi* | [**get_access_control_list**](docs/AccessControlListApi.md#get_access_control_list) | **POST** /authz/api/acl | Check Permission
*AccountSettingApi* | [**get_account_setting**](docs/AccountSettingApi.md#get_account_setting) | **GET** /ng/api/account-setting | Get the AccountSetting by accountIdentifier
*AccountSettingApi* | [**list_account_setting**](docs/AccountSettingApi.md#list_account_setting) | **GET** /ng/api/account-setting/list | Get the AccountSetting by accountIdentifier
*AccountSettingApi* | [**update_account_setting**](docs/AccountSettingApi.md#update_account_setting) | **PUT** /ng/api/account-setting | Updates account settings
*AccountConnectorApi* | [**create_account_scoped_connector**](docs/AccountConnectorApi.md#create_account_scoped_connector) | **POST** /v1/connectors | Create a Connector
*AccountConnectorApi* | [**delete_account_scoped_connector**](docs/AccountConnectorApi.md#delete_account_scoped_connector) | **DELETE** /v1/connectors/{connector} | Delete a connector
*AccountConnectorApi* | [**get_account_scoped_connector**](docs/AccountConnectorApi.md#get_account_scoped_connector) | **GET** /v1/connectors/{connector} | Retrieve a connector
*AccountConnectorApi* | [**test_account_scoped_connector**](docs/AccountConnectorApi.md#test_account_scoped_connector) | **GET** /v1/connectors/{connector}/test-connection | Test a connector
*AccountConnectorApi* | [**update_account_scoped_connector**](docs/AccountConnectorApi.md#update_account_scoped_connector) | **PUT** /v1/connectors/{connector} | Update a connector
*AccountRancherInfrastructureApi* | [**list_account_scoped_rancher_clusters_using_connector**](docs/AccountRancherInfrastructureApi.md#list_account_scoped_rancher_clusters_using_connector) | **GET** /v1/rancher/connectors/{connector}/clusters | List rancher clusters using account level connector
*AccountRancherInfrastructureApi* | [**list_account_scoped_rancher_clusters_using_env_and_infra**](docs/AccountRancherInfrastructureApi.md#list_account_scoped_rancher_clusters_using_env_and_infra) | **GET** /v1/rancher/environments/{environment}/infrastructure-definitions/{infrastructure-definition}/clusters | List rancher clusters using account level env and infra def
*AccountResourceGroupsApi* | [**create_resource_group_acc**](docs/AccountResourceGroupsApi.md#create_resource_group_acc) | **POST** /v1/resource-groups | Create a Resource Group
*AccountResourceGroupsApi* | [**delete_resource_group_acc**](docs/AccountResourceGroupsApi.md#delete_resource_group_acc) | **DELETE** /v1/resource-groups/{resource-group} | Delete a Resource Group
*AccountResourceGroupsApi* | [**get_resource_group_acc**](docs/AccountResourceGroupsApi.md#get_resource_group_acc) | **GET** /v1/resource-groups/{resource-group} | Retrieve a Resource Group
*AccountResourceGroupsApi* | [**list_resource_groups_acc**](docs/AccountResourceGroupsApi.md#list_resource_groups_acc) | **GET** /v1/resource-groups | List Resource Groups
*AccountResourceGroupsApi* | [**update_resource_group_acc**](docs/AccountResourceGroupsApi.md#update_resource_group_acc) | **PUT** /v1/resource-groups/{resource-group} | Update a Resource Group
*AccountRoleAssignmentsApi* | [**create_account_scoped_role_assignments**](docs/AccountRoleAssignmentsApi.md#create_account_scoped_role_assignments) | **POST** /v1/role-assignments | Create a role assignment
*AccountRoleAssignmentsApi* | [**delete_account_scoped_role_assignment**](docs/AccountRoleAssignmentsApi.md#delete_account_scoped_role_assignment) | **DELETE** /v1/role-assignments/{role-assignment} | Delete a role assignment
*AccountRoleAssignmentsApi* | [**get_account_scoped_role_assignment**](docs/AccountRoleAssignmentsApi.md#get_account_scoped_role_assignment) | **GET** /v1/role-assignments/{role-assignment} | Retrieve a role assignment
*AccountRoleAssignmentsApi* | [**get_account_scoped_role_assignments**](docs/AccountRoleAssignmentsApi.md#get_account_scoped_role_assignments) | **GET** /v1/role-assignments | List role assignments
*AccountRolesApi* | [**create_role_acc**](docs/AccountRolesApi.md#create_role_acc) | **POST** /v1/roles | Create a Role
*AccountRolesApi* | [**delete_role_acc**](docs/AccountRolesApi.md#delete_role_acc) | **DELETE** /v1/roles/{role} | Delete a Role
*AccountRolesApi* | [**get_role_acc**](docs/AccountRolesApi.md#get_role_acc) | **GET** /v1/roles/{role} | Retrieve a Role
*AccountRolesApi* | [**list_roles_acc**](docs/AccountRolesApi.md#list_roles_acc) | **GET** /v1/roles | List Roles
*AccountRolesApi* | [**update_role_acc**](docs/AccountRolesApi.md#update_role_acc) | **PUT** /v1/roles/{role} | Update a Role
*AccountSecretApi* | [**create_account_scoped_secret**](docs/AccountSecretApi.md#create_account_scoped_secret) | **POST** /v1/secrets | Create a secret
*AccountSecretApi* | [**delete_account_scoped_secret**](docs/AccountSecretApi.md#delete_account_scoped_secret) | **DELETE** /v1/secrets/{secret} | Deletes a secret
*AccountSecretApi* | [**get_account_scoped_secret**](docs/AccountSecretApi.md#get_account_scoped_secret) | **GET** /v1/secrets/{secret} | Retrieve a secret
*AccountSecretApi* | [**get_account_scoped_secrets**](docs/AccountSecretApi.md#get_account_scoped_secrets) | **GET** /v1/secrets | List secrets
*AccountSecretApi* | [**update_account_scoped_secret**](docs/AccountSecretApi.md#update_account_scoped_secret) | **PUT** /v1/secrets/{secret} | Update a secret
*AccountSecretApi* | [**validate_account_secret_ref**](docs/AccountSecretApi.md#validate_account_secret_ref) | **POST** /v1/secrets/validate-secret-ref | Validate secret reference
*AccountServicesApi* | [**create_account_scoped_service**](docs/AccountServicesApi.md#create_account_scoped_service) | **POST** /v1/services | Create a service
*AccountServicesApi* | [**delete_account_scoped_service**](docs/AccountServicesApi.md#delete_account_scoped_service) | **DELETE** /v1/services/{service} | Delete a service
*AccountServicesApi* | [**get_account_scoped_service**](docs/AccountServicesApi.md#get_account_scoped_service) | **GET** /v1/services/{service} | Retrieve a service
*AccountServicesApi* | [**get_account_scoped_services**](docs/AccountServicesApi.md#get_account_scoped_services) | **GET** /v1/services | List services
*AccountServicesApi* | [**update_account_scoped_service**](docs/AccountServicesApi.md#update_account_scoped_service) | **PUT** /v1/services/{service} | Update service
*AccountTemplateApi* | [**create_templates_acc**](docs/AccountTemplateApi.md#create_templates_acc) | **POST** /v1/templates | Create Template
*AccountTemplateApi* | [**delete_template_acc**](docs/AccountTemplateApi.md#delete_template_acc) | **DELETE** /v1/templates/{template}/versions/{version} | Delete Template
*AccountTemplateApi* | [**get_template_acc**](docs/AccountTemplateApi.md#get_template_acc) | **GET** /v1/templates/{template}/versions/{version} | Retrieve a Template
*AccountTemplateApi* | [**get_template_stable_acc**](docs/AccountTemplateApi.md#get_template_stable_acc) | **GET** /v1/templates/{template} | Get Stable Template
*AccountTemplateApi* | [**get_templates_list_acc**](docs/AccountTemplateApi.md#get_templates_list_acc) | **GET** /v1/templates | Get Templates List
*AccountTemplateApi* | [**import_template_acc**](docs/AccountTemplateApi.md#import_template_acc) | **POST** /v1/templates/{template}/import | Import Template
*AccountTemplateApi* | [**update_template_acc**](docs/AccountTemplateApi.md#update_template_acc) | **PUT** /v1/templates/{template}/versions/{version} | Update Template
*AccountTemplateApi* | [**update_template_stable_acc**](docs/AccountTemplateApi.md#update_template_stable_acc) | **PUT** /v1/templates/{template}/versions/{version}/stable | Update Stable Template
*AccountsApi* | [**get_account_ng**](docs/AccountsApi.md#get_account_ng) | **GET** /ng/api/accounts/{accountIdentifier} | Gets an account
*AccountsApi* | [**is_immutable_delegate_enabled**](docs/AccountsApi.md#is_immutable_delegate_enabled) | **GET** /ng/api/accounts/{accountIdentifier}/immutable-delegate-enabled | Checks if immutable delegate is enabled for account
*AccountsApi* | [**update_account_default_experience_ng**](docs/AccountsApi.md#update_account_default_experience_ng) | **PUT** /ng/api/accounts/{accountIdentifier}/default-experience | Update Default Experience
*AccountsApi* | [**update_account_name_ng**](docs/AccountsApi.md#update_account_name_ng) | **PUT** /ng/api/accounts/{accountIdentifier}/name | Update Account Name
*AgentMTLSEndpointManagementApi* | [**check_agent_mtls_endpoint_domain_prefix_availability**](docs/AgentMTLSEndpointManagementApi.md#check_agent_mtls_endpoint_domain_prefix_availability) | **GET** /ng/api/agent/mtls/check-availability | Checks whether a given agent mTLS endpoint domain prefix is available.
*AgentMTLSEndpointManagementApi* | [**create_agent_mtls_endpoint_for_account**](docs/AgentMTLSEndpointManagementApi.md#create_agent_mtls_endpoint_for_account) | **POST** /ng/api/agent/mtls/endpoint | Creates the agent mTLS endpoint for an account.
*AgentMTLSEndpointManagementApi* | [**delete_agent_mtls_endpoint_for_account**](docs/AgentMTLSEndpointManagementApi.md#delete_agent_mtls_endpoint_for_account) | **DELETE** /ng/api/agent/mtls/endpoint | Removes the agent mTLS endpoint for an account.
*AgentMTLSEndpointManagementApi* | [**get_agent_mtls_endpoint_for_account**](docs/AgentMTLSEndpointManagementApi.md#get_agent_mtls_endpoint_for_account) | **GET** /ng/api/agent/mtls/endpoint | Gets the agent mTLS endpoint for an account.
*AgentMTLSEndpointManagementApi* | [**patch_agent_mtls_endpoint_for_account**](docs/AgentMTLSEndpointManagementApi.md#patch_agent_mtls_endpoint_for_account) | **PATCH** /ng/api/agent/mtls/endpoint | Updates selected properties of the existing agent mTLS endpoint for an account.
*AgentMTLSEndpointManagementApi* | [**update_agent_mtls_endpoint_for_account**](docs/AgentMTLSEndpointManagementApi.md#update_agent_mtls_endpoint_for_account) | **PUT** /ng/api/agent/mtls/endpoint | Updates the existing agent mTLS endpoint for an account.
*AgentsApi* | [**agent_service_for_server_create**](docs/AgentsApi.md#agent_service_for_server_create) | **POST** /gitops/api/v1/agents | 
*AgentsApi* | [**agent_service_for_server_delete**](docs/AgentsApi.md#agent_service_for_server_delete) | **DELETE** /gitops/api/v1/agents/{identifier} | 
*AgentsApi* | [**agent_service_for_server_get**](docs/AgentsApi.md#agent_service_for_server_get) | **GET** /gitops/api/v1/agents/{identifier} | 
*AgentsApi* | [**agent_service_for_server_get_deploy_yaml**](docs/AgentsApi.md#agent_service_for_server_get_deploy_yaml) | **GET** /gitops/api/v1/agents/{agentIdentifier}/deploy.yaml | 
*AgentsApi* | [**agent_service_for_server_list**](docs/AgentsApi.md#agent_service_for_server_list) | **GET** /gitops/api/v1/agents | 
*AgentsApi* | [**agent_service_for_server_regenerate_credentials**](docs/AgentsApi.md#agent_service_for_server_regenerate_credentials) | **POST** /gitops/api/v1/agents/{identifier}/credentials | 
*AgentsApi* | [**agent_service_for_server_unique**](docs/AgentsApi.md#agent_service_for_server_unique) | **GET** /gitops/api/v1/agents/{identifier}/unique | 
*AgentsApi* | [**agent_service_for_server_update**](docs/AgentsApi.md#agent_service_for_server_update) | **PUT** /gitops/api/v1/agents/{agent.identifier} | 
*AiEngineApi* | [**get_prompt_resources**](docs/AiEngineApi.md#get_prompt_resources) | **GET** /ccm/api/governance/promptResources | Get supported prompt resources
*AiEngineApi* | [**get_prompt_rules**](docs/AiEngineApi.md#get_prompt_rules) | **GET** /ccm/api/governance/promptRules | Get sample prompt governance rules
*ApiKeyApi* | [**create_api_key**](docs/ApiKeyApi.md#create_api_key) | **POST** /ng/api/apikey | Creates an API key
*ApiKeyApi* | [**delete_api_key**](docs/ApiKeyApi.md#delete_api_key) | **DELETE** /ng/api/apikey/{identifier} | Deletes the API Key corresponding to the provided ID.
*ApiKeyApi* | [**get_aggregated_api_key**](docs/ApiKeyApi.md#get_aggregated_api_key) | **GET** /ng/api/apikey/aggregate/{identifier} | Fetches the API Keys details corresponding to the provided ID and Scope.
*ApiKeyApi* | [**list_api_keys**](docs/ApiKeyApi.md#list_api_keys) | **GET** /ng/api/apikey/aggregate | Fetches the list of Aggregated API Keys corresponding to the request&#x27;s filter criteria.
*ApiKeyApi* | [**list_api_keys1**](docs/ApiKeyApi.md#list_api_keys1) | **GET** /ng/api/apikey | Fetches the list of API Keys corresponding to the request&#x27;s filter criteria.
*ApiKeyApi* | [**update_api_key**](docs/ApiKeyApi.md#update_api_key) | **PUT** /ng/api/apikey/{identifier} | Updates API Key for the provided ID
*ApplicationApi* | [**application_service_list_apps**](docs/ApplicationApi.md#application_service_list_apps) | **POST** /gitops/api/v1/applications | 
*ApplicationsApi* | [**agent_application_service_create**](docs/ApplicationsApi.md#agent_application_service_create) | **POST** /gitops/api/v1/agents/{agentIdentifier}/applications | Create creates an application
*ApplicationsApi* | [**agent_application_service_delete**](docs/ApplicationsApi.md#agent_application_service_delete) | **DELETE** /gitops/api/v1/agents/{agentIdentifier}/applications/{request.name} | Delete deletes an application
*ApplicationsApi* | [**agent_application_service_delete_resource**](docs/ApplicationsApi.md#agent_application_service_delete_resource) | **DELETE** /gitops/api/v1/agents/{agentIdentifier}/applications/{request.name}/resource | DeleteResource deletes a single application resource
*ApplicationsApi* | [**agent_application_service_get**](docs/ApplicationsApi.md#agent_application_service_get) | **GET** /gitops/api/v1/agents/{agentIdentifier}/applications/{query.name} | Get returns an application by name
*ApplicationsApi* | [**agent_application_service_get_application_sync_windows**](docs/ApplicationsApi.md#agent_application_service_get_application_sync_windows) | **GET** /gitops/api/v1/agents/{agentIdentifier}/applications/{query.name}/syncwindows | Get returns sync windows of the application
*ApplicationsApi* | [**agent_application_service_get_manifests**](docs/ApplicationsApi.md#agent_application_service_get_manifests) | **GET** /gitops/api/v1/agents/{agentIdentifier}/applications/{query.name}/manifests | GetManifests returns application manifests
*ApplicationsApi* | [**agent_application_service_get_resource**](docs/ApplicationsApi.md#agent_application_service_get_resource) | **GET** /gitops/api/v1/agents/{agentIdentifier}/applications/{request.name}/resource | GetResource returns single application resource
*ApplicationsApi* | [**agent_application_service_list**](docs/ApplicationsApi.md#agent_application_service_list) | **GET** /gitops/api/v1/agents/{agentIdentifier}/applications | List returns list of applications for a specific agent
*ApplicationsApi* | [**agent_application_service_list_resource_actions**](docs/ApplicationsApi.md#agent_application_service_list_resource_actions) | **GET** /gitops/api/v1/agents/{agentIdentifier}/applications/{request.name}/resource/actions | ListResourceActions returns list of resource actions
*ApplicationsApi* | [**agent_application_service_list_resource_events**](docs/ApplicationsApi.md#agent_application_service_list_resource_events) | **GET** /gitops/api/v1/agents/{agentIdentifier}/applications/{query.name}/events | ListResourceEvents returns a list of event resources
*ApplicationsApi* | [**agent_application_service_managed_resources**](docs/ApplicationsApi.md#agent_application_service_managed_resources) | **GET** /gitops/api/v1/agents/{agentIdentifier}/applications/{query.applicationName}/managed-resources | ManagedResources returns list of managed resources
*ApplicationsApi* | [**agent_application_service_patch**](docs/ApplicationsApi.md#agent_application_service_patch) | **PATCH** /gitops/api/v1/agents/{agentIdentifier}/applications/{request.name} | Patch patch an application
*ApplicationsApi* | [**agent_application_service_patch_resource**](docs/ApplicationsApi.md#agent_application_service_patch_resource) | **POST** /gitops/api/v1/agents/{agentIdentifier}/applications/{request.name}/resource | PatchResource patch single application resource
*ApplicationsApi* | [**agent_application_service_pod_logs**](docs/ApplicationsApi.md#agent_application_service_pod_logs) | **GET** /gitops/api/v1/agents/{agentIdentifier}/applications/{query.name}/pods/{query.podName}/logs | PodLogs returns stream of log entries for the specified pod(s).
*ApplicationsApi* | [**agent_application_service_pod_logs2**](docs/ApplicationsApi.md#agent_application_service_pod_logs2) | **GET** /gitops/api/v1/agents/{agentIdentifier}/applications/{query.name}/logs | PodLogs returns stream of log entries for the specified pod(s).
*ApplicationsApi* | [**agent_application_service_resource_tree**](docs/ApplicationsApi.md#agent_application_service_resource_tree) | **GET** /gitops/api/v1/agents/{agentIdentifier}/applications/{query.name}/resource-tree | ResourceTree returns resource tree
*ApplicationsApi* | [**agent_application_service_revision_metadata**](docs/ApplicationsApi.md#agent_application_service_revision_metadata) | **GET** /gitops/api/v1/agents/{agentIdentifier}/applications/{query.name}/revisions/{query.revision}/metadata | Get the meta-data (author, date, tags, message) for a specific revision of the application
*ApplicationsApi* | [**agent_application_service_rollback**](docs/ApplicationsApi.md#agent_application_service_rollback) | **POST** /gitops/api/v1/agents/{agentIdentifier}/applications/{request.name}/rollback | Rollback syncs an application to its target state Harness Event type (rollback)
*ApplicationsApi* | [**agent_application_service_run_resource_action**](docs/ApplicationsApi.md#agent_application_service_run_resource_action) | **POST** /gitops/api/v1/agents/{agentIdentifier}/applications/{request.name}/resource/actions | RunResourceAction run resource action
*ApplicationsApi* | [**agent_application_service_sync**](docs/ApplicationsApi.md#agent_application_service_sync) | **POST** /gitops/api/v1/agents/{agentIdentifier}/applications/{request.name}/sync | Sync syncs an application to its target state Harness Event type (deploy)
*ApplicationsApi* | [**agent_application_service_terminate_operation**](docs/ApplicationsApi.md#agent_application_service_terminate_operation) | **DELETE** /gitops/api/v1/agents/{agentIdentifier}/applications/{request.name}/operation | TerminateOperation terminates the currently running operation
*ApplicationsApi* | [**agent_application_service_update**](docs/ApplicationsApi.md#agent_application_service_update) | **PUT** /gitops/api/v1/agents/{agentIdentifier}/applications/{request.application.metadata.name} | Update updates an application
*ApplicationsApi* | [**agent_application_service_update_spec**](docs/ApplicationsApi.md#agent_application_service_update_spec) | **PUT** /gitops/api/v1/agents/{agentIdentifier}/applications/{request.name}/spec | UpdateSpec updates an application spec
*ApplicationsApi* | [**agent_application_service_watch**](docs/ApplicationsApi.md#agent_application_service_watch) | **GET** /gitops/api/v1/agents/{agentIdentifier}/stream/applications | Watch returns stream of application change events
*ApplicationsApi* | [**agent_application_service_watch_resource_tree**](docs/ApplicationsApi.md#agent_application_service_watch_resource_tree) | **GET** /gitops/api/v1/agents/{agentIdentifier}/stream/applications/{query.applicationName}/resource-tree | WatchResourceTree returns stream of application resource tree
*ApplicationsApi* | [**application_service_exists**](docs/ApplicationsApi.md#application_service_exists) | **GET** /gitops/api/v1/applications/{name}/exists | Checks whether an app with the given name exists
*ApplicationsApi* | [**application_service_list_app_sync**](docs/ApplicationsApi.md#application_service_list_app_sync) | **POST** /gitops/api/v1/applications/sync | List returns list of application sync status
*ApprovalsApi* | [**add_harness_approval_activity**](docs/ApprovalsApi.md#add_harness_approval_activity) | **POST** /pipeline/api/approvals/{approvalInstanceId}/harness/activity | Approve or Reject a Pipeline Execution
*ApprovalsApi* | [**get_approval_instances_by_execution_id**](docs/ApprovalsApi.md#get_approval_instances_by_execution_id) | **GET** /v1/orgs/{org}/projects/{project}/approvals/execution/{execution-id} | Gets Approval Instances by Execution Id
*AuditApi* | [**get_audit_event_list**](docs/AuditApi.md#get_audit_event_list) | **POST** /audit/api/audits/list | List Audit Events
*AuditFiltersApi* | [**delete_audit_filter**](docs/AuditFiltersApi.md#delete_audit_filter) | **DELETE** /audit/api/auditFilters/{identifier} | Delete a Filter of type Audit by identifier
*AuditFiltersApi* | [**get_audit_filter**](docs/AuditFiltersApi.md#get_audit_filter) | **GET** /audit/api/auditFilters/{identifier} | Gets a Filter of type Audit by identifier
*AuditFiltersApi* | [**get_audit_filter_list**](docs/AuditFiltersApi.md#get_audit_filter_list) | **GET** /audit/api/auditFilters | Get the list of Filters of type Audit satisfying the criteria (if any) in the request
*AuditFiltersApi* | [**post_audit_filter**](docs/AuditFiltersApi.md#post_audit_filter) | **POST** /audit/api/auditFilters | Creates a Filter
*AuditFiltersApi* | [**update_audit_filter**](docs/AuditFiltersApi.md#update_audit_filter) | **PUT** /audit/api/auditFilters | Updates the Filter of type Audit
*AuthenticationSettingsApi* | [**create_ldap_settings**](docs/AuthenticationSettingsApi.md#create_ldap_settings) | **POST** /ng/api/authentication-settings/ldap/settings | Create Ldap setting
*AuthenticationSettingsApi* | [**delete_ldap_settings**](docs/AuthenticationSettingsApi.md#delete_ldap_settings) | **DELETE** /ng/api/authentication-settings/ldap/settings | Delete Ldap settings
*AuthenticationSettingsApi* | [**delete_saml_meta_data**](docs/AuthenticationSettingsApi.md#delete_saml_meta_data) | **DELETE** /ng/api/authentication-settings/delete-saml-metadata | Delete SAML meta data
*AuthenticationSettingsApi* | [**delete_saml_meta_data_for_saml_ssoid**](docs/AuthenticationSettingsApi.md#delete_saml_meta_data_for_saml_ssoid) | **DELETE** /ng/api/authentication-settings/saml-metadata/{samlSSOId}/delete | Delete SAML meta data for given SAML sso id
*AuthenticationSettingsApi* | [**enable_disable_authentication_for_saml_setting**](docs/AuthenticationSettingsApi.md#enable_disable_authentication_for_saml_setting) | **PUT** /ng/api/authentication-settings/saml-metadata-upload/{samlSSOId}/authentication | Update authentication enabled or not for given SAML setting
*AuthenticationSettingsApi* | [**get_authentication_settings**](docs/AuthenticationSettingsApi.md#get_authentication_settings) | **GET** /ng/api/authentication-settings | Gets authentication settings for the given Account ID
*AuthenticationSettingsApi* | [**get_authentication_settings_v2**](docs/AuthenticationSettingsApi.md#get_authentication_settings_v2) | **GET** /ng/api/authentication-settings/v2 | Gets authentication settings version 2 for the given Account ID
*AuthenticationSettingsApi* | [**get_ldap_settings**](docs/AuthenticationSettingsApi.md#get_ldap_settings) | **GET** /ng/api/authentication-settings/ldap/settings | Return configured Ldap settings for the account
*AuthenticationSettingsApi* | [**get_password_strength_settings**](docs/AuthenticationSettingsApi.md#get_password_strength_settings) | **GET** /ng/api/authentication-settings/login-settings/password-strength | Get password strength
*AuthenticationSettingsApi* | [**get_saml_login_test**](docs/AuthenticationSettingsApi.md#get_saml_login_test) | **GET** /ng/api/authentication-settings/saml-login-test | Test SAML connectivity
*AuthenticationSettingsApi* | [**get_saml_login_test_v2**](docs/AuthenticationSettingsApi.md#get_saml_login_test_v2) | **GET** /ng/api/authentication-settings/saml-login-test/{samlSSOId} | Test SAML connectivity
*AuthenticationSettingsApi* | [**remove_oauth_mechanism**](docs/AuthenticationSettingsApi.md#remove_oauth_mechanism) | **DELETE** /ng/api/authentication-settings/oauth/remove-mechanism | Delete OAuth Setting
*AuthenticationSettingsApi* | [**set_public_access**](docs/AuthenticationSettingsApi.md#set_public_access) | **PUT** /ng/api/authentication-settings/public-access | Enable/disable public access at account level
*AuthenticationSettingsApi* | [**set_session_timeout_at_account_level**](docs/AuthenticationSettingsApi.md#set_session_timeout_at_account_level) | **PUT** /ng/api/authentication-settings/session-timeout-account-level | Set session timeout at account level
*AuthenticationSettingsApi* | [**set_two_factor_auth_at_account_level**](docs/AuthenticationSettingsApi.md#set_two_factor_auth_at_account_level) | **PUT** /ng/api/authentication-settings/two-factor-admin-override-settings | Set two factor authorization
*AuthenticationSettingsApi* | [**update_auth_mechanism**](docs/AuthenticationSettingsApi.md#update_auth_mechanism) | **PUT** /ng/api/authentication-settings/update-auth-mechanism | Update Auth mechanism
*AuthenticationSettingsApi* | [**update_ldap_settings**](docs/AuthenticationSettingsApi.md#update_ldap_settings) | **PUT** /ng/api/authentication-settings/ldap/settings | Updates Ldap setting
*AuthenticationSettingsApi* | [**update_oauth_providers**](docs/AuthenticationSettingsApi.md#update_oauth_providers) | **PUT** /ng/api/authentication-settings/oauth/update-providers | Update Oauth providers
*AuthenticationSettingsApi* | [**update_saml_meta_data**](docs/AuthenticationSettingsApi.md#update_saml_meta_data) | **PUT** /ng/api/authentication-settings/saml-metadata-upload | Update SAML metadata
*AuthenticationSettingsApi* | [**update_saml_meta_data_for_saml_ssoid**](docs/AuthenticationSettingsApi.md#update_saml_meta_data_for_saml_ssoid) | **PUT** /ng/api/authentication-settings/saml-metadata-upload/{samlSSOId} | Update SAML metadata for a given SAML SSO Id
*AuthenticationSettingsApi* | [**update_whitelisted_domains**](docs/AuthenticationSettingsApi.md#update_whitelisted_domains) | **PUT** /ng/api/authentication-settings/whitelisted-domains | Updates the whitelisted domains
*AuthenticationSettingsApi* | [**upload_saml_meta_data**](docs/AuthenticationSettingsApi.md#upload_saml_meta_data) | **POST** /ng/api/authentication-settings/saml-metadata-upload | Upload SAML metadata
*CannyApi* | [**create_canny_post**](docs/CannyApi.md#create_canny_post) | **POST** /ng/api/canny/post | create Canny Post for given user
*CannyApi* | [**get_canny_boards**](docs/CannyApi.md#get_canny_boards) | **GET** /ng/api/canny/boards | Get a list of boards available on Canny
*CertificatesApi* | [**certificate_service_list_certs**](docs/CertificatesApi.md#certificate_service_list_certs) | **GET** /gitops/api/v1/certificates | List returns list of certificates
*CloudCostAnomaliesApi* | [**anomaly_filter_values**](docs/CloudCostAnomaliesApi.md#anomaly_filter_values) | **POST** /ccm/api/anomaly/filter-values | Returns the list of distinct values for all the specified Anomaly fields.
*CloudCostAnomaliesApi* | [**get_anomalies_summary**](docs/CloudCostAnomaliesApi.md#get_anomalies_summary) | **POST** /ccm/api/anomaly/summary | List Anomalies
*CloudCostAnomaliesApi* | [**list_anomalies**](docs/CloudCostAnomaliesApi.md#list_anomalies) | **POST** /ccm/api/anomaly | List Anomalies
*CloudCostAnomaliesApi* | [**list_perspective_anomalies**](docs/CloudCostAnomaliesApi.md#list_perspective_anomalies) | **POST** /ccm/api/anomaly/perspective/{perspectiveId} | List Anomalies for Perspective
*CloudCostAnomaliesApi* | [**report_anomaly_feedback**](docs/CloudCostAnomaliesApi.md#report_anomaly_feedback) | **PUT** /ccm/api/anomaly/feedback | Report Anomaly feedback
*CloudCostAutoStoppingFixedSchedulesApi* | [**create_auto_stopping_schedules**](docs/CloudCostAutoStoppingFixedSchedulesApi.md#create_auto_stopping_schedules) | **POST** /gateway/lw/api/accounts/{account_id}/schedules | Create a fixed schedule for an AutoStopping Rule
*CloudCostAutoStoppingFixedSchedulesApi* | [**delete_auto_stopping_schedule**](docs/CloudCostAutoStoppingFixedSchedulesApi.md#delete_auto_stopping_schedule) | **DELETE** /gateway/lw/api/accounts/{account_id}/schedules/{schedule_id} | Delete a fixed schedule for AutoStopping Rule.
*CloudCostAutoStoppingFixedSchedulesApi* | [**list_auto_stopping_schedules**](docs/CloudCostAutoStoppingFixedSchedulesApi.md#list_auto_stopping_schedules) | **GET** /gateway/lw/api/accounts/{account_id}/schedules | Return all the AutoStopping Rule fixed schedules
*CloudCostAutoStoppingLoadBalancersApi* | [**access_point_rules**](docs/CloudCostAutoStoppingLoadBalancersApi.md#access_point_rules) | **GET** /gateway/lw/api/accounts/{account_id}/autostopping/loadbalancers/{lb_id}/rules | Return all the AutoStopping Rules in a load balancer
*CloudCostAutoStoppingLoadBalancersApi* | [**create_load_balancer**](docs/CloudCostAutoStoppingLoadBalancersApi.md#create_load_balancer) | **POST** /gateway/lw/api/accounts/{account_id}/autostopping/loadbalancers | Create a load balancer
*CloudCostAutoStoppingLoadBalancersApi* | [**delete_load_balancer**](docs/CloudCostAutoStoppingLoadBalancersApi.md#delete_load_balancer) | **DELETE** /gateway/lw/api/accounts/{account_id}/autostopping/loadbalancers | Delete load balancers and the associated resources
*CloudCostAutoStoppingLoadBalancersApi* | [**describe_load_balancer**](docs/CloudCostAutoStoppingLoadBalancersApi.md#describe_load_balancer) | **GET** /gateway/lw/api/accounts/{account_id}/autostopping/loadbalancers/{lb_id} | Return details of a load balancer
*CloudCostAutoStoppingLoadBalancersApi* | [**edit_load_balancer**](docs/CloudCostAutoStoppingLoadBalancersApi.md#edit_load_balancer) | **PUT** /gateway/lw/api/accounts/{account_id}/autostopping/loadbalancers | Update a load balancer
*CloudCostAutoStoppingLoadBalancersApi* | [**list_load_balancers**](docs/CloudCostAutoStoppingLoadBalancersApi.md#list_load_balancers) | **GET** /gateway/lw/api/accounts/{account_id}/autostopping/loadbalancers | Return all the load balancers
*CloudCostAutoStoppingLoadBalancersApi* | [**load_balancer_activity**](docs/CloudCostAutoStoppingLoadBalancersApi.md#load_balancer_activity) | **GET** /gateway/lw/api/accounts/{account_id}/autostopping/loadbalancers/{lb_id}/last_active_at | Return last activity details of a load balancer
*CloudCostAutoStoppingRulesApi* | [**all_auto_stopping_resources**](docs/CloudCostAutoStoppingRulesApi.md#all_auto_stopping_resources) | **GET** /gateway/lw/api/accounts/{account_id}/autostopping/rules/{rule_id}/resources | List all the resources for an AutoStopping Rule
*CloudCostAutoStoppingRulesApi* | [**auto_stopping_rule_details**](docs/CloudCostAutoStoppingRulesApi.md#auto_stopping_rule_details) | **GET** /gateway/lw/api/accounts/{account_id}/autostopping/rules/{rule_id} | Return AutoStopping Rule details
*CloudCostAutoStoppingRulesApi* | [**cool_down_autostopping_rule**](docs/CloudCostAutoStoppingRulesApi.md#cool_down_autostopping_rule) | **POST** /gateway/lw/api/accounts/{account_id}/autostopping/rules/{rule_id}/cooldown | Cool down an AutoStopping Rule
*CloudCostAutoStoppingRulesApi* | [**cumulative_auto_stopping_savings**](docs/CloudCostAutoStoppingRulesApi.md#cumulative_auto_stopping_savings) | **GET** /gateway/lw/api/accounts/{account_id}/autostopping/rules/savings/cumulative | Return cumulative savings for all the AutoStopping Rules
*CloudCostAutoStoppingRulesApi* | [**delete_auto_stopping_rule**](docs/CloudCostAutoStoppingRulesApi.md#delete_auto_stopping_rule) | **DELETE** /gateway/lw/api/accounts/{account_id}/autostopping/rules/{rule_id} | Delete an AutoStopping Rule
*CloudCostAutoStoppingRulesApi* | [**get_auto_stopping_cool_down_meta**](docs/CloudCostAutoStoppingRulesApi.md#get_auto_stopping_cool_down_meta) | **GET** /gateway/lw/api/accounts/{account_id}/autostopping/rules/{rule_id}/cooldown_meta | Return metadata of cool down of an AutoStopping Rule
*CloudCostAutoStoppingRulesApi* | [**get_auto_stopping_diagnostics**](docs/CloudCostAutoStoppingRulesApi.md#get_auto_stopping_diagnostics) | **GET** /gateway/lw/api/accounts/{account_id}/autostopping/rules/{rule_id}/diagnostics | Return diagnostics result of an AutoStopping Rule
*CloudCostAutoStoppingRulesApi* | [**health_of_auto_stopping_rule**](docs/CloudCostAutoStoppingRulesApi.md#health_of_auto_stopping_rule) | **GET** /gateway/lw/api/accounts/{account_id}/autostopping/rules/{rule_id}/health | Return health status of an AutoStopping Rule
*CloudCostAutoStoppingRulesApi* | [**list_auto_stopping_rules**](docs/CloudCostAutoStoppingRulesApi.md#list_auto_stopping_rules) | **GET** /gateway/lw/api/accounts/{account_id}/autostopping/rules | List AutoStopping Rules
*CloudCostAutoStoppingRulesApi* | [**savings_from_auto_stopping_rule**](docs/CloudCostAutoStoppingRulesApi.md#savings_from_auto_stopping_rule) | **GET** /gateway/lw/api/accounts/{account_id}/autostopping/rules/{rule_id}/savings | Return savings details for an AutoStopping Rule
*CloudCostAutoStoppingRulesApi* | [**toggle_autostopping_rule**](docs/CloudCostAutoStoppingRulesApi.md#toggle_autostopping_rule) | **PUT** /gateway/lw/api/accounts/{account_id}/autostopping/rules/{rule_id}/toggle_state | Disable/Enable an Autostopping Rule
*CloudCostAutoStoppingRulesApi* | [**update_auto_stopping_rule**](docs/CloudCostAutoStoppingRulesApi.md#update_auto_stopping_rule) | **POST** /gateway/lw/api/accounts/{account_id}/autostopping/rules | Create an AutoStopping Rule
*CloudCostAutoStoppingRulesV2Api* | [**create_auto_stopping_rule_v2**](docs/CloudCostAutoStoppingRulesV2Api.md#create_auto_stopping_rule_v2) | **POST** /gateway/lw/api/accounts/{account_id}/autostopping/v2/rules | Create an AutoStopping Rule
*CloudCostAutoStoppingRulesV2Api* | [**update_auto_stopping_rule_v2**](docs/CloudCostAutoStoppingRulesV2Api.md#update_auto_stopping_rule_v2) | **PUT** /gateway/lw/api/accounts/{account_id}/autostopping/v2/rules/{rule_id} | Update an existing AutoStopping Rule
*CloudCostBIDashboardsApi* | [**list_bi_dashboards**](docs/CloudCostBIDashboardsApi.md#list_bi_dashboards) | **GET** /ccm/api/bi-dashboards | List all the BI Dashboards for CCM
*CloudCostBudgetGroupsApi* | [**create_budget_group**](docs/CloudCostBudgetGroupsApi.md#create_budget_group) | **POST** /ccm/api/budgetGroups | Create a Budget Group
*CloudCostBudgetGroupsApi* | [**delete_budget_group**](docs/CloudCostBudgetGroupsApi.md#delete_budget_group) | **DELETE** /ccm/api/budgetGroups/{id} | Delete a budget group
*CloudCostBudgetGroupsApi* | [**get_budget_and_budget_groups_list**](docs/CloudCostBudgetGroupsApi.md#get_budget_and_budget_groups_list) | **GET** /ccm/api/budgetGroups/summary | Get list of budget and budget group summaries
*CloudCostBudgetGroupsApi* | [**get_budget_group**](docs/CloudCostBudgetGroupsApi.md#get_budget_group) | **GET** /ccm/api/budgetGroups/{id} | Fetch Budget group details
*CloudCostBudgetGroupsApi* | [**get_last_period_cost**](docs/CloudCostBudgetGroupsApi.md#get_last_period_cost) | **POST** /ccm/api/budgetGroups/aggregatedAmount | Get aggregated amount for given budget groups/budgets
*CloudCostBudgetGroupsApi* | [**list_budget_groups**](docs/CloudCostBudgetGroupsApi.md#list_budget_groups) | **GET** /ccm/api/budgetGroups | List all the Budget groups
*CloudCostBudgetGroupsApi* | [**update_budget_group**](docs/CloudCostBudgetGroupsApi.md#update_budget_group) | **PUT** /ccm/api/budgetGroups/{id} | Update an existing budget group
*CloudCostBudgetsApi* | [**clone_budget**](docs/CloudCostBudgetsApi.md#clone_budget) | **POST** /ccm/api/budgets/{id} | Clone a budget
*CloudCostBudgetsApi* | [**create_budget**](docs/CloudCostBudgetsApi.md#create_budget) | **POST** /ccm/api/budgets | Create a Budget
*CloudCostBudgetsApi* | [**delete_budget**](docs/CloudCostBudgetsApi.md#delete_budget) | **DELETE** /ccm/api/budgets/{id} | Delete a budget
*CloudCostBudgetsApi* | [**get_budget**](docs/CloudCostBudgetsApi.md#get_budget) | **GET** /ccm/api/budgets/{id} | Fetch Budget details
*CloudCostBudgetsApi* | [**get_cost_details**](docs/CloudCostBudgetsApi.md#get_cost_details) | **GET** /ccm/api/budgets/{id}/costDetails | Fetch the cost details of a Budget
*CloudCostBudgetsApi* | [**list_budgets**](docs/CloudCostBudgetsApi.md#list_budgets) | **GET** /ccm/api/budgets | List all the Budgets
*CloudCostBudgetsApi* | [**list_budgets_for_perspective**](docs/CloudCostBudgetsApi.md#list_budgets_for_perspective) | **GET** /ccm/api/budgets/perspectiveBudgets | List all the Budgets associated with a Perspective
*CloudCostBudgetsApi* | [**update_budget**](docs/CloudCostBudgetsApi.md#update_budget) | **PUT** /ccm/api/budgets/{id} | Update an existing budget
*CloudCostCostCategoriesApi* | [**create_business_mapping**](docs/CloudCostCostCategoriesApi.md#create_business_mapping) | **POST** /ccm/api/business-mapping | Create Cost category
*CloudCostCostCategoriesApi* | [**delete_business_mapping**](docs/CloudCostCostCategoriesApi.md#delete_business_mapping) | **DELETE** /ccm/api/business-mapping/{id} | Delete a Cost category
*CloudCostCostCategoriesApi* | [**get_business_mapping**](docs/CloudCostCostCategoriesApi.md#get_business_mapping) | **GET** /ccm/api/business-mapping/{id} | Fetch details of a Cost category
*CloudCostCostCategoriesApi* | [**get_business_mapping_list**](docs/CloudCostCostCategoriesApi.md#get_business_mapping_list) | **GET** /ccm/api/business-mapping | Return details of all the Cost categories
*CloudCostCostCategoriesApi* | [**update_business_mapping**](docs/CloudCostCostCategoriesApi.md#update_business_mapping) | **PUT** /ccm/api/business-mapping | Update a Cost category
*CloudCostDetailsApi* | [**cluster_data**](docs/CloudCostDetailsApi.md#cluster_data) | **POST** /ccm/api/costdetails/clusterData | Returns cluster data in a tabular format
*CloudCostDetailsApi* | [**costdetailoverview**](docs/CloudCostDetailsApi.md#costdetailoverview) | **POST** /ccm/api/costdetails/overview | Returns an overview of the cost
*CloudCostDetailsApi* | [**costdetailtabular**](docs/CloudCostDetailsApi.md#costdetailtabular) | **POST** /ccm/api/costdetails/tabularformat | Returns cost details in a tabular format
*CloudCostDetailsApi* | [**costdetailttimeseries**](docs/CloudCostDetailsApi.md#costdetailttimeseries) | **POST** /ccm/api/costdetails/timeseriesformat | Returns cost details in a time series format
*CloudCostK8SConnectorsMetadataApi* | [**ccm_k8s_meta**](docs/CloudCostK8SConnectorsMetadataApi.md#ccm_k8s_meta) | **POST** /ccm/api/ccmK8sMeta | Get CCM K8S Metadata
*CloudCostOverviewApi* | [**get_ccm_overview**](docs/CloudCostOverviewApi.md#get_ccm_overview) | **GET** /ccm/api/overview | Fetch high level overview details about CCM feature.
*CloudCostPerspectiveReportsApi* | [**create_report_setting**](docs/CloudCostPerspectiveReportsApi.md#create_report_setting) | **POST** /ccm/api/perspectiveReport/{accountIdentifier} | Create a schedule for a Report
*CloudCostPerspectiveReportsApi* | [**delete_report_setting**](docs/CloudCostPerspectiveReportsApi.md#delete_report_setting) | **DELETE** /ccm/api/perspectiveReport/{accountIdentifier} | Delete cost Perspective report
*CloudCostPerspectiveReportsApi* | [**get_report_setting**](docs/CloudCostPerspectiveReportsApi.md#get_report_setting) | **GET** /ccm/api/perspectiveReport/{accountIdentifier} | Fetch details of a cost Report
*CloudCostPerspectiveReportsApi* | [**update_report_setting**](docs/CloudCostPerspectiveReportsApi.md#update_report_setting) | **PUT** /ccm/api/perspectiveReport/{accountIdentifier} | Update a cost Perspective Report
*CloudCostPerspectivesApi* | [**create_perspective**](docs/CloudCostPerspectivesApi.md#create_perspective) | **POST** /ccm/api/perspective | Create a Perspective
*CloudCostPerspectivesApi* | [**delete_perspective**](docs/CloudCostPerspectivesApi.md#delete_perspective) | **DELETE** /ccm/api/perspective | Delete a Perspective
*CloudCostPerspectivesApi* | [**get_all_perspectives**](docs/CloudCostPerspectivesApi.md#get_all_perspectives) | **GET** /ccm/api/perspective/getAllPerspectives | Return details of all the Perspectives
*CloudCostPerspectivesApi* | [**get_last_period_cost1**](docs/CloudCostPerspectivesApi.md#get_last_period_cost1) | **GET** /ccm/api/perspective/lastPeriodCost | Get the last period cost for a Perspective
*CloudCostPerspectivesApi* | [**get_last_year_monthly_cost**](docs/CloudCostPerspectivesApi.md#get_last_year_monthly_cost) | **GET** /ccm/api/perspective/lastYearMonthlyCost | Get the last twelve month cost for a Perspective
*CloudCostPerspectivesApi* | [**get_perspective**](docs/CloudCostPerspectivesApi.md#get_perspective) | **GET** /ccm/api/perspective | Fetch details of a Perspective
*CloudCostPerspectivesApi* | [**update_perspective**](docs/CloudCostPerspectivesApi.md#update_perspective) | **PUT** /ccm/api/perspective | Update a Perspective
*CloudCostPerspectivesFoldersApi* | [**create_perspective_folder**](docs/CloudCostPerspectivesFoldersApi.md#create_perspective_folder) | **POST** /ccm/api/perspectiveFolders/create | Create a Perspective folder
*CloudCostPerspectivesFoldersApi* | [**delete_folder**](docs/CloudCostPerspectivesFoldersApi.md#delete_folder) | **DELETE** /ccm/api/perspectiveFolders/{folderId} | Delete a folder
*CloudCostPerspectivesFoldersApi* | [**get_all_folder_perspectives**](docs/CloudCostPerspectivesFoldersApi.md#get_all_folder_perspectives) | **GET** /ccm/api/perspectiveFolders/{folderId}/perspectives | Return details of all the Perspectives
*CloudCostPerspectivesFoldersApi* | [**get_folders**](docs/CloudCostPerspectivesFoldersApi.md#get_folders) | **GET** /ccm/api/perspectiveFolders | Fetch folders for an account
*CloudCostPerspectivesFoldersApi* | [**move_perspectives**](docs/CloudCostPerspectivesFoldersApi.md#move_perspectives) | **POST** /ccm/api/perspectiveFolders/movePerspectives | Move a Perspective
*CloudCostPerspectivesFoldersApi* | [**update_folder**](docs/CloudCostPerspectivesFoldersApi.md#update_folder) | **PUT** /ccm/api/perspectiveFolders | Update a folder
*CloudCostRecommendationIgnoreListApi* | [**add_recommendations_ignore_list**](docs/CloudCostRecommendationIgnoreListApi.md#add_recommendations_ignore_list) | **POST** /ccm/api/recommendation/ignore-list/add | Add resources to recommendations ignore list
*CloudCostRecommendationIgnoreListApi* | [**get_recommendations_ignore_list**](docs/CloudCostRecommendationIgnoreListApi.md#get_recommendations_ignore_list) | **GET** /ccm/api/recommendation/ignore-list | Get resources in recommendations ignore list
*CloudCostRecommendationIgnoreListApi* | [**remove_recommendations_ignore_list**](docs/CloudCostRecommendationIgnoreListApi.md#remove_recommendations_ignore_list) | **POST** /ccm/api/recommendation/ignore-list/remove | Remove resources from recommendations ignore list
*CloudCostRecommendationJiraApi* | [**create_recommendation_jira**](docs/CloudCostRecommendationJiraApi.md#create_recommendation_jira) | **POST** /ccm/api/recommendation/jira/create | Create jira for recommendation
*CloudCostRecommendationServicenowApi* | [**create_recommendation_servicenow_ticket**](docs/CloudCostRecommendationServicenowApi.md#create_recommendation_servicenow_ticket) | **POST** /ccm/api/recommendation/servicenow/create | Create servicenow ticket for recommendation
*CloudCostRecommendationsApi* | [**change_recommendation_state**](docs/CloudCostRecommendationsApi.md#change_recommendation_state) | **POST** /ccm/api/recommendation/overview/change-state | Return void
*CloudCostRecommendationsApi* | [**list_recommendations**](docs/CloudCostRecommendationsApi.md#list_recommendations) | **POST** /ccm/api/recommendation/overview/list | Return the list of Recommendations
*CloudCostRecommendationsApi* | [**recommendation_filter_values**](docs/CloudCostRecommendationsApi.md#recommendation_filter_values) | **POST** /ccm/api/recommendation/overview/filter-values | Return the list of filter values for the Recommendations
*CloudCostRecommendationsApi* | [**recommendation_stats**](docs/CloudCostRecommendationsApi.md#recommendation_stats) | **POST** /ccm/api/recommendation/overview/stats | Return Recommendations statistics
*CloudCostRecommendationsApi* | [**recommendations_count**](docs/CloudCostRecommendationsApi.md#recommendations_count) | **POST** /ccm/api/recommendation/overview/count | Return the number of Recommendations
*CloudCostRecommendationsDetailsApi* | [**azure_vm_recommendation_detail**](docs/CloudCostRecommendationsDetailsApi.md#azure_vm_recommendation_detail) | **GET** /ccm/api/recommendation/details/azure-vm | Return Azure VM Recommendation
*CloudCostRecommendationsDetailsApi* | [**ec2_recommendation_detail**](docs/CloudCostRecommendationsDetailsApi.md#ec2_recommendation_detail) | **GET** /ccm/api/recommendation/details/ec2-instance | Return EC2 Recommendation
*CloudCostRecommendationsDetailsApi* | [**ecs_recommendation_detail**](docs/CloudCostRecommendationsDetailsApi.md#ecs_recommendation_detail) | **GET** /ccm/api/recommendation/details/ecs-service | Return ECS Recommendation
*CloudCostRecommendationsDetailsApi* | [**node_recommendation_detail**](docs/CloudCostRecommendationsDetailsApi.md#node_recommendation_detail) | **GET** /ccm/api/recommendation/details/node-pool | Return node pool Recommendation
*CloudCostRecommendationsDetailsApi* | [**workload_recommendation_detail**](docs/CloudCostRecommendationsDetailsApi.md#workload_recommendation_detail) | **GET** /ccm/api/recommendation/details/workload | Return workload Recommendation
*ClustersApi* | [**agent_cluster_service_create**](docs/ClustersApi.md#agent_cluster_service_create) | **POST** /gitops/api/v1/agents/{agentIdentifier}/clusters | Create creates a cluster
*ClustersApi* | [**agent_cluster_service_delete**](docs/ClustersApi.md#agent_cluster_service_delete) | **DELETE** /gitops/api/v1/agents/{agentIdentifier}/clusters/{identifier} | Delete deletes a cluster
*ClustersApi* | [**agent_cluster_service_get**](docs/ClustersApi.md#agent_cluster_service_get) | **GET** /gitops/api/v1/agents/{agentIdentifier}/clusters/{identifier} | Get returns a cluster by identifier
*ClustersApi* | [**agent_cluster_service_list**](docs/ClustersApi.md#agent_cluster_service_list) | **GET** /gitops/api/v1/agents/{agentIdentifier}/clusters | List returns list of clusters
*ClustersApi* | [**agent_cluster_service_update**](docs/ClustersApi.md#agent_cluster_service_update) | **PUT** /gitops/api/v1/agents/{agentIdentifier}/clusters/{identifier} | Update updates a cluster
*ClustersApi* | [**agent_gpg_key_service_list**](docs/ClustersApi.md#agent_gpg_key_service_list) | **GET** /gitops/api/v1/agents/{agentIdentifier}/gpgkeys | List all available repository certificates
*ClustersApi* | [**cluster_service_exists**](docs/ClustersApi.md#cluster_service_exists) | **GET** /gitops/api/v1/clusters/exists | Checks for whether the cluster exists
*ClustersApi* | [**cluster_service_list_clusters**](docs/ClustersApi.md#cluster_service_list_clusters) | **POST** /gitops/api/v1/clusters | List returns list of Clusters
*ClustersApi* | [**delete_cluster**](docs/ClustersApi.md#delete_cluster) | **DELETE** /ng/api/gitops/clusters/{identifier} | Delete a Cluster by identifier
*ClustersApi* | [**get_cluster**](docs/ClustersApi.md#get_cluster) | **GET** /ng/api/gitops/clusters/{identifier} | Gets a Cluster by identifier
*ClustersApi* | [**get_cluster_list**](docs/ClustersApi.md#get_cluster_list) | **GET** /ng/api/gitops/clusters | Gets cluster list
*ClustersApi* | [**link_cluster**](docs/ClustersApi.md#link_cluster) | **POST** /ng/api/gitops/clusters | link a Cluster
*ClustersApi* | [**link_clusters**](docs/ClustersApi.md#link_clusters) | **POST** /ng/api/gitops/clusters/batch | Link Clusters
*ClustersApi* | [**unlink_clusters_in_batch**](docs/ClustersApi.md#unlink_clusters_in_batch) | **POST** /ng/api/gitops/clusters/batchunlink | Unlink Clusters
*CommitmentOrchestratorAPIsApi* | [**event_logs**](docs/CommitmentOrchestratorAPIsApi.md#event_logs) | **POST** /gateway/lw/api/accounts/{account_id}/v1/events/logs | List event logs
*CommitmentOrchestratorEventsAPIsApi* | [**events_chart**](docs/CommitmentOrchestratorEventsAPIsApi.md#events_chart) | **POST** /gateway/lw/api/accounts/{account_id}/v1/events/chart | List event logs
*CommitmentOrchestratorSetupAPIsApi* | [**list_masters**](docs/CommitmentOrchestratorSetupAPIsApi.md#list_masters) | **POST** /gateway/lw/api/accounts/{account_id}/v1/setup/listMasterAccounts | List master accounts for commitment Setup
*CommitmentOrchestratorSetupAPIsApi* | [**list_setups**](docs/CommitmentOrchestratorSetupAPIsApi.md#list_setups) | **GET** /gateway/lw/api/accounts/{account_id}/v1/setup/list | List of commitment Setups
*CommitmentOrchestratorSetupAPIsApi* | [**setup_validate**](docs/CommitmentOrchestratorSetupAPIsApi.md#setup_validate) | **POST** /gateway/lw/api/accounts/{account_id}/v1/setup/validate | Validate commitment Setup
*ConnectorsApi* | [**create_connector**](docs/ConnectorsApi.md#create_connector) | **POST** /ng/api/connectors | Create a Connector
*ConnectorsApi* | [**delete_connector**](docs/ConnectorsApi.md#delete_connector) | **DELETE** /ng/api/connectors/{identifier} | Delete a Connector
*ConnectorsApi* | [**get_all_allowed_field_values**](docs/ConnectorsApi.md#get_all_allowed_field_values) | **GET** /ng/api/connectors/fieldValues | List all the configured field values for the given Connector type.
*ConnectorsApi* | [**get_ccmk8_s_connector_list**](docs/ConnectorsApi.md#get_ccmk8_s_connector_list) | **POST** /ng/api/connectors/ccmK8sList | Fetches the list of CMC K8S Connectors corresponding to the request&#x27;s filter criteria.
*ConnectorsApi* | [**get_ce_aws_template**](docs/ConnectorsApi.md#get_ce_aws_template) | **POST** /ng/api/connectors/getceawstemplateurl | Get the Template URL of connector
*ConnectorsApi* | [**get_connector**](docs/ConnectorsApi.md#get_connector) | **GET** /ng/api/connectors/{identifier} | Return Connector details
*ConnectorsApi* | [**get_connector_catalogue**](docs/ConnectorsApi.md#get_connector_catalogue) | **GET** /ng/api/connectors/catalogue | Lists all Connectors for an account
*ConnectorsApi* | [**get_connector_list**](docs/ConnectorsApi.md#get_connector_list) | **GET** /ng/api/connectors | List all Connectors using filters
*ConnectorsApi* | [**get_connector_list_v2**](docs/ConnectorsApi.md#get_connector_list_v2) | **POST** /ng/api/connectors/listV2 | Fetches the list of Connectors corresponding to the request&#x27;s filter criteria.
*ConnectorsApi* | [**get_connector_statistics**](docs/ConnectorsApi.md#get_connector_statistics) | **GET** /ng/api/connectors/stats | Gets the connector&#x27;s statistics by Account Identifier, Project Identifier and Organization Identifier
*ConnectorsApi* | [**get_test_connection_result**](docs/ConnectorsApi.md#get_test_connection_result) | **POST** /ng/api/connectors/testConnection/{identifier} | Test Harness Connector connection with third-party tool
*ConnectorsApi* | [**get_test_git_repo_connection_result**](docs/ConnectorsApi.md#get_test_git_repo_connection_result) | **POST** /ng/api/connectors/testGitRepoConnection/{identifier} | Test Git Connector sync with repo
*ConnectorsApi* | [**list_connector_by_fqn**](docs/ConnectorsApi.md#list_connector_by_fqn) | **POST** /ng/api/connectors/listbyfqn | Get list of Connectors by FQN
*ConnectorsApi* | [**update_connector**](docs/ConnectorsApi.md#update_connector) | **PUT** /ng/api/connectors | Update a Connector
*ConnectorsApi* | [**validate_the_identifier_is_unique**](docs/ConnectorsApi.md#validate_the_identifier_is_unique) | **GET** /ng/api/connectors/validateUniqueIdentifier | Test a Harness Connector
*CustomDeploymentApi* | [**get_custom_deployment_entity_references**](docs/CustomDeploymentApi.md#get_custom_deployment_entity_references) | **POST** /ng/api/customDeployment/get-references | Gets Custom Deployment Entity References
*CustomDeploymentApi* | [**get_custom_deployment_expression_variables**](docs/CustomDeploymentApi.md#get_custom_deployment_expression_variables) | **POST** /ng/api/customDeployment/expression-variables | Gets Custom Deployment Expression Variables
*CustomDeploymentApi* | [**get_custom_deployment_infra_variables**](docs/CustomDeploymentApi.md#get_custom_deployment_infra_variables) | **GET** /ng/api/customDeployment/variables/{templateIdentifier} | Gets Infra Variables from a Custom Deployment Template by identifier
*CustomDeploymentApi* | [**get_updated_yaml_for_infrastructure**](docs/CustomDeploymentApi.md#get_updated_yaml_for_infrastructure) | **POST** /ng/api/customDeployment/get-updated-Yaml/{infraIdentifier} | Return the updated yaml for infrastructure based on Deployment template
*CustomDeploymentApi* | [**validate_infrastructure_for_deployment_template**](docs/CustomDeploymentApi.md#validate_infrastructure_for_deployment_template) | **GET** /ng/api/customDeployment/validate-infrastructure/{infraIdentifier} | This validates whether Infrastructure is valid or not
*CustomDashboardsApi* | [**get_dashboard_data**](docs/CustomDashboardsApi.md#get_dashboard_data) | **GET** /dashboard/api/dashboards/{dashboard_id}/download | Download data within a Dashboard
*DashboardAggregatesApi* | [**dashboard_service_recent_deployments**](docs/DashboardAggregatesApi.md#dashboard_service_recent_deployments) | **POST** /gitops/api/v1/dashboard/activity | Returns aggregate statistics of recent deployments
*DashboardAggregatesApi* | [**dashboard_service_top_application_phase_stats**](docs/DashboardAggregatesApi.md#dashboard_service_top_application_phase_stats) | **GET** /gitops/api/v1/dashboard/topapps | List phase status counts for top 5 most deployed apps
*DashboardsApi* | [**dashboard_service_get_dashboard_overview**](docs/DashboardsApi.md#dashboard_service_get_dashboard_overview) | **GET** /gitops/api/v1/dashboard/overview | GetDashboradOverview gets dashboard overview
*DashboardsApi* | [**dashboard_service_recently_created_counts**](docs/DashboardsApi.md#dashboard_service_recently_created_counts) | **GET** /gitops/api/v1/dashboard/counts | List count of Cluster, Repos and Apps created within a time series
*DelegateDownloadResourceApi* | [**download_docker_delegate_yaml**](docs/DelegateDownloadResourceApi.md#download_docker_delegate_yaml) | **POST** /ng/api/download-delegates/docker | Downloads a docker delegate yaml file.
*DelegateDownloadResourceApi* | [**download_kubernetes_delegate_yaml**](docs/DelegateDownloadResourceApi.md#download_kubernetes_delegate_yaml) | **POST** /ng/api/download-delegates/kubernetes | Downloads a kubernetes delegate yaml file.
*DelegateGroupTagsResourceApi* | [**add_tags_to_delegate_group**](docs/DelegateGroupTagsResourceApi.md#add_tags_to_delegate_group) | **POST** /ng/api/delegate-group-tags/{groupIdentifier} | Add given list of tags to the Delegate group
*DelegateGroupTagsResourceApi* | [**delete_tags_from_delegate_group**](docs/DelegateGroupTagsResourceApi.md#delete_tags_from_delegate_group) | **DELETE** /ng/api/delegate-group-tags/{groupIdentifier} | Deletes all tags from the Delegate group
*DelegateGroupTagsResourceApi* | [**list_delegate_groups_using_tags**](docs/DelegateGroupTagsResourceApi.md#list_delegate_groups_using_tags) | **POST** /ng/api/delegate-group-tags/delegate-groups | List delegate groups that are having mentioned tags.
*DelegateGroupTagsResourceApi* | [**list_tags_for_delegate_group**](docs/DelegateGroupTagsResourceApi.md#list_tags_for_delegate_group) | **GET** /ng/api/delegate-group-tags/{groupIdentifier} | Retrieves list of tags attached with Delegate group
*DelegateGroupTagsResourceApi* | [**update_tags_of_delegate_group**](docs/DelegateGroupTagsResourceApi.md#update_tags_of_delegate_group) | **PUT** /ng/api/delegate-group-tags/{groupIdentifier} | Clears all existing tags with delegate group and attach given set of tags to delegate group.
*DelegateSetupResourceApi* | [**delete_delegate**](docs/DelegateSetupResourceApi.md#delete_delegate) | **DELETE** /ng/api/delegate-setup/delegate/{delegateIdentifier} | Deletes a Delegate by its identifier.
*DelegateSetupResourceApi* | [**generate_ng_helm_values_yaml**](docs/DelegateSetupResourceApi.md#generate_ng_helm_values_yaml) | **POST** /ng/api/delegate-setup/generate-helm-values | Generates helm values yaml file from the data specified in request body (Delegate setup details).
*DelegateSetupResourceApi* | [**generate_terraform_module**](docs/DelegateSetupResourceApi.md#generate_terraform_module) | **GET** /ng/api/delegate-setup/delegate-terraform-module-file | Generates delegate terraform example module file from the account
*DelegateSetupResourceApi* | [**list_delegates**](docs/DelegateSetupResourceApi.md#list_delegates) | **POST** /ng/api/delegate-setup/listDelegates | Lists all delegates in NG filtered by provided conditions
*DelegateSetupResourceApi* | [**override_delegate_image_tag**](docs/DelegateSetupResourceApi.md#override_delegate_image_tag) | **PUT** /ng/api/delegate-setup/override-delegate-tag | Overrides delegate image tag for account
*DelegateSetupResourceApi* | [**published_delegate_version**](docs/DelegateSetupResourceApi.md#published_delegate_version) | **GET** /ng/api/delegate-setup/latest-supported-version | Gets the latest supported delegate version. The version has YY.MM.XXXXX format. You can use any version lower than the returned results(upto 3 months old)
*DelegateTokenResourceApi* | [**create_delegate_token**](docs/DelegateTokenResourceApi.md#create_delegate_token) | **POST** /ng/api/delegate-token-ng | Creates Delegate Token.
*DelegateTokenResourceApi* | [**get_delegate_groups_using_token**](docs/DelegateTokenResourceApi.md#get_delegate_groups_using_token) | **GET** /ng/api/delegate-token-ng/delegate-groups | Lists delegate groups that are using the specified delegate token.
*DelegateTokenResourceApi* | [**get_delegate_tokens**](docs/DelegateTokenResourceApi.md#get_delegate_tokens) | **GET** /ng/api/delegate-token-ng | Retrieves Delegate Tokens by Account, Organization, Project and status.
*DelegateTokenResourceApi* | [**revoke_delegate_token**](docs/DelegateTokenResourceApi.md#revoke_delegate_token) | **PUT** /ng/api/delegate-token-ng | Revokes Delegate Token.
*DowntimeApi* | [**delete_downtime_data**](docs/DowntimeApi.md#delete_downtime_data) | **DELETE** /cv/api/account/{accountIdentifier}/org/{orgIdentifier}/project/{projectIdentifier}/downtime/identifier/{identifier} | 
*DowntimeApi* | [**get_associated_monitored_services**](docs/DowntimeApi.md#get_associated_monitored_services) | **GET** /cv/api/account/{accountIdentifier}/org/{orgIdentifier}/project/{projectIdentifier}/downtime/monitored-services/{identifier} | 
*DowntimeApi* | [**get_downtime**](docs/DowntimeApi.md#get_downtime) | **GET** /cv/api/account/{accountIdentifier}/org/{orgIdentifier}/project/{projectIdentifier}/downtime/identifier/{identifier} | 
*DowntimeApi* | [**get_downtime_associated_monitored_services**](docs/DowntimeApi.md#get_downtime_associated_monitored_services) | **GET** /cv/api/account/{accountIdentifier}/org/{orgIdentifier}/project/{projectIdentifier}/downtime/monitored-services | 
*DowntimeApi* | [**get_history**](docs/DowntimeApi.md#get_history) | **GET** /cv/api/account/{accountIdentifier}/org/{orgIdentifier}/project/{projectIdentifier}/downtime/history | 
*DowntimeApi* | [**list_downtimes**](docs/DowntimeApi.md#list_downtimes) | **GET** /cv/api/account/{accountIdentifier}/org/{orgIdentifier}/project/{projectIdentifier}/downtime/list | 
*DowntimeApi* | [**save_downtime**](docs/DowntimeApi.md#save_downtime) | **POST** /cv/api/account/{accountIdentifier}/org/{orgIdentifier}/project/{projectIdentifier}/downtime | 
*DowntimeApi* | [**update_downtime_data**](docs/DowntimeApi.md#update_downtime_data) | **PUT** /cv/api/account/{accountIdentifier}/org/{orgIdentifier}/project/{projectIdentifier}/downtime/identifier/{identifier} | 
*DowntimeApi* | [**update_downtime_enabled**](docs/DowntimeApi.md#update_downtime_enabled) | **PUT** /cv/api/account/{accountIdentifier}/org/{orgIdentifier}/project/{projectIdentifier}/downtime/flag/{identifier} | 
*EULAApi* | [**sign_eula**](docs/EULAApi.md#sign_eula) | **POST** /v1/eula/sign | Sign an End User License Agreement
*EULAApi* | [**validate_eula_sign**](docs/EULAApi.md#validate_eula_sign) | **GET** v1/eula/validate-sign | Validate specified agreement is signed or not
*EnvironmentGroupApi* | [**delete_environment_group**](docs/EnvironmentGroupApi.md#delete_environment_group) | **DELETE** /ng/api/environmentGroup/{envGroupIdentifier} | Delete en Environment Group by Identifier
*EnvironmentGroupApi* | [**get_environment_group**](docs/EnvironmentGroupApi.md#get_environment_group) | **GET** /ng/api/environmentGroup/{envGroupIdentifier} | Gets an Environment Group by identifier
*EnvironmentGroupApi* | [**get_environment_group_list**](docs/EnvironmentGroupApi.md#get_environment_group_list) | **POST** /ng/api/environmentGroup/list | Gets Environment Group list
*EnvironmentGroupApi* | [**post_environment_group**](docs/EnvironmentGroupApi.md#post_environment_group) | **POST** /ng/api/environmentGroup | Create an Environment Group
*EnvironmentGroupApi* | [**update_environment_group**](docs/EnvironmentGroupApi.md#update_environment_group) | **PUT** /ng/api/environmentGroup/{envGroupIdentifier} | Update an Environment Group by Identifier
*EnvironmentsApi* | [**create_environment_v2**](docs/EnvironmentsApi.md#create_environment_v2) | **POST** /ng/api/environmentsV2 | Create an Environment
*EnvironmentsApi* | [**delete_environment_v2**](docs/EnvironmentsApi.md#delete_environment_v2) | **DELETE** /ng/api/environmentsV2/{environmentIdentifier} | Delete an Environment by identifier
*EnvironmentsApi* | [**delete_service_override**](docs/EnvironmentsApi.md#delete_service_override) | **DELETE** /ng/api/environmentsV2/serviceOverrides | Delete a ServiceOverride entity
*EnvironmentsApi* | [**get_environment_access_list**](docs/EnvironmentsApi.md#get_environment_access_list) | **GET** /ng/api/environmentsV2/list/access | Gets Environment Access list
*EnvironmentsApi* | [**get_environment_list**](docs/EnvironmentsApi.md#get_environment_list) | **GET** /ng/api/environmentsV2 | Gets Environment list for a project
*EnvironmentsApi* | [**get_environment_v2**](docs/EnvironmentsApi.md#get_environment_v2) | **GET** /ng/api/environmentsV2/{environmentIdentifier} | Gets an Environment by identifier
*EnvironmentsApi* | [**get_service_overrides_list**](docs/EnvironmentsApi.md#get_service_overrides_list) | **GET** /ng/api/environmentsV2/serviceOverrides | Gets Service Overrides list
*EnvironmentsApi* | [**update_environment_v2**](docs/EnvironmentsApi.md#update_environment_v2) | **PUT** /ng/api/environmentsV2 | Update an Environment by identifier
*EnvironmentsApi* | [**upsert_environment_v2**](docs/EnvironmentsApi.md#upsert_environment_v2) | **PUT** /ng/api/environmentsV2/upsert | Upsert an Environment by identifier
*EnvironmentsApi* | [**upsert_service_override**](docs/EnvironmentsApi.md#upsert_service_override) | **POST** /ng/api/environmentsV2/serviceOverrides | upsert a Service Override for an Environment
*FeatureFlagsApi* | [**create_feature_flag**](docs/FeatureFlagsApi.md#create_feature_flag) | **POST** /cf/admin/features | Creates a Feature Flag
*FeatureFlagsApi* | [**delete_feature_flag**](docs/FeatureFlagsApi.md#delete_feature_flag) | **DELETE** /cf/admin/features/{identifier} | Delete a Feature Flag
*FeatureFlagsApi* | [**get_all_features**](docs/FeatureFlagsApi.md#get_all_features) | **GET** /cf/admin/features | Returns all Feature Flags for the project
*FeatureFlagsApi* | [**get_dependent_features**](docs/FeatureFlagsApi.md#get_dependent_features) | **GET** /cf/admin/features/{identifier}/dependants | Return a list of dependant flags
*FeatureFlagsApi* | [**get_feature_flag**](docs/FeatureFlagsApi.md#get_feature_flag) | **GET** /cf/admin/features/{identifier} | Returns a Feature Flag
*FeatureFlagsApi* | [**patch_feature**](docs/FeatureFlagsApi.md#patch_feature) | **PATCH** /cf/admin/features/{identifier} | Updates a Feature Flag
*FeatureFlagsApi* | [**restore_feature_flag**](docs/FeatureFlagsApi.md#restore_feature_flag) | **POST** /cf/admin/features/{identifier}/restore | Restore a Feature Flag
*FileStoreApi* | [**create**](docs/FileStoreApi.md#create) | **POST** /ng/api/file-store | Create Folder or File including content
*FileStoreApi* | [**create_via_yaml**](docs/FileStoreApi.md#create_via_yaml) | **POST** /ng/api/file-store/yaml | Creates File or Folder metadata via YAML
*FileStoreApi* | [**delete_file**](docs/FileStoreApi.md#delete_file) | **DELETE** /ng/api/file-store/{identifier} | Delete File or Folder by identifier
*FileStoreApi* | [**download_file**](docs/FileStoreApi.md#download_file) | **GET** /ng/api/file-store/files/{identifier}/download | Download File
*FileStoreApi* | [**get_created_by_list**](docs/FileStoreApi.md#get_created_by_list) | **GET** /ng/api/file-store/files/createdBy | Get list of created by user details
*FileStoreApi* | [**get_entity_types**](docs/FileStoreApi.md#get_entity_types) | **GET** /ng/api/file-store/supported-entity-types | Get the list of supported entity types for files
*FileStoreApi* | [**get_file**](docs/FileStoreApi.md#get_file) | **GET** /ng/api/file-store/{identifier} | Get the Folder or File metadata
*FileStoreApi* | [**get_file_content_using_scoped_file_path**](docs/FileStoreApi.md#get_file_content_using_scoped_file_path) | **GET** /ng/api/file-store/files/{scopedFilePath}/content | Get file content of scopedFilePath
*FileStoreApi* | [**get_folder_nodes**](docs/FileStoreApi.md#get_folder_nodes) | **POST** /ng/api/file-store/folder | Get folder nodes at first level, not including sub-nodes
*FileStoreApi* | [**get_referenced_by**](docs/FileStoreApi.md#get_referenced_by) | **GET** /ng/api/file-store/{identifier}/referenced-by | Get list of entities where file is referenced by queried entity type
*FileStoreApi* | [**list_files_and_folders**](docs/FileStoreApi.md#list_files_and_folders) | **GET** /ng/api/file-store | List Files and Folders metadata
*FileStoreApi* | [**list_files_with_filter**](docs/FileStoreApi.md#list_files_with_filter) | **POST** /ng/api/file-store/files/filter | Get filtered list of Files or Folders
*FileStoreApi* | [**update**](docs/FileStoreApi.md#update) | **PUT** /ng/api/file-store/{identifier} | Update Folder or File including content
*FileStoreApi* | [**update_via_yaml**](docs/FileStoreApi.md#update_via_yaml) | **PUT** /ng/api/file-store/yaml/{identifier} | Update File or Folder metadata via YAML
*FilterApi* | [**ccmdelete_filter**](docs/FilterApi.md#ccmdelete_filter) | **DELETE** /ccm/api/filters/{identifier} | Delete a Filter
*FilterApi* | [**ccmget_connector_list_v2**](docs/FilterApi.md#ccmget_connector_list_v2) | **GET** /ccm/api/filters | List Filters
*FilterApi* | [**ccmget_filter**](docs/FilterApi.md#ccmget_filter) | **GET** /ccm/api/filters/{identifier} | Return Filter Details
*FilterApi* | [**ccmpost_filter**](docs/FilterApi.md#ccmpost_filter) | **POST** /ccm/api/filters | Create a Filter
*FilterApi* | [**ccmupdate_filter**](docs/FilterApi.md#ccmupdate_filter) | **PUT** /ccm/api/filters | Update a Filter
*FilterApi* | [**delete_filter**](docs/FilterApi.md#delete_filter) | **DELETE** /ng/api/filters/{identifier} | Delete a Filter
*FilterApi* | [**get_connector_list_v21**](docs/FilterApi.md#get_connector_list_v21) | **GET** /ng/api/filters | List Filters
*FilterApi* | [**get_filter**](docs/FilterApi.md#get_filter) | **GET** /ng/api/filters/{identifier} | Return Filter Details
*FilterApi* | [**pipelinedelete_filter**](docs/FilterApi.md#pipelinedelete_filter) | **DELETE** /pipeline/api/filters/{identifier} | Delete a Filter
*FilterApi* | [**pipelineget_connector_list_v2**](docs/FilterApi.md#pipelineget_connector_list_v2) | **GET** /pipeline/api/filters | List Filters
*FilterApi* | [**pipelineget_filter**](docs/FilterApi.md#pipelineget_filter) | **GET** /pipeline/api/filters/{identifier} | Return Filter Details
*FilterApi* | [**pipelinepost_filter**](docs/FilterApi.md#pipelinepost_filter) | **POST** /pipeline/api/filters | Create a Filter
*FilterApi* | [**pipelineupdate_filter**](docs/FilterApi.md#pipelineupdate_filter) | **PUT** /pipeline/api/filters | Update a Filter
*FilterApi* | [**post_filter**](docs/FilterApi.md#post_filter) | **POST** /ng/api/filters | Create a Filter
*FilterApi* | [**templatedelete_filter**](docs/FilterApi.md#templatedelete_filter) | **DELETE** /template/api/filters/{identifier} | Delete a Filter
*FilterApi* | [**templateget_connector_list_v2**](docs/FilterApi.md#templateget_connector_list_v2) | **GET** /template/api/filters | List Filters
*FilterApi* | [**templateget_filter**](docs/FilterApi.md#templateget_filter) | **GET** /template/api/filters/{identifier} | Return Filter Details
*FilterApi* | [**templatepost_filter**](docs/FilterApi.md#templatepost_filter) | **POST** /template/api/filters | Create a Filter
*FilterApi* | [**templateupdate_filter**](docs/FilterApi.md#templateupdate_filter) | **PUT** /template/api/filters | Update a Filter
*FilterApi* | [**update_filter**](docs/FilterApi.md#update_filter) | **PUT** /ng/api/filters | Update a Filter
*FilterResourceGroupsApi* | [**filter_resource_groups**](docs/FilterResourceGroupsApi.md#filter_resource_groups) | **POST** /v1/resource-groups/filter | Filter Resource Groups
*FreezeCRUDApi* | [**create_freeze**](docs/FreezeCRUDApi.md#create_freeze) | **POST** /ng/api/freeze | Create a Freeze
*FreezeCRUDApi* | [**create_global_freeze**](docs/FreezeCRUDApi.md#create_global_freeze) | **POST** /ng/api/freeze/manageGlobalFreeze | Create Global Freeze
*FreezeCRUDApi* | [**delete_freeze**](docs/FreezeCRUDApi.md#delete_freeze) | **DELETE** /ng/api/freeze/{freezeIdentifier} | Delete a Freeze
*FreezeCRUDApi* | [**delete_many_freezes**](docs/FreezeCRUDApi.md#delete_many_freezes) | **POST** /ng/api/freeze/delete | Delete many Freezes
*FreezeCRUDApi* | [**get_freeze**](docs/FreezeCRUDApi.md#get_freeze) | **GET** /ng/api/freeze/{freezeIdentifier} | Get a Freeze
*FreezeCRUDApi* | [**get_freeze_list**](docs/FreezeCRUDApi.md#get_freeze_list) | **POST** /ng/api/freeze/list | Gets Freeze list
*FreezeCRUDApi* | [**get_frozen_execution_details**](docs/FreezeCRUDApi.md#get_frozen_execution_details) | **GET** /ng/api/freeze/getFrozenExecutionDetails | Get list of freeze acted on a frozen execution
*FreezeCRUDApi* | [**get_global_freeze**](docs/FreezeCRUDApi.md#get_global_freeze) | **GET** /ng/api/freeze/getGlobalFreeze | Get Global Freeze Yaml
*FreezeCRUDApi* | [**update_freeze**](docs/FreezeCRUDApi.md#update_freeze) | **PUT** /ng/api/freeze/{freezeIdentifier} | Updates a Freeze
*FreezeCRUDApi* | [**update_freeze_status**](docs/FreezeCRUDApi.md#update_freeze_status) | **POST** /ng/api/freeze/updateFreezeStatus | Update the status of Freeze to active or inactive
*GPGKeysApi* | [**gnu_pg_key_service_list_gpg_keys**](docs/GPGKeysApi.md#gnu_pg_key_service_list_gpg_keys) | **GET** /gitops/api/v1/gpgkeys | List all available repository certificates
*GitBranchesApi* | [**get_list_of_branches_with_status**](docs/GitBranchesApi.md#get_list_of_branches_with_status) | **GET** /ng/api/git-sync-branch/listBranchesWithStatus | Lists branches with their status(Synced, Unsynced) by Git Sync Config Id for the given scope
*GitBranchesApi* | [**sync_git_branch**](docs/GitBranchesApi.md#sync_git_branch) | **POST** /ng/api/git-sync-branch/sync | Sync the content of new Git Branch into harness with Git Sync Config Id
*GitFullSyncApi* | [**create_git_full_sync_config**](docs/GitFullSyncApi.md#create_git_full_sync_config) | **POST** /ng/api/git-full-sync/config | Create Configuration for Git Full Sync for the provided scope
*GitFullSyncApi* | [**get_git_full_sync_config**](docs/GitFullSyncApi.md#get_git_full_sync_config) | **GET** /ng/api/git-full-sync/config | Fetch Configuration for Git Full Sync for the provided scope
*GitFullSyncApi* | [**list_full_sync_files**](docs/GitFullSyncApi.md#list_full_sync_files) | **POST** /ng/api/git-full-sync/files | List files in full sync along with their status
*GitFullSyncApi* | [**trigger_full_sync**](docs/GitFullSyncApi.md#trigger_full_sync) | **POST** /ng/api/git-full-sync | Trigger Full Sync
*GitFullSyncApi* | [**update_git_full_sync_config**](docs/GitFullSyncApi.md#update_git_full_sync_config) | **PUT** /ng/api/git-full-sync/config | Update Configuration for Git Full Sync for the provided scope
*GitSyncApi* | [**create_git_sync_config**](docs/GitSyncApi.md#create_git_sync_config) | **POST** /ng/api/git-sync | Creates Git Sync Config in given scope
*GitSyncApi* | [**get_git_sync_config_list**](docs/GitSyncApi.md#get_git_sync_config_list) | **GET** /ng/api/git-sync | Lists Git Sync Config for the given scope
*GitSyncApi* | [**is_git_sync_enabled**](docs/GitSyncApi.md#is_git_sync_enabled) | **GET** /ng/api/git-sync/git-sync-enabled | Check whether Git Sync is enabled for given scope or not
*GitSyncApi* | [**update_default_folder**](docs/GitSyncApi.md#update_default_folder) | **PUT** /ng/api/git-sync/{identifier}/folder/{folderIdentifier}/default | Update existing Git Sync Config default root folder by Identifier
*GitSyncApi* | [**update_git_sync_config**](docs/GitSyncApi.md#update_git_sync_config) | **PUT** /ng/api/git-sync | Update existing Git Sync Config by Identifier
*GitSyncErrorsApi* | [**get_git_sync_errors_count**](docs/GitSyncErrorsApi.md#get_git_sync_errors_count) | **GET** /ng/api/git-sync-errors/count | Get Errors Count for the given scope, Repo and Branch
*GitSyncErrorsApi* | [**list_git_sync_errors**](docs/GitSyncErrorsApi.md#list_git_sync_errors) | **GET** /ng/api/git-sync-errors | Lists Git to Harness Errors by file or connectivity errors for the given scope, Repo and Branch
*GitSyncErrorsApi* | [**list_git_to_harness_error_for_commit**](docs/GitSyncErrorsApi.md#list_git_to_harness_error_for_commit) | **GET** /ng/api/git-sync-errors/commits/{commitId} | Lists Git to Harness Errors for the given Commit Id
*GitSyncErrorsApi* | [**list_git_to_harness_errors_grouped_by_commits**](docs/GitSyncErrorsApi.md#list_git_to_harness_errors_grouped_by_commits) | **GET** /ng/api/git-sync-errors/aggregate | Lists Git to Harness Errors grouped by Commits for the given scope, Repo and Branch
*GitSyncSettingsApi* | [**create_git_sync_setting**](docs/GitSyncSettingsApi.md#create_git_sync_setting) | **POST** /ng/api/git-sync-settings | Creates Git Sync Setting in a scope
*GitSyncSettingsApi* | [**get_git_sync_settings**](docs/GitSyncSettingsApi.md#get_git_sync_settings) | **GET** /ng/api/git-sync-settings | Get Git Sync Setting for the given scope
*GitSyncSettingsApi* | [**update_git_sync_setting**](docs/GitSyncSettingsApi.md#update_git_sync_setting) | **PUT** /ng/api/git-sync-settings | This updates the existing Git Sync settings within the scope. Only changing Connectivity Mode is allowed
*GlobalTemplatesApi* | [**get_global_template_input_set_yaml**](docs/GlobalTemplatesApi.md#get_global_template_input_set_yaml) | **GET** /template/api/globalTemplates/inputs/{globalTemplateIdentifier} | Gets Global Template Input Set YAML
*GnuPGPKeysApi* | [**agent_gpg_key_service_create**](docs/GnuPGPKeysApi.md#agent_gpg_key_service_create) | **POST** /gitops/api/v1/agents/{agentIdentifier}/gpgkeys | Create one or more GPG public keys in the server&#x27;s configuration
*GnuPGPKeysApi* | [**agent_gpg_key_service_delete**](docs/GnuPGPKeysApi.md#agent_gpg_key_service_delete) | **DELETE** /gitops/api/v1/agents/{agentIdentifier}/gpgkeys/{query.keyID} | Delete specified GPG public key from the server&#x27;s configuration
*GnuPGPKeysApi* | [**agent_gpg_key_service_get**](docs/GnuPGPKeysApi.md#agent_gpg_key_service_get) | **GET** /gitops/api/v1/agents/{agentIdentifier}/gpgkeys/{query.keyID} | Get information about specified GPG public key from the server
*GoogleSecretManagerConnectorApi* | [**get_gcp_regions**](docs/GoogleSecretManagerConnectorApi.md#get_gcp_regions) | **GET** /ng/api/google-secret-manager-connector/gcp-regions | Get list of GCP Regions
*HarnessResourceGroupApi* | [**create_resource_group_v2**](docs/HarnessResourceGroupApi.md#create_resource_group_v2) | **POST** /resourcegroup/api/v2/resourcegroup | Create Resource Group
*HarnessResourceGroupApi* | [**delete_resource_group_v2**](docs/HarnessResourceGroupApi.md#delete_resource_group_v2) | **DELETE** /resourcegroup/api/v2/resourcegroup/{identifier} | Delete Resource Group
*HarnessResourceGroupApi* | [**get_filter_resource_group_list_v2**](docs/HarnessResourceGroupApi.md#get_filter_resource_group_list_v2) | **POST** /resourcegroup/api/v2/resourcegroup/filter | List Resource Groups by filter
*HarnessResourceGroupApi* | [**get_resource_group_list_v2**](docs/HarnessResourceGroupApi.md#get_resource_group_list_v2) | **GET** /resourcegroup/api/v2/resourcegroup | List Resource Groups
*HarnessResourceGroupApi* | [**get_resource_group_v2**](docs/HarnessResourceGroupApi.md#get_resource_group_v2) | **GET** /resourcegroup/api/v2/resourcegroup/{identifier} | Get Resource Group
*HarnessResourceGroupApi* | [**update_resource_group_v2**](docs/HarnessResourceGroupApi.md#update_resource_group_v2) | **PUT** /resourcegroup/api/v2/resourcegroup/{identifier} | Update Resource Group
*HarnessResourceTypeApi* | [**get_resource_types**](docs/HarnessResourceTypeApi.md#get_resource_types) | **GET** /resourcegroup/api/resourcetype | Gets all resource types available at this scope
*HostsApi* | [**filter_hosts_by_connector**](docs/HostsApi.md#filter_hosts_by_connector) | **POST** /ng/api/hosts/filter | Gets the list of hosts filtered by accountIdentifier and connectorIdentifier
*HostsApi* | [**validate_hosts1**](docs/HostsApi.md#validate_hosts1) | **POST** /ng/api/hosts/validate | Validates hosts connectivity credentials
*IPAllowlistApi* | [**create_ip_allowlist_config**](docs/IPAllowlistApi.md#create_ip_allowlist_config) | **POST** /v1/ip-allowlist | Create a IP Allowlist config
*IPAllowlistApi* | [**delete_ip_allowlist_config**](docs/IPAllowlistApi.md#delete_ip_allowlist_config) | **DELETE** /v1/ip-allowlist/{ip-config-identifier} | Delete an IP Allowlist config
*IPAllowlistApi* | [**get_ip_allowlist_config**](docs/IPAllowlistApi.md#get_ip_allowlist_config) | **GET** /v1/ip-allowlist/{ip-config-identifier} | Retrieve a IP Allowlist config
*IPAllowlistApi* | [**get_ip_allowlist_configs**](docs/IPAllowlistApi.md#get_ip_allowlist_configs) | **GET** /v1/ip-allowlist | List IP Allowlist Configs
*IPAllowlistApi* | [**update_ip_allowlist_config**](docs/IPAllowlistApi.md#update_ip_allowlist_config) | **PUT** /v1/ip-allowlist/{ip-config-identifier} | Update IP Allowlist config
*IPAllowlistApi* | [**validate_ip_address_allowlisted_or_not**](docs/IPAllowlistApi.md#validate_ip_address_allowlisted_or_not) | **GET** /v1/ip-allowlist/validate/ip-address | Validate IP address lies in a specified range or not
*IPAllowlistApi* | [**validate_unique_ip_allowlist_config_identifier**](docs/IPAllowlistApi.md#validate_unique_ip_allowlist_config_identifier) | **GET** /v1/ip-allowlist/validate-unique-identifier/{ip-config-identifier} | Validate unique IP Allowlist config identifier
*InfrastructuresApi* | [**create_infrastructure**](docs/InfrastructuresApi.md#create_infrastructure) | **POST** /ng/api/infrastructures | Create an Infrastructure in an Environment
*InfrastructuresApi* | [**delete_infrastructure**](docs/InfrastructuresApi.md#delete_infrastructure) | **DELETE** /ng/api/infrastructures/{infraIdentifier} | Delete an Infrastructure by identifier
*InfrastructuresApi* | [**get_infrastructure**](docs/InfrastructuresApi.md#get_infrastructure) | **GET** /ng/api/infrastructures/{infraIdentifier} | Gets an Infrastructure by identifier
*InfrastructuresApi* | [**get_infrastructure_list**](docs/InfrastructuresApi.md#get_infrastructure_list) | **GET** /ng/api/infrastructures | Gets Infrastructure list
*InfrastructuresApi* | [**update_infrastructure**](docs/InfrastructuresApi.md#update_infrastructure) | **PUT** /ng/api/infrastructures | Update an Infrastructure by identifier
*InputSetsApi* | [**create_input_set**](docs/InputSetsApi.md#create_input_set) | **POST** /v1/orgs/{org}/projects/{project}/input-sets | Create an Input Set
*InputSetsApi* | [**delete_input_set**](docs/InputSetsApi.md#delete_input_set) | **DELETE** /v1/orgs/{org}/projects/{project}/input-sets/{input-set} | Delete an Input Set
*InputSetsApi* | [**get_input_set**](docs/InputSetsApi.md#get_input_set) | **GET** /v1/orgs/{org}/projects/{project}/input-sets/{input-set} | Retrieve an Input Set
*InputSetsApi* | [**import_input_set_from_git**](docs/InputSetsApi.md#import_input_set_from_git) | **POST** /v1/orgs/{org}/projects/{project}/input-sets/{input-set}/import | Get Input Set YAML from Git Repository
*InputSetsApi* | [**input_sets_move_config**](docs/InputSetsApi.md#input_sets_move_config) | **POST** /v1/orgs/{org}/projects/{project}/input-sets/{input-set}/move-config | Move InputSet YAML from inline to remote
*InputSetsApi* | [**list_input_sets**](docs/InputSetsApi.md#list_input_sets) | **GET** /v1/orgs/{org}/projects/{project}/input-sets | List Input Sets
*InputSetsApi* | [**update_input_set**](docs/InputSetsApi.md#update_input_set) | **PUT** /v1/orgs/{org}/projects/{project}/input-sets/{input-set} | Update an Input Set
*InputSetsApi* | [**update_input_set_git_metadata**](docs/InputSetsApi.md#update_input_set_git_metadata) | **PUT** /v1/orgs/{org}/projects/{project}/input-sets/{input-set}/git-metadata | Update GitMetadata for Remote InputSet
*InviteApi* | [**delete_invite**](docs/InviteApi.md#delete_invite) | **DELETE** /ng/api/invites/{inviteId} | Delete Invite
*InviteApi* | [**get_invite**](docs/InviteApi.md#get_invite) | **GET** /ng/api/invites/invite | Get Invite
*InviteApi* | [**get_invites**](docs/InviteApi.md#get_invites) | **GET** /ng/api/invites | List Invites
*InviteApi* | [**get_pending_users_aggregated**](docs/InviteApi.md#get_pending_users_aggregated) | **POST** /ng/api/invites/aggregate | Get pending users
*InviteApi* | [**update_invite**](docs/InviteApi.md#update_invite) | **PUT** /ng/api/invites/{inviteId} | Resend invite
*MonitoredServicesApi* | [**create_default_monitored_service**](docs/MonitoredServicesApi.md#create_default_monitored_service) | **POST** /cv/api/monitored-service/create-default | 
*MonitoredServicesApi* | [**cvget_anomalies_summary**](docs/MonitoredServicesApi.md#cvget_anomalies_summary) | **GET** /cv/api/monitored-service/{identifier}/anomaliesCount | 
*MonitoredServicesApi* | [**delete_monitored_service**](docs/MonitoredServicesApi.md#delete_monitored_service) | **DELETE** /cv/api/monitored-service/{identifier} | Delete monitored service data
*MonitoredServicesApi* | [**get_all_monitored_services_with_health_sources**](docs/MonitoredServicesApi.md#get_all_monitored_services_with_health_sources) | **GET** /cv/api/monitored-service/all/time-series-health-sources | 
*MonitoredServicesApi* | [**get_count_of_services**](docs/MonitoredServicesApi.md#get_count_of_services) | **GET** /cv/api/monitored-service/count-of-services | 
*MonitoredServicesApi* | [**get_environments**](docs/MonitoredServicesApi.md#get_environments) | **GET** /cv/api/monitored-service/environments | 
*MonitoredServicesApi* | [**get_health_sources**](docs/MonitoredServicesApi.md#get_health_sources) | **GET** /cv/api/monitored-service/health-sources | 
*MonitoredServicesApi* | [**get_health_sources_for_monitored_service_identifier**](docs/MonitoredServicesApi.md#get_health_sources_for_monitored_service_identifier) | **GET** /cv/api/monitored-service/{monitoredServiceIdentifier}/health-sources | 
*MonitoredServicesApi* | [**get_list**](docs/MonitoredServicesApi.md#get_list) | **GET** /cv/api/monitored-service/list | 
*MonitoredServicesApi* | [**get_list_v2**](docs/MonitoredServicesApi.md#get_list_v2) | **GET** /cv/api/monitored-service/platform/list | 
*MonitoredServicesApi* | [**get_monitored_service**](docs/MonitoredServicesApi.md#get_monitored_service) | **GET** /cv/api/monitored-service/{identifier} | Get monitored service data
*MonitoredServicesApi* | [**get_monitored_service_change_details**](docs/MonitoredServicesApi.md#get_monitored_service_change_details) | **GET** /cv/api/monitored-service/{monitoredServiceIdentifier}/change-details | 
*MonitoredServicesApi* | [**get_monitored_service_details**](docs/MonitoredServicesApi.md#get_monitored_service_details) | **GET** /cv/api/monitored-service/{monitoredServiceIdentifier}/service-details | 
*MonitoredServicesApi* | [**get_monitored_service_details1**](docs/MonitoredServicesApi.md#get_monitored_service_details1) | **GET** /cv/api/monitored-service/service-details | 
*MonitoredServicesApi* | [**get_monitored_service_from_service_and_environment**](docs/MonitoredServicesApi.md#get_monitored_service_from_service_and_environment) | **GET** /cv/api/monitored-service/service-environment | 
*MonitoredServicesApi* | [**get_monitored_service_logs**](docs/MonitoredServicesApi.md#get_monitored_service_logs) | **GET** /cv/api/monitored-service/{monitoredServiceIdentifier}/logs | 
*MonitoredServicesApi* | [**get_monitored_service_score**](docs/MonitoredServicesApi.md#get_monitored_service_score) | **GET** /cv/api/monitored-service/{identifier}/scores | 
*MonitoredServicesApi* | [**get_ms_secondary_events**](docs/MonitoredServicesApi.md#get_ms_secondary_events) | **GET** /cv/api/monitored-service/{identifier}/secondary-events | 
*MonitoredServicesApi* | [**get_ms_secondary_events_details**](docs/MonitoredServicesApi.md#get_ms_secondary_events_details) | **GET** /cv/api/monitored-service/secondary-events-details | 
*MonitoredServicesApi* | [**get_notification_rules_for_monitored_service**](docs/MonitoredServicesApi.md#get_notification_rules_for_monitored_service) | **GET** /cv/api/monitored-service/{identifier}/notification-rules | Get notification rules for MonitoredService
*MonitoredServicesApi* | [**get_over_all_health_score**](docs/MonitoredServicesApi.md#get_over_all_health_score) | **GET** /cv/api/monitored-service/{identifier}/overall-health-score | 
*MonitoredServicesApi* | [**get_services**](docs/MonitoredServicesApi.md#get_services) | **GET** /cv/api/monitored-service/services | 
*MonitoredServicesApi* | [**get_slo_metrics**](docs/MonitoredServicesApi.md#get_slo_metrics) | **GET** /cv/api/monitored-service/{monitoredServiceIdentifier}/health-source/{healthSourceIdentifier}/slo-metrics | 
*MonitoredServicesApi* | [**list**](docs/MonitoredServicesApi.md#list) | **GET** /cv/api/monitored-service | 
*MonitoredServicesApi* | [**save_monitored_service**](docs/MonitoredServicesApi.md#save_monitored_service) | **POST** /cv/api/monitored-service | Saves monitored service data
*MonitoredServicesApi* | [**save_monitored_service_from_template_input**](docs/MonitoredServicesApi.md#save_monitored_service_from_template_input) | **POST** /cv/api/monitored-service/template-input | Saves monitored service from template input
*MonitoredServicesApi* | [**save_monitored_service_from_yaml**](docs/MonitoredServicesApi.md#save_monitored_service_from_yaml) | **POST** /cv/api/monitored-service/yaml | 
*MonitoredServicesApi* | [**set_health_monitoring_flag**](docs/MonitoredServicesApi.md#set_health_monitoring_flag) | **PUT** /cv/api/monitored-service/{identifier}/health-monitoring-flag | 
*MonitoredServicesApi* | [**update_monitored_service**](docs/MonitoredServicesApi.md#update_monitored_service) | **PUT** /cv/api/monitored-service/{identifier} | Updates monitored service data
*MonitoredServicesApi* | [**update_monitored_service_from_template_input**](docs/MonitoredServicesApi.md#update_monitored_service_from_template_input) | **PUT** /cv/api/monitored-service/{identifier}/template-input | Update monitored service from yaml or template
*MonitoredServicesApi* | [**update_monitored_service_from_yaml**](docs/MonitoredServicesApi.md#update_monitored_service_from_yaml) | **PUT** /cv/api/monitored-service/{identifier}/yaml | 
*MonitoredServicesApi* | [**yaml_template**](docs/MonitoredServicesApi.md#yaml_template) | **GET** /cv/api/monitored-service/yaml-template | 
*NGSLOsApi* | [**delete_slo_data_ng**](docs/NGSLOsApi.md#delete_slo_data_ng) | **DELETE** /cv/api/account/{accountIdentifier}/org/{orgIdentifier}/project/{projectIdentifier}/slo/v2/identifier/{identifier} | Delete SLO data
*NGSLOsApi* | [**get_onboarding_graph_ng**](docs/NGSLOsApi.md#get_onboarding_graph_ng) | **POST** /cv/api/account/{accountIdentifier}/org/{orgIdentifier}/project/{projectIdentifier}/slo/v2/composite-slo/onboarding-graph | Get onBoarding graph for composite slo
*NGSLOsApi* | [**get_service_level_objective_ng**](docs/NGSLOsApi.md#get_service_level_objective_ng) | **GET** /cv/api/account/{accountIdentifier}/org/{orgIdentifier}/project/{projectIdentifier}/slo/v2/identifier/{identifier} | Get SLO data
*NGSLOsApi* | [**get_service_level_objectives_ng**](docs/NGSLOsApi.md#get_service_level_objectives_ng) | **GET** /cv/api/account/{accountIdentifier}/org/{orgIdentifier}/project/{projectIdentifier}/slo/v2 | Get all SLOs
*NGSLOsApi* | [**get_slo_health_list_view_ng**](docs/NGSLOsApi.md#get_slo_health_list_view_ng) | **POST** /cv/api/account/{accountIdentifier}/org/{orgIdentifier}/project/{projectIdentifier}/slo/v2/status-list | Get SLO list view
*NGSLOsApi* | [**save_slo_data_ng**](docs/NGSLOsApi.md#save_slo_data_ng) | **POST** /cv/api/account/{accountIdentifier}/org/{orgIdentifier}/project/{projectIdentifier}/slo/v2 | Saves SLO data
*NGSLOsApi* | [**update_slo_data_ng**](docs/NGSLOsApi.md#update_slo_data_ng) | **PUT** /cv/api/account/{accountIdentifier}/org/{orgIdentifier}/project/{projectIdentifier}/slo/v2/identifier/{identifier} | Update SLO data
*NextgenLdapApi* | [**post_ldap_authentication_test**](docs/NextgenLdapApi.md#post_ldap_authentication_test) | **POST** /ng/api/ldap/ldap-login-test | Test LDAP authentication
*NextgenLdapApi* | [**search_ldap_groups**](docs/NextgenLdapApi.md#search_ldap_groups) | **GET** /ng/api/ldap/{ldapId}/search/group | Return Ldap groups matching name
*OIDCApi* | [**get_harness_open_id_config**](docs/OIDCApi.md#get_harness_open_id_config) | **GET** /ng/api/oidc/account/{accountId}/.wellknown/jwks | Get the openid configuration for Harness
*OIDCApi* | [**get_harness_open_id_config1**](docs/OIDCApi.md#get_harness_open_id_config1) | **GET** /ng/api/oidc/account/{accountId}/.well-known/openid-configuration | Get the openid configuration for Harness
*OidcAccessTokenApi* | [**generate_oidc_access_token_for_gcp**](docs/OidcAccessTokenApi.md#generate_oidc_access_token_for_gcp) | **POST** /ng/api/oidc/access-token/gcp/workload-access | Generates an OIDC Access Token for GCP
*OidcIDTokenApi* | [**generate_oidc_id_token_for_gcp**](docs/OidcIDTokenApi.md#generate_oidc_id_token_for_gcp) | **POST** /ng/api/oidc/id-token/gcp | Generates an OIDC ID Token for GCP
*OrgConnectorApi* | [**create_org_scoped_connector**](docs/OrgConnectorApi.md#create_org_scoped_connector) | **POST** /v1/orgs/{org}/connectors | Create a Connector
*OrgConnectorApi* | [**delete_org_scoped_connector**](docs/OrgConnectorApi.md#delete_org_scoped_connector) | **DELETE** /v1/orgs/{org}/connectors/{connector} | Delete a connector
*OrgConnectorApi* | [**get_org_scoped_connector**](docs/OrgConnectorApi.md#get_org_scoped_connector) | **GET** /v1/orgs/{org}/connectors/{connector} | Retrieve a connector
*OrgConnectorApi* | [**test_org_scoped_connector**](docs/OrgConnectorApi.md#test_org_scoped_connector) | **GET** /v1/orgs/{org}/connectors/{connector}/test-connection | Test a connector
*OrgConnectorApi* | [**update_org_scoped_connector**](docs/OrgConnectorApi.md#update_org_scoped_connector) | **PUT** /v1/orgs/{org}/connectors/{connector} | Update a connector
*OrgProjectApi* | [**create_org_scoped_project**](docs/OrgProjectApi.md#create_org_scoped_project) | **POST** /v1/orgs/{org}/projects | Create a project
*OrgProjectApi* | [**delete_org_scoped_project**](docs/OrgProjectApi.md#delete_org_scoped_project) | **DELETE** /v1/orgs/{org}/projects/{project} | Delete a project
*OrgProjectApi* | [**get_org_scoped_project**](docs/OrgProjectApi.md#get_org_scoped_project) | **GET** /v1/orgs/{org}/projects/{project} | Retrieve a project
*OrgProjectApi* | [**get_org_scoped_projects**](docs/OrgProjectApi.md#get_org_scoped_projects) | **GET** /v1/orgs/{org}/projects | List projects
*OrgProjectApi* | [**update_org_scoped_project**](docs/OrgProjectApi.md#update_org_scoped_project) | **PUT** /v1/orgs/{org}/projects/{project} | Update a project
*OrgRancherInfrastructureApi* | [**list_org_scoped_rancher_clusters_using_connector**](docs/OrgRancherInfrastructureApi.md#list_org_scoped_rancher_clusters_using_connector) | **GET** /v1/orgs/{org}/rancher/connectors/{connector}/clusters | List rancher clusters using org level connector
*OrgRancherInfrastructureApi* | [**list_org_scoped_rancher_clusters_using_env_and_infra**](docs/OrgRancherInfrastructureApi.md#list_org_scoped_rancher_clusters_using_env_and_infra) | **GET** /v1/orgs/{org}/rancher/environments/{environment}/infrastructure-definitions/{infrastructure-definition}/clusters | List rancher clusters using org level env and infra def
*OrgRoleAssignmentsApi* | [**create_org_scoped_role_assignments**](docs/OrgRoleAssignmentsApi.md#create_org_scoped_role_assignments) | **POST** /v1/orgs/{org}/role-assignments | Create a role assignment
*OrgRoleAssignmentsApi* | [**delete_org_scoped_role_assignment**](docs/OrgRoleAssignmentsApi.md#delete_org_scoped_role_assignment) | **DELETE** /v1/orgs/{org}/role-assignments/{role-assignment} | Delete a role assignment
*OrgRoleAssignmentsApi* | [**get_org_scoped_role_assignment**](docs/OrgRoleAssignmentsApi.md#get_org_scoped_role_assignment) | **GET** /v1/orgs/{org}/role-assignments/{role-assignment} | Retrieve a role assignment
*OrgRoleAssignmentsApi* | [**get_org_scoped_role_assignments**](docs/OrgRoleAssignmentsApi.md#get_org_scoped_role_assignments) | **GET** /v1/orgs/{org}/role-assignments | List role assignments
*OrgSecretApi* | [**create_org_scoped_secret**](docs/OrgSecretApi.md#create_org_scoped_secret) | **POST** /v1/orgs/{org}/secrets | Create a secret
*OrgSecretApi* | [**delete_org_scoped_secret**](docs/OrgSecretApi.md#delete_org_scoped_secret) | **DELETE** /v1/orgs/{org}/secrets/{secret} | Delete a secret
*OrgSecretApi* | [**get_org_scoped_secret**](docs/OrgSecretApi.md#get_org_scoped_secret) | **GET** /v1/orgs/{org}/secrets/{secret} | Retrieve a secret
*OrgSecretApi* | [**get_org_scoped_secrets**](docs/OrgSecretApi.md#get_org_scoped_secrets) | **GET** /v1/orgs/{org}/secrets | List secrets
*OrgSecretApi* | [**update_org_scoped_secret**](docs/OrgSecretApi.md#update_org_scoped_secret) | **PUT** /v1/orgs/{org}/secrets/{secret} | Update a secret
*OrgSecretApi* | [**validate_org_secret_ref**](docs/OrgSecretApi.md#validate_org_secret_ref) | **POST** /v1/orgs/{org}/secrets/validate-secret-ref | Validate secret reference
*OrgServicesApi* | [**create_org_scoped_service**](docs/OrgServicesApi.md#create_org_scoped_service) | **POST** /v1/orgs/{org}/services | Create a service
*OrgServicesApi* | [**delete_org_scoped_service**](docs/OrgServicesApi.md#delete_org_scoped_service) | **DELETE** /v1/orgs/{org}/services/{service} | Delete a service
*OrgServicesApi* | [**get_org_scoped_service**](docs/OrgServicesApi.md#get_org_scoped_service) | **GET** /v1/orgs/{org}/services/{service} | Retrieve a service
*OrgServicesApi* | [**get_org_scoped_services**](docs/OrgServicesApi.md#get_org_scoped_services) | **GET** /v1/orgs/{org}/services | List Services
*OrgServicesApi* | [**update_org_scoped_service**](docs/OrgServicesApi.md#update_org_scoped_service) | **PUT** /v1/orgs/{org}/services/{service} | Update Service
*OrgTemplateApi* | [**create_templates_org**](docs/OrgTemplateApi.md#create_templates_org) | **POST** /v1/orgs/{org}/templates | Create Template
*OrgTemplateApi* | [**delete_template_org**](docs/OrgTemplateApi.md#delete_template_org) | **DELETE** /v1/orgs/{org}/templates/{template}/versions/{version} | Delete Template
*OrgTemplateApi* | [**get_template_org**](docs/OrgTemplateApi.md#get_template_org) | **GET** /v1/orgs/{org}/templates/{template}/versions/{version} | Retrieve a Template
*OrgTemplateApi* | [**get_template_stable_org**](docs/OrgTemplateApi.md#get_template_stable_org) | **GET** /v1/orgs/{org}/templates/{template} | Get Stable Template
*OrgTemplateApi* | [**get_templates_list_org**](docs/OrgTemplateApi.md#get_templates_list_org) | **GET** /v1/orgs/{org}/templates | Get Templates List
*OrgTemplateApi* | [**import_template_org**](docs/OrgTemplateApi.md#import_template_org) | **POST** /v1/orgs/{org}/templates/{template}/import | Import template
*OrgTemplateApi* | [**update_template_org**](docs/OrgTemplateApi.md#update_template_org) | **PUT** /v1/orgs/{org}/templates/{template}/versions/{version} | Update Template
*OrgTemplateApi* | [**update_template_stable_org**](docs/OrgTemplateApi.md#update_template_stable_org) | **PUT** /v1/orgs/{org}/templates/{template}/versions/{version}/stable | Update Stable Template
*OrganizationApi* | [**create_organization**](docs/OrganizationApi.md#create_organization) | **POST** /v1/orgs | Create an organization [Beta]
*OrganizationApi* | [**delete_organization**](docs/OrganizationApi.md#delete_organization) | **DELETE** /v1/orgs/{org} | Delete an organization [Beta]
*OrganizationApi* | [**delete_organization_0**](docs/OrganizationApi.md#delete_organization_0) | **DELETE** /ng/api/organizations/{identifier} | Delete an Organization
*OrganizationApi* | [**get_organization**](docs/OrganizationApi.md#get_organization) | **GET** /v1/orgs/{org} | Retrieve an organization [Beta]
*OrganizationApi* | [**get_organization_0**](docs/OrganizationApi.md#get_organization_0) | **GET** /ng/api/organizations/{identifier} | List Organization details
*OrganizationApi* | [**get_organization_list**](docs/OrganizationApi.md#get_organization_list) | **GET** /ng/api/organizations | List Organizations by filter
*OrganizationApi* | [**get_organizations**](docs/OrganizationApi.md#get_organizations) | **GET** /v1/orgs | List organizations [Beta]
*OrganizationApi* | [**post_organization**](docs/OrganizationApi.md#post_organization) | **POST** /ng/api/organizations | Create an Organization
*OrganizationApi* | [**put_organization**](docs/OrganizationApi.md#put_organization) | **PUT** /ng/api/organizations/{identifier} | Update an Organization
*OrganizationApi* | [**update_organization**](docs/OrganizationApi.md#update_organization) | **PUT** /v1/orgs/{org} | Update an organization [Beta]
*OrganizationResourceGroupsApi* | [**create_resource_group_org**](docs/OrganizationResourceGroupsApi.md#create_resource_group_org) | **POST** /v1/orgs/{org}/resource-groups | Create a Resource Group
*OrganizationResourceGroupsApi* | [**delete_resource_group_org**](docs/OrganizationResourceGroupsApi.md#delete_resource_group_org) | **DELETE** /v1/orgs/{org}/resource-groups/{resource-group} | Delete a Resource Group
*OrganizationResourceGroupsApi* | [**get_resource_group_org**](docs/OrganizationResourceGroupsApi.md#get_resource_group_org) | **GET** /v1/orgs/{org}/resource-groups/{resource-group} | Retrieve a Resource Group
*OrganizationResourceGroupsApi* | [**list_resource_groups_org**](docs/OrganizationResourceGroupsApi.md#list_resource_groups_org) | **GET** /v1/orgs/{org}/resource-groups | List Resource Groups
*OrganizationResourceGroupsApi* | [**update_resource_group_org**](docs/OrganizationResourceGroupsApi.md#update_resource_group_org) | **PUT** /v1/orgs/{org}/resource-groups/{resource-group} | Update a Resource Group
*OrganizationRolesApi* | [**create_role_org**](docs/OrganizationRolesApi.md#create_role_org) | **POST** /v1/orgs/{org}/roles | Create a Role
*OrganizationRolesApi* | [**delete_role_org**](docs/OrganizationRolesApi.md#delete_role_org) | **DELETE** /v1/orgs/{org}/roles/{role} | Delete a Role
*OrganizationRolesApi* | [**get_role_org**](docs/OrganizationRolesApi.md#get_role_org) | **GET** /v1/orgs/{org}/roles/{role} | Retrieve a Role
*OrganizationRolesApi* | [**list_roles_org**](docs/OrganizationRolesApi.md#list_roles_org) | **GET** /v1/orgs/{org}/roles | List Roles
*OrganizationRolesApi* | [**update_role_org**](docs/OrganizationRolesApi.md#update_role_org) | **PUT** /v1/orgs/{org}/roles/{role} | Update a Role
*PermissionsApi* | [**get_permission_list**](docs/PermissionsApi.md#get_permission_list) | **GET** /authz/api/permissions | List Permissions
*PermissionsApi* | [**get_permission_resource_types_list**](docs/PermissionsApi.md#get_permission_resource_types_list) | **GET** /authz/api/permissions/resourcetypes | List Resource Types
*PipelineApi* | [**delete_pipeline**](docs/PipelineApi.md#delete_pipeline) | **DELETE** /pipeline/api/pipelines/{pipelineIdentifier} | Delete a Pipeline
*PipelineApi* | [**get_pipeline**](docs/PipelineApi.md#get_pipeline) | **GET** /pipeline/api/pipelines/{pipelineIdentifier} | Fetch a Pipeline
*PipelineApi* | [**get_pipeline_list**](docs/PipelineApi.md#get_pipeline_list) | **POST** /pipeline/api/pipelines/list | List Pipelines
*PipelineApi* | [**get_pipeline_summary**](docs/PipelineApi.md#get_pipeline_summary) | **GET** /pipeline/api/pipelines/summary/{pipelineIdentifier} | Fetch Pipeline Summary
*PipelineApi* | [**import_pipeline**](docs/PipelineApi.md#import_pipeline) | **POST** /pipeline/api/pipelines/import/{pipelineIdentifier} | Import and Create Pipeline from Git Repository
*PipelineApi* | [**post_pipeline**](docs/PipelineApi.md#post_pipeline) | **POST** /pipeline/api/pipelines | Create a Pipeline
*PipelineApi* | [**post_pipeline_v2**](docs/PipelineApi.md#post_pipeline_v2) | **POST** /pipeline/api/pipelines/v2 | Create a Pipeline
*PipelineApi* | [**update_pipeline**](docs/PipelineApi.md#update_pipeline) | **PUT** /pipeline/api/pipelines/{pipelineIdentifier} | Update a Pipeline
*PipelineApi* | [**update_pipeline_git_details**](docs/PipelineApi.md#update_pipeline_git_details) | **PUT** /pipeline/api/pipelines/{pipelineIdentifier}/update-git-metadata | Update git-metadata in remote pipeline Entity
*PipelineApi* | [**update_pipeline_v2**](docs/PipelineApi.md#update_pipeline_v2) | **PUT** /pipeline/api/pipelines/v2/{pipelineIdentifier} | Update a Pipeline
*PipelineDashboardApi* | [**get_pipeline_execution**](docs/PipelineDashboardApi.md#get_pipeline_execution) | **GET** /pipeline/api/pipelines/pipelineExecution | Fetch Execution Details for an Interval
*PipelineExecuteApi* | [**handle_stage_interrupt**](docs/PipelineExecuteApi.md#handle_stage_interrupt) | **PUT** /pipeline/api/pipeline/execute/interrupt/{planExecutionId}/{nodeExecutionId} | Handles the interrupt for a given stage in a pipeline
*PipelineExecuteApi* | [**post_pipeline_execute_with_input_set_list**](docs/PipelineExecuteApi.md#post_pipeline_execute_with_input_set_list) | **POST** /pipeline/api/pipeline/execute/{identifier}/inputSetList | Execute a Pipeline with Input Set References
*PipelineExecuteApi* | [**post_pipeline_execute_with_input_set_yaml**](docs/PipelineExecuteApi.md#post_pipeline_execute_with_input_set_yaml) | **POST** /pipeline/api/pipeline/execute/{identifier} | Execute a Pipeline with Runtime Input YAML
*PipelineExecuteApi* | [**put_handle_interrupt**](docs/PipelineExecuteApi.md#put_handle_interrupt) | **PUT** /pipeline/api/pipeline/execute/interrupt/{planExecutionId} | Execute an Interrupt
*PipelineExecuteApi* | [**retry_history**](docs/PipelineExecuteApi.md#retry_history) | **GET** /pipeline/api/pipeline/execute/retryHistory/{planExecutionId} | Retry History for a given execution
*PipelineExecuteApi* | [**retry_pipeline**](docs/PipelineExecuteApi.md#retry_pipeline) | **POST** /pipeline/api/pipeline/execute/retry/{identifier} | Retry a executed pipeline with inputSet pipeline yaml
*PipelineExecutionApi* | [**execute_pipeline**](docs/PipelineExecutionApi.md#execute_pipeline) | **POST** /v1/orgs/{org}/projects/{project}/pipelines/{pipeline}/execute | Execute Pipeline
*PipelineExecutionDetailsApi* | [**get_execution_detail**](docs/PipelineExecutionDetailsApi.md#get_execution_detail) | **GET** /pipeline/api/pipelines/execution/{planExecutionId} | Fetch Execution Details
*PipelineExecutionDetailsApi* | [**get_execution_detail_v2**](docs/PipelineExecutionDetailsApi.md#get_execution_detail_v2) | **GET** /pipeline/api/pipelines/execution/v2/{planExecutionId} | Fetch Execution Details
*PipelineExecutionDetailsApi* | [**get_execution_sub_graph_for_node_execution**](docs/PipelineExecutionDetailsApi.md#get_execution_sub_graph_for_node_execution) | **GET** /pipeline/api/pipelines/execution/subGraph/{planExecutionId}/{nodeExecutionId} | Fetch Execution SubGraph for a Given NodeExecution ID
*PipelineExecutionDetailsApi* | [**get_inputset_yaml_v2**](docs/PipelineExecutionDetailsApi.md#get_inputset_yaml_v2) | **GET** /pipeline/api/pipelines/execution/{planExecutionId}/inputsetV2 | Get the Input Set YAML used for given Plan Execution
*PipelineExecutionDetailsApi* | [**get_list_of_execution_identifier**](docs/PipelineExecutionDetailsApi.md#get_list_of_execution_identifier) | **POST** /pipeline/api/pipelines/execution/executionSummary | List Execution Identifier
*PipelineExecutionDetailsApi* | [**get_list_of_executions**](docs/PipelineExecutionDetailsApi.md#get_list_of_executions) | **POST** /pipeline/api/pipelines/execution/summary | List Executions
*PipelineExecutionDetailsApi* | [**get_notes_for_execution**](docs/PipelineExecutionDetailsApi.md#get_notes_for_execution) | **GET** /pipeline/api/pipelines/execution/{planExecutionId}/notes | Get Notes for a pipelineExecution
*PipelineExecutionDetailsApi* | [**update_notes_for_execution**](docs/PipelineExecutionDetailsApi.md#update_notes_for_execution) | **PUT** /pipeline/api/pipelines/execution/{planExecutionId}/notes | Updates Notes for a pipelineExecution
*PipelineInputSetApi* | [**delete_input_set**](docs/PipelineInputSetApi.md#delete_input_set) | **DELETE** /pipeline/api/inputSets/{inputSetIdentifier} | Delete an Input Set
*PipelineInputSetApi* | [**get_input_set**](docs/PipelineInputSetApi.md#get_input_set) | **GET** /pipeline/api/inputSets/{inputSetIdentifier} | Fetch an Input Set
*PipelineInputSetApi* | [**get_overlay_input_set**](docs/PipelineInputSetApi.md#get_overlay_input_set) | **GET** /pipeline/api/inputSets/overlay/{inputSetIdentifier} | Gets an Overlay Input Set by identifier
*PipelineInputSetApi* | [**list_input_set**](docs/PipelineInputSetApi.md#list_input_set) | **GET** /pipeline/api/inputSets | List Input Sets
*PipelineInputSetApi* | [**post_input_set**](docs/PipelineInputSetApi.md#post_input_set) | **POST** /pipeline/api/inputSets | Create an Input Set
*PipelineInputSetApi* | [**post_overlay_input_set**](docs/PipelineInputSetApi.md#post_overlay_input_set) | **POST** /pipeline/api/inputSets/overlay | Create an Overlay Input Set for a pipeline
*PipelineInputSetApi* | [**put_input_set**](docs/PipelineInputSetApi.md#put_input_set) | **PUT** /pipeline/api/inputSets/{inputSetIdentifier} | Update an Input Set
*PipelineInputSetApi* | [**put_overlay_input_set**](docs/PipelineInputSetApi.md#put_overlay_input_set) | **PUT** /pipeline/api/inputSets/overlay/{inputSetIdentifier} | Update an Overlay Input Set for a pipeline
*PipelineInputSetApi* | [**runtime_input_template**](docs/PipelineInputSetApi.md#runtime_input_template) | **POST** /pipeline/api/inputSets/template | Fetch Runtime Input Template
*PipelineInputSetApi* | [**update_input_set_git_details**](docs/PipelineInputSetApi.md#update_input_set_git_details) | **PUT** /pipeline/api/inputSets/{inputSetIdentifier}/update-git-metadata | Update git-metadata in remote input-set
*PipelineRefreshApi* | [**validate_template_inputs**](docs/PipelineRefreshApi.md#validate_template_inputs) | **GET** /pipeline/api/refresh-template/validate-template-inputs | Validates template inputs in a pipeline&#x27;s YAML specification.
*PipelinesApi* | [**create_pipeline**](docs/PipelinesApi.md#create_pipeline) | **POST** /v1/orgs/{org}/projects/{project}/pipelines | Create a Pipeline
*PipelinesApi* | [**delete_pipeline**](docs/PipelinesApi.md#delete_pipeline) | **DELETE** /v1/orgs/{org}/projects/{project}/pipelines/{pipeline} | Delete a Pipeline
*PipelinesApi* | [**get_pipeline**](docs/PipelinesApi.md#get_pipeline) | **GET** /v1/orgs/{org}/projects/{project}/pipelines/{pipeline} | Retrieve a Pipeline
*PipelinesApi* | [**import_pipeline_from_git**](docs/PipelinesApi.md#import_pipeline_from_git) | **POST** /v1/orgs/{org}/projects/{project}/pipelines/{pipeline}/import | Get Pipeline YAML from Git Repository
*PipelinesApi* | [**list_pipelines**](docs/PipelinesApi.md#list_pipelines) | **GET** /v1/orgs/{org}/projects/{project}/pipelines | List Pipelines
*PipelinesApi* | [**move_config**](docs/PipelinesApi.md#move_config) | **POST** /v1/orgs/{org}/projects/{project}/pipelines/{pipeline}/move-config | Move Pipeline YAML from inline to remote
*PipelinesApi* | [**update_pipeline**](docs/PipelinesApi.md#update_pipeline) | **PUT** /v1/orgs/{org}/projects/{project}/pipelines/{pipeline} | Update a Pipeline
*PipelinesApi* | [**update_pipeline_git_metadata**](docs/PipelinesApi.md#update_pipeline_git_metadata) | **PUT** /v1/orgs/{org}/projects/{project}/pipelines/{pipeline}/git-metadata | Update GitMetadata for Remote Pipelines
*ProjectApi* | [**delete_project**](docs/ProjectApi.md#delete_project) | **DELETE** /ng/api/projects/{identifier} | Delete a Project
*ProjectApi* | [**get_project**](docs/ProjectApi.md#get_project) | **GET** /ng/api/projects/{identifier} | List Project details
*ProjectApi* | [**get_project_list**](docs/ProjectApi.md#get_project_list) | **GET** /ng/api/projects | List all Projects for a user
*ProjectApi* | [**get_project_list_with_multi_org_filter**](docs/ProjectApi.md#get_project_list_with_multi_org_filter) | **GET** /ng/api/projects/list | List user&#x27;s project with support to filter by multiple organizations
*ProjectApi* | [**post_project**](docs/ProjectApi.md#post_project) | **POST** /ng/api/projects | Create a Project
*ProjectApi* | [**put_project**](docs/ProjectApi.md#put_project) | **PUT** /ng/api/projects/{identifier} | Update a Project
*ProjectConnectorApi* | [**create_project_scoped_connector**](docs/ProjectConnectorApi.md#create_project_scoped_connector) | **POST** /v1/orgs/{org}/projects/{project}/connectors | Create a Connector
*ProjectConnectorApi* | [**delete_project_scoped_connector**](docs/ProjectConnectorApi.md#delete_project_scoped_connector) | **DELETE** /v1/orgs/{org}/projects/{project}/connectors/{connector} | Delete a connector
*ProjectConnectorApi* | [**get_project_scoped_connector**](docs/ProjectConnectorApi.md#get_project_scoped_connector) | **GET** /v1/orgs/{org}/projects/{project}/connectors/{connector} | Retrieve a connector
*ProjectConnectorApi* | [**test_project_scoped_connector**](docs/ProjectConnectorApi.md#test_project_scoped_connector) | **GET** /v1/orgs/{org}/projects/{project}/connectors/{connector}/test-connection | Test a connector
*ProjectConnectorApi* | [**update_project_scoped_connector**](docs/ProjectConnectorApi.md#update_project_scoped_connector) | **PUT** /v1/orgs/{org}/projects/{project}/connectors/{connector} | Update a connector
*ProjectRancherInfrastructureApi* | [**list_project_scoped_rancher_clusters_using_connector**](docs/ProjectRancherInfrastructureApi.md#list_project_scoped_rancher_clusters_using_connector) | **GET** /v1/orgs/{org}/projects/{project}/rancher/connectors/{connector}/clusters | List rancher clusters using project level connector
*ProjectRancherInfrastructureApi* | [**list_project_scoped_rancher_clusters_using_env_and_infra**](docs/ProjectRancherInfrastructureApi.md#list_project_scoped_rancher_clusters_using_env_and_infra) | **GET** /v1/orgs/{org}/projects/{project}/rancher/environments/{environment}/infrastructure-definitions/{infrastructure-definition}/clusters | List rancher clusters using project level env and infra def
*ProjectResourceGroupsApi* | [**create_resource_group_project**](docs/ProjectResourceGroupsApi.md#create_resource_group_project) | **POST** /v1/orgs/{org}/projects/{project}/resource-groups | Create a Resource Group
*ProjectResourceGroupsApi* | [**delete_resource_group_project**](docs/ProjectResourceGroupsApi.md#delete_resource_group_project) | **DELETE** /v1/orgs/{org}/projects/{project}/resource-groups/{resource-group} | Delete a Resource Group
*ProjectResourceGroupsApi* | [**get_resource_group_project**](docs/ProjectResourceGroupsApi.md#get_resource_group_project) | **GET** /v1/orgs/{org}/projects/{project}/resource-groups/{resource-group} | Retrieve a Resource Group
*ProjectResourceGroupsApi* | [**list_resource_groups_project**](docs/ProjectResourceGroupsApi.md#list_resource_groups_project) | **GET** /v1/orgs/{org}/projects/{project}/resource-groups | List Resource Groups
*ProjectResourceGroupsApi* | [**update_resource_group_project**](docs/ProjectResourceGroupsApi.md#update_resource_group_project) | **PUT** /v1/orgs/{org}/projects/{project}/resource-groups/{resource-group} | Update a Resource Group
*ProjectRoleAssignmentsApi* | [**create_project_scoped_role_assignments**](docs/ProjectRoleAssignmentsApi.md#create_project_scoped_role_assignments) | **POST** /v1/orgs/{org}/projects/{project}/role-assignments | Create a role assignment
*ProjectRoleAssignmentsApi* | [**delete_project_scoped_role_assignment**](docs/ProjectRoleAssignmentsApi.md#delete_project_scoped_role_assignment) | **DELETE** /v1/orgs/{org}/projects/{project}/role-assignments/{role-assignment} | Delete a role assignment
*ProjectRoleAssignmentsApi* | [**get_project_scoped_role_assignment**](docs/ProjectRoleAssignmentsApi.md#get_project_scoped_role_assignment) | **GET** /v1/orgs/{org}/projects/{project}/role-assignments/{role-assignment} | Retrieve a role assignment
*ProjectRoleAssignmentsApi* | [**get_project_scoped_role_assignments**](docs/ProjectRoleAssignmentsApi.md#get_project_scoped_role_assignments) | **GET** /v1/orgs/{org}/projects/{project}/role-assignments | List role assignments
*ProjectRolesApi* | [**create_role_project**](docs/ProjectRolesApi.md#create_role_project) | **POST** /v1/orgs/{org}/projects/{project}/roles | Create a Role
*ProjectRolesApi* | [**delete_role_project**](docs/ProjectRolesApi.md#delete_role_project) | **DELETE** /v1/orgs/{org}/projects/{project}/roles/{role} | Delete a Role
*ProjectRolesApi* | [**get_role_project**](docs/ProjectRolesApi.md#get_role_project) | **GET** /v1/orgs/{org}/projects/{project}/roles/{role} | Retrieve a Role
*ProjectRolesApi* | [**list_roles_project**](docs/ProjectRolesApi.md#list_roles_project) | **GET** /v1/orgs/{org}/projects/{project}/roles | List Roles
*ProjectRolesApi* | [**update_role_project**](docs/ProjectRolesApi.md#update_role_project) | **PUT** /v1/orgs/{org}/projects/{project}/roles/{role} | Update a Role
*ProjectSecretApi* | [**create_project_scoped_secret**](docs/ProjectSecretApi.md#create_project_scoped_secret) | **POST** /v1/orgs/{org}/projects/{project}/secrets | Create a secret
*ProjectSecretApi* | [**delete_project_scoped_secret**](docs/ProjectSecretApi.md#delete_project_scoped_secret) | **DELETE** /v1/orgs/{org}/projects/{project}/secrets/{secret} | Delete a secret
*ProjectSecretApi* | [**get_project_scoped_secret**](docs/ProjectSecretApi.md#get_project_scoped_secret) | **GET** /v1/orgs/{org}/projects/{project}/secrets/{secret} | Retrieve a secret
*ProjectSecretApi* | [**get_project_scoped_secrets**](docs/ProjectSecretApi.md#get_project_scoped_secrets) | **GET** /v1/orgs/{org}/projects/{project}/secrets | List secrets
*ProjectSecretApi* | [**update_project_scoped_secret**](docs/ProjectSecretApi.md#update_project_scoped_secret) | **PUT** /v1/orgs/{org}/projects/{project}/secrets/{secret} | Update a secret
*ProjectSecretApi* | [**validate_project_secret_ref**](docs/ProjectSecretApi.md#validate_project_secret_ref) | **POST** /v1/orgs/{org}/projects/{project}/secrets/validate-secret-ref | Validate secret reference
*ProjectServicesApi* | [**create_service**](docs/ProjectServicesApi.md#create_service) | **POST** /v1/orgs/{org}/projects/{project}/services | Create a Service
*ProjectServicesApi* | [**delete_service**](docs/ProjectServicesApi.md#delete_service) | **DELETE** /v1/orgs/{org}/projects/{project}/services/{service} | Delete a Service
*ProjectServicesApi* | [**get_service**](docs/ProjectServicesApi.md#get_service) | **GET** /v1/orgs/{org}/projects/{project}/services/{service} | Retrieve a service
*ProjectServicesApi* | [**get_services**](docs/ProjectServicesApi.md#get_services) | **GET** /v1/orgs/{org}/projects/{project}/services | List Services
*ProjectServicesApi* | [**update_service**](docs/ProjectServicesApi.md#update_service) | **PUT** /v1/orgs/{org}/projects/{project}/services/{service} | Update Service
*ProjectTemplateApi* | [**create_templates_project**](docs/ProjectTemplateApi.md#create_templates_project) | **POST** /v1/orgs/{org}/projects/{project}/templates | Create Template
*ProjectTemplateApi* | [**delete_template_project**](docs/ProjectTemplateApi.md#delete_template_project) | **DELETE** /v1/orgs/{org}/projects/{project}/templates/{template}/versions/{version} | Delete Template
*ProjectTemplateApi* | [**get_template_project**](docs/ProjectTemplateApi.md#get_template_project) | **GET** /v1/orgs/{org}/projects/{project}/templates/{template}/versions/{version} | Retrieve a Template
*ProjectTemplateApi* | [**get_template_stable_project**](docs/ProjectTemplateApi.md#get_template_stable_project) | **GET** /v1/orgs/{org}/projects/{project}/templates/{template} | Get Stable Template
*ProjectTemplateApi* | [**get_templates_list_project**](docs/ProjectTemplateApi.md#get_templates_list_project) | **GET** /v1/orgs/{org}/projects/{project}/templates | Get Templates List
*ProjectTemplateApi* | [**import_template_project**](docs/ProjectTemplateApi.md#import_template_project) | **POST** /v1/orgs/{org}/projects/{project}/templates/{template}/import | Import Template
*ProjectTemplateApi* | [**update_template_project**](docs/ProjectTemplateApi.md#update_template_project) | **PUT** /v1/orgs/{org}/projects/{project}/templates/{template}/versions/{version} | Update Template
*ProjectTemplateApi* | [**update_template_stable_project**](docs/ProjectTemplateApi.md#update_template_stable_project) | **PUT** /v1/orgs/{org}/projects/{project}/templates/{template}/versions/{version}/stable | Update Stable Template
*ProjectMappingsApi* | [**app_project_mapping_service_create**](docs/ProjectMappingsApi.md#app_project_mapping_service_create) | **POST** /gitops/api/v1/agents/{agentIdentifier}/appprojectsmapping | CreateAppProjectMapping creates a new mapping between Harness Project and argo project
*ProjectMappingsApi* | [**app_project_mapping_service_delete**](docs/ProjectMappingsApi.md#app_project_mapping_service_delete) | **DELETE** /gitops/api/v1/agents/{agentIdentifier}/appprojectsmapping/{name} | Delete an argo project to harness project mapping
*ProjectMappingsApi* | [**app_project_mapping_service_get_app_project_mapping_list**](docs/ProjectMappingsApi.md#app_project_mapping_service_get_app_project_mapping_list) | **GET** /gitops/api/v1/appprojectsmapping | 
*ProjectMappingsApi* | [**app_project_mapping_service_get_app_project_mapping_list_by_agent**](docs/ProjectMappingsApi.md#app_project_mapping_service_get_app_project_mapping_list_by_agent) | **GET** /gitops/api/v1/agents/{agentIdentifier}/appprojectsmapping | 
*ProjectsApi* | [**agent_project_service_create**](docs/ProjectsApi.md#agent_project_service_create) | **POST** /gitops/api/v1/agents/{agentIdentifier}/projects | Create a new project
*ProjectsApi* | [**agent_project_service_delete**](docs/ProjectsApi.md#agent_project_service_delete) | **DELETE** /gitops/api/v1/agents/{agentIdentifier}/projects/{query.name} | Delete deletes a project
*ProjectsApi* | [**agent_project_service_get**](docs/ProjectsApi.md#agent_project_service_get) | **GET** /gitops/api/v1/agents/{agentIdentifier}/projects/{query.name} | Get returns a project by name
*ProjectsApi* | [**agent_project_service_list**](docs/ProjectsApi.md#agent_project_service_list) | **GET** /gitops/api/v1/agents/{agentIdentifier}/projects | List returns list of projects
*ProjectsApi* | [**agent_project_service_update**](docs/ProjectsApi.md#agent_project_service_update) | **PUT** /gitops/api/v1/agents/{agentIdentifier}/projects/{request.project.metadata.name} | Update updates a project
*ProxyApi* | [**create_proxy_key**](docs/ProxyApi.md#create_proxy_key) | **POST** /cf/admin/proxy/keys | Creates a Proxy Key in the account &amp; org
*ProxyApi* | [**delete_proxy_key**](docs/ProxyApi.md#delete_proxy_key) | **DELETE** /cf/admin/proxy/keys/{identifier} | Deletes a ProxyKey
*ProxyApi* | [**get_proxy_key**](docs/ProxyApi.md#get_proxy_key) | **GET** /cf/admin/proxy/keys/{identifier} | Returns a ProxyKey
*ProxyApi* | [**get_proxy_keys**](docs/ProxyApi.md#get_proxy_keys) | **GET** /cf/admin/proxy/keys | Returns all Proxy keys in an account
*ProxyApi* | [**patch_proxy_key**](docs/ProxyApi.md#patch_proxy_key) | **PATCH** /cf/admin/proxy/keys/{identifier} | Updates a Proxy Key in the account &amp; org
*ProxyApi* | [**update_proxy_key**](docs/ProxyApi.md#update_proxy_key) | **PUT** /cf/admin/proxy/keys/{identifier} | Updates a Proxy Key in the account &amp; org
*ReconcilerApi* | [**reconciler_service_collect_counts**](docs/ReconcilerApi.md#reconciler_service_collect_counts) | **POST** /gitops/api/v1/agents/{agentIdentifier}/reconcile/counts | Returns number of entities that exist in the cluster on the agent. Filter can be used to count only global entities (with empty project) and those specified by the filter.
*ReconcilerApi* | [**reconciler_service_import_data**](docs/ReconcilerApi.md#reconciler_service_import_data) | **POST** /gitops/api/v1/agents/{agentIdentifier}/reconcile/import | Imports data from cluster via agent. There must be at least one project mapping in the database. Returns number of entities imported.
*RepositoriesApi* | [**agent_repository_service_create_repository**](docs/RepositoriesApi.md#agent_repository_service_create_repository) | **POST** /gitops/api/v1/agents/{agentIdentifier}/repositories | CreateRepository creates a new repository configuration
*RepositoriesApi* | [**agent_repository_service_delete_repository**](docs/RepositoriesApi.md#agent_repository_service_delete_repository) | **DELETE** /gitops/api/v1/agents/{agentIdentifier}/repositories/{identifier} | DeleteRepository deletes a repository from the configuration
*RepositoriesApi* | [**agent_repository_service_get**](docs/RepositoriesApi.md#agent_repository_service_get) | **GET** /gitops/api/v1/agents/{agentIdentifier}/repositories/{identifier} | Get returns a repository or its credentials
*RepositoriesApi* | [**agent_repository_service_get_app_details**](docs/RepositoriesApi.md#agent_repository_service_get_app_details) | **GET** /gitops/api/v1/agents/{agentIdentifier}/repositories/{identifier}/appdetails | GetAppDetails returns application details by given path
*RepositoriesApi* | [**agent_repository_service_get_helm_charts**](docs/RepositoriesApi.md#agent_repository_service_get_helm_charts) | **GET** /gitops/api/v1/agents/{agentIdentifier}/repositories/{identifier}/helmcharts | GetHelmCharts returns list of helm charts in the specified repository
*RepositoriesApi* | [**agent_repository_service_list_apps**](docs/RepositoriesApi.md#agent_repository_service_list_apps) | **GET** /gitops/api/v1/agents/{agentIdentifier}/repositories/{identifier}/apps | ListApps returns list of apps in the repo
*RepositoriesApi* | [**agent_repository_service_list_refs**](docs/RepositoriesApi.md#agent_repository_service_list_refs) | **GET** /gitops/api/v1/agents/{agentIdentifier}/repositories/{identifier}/refs | Returns a list of refs (e.g. branches and tags) in the repo
*RepositoriesApi* | [**agent_repository_service_list_repositories**](docs/RepositoriesApi.md#agent_repository_service_list_repositories) | **GET** /gitops/api/v1/agents/{agentIdentifier}/repositories | ListRepositories gets a list of all configured repositories
*RepositoriesApi* | [**agent_repository_service_update_repository**](docs/RepositoriesApi.md#agent_repository_service_update_repository) | **PUT** /gitops/api/v1/agents/{agentIdentifier}/repositories/{identifier} | UpdateRepository updates a repository configuration
*RepositoriesApi* | [**agent_repository_service_validate_access**](docs/RepositoriesApi.md#agent_repository_service_validate_access) | **POST** /gitops/api/v1/agents/{agentIdentifier}/repositories/validate | ValidateAccess gets connection state for a repository
*RepositoriesApi* | [**repository_service_exists**](docs/RepositoriesApi.md#repository_service_exists) | **GET** /gitops/api/v1/repositories/exists | Checks whether a repository with the given name exists
*RepositoriesApi* | [**repository_service_list_repositories**](docs/RepositoriesApi.md#repository_service_list_repositories) | **POST** /gitops/api/v1/repositories | List returns list of Repositories
*RepositoryCertificatesApi* | [**agent_certificate_service_create**](docs/RepositoryCertificatesApi.md#agent_certificate_service_create) | **POST** /gitops/api/v1/agents/{agentIdentifier}/certificates | Creates repository certificates on the server
*RepositoryCertificatesApi* | [**agent_certificate_service_delete**](docs/RepositoryCertificatesApi.md#agent_certificate_service_delete) | **DELETE** /gitops/api/v1/agents/{agentIdentifier}/certificates | Delete the certificates that match the RepositoryCertificateQuery
*RepositoryCertificatesApi* | [**agent_certificate_service_list**](docs/RepositoryCertificatesApi.md#agent_certificate_service_list) | **GET** /gitops/api/v1/agents/{agentIdentifier}/certificates | List all available repository certificates
*RepositoryCredentialsApi* | [**agent_repository_credentials_service_create_repository_credentials**](docs/RepositoryCredentialsApi.md#agent_repository_credentials_service_create_repository_credentials) | **POST** /gitops/api/v1/agents/{agentIdentifier}/repocreds | Create creates a new repository credential
*RepositoryCredentialsApi* | [**agent_repository_credentials_service_delete_repository_credentials**](docs/RepositoryCredentialsApi.md#agent_repository_credentials_service_delete_repository_credentials) | **DELETE** /gitops/api/v1/agents/{agentIdentifier}/repocreds/{identifier} | Delete deletes a repository credential
*RepositoryCredentialsApi* | [**agent_repository_credentials_service_get_credentials_for_repository_url**](docs/RepositoryCredentialsApi.md#agent_repository_credentials_service_get_credentials_for_repository_url) | **POST** /gitops/api/v1/agents/{agentIdentifier}/repocreds/get | Get returns a repository credential given its url
*RepositoryCredentialsApi* | [**agent_repository_credentials_service_get_repository_credentials**](docs/RepositoryCredentialsApi.md#agent_repository_credentials_service_get_repository_credentials) | **GET** /gitops/api/v1/agents/{agentIdentifier}/repocreds/{identifier} | Get returns a repository credential given its identifier
*RepositoryCredentialsApi* | [**agent_repository_credentials_service_list_repository_credentials**](docs/RepositoryCredentialsApi.md#agent_repository_credentials_service_list_repository_credentials) | **POST** /gitops/api/v1/repocreds | List repository credentials
*RepositoryCredentialsApi* | [**agent_repository_credentials_service_update_repository_credentials**](docs/RepositoryCredentialsApi.md#agent_repository_credentials_service_update_repository_credentials) | **PUT** /gitops/api/v1/agents/{agentIdentifier}/repocreds/{identifier} | Update updates a repository credential
*RoleAssignmentsApi* | [**bulk_delete_role_assignment**](docs/RoleAssignmentsApi.md#bulk_delete_role_assignment) | **POST** /authz/api/roleassignments/delete/batch | Bulk Delete Role Assignment
*RoleAssignmentsApi* | [**delete_role_assignment**](docs/RoleAssignmentsApi.md#delete_role_assignment) | **DELETE** /authz/api/roleassignments/{identifier} | Delete Role Assignment
*RoleAssignmentsApi* | [**get_filtered_role_assignment_by_scope_list**](docs/RoleAssignmentsApi.md#get_filtered_role_assignment_by_scope_list) | **POST** /authz/api/roleassignments/v2/filter | List Role Assignments by scope filter
*RoleAssignmentsApi* | [**get_filtered_role_assignment_list**](docs/RoleAssignmentsApi.md#get_filtered_role_assignment_list) | **POST** /authz/api/roleassignments/filter | List Role Assignments by filter
*RoleAssignmentsApi* | [**get_role_assignment**](docs/RoleAssignmentsApi.md#get_role_assignment) | **GET** /authz/api/roleassignments/{identifier} | Get Role Assignment
*RoleAssignmentsApi* | [**get_role_assignment_aggregate_list**](docs/RoleAssignmentsApi.md#get_role_assignment_aggregate_list) | **POST** /authz/api/roleassignments/aggregate | List Aggregated Role Assignments by filter
*RoleAssignmentsApi* | [**get_role_assignment_list**](docs/RoleAssignmentsApi.md#get_role_assignment_list) | **GET** /authz/api/roleassignments | List Role Assignments
*RoleAssignmentsApi* | [**post_role_assignment**](docs/RoleAssignmentsApi.md#post_role_assignment) | **POST** /authz/api/roleassignments | Create Role Assignment
*RoleAssignmentsApi* | [**post_role_assignments**](docs/RoleAssignmentsApi.md#post_role_assignments) | **POST** /authz/api/roleassignments/multi | Create Role Assignments
*RoleAssignmentsApi* | [**validate_role_assignment**](docs/RoleAssignmentsApi.md#validate_role_assignment) | **POST** /authz/api/roleassignments/validate | Validate Role Assignment
*RolesApi* | [**delete_role**](docs/RolesApi.md#delete_role) | **DELETE** /authz/api/roles/{identifier} | Delete Role
*RolesApi* | [**get_role**](docs/RolesApi.md#get_role) | **GET** /authz/api/roles/{identifier} | Get Role
*RolesApi* | [**get_role_list**](docs/RolesApi.md#get_role_list) | **GET** /authz/api/roles | List Roles
*RolesApi* | [**post_role**](docs/RolesApi.md#post_role) | **POST** /authz/api/roles | Create Role
*RolesApi* | [**put_role**](docs/RolesApi.md#put_role) | **PUT** /authz/api/roles/{identifier} | Update Role
*RuleApi* | [**clone_rule**](docs/RuleApi.md#clone_rule) | **POST** /ccm/api/governance/ruleClone | Clone a rule
*RuleApi* | [**delete_rule**](docs/RuleApi.md#delete_rule) | **DELETE** /ccm/api/governance/rule/{ruleID} | Delete a rule
*RuleApi* | [**enqueue_governance_job**](docs/RuleApi.md#enqueue_governance_job) | **POST** /ccm/api/governance/enqueueAdhoc | Enqueues job for execution
*RuleApi* | [**get_policies**](docs/RuleApi.md#get_policies) | **POST** /ccm/api/governance/rule/list | Fetch rules for account
*RuleApi* | [**governance_connector_list**](docs/RuleApi.md#governance_connector_list) | **GET** /ccm/api/governance/connectorList | connectors with governance enabled and valid permission
*RuleApi* | [**rule_schema**](docs/RuleApi.md#rule_schema) | **GET** /ccm/api/governance/ruleSchema | Get Schema for entity
*RuleApi* | [**update_rule**](docs/RuleApi.md#update_rule) | **PUT** /ccm/api/governance/rule | Update a Rule
*RuleApi* | [**validate_rule**](docs/RuleApi.md#validate_rule) | **POST** /ccm/api/governance/ruleValidate | Validate a rule
*RuleEnforcementApi* | [**add_rule_enforcement**](docs/RuleEnforcementApi.md#add_rule_enforcement) | **POST** /ccm/api/governance/enforcement | Add a new rule Enforcement 
*RuleEnforcementApi* | [**ccmget_execution_detail**](docs/RuleEnforcementApi.md#ccmget_execution_detail) | **POST** /ccm/api/governance/execution/details | Fetch Rule Enforcement execution details for account
*RuleEnforcementApi* | [**get_rule_enforcement**](docs/RuleEnforcementApi.md#get_rule_enforcement) | **POST** /ccm/api/governance/enforcement/list | Fetch Rule Enforcements for account
*RuleEnforcementApi* | [**get_rule_enforcement_count**](docs/RuleEnforcementApi.md#get_rule_enforcement_count) | **POST** /ccm/api/governance/enforcement/count | Fetch Rule Enforcement count for account
*SLOsApi* | [**get_error_budget_reset_history**](docs/SLOsApi.md#get_error_budget_reset_history) | **GET** /cv/api/slo/{identifier}/errorBudgetResetHistory | Get Error budget reset history
*SLOsApi* | [**get_metric_graph_for_slo**](docs/SLOsApi.md#get_metric_graph_for_slo) | **GET** /cv/api/v1/orgs/{org}/projects/{project}/metric-graph/{slo-identifier} | Get Metric Graph For SLO
*SLOsApi* | [**get_notification_rules_for_slo**](docs/SLOsApi.md#get_notification_rules_for_slo) | **GET** /cv/api/slo/{identifier}/notification-rules | Get notification rules for SLO
*SLOsApi* | [**get_service_level_objective_logs**](docs/SLOsApi.md#get_service_level_objective_logs) | **GET** /cv/api/slo/{identifier}/logs | Get SLO logs
*SLOsApi* | [**list_slo**](docs/SLOsApi.md#list_slo) | **GET** /cv/api/v1/orgs/{org}/projects/{project}/slo | List SLOs
*SLOsApi* | [**reset_error_budget**](docs/SLOsApi.md#reset_error_budget) | **POST** /cv/api/slo/{identifier}/resetErrorBudget | Reset Error budget history
*SLOsDashboardApi* | [**get_secondary_event_details**](docs/SLOsDashboardApi.md#get_secondary_event_details) | **GET** /cv/api/slo-dashboard/secondary-events-details | 
*SLOsDashboardApi* | [**get_secondary_events**](docs/SLOsDashboardApi.md#get_secondary_events) | **GET** /cv/api/slo-dashboard/secondary-events/{identifier} | 
*SLOsDashboardApi* | [**get_service_level_objectives_risk_count**](docs/SLOsDashboardApi.md#get_service_level_objectives_risk_count) | **GET** /cv/api/slo-dashboard/risk-count | Get all SLOs count by risk
*SLOsDashboardApi* | [**get_slo_associated_environment_identifiers**](docs/SLOsDashboardApi.md#get_slo_associated_environment_identifiers) | **GET** /cv/api/slo-dashboard/environment-identifiers | 
*SLOsDashboardApi* | [**get_slo_associated_monitored_services**](docs/SLOsDashboardApi.md#get_slo_associated_monitored_services) | **GET** /cv/api/slo-dashboard/monitored-services | 
*SLOsDashboardApi* | [**get_slo_consumption_breakdown_view**](docs/SLOsDashboardApi.md#get_slo_consumption_breakdown_view) | **GET** /cv/api/slo-dashboard/widget/{identifier}/consumption | Get SLO consumption breakdown
*SLOsDashboardApi* | [**get_slo_details**](docs/SLOsDashboardApi.md#get_slo_details) | **GET** /cv/api/slo-dashboard/widget/{identifier} | Get SLO dashboard details
*SLOsDashboardApi* | [**get_slo_health_list_view**](docs/SLOsDashboardApi.md#get_slo_health_list_view) | **GET** /cv/api/slo-dashboard/widgets/list | Get SLO list view
*SLOsDashboardApi* | [**get_slo_health_list_view_v2**](docs/SLOsDashboardApi.md#get_slo_health_list_view_v2) | **POST** /cv/api/slo-dashboard/widgets/list | Get SLO list view
*SMTPApi* | [**create_smtp_config**](docs/SMTPApi.md#create_smtp_config) | **POST** /ng/api/smtpConfig | Creates SMTP config
*SMTPApi* | [**delete_smtp_config**](docs/SMTPApi.md#delete_smtp_config) | **DELETE** /ng/api/smtpConfig/{identifier} | Delete Smtp Config by identifier
*SMTPApi* | [**get_smtp_config**](docs/SMTPApi.md#get_smtp_config) | **GET** /ng/api/smtpConfig | Gets Smtp config by accountId
*SMTPApi* | [**update_smtp**](docs/SMTPApi.md#update_smtp) | **PUT** /ng/api/smtpConfig | Updates the Smtp Config
*SMTPApi* | [**validate_connectivity**](docs/SMTPApi.md#validate_connectivity) | **POST** /ng/api/smtpConfig/validate-connectivity | Tests the config&#x27;s connectivity by sending a test email
*SMTPApi* | [**validate_name**](docs/SMTPApi.md#validate_name) | **POST** /ng/api/smtpConfig/validateName | Checks whether other connectors exist with the same name
*SecretManagersApi* | [**get_metadata**](docs/SecretManagersApi.md#get_metadata) | **POST** /ng/api/secret-managers/meta-data | Gets the metadata of Secret Manager
*SecretsApi* | [**delete_secret_v2**](docs/SecretsApi.md#delete_secret_v2) | **DELETE** /ng/api/v2/secrets/{identifier} | Deletes Secret by ID and Scope
*SecretsApi* | [**get_secret_v2**](docs/SecretsApi.md#get_secret_v2) | **GET** /ng/api/v2/secrets/{identifier} | Get the Secret by ID and Scope
*SecretsApi* | [**list_secrets_v2**](docs/SecretsApi.md#list_secrets_v2) | **GET** /ng/api/v2/secrets | Fetches the list of Secrets corresponding to the request&#x27;s filter criteria.
*SecretsApi* | [**list_secrets_v3**](docs/SecretsApi.md#list_secrets_v3) | **POST** /ng/api/v2/secrets/list | Fetches the list of Secrets corresponding to the request&#x27;s filter criteria.
*SecretsApi* | [**post_secret**](docs/SecretsApi.md#post_secret) | **POST** /ng/api/v2/secrets | Creates a Secret at given Scope
*SecretsApi* | [**post_secret_file_v2**](docs/SecretsApi.md#post_secret_file_v2) | **POST** /ng/api/v2/secrets/files | Creates a Secret File
*SecretsApi* | [**post_secret_via_yaml**](docs/SecretsApi.md#post_secret_via_yaml) | **POST** /ng/api/v2/secrets/yaml | Creates a secret via YAML
*SecretsApi* | [**put_secret**](docs/SecretsApi.md#put_secret) | **PUT** /ng/api/v2/secrets/{identifier} | Updates the Secret by ID and Scope
*SecretsApi* | [**put_secret_file_v2**](docs/SecretsApi.md#put_secret_file_v2) | **PUT** /ng/api/v2/secrets/files/{identifier} | Updates the Secret file by ID and Scope
*SecretsApi* | [**put_secret_via_yaml**](docs/SecretsApi.md#put_secret_via_yaml) | **PUT** /ng/api/v2/secrets/{identifier}/yaml | Updates the Secret by ID and Scope via YAML
*SecretsApi* | [**validate_secret**](docs/SecretsApi.md#validate_secret) | **POST** /ng/api/v2/secrets/validate | Validates Secret with the provided ID and Scope
*SecretsApi* | [**validate_secret_identifier_is_unique**](docs/SecretsApi.md#validate_secret_identifier_is_unique) | **GET** /ng/api/v2/secrets/validateUniqueIdentifier/{identifier} | Checks whether the identifier is unique or not
*ServiceLevelObjectiveApi* | [**get_metric_graph_for_slo**](docs/ServiceLevelObjectiveApi.md#get_metric_graph_for_slo) | **GET** /cv/api/v1/orgs/{org}/projects/{project}/metric-graph/{slo-identifier} | Get Metric Graph For SLO
*ServiceLevelObjectiveApi* | [**list_slo**](docs/ServiceLevelObjectiveApi.md#list_slo) | **GET** /cv/api/v1/orgs/{org}/projects/{project}/slo | List SLOs
*ServiceOverridesApi* | [**create_service_override**](docs/ServiceOverridesApi.md#create_service_override) | **POST** /ng/api/serviceOverrides | Create an ServiceOverride Entity
*ServiceOverridesApi* | [**delete_service_override1**](docs/ServiceOverridesApi.md#delete_service_override1) | **DELETE** /ng/api/serviceOverrides/{identifier} | Delete a ServiceOverride entity
*ServiceOverridesApi* | [**get_service_overrides**](docs/ServiceOverridesApi.md#get_service_overrides) | **GET** /ng/api/serviceOverrides/{identifier} | Gets Service Overrides by Identifier
*ServiceOverridesApi* | [**update_service_override**](docs/ServiceOverridesApi.md#update_service_override) | **PUT** /ng/api/serviceOverrides | Update an ServiceOverride Entity
*ServiceAccountApi* | [**create_service_account**](docs/ServiceAccountApi.md#create_service_account) | **POST** /ng/api/serviceaccount | Create a Service Account
*ServiceAccountApi* | [**delete_service_account**](docs/ServiceAccountApi.md#delete_service_account) | **DELETE** /ng/api/serviceaccount/{identifier} | Delete a Service Account
*ServiceAccountApi* | [**get_aggregated_service_account**](docs/ServiceAccountApi.md#get_aggregated_service_account) | **GET** /ng/api/serviceaccount/aggregate/{identifier} | Get Service Account In Scope
*ServiceAccountApi* | [**list_aggregated_service_accounts**](docs/ServiceAccountApi.md#list_aggregated_service_accounts) | **GET** /ng/api/serviceaccount/aggregate | List aggregated Service Accounts
*ServiceAccountApi* | [**list_service_account**](docs/ServiceAccountApi.md#list_service_account) | **GET** /ng/api/serviceaccount | Get Service Accounts
*ServiceAccountApi* | [**update_service_account**](docs/ServiceAccountApi.md#update_service_account) | **PUT** /ng/api/serviceaccount/{identifier} | Update a Service Account
*ServiceDashboardApi* | [**pipeline_execution_count**](docs/ServiceDashboardApi.md#pipeline_execution_count) | **GET** /ng/api/dashboard/getPipelineExecutionCount | Get pipeline execution count for a service with grouping support on artifact and deployment status
*ServicesApi* | [**create_service_v2**](docs/ServicesApi.md#create_service_v2) | **POST** /ng/api/servicesV2 | Create a Service
*ServicesApi* | [**create_services_v2**](docs/ServicesApi.md#create_services_v2) | **POST** /ng/api/servicesV2/batch | Create Services
*ServicesApi* | [**delete_service_v2**](docs/ServicesApi.md#delete_service_v2) | **DELETE** /ng/api/servicesV2/{serviceIdentifier} | Delete a Service by identifier
*ServicesApi* | [**get_service_access_list**](docs/ServicesApi.md#get_service_access_list) | **GET** /ng/api/servicesV2/list/access | Gets Service Access list
*ServicesApi* | [**get_service_list**](docs/ServicesApi.md#get_service_list) | **GET** /ng/api/servicesV2 | Gets Service list
*ServicesApi* | [**get_service_v2**](docs/ServicesApi.md#get_service_v2) | **GET** /ng/api/servicesV2/{serviceIdentifier} | Gets a Service by identifier
*ServicesApi* | [**hook_actions**](docs/ServicesApi.md#hook_actions) | **GET** /ng/api/servicesV2/hooks/actions | Retrieving the list of actions available for service hooks
*ServicesApi* | [**k8s_cmd_flags**](docs/ServicesApi.md#k8s_cmd_flags) | **GET** /ng/api/servicesV2/k8s/command-flags | Retrieving the list of Kubernetes Command Options
*ServicesApi* | [**kustomize_cmd_flags**](docs/ServicesApi.md#kustomize_cmd_flags) | **GET** /ng/api/servicesV2/kustomize/command-flags | Retrieving the list of Kustomize Command Flags
*ServicesApi* | [**update_service_v2**](docs/ServicesApi.md#update_service_v2) | **PUT** /ng/api/servicesV2 | Update a Service by identifier
*ServicesApi* | [**upsert_service_v2**](docs/ServicesApi.md#upsert_service_v2) | **PUT** /ng/api/servicesV2/upsert | Upsert a Service by identifier
*SettingApi* | [**get_setting_value**](docs/SettingApi.md#get_setting_value) | **GET** /ng/api/settings/{identifier} | Get a setting value by identifier
*SettingApi* | [**get_settings_list**](docs/SettingApi.md#get_settings_list) | **GET** /ng/api/settings | Get list of settings under the specified category
*SettingApi* | [**update_setting_value**](docs/SettingApi.md#update_setting_value) | **PUT** /ng/api/settings | Update settings
*SourceCodeManagerApi* | [**create_source_code_manager**](docs/SourceCodeManagerApi.md#create_source_code_manager) | **POST** /ng/api/source-code-manager | Creates Source Code Manager
*SourceCodeManagerApi* | [**delete_source_code_manager**](docs/SourceCodeManagerApi.md#delete_source_code_manager) | **DELETE** /ng/api/source-code-manager/{identifier} | Deletes the Source Code Manager corresponding to the specified Source Code Manager Id
*SourceCodeManagerApi* | [**get_source_code_managers**](docs/SourceCodeManagerApi.md#get_source_code_managers) | **GET** /ng/api/source-code-manager | Lists Source Code Managers for the given account
*SourceCodeManagerApi* | [**update_source_code_manager**](docs/SourceCodeManagerApi.md#update_source_code_manager) | **PUT** /ng/api/source-code-manager/{identifier} | Updates Source Code Manager Details with the given Source Code Manager Id
*SrmNotificationApi* | [**delete_notification_rule_data**](docs/SrmNotificationApi.md#delete_notification_rule_data) | **DELETE** /cv/api/notification-rule/{identifier} | 
*SrmNotificationApi* | [**get_notification_rule_data**](docs/SrmNotificationApi.md#get_notification_rule_data) | **GET** /cv/api/notification-rule/{identifier} | 
*SrmNotificationApi* | [**get_notification_rule_data1**](docs/SrmNotificationApi.md#get_notification_rule_data1) | **GET** /cv/api/notification-rule | 
*SrmNotificationApi* | [**save_notification_rule_data**](docs/SrmNotificationApi.md#save_notification_rule_data) | **POST** /cv/api/notification-rule | 
*SrmNotificationApi* | [**update_notification_rule_data**](docs/SrmNotificationApi.md#update_notification_rule_data) | **PUT** /cv/api/notification-rule/{identifier} | 
*TagsApi* | [**create_tag**](docs/TagsApi.md#create_tag) | **POST** /cf/admin/tags | Creates a Tag
*TagsApi* | [**delete_tag**](docs/TagsApi.md#delete_tag) | **DELETE** /cf/admin/tags/{identifier} | Delete a Tag
*TagsApi* | [**get_all_tags**](docs/TagsApi.md#get_all_tags) | **GET** /cf/admin/tags | Returns all Tags
*TagsApi* | [**get_tag**](docs/TagsApi.md#get_tag) | **GET** /cf/admin/tags/{identifier} | Returns a Tag
*TargetGroupsApi* | [**create_segment**](docs/TargetGroupsApi.md#create_segment) | **POST** /cf/admin/segments | Creates a Target Group
*TargetGroupsApi* | [**delete_segment**](docs/TargetGroupsApi.md#delete_segment) | **DELETE** /cf/admin/segments/{identifier} | Deletes a Target Group
*TargetGroupsApi* | [**get_all_segments**](docs/TargetGroupsApi.md#get_all_segments) | **GET** /cf/admin/segments | Returns all Target Groups
*TargetGroupsApi* | [**get_available_flags_for_segment**](docs/TargetGroupsApi.md#get_available_flags_for_segment) | **GET** /cf/admin/segments/{identifier}/available_flags | Returns Feature Flags that are available to be added to the given Target Group
*TargetGroupsApi* | [**get_segment**](docs/TargetGroupsApi.md#get_segment) | **GET** /cf/admin/segments/{identifier} | Returns Target Group details for the given identifier
*TargetGroupsApi* | [**get_segment_flags**](docs/TargetGroupsApi.md#get_segment_flags) | **GET** /cf/admin/segments/{identifier}/flags | Returns Feature Flags in a Target Group
*TargetGroupsApi* | [**patch_segment**](docs/TargetGroupsApi.md#patch_segment) | **PATCH** /cf/admin/segments/{identifier} | Updates a Target Group
*TargetsApi* | [**create_target**](docs/TargetsApi.md#create_target) | **POST** /cf/admin/targets | Creates a Target
*TargetsApi* | [**delete_target**](docs/TargetsApi.md#delete_target) | **DELETE** /cf/admin/targets/{identifier} | Deletes a Target
*TargetsApi* | [**get_all_targets**](docs/TargetsApi.md#get_all_targets) | **GET** /cf/admin/targets | Returns all Targets
*TargetsApi* | [**get_target**](docs/TargetsApi.md#get_target) | **GET** /cf/admin/targets/{identifier} | Returns details of a Target
*TargetsApi* | [**get_target_segments**](docs/TargetsApi.md#get_target_segments) | **GET** /cf/admin/targets/{identifier}/segments | Returns Target Groups for the given Target
*TargetsApi* | [**modify_target**](docs/TargetsApi.md#modify_target) | **PUT** /cf/admin/targets/{identifier} | Modifies a Target
*TargetsApi* | [**patch_target**](docs/TargetsApi.md#patch_target) | **PATCH** /cf/admin/targets/{identifier} | Updates a Target
*TargetsApi* | [**upload_targets**](docs/TargetsApi.md#upload_targets) | **POST** /cf/admin/targets/upload | Add Target details
*TemplatesApi* | [**create_template**](docs/TemplatesApi.md#create_template) | **POST** /template/api/templates | Create a Template
*TemplatesApi* | [**delete_template_version**](docs/TemplatesApi.md#delete_template_version) | **DELETE** /template/api/templates/{templateIdentifier}/{versionLabel} | Delete Template Version
*TemplatesApi* | [**get_refreshed_yaml**](docs/TemplatesApi.md#get_refreshed_yaml) | **POST** /template/api/refresh-template/refreshed-yaml | Get YAML with updated Template Inputs
*TemplatesApi* | [**get_template**](docs/TemplatesApi.md#get_template) | **GET** /template/api/templates/{templateIdentifier} | Get Template
*TemplatesApi* | [**get_template_input_set_yaml**](docs/TemplatesApi.md#get_template_input_set_yaml) | **GET** /template/api/templates/templateInputs/{templateIdentifier} | Gets Template Input Set YAML
*TemplatesApi* | [**get_template_metadata_list**](docs/TemplatesApi.md#get_template_metadata_list) | **POST** /template/api/templates/list-metadata | Gets all metadata of template list
*TemplatesApi* | [**move_template_configs**](docs/TemplatesApi.md#move_template_configs) | **POST** /template/api/templates/move-config/{templateIdentifier} | Move Template YAML from inline to remote
*TemplatesApi* | [**templatevalidate_template_inputs**](docs/TemplatesApi.md#templatevalidate_template_inputs) | **GET** /template/api/refresh-template/validate-template-inputs | Validate Template Inputs in a YAML
*TemplatesApi* | [**update_existing_template_version**](docs/TemplatesApi.md#update_existing_template_version) | **PUT** /template/api/templates/update/{templateIdentifier}/{versionLabel} | Update Template Version
*TemplatesApi* | [**update_git_details**](docs/TemplatesApi.md#update_git_details) | **POST** /template/api/templates/update/git-metadata/{templateIdentifier}/{versionLabel} | Update git metadata details for a remote template
*TemplatesApi* | [**update_stable_template**](docs/TemplatesApi.md#update_stable_template) | **PUT** /template/api/templates/updateStableTemplate/{templateIdentifier}/{versionLabel} | Update Stable Template Version
*TokenApi* | [**create_token**](docs/TokenApi.md#create_token) | **POST** /ng/api/token | Create a Token
*TokenApi* | [**delete_token**](docs/TokenApi.md#delete_token) | **DELETE** /ng/api/token/{identifier} | Delete a Token
*TokenApi* | [**list_aggregated_tokens**](docs/TokenApi.md#list_aggregated_tokens) | **GET** /ng/api/token/aggregate | List all Tokens
*TokenApi* | [**rotate_token**](docs/TokenApi.md#rotate_token) | **POST** /ng/api/token/rotate/{identifier} | Rotate a Token
*TokenApi* | [**update_token**](docs/TokenApi.md#update_token) | **PUT** /ng/api/token/{identifier} | Update a Token
*TokenApi* | [**validate_token**](docs/TokenApi.md#validate_token) | **POST** /ng/api/token/validate | Validate a Token
*TriggersApi* | [**create_trigger**](docs/TriggersApi.md#create_trigger) | **POST** /pipeline/api/triggers | Creates Trigger for triggering target pipeline identifier.
*TriggersApi* | [**delete_trigger**](docs/TriggersApi.md#delete_trigger) | **DELETE** /pipeline/api/triggers/{triggerIdentifier} | Deletes Trigger by identifier.
*TriggersApi* | [**get_list_for_target**](docs/TriggersApi.md#get_list_for_target) | **GET** /pipeline/api/triggers | Gets the paginated list of triggers for accountIdentifier, orgIdentifier, projectIdentifier, targetIdentifier.
*TriggersApi* | [**get_trigger**](docs/TriggersApi.md#get_trigger) | **GET** /pipeline/api/triggers/{triggerIdentifier} | Gets the trigger by accountIdentifier, orgIdentifier, projectIdentifier, targetIdentifier and triggerIdentifier.
*TriggersApi* | [**get_trigger_catalog**](docs/TriggersApi.md#get_trigger_catalog) | **GET** /pipeline/api/triggers/catalog | Lists all Triggers
*TriggersApi* | [**get_trigger_details**](docs/TriggersApi.md#get_trigger_details) | **GET** /pipeline/api/triggers/{triggerIdentifier}/details | Fetches Trigger details for a specific accountIdentifier, orgIdentifier, projectIdentifier, targetIdentifier, triggerIdentifier.
*TriggersApi* | [**trigger_event_history**](docs/TriggersApi.md#trigger_event_history) | **GET** /pipeline/api/triggers/{triggerIdentifier}/eventHistory | Get event history for a trigger
*TriggersApi* | [**update_trigger**](docs/TriggersApi.md#update_trigger) | **PUT** /pipeline/api/triggers/{triggerIdentifier} | Updates trigger for pipeline with target pipeline identifier.
*TriggersEventsApi* | [**polled_response_trigger_identifier**](docs/TriggersEventsApi.md#polled_response_trigger_identifier) | **GET** /pipeline/api/triggers/eventHistory/polledResponse/{triggerIdentifier} | Get all the polled response for a given trigger
*TriggersEventsApi* | [**trigger_event_history_build_source_type**](docs/TriggersEventsApi.md#trigger_event_history_build_source_type) | **GET** /pipeline/api/triggers/eventHistory/artifact-manifest-info | Get artifact and manifest trigger event history based on build source type
*TriggersEventsApi* | [**trigger_event_history_new**](docs/TriggersEventsApi.md#trigger_event_history_new) | **GET** /pipeline/api/triggers/eventHistory/{triggerIdentifier} | Get event history for a trigger
*TriggersEventsApi* | [**trigger_history_event_correlation**](docs/TriggersEventsApi.md#trigger_history_event_correlation) | **GET** /pipeline/api/triggers/eventHistory/eventCorrelation/{eventCorrelationId} | Get Trigger history event correlation
*TriggersEventsApi* | [**trigger_history_event_correlation_v2**](docs/TriggersEventsApi.md#trigger_history_event_correlation_v2) | **GET** /pipeline/api/triggers/eventHistory/v2/eventCorrelation/{eventCorrelationId} | Get Trigger history event correlation V2
*UsageApi* | [**ccmdownload_active_service_csv_report**](docs/UsageApi.md#ccmdownload_active_service_csv_report) | **GET** /ccm/api/usage/cd/active-services/csv/download | Download CSV Active Services report
*UsageApi* | [**ccmget_cd_license_usage_for_service_instances**](docs/UsageApi.md#ccmget_cd_license_usage_for_service_instances) | **GET** /ccm/api/usage/CD/serviceInstancesLicense | Gets License Usage By Module, Timestamp, and Account Identifier
*UsageApi* | [**ccmget_cd_license_usage_for_services**](docs/UsageApi.md#ccmget_cd_license_usage_for_services) | **GET** /ccm/api/usage/CD/servicesLicense | Gets License Usage By Module, Timestamp, and Account Identifier
*UsageApi* | [**ccmget_license_usage**](docs/UsageApi.md#ccmget_license_usage) | **GET** /ccm/api/usage/{module} | Gets License Usage By Module, Timestamp, and Account Identifier
*UsageApi* | [**cvget_license_usage**](docs/UsageApi.md#cvget_license_usage) | **GET** /cv/api/usage/CV | 
*UsageApi* | [**download_active_monitored_service_csv_report**](docs/UsageApi.md#download_active_monitored_service_csv_report) | **GET** /cv/api/usage/SRM/active-monitored-services/csv/download | Download CSV Active Monitored Services report
*UsageApi* | [**download_active_service_csv_report**](docs/UsageApi.md#download_active_service_csv_report) | **GET** /ng/api/usage/cd/active-services/csv/download | Download CSV Active Services report
*UsageApi* | [**download_active_service_monitored_csv_report**](docs/UsageApi.md#download_active_service_monitored_csv_report) | **GET** /cv/api/usage/SRM/active-services-monitored/csv/download | Download CSV Active Services Monitored report
*UsageApi* | [**get_cd_license_usage_for_service_instances**](docs/UsageApi.md#get_cd_license_usage_for_service_instances) | **GET** /ng/api/usage/CD/serviceInstancesLicense | Gets License Usage By Module, Timestamp, and Account Identifier
*UsageApi* | [**get_cd_license_usage_for_services**](docs/UsageApi.md#get_cd_license_usage_for_services) | **GET** /ng/api/usage/CD/servicesLicense | Gets License Usage By Module, Timestamp, and Account Identifier
*UsageApi* | [**get_license_usage**](docs/UsageApi.md#get_license_usage) | **GET** /ng/api/usage/{module} | Gets License Usage By Module, Timestamp, and Account Identifier
*UsageApi* | [**get_srm_license_usage**](docs/UsageApi.md#get_srm_license_usage) | **GET** /cv/api/usage/SRM | 
*UsageApi* | [**list_srm_active_monitored_services**](docs/UsageApi.md#list_srm_active_monitored_services) | **POST** /cv/api/usage/SRM/active-monitored-services | Returns a List of active monitored services along with identifier,Active Monitored Services Count and other details
*UserApi* | [**add_users**](docs/UserApi.md#add_users) | **POST** /ng/api/user/users | Add user(s) to scope
*UserApi* | [**change_user_password**](docs/UserApi.md#change_user_password) | **PUT** /ng/api/user/password | Change user password
*UserApi* | [**check_if_last_admin**](docs/UserApi.md#check_if_last_admin) | **GET** /ng/api/user/last-admin | Check if user is last admin
*UserApi* | [**disable_t_two_factor_auth**](docs/UserApi.md#disable_t_two_factor_auth) | **PUT** /ng/api/user/disable-two-factor-auth | Disable two factor authentication
*UserApi* | [**enable_two_factor_auth**](docs/UserApi.md#enable_two_factor_auth) | **PUT** /ng/api/user/enable-two-factor-auth | Enable two factor authentication
*UserApi* | [**get_aggregated_user**](docs/UserApi.md#get_aggregated_user) | **GET** /ng/api/user/aggregate/{userId} | Get detailed user information
*UserApi* | [**get_aggregated_users**](docs/UserApi.md#get_aggregated_users) | **POST** /ng/api/user/aggregate | Get list of users
*UserApi* | [**get_current_user_info**](docs/UserApi.md#get_current_user_info) | **GET** /ng/api/user/currentUser | Get Current User Info
*UserApi* | [**get_two_factor_auth_settings**](docs/UserApi.md#get_two_factor_auth_settings) | **GET** /ng/api/user/two-factor-auth/{authMechanism} | Gets Two Factor Auth Settings
*UserApi* | [**get_users**](docs/UserApi.md#get_users) | **POST** /ng/api/user/batch | Get users list
*UserApi* | [**remove_user**](docs/UserApi.md#remove_user) | **DELETE** /ng/api/user/{userId} | Remove user from scope
*UserApi* | [**reset2fa**](docs/UserApi.md#reset2fa) | **GET** /ng/api/user/reset-two-factor-auth/{userId} | Reset two factor authorization
*UserApi* | [**unlock_user**](docs/UserApi.md#unlock_user) | **PUT** /ng/api/user/unlock-user/{userId} | Unlock user
*UserApi* | [**update_user_info**](docs/UserApi.md#update_user_info) | **PUT** /ng/api/user | Update User
*UserApi* | [**update_user_info1**](docs/UserApi.md#update_user_info1) | **PUT** /ng/api/user/{userId} | Update User
*UserGroupApi* | [**copy_user_group**](docs/UserGroupApi.md#copy_user_group) | **PUT** /ng/api/user-groups/copy | Copy User Group
*UserGroupApi* | [**delete_member**](docs/UserGroupApi.md#delete_member) | **DELETE** /ng/api/user-groups/{identifier}/member/{userIdentifier} | Remove user from User Group
*UserGroupApi* | [**delete_user_group**](docs/UserGroupApi.md#delete_user_group) | **DELETE** /ng/api/user-groups/{identifier} | Delete a User Group in an account/org/project
*UserGroupApi* | [**get_batch_users_group_list**](docs/UserGroupApi.md#get_batch_users_group_list) | **POST** /ng/api/user-groups/batch | List User Groups by filter
*UserGroupApi* | [**get_filtered_user_groups_list**](docs/UserGroupApi.md#get_filtered_user_groups_list) | **POST** /ng/api/user-groups/filter | Get filtered User Groups
*UserGroupApi* | [**get_inheriting_child_scope_list**](docs/UserGroupApi.md#get_inheriting_child_scope_list) | **GET** /ng/api/user-groups/{identifier}/scopes | Get Inheriting Child Scopes
*UserGroupApi* | [**get_member**](docs/UserGroupApi.md#get_member) | **GET** /ng/api/user-groups/{identifier}/member/{userIdentifier} | Check user membership
*UserGroupApi* | [**get_user_group**](docs/UserGroupApi.md#get_user_group) | **GET** /ng/api/user-groups/{identifier} | Get User Group
*UserGroupApi* | [**get_user_group_list**](docs/UserGroupApi.md#get_user_group_list) | **GET** /ng/api/user-groups | List the User Groups in an account/org/project
*UserGroupApi* | [**get_user_list_in_user_group**](docs/UserGroupApi.md#get_user_list_in_user_group) | **POST** /ng/api/user-groups/{identifier}/users | List users in User Group
*UserGroupApi* | [**link_user_group_to_ldap**](docs/UserGroupApi.md#link_user_group_to_ldap) | **PUT** /ng/api/user-groups/{userGroupId}/link/ldap/{ldapId} | Link LDAP Group to the User Group to an account/org/project
*UserGroupApi* | [**link_user_group_to_saml**](docs/UserGroupApi.md#link_user_group_to_saml) | **PUT** /ng/api/user-groups/{userGroupId}/link/saml/{samlId} | Link SAML Group to the User Group in an account/org/project
*UserGroupApi* | [**post_user_group**](docs/UserGroupApi.md#post_user_group) | **POST** /ng/api/user-groups | Create User Group
*UserGroupApi* | [**post_user_group_v2**](docs/UserGroupApi.md#post_user_group_v2) | **POST** /ng/api/v2/user-groups | Create User Group
*UserGroupApi* | [**put_member**](docs/UserGroupApi.md#put_member) | **PUT** /ng/api/user-groups/{identifier}/member/{userIdentifier} | Add user to User Group
*UserGroupApi* | [**put_user_group**](docs/UserGroupApi.md#put_user_group) | **PUT** /ng/api/user-groups | Update User Group
*UserGroupApi* | [**put_user_group_v2**](docs/UserGroupApi.md#put_user_group_v2) | **PUT** /ng/api/v2/user-groups | Update User Group
*UserGroupApi* | [**unlink_user_groupfrom_sso**](docs/UserGroupApi.md#unlink_user_groupfrom_sso) | **PUT** /ng/api/user-groups/{userGroupId}/unlink | Unlink SSO Group from the User Group in an account/org/project
*ValidateHostApi* | [**validate_hosts**](docs/ValidateHostApi.md#validate_hosts) | **POST** /ng/api/host-validation | Validates hosts connectivity credentials
*VariablesApi* | [**create_variable**](docs/VariablesApi.md#create_variable) | **POST** /ng/api/variables | Creates a Variable.
*VariablesApi* | [**delete_variable**](docs/VariablesApi.md#delete_variable) | **DELETE** /ng/api/variables/{identifier} | Deletes Variable by ID.
*VariablesApi* | [**get_variable**](docs/VariablesApi.md#get_variable) | **GET** /ng/api/variables/{identifier} | Get the Variable by scope identifiers and variable identifier.
*VariablesApi* | [**get_variable_list**](docs/VariablesApi.md#get_variable_list) | **GET** /ng/api/variables | Fetches the list of Variables.
*VariablesApi* | [**update_variable**](docs/VariablesApi.md#update_variable) | **PUT** /ng/api/variables | Updates the Variable.
*WebhookEventHandlerApi* | [**process_webhook_event**](docs/WebhookEventHandlerApi.md#process_webhook_event) | **POST** /ng/api/webhook | Process event payload for webhook triggers.
*WebhookTriggersApi* | [**fetch_webhook_details**](docs/WebhookTriggersApi.md#fetch_webhook_details) | **GET** /pipeline/api/webhook/triggerProcessingDetails | Gets webhook event processing details for input eventId.
*WebhookTriggersApi* | [**fetch_webhook_execution_details**](docs/WebhookTriggersApi.md#fetch_webhook_execution_details) | **GET** /pipeline/api/webhook/triggerExecutionDetails/{eventId} | Gets webhook event processing details for input eventId.
*WebhookTriggersApi* | [**pipelineprocess_webhook_event**](docs/WebhookTriggersApi.md#pipelineprocess_webhook_event) | **POST** /pipeline/api/webhook/trigger | Handles event payload for webhook triggers.
*WebhookTriggersApi* | [**process_custom_webhook_event**](docs/WebhookTriggersApi.md#process_custom_webhook_event) | **POST** /pipeline/api/webhook/custom | Handles event payload for custom webhook triggers.
*WebhookTriggersApi* | [**process_custom_webhook_event_v2**](docs/WebhookTriggersApi.md#process_custom_webhook_event_v2) | **POST** /pipeline/api/webhook/custom/v2 | Handles event payload for custom webhook triggers.
*WebhookTriggersApi* | [**process_custom_webhook_event_v3**](docs/WebhookTriggersApi.md#process_custom_webhook_event_v3) | **POST** /pipeline/api/webhook/custom/{webhookToken}/v3 | Handles event payload for custom webhook triggers.
*ZendeskApi* | [**create_zendesk_ticket**](docs/ZendeskApi.md#create_zendesk_ticket) | **POST** /resourcegroup/api/zendesk | create zendesk ticket for given user
*ZendeskApi* | [**get_coveo_token**](docs/ZendeskApi.md#get_coveo_token) | **GET** /resourcegroup/api/zendesk/token | get short live token for Coveo
*AidaApi* | [**aida_analyze**](docs/AidaApi.md#aida_analyze) | **POST** /pm/api/v1/aida/analyze | 
*AidaApi* | [**aida_generate**](docs/AidaApi.md#aida_generate) | **POST** /pm/api/v1/aida/generate | 
*DashboardApi* | [**dashboard_metrics**](docs/DashboardApi.md#dashboard_metrics) | **GET** /pm/api/v1/dashboard | 
*EvaluateApi* | [**evaluate_evaluate**](docs/EvaluateApi.md#evaluate_evaluate) | **POST** /pm/api/v1/evaluate | 
*EvaluationsApi* | [**evaluations_find**](docs/EvaluationsApi.md#evaluations_find) | **GET** /pm/api/v1/evaluations/{id} | 
*EvaluationsApi* | [**evaluations_list**](docs/EvaluationsApi.md#evaluations_list) | **GET** /pm/api/v1/evaluations | 
*ExamplesApi* | [**examples_list**](docs/ExamplesApi.md#examples_list) | **GET** /pm/api/v1/examples | 
*PoliciesApi* | [**policies_create**](docs/PoliciesApi.md#policies_create) | **POST** /pm/api/v1/policies | 
*PoliciesApi* | [**policies_delete**](docs/PoliciesApi.md#policies_delete) | **DELETE** /pm/api/v1/policies/{identifier} | 
*PoliciesApi* | [**policies_find**](docs/PoliciesApi.md#policies_find) | **GET** /pm/api/v1/policies/{identifier} | 
*PoliciesApi* | [**policies_list**](docs/PoliciesApi.md#policies_list) | **GET** /pm/api/v1/policies | 
*PoliciesApi* | [**policies_update**](docs/PoliciesApi.md#policies_update) | **PATCH** /pm/api/v1/policies/{identifier} | 
*PolicysetsApi* | [**policysets_create**](docs/PolicysetsApi.md#policysets_create) | **POST** /pm/api/v1/policysets | 
*PolicysetsApi* | [**policysets_delete**](docs/PolicysetsApi.md#policysets_delete) | **DELETE** /pm/api/v1/policysets/{identifier} | 
*PolicysetsApi* | [**policysets_find**](docs/PolicysetsApi.md#policysets_find) | **GET** /pm/api/v1/policysets/{identifier} | 
*PolicysetsApi* | [**policysets_list**](docs/PolicysetsApi.md#policysets_list) | **GET** /pm/api/v1/policysets | 
*PolicysetsApi* | [**policysets_update**](docs/PolicysetsApi.md#policysets_update) | **PATCH** /pm/api/v1/policysets/{identifier} | 
*SystemApi* | [**system_health**](docs/SystemApi.md#system_health) | **GET** /pm/api/v1/system/health | 
*SystemApi* | [**system_version**](docs/SystemApi.md#system_version) | **GET** /pm/api/v1/system/version | 
*TasApi* | [**get_tas_organizations**](docs/TasApi.md#get_tas_organizations) | **GET** /ng/api/tas/organizations | Return the Tas organizations
*TasApi* | [**get_tas_spaces**](docs/TasApi.md#get_tas_spaces) | **GET** /ng/api/tas/space | Return the Tas spaces
*TasApi* | [**get_tas_spaces_v2**](docs/TasApi.md#get_tas_spaces_v2) | **GET** /ng/api/tas/v2/space | Return the Tas spaces

## Documentation For Models

 - [ACLAggregateFilter](docs/ACLAggregateFilter.md)
 - [ASGMinimal](docs/ASGMinimal.md)
 - [AWSViewPreferences](docs/AWSViewPreferences.md)
 - [AbortedBy](docs/AbortedBy.md)
 - [AbstractServiceLevelObjective](docs/AbstractServiceLevelObjective.md)
 - [AccessCheckRequest](docs/AccessCheckRequest.md)
 - [AccessCheckResponse](docs/AccessCheckResponse.md)
 - [AccessControl](docs/AccessControl.md)
 - [AccessDeniedError](docs/AccessDeniedError.md)
 - [AccessPoint](docs/AccessPoint.md)
 - [AccessPointActivityResponse](docs/AccessPointActivityResponse.md)
 - [AccessPointMeta](docs/AccessPointMeta.md)
 - [AccessPointMetaDns](docs/AccessPointMetaDns.md)
 - [AccessPointMetaDnsRoute53](docs/AccessPointMetaDnsRoute53.md)
 - [Account](docs/Account.md)
 - [AccountSettingConfig](docs/AccountSettingConfig.md)
 - [AccountSettingResponse](docs/AccountSettingResponse.md)
 - [AccountSettings](docs/AccountSettings.md)
 - [Action](docs/Action.md)
 - [ActiveMonitoredService](docs/ActiveMonitoredService.md)
 - [ActiveServiceMonitoredFilterParams](docs/ActiveServiceMonitoredFilterParams.md)
 - [AddCollaboratorAuditEventData](docs/AddCollaboratorAuditEventData.md)
 - [AddUsersDTO](docs/AddUsersDTO.md)
 - [AddUsersResponse](docs/AddUsersResponse.md)
 - [AdditionalMetadata](docs/AdditionalMetadata.md)
 - [AdviserIssuer](docs/AdviserIssuer.md)
 - [AffectedEntity](docs/AffectedEntity.md)
 - [AgentMtlsEndpointDetails](docs/AgentMtlsEndpointDetails.md)
 - [AgentMtlsEndpointRequest](docs/AgentMtlsEndpointRequest.md)
 - [AggregateStatus](docs/AggregateStatus.md)
 - [AgreementType](docs/AgreementType.md)
 - [AlertThreshold](docs/AlertThreshold.md)
 - [AllEntitiesRule](docs/AllEntitiesRule.md)
 - [AllResourcesOfAccountResponse](docs/AllResourcesOfAccountResponse.md)
 - [AllowedSourceType](docs/AllowedSourceType.md)
 - [Ambiance](docs/Ambiance.md)
 - [AnalysisDTO](docs/AnalysisDTO.md)
 - [AnalyzeRequestBody](docs/AnalyzeRequestBody.md)
 - [AnalyzeResponse](docs/AnalyzeResponse.md)
 - [AnnotationInstance](docs/AnnotationInstance.md)
 - [AnnotationInstanceDetails](docs/AnnotationInstanceDetails.md)
 - [AnomaliesSummaryDTO](docs/AnomaliesSummaryDTO.md)
 - [AnomalyData](docs/AnomalyData.md)
 - [AnomalyFeedback](docs/AnomalyFeedback.md)
 - [AnomalyFilterProperties](docs/AnomalyFilterProperties.md)
 - [AnomalySummary](docs/AnomalySummary.md)
 - [AnyOfHealthSourceSpec](docs/AnyOfHealthSourceSpec.md)
 - [ApiCallLogDTO](docs/ApiCallLogDTO.md)
 - [ApiCallLogDTOField](docs/ApiCallLogDTOField.md)
 - [ApiFilestoreBody](docs/ApiFilestoreBody.md)
 - [ApiKey](docs/ApiKey.md)
 - [ApiKeyAggregate](docs/ApiKeyAggregate.md)
 - [ApiKeyRequestType](docs/ApiKeyRequestType.md)
 - [ApiKeys](docs/ApiKeys.md)
 - [ApiZendeskBody](docs/ApiZendeskBody.md)
 - [Apicorev1Event](docs/Apicorev1Event.md)
 - [AppDMetricDefinitions](docs/AppDMetricDefinitions.md)
 - [AppDynamicsConnectorDTO](docs/AppDynamicsConnectorDTO.md)
 - [AppDynamicsHealthSource](docs/AppDynamicsHealthSource.md)
 - [AppdynamicsClientIdConnectorSpec](docs/AppdynamicsClientIdConnectorSpec.md)
 - [AppdynamicsConnectorSpec](docs/AppdynamicsConnectorSpec.md)
 - [ApplicationBudgetScope](docs/ApplicationBudgetScope.md)
 - [ApplicationSettingsConfiguration](docs/ApplicationSettingsConfiguration.md)
 - [ApplicationsApplication](docs/ApplicationsApplication.md)
 - [ApplicationsApplicationCondition](docs/ApplicationsApplicationCondition.md)
 - [ApplicationsApplicationCreateRequest](docs/ApplicationsApplicationCreateRequest.md)
 - [ApplicationsApplicationDeleteRequest](docs/ApplicationsApplicationDeleteRequest.md)
 - [ApplicationsApplicationDestination](docs/ApplicationsApplicationDestination.md)
 - [ApplicationsApplicationList](docs/ApplicationsApplicationList.md)
 - [ApplicationsApplicationManifestQuery](docs/ApplicationsApplicationManifestQuery.md)
 - [ApplicationsApplicationPatchRequest](docs/ApplicationsApplicationPatchRequest.md)
 - [ApplicationsApplicationPodLogsQuery](docs/ApplicationsApplicationPodLogsQuery.md)
 - [ApplicationsApplicationQuery](docs/ApplicationsApplicationQuery.md)
 - [ApplicationsApplicationResourceDeleteRequest](docs/ApplicationsApplicationResourceDeleteRequest.md)
 - [ApplicationsApplicationResourceEventsQuery](docs/ApplicationsApplicationResourceEventsQuery.md)
 - [ApplicationsApplicationResourcePatchRequest](docs/ApplicationsApplicationResourcePatchRequest.md)
 - [ApplicationsApplicationResourceRequest](docs/ApplicationsApplicationResourceRequest.md)
 - [ApplicationsApplicationResourceResponse](docs/ApplicationsApplicationResourceResponse.md)
 - [ApplicationsApplicationResponse](docs/ApplicationsApplicationResponse.md)
 - [ApplicationsApplicationRollbackRequest](docs/ApplicationsApplicationRollbackRequest.md)
 - [ApplicationsApplicationSource](docs/ApplicationsApplicationSource.md)
 - [ApplicationsApplicationSourceDirectory](docs/ApplicationsApplicationSourceDirectory.md)
 - [ApplicationsApplicationSourceHelm](docs/ApplicationsApplicationSourceHelm.md)
 - [ApplicationsApplicationSourceJsonnet](docs/ApplicationsApplicationSourceJsonnet.md)
 - [ApplicationsApplicationSourceKsonnet](docs/ApplicationsApplicationSourceKsonnet.md)
 - [ApplicationsApplicationSourceKustomize](docs/ApplicationsApplicationSourceKustomize.md)
 - [ApplicationsApplicationSourcePlugin](docs/ApplicationsApplicationSourcePlugin.md)
 - [ApplicationsApplicationSpec](docs/ApplicationsApplicationSpec.md)
 - [ApplicationsApplicationStatus](docs/ApplicationsApplicationStatus.md)
 - [ApplicationsApplicationSummary](docs/ApplicationsApplicationSummary.md)
 - [ApplicationsApplicationSyncRequest](docs/ApplicationsApplicationSyncRequest.md)
 - [ApplicationsApplicationSyncWindow](docs/ApplicationsApplicationSyncWindow.md)
 - [ApplicationsApplicationSyncWindowsQuery](docs/ApplicationsApplicationSyncWindowsQuery.md)
 - [ApplicationsApplicationSyncWindowsResponse](docs/ApplicationsApplicationSyncWindowsResponse.md)
 - [ApplicationsApplicationTree](docs/ApplicationsApplicationTree.md)
 - [ApplicationsApplicationUpdateRequest](docs/ApplicationsApplicationUpdateRequest.md)
 - [ApplicationsApplicationUpdateSpecRequest](docs/ApplicationsApplicationUpdateSpecRequest.md)
 - [ApplicationsApplicationWatchEvent](docs/ApplicationsApplicationWatchEvent.md)
 - [ApplicationsBackoff](docs/ApplicationsBackoff.md)
 - [ApplicationsComparedTo](docs/ApplicationsComparedTo.md)
 - [ApplicationsEnvEntry](docs/ApplicationsEnvEntry.md)
 - [ApplicationsHealthStatus](docs/ApplicationsHealthStatus.md)
 - [ApplicationsHelmFileParameter](docs/ApplicationsHelmFileParameter.md)
 - [ApplicationsHelmParameter](docs/ApplicationsHelmParameter.md)
 - [ApplicationsHostInfo](docs/ApplicationsHostInfo.md)
 - [ApplicationsHostResourceInfo](docs/ApplicationsHostResourceInfo.md)
 - [ApplicationsInfo](docs/ApplicationsInfo.md)
 - [ApplicationsInfoItem](docs/ApplicationsInfoItem.md)
 - [ApplicationsJsonnetVar](docs/ApplicationsJsonnetVar.md)
 - [ApplicationsKsonnetParameter](docs/ApplicationsKsonnetParameter.md)
 - [ApplicationsLogEntry](docs/ApplicationsLogEntry.md)
 - [ApplicationsManagedResourcesResponse](docs/ApplicationsManagedResourcesResponse.md)
 - [ApplicationsOperation](docs/ApplicationsOperation.md)
 - [ApplicationsOperationInitiator](docs/ApplicationsOperationInitiator.md)
 - [ApplicationsOperationState](docs/ApplicationsOperationState.md)
 - [ApplicationsOperationTerminateRequest](docs/ApplicationsOperationTerminateRequest.md)
 - [ApplicationsOperationTerminateResponse](docs/ApplicationsOperationTerminateResponse.md)
 - [ApplicationsResourceAction](docs/ApplicationsResourceAction.md)
 - [ApplicationsResourceActionParam](docs/ApplicationsResourceActionParam.md)
 - [ApplicationsResourceActionRunRequest](docs/ApplicationsResourceActionRunRequest.md)
 - [ApplicationsResourceActionsListResponse](docs/ApplicationsResourceActionsListResponse.md)
 - [ApplicationsResourceDiff](docs/ApplicationsResourceDiff.md)
 - [ApplicationsResourceIgnoreDifferences](docs/ApplicationsResourceIgnoreDifferences.md)
 - [ApplicationsResourceNetworkingInfo](docs/ApplicationsResourceNetworkingInfo.md)
 - [ApplicationsResourceNode](docs/ApplicationsResourceNode.md)
 - [ApplicationsResourceRef](docs/ApplicationsResourceRef.md)
 - [ApplicationsResourceResult](docs/ApplicationsResourceResult.md)
 - [ApplicationsResourceStatus](docs/ApplicationsResourceStatus.md)
 - [ApplicationsResourcesQuery](docs/ApplicationsResourcesQuery.md)
 - [ApplicationsRetryStrategy](docs/ApplicationsRetryStrategy.md)
 - [ApplicationsRevisionHistory](docs/ApplicationsRevisionHistory.md)
 - [ApplicationsRevisionMetadataQuery](docs/ApplicationsRevisionMetadataQuery.md)
 - [ApplicationsSyncOperation](docs/ApplicationsSyncOperation.md)
 - [ApplicationsSyncOperationResource](docs/ApplicationsSyncOperationResource.md)
 - [ApplicationsSyncOperationResult](docs/ApplicationsSyncOperationResult.md)
 - [ApplicationsSyncOptions](docs/ApplicationsSyncOptions.md)
 - [ApplicationsSyncPolicy](docs/ApplicationsSyncPolicy.md)
 - [ApplicationsSyncPolicyAutomated](docs/ApplicationsSyncPolicyAutomated.md)
 - [ApplicationsSyncStatus](docs/ApplicationsSyncStatus.md)
 - [ApplicationsSyncStrategy](docs/ApplicationsSyncStrategy.md)
 - [ApplicationsSyncStrategyApply](docs/ApplicationsSyncStrategyApply.md)
 - [ApplicationsSyncStrategyHook](docs/ApplicationsSyncStrategyHook.md)
 - [Applicationv1alpha1RepositoryCertificate](docs/Applicationv1alpha1RepositoryCertificate.md)
 - [Applicationv1alpha1RepositoryCertificateList](docs/Applicationv1alpha1RepositoryCertificateList.md)
 - [AppprojectsAppProject](docs/AppprojectsAppProject.md)
 - [AppprojectsAppProjectList](docs/AppprojectsAppProjectList.md)
 - [AppprojectsAppProjectSpec](docs/AppprojectsAppProjectSpec.md)
 - [AppprojectsAppProjectStatus](docs/AppprojectsAppProjectStatus.md)
 - [AppprojectsApplicationDestination](docs/AppprojectsApplicationDestination.md)
 - [AppprojectsJWTToken](docs/AppprojectsJWTToken.md)
 - [AppprojectsJWTTokens](docs/AppprojectsJWTTokens.md)
 - [AppprojectsOrphanedResourceKey](docs/AppprojectsOrphanedResourceKey.md)
 - [AppprojectsOrphanedResourcesMonitorSettings](docs/AppprojectsOrphanedResourcesMonitorSettings.md)
 - [AppprojectsProjectRole](docs/AppprojectsProjectRole.md)
 - [AppprojectsSignatureKey](docs/AppprojectsSignatureKey.md)
 - [AppprojectsSyncWindow](docs/AppprojectsSyncWindow.md)
 - [ApprovalInstanceDetailsDTO](docs/ApprovalInstanceDetailsDTO.md)
 - [ApprovalInstanceResponse](docs/ApprovalInstanceResponse.md)
 - [ApprovalInstanceResponseBody](docs/ApprovalInstanceResponseBody.md)
 - [ApprovalUserGroup](docs/ApprovalUserGroup.md)
 - [ApproverInput](docs/ApproverInput.md)
 - [ApproverInputInfo](docs/ApproverInputInfo.md)
 - [Approvers](docs/Approvers.md)
 - [ArtifactoryAnonymousConnectorSpec](docs/ArtifactoryAnonymousConnectorSpec.md)
 - [ArtifactoryAuthCredentials](docs/ArtifactoryAuthCredentials.md)
 - [ArtifactoryAuthentication](docs/ArtifactoryAuthentication.md)
 - [ArtifactoryConnector](docs/ArtifactoryConnector.md)
 - [ArtifactoryConnectorSpec](docs/ArtifactoryConnectorSpec.md)
 - [ArtifactoryEncryptedConnectorSpec](docs/ArtifactoryEncryptedConnectorSpec.md)
 - [ArtifactoryUsernamePasswordAuth](docs/ArtifactoryUsernamePasswordAuth.md)
 - [AsyncChainExecutableResponse](docs/AsyncChainExecutableResponse.md)
 - [AsyncChainExecutableResponseOrBuilder](docs/AsyncChainExecutableResponseOrBuilder.md)
 - [AsyncExecutableResponse](docs/AsyncExecutableResponse.md)
 - [AsyncExecutableResponseOrBuilder](docs/AsyncExecutableResponseOrBuilder.md)
 - [AttributeFilter](docs/AttributeFilter.md)
 - [AuditEnvironment](docs/AuditEnvironment.md)
 - [AuditError](docs/AuditError.md)
 - [AuditErrorMetadata](docs/AuditErrorMetadata.md)
 - [AuditEvent](docs/AuditEvent.md)
 - [AuditEventDTO](docs/AuditEventDTO.md)
 - [AuditEventData](docs/AuditEventData.md)
 - [AuditFailure](docs/AuditFailure.md)
 - [AuditFilterProperties](docs/AuditFilterProperties.md)
 - [AuditFilterPropertiesV1DTO](docs/AuditFilterPropertiesV1DTO.md)
 - [AuditHttpRequestInfo](docs/AuditHttpRequestInfo.md)
 - [AuditPrincipal](docs/AuditPrincipal.md)
 - [AuditRequestMetadata](docs/AuditRequestMetadata.md)
 - [AuditResource](docs/AuditResource.md)
 - [AuditResourceScope](docs/AuditResourceScope.md)
 - [AuditResponseMessage](docs/AuditResponseMessage.md)
 - [AuditRoleBinding](docs/AuditRoleBinding.md)
 - [AuthenticationInfo](docs/AuthenticationInfo.md)
 - [AuthenticationInfoDTO](docs/AuthenticationInfoDTO.md)
 - [AuthenticationSettingsResponse](docs/AuthenticationSettingsResponse.md)
 - [AuthenticationsettingsSamlmetadatauploadBody](docs/AuthenticationsettingsSamlmetadatauploadBody.md)
 - [AuthenticationsettingsSamlmetadatauploadBody1](docs/AuthenticationsettingsSamlmetadatauploadBody1.md)
 - [AuthzError](docs/AuthzError.md)
 - [AuthzErrorMetadata](docs/AuthzErrorMetadata.md)
 - [AuthzFailure](docs/AuthzFailure.md)
 - [AuthzPrincipal](docs/AuthzPrincipal.md)
 - [AuthzResourceFilter](docs/AuthzResourceFilter.md)
 - [AuthzResponseMessage](docs/AuthzResponseMessage.md)
 - [AuthzRoleAssignment](docs/AuthzRoleAssignment.md)
 - [AuthzRoleAssignmentResponse](docs/AuthzRoleAssignmentResponse.md)
 - [AuthzScope](docs/AuthzScope.md)
 - [AuthzValidationResult](docs/AuthzValidationResult.md)
 - [AutoApproval](docs/AutoApproval.md)
 - [AutoCUDConfig](docs/AutoCUDConfig.md)
 - [AutoCUDSetup](docs/AutoCUDSetup.md)
 - [AwsAccessKeyConnectorSpec](docs/AwsAccessKeyConnectorSpec.md)
 - [AwsCodeCommitAuthentication](docs/AwsCodeCommitAuthentication.md)
 - [AwsCodeCommitConnector](docs/AwsCodeCommitConnector.md)
 - [AwsCodeCommitConnectorSpec](docs/AwsCodeCommitConnectorSpec.md)
 - [AwsCodeCommitCredentials](docs/AwsCodeCommitCredentials.md)
 - [AwsCodeCommitHttpsCredentials](docs/AwsCodeCommitHttpsCredentials.md)
 - [AwsCodeCommitHttpsCredentialsSpec](docs/AwsCodeCommitHttpsCredentialsSpec.md)
 - [AwsCodeCommitSecretKeyAccessKey](docs/AwsCodeCommitSecretKeyAccessKey.md)
 - [AwsConnector](docs/AwsConnector.md)
 - [AwsCredential](docs/AwsCredential.md)
 - [AwsCredentialSpec](docs/AwsCredentialSpec.md)
 - [AwsCurAttributes](docs/AwsCurAttributes.md)
 - [AwsEncryptedAccessKeyConnectorSpec](docs/AwsEncryptedAccessKeyConnectorSpec.md)
 - [AwsEqualJitterBackoffStrategy](docs/AwsEqualJitterBackoffStrategy.md)
 - [AwsFixedDelayBackoffStrategy](docs/AwsFixedDelayBackoffStrategy.md)
 - [AwsFullJitterBackoffStrategy](docs/AwsFullJitterBackoffStrategy.md)
 - [AwsIAMRoleConnectorSpec](docs/AwsIAMRoleConnectorSpec.md)
 - [AwsIRSAConnectorSpec](docs/AwsIRSAConnectorSpec.md)
 - [AwsKmsAccessKeyConnectorSpec](docs/AwsKmsAccessKeyConnectorSpec.md)
 - [AwsKmsAssumeIAMConnectorSpec](docs/AwsKmsAssumeIAMConnectorSpec.md)
 - [AwsKmsAssumeSTSConnectorSpec](docs/AwsKmsAssumeSTSConnectorSpec.md)
 - [AwsKmsConnector](docs/AwsKmsConnector.md)
 - [AwsKmsConnectorCredential](docs/AwsKmsConnectorCredential.md)
 - [AwsKmsCredentialSpec](docs/AwsKmsCredentialSpec.md)
 - [AwsKmsCredentialSpecAssumeIAM](docs/AwsKmsCredentialSpecAssumeIAM.md)
 - [AwsKmsCredentialSpecAssumeSTS](docs/AwsKmsCredentialSpecAssumeSTS.md)
 - [AwsKmsCredentialSpecManualConfig](docs/AwsKmsCredentialSpecManualConfig.md)
 - [AwsManualConfigSpec](docs/AwsManualConfigSpec.md)
 - [AwsPrometheusHealthSource](docs/AwsPrometheusHealthSource.md)
 - [AwsRecommendationAdhocDTO](docs/AwsRecommendationAdhocDTO.md)
 - [AwsS3StreamingDestinationSpecDTO](docs/AwsS3StreamingDestinationSpecDTO.md)
 - [AwsSMCredentialSpecAssumeIAM](docs/AwsSMCredentialSpecAssumeIAM.md)
 - [AwsSMCredentialSpecAssumeSTS](docs/AwsSMCredentialSpecAssumeSTS.md)
 - [AwsSMCredentialSpecManualConfig](docs/AwsSMCredentialSpecManualConfig.md)
 - [AwsSdkClientBackOffStrategySpec](docs/AwsSdkClientBackOffStrategySpec.md)
 - [AwsSdkClientBackoffStrategy](docs/AwsSdkClientBackoffStrategy.md)
 - [AwsSecretManager](docs/AwsSecretManager.md)
 - [AwsSecretManagerAccessKeyConnectorSpec](docs/AwsSecretManagerAccessKeyConnectorSpec.md)
 - [AwsSecretManagerAssumeIAMConnectorSpec](docs/AwsSecretManagerAssumeIAMConnectorSpec.md)
 - [AwsSecretManagerAssumeSTSConnectorSpec](docs/AwsSecretManagerAssumeSTSConnectorSpec.md)
 - [AwsSecretManagerCredential](docs/AwsSecretManagerCredential.md)
 - [AwsSecretManagerCredentialSpec](docs/AwsSecretManagerCredentialSpec.md)
 - [AzureArtifactsAuthentication](docs/AzureArtifactsAuthentication.md)
 - [AzureArtifactsConnector](docs/AzureArtifactsConnector.md)
 - [AzureArtifactsHttpCredentials](docs/AzureArtifactsHttpCredentials.md)
 - [AzureArtifactsUsernameToken](docs/AzureArtifactsUsernameToken.md)
 - [AzureAuth](docs/AzureAuth.md)
 - [AzureAuthCredential](docs/AzureAuthCredential.md)
 - [AzureClientCertificateConnectorSpec](docs/AzureClientCertificateConnectorSpec.md)
 - [AzureClientKeyCert](docs/AzureClientKeyCert.md)
 - [AzureClientSecretKey](docs/AzureClientSecretKey.md)
 - [AzureClientSecretKeyConnectorSpec](docs/AzureClientSecretKeyConnectorSpec.md)
 - [AzureConnector](docs/AzureConnector.md)
 - [AzureCredential](docs/AzureCredential.md)
 - [AzureCredentialSpec](docs/AzureCredentialSpec.md)
 - [AzureInheritFromDelegateDetails](docs/AzureInheritFromDelegateDetails.md)
 - [AzureInheritFromDelegateSystemAssignedManagedIdentityConnectorSpec](docs/AzureInheritFromDelegateSystemAssignedManagedIdentityConnectorSpec.md)
 - [AzureInheritFromDelegateUserAssignedManagedIdentityConnectorSpec](docs/AzureInheritFromDelegateUserAssignedManagedIdentityConnectorSpec.md)
 - [AzureKeyVaultConnector](docs/AzureKeyVaultConnector.md)
 - [AzureMSIAuth](docs/AzureMSIAuth.md)
 - [AzureManualDetails](docs/AzureManualDetails.md)
 - [AzureRecommendationAdhocDTO](docs/AzureRecommendationAdhocDTO.md)
 - [AzureRepoApiAccess](docs/AzureRepoApiAccess.md)
 - [AzureRepoApiAccessSpec](docs/AzureRepoApiAccessSpec.md)
 - [AzureRepoAuthentication](docs/AzureRepoAuthentication.md)
 - [AzureRepoConfig](docs/AzureRepoConfig.md)
 - [AzureRepoCredentials](docs/AzureRepoCredentials.md)
 - [AzureRepoHttpCredentials](docs/AzureRepoHttpCredentials.md)
 - [AzureRepoHttpCredentialsSpec](docs/AzureRepoHttpCredentialsSpec.md)
 - [AzureRepoSshCredentials](docs/AzureRepoSshCredentials.md)
 - [AzureRepoTokenSpec](docs/AzureRepoTokenSpec.md)
 - [AzureRepoUsernameToken](docs/AzureRepoUsernameToken.md)
 - [AzureSystemAssignedMSIAuth](docs/AzureSystemAssignedMSIAuth.md)
 - [AzureUserAssignedMSIAuth](docs/AzureUserAssignedMSIAuth.md)
 - [AzureVmDTO](docs/AzureVmDTO.md)
 - [AzureVmRecommendation](docs/AzureVmRecommendation.md)
 - [BIDashboardSummary](docs/BIDashboardSummary.md)
 - [BambooAuthCredentialsDTO](docs/BambooAuthCredentialsDTO.md)
 - [BambooAuthenticationDTO](docs/BambooAuthenticationDTO.md)
 - [BambooConnector](docs/BambooConnector.md)
 - [BambooUserNamePasswordDTO](docs/BambooUserNamePasswordDTO.md)
 - [BaseSSHSpec](docs/BaseSSHSpec.md)
 - [BaseWinRmSpec](docs/BaseWinRmSpec.md)
 - [BillingExportSpec](docs/BillingExportSpec.md)
 - [BitbucketApiAccess](docs/BitbucketApiAccess.md)
 - [BitbucketAuthentication](docs/BitbucketAuthentication.md)
 - [BitbucketConnector](docs/BitbucketConnector.md)
 - [BitbucketCredentials](docs/BitbucketCredentials.md)
 - [BitbucketHttpCredentials](docs/BitbucketHttpCredentials.md)
 - [BitbucketHttpCredentialsSpec](docs/BitbucketHttpCredentialsSpec.md)
 - [BitbucketOauth](docs/BitbucketOauth.md)
 - [BitbucketSshCredentials](docs/BitbucketSshCredentials.md)
 - [BitbucketUsernamePassword](docs/BitbucketUsernamePassword.md)
 - [BitbucketUsernameTokenApiAccess](docs/BitbucketUsernameTokenApiAccess.md)
 - [Board](docs/Board.md)
 - [Budget](docs/Budget.md)
 - [BudgetCostData](docs/BudgetCostData.md)
 - [BudgetData](docs/BudgetData.md)
 - [BudgetGroup](docs/BudgetGroup.md)
 - [BudgetGroupChildEntityDTO](docs/BudgetGroupChildEntityDTO.md)
 - [BudgetMonthlyBreakdown](docs/BudgetMonthlyBreakdown.md)
 - [BudgetScope](docs/BudgetScope.md)
 - [BudgetSummary](docs/BudgetSummary.md)
 - [BuildDetails](docs/BuildDetails.md)
 - [BuildInfo](docs/BuildInfo.md)
 - [BuildInfoOrBuilder](docs/BuildInfoOrBuilder.md)
 - [BurnRate](docs/BurnRate.md)
 - [BusinessMapping](docs/BusinessMapping.md)
 - [BusinessMappingListDTO](docs/BusinessMappingListDTO.md)
 - [ByteString](docs/ByteString.md)
 - [CCMAggregation](docs/CCMAggregation.md)
 - [CCMEcsEntity](docs/CCMEcsEntity.md)
 - [CCMGroupBy](docs/CCMGroupBy.md)
 - [CCMJiraCreateDTO](docs/CCMJiraCreateDTO.md)
 - [CCMJiraDetails](docs/CCMJiraDetails.md)
 - [CCMK8sEntity](docs/CCMK8sEntity.md)
 - [CCMOverview](docs/CCMOverview.md)
 - [CCMRecommendationFilterProperties](docs/CCMRecommendationFilterProperties.md)
 - [CCMServiceNowCreateDTO](docs/CCMServiceNowCreateDTO.md)
 - [CCMServiceNowDetails](docs/CCMServiceNowDetails.md)
 - [CCMSort](docs/CCMSort.md)
 - [CCMTimeFilter](docs/CCMTimeFilter.md)
 - [CEAwsConnector](docs/CEAwsConnector.md)
 - [CEAzureConnector](docs/CEAzureConnector.md)
 - [CEKubernetesClusterConfigDTO](docs/CEKubernetesClusterConfigDTO.md)
 - [CEReportSchedule](docs/CEReportSchedule.md)
 - [CEView](docs/CEView.md)
 - [CEViewFolder](docs/CEViewFolder.md)
 - [CVNGEmailChannelSpec](docs/CVNGEmailChannelSpec.md)
 - [CVNGLog](docs/CVNGLog.md)
 - [CVNGLogTag](docs/CVNGLogTag.md)
 - [CVNGMSTeamsChannelSpec](docs/CVNGMSTeamsChannelSpec.md)
 - [CVNGNotificationChannel](docs/CVNGNotificationChannel.md)
 - [CVNGNotificationChannelSpec](docs/CVNGNotificationChannelSpec.md)
 - [CVNGPagerDutyChannelSpec](docs/CVNGPagerDutyChannelSpec.md)
 - [CVNGSlackChannelSpec](docs/CVNGSlackChannelSpec.md)
 - [CacheResponseMetadata](docs/CacheResponseMetadata.md)
 - [CacheResponseMetadataDTO](docs/CacheResponseMetadataDTO.md)
 - [CalenderSLOTargetSpec](docs/CalenderSLOTargetSpec.md)
 - [CalenderSpec](docs/CalenderSpec.md)
 - [CannyBoardsResponse](docs/CannyBoardsResponse.md)
 - [CannyPostBody](docs/CannyPostBody.md)
 - [CannyResponse](docs/CannyResponse.md)
 - [CategoryCountDetails](docs/CategoryCountDetails.md)
 - [CcmBitbucketConnector](docs/CcmBitbucketConnector.md)
 - [CcmConnectorConnectivityDetails](docs/CcmConnectorConnectivityDetails.md)
 - [CcmConnectorResponse](docs/CcmConnectorResponse.md)
 - [CcmDockerConnector](docs/CcmDockerConnector.md)
 - [CcmEntityGitDetails](docs/CcmEntityGitDetails.md)
 - [CcmError](docs/CcmError.md)
 - [CcmErrorDetail](docs/CcmErrorDetail.md)
 - [CcmErrorMetadata](docs/CcmErrorMetadata.md)
 - [CcmExecutionDetails](docs/CcmExecutionDetails.md)
 - [CcmGitConfig](docs/CcmGitConfig.md)
 - [CcmGithubConnector](docs/CcmGithubConnector.md)
 - [CcmGovernanceMetadata](docs/CcmGovernanceMetadata.md)
 - [CcmK8sConnectorResponse](docs/CcmK8sConnectorResponse.md)
 - [CcmK8sMetaDTO](docs/CcmK8sMetaDTO.md)
 - [CcmK8sMetaInfo](docs/CcmK8sMetaInfo.md)
 - [CcmK8sMetaInfoResponseDTO](docs/CcmK8sMetaInfoResponseDTO.md)
 - [CcmPolicyMetadata](docs/CcmPolicyMetadata.md)
 - [CcmPolicySetMetadata](docs/CcmPolicySetMetadata.md)
 - [CcmPolicySetMetadataOrBuilder](docs/CcmPolicySetMetadataOrBuilder.md)
 - [CertificateData](docs/CertificateData.md)
 - [CertificateRepositoryCertificateCreateRequest](docs/CertificateRepositoryCertificateCreateRequest.md)
 - [CertificateRepositoryCertificateQuery](docs/CertificateRepositoryCertificateQuery.md)
 - [CertificatesRepositoryCertificate](docs/CertificatesRepositoryCertificate.md)
 - [CertificatesRepositoryCertificateList](docs/CertificatesRepositoryCertificateList.md)
 - [CfApiKey](docs/CfApiKey.md)
 - [CfError](docs/CfError.md)
 - [CfGitDetails](docs/CfGitDetails.md)
 - [CfService](docs/CfService.md)
 - [ChangeImpactConditionSpec](docs/ChangeImpactConditionSpec.md)
 - [ChangeObservedConditionSpec](docs/ChangeObservedConditionSpec.md)
 - [ChangeSourceDTO](docs/ChangeSourceDTO.md)
 - [ChangeSourceSpec](docs/ChangeSourceSpec.md)
 - [ChangeSummaryDTO](docs/ChangeSummaryDTO.md)
 - [ChaosAuditEventData](docs/ChaosAuditEventData.md)
 - [ChartResponse](docs/ChartResponse.md)
 - [Child](docs/Child.md)
 - [ChildChainExecutableResponse](docs/ChildChainExecutableResponse.md)
 - [ChildChainExecutableResponseOrBuilder](docs/ChildChainExecutableResponseOrBuilder.md)
 - [ChildExecutableResponse](docs/ChildExecutableResponse.md)
 - [ChildExecutableResponseOrBuilder](docs/ChildExecutableResponseOrBuilder.md)
 - [ChildExecutionDetail](docs/ChildExecutionDetail.md)
 - [ChildOrBuilder](docs/ChildOrBuilder.md)
 - [ChildrenExecutableResponse](docs/ChildrenExecutableResponse.md)
 - [ChildrenExecutableResponseOrBuilder](docs/ChildrenExecutableResponseOrBuilder.md)
 - [Clause](docs/Clause.md)
 - [CloneRuleDTO](docs/CloneRuleDTO.md)
 - [CloudWatchMetricDefinition](docs/CloudWatchMetricDefinition.md)
 - [CloudWatchMetricsHealthSource](docs/CloudWatchMetricsHealthSource.md)
 - [ClusterBasicDTO](docs/ClusterBasicDTO.md)
 - [ClusterBatchRequest](docs/ClusterBatchRequest.md)
 - [ClusterBatchResponse](docs/ClusterBatchResponse.md)
 - [ClusterBudgetScope](docs/ClusterBudgetScope.md)
 - [ClusterCostDetails](docs/ClusterCostDetails.md)
 - [ClusterCostDetailsQueryParams](docs/ClusterCostDetailsQueryParams.md)
 - [ClusterRecommendationAccuracy](docs/ClusterRecommendationAccuracy.md)
 - [ClusterRequest](docs/ClusterRequest.md)
 - [ClusterResponse](docs/ClusterResponse.md)
 - [ClustersAWSAuthConfig](docs/ClustersAWSAuthConfig.md)
 - [ClustersCluster](docs/ClustersCluster.md)
 - [ClustersClusterCacheInfo](docs/ClustersClusterCacheInfo.md)
 - [ClustersClusterConfig](docs/ClustersClusterConfig.md)
 - [ClustersClusterCreateRequest](docs/ClustersClusterCreateRequest.md)
 - [ClustersClusterID](docs/ClustersClusterID.md)
 - [ClustersClusterInfo](docs/ClustersClusterInfo.md)
 - [ClustersClusterList](docs/ClustersClusterList.md)
 - [ClustersClusterQuery](docs/ClustersClusterQuery.md)
 - [ClustersClusterResponse](docs/ClustersClusterResponse.md)
 - [ClustersClusterUpdateRequest](docs/ClustersClusterUpdateRequest.md)
 - [ClustersExecProviderConfig](docs/ClustersExecProviderConfig.md)
 - [ClustersTLSClientConfig](docs/ClustersTLSClientConfig.md)
 - [CommonsConnectionState](docs/CommonsConnectionState.md)
 - [CompositeServiceLevelObjectiveSpec](docs/CompositeServiceLevelObjectiveSpec.md)
 - [Condition](docs/Condition.md)
 - [ConfigFile](docs/ConfigFile.md)
 - [ConfigFileAttributeStepParameters](docs/ConfigFileAttributeStepParameters.md)
 - [ConfigFileAttributes](docs/ConfigFileAttributes.md)
 - [ConfigFileWrapper](docs/ConfigFileWrapper.md)
 - [ConnectionStringsConfiguration](docs/ConnectionStringsConfiguration.md)
 - [Connector](docs/Connector.md)
 - [Connector2](docs/Connector2.md)
 - [ConnectorActivityDetails](docs/ConnectorActivityDetails.md)
 - [ConnectorCatalogueItem](docs/ConnectorCatalogueItem.md)
 - [ConnectorCatalogueResponse](docs/ConnectorCatalogueResponse.md)
 - [ConnectorConfig](docs/ConnectorConfig.md)
 - [ConnectorConnectivityDetail](docs/ConnectorConnectivityDetail.md)
 - [ConnectorConnectivityDetails](docs/ConnectorConnectivityDetails.md)
 - [ConnectorFilterProperties](docs/ConnectorFilterProperties.md)
 - [ConnectorInfo](docs/ConnectorInfo.md)
 - [ConnectorRequest](docs/ConnectorRequest.md)
 - [ConnectorResponse](docs/ConnectorResponse.md)
 - [ConnectorResponse1](docs/ConnectorResponse1.md)
 - [ConnectorSettings](docs/ConnectorSettings.md)
 - [ConnectorSpec](docs/ConnectorSpec.md)
 - [ConnectorStatistics](docs/ConnectorStatistics.md)
 - [ConnectorStatusStats](docs/ConnectorStatusStats.md)
 - [ConnectorTestConnectionErrorDetail](docs/ConnectorTestConnectionErrorDetail.md)
 - [ConnectorTestConnectionResponse](docs/ConnectorTestConnectionResponse.md)
 - [ConnectorTypeStats](docs/ConnectorTypeStats.md)
 - [ConnectorValidationResult](docs/ConnectorValidationResult.md)
 - [ContainerHistogramDTO](docs/ContainerHistogramDTO.md)
 - [ContainerRecommendation](docs/ContainerRecommendation.md)
 - [ContainerSvc](docs/ContainerSvc.md)
 - [CoolDownMetaFailureResponse](docs/CoolDownMetaFailureResponse.md)
 - [CoolDownMetaSuccessResponse](docs/CoolDownMetaSuccessResponse.md)
 - [CoolDownOption](docs/CoolDownOption.md)
 - [Cost](docs/Cost.md)
 - [CostCategoryDeleteDTO](docs/CostCategoryDeleteDTO.md)
 - [CostDetailsQueryParams](docs/CostDetailsQueryParams.md)
 - [CostOverview](docs/CostOverview.md)
 - [CostTarget](docs/CostTarget.md)
 - [CountGroupedOnArtifact](docs/CountGroupedOnArtifact.md)
 - [CountGroupedOnService](docs/CountGroupedOnService.md)
 - [CountGroupedOnStatus](docs/CountGroupedOnStatus.md)
 - [CountServiceDTO](docs/CountServiceDTO.md)
 - [CoveoResponseDTO](docs/CoveoResponseDTO.md)
 - [CreateAccessPointResponse](docs/CreateAccessPointResponse.md)
 - [CreateGitXWebhookRequest](docs/CreateGitXWebhookRequest.md)
 - [CreateGitXWebhookResponse](docs/CreateGitXWebhookResponse.md)
 - [CreateOrganizationRequest](docs/CreateOrganizationRequest.md)
 - [CreatePerspectiveFolderDTO](docs/CreatePerspectiveFolderDTO.md)
 - [CreateProjectRequest](docs/CreateProjectRequest.md)
 - [CreateRequestBody](docs/CreateRequestBody.md)
 - [CreateRequestBody2](docs/CreateRequestBody2.md)
 - [CreateResourceGroupRequest](docs/CreateResourceGroupRequest.md)
 - [CreateRoleRequest](docs/CreateRoleRequest.md)
 - [CreateRuleDTO](docs/CreateRuleDTO.md)
 - [CreateRuleEnforcementDTO](docs/CreateRuleEnforcementDTO.md)
 - [CriteriaSpecDTO](docs/CriteriaSpecDTO.md)
 - [CriteriaSpecWrapper](docs/CriteriaSpecWrapper.md)
 - [CrossAccountAccess](docs/CrossAccountAccess.md)
 - [CumulativeSavings](docs/CumulativeSavings.md)
 - [CumulativeSavingsResponse](docs/CumulativeSavingsResponse.md)
 - [CurrentOrUpcomingWindow](docs/CurrentOrUpcomingWindow.md)
 - [CustomDeploymentInfraResponseDTO](docs/CustomDeploymentInfraResponseDTO.md)
 - [CustomDeploymentRefreshYamlDTO](docs/CustomDeploymentRefreshYamlDTO.md)
 - [CustomDeploymentVariableProperties](docs/CustomDeploymentVariableProperties.md)
 - [CustomDeploymentVariableResponseDTO](docs/CustomDeploymentVariableResponseDTO.md)
 - [CustomDeploymentYamlDTO](docs/CustomDeploymentYamlDTO.md)
 - [CustomDeploymentYamlRequestDTO](docs/CustomDeploymentYamlRequestDTO.md)
 - [CustomHealthConnectorDTO](docs/CustomHealthConnectorDTO.md)
 - [CustomHealthKeyAndValue](docs/CustomHealthKeyAndValue.md)
 - [CustomHealthLogDefinition](docs/CustomHealthLogDefinition.md)
 - [CustomHealthMetricDefinition](docs/CustomHealthMetricDefinition.md)
 - [CustomHealthRequestDefinition](docs/CustomHealthRequestDefinition.md)
 - [CustomHealthSourceLog](docs/CustomHealthSourceLog.md)
 - [CustomHealthSourceMetric](docs/CustomHealthSourceMetric.md)
 - [CustomSecretManager](docs/CustomSecretManager.md)
 - [CvError](docs/CvError.md)
 - [CvErrorMetadata](docs/CvErrorMetadata.md)
 - [CvFailure](docs/CvFailure.md)
 - [CvResponseDTOListServiceResponse](docs/CvResponseDTOListServiceResponse.md)
 - [CvResponseMessage](docs/CvResponseMessage.md)
 - [CvRestResponseBoolean](docs/CvRestResponseBoolean.md)
 - [CvServiceResponse](docs/CvServiceResponse.md)
 - [DashboardDownloadResponse](docs/DashboardDownloadResponse.md)
 - [DashboardMetrics](docs/DashboardMetrics.md)
 - [DashboardPipelineExecution](docs/DashboardPipelineExecution.md)
 - [DashboardsErrorResponse](docs/DashboardsErrorResponse.md)
 - [DataCollectionFailureInstanceDetails](docs/DataCollectionFailureInstanceDetails.md)
 - [DataPoint](docs/DataPoint.md)
 - [DataPoints](docs/DataPoints.md)
 - [DatadogConnectorDTO](docs/DatadogConnectorDTO.md)
 - [DatadogLogHealthSource](docs/DatadogLogHealthSource.md)
 - [DatadogLogHealthSourceQueryDTO](docs/DatadogLogHealthSourceQueryDTO.md)
 - [DatadogMetricHealthDefinition](docs/DatadogMetricHealthDefinition.md)
 - [DatadogMetricHealthSource](docs/DatadogMetricHealthSource.md)
 - [DelegateConnectionDetails](docs/DelegateConnectionDetails.md)
 - [DelegateDeleteResponse](docs/DelegateDeleteResponse.md)
 - [DelegateDownloadRequest](docs/DelegateDownloadRequest.md)
 - [DelegateFilterPropertiesDTO](docs/DelegateFilterPropertiesDTO.md)
 - [DelegateGroupDTO](docs/DelegateGroupDTO.md)
 - [DelegateGroupDetails](docs/DelegateGroupDetails.md)
 - [DelegateGroupListing](docs/DelegateGroupListing.md)
 - [DelegateGroupTags](docs/DelegateGroupTags.md)
 - [DelegateInfo](docs/DelegateInfo.md)
 - [DelegateInner](docs/DelegateInner.md)
 - [DelegateListResponse](docs/DelegateListResponse.md)
 - [DelegateReplica](docs/DelegateReplica.md)
 - [DelegateSetupDetails](docs/DelegateSetupDetails.md)
 - [DelegateTokenDetails](docs/DelegateTokenDetails.md)
 - [DeleteAccessPointPayload](docs/DeleteAccessPointPayload.md)
 - [DeploymentImpactReportConditionSpec](docs/DeploymentImpactReportConditionSpec.md)
 - [DeploymentVerificationDTO](docs/DeploymentVerificationDTO.md)
 - [Descriptor](docs/Descriptor.md)
 - [DescriptorProto](docs/DescriptorProto.md)
 - [DescriptorProtoOrBuilder](docs/DescriptorProtoOrBuilder.md)
 - [Distribution](docs/Distribution.md)
 - [DockerAuthCredentials](docs/DockerAuthCredentials.md)
 - [DockerAuthentication](docs/DockerAuthentication.md)
 - [DockerConnector](docs/DockerConnector.md)
 - [DockerUserNamePassword](docs/DockerUserNamePassword.md)
 - [Document](docs/Document.md)
 - [Downtime](docs/Downtime.md)
 - [DowntimeDuration](docs/DowntimeDuration.md)
 - [DowntimeHistoryView](docs/DowntimeHistoryView.md)
 - [DowntimeInstanceDetails](docs/DowntimeInstanceDetails.md)
 - [DowntimeListView](docs/DowntimeListView.md)
 - [DowntimeRecurrence](docs/DowntimeRecurrence.md)
 - [DowntimeResponse](docs/DowntimeResponse.md)
 - [DowntimeSpec](docs/DowntimeSpec.md)
 - [DowntimeSpecDTO](docs/DowntimeSpecDTO.md)
 - [DowntimeStatus](docs/DowntimeStatus.md)
 - [DowntimeStatusDetails](docs/DowntimeStatusDetails.md)
 - [DynatraceConnectorDTO](docs/DynatraceConnectorDTO.md)
 - [DynatraceHealthSource](docs/DynatraceHealthSource.md)
 - [DynatraceMetricDefinition](docs/DynatraceMetricDefinition.md)
 - [EC2InstanceDTO](docs/EC2InstanceDTO.md)
 - [EC2InstanceRecommendation](docs/EC2InstanceRecommendation.md)
 - [ECSRecommendationDTO](docs/ECSRecommendationDTO.md)
 - [ELKConnectorDTO](docs/ELKConnectorDTO.md)
 - [ELKHealthSource](docs/ELKHealthSource.md)
 - [ELKHealthSourceQueryDTO](docs/ELKHealthSourceQueryDTO.md)
 - [EdgeLayoutList](docs/EdgeLayoutList.md)
 - [EmailConfigDTO](docs/EmailConfigDTO.md)
 - [EmbeddedUser](docs/EmbeddedUser.md)
 - [EmbeddedUserDetailsDTO](docs/EmbeddedUserDetailsDTO.md)
 - [EnforcementCount](docs/EnforcementCount.md)
 - [EnforcementCountDTO](docs/EnforcementCountDTO.md)
 - [EnforcementCountRequest](docs/EnforcementCountRequest.md)
 - [EntitiesRule](docs/EntitiesRule.md)
 - [EntityDetail](docs/EntityDetail.md)
 - [EntityDetailProtoDTO](docs/EntityDetailProtoDTO.md)
 - [EntityDetails](docs/EntityDetails.md)
 - [EntityGitDetails](docs/EntityGitDetails.md)
 - [EntityGitDetails1](docs/EntityGitDetails1.md)
 - [EntityGitMetadata](docs/EntityGitMetadata.md)
 - [EntityGitMetadataOrBuilder](docs/EntityGitMetadataOrBuilder.md)
 - [EntityIdentifiersRule](docs/EntityIdentifiersRule.md)
 - [EntityInfo](docs/EntityInfo.md)
 - [EntityReference](docs/EntityReference.md)
 - [EntityReferredByInfraSetupUsageDetail](docs/EntityReferredByInfraSetupUsageDetail.md)
 - [EntityReferredByPipelineSetupUsageDetail](docs/EntityReferredByPipelineSetupUsageDetail.md)
 - [EntitySetupUsage](docs/EntitySetupUsage.md)
 - [EnumDescriptor](docs/EnumDescriptor.md)
 - [EnumDescriptorProto](docs/EnumDescriptorProto.md)
 - [EnumDescriptorProtoOrBuilder](docs/EnumDescriptorProtoOrBuilder.md)
 - [EnumOptions](docs/EnumOptions.md)
 - [EnumOptionsOrBuilder](docs/EnumOptionsOrBuilder.md)
 - [EnumReservedRange](docs/EnumReservedRange.md)
 - [EnumReservedRangeOrBuilder](docs/EnumReservedRangeOrBuilder.md)
 - [EnumValueDescriptor](docs/EnumValueDescriptor.md)
 - [EnumValueDescriptorProto](docs/EnumValueDescriptorProto.md)
 - [EnumValueDescriptorProtoOrBuilder](docs/EnumValueDescriptorProtoOrBuilder.md)
 - [EnumValueOptions](docs/EnumValueOptions.md)
 - [EnumValueOptionsOrBuilder](docs/EnumValueOptionsOrBuilder.md)
 - [Environment](docs/Environment.md)
 - [EnvironmentGroup](docs/EnvironmentGroup.md)
 - [EnvironmentGroupDelete](docs/EnvironmentGroupDelete.md)
 - [EnvironmentGroupRequest](docs/EnvironmentGroupRequest.md)
 - [EnvironmentGroupResponse](docs/EnvironmentGroupResponse.md)
 - [EnvironmentIdentifierResponse](docs/EnvironmentIdentifierResponse.md)
 - [EnvironmentRequest](docs/EnvironmentRequest.md)
 - [EnvironmentResponse](docs/EnvironmentResponse.md)
 - [EnvironmentResponseDetails](docs/EnvironmentResponseDetails.md)
 - [EnvironmentType](docs/EnvironmentType.md)
 - [Error](docs/Error.md)
 - [ErrorBudgetBurnRateConditionSpec](docs/ErrorBudgetBurnRateConditionSpec.md)
 - [ErrorBudgetRemainingMinutesConditionSpec](docs/ErrorBudgetRemainingMinutesConditionSpec.md)
 - [ErrorBudgetRemainingPercentageConditionSpec](docs/ErrorBudgetRemainingPercentageConditionSpec.md)
 - [ErrorDetail](docs/ErrorDetail.md)
 - [ErrorMetadata](docs/ErrorMetadata.md)
 - [ErrorMetadata1](docs/ErrorMetadata1.md)
 - [ErrorNodeSummary](docs/ErrorNodeSummary.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [ErrorResultWithIdentifier](docs/ErrorResultWithIdentifier.md)
 - [ErrorTrackingConditionSpec](docs/ErrorTrackingConditionSpec.md)
 - [ErrorTrackingConnectorDTO](docs/ErrorTrackingConnectorDTO.md)
 - [ErrorTrackingHealthSource](docs/ErrorTrackingHealthSource.md)
 - [EulaSignRequest](docs/EulaSignRequest.md)
 - [EulaSignResponse](docs/EulaSignResponse.md)
 - [EvaluateRequestBody](docs/EvaluateRequestBody.md)
 - [EvaluatedPolicy](docs/EvaluatedPolicy.md)
 - [Evaluation](docs/Evaluation.md)
 - [EvaluationCounts](docs/EvaluationCounts.md)
 - [EvaluationDetail](docs/EvaluationDetail.md)
 - [EventLogsSuccessResponse](docs/EventLogsSuccessResponse.md)
 - [EventLogsSuccessResponseResponse](docs/EventLogsSuccessResponseResponse.md)
 - [EventResponse](docs/EventResponse.md)
 - [EventsChartsSuccessResponse](docs/EventsChartsSuccessResponse.md)
 - [EventsChartsSuccessResponseResponse](docs/EventsChartsSuccessResponseResponse.md)
 - [EventsFilter](docs/EventsFilter.md)
 - [ExclusionEntry](docs/ExclusionEntry.md)
 - [ExecutableResponse](docs/ExecutableResponse.md)
 - [ExecutionDetailDTO](docs/ExecutionDetailDTO.md)
 - [ExecutionDetailRequest](docs/ExecutionDetailRequest.md)
 - [ExecutionDetails](docs/ExecutionDetails.md)
 - [ExecutionEnforcementDetails](docs/ExecutionEnforcementDetails.md)
 - [ExecutionErrorInfo](docs/ExecutionErrorInfo.md)
 - [ExecutionGraph](docs/ExecutionGraph.md)
 - [ExecutionInfo](docs/ExecutionInfo.md)
 - [ExecutionLogDTO](docs/ExecutionLogDTO.md)
 - [ExecutionMetadata](docs/ExecutionMetadata.md)
 - [ExecutionMetadataOrBuilder](docs/ExecutionMetadataOrBuilder.md)
 - [ExecutionNode](docs/ExecutionNode.md)
 - [ExecutionNodeAdjacencyList](docs/ExecutionNodeAdjacencyList.md)
 - [ExecutionPrincipalInfo](docs/ExecutionPrincipalInfo.md)
 - [ExecutionPrincipalInfoOrBuilder](docs/ExecutionPrincipalInfoOrBuilder.md)
 - [ExecutionSummaryInfo](docs/ExecutionSummaryInfo.md)
 - [ExecutionTriggerInfo](docs/ExecutionTriggerInfo.md)
 - [ExecutionTriggerInfoOrBuilder](docs/ExecutionTriggerInfoOrBuilder.md)
 - [ExecutorInfo](docs/ExecutorInfo.md)
 - [ExpressionBlock](docs/ExpressionBlock.md)
 - [ExpressionBlockOrBuilder](docs/ExpressionBlockOrBuilder.md)
 - [ExtensionRange](docs/ExtensionRange.md)
 - [ExtensionRangeOptions](docs/ExtensionRangeOptions.md)
 - [ExtensionRangeOptionsOrBuilder](docs/ExtensionRangeOptionsOrBuilder.md)
 - [ExtensionRangeOrBuilder](docs/ExtensionRangeOrBuilder.md)
 - [FQNtoError](docs/FQNtoError.md)
 - [FailMetricCustomThresholdSpec](docs/FailMetricCustomThresholdSpec.md)
 - [FailMetricThresholdSpec](docs/FailMetricThresholdSpec.md)
 - [Failure](docs/Failure.md)
 - [FailureInfoCard](docs/FailureInfoCard.md)
 - [FailureInfoDTO](docs/FailureInfoDTO.md)
 - [FavoriteDTO](docs/FavoriteDTO.md)
 - [FavoriteResponse](docs/FavoriteResponse.md)
 - [FavoritesResourceType](docs/FavoritesResourceType.md)
 - [Feature](docs/Feature.md)
 - [FeatureCounts](docs/FeatureCounts.md)
 - [FeatureEnvProperties](docs/FeatureEnvProperties.md)
 - [FeatureFlagAuditEventData](docs/FeatureFlagAuditEventData.md)
 - [FeatureFlagRequestKind](docs/FeatureFlagRequestKind.md)
 - [FeaturePipeline](docs/FeaturePipeline.md)
 - [FeatureResponseMetadata](docs/FeatureResponseMetadata.md)
 - [FeatureResponseMetadataDetails](docs/FeatureResponseMetadataDetails.md)
 - [FeatureResponseMetadataDetailsPipelineMetadata](docs/FeatureResponseMetadataDetailsPipelineMetadata.md)
 - [FeatureState](docs/FeatureState.md)
 - [FeatureStatus](docs/FeatureStatus.md)
 - [Features](docs/Features.md)
 - [FieldDescriptor](docs/FieldDescriptor.md)
 - [FieldDescriptorProto](docs/FieldDescriptorProto.md)
 - [FieldDescriptorProtoOrBuilder](docs/FieldDescriptorProtoOrBuilder.md)
 - [FieldError](docs/FieldError.md)
 - [FieldFilter](docs/FieldFilter.md)
 - [FieldOptions](docs/FieldOptions.md)
 - [FieldOptionsOrBuilder](docs/FieldOptionsOrBuilder.md)
 - [FieldValues](docs/FieldValues.md)
 - [File](docs/File.md)
 - [FileDescriptor](docs/FileDescriptor.md)
 - [FileDescriptorProto](docs/FileDescriptorProto.md)
 - [FileNode](docs/FileNode.md)
 - [FileOptions](docs/FileOptions.md)
 - [FileOptionsOrBuilder](docs/FileOptionsOrBuilder.md)
 - [FileStoreNode](docs/FileStoreNode.md)
 - [FileStoreRequest](docs/FileStoreRequest.md)
 - [FilesFilterPropertiesDTO](docs/FilesFilterPropertiesDTO.md)
 - [FilesIdentifierBody](docs/FilesIdentifierBody.md)
 - [FilestoreIdentifierBody](docs/FilestoreIdentifierBody.md)
 - [Filter](docs/Filter.md)
 - [FilterObject](docs/FilterObject.md)
 - [FilterProperties](docs/FilterProperties.md)
 - [FilterStats](docs/FilterStats.md)
 - [FilterType](docs/FilterType.md)
 - [FilterValues](docs/FilterValues.md)
 - [FixedSchedule](docs/FixedSchedule.md)
 - [FixedSchedulesListResponse](docs/FixedSchedulesListResponse.md)
 - [FlagBasicInfo](docs/FlagBasicInfo.md)
 - [FlagBasicInfos](docs/FlagBasicInfos.md)
 - [FolderNode](docs/FolderNode.md)
 - [ForMetadata](docs/ForMetadata.md)
 - [ForMetadataOrBuilder](docs/ForMetadataOrBuilder.md)
 - [FormDataContentDisposition](docs/FormDataContentDisposition.md)
 - [FreezeDetailedResponse](docs/FreezeDetailedResponse.md)
 - [FreezeErrorResponseDTO](docs/FreezeErrorResponseDTO.md)
 - [FreezeFilterPropertiesDTO](docs/FreezeFilterPropertiesDTO.md)
 - [FreezeResponse](docs/FreezeResponse.md)
 - [FreezeResponseWrapperDTO](docs/FreezeResponseWrapperDTO.md)
 - [FreezeSummaryResponse](docs/FreezeSummaryResponse.md)
 - [FreezeWindow](docs/FreezeWindow.md)
 - [FrozenExecutionDetail](docs/FrozenExecutionDetail.md)
 - [FrozenExecutionDetails](docs/FrozenExecutionDetails.md)
 - [GCPViewPreferences](docs/GCPViewPreferences.md)
 - [GatewayAccountRequest](docs/GatewayAccountRequest.md)
 - [GatewayruntimeError](docs/GatewayruntimeError.md)
 - [GcpBillingExportSpecDTO](docs/GcpBillingExportSpecDTO.md)
 - [GcpCloudCostConnectorDTO](docs/GcpCloudCostConnectorDTO.md)
 - [GcpConnector](docs/GcpConnector.md)
 - [GcpConnectorCredential](docs/GcpConnectorCredential.md)
 - [GcpCredentialSpec](docs/GcpCredentialSpec.md)
 - [GcpKmsConnector](docs/GcpKmsConnector.md)
 - [GcpManualDetails](docs/GcpManualDetails.md)
 - [GcpOidcAccessTokenRequest](docs/GcpOidcAccessTokenRequest.md)
 - [GcpOidcTokenRequest](docs/GcpOidcTokenRequest.md)
 - [GcpSecretManager](docs/GcpSecretManager.md)
 - [GenerateRequestBody](docs/GenerateRequestBody.md)
 - [GetAccessPointResponse](docs/GetAccessPointResponse.md)
 - [GitAuthentication](docs/GitAuthentication.md)
 - [GitBranch](docs/GitBranch.md)
 - [GitBranchList](docs/GitBranchList.md)
 - [GitConfig](docs/GitConfig.md)
 - [GitCreateDetails](docs/GitCreateDetails.md)
 - [GitCreateDetails1](docs/GitCreateDetails1.md)
 - [GitDetails](docs/GitDetails.md)
 - [GitEnabled](docs/GitEnabled.md)
 - [GitErrorResult](docs/GitErrorResult.md)
 - [GitFindDetails](docs/GitFindDetails.md)
 - [GitFullSyncConfig](docs/GitFullSyncConfig.md)
 - [GitFullSyncConfigRequest](docs/GitFullSyncConfigRequest.md)
 - [GitFullSyncEntityInfo](docs/GitFullSyncEntityInfo.md)
 - [GitFullSyncEntityInfoFilter](docs/GitFullSyncEntityInfoFilter.md)
 - [GitHTTPAuthenticationDTO](docs/GitHTTPAuthenticationDTO.md)
 - [GitHttpConnectorSpec](docs/GitHttpConnectorSpec.md)
 - [GitHttpEncryptedConnectorSpec](docs/GitHttpEncryptedConnectorSpec.md)
 - [GitImportDetails](docs/GitImportDetails.md)
 - [GitImportInfo](docs/GitImportInfo.md)
 - [GitMetadataUpdateRequestBody](docs/GitMetadataUpdateRequestBody.md)
 - [GitMetadataUpdateResponseBody](docs/GitMetadataUpdateResponseBody.md)
 - [GitMoveDetails](docs/GitMoveDetails.md)
 - [GitSSHAuthentication](docs/GitSSHAuthentication.md)
 - [GitSshConnectorSpec](docs/GitSshConnectorSpec.md)
 - [GitSyncConfig](docs/GitSyncConfig.md)
 - [GitSyncError](docs/GitSyncError.md)
 - [GitSyncErrorAggregateByCommit](docs/GitSyncErrorAggregateByCommit.md)
 - [GitSyncErrorCount](docs/GitSyncErrorCount.md)
 - [GitSyncErrorDetails](docs/GitSyncErrorDetails.md)
 - [GitSyncFolderConfig](docs/GitSyncFolderConfig.md)
 - [GitSyncPatchOperation](docs/GitSyncPatchOperation.md)
 - [GitSyncSettings](docs/GitSyncSettings.md)
 - [GitUpdateDetails](docs/GitUpdateDetails.md)
 - [GitUpdateDetails1](docs/GitUpdateDetails1.md)
 - [GitXWebhookEventResponse](docs/GitXWebhookEventResponse.md)
 - [GitXWebhookResponse](docs/GitXWebhookResponse.md)
 - [GithubApiAccess](docs/GithubApiAccess.md)
 - [GithubApiAccessSpec](docs/GithubApiAccessSpec.md)
 - [GithubApp](docs/GithubApp.md)
 - [GithubAppSpec](docs/GithubAppSpec.md)
 - [GithubAuthentication](docs/GithubAuthentication.md)
 - [GithubConnector](docs/GithubConnector.md)
 - [GithubCredentials](docs/GithubCredentials.md)
 - [GithubHttpCredentials](docs/GithubHttpCredentials.md)
 - [GithubHttpCredentialsSpec](docs/GithubHttpCredentialsSpec.md)
 - [GithubOauth](docs/GithubOauth.md)
 - [GithubSshCredentials](docs/GithubSshCredentials.md)
 - [GithubTokenSpec](docs/GithubTokenSpec.md)
 - [GithubUsernamePassword](docs/GithubUsernamePassword.md)
 - [GithubUsernameToken](docs/GithubUsernameToken.md)
 - [GitlabApiAccess](docs/GitlabApiAccess.md)
 - [GitlabApiAccessSpec](docs/GitlabApiAccessSpec.md)
 - [GitlabAuthentication](docs/GitlabAuthentication.md)
 - [GitlabConnector](docs/GitlabConnector.md)
 - [GitlabCredentials](docs/GitlabCredentials.md)
 - [GitlabHttpCredentials](docs/GitlabHttpCredentials.md)
 - [GitlabHttpCredentialsSpec](docs/GitlabHttpCredentialsSpec.md)
 - [GitlabKerberos](docs/GitlabKerberos.md)
 - [GitlabOauth](docs/GitlabOauth.md)
 - [GitlabSshCredentials](docs/GitlabSshCredentials.md)
 - [GitlabTokenSpec](docs/GitlabTokenSpec.md)
 - [GitlabUsernamePassword](docs/GitlabUsernamePassword.md)
 - [GitlabUsernameToken](docs/GitlabUsernameToken.md)
 - [GovernanceAdhocEnqueueDTO](docs/GovernanceAdhocEnqueueDTO.md)
 - [GovernanceEnqueueResponseDTO](docs/GovernanceEnqueueResponseDTO.md)
 - [GovernanceMetadata](docs/GovernanceMetadata.md)
 - [GovernanceMetadata1](docs/GovernanceMetadata1.md)
 - [GovernanceMetadata2](docs/GovernanceMetadata2.md)
 - [GovernancePromptRule](docs/GovernancePromptRule.md)
 - [GovernanceStatus](docs/GovernanceStatus.md)
 - [GpgkeysGnuPGPublicKey](docs/GpgkeysGnuPGPublicKey.md)
 - [GpgkeysGnuPGPublicKeyCreateRequest](docs/GpgkeysGnuPGPublicKeyCreateRequest.md)
 - [GpgkeysGnuPGPublicKeyCreateResponse](docs/GpgkeysGnuPGPublicKeyCreateResponse.md)
 - [GpgkeysGnuPGPublicKeyList](docs/GpgkeysGnuPGPublicKeyList.md)
 - [GpgkeysGnuPGPublicKeyQuery](docs/GpgkeysGnuPGPublicKeyQuery.md)
 - [GpgkeysGnuPGPublicKeyResponse](docs/GpgkeysGnuPGPublicKeyResponse.md)
 - [GraphLayoutNode](docs/GraphLayoutNode.md)
 - [HTTPProxy](docs/HTTPProxy.md)
 - [HarnessApiAccess](docs/HarnessApiAccess.md)
 - [HarnessApiAccessSpec](docs/HarnessApiAccessSpec.md)
 - [HarnessApprovalActivity](docs/HarnessApprovalActivity.md)
 - [HarnessApprovalActivityRequest](docs/HarnessApprovalActivityRequest.md)
 - [HarnessApprovalInstanceDetails](docs/HarnessApprovalInstanceDetails.md)
 - [HarnessAuthentication](docs/HarnessAuthentication.md)
 - [HarnessConnector](docs/HarnessConnector.md)
 - [HarnessHttpCredentials](docs/HarnessHttpCredentials.md)
 - [HarnessHttpCredentialsSpec](docs/HarnessHttpCredentialsSpec.md)
 - [HarnessJWTTokenSpec](docs/HarnessJWTTokenSpec.md)
 - [HarnessTokenSpec](docs/HarnessTokenSpec.md)
 - [HarnessUsernameToken](docs/HarnessUsernameToken.md)
 - [HealthMonitoringFlagResponse](docs/HealthMonitoringFlagResponse.md)
 - [HealthScoreConditionSpec](docs/HealthScoreConditionSpec.md)
 - [HealthScoreDTO](docs/HealthScoreDTO.md)
 - [HealthSource](docs/HealthSource.md)
 - [HealthSourceDTO](docs/HealthSourceDTO.md)
 - [HealthSourceParamsDTO](docs/HealthSourceParamsDTO.md)
 - [HealthSourceSpec](docs/HealthSourceSpec.md)
 - [HealthSourceSummary](docs/HealthSourceSummary.md)
 - [HistogramExp](docs/HistogramExp.md)
 - [HistoricalTrend](docs/HistoricalTrend.md)
 - [HostDTO](docs/HostDTO.md)
 - [HostFilterDTO](docs/HostFilterDTO.md)
 - [HostValidationDTO](docs/HostValidationDTO.md)
 - [HostValidationParams](docs/HostValidationParams.md)
 - [HrepocredsRepoCreds](docs/HrepocredsRepoCreds.md)
 - [HrepocredsRepoCredsCreateRequest](docs/HrepocredsRepoCredsCreateRequest.md)
 - [HrepocredsRepoCredsQuery](docs/HrepocredsRepoCredsQuery.md)
 - [HrepocredsRepoCredsResponse](docs/HrepocredsRepoCredsResponse.md)
 - [HrepocredsRepoCredsUpdateRequest](docs/HrepocredsRepoCredsUpdateRequest.md)
 - [HttpHelmAuthCredentials](docs/HttpHelmAuthCredentials.md)
 - [HttpHelmAuthentication](docs/HttpHelmAuthentication.md)
 - [HttpHelmConnector](docs/HttpHelmConnector.md)
 - [HttpHelmUsernamePassword](docs/HttpHelmUsernamePassword.md)
 - [HttpRequestInfo](docs/HttpRequestInfo.md)
 - [IPAllowlistConfig](docs/IPAllowlistConfig.md)
 - [IPAllowlistConfigRequest](docs/IPAllowlistConfigRequest.md)
 - [IPAllowlistConfigResponse](docs/IPAllowlistConfigResponse.md)
 - [IPAllowlistConfigValidateResponse](docs/IPAllowlistConfigValidateResponse.md)
 - [IdentifierRefProtoDTO](docs/IdentifierRefProtoDTO.md)
 - [IdentifierRefProtoDTOOrBuilder](docs/IdentifierRefProtoDTOOrBuilder.md)
 - [IgnoreMetricThresholdSpec](docs/IgnoreMetricThresholdSpec.md)
 - [InfraDefinitionReferenceProtoDTO](docs/InfraDefinitionReferenceProtoDTO.md)
 - [InfraDefinitionReferenceProtoDTOOrBuilder](docs/InfraDefinitionReferenceProtoDTOOrBuilder.md)
 - [InfrastructureRequest](docs/InfrastructureRequest.md)
 - [InfrastructureResponse](docs/InfrastructureResponse.md)
 - [InfrastructureResponseDTO](docs/InfrastructureResponseDTO.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [InlineResponse201](docs/InlineResponse201.md)
 - [InputSetCreateRequestBody](docs/InputSetCreateRequestBody.md)
 - [InputSetError](docs/InputSetError.md)
 - [InputSetErrorDetails](docs/InputSetErrorDetails.md)
 - [InputSetErrorWrapper](docs/InputSetErrorWrapper.md)
 - [InputSetGitUpdateDetails](docs/InputSetGitUpdateDetails.md)
 - [InputSetGitUpdateResponse](docs/InputSetGitUpdateResponse.md)
 - [InputSetImportRequestBody](docs/InputSetImportRequestBody.md)
 - [InputSetImportRequestDTO](docs/InputSetImportRequestDTO.md)
 - [InputSetImportResponseBody](docs/InputSetImportResponseBody.md)
 - [InputSetMoveConfigRequestBody](docs/InputSetMoveConfigRequestBody.md)
 - [InputSetMoveConfigResponseBody](docs/InputSetMoveConfigResponseBody.md)
 - [InputSetReferenceProtoDTO](docs/InputSetReferenceProtoDTO.md)
 - [InputSetReferenceProtoDTOOrBuilder](docs/InputSetReferenceProtoDTOOrBuilder.md)
 - [InputSetResponse](docs/InputSetResponse.md)
 - [InputSetResponseBody](docs/InputSetResponseBody.md)
 - [InputSetSummaryResponse](docs/InputSetSummaryResponse.md)
 - [InputSetTemplateRequest](docs/InputSetTemplateRequest.md)
 - [InputSetTemplateResponse](docs/InputSetTemplateResponse.md)
 - [InputSetTemplateWithReplacedExpressionsResponse](docs/InputSetTemplateWithReplacedExpressionsResponse.md)
 - [InputSetUpdateRequestBody](docs/InputSetUpdateRequestBody.md)
 - [InputSetValidator](docs/InputSetValidator.md)
 - [InputsResponseBody](docs/InputsResponseBody.md)
 - [InputsResponseBodyOptions](docs/InputsResponseBodyOptions.md)
 - [InputsResponseBodyOptionsClone](docs/InputsResponseBodyOptionsClone.md)
 - [InputsResponseBodyOptionsCloneRef](docs/InputsResponseBodyOptionsCloneRef.md)
 - [InstanceBasedRoutingData](docs/InstanceBasedRoutingData.md)
 - [InstanceBasedRoutingDataV2](docs/InstanceBasedRoutingDataV2.md)
 - [InterruptConfig](docs/InterruptConfig.md)
 - [InterruptEffectDTO](docs/InterruptEffectDTO.md)
 - [InterruptResponse](docs/InterruptResponse.md)
 - [InvitationSource](docs/InvitationSource.md)
 - [Invite](docs/Invite.md)
 - [IssuedBy](docs/IssuedBy.md)
 - [JenkinsAuthCredentialsDTO](docs/JenkinsAuthCredentialsDTO.md)
 - [JenkinsAuthentication](docs/JenkinsAuthentication.md)
 - [JenkinsBearerTokenDTO](docs/JenkinsBearerTokenDTO.md)
 - [JenkinsConnector](docs/JenkinsConnector.md)
 - [JenkinsUserNamePasswordDTO](docs/JenkinsUserNamePasswordDTO.md)
 - [JexlCriteriaSpec](docs/JexlCriteriaSpec.md)
 - [JiraApprovalInstanceDetails](docs/JiraApprovalInstanceDetails.md)
 - [JiraAuthCredentials](docs/JiraAuthCredentials.md)
 - [JiraAuthentication](docs/JiraAuthentication.md)
 - [JiraConnector](docs/JiraConnector.md)
 - [JiraIssue](docs/JiraIssue.md)
 - [JiraIssueKeyNG](docs/JiraIssueKeyNG.md)
 - [JiraIssueNG](docs/JiraIssueNG.md)
 - [JiraPATPassword](docs/JiraPATPassword.md)
 - [JiraUserNamePassword](docs/JiraUserNamePassword.md)
 - [JwksPublicKeyDTO](docs/JwksPublicKeyDTO.md)
 - [JwksPublicKeysDTO](docs/JwksPublicKeysDTO.md)
 - [K8sConfigDetails](docs/K8sConfigDetails.md)
 - [K8sLabel](docs/K8sLabel.md)
 - [K8sRecommendationFilterProperties](docs/K8sRecommendationFilterProperties.md)
 - [KerberosConfigDTO](docs/KerberosConfigDTO.md)
 - [KerberosWinRmConfigDTO](docs/KerberosWinRmConfigDTO.md)
 - [KeyValuesCriteriaSpec](docs/KeyValuesCriteriaSpec.md)
 - [KubernetesAuth](docs/KubernetesAuth.md)
 - [KubernetesAuthCredential](docs/KubernetesAuthCredential.md)
 - [KubernetesClientKeyCert](docs/KubernetesClientKeyCert.md)
 - [KubernetesClusterConfig](docs/KubernetesClusterConfig.md)
 - [KubernetesClusterDetails](docs/KubernetesClusterDetails.md)
 - [KubernetesCredential](docs/KubernetesCredential.md)
 - [KubernetesCredentialSpec](docs/KubernetesCredentialSpec.md)
 - [KubernetesDependencyMetadata](docs/KubernetesDependencyMetadata.md)
 - [KubernetesOpenIdConnect](docs/KubernetesOpenIdConnect.md)
 - [KubernetesServiceAccount](docs/KubernetesServiceAccount.md)
 - [KubernetesUserNamePassword](docs/KubernetesUserNamePassword.md)
 - [LDAPSettings](docs/LDAPSettings.md)
 - [LastModified](docs/LastModified.md)
 - [LastStreamedCard](docs/LastStreamedCard.md)
 - [LastTriggerExecutionDetails](docs/LastTriggerExecutionDetails.md)
 - [LdapConnectionSettings](docs/LdapConnectionSettings.md)
 - [LdapGroupResponse](docs/LdapGroupResponse.md)
 - [LdapGroupSettings](docs/LdapGroupSettings.md)
 - [LdapLdaplogintestBody](docs/LdapLdaplogintestBody.md)
 - [LdapLinkGroupRequest](docs/LdapLinkGroupRequest.md)
 - [LdapResponse](docs/LdapResponse.md)
 - [LdapUserResponse](docs/LdapUserResponse.md)
 - [LdapUserSettings](docs/LdapUserSettings.md)
 - [Level](docs/Level.md)
 - [LevelOrBuilder](docs/LevelOrBuilder.md)
 - [LicenseUsage](docs/LicenseUsage.md)
 - [LinkedEnforcements](docs/LinkedEnforcements.md)
 - [LinkedPolicy](docs/LinkedPolicy.md)
 - [Linkedpolicyidentifier](docs/Linkedpolicyidentifier.md)
 - [ListAccessPointResponse](docs/ListAccessPointResponse.md)
 - [ListDTO](docs/ListDTO.md)
 - [ListMasterContent](docs/ListMasterContent.md)
 - [ListMasterSuccessResponse](docs/ListMasterSuccessResponse.md)
 - [ListMasterSuccessResponseResponse](docs/ListMasterSuccessResponseResponse.md)
 - [ListMasterSuccessResponseResponseData](docs/ListMasterSuccessResponseResponseData.md)
 - [ListSetupsSuccessResponse](docs/ListSetupsSuccessResponse.md)
 - [LiveMonitoringDTO](docs/LiveMonitoringDTO.md)
 - [LocalConnector](docs/LocalConnector.md)
 - [Location](docs/Location.md)
 - [LocationOrBuilder](docs/LocationOrBuilder.md)
 - [LoginTypeResponse](docs/LoginTypeResponse.md)
 - [LwCOConnector](docs/LwCOConnector.md)
 - [LwService](docs/LwService.md)
 - [LwServiceResponse](docs/LwServiceResponse.md)
 - [MSDropdownResponse](docs/MSDropdownResponse.md)
 - [ManifestAttributes](docs/ManifestAttributes.md)
 - [ManifestConfig](docs/ManifestConfig.md)
 - [ManifestConfigWrapper](docs/ManifestConfigWrapper.md)
 - [ManifestsResponseDTO](docs/ManifestsResponseDTO.md)
 - [ManualIssuer](docs/ManualIssuer.md)
 - [MatrixMetadata](docs/MatrixMetadata.md)
 - [MatrixMetadataOrBuilder](docs/MatrixMetadataOrBuilder.md)
 - [MergeInputSetRequest](docs/MergeInputSetRequest.md)
 - [Message](docs/Message.md)
 - [MessageLite](docs/MessageLite.md)
 - [MessageOptions](docs/MessageOptions.md)
 - [MessageOptionsOrBuilder](docs/MessageOptionsOrBuilder.md)
 - [MethodDescriptor](docs/MethodDescriptor.md)
 - [MethodDescriptorProto](docs/MethodDescriptorProto.md)
 - [MethodDescriptorProtoOrBuilder](docs/MethodDescriptorProtoOrBuilder.md)
 - [MethodOptions](docs/MethodOptions.md)
 - [MethodOptionsOrBuilder](docs/MethodOptionsOrBuilder.md)
 - [MetricDTO](docs/MetricDTO.md)
 - [MetricGraph](docs/MetricGraph.md)
 - [MetricLessServiceLevelIndicatorSpec](docs/MetricLessServiceLevelIndicatorSpec.md)
 - [MetricResponseMapping](docs/MetricResponseMapping.md)
 - [MetricThreshold](docs/MetricThreshold.md)
 - [MetricThresholdCriteria](docs/MetricThresholdCriteria.md)
 - [MetricThresholdCriteriaSpec](docs/MetricThresholdCriteriaSpec.md)
 - [MetricThresholdSpec](docs/MetricThresholdSpec.md)
 - [MicroserviceVersionInfo](docs/MicroserviceVersionInfo.md)
 - [MicrosoftTeamsConfigDTO](docs/MicrosoftTeamsConfigDTO.md)
 - [ModuleType](docs/ModuleType.md)
 - [ModuleType1](docs/ModuleType1.md)
 - [ModuleVersionsResponse](docs/ModuleVersionsResponse.md)
 - [MonitoredService](docs/MonitoredService.md)
 - [MonitoredServiceChangeDetailSLO](docs/MonitoredServiceChangeDetailSLO.md)
 - [MonitoredServiceDetail](docs/MonitoredServiceDetail.md)
 - [MonitoredServiceListItemDTO](docs/MonitoredServiceListItemDTO.md)
 - [MonitoredServicePlatformResponse](docs/MonitoredServicePlatformResponse.md)
 - [MonitoredServiceResponse](docs/MonitoredServiceResponse.md)
 - [MonitoredServiceWithHealthSources](docs/MonitoredServiceWithHealthSources.md)
 - [MonthlyCalenderSpec](docs/MonthlyCalenderSpec.md)
 - [MoveConfigOperationType](docs/MoveConfigOperationType.md)
 - [MovePerspectiveDTO](docs/MovePerspectiveDTO.md)
 - [NGAuthSettings](docs/NGAuthSettings.md)
 - [NGProcessWebhookResponse](docs/NGProcessWebhookResponse.md)
 - [NGTag](docs/NGTag.md)
 - [NGTriggerDetailsResponseDTO](docs/NGTriggerDetailsResponseDTO.md)
 - [NGTriggerEventHistoryBaseDTO](docs/NGTriggerEventHistoryBaseDTO.md)
 - [NGTriggerEventHistoryDTO](docs/NGTriggerEventHistoryDTO.md)
 - [NGTriggerEventInfo](docs/NGTriggerEventInfo.md)
 - [NGTriggerResponse](docs/NGTriggerResponse.md)
 - [NGVariable](docs/NGVariable.md)
 - [NTLMConfig](docs/NTLMConfig.md)
 - [NamePart](docs/NamePart.md)
 - [NamePartOrBuilder](docs/NamePartOrBuilder.md)
 - [NameValuePairWithDefault](docs/NameValuePairWithDefault.md)
 - [NewRelicConnectorDTO](docs/NewRelicConnectorDTO.md)
 - [NewRelicHealthSource](docs/NewRelicHealthSource.md)
 - [NewRelicMetricDefinition](docs/NewRelicMetricDefinition.md)
 - [NextGenHealthSource](docs/NextGenHealthSource.md)
 - [NexusAuthCredentials](docs/NexusAuthCredentials.md)
 - [NexusAuthentication](docs/NexusAuthentication.md)
 - [NexusConnector](docs/NexusConnector.md)
 - [NexusUsernamePasswordAuth](docs/NexusUsernamePasswordAuth.md)
 - [NgSmtp](docs/NgSmtp.md)
 - [NodeErrorInfo](docs/NodeErrorInfo.md)
 - [NodeExecutionDetails](docs/NodeExecutionDetails.md)
 - [NodeExecutionEventData](docs/NodeExecutionEventData.md)
 - [NodeInfo](docs/NodeInfo.md)
 - [NodePool](docs/NodePool.md)
 - [NodePoolId](docs/NodePoolId.md)
 - [NodeRecommendationDTO](docs/NodeRecommendationDTO.md)
 - [NodeRunInfo](docs/NodeRunInfo.md)
 - [NotificationRule](docs/NotificationRule.md)
 - [NotificationRuleCondition](docs/NotificationRuleCondition.md)
 - [NotificationRuleConditionSpec](docs/NotificationRuleConditionSpec.md)
 - [NotificationRuleRefDTO](docs/NotificationRuleRefDTO.md)
 - [NotificationRuleResponse](docs/NotificationRuleResponse.md)
 - [NotificationSettingConfig](docs/NotificationSettingConfig.md)
 - [NotificationSettingConfigDTO](docs/NotificationSettingConfigDTO.md)
 - [NumberNGVariable](docs/NumberNGVariable.md)
 - [OAuthSettings](docs/OAuthSettings.md)
 - [OccurrenceSchedule](docs/OccurrenceSchedule.md)
 - [OciHelmAuthCredentials](docs/OciHelmAuthCredentials.md)
 - [OciHelmAuthentication](docs/OciHelmAuthentication.md)
 - [OciHelmConnector](docs/OciHelmConnector.md)
 - [OciHelmUsernamePassword](docs/OciHelmUsernamePassword.md)
 - [OidcConfiguration](docs/OidcConfiguration.md)
 - [OidcWorkloadAccessTokenResponse](docs/OidcWorkloadAccessTokenResponse.md)
 - [OneofDescriptor](docs/OneofDescriptor.md)
 - [OneofDescriptorProto](docs/OneofDescriptorProto.md)
 - [OneofDescriptorProtoOrBuilder](docs/OneofDescriptorProtoOrBuilder.md)
 - [OneofOptions](docs/OneofOptions.md)
 - [OneofOptionsOrBuilder](docs/OneofOptionsOrBuilder.md)
 - [OnetimeDowntimeSpec](docs/OnetimeDowntimeSpec.md)
 - [OnetimeDurationBasedSpec](docs/OnetimeDurationBasedSpec.md)
 - [OnetimeEndTimeBasedSpec](docs/OnetimeEndTimeBasedSpec.md)
 - [OnetimeSpec](docs/OnetimeSpec.md)
 - [OpaAuditEventData](docs/OpaAuditEventData.md)
 - [Opts](docs/Opts.md)
 - [OrchestrationMap](docs/OrchestrationMap.md)
 - [Organization](docs/Organization.md)
 - [Organization1](docs/Organization1.md)
 - [OrganizationDictionary](docs/OrganizationDictionary.md)
 - [OrganizationRequest](docs/OrganizationRequest.md)
 - [OrganizationResponse](docs/OrganizationResponse.md)
 - [OrganizationResponse1](docs/OrganizationResponse1.md)
 - [OverlayInputSetResponse](docs/OverlayInputSetResponse.md)
 - [PMSGitUpdateResponse](docs/PMSGitUpdateResponse.md)
 - [PMSPipelineResponse](docs/PMSPipelineResponse.md)
 - [PMSPipelineSummaryResponse](docs/PMSPipelineSummaryResponse.md)
 - [PageActiveMonitoredService](docs/PageActiveMonitoredService.md)
 - [PageFile](docs/PageFile.md)
 - [PageNGTriggerEventHistoryBaseDTO](docs/PageNGTriggerEventHistoryBaseDTO.md)
 - [PageNGTriggerEventHistoryDTO](docs/PageNGTriggerEventHistoryDTO.md)
 - [PagePMSPipelineSummaryResponse](docs/PagePMSPipelineSummaryResponse.md)
 - [PagePipelineExecutionIdentifierSummary](docs/PagePipelineExecutionIdentifierSummary.md)
 - [PagePipelineExecutionSummary](docs/PagePipelineExecutionSummary.md)
 - [PageResponseApiKeyAggregate](docs/PageResponseApiKeyAggregate.md)
 - [PageResponseAuditEvent](docs/PageResponseAuditEvent.md)
 - [PageResponseCVNGLog](docs/PageResponseCVNGLog.md)
 - [PageResponseCcmK8sConnectorResponse](docs/PageResponseCcmK8sConnectorResponse.md)
 - [PageResponseClusterResponse](docs/PageResponseClusterResponse.md)
 - [PageResponseConnectorResponse](docs/PageResponseConnectorResponse.md)
 - [PageResponseDowntimeHistoryView](docs/PageResponseDowntimeHistoryView.md)
 - [PageResponseDowntimeListView](docs/PageResponseDowntimeListView.md)
 - [PageResponseEntitySetupUsage](docs/PageResponseEntitySetupUsage.md)
 - [PageResponseEnvironmentGroup](docs/PageResponseEnvironmentGroup.md)
 - [PageResponseEnvironmentIdentifierResponse](docs/PageResponseEnvironmentIdentifierResponse.md)
 - [PageResponseEnvironmentResponse](docs/PageResponseEnvironmentResponse.md)
 - [PageResponseFilter](docs/PageResponseFilter.md)
 - [PageResponseFreezeSummaryResponse](docs/PageResponseFreezeSummaryResponse.md)
 - [PageResponseGitBranch](docs/PageResponseGitBranch.md)
 - [PageResponseGitFullSyncEntityInfo](docs/PageResponseGitFullSyncEntityInfo.md)
 - [PageResponseGitSyncError](docs/PageResponseGitSyncError.md)
 - [PageResponseGitSyncErrorAggregateByCommit](docs/PageResponseGitSyncErrorAggregateByCommit.md)
 - [PageResponseHostDTO](docs/PageResponseHostDTO.md)
 - [PageResponseInfrastructureResponse](docs/PageResponseInfrastructureResponse.md)
 - [PageResponseInputSetSummaryResponse](docs/PageResponseInputSetSummaryResponse.md)
 - [PageResponseInvite](docs/PageResponseInvite.md)
 - [PageResponseMSDropdownResponse](docs/PageResponseMSDropdownResponse.md)
 - [PageResponseMonitoredServiceListItemDTO](docs/PageResponseMonitoredServiceListItemDTO.md)
 - [PageResponseMonitoredServicePlatformResponse](docs/PageResponseMonitoredServicePlatformResponse.md)
 - [PageResponseMonitoredServiceResponse](docs/PageResponseMonitoredServiceResponse.md)
 - [PageResponseNGTriggerDetailsResponseDTO](docs/PageResponseNGTriggerDetailsResponseDTO.md)
 - [PageResponseNotificationRuleResponse](docs/PageResponseNotificationRuleResponse.md)
 - [PageResponseOrganizationResponse](docs/PageResponseOrganizationResponse.md)
 - [PageResponseProjectResponse](docs/PageResponseProjectResponse.md)
 - [PageResponseResourceGroupV2Response](docs/PageResponseResourceGroupV2Response.md)
 - [PageResponseRoleAssignmentAggregate](docs/PageResponseRoleAssignmentAggregate.md)
 - [PageResponseRoleAssignmentResponse](docs/PageResponseRoleAssignmentResponse.md)
 - [PageResponseRoleWithPrincipalCountResponse](docs/PageResponseRoleWithPrincipalCountResponse.md)
 - [PageResponseSLOConsumptionBreakdown](docs/PageResponseSLOConsumptionBreakdown.md)
 - [PageResponseSLOHealthListView](docs/PageResponseSLOHealthListView.md)
 - [PageResponseSecretResponse](docs/PageResponseSecretResponse.md)
 - [PageResponseServiceAccountAggregate](docs/PageResponseServiceAccountAggregate.md)
 - [PageResponseServiceLevelObjectiveV2Response](docs/PageResponseServiceLevelObjectiveV2Response.md)
 - [PageResponseServiceOverrideResponse](docs/PageResponseServiceOverrideResponse.md)
 - [PageResponseServiceResponse](docs/PageResponseServiceResponse.md)
 - [PageResponseTokenAggregate](docs/PageResponseTokenAggregate.md)
 - [PageResponseUserAggregate](docs/PageResponseUserAggregate.md)
 - [PageResponseUserGroup](docs/PageResponseUserGroup.md)
 - [PageResponseUserMetadata](docs/PageResponseUserMetadata.md)
 - [PageResponseVariableResponseDTO](docs/PageResponseVariableResponseDTO.md)
 - [PageTemplateMetadataSummaryResponse](docs/PageTemplateMetadataSummaryResponse.md)
 - [Pageable](docs/Pageable.md)
 - [PagerDutyConfigDTO](docs/PagerDutyConfigDTO.md)
 - [PagerDutyConnectorDTO](docs/PagerDutyConnectorDTO.md)
 - [Pagination](docs/Pagination.md)
 - [PaginationInput](docs/PaginationInput.md)
 - [ParameterFieldDouble](docs/ParameterFieldDouble.md)
 - [ParameterFieldSecretRefData](docs/ParameterFieldSecretRefData.md)
 - [ParameterFieldStoreConfigWrapper](docs/ParameterFieldStoreConfigWrapper.md)
 - [ParameterFieldString](docs/ParameterFieldString.md)
 - [ParentStageInfo](docs/ParentStageInfo.md)
 - [Parser](docs/Parser.md)
 - [ParserAmbiance](docs/ParserAmbiance.md)
 - [ParserAsyncChainExecutableResponse](docs/ParserAsyncChainExecutableResponse.md)
 - [ParserAsyncExecutableResponse](docs/ParserAsyncExecutableResponse.md)
 - [ParserBuildInfo](docs/ParserBuildInfo.md)
 - [ParserChild](docs/ParserChild.md)
 - [ParserChildChainExecutableResponse](docs/ParserChildChainExecutableResponse.md)
 - [ParserChildExecutableResponse](docs/ParserChildExecutableResponse.md)
 - [ParserChildrenExecutableResponse](docs/ParserChildrenExecutableResponse.md)
 - [ParserDescriptorProto](docs/ParserDescriptorProto.md)
 - [ParserEntityDetailProtoDTO](docs/ParserEntityDetailProtoDTO.md)
 - [ParserEntityGitMetadata](docs/ParserEntityGitMetadata.md)
 - [ParserEnumDescriptorProto](docs/ParserEnumDescriptorProto.md)
 - [ParserEnumOptions](docs/ParserEnumOptions.md)
 - [ParserEnumReservedRange](docs/ParserEnumReservedRange.md)
 - [ParserEnumValueDescriptorProto](docs/ParserEnumValueDescriptorProto.md)
 - [ParserEnumValueOptions](docs/ParserEnumValueOptions.md)
 - [ParserExecutableResponse](docs/ParserExecutableResponse.md)
 - [ParserExecutionErrorInfo](docs/ParserExecutionErrorInfo.md)
 - [ParserExecutionMetadata](docs/ParserExecutionMetadata.md)
 - [ParserExecutionPrincipalInfo](docs/ParserExecutionPrincipalInfo.md)
 - [ParserExecutionTriggerInfo](docs/ParserExecutionTriggerInfo.md)
 - [ParserExpressionBlock](docs/ParserExpressionBlock.md)
 - [ParserExtensionRange](docs/ParserExtensionRange.md)
 - [ParserExtensionRangeOptions](docs/ParserExtensionRangeOptions.md)
 - [ParserFieldDescriptorProto](docs/ParserFieldDescriptorProto.md)
 - [ParserFieldOptions](docs/ParserFieldOptions.md)
 - [ParserFileDescriptorProto](docs/ParserFileDescriptorProto.md)
 - [ParserFileOptions](docs/ParserFileOptions.md)
 - [ParserForMetadata](docs/ParserForMetadata.md)
 - [ParserGovernanceMetadata](docs/ParserGovernanceMetadata.md)
 - [ParserIdentifierRefProtoDTO](docs/ParserIdentifierRefProtoDTO.md)
 - [ParserInfraDefinitionReferenceProtoDTO](docs/ParserInfraDefinitionReferenceProtoDTO.md)
 - [ParserInputSetReferenceProtoDTO](docs/ParserInputSetReferenceProtoDTO.md)
 - [ParserLevel](docs/ParserLevel.md)
 - [ParserLocation](docs/ParserLocation.md)
 - [ParserMatrixMetadata](docs/ParserMatrixMetadata.md)
 - [ParserMessage](docs/ParserMessage.md)
 - [ParserMessageLite](docs/ParserMessageLite.md)
 - [ParserMessageOptions](docs/ParserMessageOptions.md)
 - [ParserMethodDescriptorProto](docs/ParserMethodDescriptorProto.md)
 - [ParserMethodOptions](docs/ParserMethodOptions.md)
 - [ParserNamePart](docs/ParserNamePart.md)
 - [ParserNodeRunInfo](docs/ParserNodeRunInfo.md)
 - [ParserOneofDescriptorProto](docs/ParserOneofDescriptorProto.md)
 - [ParserOneofOptions](docs/ParserOneofOptions.md)
 - [ParserPipelineStageInfo](docs/ParserPipelineStageInfo.md)
 - [ParserPolicyMetadata](docs/ParserPolicyMetadata.md)
 - [ParserPolicySetMetadata](docs/ParserPolicySetMetadata.md)
 - [ParserPostExecutionRollbackInfo](docs/ParserPostExecutionRollbackInfo.md)
 - [ParserRerunInfo](docs/ParserRerunInfo.md)
 - [ParserReservedRange](docs/ParserReservedRange.md)
 - [ParserRetryExecutionInfo](docs/ParserRetryExecutionInfo.md)
 - [ParserServiceDescriptorProto](docs/ParserServiceDescriptorProto.md)
 - [ParserServiceOptions](docs/ParserServiceOptions.md)
 - [ParserSkipInfo](docs/ParserSkipInfo.md)
 - [ParserSkipTaskExecutableResponse](docs/ParserSkipTaskExecutableResponse.md)
 - [ParserSourceCodeInfo](docs/ParserSourceCodeInfo.md)
 - [ParserStepType](docs/ParserStepType.md)
 - [ParserStrategyMetadata](docs/ParserStrategyMetadata.md)
 - [ParserStringValue](docs/ParserStringValue.md)
 - [ParserSyncExecutableResponse](docs/ParserSyncExecutableResponse.md)
 - [ParserTaskChainExecutableResponse](docs/ParserTaskChainExecutableResponse.md)
 - [ParserTaskExecutableResponse](docs/ParserTaskExecutableResponse.md)
 - [ParserTemplateReferenceProtoDTO](docs/ParserTemplateReferenceProtoDTO.md)
 - [ParserTriggerReferenceProtoDTO](docs/ParserTriggerReferenceProtoDTO.md)
 - [ParserTriggeredBy](docs/ParserTriggeredBy.md)
 - [ParserUninterpretedOption](docs/ParserUninterpretedOption.md)
 - [ParserUnitProgress](docs/ParserUnitProgress.md)
 - [PasswordChange](docs/PasswordChange.md)
 - [PasswordStrengthPolicy](docs/PasswordStrengthPolicy.md)
 - [PatchInstruction](docs/PatchInstruction.md)
 - [PatchInstructionInner](docs/PatchInstructionInner.md)
 - [Permission](docs/Permission.md)
 - [PermissionCheck](docs/PermissionCheck.md)
 - [PermissionResponse](docs/PermissionResponse.md)
 - [Perspective](docs/Perspective.md)
 - [PerspectiveAnomalyData](docs/PerspectiveAnomalyData.md)
 - [PerspectiveBudgetScope](docs/PerspectiveBudgetScope.md)
 - [PerspectiveData](docs/PerspectiveData.md)
 - [PerspectiveEntityStatsData](docs/PerspectiveEntityStatsData.md)
 - [PerspectiveQueryDTO](docs/PerspectiveQueryDTO.md)
 - [PerspectiveTimeSeriesData](docs/PerspectiveTimeSeriesData.md)
 - [PhysicalDataCenterConnectorDTO](docs/PhysicalDataCenterConnectorDTO.md)
 - [PipelineCount](docs/PipelineCount.md)
 - [PipelineCreateRequestBody](docs/PipelineCreateRequestBody.md)
 - [PipelineCreateResponseBody](docs/PipelineCreateResponseBody.md)
 - [PipelineEntityGitDetails](docs/PipelineEntityGitDetails.md)
 - [PipelineError](docs/PipelineError.md)
 - [PipelineErrorMetadata](docs/PipelineErrorMetadata.md)
 - [PipelineExecuteBody](docs/PipelineExecuteBody.md)
 - [PipelineExecuteResponseBody](docs/PipelineExecuteResponseBody.md)
 - [PipelineExecution](docs/PipelineExecution.md)
 - [PipelineExecutionCountInfo](docs/PipelineExecutionCountInfo.md)
 - [PipelineExecutionDetail](docs/PipelineExecutionDetail.md)
 - [PipelineExecutionIdentifierSummary](docs/PipelineExecutionIdentifierSummary.md)
 - [PipelineExecutionNotes](docs/PipelineExecutionNotes.md)
 - [PipelineExecutionSummary](docs/PipelineExecutionSummary.md)
 - [PipelineFailure](docs/PipelineFailure.md)
 - [PipelineFilterProperties](docs/PipelineFilterProperties.md)
 - [PipelineFilterPropertiesModuleProperties](docs/PipelineFilterPropertiesModuleProperties.md)
 - [PipelineGetResponseBody](docs/PipelineGetResponseBody.md)
 - [PipelineGovernanceMetadata](docs/PipelineGovernanceMetadata.md)
 - [PipelineImportRequest](docs/PipelineImportRequest.md)
 - [PipelineImportRequestBody](docs/PipelineImportRequestBody.md)
 - [PipelineImportRequestDTO](docs/PipelineImportRequestDTO.md)
 - [PipelineInputSetError](docs/PipelineInputSetError.md)
 - [PipelineListResponseBody](docs/PipelineListResponseBody.md)
 - [PipelineMoveConfigRequestBody](docs/PipelineMoveConfigRequestBody.md)
 - [PipelineMoveConfigResponseBody](docs/PipelineMoveConfigResponseBody.md)
 - [PipelineNodeInfo](docs/PipelineNodeInfo.md)
 - [PipelinePolicyMetadata](docs/PipelinePolicyMetadata.md)
 - [PipelinePolicySetMetadata](docs/PipelinePolicySetMetadata.md)
 - [PipelinePolicySetMetadataOrBuilder](docs/PipelinePolicySetMetadataOrBuilder.md)
 - [PipelineResponseMessage](docs/PipelineResponseMessage.md)
 - [PipelineSaveResponse](docs/PipelineSaveResponse.md)
 - [PipelineSaveResponseBody](docs/PipelineSaveResponseBody.md)
 - [PipelineStageInfo](docs/PipelineStageInfo.md)
 - [PipelineStageInfoOrBuilder](docs/PipelineStageInfoOrBuilder.md)
 - [PipelineTemplateResponse](docs/PipelineTemplateResponse.md)
 - [PipelineUpdateRequestBody](docs/PipelineUpdateRequestBody.md)
 - [PlanExecution](docs/PlanExecution.md)
 - [PlanExecutionResponse](docs/PlanExecutionResponse.md)
 - [PmsStepDetails](docs/PmsStepDetails.md)
 - [Point](docs/Point.md)
 - [Policy](docs/Policy.md)
 - [PolicyExample](docs/PolicyExample.md)
 - [PolicyHealth](docs/PolicyHealth.md)
 - [PolicyManagementError](docs/PolicyManagementError.md)
 - [PolicyManagementPolicy](docs/PolicyManagementPolicy.md)
 - [PolicyManagementPolicySet](docs/PolicyManagementPolicySet.md)
 - [PolicyManagementResourceGroup](docs/PolicyManagementResourceGroup.md)
 - [PolicyMetadata](docs/PolicyMetadata.md)
 - [PolicyMetadata1](docs/PolicyMetadata1.md)
 - [PolicyMetadataOrBuilder](docs/PolicyMetadataOrBuilder.md)
 - [PolicySample](docs/PolicySample.md)
 - [PolicySet](docs/PolicySet.md)
 - [PolicySetMetadata](docs/PolicySetMetadata.md)
 - [PolicySetMetadata1](docs/PolicySetMetadata1.md)
 - [PolicySetMetadataOrBuilder](docs/PolicySetMetadataOrBuilder.md)
 - [PolledResponse](docs/PolledResponse.md)
 - [PollingInfoForTriggers](docs/PollingInfoForTriggers.md)
 - [PollingSubscriptionStatus](docs/PollingSubscriptionStatus.md)
 - [PortConfig](docs/PortConfig.md)
 - [PostExecutionRollbackInfo](docs/PostExecutionRollbackInfo.md)
 - [PostExecutionRollbackInfoOrBuilder](docs/PostExecutionRollbackInfoOrBuilder.md)
 - [Prerequisite](docs/Prerequisite.md)
 - [Principal](docs/Principal.md)
 - [Principal1](docs/Principal1.md)
 - [Principal2](docs/Principal2.md)
 - [PrincipalType](docs/PrincipalType.md)
 - [PrincipalV2](docs/PrincipalV2.md)
 - [Project](docs/Project.md)
 - [Project1](docs/Project1.md)
 - [ProjectDictionary](docs/ProjectDictionary.md)
 - [ProjectParams](docs/ProjectParams.md)
 - [ProjectRequest](docs/ProjectRequest.md)
 - [ProjectRequest1](docs/ProjectRequest1.md)
 - [ProjectResponse](docs/ProjectResponse.md)
 - [ProjectResponse1](docs/ProjectResponse1.md)
 - [ProjectsEmptyResponse](docs/ProjectsEmptyResponse.md)
 - [ProjectsProjectCreateRequest](docs/ProjectsProjectCreateRequest.md)
 - [ProjectsProjectQuery](docs/ProjectsProjectQuery.md)
 - [ProjectsProjectUpdateRequest](docs/ProjectsProjectUpdateRequest.md)
 - [PrometheusConnectorDTO](docs/PrometheusConnectorDTO.md)
 - [PrometheusFilter](docs/PrometheusFilter.md)
 - [PrometheusHealthSource](docs/PrometheusHealthSource.md)
 - [PrometheusMetricDefinition](docs/PrometheusMetricDefinition.md)
 - [ProtobufAny](docs/ProtobufAny.md)
 - [ProtobufFieldMask](docs/ProtobufFieldMask.md)
 - [ProtobufNullValue](docs/ProtobufNullValue.md)
 - [ProtocolStringList](docs/ProtocolStringList.md)
 - [Proxy](docs/Proxy.md)
 - [ProxyKey](docs/ProxyKey.md)
 - [ProxyKeyInstruction](docs/ProxyKeyInstruction.md)
 - [ProxyKeyInstructionInstructions](docs/ProxyKeyInstructionInstructions.md)
 - [ProxyKeyProject](docs/ProxyKeyProject.md)
 - [ProxyKeys](docs/ProxyKeys.md)
 - [PublicAccessRequest](docs/PublicAccessRequest.md)
 - [PublicAccessResponse](docs/PublicAccessResponse.md)
 - [QLCEViewEntityStatsDataPoint](docs/QLCEViewEntityStatsDataPoint.md)
 - [QLCEViewFieldInput](docs/QLCEViewFieldInput.md)
 - [QLCEViewFilter](docs/QLCEViewFilter.md)
 - [QLCEViewFilterWrapper](docs/QLCEViewFilterWrapper.md)
 - [QLCEViewGroupBy](docs/QLCEViewGroupBy.md)
 - [QLCEViewMetadataFilter](docs/QLCEViewMetadataFilter.md)
 - [QLCEViewRule](docs/QLCEViewRule.md)
 - [QLCEViewTimeFilter](docs/QLCEViewTimeFilter.md)
 - [QLCEViewTimeTruncGroupBy](docs/QLCEViewTimeTruncGroupBy.md)
 - [QuarterlyCalenderSpec](docs/QuarterlyCalenderSpec.md)
 - [QueryDefinition](docs/QueryDefinition.md)
 - [QueryParamsDTO](docs/QueryParamsDTO.md)
 - [RDSDatabase](docs/RDSDatabase.md)
 - [RancherAuthentication](docs/RancherAuthentication.md)
 - [RancherConnector](docs/RancherConnector.md)
 - [RancherConnectorBearerTokenAuthentication](docs/RancherConnectorBearerTokenAuthentication.md)
 - [RancherConnectorConfig](docs/RancherConnectorConfig.md)
 - [RancherConnectorConfigAuth](docs/RancherConnectorConfigAuth.md)
 - [RancherConnectorConfigAuthentication](docs/RancherConnectorConfigAuthentication.md)
 - [RatioSLIMetricSpec](docs/RatioSLIMetricSpec.md)
 - [RecentExecutionInfo](docs/RecentExecutionInfo.md)
 - [RecommendClusterRequest](docs/RecommendClusterRequest.md)
 - [RecommendationAdhocDTO](docs/RecommendationAdhocDTO.md)
 - [RecommendationAzureVmId](docs/RecommendationAzureVmId.md)
 - [RecommendationDetailsDTO](docs/RecommendationDetailsDTO.md)
 - [RecommendationEC2InstanceId](docs/RecommendationEC2InstanceId.md)
 - [RecommendationECSServiceId](docs/RecommendationECSServiceId.md)
 - [RecommendationGovernanceRuleId](docs/RecommendationGovernanceRuleId.md)
 - [RecommendationItem](docs/RecommendationItem.md)
 - [RecommendationNodepoolId](docs/RecommendationNodepoolId.md)
 - [RecommendationOverviewStats](docs/RecommendationOverviewStats.md)
 - [RecommendationResponse](docs/RecommendationResponse.md)
 - [RecommendationWorkloadId](docs/RecommendationWorkloadId.md)
 - [Recommendations](docs/Recommendations.md)
 - [RecommendationsIgnoreList](docs/RecommendationsIgnoreList.md)
 - [RecommendationsIgnoreResourcesDTO](docs/RecommendationsIgnoreResourcesDTO.md)
 - [ReconcilerReconcileCountsResponse](docs/ReconcilerReconcileCountsResponse.md)
 - [Recurrence](docs/Recurrence.md)
 - [RecurrenceSpec](docs/RecurrenceSpec.md)
 - [RecurringDowntimeSpec](docs/RecurringDowntimeSpec.md)
 - [Reference](docs/Reference.md)
 - [ReferenceDTO](docs/ReferenceDTO.md)
 - [ReferencedByDTO](docs/ReferencedByDTO.md)
 - [RefreshRequestDTO](docs/RefreshRequestDTO.md)
 - [RefreshResponse](docs/RefreshResponse.md)
 - [RepositoriesAppInfo](docs/RepositoriesAppInfo.md)
 - [RepositoriesDirectoryAppSpec](docs/RepositoriesDirectoryAppSpec.md)
 - [RepositoriesHelmAppSpec](docs/RepositoriesHelmAppSpec.md)
 - [RepositoriesHelmChart](docs/RepositoriesHelmChart.md)
 - [RepositoriesHelmChartsResponse](docs/RepositoriesHelmChartsResponse.md)
 - [RepositoriesKsonnetAppSpec](docs/RepositoriesKsonnetAppSpec.md)
 - [RepositoriesKsonnetEnvironment](docs/RepositoriesKsonnetEnvironment.md)
 - [RepositoriesKsonnetEnvironmentDestination](docs/RepositoriesKsonnetEnvironmentDestination.md)
 - [RepositoriesKustomizeAppSpec](docs/RepositoriesKustomizeAppSpec.md)
 - [RepositoriesManifestResponse](docs/RepositoriesManifestResponse.md)
 - [RepositoriesRefs](docs/RepositoriesRefs.md)
 - [RepositoriesRepoAccessQuery](docs/RepositoriesRepoAccessQuery.md)
 - [RepositoriesRepoAppDetailsQuery](docs/RepositoriesRepoAppDetailsQuery.md)
 - [RepositoriesRepoAppDetailsResponse](docs/RepositoriesRepoAppDetailsResponse.md)
 - [RepositoriesRepoAppsQuery](docs/RepositoriesRepoAppsQuery.md)
 - [RepositoriesRepoAppsResponse](docs/RepositoriesRepoAppsResponse.md)
 - [RepositoriesRepoCreateRequest](docs/RepositoriesRepoCreateRequest.md)
 - [RepositoriesRepoQuery](docs/RepositoriesRepoQuery.md)
 - [RepositoriesRepoResponse](docs/RepositoriesRepoResponse.md)
 - [RepositoriesRepoUpdateRequest](docs/RepositoriesRepoUpdateRequest.md)
 - [RepositoriesRepository](docs/RepositoriesRepository.md)
 - [RepositoriesRepositoryList](docs/RepositoriesRepositoryList.md)
 - [RepositoriesRevisionMetadata](docs/RepositoriesRevisionMetadata.md)
 - [RequestBasedServiceLevelIndicatorSpec](docs/RequestBasedServiceLevelIndicatorSpec.md)
 - [RequestMetadata](docs/RequestMetadata.md)
 - [RerunInfo](docs/RerunInfo.md)
 - [RerunInfoOrBuilder](docs/RerunInfoOrBuilder.md)
 - [ReservedRange](docs/ReservedRange.md)
 - [ReservedRangeOrBuilder](docs/ReservedRangeOrBuilder.md)
 - [Resource](docs/Resource.md)
 - [ResourceDTO](docs/ResourceDTO.md)
 - [ResourceFilter](docs/ResourceFilter.md)
 - [ResourceGroup](docs/ResourceGroup.md)
 - [ResourceGroupFilter](docs/ResourceGroupFilter.md)
 - [ResourceGroupFilterRequestBody](docs/ResourceGroupFilterRequestBody.md)
 - [ResourceGroupIdentifier](docs/ResourceGroupIdentifier.md)
 - [ResourceGroupScope](docs/ResourceGroupScope.md)
 - [ResourceGroupV2](docs/ResourceGroupV2.md)
 - [ResourceGroupV2Request](docs/ResourceGroupV2Request.md)
 - [ResourceGroupV2Response](docs/ResourceGroupV2Response.md)
 - [ResourceGroupsResponse](docs/ResourceGroupsResponse.md)
 - [ResourceRequirement](docs/ResourceRequirement.md)
 - [ResourceScope](docs/ResourceScope.md)
 - [ResourceScopeDTO](docs/ResourceScopeDTO.md)
 - [ResourceSelectorFilter](docs/ResourceSelectorFilter.md)
 - [ResourceSelectorV2](docs/ResourceSelectorV2.md)
 - [ResourceType](docs/ResourceType.md)
 - [ResourcegroupError](docs/ResourcegroupError.md)
 - [ResourcegroupErrorMetadata](docs/ResourcegroupErrorMetadata.md)
 - [ResourcegroupFailure](docs/ResourcegroupFailure.md)
 - [ResourcegroupResourceFilter](docs/ResourcegroupResourceFilter.md)
 - [ResourcegroupResourceGroupV2](docs/ResourcegroupResourceGroupV2.md)
 - [ResourcegroupResourceSelectorFilter](docs/ResourcegroupResourceSelectorFilter.md)
 - [ResourcegroupResponseMessage](docs/ResourcegroupResponseMessage.md)
 - [ResponseDTOAccessCheckResponse](docs/ResponseDTOAccessCheckResponse.md)
 - [ResponseDTOAccount](docs/ResponseDTOAccount.md)
 - [ResponseDTOAccountSettingResponse](docs/ResponseDTOAccountSettingResponse.md)
 - [ResponseDTOAddUsersResponse](docs/ResponseDTOAddUsersResponse.md)
 - [ResponseDTOApiKey](docs/ResponseDTOApiKey.md)
 - [ResponseDTOApiKeyAggregate](docs/ResponseDTOApiKeyAggregate.md)
 - [ResponseDTOApprovalInstanceResponse](docs/ResponseDTOApprovalInstanceResponse.md)
 - [ResponseDTOAzureVmRecommendation](docs/ResponseDTOAzureVmRecommendation.md)
 - [ResponseDTOBoolean](docs/ResponseDTOBoolean.md)
 - [ResponseDTOBudget](docs/ResponseDTOBudget.md)
 - [ResponseDTOBudgetData](docs/ResponseDTOBudgetData.md)
 - [ResponseDTOBudgetGroup](docs/ResponseDTOBudgetGroup.md)
 - [ResponseDTOCCMJiraDetails](docs/ResponseDTOCCMJiraDetails.md)
 - [ResponseDTOCCMOverview](docs/ResponseDTOCCMOverview.md)
 - [ResponseDTOCCMServiceNowDetails](docs/ResponseDTOCCMServiceNowDetails.md)
 - [ResponseDTOCEView](docs/ResponseDTOCEView.md)
 - [ResponseDTOCEViewFolder](docs/ResponseDTOCEViewFolder.md)
 - [ResponseDTOCannyBoardsResponse](docs/ResponseDTOCannyBoardsResponse.md)
 - [ResponseDTOCannyResponse](docs/ResponseDTOCannyResponse.md)
 - [ResponseDTOCcmK8sMetaInfoResponseDTO](docs/ResponseDTOCcmK8sMetaInfoResponseDTO.md)
 - [ResponseDTOClusterBatchResponse](docs/ResponseDTOClusterBatchResponse.md)
 - [ResponseDTOClusterResponse](docs/ResponseDTOClusterResponse.md)
 - [ResponseDTOConnectorCatalogueResponse](docs/ResponseDTOConnectorCatalogueResponse.md)
 - [ResponseDTOConnectorResponse](docs/ResponseDTOConnectorResponse.md)
 - [ResponseDTOConnectorStatistics](docs/ResponseDTOConnectorStatistics.md)
 - [ResponseDTOConnectorValidationResult](docs/ResponseDTOConnectorValidationResult.md)
 - [ResponseDTOCostOverview](docs/ResponseDTOCostOverview.md)
 - [ResponseDTOCoveoResponseDTO](docs/ResponseDTOCoveoResponseDTO.md)
 - [ResponseDTOCustomDeploymentInfraResponseDTO](docs/ResponseDTOCustomDeploymentInfraResponseDTO.md)
 - [ResponseDTOCustomDeploymentRefreshYamlDTO](docs/ResponseDTOCustomDeploymentRefreshYamlDTO.md)
 - [ResponseDTOCustomDeploymentVariableResponseDTO](docs/ResponseDTOCustomDeploymentVariableResponseDTO.md)
 - [ResponseDTODashboardPipelineExecution](docs/ResponseDTODashboardPipelineExecution.md)
 - [ResponseDTODouble](docs/ResponseDTODouble.md)
 - [ResponseDTOEC2InstanceRecommendation](docs/ResponseDTOEC2InstanceRecommendation.md)
 - [ResponseDTOECSRecommendationDTO](docs/ResponseDTOECSRecommendationDTO.md)
 - [ResponseDTOEnforcementCount](docs/ResponseDTOEnforcementCount.md)
 - [ResponseDTOEnvironmentGroup](docs/ResponseDTOEnvironmentGroup.md)
 - [ResponseDTOEnvironmentGroupDelete](docs/ResponseDTOEnvironmentGroupDelete.md)
 - [ResponseDTOEnvironmentResponse](docs/ResponseDTOEnvironmentResponse.md)
 - [ResponseDTOExecutionDetails](docs/ResponseDTOExecutionDetails.md)
 - [ResponseDTOFieldValues](docs/ResponseDTOFieldValues.md)
 - [ResponseDTOFile](docs/ResponseDTOFile.md)
 - [ResponseDTOFilter](docs/ResponseDTOFilter.md)
 - [ResponseDTOFolderNode](docs/ResponseDTOFolderNode.md)
 - [ResponseDTOFreezeDetailedResponse](docs/ResponseDTOFreezeDetailedResponse.md)
 - [ResponseDTOFreezeResponse](docs/ResponseDTOFreezeResponse.md)
 - [ResponseDTOFreezeResponseWrapperDTO](docs/ResponseDTOFreezeResponseWrapperDTO.md)
 - [ResponseDTOFrozenExecutionDetails](docs/ResponseDTOFrozenExecutionDetails.md)
 - [ResponseDTOGitBranchList](docs/ResponseDTOGitBranchList.md)
 - [ResponseDTOGitFullSyncConfig](docs/ResponseDTOGitFullSyncConfig.md)
 - [ResponseDTOGitSyncErrorCount](docs/ResponseDTOGitSyncErrorCount.md)
 - [ResponseDTOGitSyncSettings](docs/ResponseDTOGitSyncSettings.md)
 - [ResponseDTOGovernanceEnqueueResponseDTO](docs/ResponseDTOGovernanceEnqueueResponseDTO.md)
 - [ResponseDTOHealthScoreDTO](docs/ResponseDTOHealthScoreDTO.md)
 - [ResponseDTOHistoricalTrend](docs/ResponseDTOHistoricalTrend.md)
 - [ResponseDTOInfrastructureResponse](docs/ResponseDTOInfrastructureResponse.md)
 - [ResponseDTOInputSetGitUpdateResponse](docs/ResponseDTOInputSetGitUpdateResponse.md)
 - [ResponseDTOInputSetResponse](docs/ResponseDTOInputSetResponse.md)
 - [ResponseDTOInputSetTemplateResponse](docs/ResponseDTOInputSetTemplateResponse.md)
 - [ResponseDTOInputSetTemplateWithReplacedExpressionsResponse](docs/ResponseDTOInputSetTemplateWithReplacedExpressionsResponse.md)
 - [ResponseDTOInteger](docs/ResponseDTOInteger.md)
 - [ResponseDTOInterruptResponse](docs/ResponseDTOInterruptResponse.md)
 - [ResponseDTOInvite](docs/ResponseDTOInvite.md)
 - [ResponseDTOLicenseUsage](docs/ResponseDTOLicenseUsage.md)
 - [ResponseDTOListAccountSettings](docs/ResponseDTOListAccountSettings.md)
 - [ResponseDTOListAnomalyData](docs/ResponseDTOListAnomalyData.md)
 - [ResponseDTOListAnomalySummary](docs/ResponseDTOListAnomalySummary.md)
 - [ResponseDTOListApiKey](docs/ResponseDTOListApiKey.md)
 - [ResponseDTOListBIDashboardSummary](docs/ResponseDTOListBIDashboardSummary.md)
 - [ResponseDTOListBudget](docs/ResponseDTOListBudget.md)
 - [ResponseDTOListBudgetGroup](docs/ResponseDTOListBudgetGroup.md)
 - [ResponseDTOListBudgetSummary](docs/ResponseDTOListBudgetSummary.md)
 - [ResponseDTOListCEReportSchedule](docs/ResponseDTOListCEReportSchedule.md)
 - [ResponseDTOListCEView](docs/ResponseDTOListCEView.md)
 - [ResponseDTOListCEViewFolder](docs/ResponseDTOListCEViewFolder.md)
 - [ResponseDTOListClusterCostDetails](docs/ResponseDTOListClusterCostDetails.md)
 - [ResponseDTOListConnectorResponse](docs/ResponseDTOListConnectorResponse.md)
 - [ResponseDTOListEntityDetailProtoDTO](docs/ResponseDTOListEntityDetailProtoDTO.md)
 - [ResponseDTOListEntityType](docs/ResponseDTOListEntityType.md)
 - [ResponseDTOListEnvironmentResponse](docs/ResponseDTOListEnvironmentResponse.md)
 - [ResponseDTOListFilterStats](docs/ResponseDTOListFilterStats.md)
 - [ResponseDTOListGovernancePromptRule](docs/ResponseDTOListGovernancePromptRule.md)
 - [ResponseDTOListHostValidationDTO](docs/ResponseDTOListHostValidationDTO.md)
 - [ResponseDTOListMonitoredServiceWithHealthSources](docs/ResponseDTOListMonitoredServiceWithHealthSources.md)
 - [ResponseDTOListPermissionResponse](docs/ResponseDTOListPermissionResponse.md)
 - [ResponseDTOListPerspective](docs/ResponseDTOListPerspective.md)
 - [ResponseDTOListPerspectiveAnomalyData](docs/ResponseDTOListPerspectiveAnomalyData.md)
 - [ResponseDTOListRoleAssignmentResponse](docs/ResponseDTOListRoleAssignmentResponse.md)
 - [ResponseDTOListRuleEnforcement](docs/ResponseDTOListRuleEnforcement.md)
 - [ResponseDTOListScopeName](docs/ResponseDTOListScopeName.md)
 - [ResponseDTOListSecondaryEventsResponse](docs/ResponseDTOListSecondaryEventsResponse.md)
 - [ResponseDTOListServiceAccount](docs/ResponseDTOListServiceAccount.md)
 - [ResponseDTOListServiceResponse](docs/ResponseDTOListServiceResponse.md)
 - [ResponseDTOListSettingResponseDTO](docs/ResponseDTOListSettingResponseDTO.md)
 - [ResponseDTOListSettingUpdateResponseDTO](docs/ResponseDTOListSettingUpdateResponseDTO.md)
 - [ResponseDTOListSourceCodeManager](docs/ResponseDTOListSourceCodeManager.md)
 - [ResponseDTOListString](docs/ResponseDTOListString.md)
 - [ResponseDTOListUserGroup](docs/ResponseDTOListUserGroup.md)
 - [ResponseDTOListValueDataPoint](docs/ResponseDTOListValueDataPoint.md)
 - [ResponseDTOMonitoredServiceResponse](docs/ResponseDTOMonitoredServiceResponse.md)
 - [ResponseDTONGProcessWebhookResponse](docs/ResponseDTONGProcessWebhookResponse.md)
 - [ResponseDTONGTriggerDetailsResponseDTO](docs/ResponseDTONGTriggerDetailsResponseDTO.md)
 - [ResponseDTONGTriggerResponse](docs/ResponseDTONGTriggerResponse.md)
 - [ResponseDTONgSmtp](docs/ResponseDTONgSmtp.md)
 - [ResponseDTONodeExecutionDetails](docs/ResponseDTONodeExecutionDetails.md)
 - [ResponseDTONodeRecommendationDTO](docs/ResponseDTONodeRecommendationDTO.md)
 - [ResponseDTOOidcWorkloadAccessTokenResponse](docs/ResponseDTOOidcWorkloadAccessTokenResponse.md)
 - [ResponseDTOOptionalInvite](docs/ResponseDTOOptionalInvite.md)
 - [ResponseDTOOrganizationResponse](docs/ResponseDTOOrganizationResponse.md)
 - [ResponseDTOOverlayInputSetResponse](docs/ResponseDTOOverlayInputSetResponse.md)
 - [ResponseDTOPMSGitUpdateResponse](docs/ResponseDTOPMSGitUpdateResponse.md)
 - [ResponseDTOPMSPipelineResponse](docs/ResponseDTOPMSPipelineResponse.md)
 - [ResponseDTOPMSPipelineSummaryResponse](docs/ResponseDTOPMSPipelineSummaryResponse.md)
 - [ResponseDTOPageActiveMonitoredService](docs/ResponseDTOPageActiveMonitoredService.md)
 - [ResponseDTOPageFile](docs/ResponseDTOPageFile.md)
 - [ResponseDTOPageNGTriggerEventHistoryBaseDTO](docs/ResponseDTOPageNGTriggerEventHistoryBaseDTO.md)
 - [ResponseDTOPageNGTriggerEventHistoryDTO](docs/ResponseDTOPageNGTriggerEventHistoryDTO.md)
 - [ResponseDTOPagePMSPipelineSummaryResponse](docs/ResponseDTOPagePMSPipelineSummaryResponse.md)
 - [ResponseDTOPagePipelineExecutionIdentifierSummary](docs/ResponseDTOPagePipelineExecutionIdentifierSummary.md)
 - [ResponseDTOPagePipelineExecutionSummary](docs/ResponseDTOPagePipelineExecutionSummary.md)
 - [ResponseDTOPageResponseApiKeyAggregate](docs/ResponseDTOPageResponseApiKeyAggregate.md)
 - [ResponseDTOPageResponseAuditEvent](docs/ResponseDTOPageResponseAuditEvent.md)
 - [ResponseDTOPageResponseCcmK8sConnectorResponse](docs/ResponseDTOPageResponseCcmK8sConnectorResponse.md)
 - [ResponseDTOPageResponseClusterResponse](docs/ResponseDTOPageResponseClusterResponse.md)
 - [ResponseDTOPageResponseConnectorResponse](docs/ResponseDTOPageResponseConnectorResponse.md)
 - [ResponseDTOPageResponseDowntimeHistoryView](docs/ResponseDTOPageResponseDowntimeHistoryView.md)
 - [ResponseDTOPageResponseDowntimeListView](docs/ResponseDTOPageResponseDowntimeListView.md)
 - [ResponseDTOPageResponseEntitySetupUsage](docs/ResponseDTOPageResponseEntitySetupUsage.md)
 - [ResponseDTOPageResponseEnvironmentGroup](docs/ResponseDTOPageResponseEnvironmentGroup.md)
 - [ResponseDTOPageResponseEnvironmentIdentifierResponse](docs/ResponseDTOPageResponseEnvironmentIdentifierResponse.md)
 - [ResponseDTOPageResponseEnvironmentResponse](docs/ResponseDTOPageResponseEnvironmentResponse.md)
 - [ResponseDTOPageResponseFilter](docs/ResponseDTOPageResponseFilter.md)
 - [ResponseDTOPageResponseFreezeSummaryResponse](docs/ResponseDTOPageResponseFreezeSummaryResponse.md)
 - [ResponseDTOPageResponseGitFullSyncEntityInfo](docs/ResponseDTOPageResponseGitFullSyncEntityInfo.md)
 - [ResponseDTOPageResponseGitSyncError](docs/ResponseDTOPageResponseGitSyncError.md)
 - [ResponseDTOPageResponseGitSyncErrorAggregateByCommit](docs/ResponseDTOPageResponseGitSyncErrorAggregateByCommit.md)
 - [ResponseDTOPageResponseHostDTO](docs/ResponseDTOPageResponseHostDTO.md)
 - [ResponseDTOPageResponseInfrastructureResponse](docs/ResponseDTOPageResponseInfrastructureResponse.md)
 - [ResponseDTOPageResponseInputSetSummaryResponse](docs/ResponseDTOPageResponseInputSetSummaryResponse.md)
 - [ResponseDTOPageResponseInvite](docs/ResponseDTOPageResponseInvite.md)
 - [ResponseDTOPageResponseMSDropdownResponse](docs/ResponseDTOPageResponseMSDropdownResponse.md)
 - [ResponseDTOPageResponseMonitoredServiceListItemDTO](docs/ResponseDTOPageResponseMonitoredServiceListItemDTO.md)
 - [ResponseDTOPageResponseMonitoredServicePlatformResponse](docs/ResponseDTOPageResponseMonitoredServicePlatformResponse.md)
 - [ResponseDTOPageResponseMonitoredServiceResponse](docs/ResponseDTOPageResponseMonitoredServiceResponse.md)
 - [ResponseDTOPageResponseNGTriggerDetailsResponseDTO](docs/ResponseDTOPageResponseNGTriggerDetailsResponseDTO.md)
 - [ResponseDTOPageResponseNotificationRuleResponse](docs/ResponseDTOPageResponseNotificationRuleResponse.md)
 - [ResponseDTOPageResponseOrganizationResponse](docs/ResponseDTOPageResponseOrganizationResponse.md)
 - [ResponseDTOPageResponseProjectResponse](docs/ResponseDTOPageResponseProjectResponse.md)
 - [ResponseDTOPageResponseResourceGroupV2Response](docs/ResponseDTOPageResponseResourceGroupV2Response.md)
 - [ResponseDTOPageResponseRoleAssignmentAggregate](docs/ResponseDTOPageResponseRoleAssignmentAggregate.md)
 - [ResponseDTOPageResponseRoleAssignmentResponse](docs/ResponseDTOPageResponseRoleAssignmentResponse.md)
 - [ResponseDTOPageResponseRoleWithPrincipalCountResponse](docs/ResponseDTOPageResponseRoleWithPrincipalCountResponse.md)
 - [ResponseDTOPageResponseSLOConsumptionBreakdown](docs/ResponseDTOPageResponseSLOConsumptionBreakdown.md)
 - [ResponseDTOPageResponseSLOHealthListView](docs/ResponseDTOPageResponseSLOHealthListView.md)
 - [ResponseDTOPageResponseSecretResponse](docs/ResponseDTOPageResponseSecretResponse.md)
 - [ResponseDTOPageResponseServiceAccountAggregate](docs/ResponseDTOPageResponseServiceAccountAggregate.md)
 - [ResponseDTOPageResponseServiceLevelObjectiveV2Response](docs/ResponseDTOPageResponseServiceLevelObjectiveV2Response.md)
 - [ResponseDTOPageResponseServiceOverrideResponse](docs/ResponseDTOPageResponseServiceOverrideResponse.md)
 - [ResponseDTOPageResponseServiceResponse](docs/ResponseDTOPageResponseServiceResponse.md)
 - [ResponseDTOPageResponseTokenAggregate](docs/ResponseDTOPageResponseTokenAggregate.md)
 - [ResponseDTOPageResponseUserAggregate](docs/ResponseDTOPageResponseUserAggregate.md)
 - [ResponseDTOPageResponseUserGroup](docs/ResponseDTOPageResponseUserGroup.md)
 - [ResponseDTOPageResponseUserMetadata](docs/ResponseDTOPageResponseUserMetadata.md)
 - [ResponseDTOPageResponseVariableResponseDTO](docs/ResponseDTOPageResponseVariableResponseDTO.md)
 - [ResponseDTOPageTemplateMetadataSummaryResponse](docs/ResponseDTOPageTemplateMetadataSummaryResponse.md)
 - [ResponseDTOPasswordChangeResponse](docs/ResponseDTOPasswordChangeResponse.md)
 - [ResponseDTOPerspectiveData](docs/ResponseDTOPerspectiveData.md)
 - [ResponseDTOPerspectiveEntityStatsData](docs/ResponseDTOPerspectiveEntityStatsData.md)
 - [ResponseDTOPerspectiveTimeSeriesData](docs/ResponseDTOPerspectiveTimeSeriesData.md)
 - [ResponseDTOPipelineExecutionCountInfo](docs/ResponseDTOPipelineExecutionCountInfo.md)
 - [ResponseDTOPipelineExecutionDetail](docs/ResponseDTOPipelineExecutionDetail.md)
 - [ResponseDTOPipelineExecutionNotes](docs/ResponseDTOPipelineExecutionNotes.md)
 - [ResponseDTOPipelineSaveResponse](docs/ResponseDTOPipelineSaveResponse.md)
 - [ResponseDTOPlanExecutionResponse](docs/ResponseDTOPlanExecutionResponse.md)
 - [ResponseDTOPollingInfoForTriggers](docs/ResponseDTOPollingInfoForTriggers.md)
 - [ResponseDTOProjectResponse](docs/ResponseDTOProjectResponse.md)
 - [ResponseDTORecommendationOverviewStats](docs/ResponseDTORecommendationOverviewStats.md)
 - [ResponseDTORecommendations](docs/ResponseDTORecommendations.md)
 - [ResponseDTORecommendationsIgnoreList](docs/ResponseDTORecommendationsIgnoreList.md)
 - [ResponseDTORefreshResponse](docs/ResponseDTORefreshResponse.md)
 - [ResponseDTOResourceGroupV2Response](docs/ResponseDTOResourceGroupV2Response.md)
 - [ResponseDTOResourceType](docs/ResponseDTOResourceType.md)
 - [ResponseDTORetryHistoryResponse](docs/ResponseDTORetryHistoryResponse.md)
 - [ResponseDTORoleAssignmentAggregateResponse](docs/ResponseDTORoleAssignmentAggregateResponse.md)
 - [ResponseDTORoleAssignmentDeleteResponseDTO](docs/ResponseDTORoleAssignmentDeleteResponseDTO.md)
 - [ResponseDTORoleAssignmentResponse](docs/ResponseDTORoleAssignmentResponse.md)
 - [ResponseDTORoleAssignmentValidationResponse](docs/ResponseDTORoleAssignmentValidationResponse.md)
 - [ResponseDTORoleResponse](docs/ResponseDTORoleResponse.md)
 - [ResponseDTORule](docs/ResponseDTORule.md)
 - [ResponseDTORuleEnforcement](docs/ResponseDTORuleEnforcement.md)
 - [ResponseDTORuleList](docs/ResponseDTORuleList.md)
 - [ResponseDTOSLODashboardDetail](docs/ResponseDTOSLODashboardDetail.md)
 - [ResponseDTOSLORiskCountResponse](docs/ResponseDTOSLORiskCountResponse.md)
 - [ResponseDTOSRMLicenseUsageDTO](docs/ResponseDTOSRMLicenseUsageDTO.md)
 - [ResponseDTOSecondaryEventDetailsResponse](docs/ResponseDTOSecondaryEventDetailsResponse.md)
 - [ResponseDTOSecretManagerMetadataDTO](docs/ResponseDTOSecretManagerMetadataDTO.md)
 - [ResponseDTOSecretResponse](docs/ResponseDTOSecretResponse.md)
 - [ResponseDTOSecretValidationResult](docs/ResponseDTOSecretValidationResult.md)
 - [ResponseDTOServiceAccount](docs/ResponseDTOServiceAccount.md)
 - [ResponseDTOServiceAccountAggregate](docs/ResponseDTOServiceAccountAggregate.md)
 - [ResponseDTOServiceInstanceUsageDTO](docs/ResponseDTOServiceInstanceUsageDTO.md)
 - [ResponseDTOServiceOverrideResponse](docs/ResponseDTOServiceOverrideResponse.md)
 - [ResponseDTOServiceOverrideResponseV2](docs/ResponseDTOServiceOverrideResponseV2.md)
 - [ResponseDTOServiceResponse](docs/ResponseDTOServiceResponse.md)
 - [ResponseDTOServiceUsageDTO](docs/ResponseDTOServiceUsageDTO.md)
 - [ResponseDTOSetEmbeddedUserDetailsDTO](docs/ResponseDTOSetEmbeddedUserDetailsDTO.md)
 - [ResponseDTOSetK8sCommandFlagType](docs/ResponseDTOSetK8sCommandFlagType.md)
 - [ResponseDTOSetKustomizeCommandFlagType](docs/ResponseDTOSetKustomizeCommandFlagType.md)
 - [ResponseDTOSetServiceHookAction](docs/ResponseDTOSetServiceHookAction.md)
 - [ResponseDTOSetString](docs/ResponseDTOSetString.md)
 - [ResponseDTOSettingValueResponseDTO](docs/ResponseDTOSettingValueResponseDTO.md)
 - [ResponseDTOSourceCodeManager](docs/ResponseDTOSourceCodeManager.md)
 - [ResponseDTOString](docs/ResponseDTOString.md)
 - [ResponseDTOTemplateMoveConfigResponse](docs/ResponseDTOTemplateMoveConfigResponse.md)
 - [ResponseDTOTemplateResponse](docs/ResponseDTOTemplateResponse.md)
 - [ResponseDTOTemplateUpdateGitDetailsResponse](docs/ResponseDTOTemplateUpdateGitDetailsResponse.md)
 - [ResponseDTOTemplateWrapperResponse](docs/ResponseDTOTemplateWrapperResponse.md)
 - [ResponseDTOToken](docs/ResponseDTOToken.md)
 - [ResponseDTOTriggerCatalogResponse](docs/ResponseDTOTriggerCatalogResponse.md)
 - [ResponseDTOTriggerGitFullSyncResponse](docs/ResponseDTOTriggerGitFullSyncResponse.md)
 - [ResponseDTOTwoFactorAuthSettingsInfo](docs/ResponseDTOTwoFactorAuthSettingsInfo.md)
 - [ResponseDTOUserAggregate](docs/ResponseDTOUserAggregate.md)
 - [ResponseDTOUserGroup](docs/ResponseDTOUserGroup.md)
 - [ResponseDTOUserGroupResponseV2](docs/ResponseDTOUserGroupResponseV2.md)
 - [ResponseDTOUserInfo](docs/ResponseDTOUserInfo.md)
 - [ResponseDTOValidateTemplateInputsResponseDTO](docs/ResponseDTOValidateTemplateInputsResponseDTO.md)
 - [ResponseDTOValidationResult](docs/ResponseDTOValidationResult.md)
 - [ResponseDTOVariableResponseDTO](docs/ResponseDTOVariableResponseDTO.md)
 - [ResponseDTOVoid](docs/ResponseDTOVoid.md)
 - [ResponseDTOWebhookEventProcessingDetails](docs/ResponseDTOWebhookEventProcessingDetails.md)
 - [ResponseDTOWebhookExecutionDetails](docs/ResponseDTOWebhookExecutionDetails.md)
 - [ResponseDTOWorkloadRecommendationDTO](docs/ResponseDTOWorkloadRecommendationDTO.md)
 - [ResponseDTOZendeskResponseDTO](docs/ResponseDTOZendeskResponseDTO.md)
 - [ResponseMessage](docs/ResponseMessage.md)
 - [ResponseMessageException](docs/ResponseMessageException.md)
 - [ResponseMessageExceptionStackTrace](docs/ResponseMessageExceptionStackTrace.md)
 - [ResponseMessageExceptionSuppressed](docs/ResponseMessageExceptionSuppressed.md)
 - [RestResponseAgentMtlsEndpointDetails](docs/RestResponseAgentMtlsEndpointDetails.md)
 - [RestResponseAnomaliesSummaryDTO](docs/RestResponseAnomaliesSummaryDTO.md)
 - [RestResponseAuthenticationSettingsResponse](docs/RestResponseAuthenticationSettingsResponse.md)
 - [RestResponseBoolean](docs/RestResponseBoolean.md)
 - [RestResponseBusinessMapping](docs/RestResponseBusinessMapping.md)
 - [RestResponseBusinessMappingListDTO](docs/RestResponseBusinessMappingListDTO.md)
 - [RestResponseCollectionLdapGroupResponse](docs/RestResponseCollectionLdapGroupResponse.md)
 - [RestResponseCostCategoryDeleteDTO](docs/RestResponseCostCategoryDeleteDTO.md)
 - [RestResponseDelegateDeleteResponse](docs/RestResponseDelegateDeleteResponse.md)
 - [RestResponseDelegateGroupDTO](docs/RestResponseDelegateGroupDTO.md)
 - [RestResponseDelegateGroupListing](docs/RestResponseDelegateGroupListing.md)
 - [RestResponseDelegateTokenDetails](docs/RestResponseDelegateTokenDetails.md)
 - [RestResponseDowntimeResponse](docs/RestResponseDowntimeResponse.md)
 - [RestResponseHealthMonitoringFlagResponse](docs/RestResponseHealthMonitoringFlagResponse.md)
 - [RestResponseLDAPSettings](docs/RestResponseLDAPSettings.md)
 - [RestResponseLdapResponse](docs/RestResponseLdapResponse.md)
 - [RestResponseListDelegateGroupDTO](docs/RestResponseListDelegateGroupDTO.md)
 - [RestResponseListDelegateListResponse](docs/RestResponseListDelegateListResponse.md)
 - [RestResponseListDelegateTokenDetails](docs/RestResponseListDelegateTokenDetails.md)
 - [RestResponseListHealthSourceDTO](docs/RestResponseListHealthSourceDTO.md)
 - [RestResponseListMetricDTO](docs/RestResponseListMetricDTO.md)
 - [RestResponseListMonitoredServiceChangeDetailSLO](docs/RestResponseListMonitoredServiceChangeDetailSLO.md)
 - [RestResponseListMonitoredServiceDetail](docs/RestResponseListMonitoredServiceDetail.md)
 - [RestResponseListSLOErrorBudgetReset](docs/RestResponseListSLOErrorBudgetReset.md)
 - [RestResponseLoginTypeResponse](docs/RestResponseLoginTypeResponse.md)
 - [RestResponseMonitoredServiceResponse](docs/RestResponseMonitoredServiceResponse.md)
 - [RestResponseNotificationRuleResponse](docs/RestResponseNotificationRuleResponse.md)
 - [RestResponsePageResponseCVNGLog](docs/RestResponsePageResponseCVNGLog.md)
 - [RestResponsePasswordStrengthPolicy](docs/RestResponsePasswordStrengthPolicy.md)
 - [RestResponseSLOErrorBudgetReset](docs/RestResponseSLOErrorBudgetReset.md)
 - [RestResponseSSOConfig](docs/RestResponseSSOConfig.md)
 - [RestResponseServiceLevelObjectiveV2Response](docs/RestResponseServiceLevelObjectiveV2Response.md)
 - [RestResponseString](docs/RestResponseString.md)
 - [RestResponseSupportedDelegateVersion](docs/RestResponseSupportedDelegateVersion.md)
 - [RestResponseTimeGraphResponse](docs/RestResponseTimeGraphResponse.md)
 - [RestResponseUserGroup](docs/RestResponseUserGroup.md)
 - [Results](docs/Results.md)
 - [RetryExecutionInfo](docs/RetryExecutionInfo.md)
 - [RetryExecutionInfoOrBuilder](docs/RetryExecutionInfoOrBuilder.md)
 - [RetryHistoryResponse](docs/RetryHistoryResponse.md)
 - [RetryInterruptConfig](docs/RetryInterruptConfig.md)
 - [RetryStagesMetadata](docs/RetryStagesMetadata.md)
 - [RiskCount](docs/RiskCount.md)
 - [RiskData](docs/RiskData.md)
 - [RiskProfile](docs/RiskProfile.md)
 - [Role](docs/Role.md)
 - [RoleAssignment](docs/RoleAssignment.md)
 - [RoleAssignmentAggregate](docs/RoleAssignmentAggregate.md)
 - [RoleAssignmentAggregateResponse](docs/RoleAssignmentAggregateResponse.md)
 - [RoleAssignmentCreateRequest](docs/RoleAssignmentCreateRequest.md)
 - [RoleAssignmentDeleteResponseDTO](docs/RoleAssignmentDeleteResponseDTO.md)
 - [RoleAssignmentErrorResponseDTO](docs/RoleAssignmentErrorResponseDTO.md)
 - [RoleAssignmentFilter](docs/RoleAssignmentFilter.md)
 - [RoleAssignmentFilterV2](docs/RoleAssignmentFilterV2.md)
 - [RoleAssignmentMetadata](docs/RoleAssignmentMetadata.md)
 - [RoleAssignmentResponse](docs/RoleAssignmentResponse.md)
 - [RoleAssignmentValidationRequest](docs/RoleAssignmentValidationRequest.md)
 - [RoleAssignmentValidationResponse](docs/RoleAssignmentValidationResponse.md)
 - [RoleBinding](docs/RoleBinding.md)
 - [RoleResponse](docs/RoleResponse.md)
 - [RoleScope](docs/RoleScope.md)
 - [RoleWithPrincipalCountResponse](docs/RoleWithPrincipalCountResponse.md)
 - [RolesResponse](docs/RolesResponse.md)
 - [RollingSLOTargetSpec](docs/RollingSLOTargetSpec.md)
 - [RoutingData](docs/RoutingData.md)
 - [RoutingDataK8s](docs/RoutingDataK8s.md)
 - [RoutingDataV2](docs/RoutingDataV2.md)
 - [RoutingRule](docs/RoutingRule.md)
 - [Rule](docs/Rule.md)
 - [RuleClone](docs/RuleClone.md)
 - [RuleEnforcement](docs/RuleEnforcement.md)
 - [RuleList](docs/RuleList.md)
 - [RuleRequest](docs/RuleRequest.md)
 - [RuntimeStreamError](docs/RuntimeStreamError.md)
 - [SLIDTO](docs/SLIDTO.md)
 - [SLIEvaluationType](docs/SLIEvaluationType.md)
 - [SLIMetricSpec](docs/SLIMetricSpec.md)
 - [SLOConsumptionBreakdown](docs/SLOConsumptionBreakdown.md)
 - [SLODashboardApiFilter](docs/SLODashboardApiFilter.md)
 - [SLODashboardDetail](docs/SLODashboardDetail.md)
 - [SLODashboardWidget](docs/SLODashboardWidget.md)
 - [SLOError](docs/SLOError.md)
 - [SLOErrorBudgetReset](docs/SLOErrorBudgetReset.md)
 - [SLOErrorBudgetResetInstanceDetails](docs/SLOErrorBudgetResetInstanceDetails.md)
 - [SLOHealthListView](docs/SLOHealthListView.md)
 - [SLORiskCountResponse](docs/SLORiskCountResponse.md)
 - [SLOTargetDTO](docs/SLOTargetDTO.md)
 - [SLOTargetFilterDTO](docs/SLOTargetFilterDTO.md)
 - [SLOTargetSpec](docs/SLOTargetSpec.md)
 - [SLOTargetType](docs/SLOTargetType.md)
 - [SRMAnalysisStepInstanceDetails](docs/SRMAnalysisStepInstanceDetails.md)
 - [SRMAnalysisStepInstanceDetailsAnalysisDuration](docs/SRMAnalysisStepInstanceDetailsAnalysisDuration.md)
 - [SRMAnalysisStepInstanceDetailsAnalysisDurationUnits](docs/SRMAnalysisStepInstanceDetailsAnalysisDurationUnits.md)
 - [SRMLicenseUsageDTO](docs/SRMLicenseUsageDTO.md)
 - [SSHAuth](docs/SSHAuth.md)
 - [SSHConfig](docs/SSHConfig.md)
 - [SSHCredentialSpec](docs/SSHCredentialSpec.md)
 - [SSHKerberosTGTKeyTabFileSpec](docs/SSHKerberosTGTKeyTabFileSpec.md)
 - [SSHKerberosTGTPasswordSpec](docs/SSHKerberosTGTPasswordSpec.md)
 - [SSHKeyPathCredential](docs/SSHKeyPathCredential.md)
 - [SSHKeyPathSpec](docs/SSHKeyPathSpec.md)
 - [SSHKeyReferenceCredentialDTO](docs/SSHKeyReferenceCredentialDTO.md)
 - [SSHKeyReferenceSpec](docs/SSHKeyReferenceSpec.md)
 - [SSHKeySpec](docs/SSHKeySpec.md)
 - [SSHPasswordCredentialDTO](docs/SSHPasswordCredentialDTO.md)
 - [SSHPasswordSpec](docs/SSHPasswordSpec.md)
 - [SSOConfig](docs/SSOConfig.md)
 - [SSORequest](docs/SSORequest.md)
 - [SSOSettings](docs/SSOSettings.md)
 - [SamlLinkGroupRequest](docs/SamlLinkGroupRequest.md)
 - [SamlmetadatauploadSamlSSOIdBody](docs/SamlmetadatauploadSamlSSOIdBody.md)
 - [SaveServiceRequest](docs/SaveServiceRequest.md)
 - [SaveServiceRequestV2](docs/SaveServiceRequestV2.md)
 - [SaveStaticSchedulesRequest](docs/SaveStaticSchedulesRequest.md)
 - [ScheduledApproval](docs/ScheduledApproval.md)
 - [Scope](docs/Scope.md)
 - [Scope1](docs/Scope1.md)
 - [ScopeName](docs/ScopeName.md)
 - [ScopeResponse](docs/ScopeResponse.md)
 - [ScopeSelector](docs/ScopeSelector.md)
 - [SecondaryEventDetails](docs/SecondaryEventDetails.md)
 - [SecondaryEventDetailsResponse](docs/SecondaryEventDetailsResponse.md)
 - [SecondaryEventsResponse](docs/SecondaryEventsResponse.md)
 - [Secret](docs/Secret.md)
 - [Secret1](docs/Secret1.md)
 - [SecretFileSpec](docs/SecretFileSpec.md)
 - [SecretFileSpec1](docs/SecretFileSpec1.md)
 - [SecretManagerMetadataDTO](docs/SecretManagerMetadataDTO.md)
 - [SecretManagerMetadataRequest](docs/SecretManagerMetadataRequest.md)
 - [SecretManagerMetadataRequestSpecDTO](docs/SecretManagerMetadataRequestSpecDTO.md)
 - [SecretManagerMetadataSpecDTO](docs/SecretManagerMetadataSpecDTO.md)
 - [SecretNGVariable](docs/SecretNGVariable.md)
 - [SecretReferredByConnectorSetupUsageDetail](docs/SecretReferredByConnectorSetupUsageDetail.md)
 - [SecretRequest](docs/SecretRequest.md)
 - [SecretRequestWrapper](docs/SecretRequestWrapper.md)
 - [SecretResourceFilter](docs/SecretResourceFilter.md)
 - [SecretResponse](docs/SecretResponse.md)
 - [SecretResponse1](docs/SecretResponse1.md)
 - [SecretSpec](docs/SecretSpec.md)
 - [SecretSpec1](docs/SecretSpec1.md)
 - [SecretTextSpec](docs/SecretTextSpec.md)
 - [SecretTextSpec1](docs/SecretTextSpec1.md)
 - [SecretTextSpecAdditionalMetadata](docs/SecretTextSpecAdditionalMetadata.md)
 - [SecretValidationMetaData](docs/SecretValidationMetaData.md)
 - [SecretValidationMetadata](docs/SecretValidationMetadata.md)
 - [SecretValidationResponse](docs/SecretValidationResponse.md)
 - [SecretValidationResult](docs/SecretValidationResult.md)
 - [SecretsFilesBody](docs/SecretsFilesBody.md)
 - [Segment](docs/Segment.md)
 - [SegmentFlag](docs/SegmentFlag.md)
 - [Segments](docs/Segments.md)
 - [Serve](docs/Serve.md)
 - [Service](docs/Service.md)
 - [ServiceAccount](docs/ServiceAccount.md)
 - [ServiceAccountAggregate](docs/ServiceAccountAggregate.md)
 - [ServiceAccountConfig](docs/ServiceAccountConfig.md)
 - [ServiceDep](docs/ServiceDep.md)
 - [ServiceDepTree](docs/ServiceDepTree.md)
 - [ServiceDependencyDTO](docs/ServiceDependencyDTO.md)
 - [ServiceDependencyMetadata](docs/ServiceDependencyMetadata.md)
 - [ServiceDescriptor](docs/ServiceDescriptor.md)
 - [ServiceDescriptorProto](docs/ServiceDescriptorProto.md)
 - [ServiceDescriptorProtoOrBuilder](docs/ServiceDescriptorProtoOrBuilder.md)
 - [ServiceDiagnostics](docs/ServiceDiagnostics.md)
 - [ServiceDiagnosticsResponse](docs/ServiceDiagnosticsResponse.md)
 - [ServiceError](docs/ServiceError.md)
 - [ServiceHealthResponse](docs/ServiceHealthResponse.md)
 - [ServiceInstanceUsageDTO](docs/ServiceInstanceUsageDTO.md)
 - [ServiceLevelIndicatorDTO](docs/ServiceLevelIndicatorDTO.md)
 - [ServiceLevelIndicatorSpec](docs/ServiceLevelIndicatorSpec.md)
 - [ServiceLevelObjectiveDetailsDTO](docs/ServiceLevelObjectiveDetailsDTO.md)
 - [ServiceLevelObjectiveSpec](docs/ServiceLevelObjectiveSpec.md)
 - [ServiceLevelObjectiveType](docs/ServiceLevelObjectiveType.md)
 - [ServiceLevelObjectiveV2Response](docs/ServiceLevelObjectiveV2Response.md)
 - [ServiceMetadata](docs/ServiceMetadata.md)
 - [ServiceMetadataAutostoppingProxyConfig](docs/ServiceMetadataAutostoppingProxyConfig.md)
 - [ServiceMetadataCloudProviderDetails](docs/ServiceMetadataCloudProviderDetails.md)
 - [ServiceNowADFS](docs/ServiceNowADFS.md)
 - [ServiceNowApprovalInstanceDetails](docs/ServiceNowApprovalInstanceDetails.md)
 - [ServiceNowAuthCredentials](docs/ServiceNowAuthCredentials.md)
 - [ServiceNowAuthentication](docs/ServiceNowAuthentication.md)
 - [ServiceNowChangeWindowSpec](docs/ServiceNowChangeWindowSpec.md)
 - [ServiceNowConnector](docs/ServiceNowConnector.md)
 - [ServiceNowFieldValueNG](docs/ServiceNowFieldValueNG.md)
 - [ServiceNowRefreshToken](docs/ServiceNowRefreshToken.md)
 - [ServiceNowTicketKeyNG](docs/ServiceNowTicketKeyNG.md)
 - [ServiceNowTicketNG](docs/ServiceNowTicketNG.md)
 - [ServiceNowUserNamePassword](docs/ServiceNowUserNamePassword.md)
 - [ServiceOptions](docs/ServiceOptions.md)
 - [ServiceOptionsOrBuilder](docs/ServiceOptionsOrBuilder.md)
 - [ServiceOverrideRequest](docs/ServiceOverrideRequest.md)
 - [ServiceOverrideRequestV2](docs/ServiceOverrideRequestV2.md)
 - [ServiceOverrideResponse](docs/ServiceOverrideResponse.md)
 - [ServiceOverrideResponseV2](docs/ServiceOverrideResponseV2.md)
 - [ServiceOverrideSpec](docs/ServiceOverrideSpec.md)
 - [ServiceRequest](docs/ServiceRequest.md)
 - [ServiceRequest1](docs/ServiceRequest1.md)
 - [ServiceResponse](docs/ServiceResponse.md)
 - [ServiceResponse1](docs/ServiceResponse1.md)
 - [ServiceResponseDetails](docs/ServiceResponseDetails.md)
 - [ServiceUsageDTO](docs/ServiceUsageDTO.md)
 - [ServiceUsageRecord](docs/ServiceUsageRecord.md)
 - [ServiceV2](docs/ServiceV2.md)
 - [ServiceVersion](docs/ServiceVersion.md)
 - [ServicesResponse](docs/ServicesResponse.md)
 - [Servicev1AppProjectMapping](docs/Servicev1AppProjectMapping.md)
 - [Servicev1Application](docs/Servicev1Application.md)
 - [Servicev1ApplicationDeleteRequestOptions](docs/Servicev1ApplicationDeleteRequestOptions.md)
 - [Servicev1ApplicationPatchRequest](docs/Servicev1ApplicationPatchRequest.md)
 - [Servicev1ApplicationQuery](docs/Servicev1ApplicationQuery.md)
 - [Servicev1Applicationlist](docs/Servicev1Applicationlist.md)
 - [Servicev1Cluster](docs/Servicev1Cluster.md)
 - [Servicev1ClusterQuery](docs/Servicev1ClusterQuery.md)
 - [Servicev1GnuPGPublicKeyList](docs/Servicev1GnuPGPublicKeyList.md)
 - [Servicev1HealthStatus](docs/Servicev1HealthStatus.md)
 - [Servicev1Project](docs/Servicev1Project.md)
 - [Servicev1ReconcilerFilter](docs/Servicev1ReconcilerFilter.md)
 - [Servicev1Repository](docs/Servicev1Repository.md)
 - [Servicev1RepositoryCertificate](docs/Servicev1RepositoryCertificate.md)
 - [Servicev1RepositoryCredentials](docs/Servicev1RepositoryCredentials.md)
 - [Servicev1RepositoryCredentialsList](docs/Servicev1RepositoryCredentialsList.md)
 - [ServingRule](docs/ServingRule.md)
 - [SessionTimeoutSettings](docs/SessionTimeoutSettings.md)
 - [SettingDTO](docs/SettingDTO.md)
 - [SettingRequestDTO](docs/SettingRequestDTO.md)
 - [SettingResponseDTO](docs/SettingResponseDTO.md)
 - [SettingUpdateResponseDTO](docs/SettingUpdateResponseDTO.md)
 - [SettingValueResponseDTO](docs/SettingValueResponseDTO.md)
 - [SetupUsageDetail](docs/SetupUsageDetail.md)
 - [SetupValidateSuccessResponse](docs/SetupValidateSuccessResponse.md)
 - [SetupValidateSuccessResponseResponse](docs/SetupValidateSuccessResponseResponse.md)
 - [SharedCost](docs/SharedCost.md)
 - [SharedCostSplit](docs/SharedCostSplit.md)
 - [SignalFXConnectorDTO](docs/SignalFXConnectorDTO.md)
 - [SimpleServiceLevelObjectiveSpec](docs/SimpleServiceLevelObjectiveSpec.md)
 - [SkipInfo](docs/SkipInfo.md)
 - [SkipTaskExecutableResponse](docs/SkipTaskExecutableResponse.md)
 - [SkipTaskExecutableResponseOrBuilder](docs/SkipTaskExecutableResponseOrBuilder.md)
 - [SlackConfigDTO](docs/SlackConfigDTO.md)
 - [SloHealthIndicatorDTO](docs/SloHealthIndicatorDTO.md)
 - [SmtpConfig](docs/SmtpConfig.md)
 - [Sort](docs/Sort.md)
 - [SortOrder](docs/SortOrder.md)
 - [Source](docs/Source.md)
 - [SourceCodeInfo](docs/SourceCodeInfo.md)
 - [SourceCodeInfoOrBuilder](docs/SourceCodeInfoOrBuilder.md)
 - [SourceCodeManager](docs/SourceCodeManager.md)
 - [SourceCodeManagerAuthentication](docs/SourceCodeManagerAuthentication.md)
 - [Sources](docs/Sources.md)
 - [SplunkConnector](docs/SplunkConnector.md)
 - [SplunkHealthSource](docs/SplunkHealthSource.md)
 - [SplunkHealthSourceQueryDTO](docs/SplunkHealthSourceQueryDTO.md)
 - [SplunkMetricDefinition](docs/SplunkMetricDefinition.md)
 - [SplunkMetricHealthSource](docs/SplunkMetricHealthSource.md)
 - [SpotConnector](docs/SpotConnector.md)
 - [SpotCredential](docs/SpotCredential.md)
 - [SpotCredentialSpec](docs/SpotCredentialSpec.md)
 - [SpotPermanentTokenConfigSpec](docs/SpotPermanentTokenConfigSpec.md)
 - [StackdriverDefinition](docs/StackdriverDefinition.md)
 - [StackdriverLogHealthSource](docs/StackdriverLogHealthSource.md)
 - [StackdriverLogHealthSourceQueryDTO](docs/StackdriverLogHealthSourceQueryDTO.md)
 - [StackdriverMetricHealthSource](docs/StackdriverMetricHealthSource.md)
 - [StaticAuditFilter](docs/StaticAuditFilter.md)
 - [StaticScheduleResource](docs/StaticScheduleResource.md)
 - [StatusWiseCount](docs/StatusWiseCount.md)
 - [StepType](docs/StepType.md)
 - [StepTypeOrBuilder](docs/StepTypeOrBuilder.md)
 - [StoreConfig](docs/StoreConfig.md)
 - [StoreConfigWrapper](docs/StoreConfigWrapper.md)
 - [StoreConfigWrapperParameters](docs/StoreConfigWrapperParameters.md)
 - [StrategyMetadata](docs/StrategyMetadata.md)
 - [StrategyMetadataOrBuilder](docs/StrategyMetadataOrBuilder.md)
 - [StreamResultOfApplicationsApplicationTree](docs/StreamResultOfApplicationsApplicationTree.md)
 - [StreamResultOfApplicationsApplicationWatchEvent](docs/StreamResultOfApplicationsApplicationWatchEvent.md)
 - [StreamResultOfApplicationsLogEntry](docs/StreamResultOfApplicationsLogEntry.md)
 - [StreamingDestinationAggregateDTO](docs/StreamingDestinationAggregateDTO.md)
 - [StreamingDestinationCards](docs/StreamingDestinationCards.md)
 - [StreamingDestinationDTO](docs/StreamingDestinationDTO.md)
 - [StreamingDestinationResponse](docs/StreamingDestinationResponse.md)
 - [StreamingDestinationSpecDTO](docs/StreamingDestinationSpecDTO.md)
 - [StreamingDestinationStatus](docs/StreamingDestinationStatus.md)
 - [StringNGVariable](docs/StringNGVariable.md)
 - [StringValue](docs/StringValue.md)
 - [StringValueOrBuilder](docs/StringValueOrBuilder.md)
 - [StringVariableConfigDTO](docs/StringVariableConfigDTO.md)
 - [SumoLogicConnectorDTO](docs/SumoLogicConnectorDTO.md)
 - [SupportedDelegateVersion](docs/SupportedDelegateVersion.md)
 - [SyncExecutableResponse](docs/SyncExecutableResponse.md)
 - [SyncExecutableResponseOrBuilder](docs/SyncExecutableResponseOrBuilder.md)
 - [TCPProxy](docs/TCPProxy.md)
 - [TGTGenerationSpecDTO](docs/TGTGenerationSpecDTO.md)
 - [TGTKeyTabFilePathSpecDTO](docs/TGTKeyTabFilePathSpecDTO.md)
 - [TGTPasswordSpecDTO](docs/TGTPasswordSpecDTO.md)
 - [Tag](docs/Tag.md)
 - [TagResponseMetadata](docs/TagResponseMetadata.md)
 - [TagResponseMetadataDetails](docs/TagResponseMetadataDetails.md)
 - [Tags](docs/Tags.md)
 - [Target](docs/Target.md)
 - [TargetDetail](docs/TargetDetail.md)
 - [TargetDetailSegment](docs/TargetDetailSegment.md)
 - [TargetExecutionSummary](docs/TargetExecutionSummary.md)
 - [TargetGroupMinimal](docs/TargetGroupMinimal.md)
 - [TargetMap](docs/TargetMap.md)
 - [Targets](docs/Targets.md)
 - [TargetsUploadBody](docs/TargetsUploadBody.md)
 - [TasConnector](docs/TasConnector.md)
 - [TasCredential](docs/TasCredential.md)
 - [TasCredentialSpec](docs/TasCredentialSpec.md)
 - [TasManualDetails](docs/TasManualDetails.md)
 - [TaskChainExecutableResponse](docs/TaskChainExecutableResponse.md)
 - [TaskChainExecutableResponseOrBuilder](docs/TaskChainExecutableResponseOrBuilder.md)
 - [TaskExecutableResponse](docs/TaskExecutableResponse.md)
 - [TaskExecutableResponseOrBuilder](docs/TaskExecutableResponseOrBuilder.md)
 - [TemplateCreateRequestBody](docs/TemplateCreateRequestBody.md)
 - [TemplateDTO](docs/TemplateDTO.md)
 - [TemplateEntityGitDetails](docs/TemplateEntityGitDetails.md)
 - [TemplateError](docs/TemplateError.md)
 - [TemplateErrorMetadata](docs/TemplateErrorMetadata.md)
 - [TemplateErrorNodeSummary](docs/TemplateErrorNodeSummary.md)
 - [TemplateEventData](docs/TemplateEventData.md)
 - [TemplateFailure](docs/TemplateFailure.md)
 - [TemplateFilterProperties](docs/TemplateFilterProperties.md)
 - [TemplateGovernanceMetadata](docs/TemplateGovernanceMetadata.md)
 - [TemplateImportRequestBody](docs/TemplateImportRequestBody.md)
 - [TemplateImportRequestDTO](docs/TemplateImportRequestDTO.md)
 - [TemplateImportResponseBody](docs/TemplateImportResponseBody.md)
 - [TemplateInfo](docs/TemplateInfo.md)
 - [TemplateLinkConfigForCustomSecretManager](docs/TemplateLinkConfigForCustomSecretManager.md)
 - [TemplateMetaDataList](docs/TemplateMetaDataList.md)
 - [TemplateMetadataSummaryResponse](docs/TemplateMetadataSummaryResponse.md)
 - [TemplateMoveConfigResponse](docs/TemplateMoveConfigResponse.md)
 - [TemplateNodeInfo](docs/TemplateNodeInfo.md)
 - [TemplatePolicyMetadata](docs/TemplatePolicyMetadata.md)
 - [TemplatePolicySetMetadata](docs/TemplatePolicySetMetadata.md)
 - [TemplatePolicySetMetadataOrBuilder](docs/TemplatePolicySetMetadataOrBuilder.md)
 - [TemplateReferenceProtoDTO](docs/TemplateReferenceProtoDTO.md)
 - [TemplateReferenceProtoDTOOrBuilder](docs/TemplateReferenceProtoDTOOrBuilder.md)
 - [TemplateResponse](docs/TemplateResponse.md)
 - [TemplateResponseDTOValidateTemplateInputsResponseDTO](docs/TemplateResponseDTOValidateTemplateInputsResponseDTO.md)
 - [TemplateResponseMessage](docs/TemplateResponseMessage.md)
 - [TemplateSchemaResponse](docs/TemplateSchemaResponse.md)
 - [TemplateScope](docs/TemplateScope.md)
 - [TemplateTemplateMetadataSummaryResponse](docs/TemplateTemplateMetadataSummaryResponse.md)
 - [TemplateTemplateResponse](docs/TemplateTemplateResponse.md)
 - [TemplateUpdateGitDetailsRequest](docs/TemplateUpdateGitDetailsRequest.md)
 - [TemplateUpdateGitDetailsResponse](docs/TemplateUpdateGitDetailsResponse.md)
 - [TemplateUpdateRequestBody](docs/TemplateUpdateRequestBody.md)
 - [TemplateUpdateStableResponse](docs/TemplateUpdateStableResponse.md)
 - [TemplateValidationResponseBody](docs/TemplateValidationResponseBody.md)
 - [TemplateWithInputsResponse](docs/TemplateWithInputsResponse.md)
 - [TemplateWrapperResponse](docs/TemplateWrapperResponse.md)
 - [TerraformCloudConnector](docs/TerraformCloudConnector.md)
 - [TerraformCloudCredential](docs/TerraformCloudCredential.md)
 - [TerraformCloudCredentialSpec](docs/TerraformCloudCredentialSpec.md)
 - [TerraformCloudTokenCredentials](docs/TerraformCloudTokenCredentials.md)
 - [TestErrorMetadata](docs/TestErrorMetadata.md)
 - [ThresholdSLIMetricSpec](docs/ThresholdSLIMetricSpec.md)
 - [TimeGraphResponse](docs/TimeGraphResponse.md)
 - [TimeInDay](docs/TimeInDay.md)
 - [TimeRangeFilter](docs/TimeRangeFilter.md)
 - [TimeRangeParams](docs/TimeRangeParams.md)
 - [TimeSchedule](docs/TimeSchedule.md)
 - [TimeScheduleDays](docs/TimeScheduleDays.md)
 - [TimeSchedulePeriod](docs/TimeSchedulePeriod.md)
 - [TimeSeriesDataPoints](docs/TimeSeriesDataPoints.md)
 - [TimeSeriesMetricPackDTO](docs/TimeSeriesMetricPackDTO.md)
 - [TimeoutIssuer](docs/TimeoutIssuer.md)
 - [TimestampInfo](docs/TimestampInfo.md)
 - [Token](docs/Token.md)
 - [TokenAggregate](docs/TokenAggregate.md)
 - [TotalResourceUsage](docs/TotalResourceUsage.md)
 - [TriggerCatalogItem](docs/TriggerCatalogItem.md)
 - [TriggerCatalogResponse](docs/TriggerCatalogResponse.md)
 - [TriggerEventStatus](docs/TriggerEventStatus.md)
 - [TriggerFilterProperties](docs/TriggerFilterProperties.md)
 - [TriggerGitFullSyncResponse](docs/TriggerGitFullSyncResponse.md)
 - [TriggerIssuer](docs/TriggerIssuer.md)
 - [TriggerReferenceProtoDTO](docs/TriggerReferenceProtoDTO.md)
 - [TriggerReferenceProtoDTOOrBuilder](docs/TriggerReferenceProtoDTOOrBuilder.md)
 - [TriggerStatus](docs/TriggerStatus.md)
 - [TriggeredBy](docs/TriggeredBy.md)
 - [TriggeredByInfoAuditDetails](docs/TriggeredByInfoAuditDetails.md)
 - [TriggeredByOrBuilder](docs/TriggeredByOrBuilder.md)
 - [TwoFactorAdminOverrideSettings](docs/TwoFactorAdminOverrideSettings.md)
 - [TwoFactorAuthSettingsInfo](docs/TwoFactorAuthSettingsInfo.md)
 - [UnallocatedCost](docs/UnallocatedCost.md)
 - [UninterpretedOption](docs/UninterpretedOption.md)
 - [UninterpretedOptionOrBuilder](docs/UninterpretedOptionOrBuilder.md)
 - [UnitProgress](docs/UnitProgress.md)
 - [UnknownFieldSet](docs/UnknownFieldSet.md)
 - [UpdateGitXWebhookRequest](docs/UpdateGitXWebhookRequest.md)
 - [UpdateGitXWebhookResponse](docs/UpdateGitXWebhookResponse.md)
 - [UpdateOrganizationRequest](docs/UpdateOrganizationRequest.md)
 - [UpdateProjectRequest](docs/UpdateProjectRequest.md)
 - [UpdateRequestBody](docs/UpdateRequestBody.md)
 - [UpdateRequestBody2](docs/UpdateRequestBody2.md)
 - [UsageDataDTO](docs/UsageDataDTO.md)
 - [UserAggregate](docs/UserAggregate.md)
 - [UserFilter](docs/UserFilter.md)
 - [UserGroup](docs/UserGroup.md)
 - [UserGroupFilter](docs/UserGroupFilter.md)
 - [UserGroupRequestV2](docs/UserGroupRequestV2.md)
 - [UserGroupResponseV2](docs/UserGroupResponseV2.md)
 - [UserInfo](docs/UserInfo.md)
 - [UserInfoUpdateDTO](docs/UserInfoUpdateDTO.md)
 - [UserInvitationAuditEventData](docs/UserInvitationAuditEventData.md)
 - [UserInviteAuditEventData](docs/UserInviteAuditEventData.md)
 - [UserJourney](docs/UserJourney.md)
 - [UserJourneyDTO](docs/UserJourneyDTO.md)
 - [UserMembershipAuditEventData](docs/UserMembershipAuditEventData.md)
 - [UserMetadata](docs/UserMetadata.md)
 - [UtmInfo](docs/UtmInfo.md)
 - [V1Agent](docs/V1Agent.md)
 - [V1AgentComponentHealth](docs/V1AgentComponentHealth.md)
 - [V1AgentCredentials](docs/V1AgentCredentials.md)
 - [V1AgentHealth](docs/V1AgentHealth.md)
 - [V1AgentList](docs/V1AgentList.md)
 - [V1AgentMetadata](docs/V1AgentMetadata.md)
 - [V1AgentScope](docs/V1AgentScope.md)
 - [V1AgentType](docs/V1AgentType.md)
 - [V1ApplicationStatusCounts](docs/V1ApplicationStatusCounts.md)
 - [V1ApplicationSyncStatus](docs/V1ApplicationSyncStatus.md)
 - [V1ApplicationSyncStatusQuery](docs/V1ApplicationSyncStatusQuery.md)
 - [V1ApplicationSyncStatuslist](docs/V1ApplicationSyncStatuslist.md)
 - [V1Certificatelist](docs/V1Certificatelist.md)
 - [V1Clusterlist](docs/V1Clusterlist.md)
 - [V1ConnectedStatus](docs/V1ConnectedStatus.md)
 - [V1DashboardOverview](docs/V1DashboardOverview.md)
 - [V1DeploymentsDetails](docs/V1DeploymentsDetails.md)
 - [V1Empty](docs/V1Empty.md)
 - [V1EventList](docs/V1EventList.md)
 - [V1EventSeries](docs/V1EventSeries.md)
 - [V1EventSource](docs/V1EventSource.md)
 - [V1FieldsV1](docs/V1FieldsV1.md)
 - [V1Gnupg](docs/V1Gnupg.md)
 - [V1GroupKind](docs/V1GroupKind.md)
 - [V1HealthStatusCounts](docs/V1HealthStatusCounts.md)
 - [V1ListMeta](docs/V1ListMeta.md)
 - [V1LoadBalancerIngress](docs/V1LoadBalancerIngress.md)
 - [V1ManagedFieldsEntry](docs/V1ManagedFieldsEntry.md)
 - [V1MicroTime](docs/V1MicroTime.md)
 - [V1NodeSystemInfo](docs/V1NodeSystemInfo.md)
 - [V1ObjectMeta](docs/V1ObjectMeta.md)
 - [V1ObjectReference](docs/V1ObjectReference.md)
 - [V1OperationPhase](docs/V1OperationPhase.md)
 - [V1OwnerReference](docs/V1OwnerReference.md)
 - [V1PortStatus](docs/V1PortStatus.md)
 - [V1RecentDeploymentQuery](docs/V1RecentDeploymentQuery.md)
 - [V1RecentDeploymentsDetailsList](docs/V1RecentDeploymentsDetailsList.md)
 - [V1RecentlyCreatedCount](docs/V1RecentlyCreatedCount.md)
 - [V1RecentlyCreatedOverview](docs/V1RecentlyCreatedOverview.md)
 - [V1RepositoryCredentialsQuery](docs/V1RepositoryCredentialsQuery.md)
 - [V1RepositoryQuery](docs/V1RepositoryQuery.md)
 - [V1Repositorylist](docs/V1Repositorylist.md)
 - [V1SemanticVersion](docs/V1SemanticVersion.md)
 - [V1SyncStatusCounts](docs/V1SyncStatusCounts.md)
 - [V1Time](docs/V1Time.md)
 - [V1TopApplicationPhaseStats](docs/V1TopApplicationPhaseStats.md)
 - [V1TopApplicationPhaseStatsList](docs/V1TopApplicationPhaseStatsList.md)
 - [V1UniqueMessage](docs/V1UniqueMessage.md)
 - [V1User](docs/V1User.md)
 - [ValidateTemplateInputsResponseDTO](docs/ValidateTemplateInputsResponseDTO.md)
 - [ValidationError](docs/ValidationError.md)
 - [ValidationResult](docs/ValidationResult.md)
 - [ValidationStatus](docs/ValidationStatus.md)
 - [ValueDataPoint](docs/ValueDataPoint.md)
 - [Variable](docs/Variable.md)
 - [VariableConfigDTO](docs/VariableConfigDTO.md)
 - [VariableDTO](docs/VariableDTO.md)
 - [VariableRequestDTO](docs/VariableRequestDTO.md)
 - [VariableResponseDTO](docs/VariableResponseDTO.md)
 - [Variation](docs/Variation.md)
 - [VariationMap](docs/VariationMap.md)
 - [VaultConnector](docs/VaultConnector.md)
 - [ViewCondition](docs/ViewCondition.md)
 - [ViewField](docs/ViewField.md)
 - [ViewIdCondition](docs/ViewIdCondition.md)
 - [ViewPreferences](docs/ViewPreferences.md)
 - [ViewRule](docs/ViewRule.md)
 - [ViewTimeRange](docs/ViewTimeRange.md)
 - [ViewVisualization](docs/ViewVisualization.md)
 - [VirtualMachine](docs/VirtualMachine.md)
 - [WebhookAutoRegistrationStatus](docs/WebhookAutoRegistrationStatus.md)
 - [WebhookDetails](docs/WebhookDetails.md)
 - [WebhookEventProcessingDetails](docs/WebhookEventProcessingDetails.md)
 - [WebhookExecutionDetails](docs/WebhookExecutionDetails.md)
 - [WebhookInfo](docs/WebhookInfo.md)
 - [WeeklyCalendarSpec](docs/WeeklyCalendarSpec.md)
 - [WeightedVariation](docs/WeightedVariation.md)
 - [WinRmAuth](docs/WinRmAuth.md)
 - [WinRmCommandParameter](docs/WinRmCommandParameter.md)
 - [WinRmCredentialsSpec](docs/WinRmCredentialsSpec.md)
 - [WinRmNTLMSpec](docs/WinRmNTLMSpec.md)
 - [WinRmTGTKeyTabFileSpec](docs/WinRmTGTKeyTabFileSpec.md)
 - [WinRmTGTPasswordSpec](docs/WinRmTGTPasswordSpec.md)
 - [WindowBasedServiceLevelIndicatorSpec](docs/WindowBasedServiceLevelIndicatorSpec.md)
 - [WorkloadRecommendationDTO](docs/WorkloadRecommendationDTO.md)
 - [YAMLSchemaErrorWrapper](docs/YAMLSchemaErrorWrapper.md)
 - [YamlDiffRecord](docs/YamlDiffRecord.md)
 - [YamlDiffRecordDTO](docs/YamlDiffRecordDTO.md)
 - [YamlSchemaErrorDTO](docs/YamlSchemaErrorDTO.md)
 - [YamlSchemaErrorWrapperDTO](docs/YamlSchemaErrorWrapperDTO.md)
 - [ZendeskResponseDTO](docs/ZendeskResponseDTO.md)

## Documentation For Authorization


## x-api-key

- **Type**: API key
- **API key parameter name**: x-api-key
- **Location**: HTTP header


## Author

contact@harness.io
