# swagger_client.DelegateSetupResourceApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_delegate**](DelegateSetupResourceApi.md#delete_delegate) | **DELETE** /ng/api/delegate-setup/delegate/{delegateIdentifier} | Deletes a Delegate by its identifier.
[**generate_ng_helm_values_yaml**](DelegateSetupResourceApi.md#generate_ng_helm_values_yaml) | **POST** /ng/api/delegate-setup/generate-helm-values | Generates helm values yaml file from the data specified in request body (Delegate setup details).
[**generate_terraform_module**](DelegateSetupResourceApi.md#generate_terraform_module) | **GET** /ng/api/delegate-setup/delegate-terraform-module-file | Generates delegate terraform example module file from the account
[**list_delegates**](DelegateSetupResourceApi.md#list_delegates) | **POST** /ng/api/delegate-setup/listDelegates | Lists all delegates in NG filtered by provided conditions
[**override_delegate_image_tag**](DelegateSetupResourceApi.md#override_delegate_image_tag) | **PUT** /ng/api/delegate-setup/override-delegate-tag | Overrides delegate image tag for account
[**published_delegate_version**](DelegateSetupResourceApi.md#published_delegate_version) | **GET** /ng/api/delegate-setup/latest-supported-version | Gets the latest supported delegate version. The version has YY.MM.XXXXX format. You can use any version lower than the returned results(upto 3 months old)

# **delete_delegate**
> RestResponseDelegateDeleteResponse delete_delegate(account_identifier, delegate_identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Deletes a Delegate by its identifier.

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
api_instance = swagger_client.DelegateSetupResourceApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
delegate_identifier = 'delegate_identifier_example' # str | Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Deletes a Delegate by its identifier.
    api_response = api_instance.delete_delegate(account_identifier, delegate_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DelegateSetupResourceApi->delete_delegate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **delegate_identifier** | **str**| Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**RestResponseDelegateDeleteResponse**](RestResponseDelegateDeleteResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_ng_helm_values_yaml**
> generate_ng_helm_values_yaml(body, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Generates helm values yaml file from the data specified in request body (Delegate setup details).

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
api_instance = swagger_client.DelegateSetupResourceApi(swagger_client.ApiClient(configuration))
body = swagger_client.DelegateSetupDetails() # DelegateSetupDetails | Delegate setup details, containing data to populate yaml file values.
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Generates helm values yaml file from the data specified in request body (Delegate setup details).
    api_instance.generate_ng_helm_values_yaml(body, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
except ApiException as e:
    print("Exception when calling DelegateSetupResourceApi->generate_ng_helm_values_yaml: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DelegateSetupDetails**](DelegateSetupDetails.md)| Delegate setup details, containing data to populate yaml file values. | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_terraform_module**
> generate_terraform_module(account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Generates delegate terraform example module file from the account

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
api_instance = swagger_client.DelegateSetupResourceApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Generates delegate terraform example module file from the account
    api_instance.generate_terraform_module(account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
except ApiException as e:
    print("Exception when calling DelegateSetupResourceApi->generate_terraform_module: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_delegates**
> RestResponseListDelegateListResponse list_delegates(account_identifier, body=body, org_identifier=org_identifier, project_identifier=project_identifier)

Lists all delegates in NG filtered by provided conditions

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
api_instance = swagger_client.DelegateSetupResourceApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
body = swagger_client.DelegateFilterPropertiesDTO() # DelegateFilterPropertiesDTO | Details of the Delegate filter properties to be applied (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Lists all delegates in NG filtered by provided conditions
    api_response = api_instance.list_delegates(account_identifier, body=body, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DelegateSetupResourceApi->list_delegates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **body** | [**DelegateFilterPropertiesDTO**](DelegateFilterPropertiesDTO.md)| Details of the Delegate filter properties to be applied | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**RestResponseListDelegateListResponse**](RestResponseListDelegateListResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **override_delegate_image_tag**
> RestResponseString override_delegate_image_tag(account_identifier, delegate_tag, valid_till_next_release=valid_till_next_release, valid_for_days=valid_for_days)

Overrides delegate image tag for account

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
api_instance = swagger_client.DelegateSetupResourceApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | 
delegate_tag = 'delegate_tag_example' # str | 
valid_till_next_release = false # bool |  (optional) (default to false)
valid_for_days = 30 # int |  (optional) (default to 30)

try:
    # Overrides delegate image tag for account
    api_response = api_instance.override_delegate_image_tag(account_identifier, delegate_tag, valid_till_next_release=valid_till_next_release, valid_for_days=valid_for_days)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DelegateSetupResourceApi->override_delegate_image_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**|  | 
 **delegate_tag** | **str**|  | 
 **valid_till_next_release** | **bool**|  | [optional] [default to false]
 **valid_for_days** | **int**|  | [optional] [default to 30]

### Return type

[**RestResponseString**](RestResponseString.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **published_delegate_version**
> RestResponseSupportedDelegateVersion published_delegate_version(account_identifier)

Gets the latest supported delegate version. The version has YY.MM.XXXXX format. You can use any version lower than the returned results(upto 3 months old)

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
api_instance = swagger_client.DelegateSetupResourceApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Gets the latest supported delegate version. The version has YY.MM.XXXXX format. You can use any version lower than the returned results(upto 3 months old)
    api_response = api_instance.published_delegate_version(account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DelegateSetupResourceApi->published_delegate_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**RestResponseSupportedDelegateVersion**](RestResponseSupportedDelegateVersion.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

