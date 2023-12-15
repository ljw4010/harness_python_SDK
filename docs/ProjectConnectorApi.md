# swagger_client.ProjectConnectorApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project_scoped_connector**](ProjectConnectorApi.md#create_project_scoped_connector) | **POST** /v1/orgs/{org}/projects/{project}/connectors | Create a Connector
[**delete_project_scoped_connector**](ProjectConnectorApi.md#delete_project_scoped_connector) | **DELETE** /v1/orgs/{org}/projects/{project}/connectors/{connector} | Delete a connector
[**get_project_scoped_connector**](ProjectConnectorApi.md#get_project_scoped_connector) | **GET** /v1/orgs/{org}/projects/{project}/connectors/{connector} | Retrieve a connector
[**test_project_scoped_connector**](ProjectConnectorApi.md#test_project_scoped_connector) | **GET** /v1/orgs/{org}/projects/{project}/connectors/{connector}/test-connection | Test a connector
[**update_project_scoped_connector**](ProjectConnectorApi.md#update_project_scoped_connector) | **PUT** /v1/orgs/{org}/projects/{project}/connectors/{connector} | Update a connector

# **create_project_scoped_connector**
> ConnectorResponse create_project_scoped_connector(body, org, project, harness_account=harness_account)

Create a Connector

Creates a new connector

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
api_instance = swagger_client.ProjectConnectorApi(swagger_client.ApiClient(configuration))
body = swagger_client.ConnectorRequest() # ConnectorRequest | 
org = 'org_example' # str | Identifier field of the organization the resource is scoped to
project = 'project_example' # str | Identifier field of the project the resource is scoped to
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)

try:
    # Create a Connector
    api_response = api_instance.create_project_scoped_connector(body, org, project, harness_account=harness_account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectConnectorApi->create_project_scoped_connector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConnectorRequest**](ConnectorRequest.md)|  | 
 **org** | **str**| Identifier field of the organization the resource is scoped to | 
 **project** | **str**| Identifier field of the project the resource is scoped to | 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 

### Return type

[**ConnectorResponse**](ConnectorResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project_scoped_connector**
> delete_project_scoped_connector(org, project, connector, harness_account=harness_account)

Delete a connector

Deletes the information of the connector with the matching connector identifier. Connector types supported are GIT, ARTIFACTORY, APP_DYNAMICS and AZURE.

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
api_instance = swagger_client.ProjectConnectorApi(swagger_client.ApiClient(configuration))
org = 'org_example' # str | Identifier field of the organization the resource is scoped to
project = 'project_example' # str | Identifier field of the project the resource is scoped to
connector = 'connector_example' # str | Connector identifier
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)

try:
    # Delete a connector
    api_instance.delete_project_scoped_connector(org, project, connector, harness_account=harness_account)
except ApiException as e:
    print("Exception when calling ProjectConnectorApi->delete_project_scoped_connector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| Identifier field of the organization the resource is scoped to | 
 **project** | **str**| Identifier field of the project the resource is scoped to | 
 **connector** | **str**| Connector identifier | 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_scoped_connector**
> ConnectorResponse get_project_scoped_connector(org, project, connector, harness_account=harness_account)

Retrieve a connector

Retrieves the information of the connector with the matching connector identifier. Connector types supported are GIT, ARTIFACTORY, APP_DYNAMICS and AZURE. 

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
api_instance = swagger_client.ProjectConnectorApi(swagger_client.ApiClient(configuration))
org = 'org_example' # str | Identifier field of the organization the resource is scoped to
project = 'project_example' # str | Identifier field of the project the resource is scoped to
connector = 'connector_example' # str | Connector identifier
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)

try:
    # Retrieve a connector
    api_response = api_instance.get_project_scoped_connector(org, project, connector, harness_account=harness_account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectConnectorApi->get_project_scoped_connector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| Identifier field of the organization the resource is scoped to | 
 **project** | **str**| Identifier field of the project the resource is scoped to | 
 **connector** | **str**| Connector identifier | 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 

### Return type

[**ConnectorResponse**](ConnectorResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_project_scoped_connector**
> ConnectorTestConnectionResponse test_project_scoped_connector(org, project, connector, harness_account=harness_account)

Test a connector

Tests connection of the connector with the matching connector identifier. 

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
api_instance = swagger_client.ProjectConnectorApi(swagger_client.ApiClient(configuration))
org = 'org_example' # str | Identifier field of the organization the resource is scoped to
project = 'project_example' # str | Identifier field of the project the resource is scoped to
connector = 'connector_example' # str | Connector identifier
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)

try:
    # Test a connector
    api_response = api_instance.test_project_scoped_connector(org, project, connector, harness_account=harness_account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectConnectorApi->test_project_scoped_connector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| Identifier field of the organization the resource is scoped to | 
 **project** | **str**| Identifier field of the project the resource is scoped to | 
 **connector** | **str**| Connector identifier | 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 

### Return type

[**ConnectorTestConnectionResponse**](ConnectorTestConnectionResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project_scoped_connector**
> ConnectorResponse update_project_scoped_connector(body, org, project, connector, harness_account=harness_account)

Update a connector

Updates the information of the secret with the matching secret identifier.

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
api_instance = swagger_client.ProjectConnectorApi(swagger_client.ApiClient(configuration))
body = swagger_client.ConnectorRequest() # ConnectorRequest | 
org = 'org_example' # str | Identifier field of the organization the resource is scoped to
project = 'project_example' # str | Identifier field of the project the resource is scoped to
connector = 'connector_example' # str | Connector identifier
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)

try:
    # Update a connector
    api_response = api_instance.update_project_scoped_connector(body, org, project, connector, harness_account=harness_account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectConnectorApi->update_project_scoped_connector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConnectorRequest**](ConnectorRequest.md)|  | 
 **org** | **str**| Identifier field of the organization the resource is scoped to | 
 **project** | **str**| Identifier field of the project the resource is scoped to | 
 **connector** | **str**| Connector identifier | 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 

### Return type

[**ConnectorResponse**](ConnectorResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

