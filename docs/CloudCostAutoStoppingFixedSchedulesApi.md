# swagger_client.CloudCostAutoStoppingFixedSchedulesApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_auto_stopping_schedules**](CloudCostAutoStoppingFixedSchedulesApi.md#create_auto_stopping_schedules) | **POST** /gateway/lw/api/accounts/{account_id}/schedules | Create a fixed schedule for an AutoStopping Rule
[**delete_auto_stopping_schedule**](CloudCostAutoStoppingFixedSchedulesApi.md#delete_auto_stopping_schedule) | **DELETE** /gateway/lw/api/accounts/{account_id}/schedules/{schedule_id} | Delete a fixed schedule for AutoStopping Rule.
[**list_auto_stopping_schedules**](CloudCostAutoStoppingFixedSchedulesApi.md#list_auto_stopping_schedules) | **GET** /gateway/lw/api/accounts/{account_id}/schedules | Return all the AutoStopping Rule fixed schedules

# **create_auto_stopping_schedules**
> FixedSchedule create_auto_stopping_schedules(body, cloud_account_id, account_identifier, account_id)

Create a fixed schedule for an AutoStopping Rule

Creates an AutoStopping rule to run resources based on the schedule.

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
api_instance = swagger_client.CloudCostAutoStoppingFixedSchedulesApi(swagger_client.ApiClient(configuration))
body = swagger_client.SaveStaticSchedulesRequest() # SaveStaticSchedulesRequest | Fixed schedule payload
cloud_account_id = 'cloud_account_id_example' # str | Connector ID
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity
account_id = 'account_id_example' # str | Account Identifier for the Entity

try:
    # Create a fixed schedule for an AutoStopping Rule
    api_response = api_instance.create_auto_stopping_schedules(body, cloud_account_id, account_identifier, account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostAutoStoppingFixedSchedulesApi->create_auto_stopping_schedules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SaveStaticSchedulesRequest**](SaveStaticSchedulesRequest.md)| Fixed schedule payload | 
 **cloud_account_id** | **str**| Connector ID | 
 **account_identifier** | **str**| Account Identifier for the Entity | 
 **account_id** | **str**| Account Identifier for the Entity | 

### Return type

[**FixedSchedule**](FixedSchedule.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_auto_stopping_schedule**
> InlineResponse2002 delete_auto_stopping_schedule(account_id, schedule_id, account_identifier)

Delete a fixed schedule for AutoStopping Rule.

Deletes a fixed schedule for the given AutoStopping Rule.

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
api_instance = swagger_client.CloudCostAutoStoppingFixedSchedulesApi(swagger_client.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier for the Entity
schedule_id = 1.2 # float | ID of a fixed schedule added to an AutoStopping rule
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity

try:
    # Delete a fixed schedule for AutoStopping Rule.
    api_response = api_instance.delete_auto_stopping_schedule(account_id, schedule_id, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostAutoStoppingFixedSchedulesApi->delete_auto_stopping_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier for the Entity | 
 **schedule_id** | **float**| ID of a fixed schedule added to an AutoStopping rule | 
 **account_identifier** | **str**| Account Identifier for the Entity | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_auto_stopping_schedules**
> FixedSchedulesListResponse list_auto_stopping_schedules(account_id, cloud_account_id, account_identifier, res_id, res_type)

Return all the AutoStopping Rule fixed schedules

Returns all the AutoStopping Rule fixed schedules for the given identifier.

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
api_instance = swagger_client.CloudCostAutoStoppingFixedSchedulesApi(swagger_client.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier for the Entity
cloud_account_id = 'cloud_account_id_example' # str | Connector ID
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity
res_id = 'res_id_example' # str | IDs of resources whose fixed schedules are to be fetched. This can be an AutoStopping rule ID if the res_type is \"autostop_rule\"
res_type = 'res_type_example' # str | Type of resource to which schedules are attached

try:
    # Return all the AutoStopping Rule fixed schedules
    api_response = api_instance.list_auto_stopping_schedules(account_id, cloud_account_id, account_identifier, res_id, res_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostAutoStoppingFixedSchedulesApi->list_auto_stopping_schedules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier for the Entity | 
 **cloud_account_id** | **str**| Connector ID | 
 **account_identifier** | **str**| Account Identifier for the Entity | 
 **res_id** | **str**| IDs of resources whose fixed schedules are to be fetched. This can be an AutoStopping rule ID if the res_type is \&quot;autostop_rule\&quot; | 
 **res_type** | **str**| Type of resource to which schedules are attached | 

### Return type

[**FixedSchedulesListResponse**](FixedSchedulesListResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

