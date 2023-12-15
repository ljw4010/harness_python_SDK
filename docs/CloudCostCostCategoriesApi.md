# harness_python_sdk.CloudCostCostCategoriesApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_business_mapping**](CloudCostCostCategoriesApi.md#create_business_mapping) | **POST** /ccm/api/business-mapping | Create Cost category
[**delete_business_mapping**](CloudCostCostCategoriesApi.md#delete_business_mapping) | **DELETE** /ccm/api/business-mapping/{id} | Delete a Cost category
[**get_business_mapping**](CloudCostCostCategoriesApi.md#get_business_mapping) | **GET** /ccm/api/business-mapping/{id} | Fetch details of a Cost category
[**get_business_mapping_list**](CloudCostCostCategoriesApi.md#get_business_mapping_list) | **GET** /ccm/api/business-mapping | Return details of all the Cost categories
[**update_business_mapping**](CloudCostCostCategoriesApi.md#update_business_mapping) | **PUT** /ccm/api/business-mapping | Update a Cost category

# **create_business_mapping**
> RestResponseBusinessMapping create_business_mapping(body=body, account_identifier=account_identifier)

Create Cost category

Create Cost category that allows you to categorize based on business requirements and get a contextual view of your expenses

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
api_instance = harness_python_sdk.CloudCostCostCategoriesApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.BusinessMapping() # BusinessMapping |  (optional)
account_identifier = 'account_identifier_example' # str |  (optional)

try:
    # Create Cost category
    api_response = api_instance.create_business_mapping(body=body, account_identifier=account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostCostCategoriesApi->create_business_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BusinessMapping**](BusinessMapping.md)|  | [optional] 
 **account_identifier** | **str**|  | [optional] 

### Return type

[**RestResponseBusinessMapping**](RestResponseBusinessMapping.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_business_mapping**
> RestResponseCostCategoryDeleteDTO delete_business_mapping(account_identifier, id)

Delete a Cost category

Delete a Cost category for the given Cost category ID.

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
api_instance = harness_python_sdk.CloudCostCostCategoriesApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | 
id = 'id_example' # str | 

try:
    # Delete a Cost category
    api_response = api_instance.delete_business_mapping(account_identifier, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostCostCategoriesApi->delete_business_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**RestResponseCostCategoryDeleteDTO**](RestResponseCostCategoryDeleteDTO.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_business_mapping**
> RestResponseBusinessMapping get_business_mapping(id, account_identifier=account_identifier)

Fetch details of a Cost category

Fetch details of a Cost category for the given Cost category ID.

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
api_instance = harness_python_sdk.CloudCostCostCategoriesApi(harness_python_sdk.ApiClient(configuration))
id = 'id_example' # str | 
account_identifier = 'account_identifier_example' # str |  (optional)

try:
    # Fetch details of a Cost category
    api_response = api_instance.get_business_mapping(id, account_identifier=account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostCostCategoriesApi->get_business_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **account_identifier** | **str**|  | [optional] 

### Return type

[**RestResponseBusinessMapping**](RestResponseBusinessMapping.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_business_mapping_list**
> RestResponseBusinessMappingListDTO get_business_mapping_list(account_identifier=account_identifier, search_key=search_key, sort_type=sort_type, sort_order=sort_order, limit=limit, offset=offset)

Return details of all the Cost categories

Return details of all the Cost categories for the given account ID.

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
api_instance = harness_python_sdk.CloudCostCostCategoriesApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str |  (optional)
search_key = 'search_key_example' # str |  (optional)
sort_type = 'sort_type_example' # str |  (optional)
sort_order = 'sort_order_example' # str |  (optional)
limit = 56 # int |  (optional)
offset = 56 # int |  (optional)

try:
    # Return details of all the Cost categories
    api_response = api_instance.get_business_mapping_list(account_identifier=account_identifier, search_key=search_key, sort_type=sort_type, sort_order=sort_order, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostCostCategoriesApi->get_business_mapping_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**|  | [optional] 
 **search_key** | **str**|  | [optional] 
 **sort_type** | **str**|  | [optional] 
 **sort_order** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 

### Return type

[**RestResponseBusinessMappingListDTO**](RestResponseBusinessMappingListDTO.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_business_mapping**
> RestResponseString update_business_mapping(body=body, account_identifier=account_identifier)

Update a Cost category

Update a Cost category. It accepts a BusinessMapping object and upserts it using the uuid mentioned in the definition.

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
api_instance = harness_python_sdk.CloudCostCostCategoriesApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.BusinessMapping() # BusinessMapping |  (optional)
account_identifier = 'account_identifier_example' # str |  (optional)

try:
    # Update a Cost category
    api_response = api_instance.update_business_mapping(body=body, account_identifier=account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostCostCategoriesApi->update_business_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BusinessMapping**](BusinessMapping.md)|  | [optional] 
 **account_identifier** | **str**|  | [optional] 

### Return type

[**RestResponseString**](RestResponseString.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

