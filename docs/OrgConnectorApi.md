# harness_python_sdk.OrgConnectorApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_org_scoped_connector**](OrgConnectorApi.md#create_org_scoped_connector) | **POST** /v1/orgs/{org}/connectors | Create a Connector
[**delete_org_scoped_connector**](OrgConnectorApi.md#delete_org_scoped_connector) | **DELETE** /v1/orgs/{org}/connectors/{connector} | Delete a connector
[**get_org_scoped_connector**](OrgConnectorApi.md#get_org_scoped_connector) | **GET** /v1/orgs/{org}/connectors/{connector} | Retrieve a connector
[**test_org_scoped_connector**](OrgConnectorApi.md#test_org_scoped_connector) | **GET** /v1/orgs/{org}/connectors/{connector}/test-connection | Test a connector
[**update_org_scoped_connector**](OrgConnectorApi.md#update_org_scoped_connector) | **PUT** /v1/orgs/{org}/connectors/{connector} | Update a connector

# **create_org_scoped_connector**
> ConnectorResponse create_org_scoped_connector(body, org, harness_account=harness_account)

Create a Connector

Creates a new connector

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
api_instance = harness_python_sdk.OrgConnectorApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.ConnectorRequest() # ConnectorRequest | 
org = 'org_example' # str | Identifier field of the organization the resource is scoped to
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)

try:
    # Create a Connector
    api_response = api_instance.create_org_scoped_connector(body, org, harness_account=harness_account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgConnectorApi->create_org_scoped_connector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConnectorRequest**](ConnectorRequest.md)|  | 
 **org** | **str**| Identifier field of the organization the resource is scoped to | 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 

### Return type

[**ConnectorResponse**](ConnectorResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_org_scoped_connector**
> delete_org_scoped_connector(org, connector, harness_account=harness_account)

Delete a connector

Deletes the information of the connector with the matching connector identifier. Connector types supported are GIT, ARTIFACTORY, APP_DYNAMICS and AZURE.

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
api_instance = harness_python_sdk.OrgConnectorApi(harness_python_sdk.ApiClient(configuration))
org = 'org_example' # str | Identifier field of the organization the resource is scoped to
connector = 'connector_example' # str | Connector identifier
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)

try:
    # Delete a connector
    api_instance.delete_org_scoped_connector(org, connector, harness_account=harness_account)
except ApiException as e:
    print("Exception when calling OrgConnectorApi->delete_org_scoped_connector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| Identifier field of the organization the resource is scoped to | 
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

# **get_org_scoped_connector**
> ConnectorResponse get_org_scoped_connector(org, connector, harness_account=harness_account)

Retrieve a connector

Retrieves the information of the connector with the matching connector identifier. Connector types supported are GIT, ARTIFACTORY, APP_DYNAMICS and AZURE. 

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
api_instance = harness_python_sdk.OrgConnectorApi(harness_python_sdk.ApiClient(configuration))
org = 'org_example' # str | Identifier field of the organization the resource is scoped to
connector = 'connector_example' # str | Connector identifier
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)

try:
    # Retrieve a connector
    api_response = api_instance.get_org_scoped_connector(org, connector, harness_account=harness_account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgConnectorApi->get_org_scoped_connector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| Identifier field of the organization the resource is scoped to | 
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

# **test_org_scoped_connector**
> ConnectorTestConnectionResponse test_org_scoped_connector(org, connector, harness_account=harness_account)

Test a connector

Tests connection of the connector with the matching connector identifier. 

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
api_instance = harness_python_sdk.OrgConnectorApi(harness_python_sdk.ApiClient(configuration))
org = 'org_example' # str | Identifier field of the organization the resource is scoped to
connector = 'connector_example' # str | Connector identifier
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)

try:
    # Test a connector
    api_response = api_instance.test_org_scoped_connector(org, connector, harness_account=harness_account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgConnectorApi->test_org_scoped_connector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| Identifier field of the organization the resource is scoped to | 
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

# **update_org_scoped_connector**
> ConnectorResponse update_org_scoped_connector(body, org, connector, harness_account=harness_account)

Update a connector

Updates the information of the secret with the matching secret identifier.

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
api_instance = harness_python_sdk.OrgConnectorApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.ConnectorRequest() # ConnectorRequest | 
org = 'org_example' # str | Identifier field of the organization the resource is scoped to
connector = 'connector_example' # str | Connector identifier
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)

try:
    # Update a connector
    api_response = api_instance.update_org_scoped_connector(body, org, connector, harness_account=harness_account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgConnectorApi->update_org_scoped_connector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConnectorRequest**](ConnectorRequest.md)|  | 
 **org** | **str**| Identifier field of the organization the resource is scoped to | 
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

