# swagger_client.CloudCostPerspectivesApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_perspective**](CloudCostPerspectivesApi.md#create_perspective) | **POST** /ccm/api/perspective | Create a Perspective
[**delete_perspective**](CloudCostPerspectivesApi.md#delete_perspective) | **DELETE** /ccm/api/perspective | Delete a Perspective
[**get_all_perspectives**](CloudCostPerspectivesApi.md#get_all_perspectives) | **GET** /ccm/api/perspective/getAllPerspectives | Return details of all the Perspectives
[**get_last_period_cost1**](CloudCostPerspectivesApi.md#get_last_period_cost1) | **GET** /ccm/api/perspective/lastPeriodCost | Get the last period cost for a Perspective
[**get_last_year_monthly_cost**](CloudCostPerspectivesApi.md#get_last_year_monthly_cost) | **GET** /ccm/api/perspective/lastYearMonthlyCost | Get the last twelve month cost for a Perspective
[**get_perspective**](CloudCostPerspectivesApi.md#get_perspective) | **GET** /ccm/api/perspective | Fetch details of a Perspective
[**update_perspective**](CloudCostPerspectivesApi.md#update_perspective) | **PUT** /ccm/api/perspective | Update a Perspective

# **create_perspective**
> ResponseDTOCEView create_perspective(body, account_identifier, clone)

Create a Perspective

Create a Perspective. You can set the clone parameter as true to clone a Perspective.

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
api_instance = swagger_client.CloudCostPerspectivesApi(swagger_client.ApiClient(configuration))
body = swagger_client.CEView() # CEView | Request body containing Perspective's CEView object
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
clone = true # bool | Set the clone parameter as true to clone a Perspective.

try:
    # Create a Perspective
    api_response = api_instance.create_perspective(body, account_identifier, clone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostPerspectivesApi->create_perspective: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CEView**](CEView.md)| Request body containing Perspective&#x27;s CEView object | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **clone** | **bool**| Set the clone parameter as true to clone a Perspective. | 

### Return type

[**ResponseDTOCEView**](ResponseDTOCEView.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_perspective**
> ResponseDTOString delete_perspective(account_identifier, perspective_id)

Delete a Perspective

Delete a Perspective for the given Perspective ID.

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
api_instance = swagger_client.CloudCostPerspectivesApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
perspective_id = 'perspective_id_example' # str | Unique identifier for the Perspective

try:
    # Delete a Perspective
    api_response = api_instance.delete_perspective(account_identifier, perspective_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostPerspectivesApi->delete_perspective: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **perspective_id** | **str**| Unique identifier for the Perspective | 

### Return type

[**ResponseDTOString**](ResponseDTOString.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_perspectives**
> ResponseDTOPerspectiveData get_all_perspectives(account_identifier, page_size, page_no, search_key=search_key, sort_type=sort_type, sort_order=sort_order, cloud_filters=cloud_filters)

Return details of all the Perspectives

Return details of all the Perspectives for the given account ID.

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
api_instance = swagger_client.CloudCostPerspectivesApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
page_size = 20 # int | Number of perspectives to be shown (default to 20)
page_no = 0 # int | Number of records to be skipped (default to 0)
search_key = 'search_key_example' # str | Characters in search bar (optional)
sort_type = 'TIME' # str |  sorting filters in UI (optional) (default to TIME)
sort_order = 'DESCENDING' # str | sorting order (optional) (default to DESCENDING)
cloud_filters = ['cloud_filters_example'] # list[str] | filters for clouds and clusters (optional)

try:
    # Return details of all the Perspectives
    api_response = api_instance.get_all_perspectives(account_identifier, page_size, page_no, search_key=search_key, sort_type=sort_type, sort_order=sort_order, cloud_filters=cloud_filters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostPerspectivesApi->get_all_perspectives: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **page_size** | **int**| Number of perspectives to be shown | [default to 20]
 **page_no** | **int**| Number of records to be skipped | [default to 0]
 **search_key** | **str**| Characters in search bar | [optional] 
 **sort_type** | **str**|  sorting filters in UI | [optional] [default to TIME]
 **sort_order** | **str**| sorting order | [optional] [default to DESCENDING]
 **cloud_filters** | [**list[str]**](str.md)| filters for clouds and clusters | [optional] 

### Return type

[**ResponseDTOPerspectiveData**](ResponseDTOPerspectiveData.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_last_period_cost1**
> ResponseDTODouble get_last_period_cost1(account_identifier, perspective_id, start_time, period)

Get the last period cost for a Perspective

Get last period cost for a Perspective

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
api_instance = swagger_client.CloudCostPerspectivesApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
perspective_id = 'perspective_id_example' # str | The Perspective identifier for which we want the cost
start_time = 789 # int | The Start time (timestamp in millis) for the current period
period = 'period_example' # str | The period (DAILY, WEEKLY, MONTHLY, QUARTERLY, YEARLY) for which we want the cost

try:
    # Get the last period cost for a Perspective
    api_response = api_instance.get_last_period_cost1(account_identifier, perspective_id, start_time, period)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostPerspectivesApi->get_last_period_cost1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **perspective_id** | **str**| The Perspective identifier for which we want the cost | 
 **start_time** | **int**| The Start time (timestamp in millis) for the current period | 
 **period** | **str**| The period (DAILY, WEEKLY, MONTHLY, QUARTERLY, YEARLY) for which we want the cost | 

### Return type

[**ResponseDTODouble**](ResponseDTODouble.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_last_year_monthly_cost**
> ResponseDTOListValueDataPoint get_last_year_monthly_cost(account_identifier, perspective_id, start_time, period, type, breakdown)

Get the last twelve month cost for a Perspective

Get last twelve month cost for a Perspective

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
api_instance = swagger_client.CloudCostPerspectivesApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
perspective_id = 'perspective_id_example' # str | The Perspective identifier for which we want the cost
start_time = 789 # int | The Start time (timestamp in millis) for the current period
period = 'period_example' # str | Only support for YEARLY budget period
type = 'type_example' # str | Only support for PREVIOUS_PERIOD_SPEND budget type
breakdown = 'breakdown_example' # str | Only support for MONTHLY breakdown

try:
    # Get the last twelve month cost for a Perspective
    api_response = api_instance.get_last_year_monthly_cost(account_identifier, perspective_id, start_time, period, type, breakdown)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostPerspectivesApi->get_last_year_monthly_cost: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **perspective_id** | **str**| The Perspective identifier for which we want the cost | 
 **start_time** | **int**| The Start time (timestamp in millis) for the current period | 
 **period** | **str**| Only support for YEARLY budget period | 
 **type** | **str**| Only support for PREVIOUS_PERIOD_SPEND budget type | 
 **breakdown** | **str**| Only support for MONTHLY breakdown | 

### Return type

[**ResponseDTOListValueDataPoint**](ResponseDTOListValueDataPoint.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_perspective**
> ResponseDTOCEView get_perspective(account_identifier, perspective_id)

Fetch details of a Perspective

Fetch details of a Perspective for the given Perspective ID.

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
api_instance = swagger_client.CloudCostPerspectivesApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
perspective_id = 'perspective_id_example' # str | Unique identifier for the Perspective

try:
    # Fetch details of a Perspective
    api_response = api_instance.get_perspective(account_identifier, perspective_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostPerspectivesApi->get_perspective: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **perspective_id** | **str**| Unique identifier for the Perspective | 

### Return type

[**ResponseDTOCEView**](ResponseDTOCEView.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_perspective**
> ResponseDTOCEView update_perspective(body, account_identifier)

Update a Perspective

Update a Perspective. It accepts a CEView object and upserts it using the uuid mentioned in the definition.

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
api_instance = swagger_client.CloudCostPerspectivesApi(swagger_client.ApiClient(configuration))
body = swagger_client.CEView() # CEView | Perspective's CEView object
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Update a Perspective
    api_response = api_instance.update_perspective(body, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostPerspectivesApi->update_perspective: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CEView**](CEView.md)| Perspective&#x27;s CEView object | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**ResponseDTOCEView**](ResponseDTOCEView.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

