# swagger_client.ServiceOverridesApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_service_override**](ServiceOverridesApi.md#create_service_override) | **POST** /ng/api/serviceOverrides | Create an ServiceOverride Entity
[**delete_service_override1**](ServiceOverridesApi.md#delete_service_override1) | **DELETE** /ng/api/serviceOverrides/{identifier} | Delete a ServiceOverride entity
[**get_service_overrides**](ServiceOverridesApi.md#get_service_overrides) | **GET** /ng/api/serviceOverrides/{identifier} | Gets Service Overrides by Identifier
[**update_service_override**](ServiceOverridesApi.md#update_service_override) | **PUT** /ng/api/serviceOverrides | Update an ServiceOverride Entity

# **create_service_override**
> ResponseDTOServiceOverrideResponseV2 create_service_override(body, account_identifier)

Create an ServiceOverride Entity

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
api_instance = swagger_client.ServiceOverridesApi(swagger_client.ApiClient(configuration))
body = swagger_client.ServiceOverrideRequestV2() # ServiceOverrideRequestV2 | Details of the Service Override to be updated
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Create an ServiceOverride Entity
    api_response = api_instance.create_service_override(body, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOverridesApi->create_service_override: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ServiceOverrideRequestV2**](ServiceOverrideRequestV2.md)| Details of the Service Override to be updated | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**ResponseDTOServiceOverrideResponseV2**](ResponseDTOServiceOverrideResponseV2.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_service_override1**
> ResponseDTOBoolean delete_service_override1(identifier, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Delete a ServiceOverride entity

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
api_instance = swagger_client.ServiceOverridesApi(swagger_client.ApiClient(configuration))
identifier = 'identifier_example' # str | Service Overrides Identifier for Entity.
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Delete a ServiceOverride entity
    api_response = api_instance.delete_service_override1(identifier, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOverridesApi->delete_service_override1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Service Overrides Identifier for Entity. | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOBoolean**](ResponseDTOBoolean.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_overrides**
> ResponseDTOServiceOverrideResponseV2 get_service_overrides(identifier, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Gets Service Overrides by Identifier

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
api_instance = swagger_client.ServiceOverridesApi(swagger_client.ApiClient(configuration))
identifier = 'identifier_example' # str | Service Overrides Identifier for Entity.
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Gets Service Overrides by Identifier
    api_response = api_instance.get_service_overrides(identifier, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOverridesApi->get_service_overrides: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Service Overrides Identifier for Entity. | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOServiceOverrideResponseV2**](ResponseDTOServiceOverrideResponseV2.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_service_override**
> ResponseDTOServiceOverrideResponseV2 update_service_override(body, account_identifier)

Update an ServiceOverride Entity

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
api_instance = swagger_client.ServiceOverridesApi(swagger_client.ApiClient(configuration))
body = swagger_client.ServiceOverrideRequestV2() # ServiceOverrideRequestV2 | Details of the Service Override to be updated
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Update an ServiceOverride Entity
    api_response = api_instance.update_service_override(body, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOverridesApi->update_service_override: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ServiceOverrideRequestV2**](ServiceOverrideRequestV2.md)| Details of the Service Override to be updated | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**ResponseDTOServiceOverrideResponseV2**](ResponseDTOServiceOverrideResponseV2.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

