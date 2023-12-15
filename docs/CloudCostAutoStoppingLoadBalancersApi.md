# harness_python_sdk.CloudCostAutoStoppingLoadBalancersApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**access_point_rules**](CloudCostAutoStoppingLoadBalancersApi.md#access_point_rules) | **GET** /gateway/lw/api/accounts/{account_id}/autostopping/loadbalancers/{lb_id}/rules | Return all the AutoStopping Rules in a load balancer
[**create_load_balancer**](CloudCostAutoStoppingLoadBalancersApi.md#create_load_balancer) | **POST** /gateway/lw/api/accounts/{account_id}/autostopping/loadbalancers | Create a load balancer
[**delete_load_balancer**](CloudCostAutoStoppingLoadBalancersApi.md#delete_load_balancer) | **DELETE** /gateway/lw/api/accounts/{account_id}/autostopping/loadbalancers | Delete load balancers and the associated resources
[**describe_load_balancer**](CloudCostAutoStoppingLoadBalancersApi.md#describe_load_balancer) | **GET** /gateway/lw/api/accounts/{account_id}/autostopping/loadbalancers/{lb_id} | Return details of a load balancer
[**edit_load_balancer**](CloudCostAutoStoppingLoadBalancersApi.md#edit_load_balancer) | **PUT** /gateway/lw/api/accounts/{account_id}/autostopping/loadbalancers | Update a load balancer
[**list_load_balancers**](CloudCostAutoStoppingLoadBalancersApi.md#list_load_balancers) | **GET** /gateway/lw/api/accounts/{account_id}/autostopping/loadbalancers | Return all the load balancers
[**load_balancer_activity**](CloudCostAutoStoppingLoadBalancersApi.md#load_balancer_activity) | **GET** /gateway/lw/api/accounts/{account_id}/autostopping/loadbalancers/{lb_id}/last_active_at | Return last activity details of a load balancer

# **access_point_rules**
> ServicesResponse access_point_rules(account_id, lb_id, account_identifier)

Return all the AutoStopping Rules in a load balancer

Returns all the AutoStopping Rules for the given load balancer identifier.

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
api_instance = harness_python_sdk.CloudCostAutoStoppingLoadBalancersApi(harness_python_sdk.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier for the Entity
lb_id = 'lb_id_example' # str | ID of the load balancer for which you want to fetch the list of AutoStopping Rules
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity

try:
    # Return all the AutoStopping Rules in a load balancer
    api_response = api_instance.access_point_rules(account_id, lb_id, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostAutoStoppingLoadBalancersApi->access_point_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier for the Entity | 
 **lb_id** | **str**| ID of the load balancer for which you want to fetch the list of AutoStopping Rules | 
 **account_identifier** | **str**| Account Identifier for the Entity | 

### Return type

[**ServicesResponse**](ServicesResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_load_balancer**
> CreateAccessPointResponse create_load_balancer(body, account_identifier, account_id)

Create a load balancer

Creates a load balancer.

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
api_instance = harness_python_sdk.CloudCostAutoStoppingLoadBalancersApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.AccessPoint() # AccessPoint | 
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity
account_id = 'account_id_example' # str | Account Identifier for the Entity

try:
    # Create a load balancer
    api_response = api_instance.create_load_balancer(body, account_identifier, account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostAutoStoppingLoadBalancersApi->create_load_balancer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccessPoint**](AccessPoint.md)|  | 
 **account_identifier** | **str**| Account Identifier for the Entity | 
 **account_id** | **str**| Account Identifier for the Entity | 

### Return type

[**CreateAccessPointResponse**](CreateAccessPointResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_load_balancer**
> delete_load_balancer(body, account_identifier, account_id)

Delete load balancers and the associated resources

Deletes load balancers and the associated resources for the given identifier.

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
api_instance = harness_python_sdk.CloudCostAutoStoppingLoadBalancersApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.DeleteAccessPointPayload() # DeleteAccessPointPayload | 
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity
account_id = 'account_id_example' # str | Account Identifier for the Entity

try:
    # Delete load balancers and the associated resources
    api_instance.delete_load_balancer(body, account_identifier, account_id)
except ApiException as e:
    print("Exception when calling CloudCostAutoStoppingLoadBalancersApi->delete_load_balancer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeleteAccessPointPayload**](DeleteAccessPointPayload.md)|  | 
 **account_identifier** | **str**| Account Identifier for the Entity | 
 **account_id** | **str**| Account Identifier for the Entity | 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **describe_load_balancer**
> GetAccessPointResponse describe_load_balancer(account_id, lb_id, account_identifier)

Return details of a load balancer

Retuns details of a load balancer for the given identifier.

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
api_instance = harness_python_sdk.CloudCostAutoStoppingLoadBalancersApi(harness_python_sdk.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier for the Entity
lb_id = 'lb_id_example' # str | ID of the load balancer for which you want to fetch the details
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity

try:
    # Return details of a load balancer
    api_response = api_instance.describe_load_balancer(account_id, lb_id, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostAutoStoppingLoadBalancersApi->describe_load_balancer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier for the Entity | 
 **lb_id** | **str**| ID of the load balancer for which you want to fetch the details | 
 **account_identifier** | **str**| Account Identifier for the Entity | 

### Return type

[**GetAccessPointResponse**](GetAccessPointResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_load_balancer**
> CreateAccessPointResponse edit_load_balancer(body, account_identifier, account_id)

Update a load balancer

Updates a load balancer for the given identifier.

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
api_instance = harness_python_sdk.CloudCostAutoStoppingLoadBalancersApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.AccessPoint() # AccessPoint | 
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity
account_id = 'account_id_example' # str | Account Identifier for the Entity

try:
    # Update a load balancer
    api_response = api_instance.edit_load_balancer(body, account_identifier, account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostAutoStoppingLoadBalancersApi->edit_load_balancer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccessPoint**](AccessPoint.md)|  | 
 **account_identifier** | **str**| Account Identifier for the Entity | 
 **account_id** | **str**| Account Identifier for the Entity | 

### Return type

[**CreateAccessPointResponse**](CreateAccessPointResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_load_balancers**
> ListAccessPointResponse list_load_balancers(account_id, cloud_account_id, account_identifier, vpc=vpc, region=region)

Return all the load balancers

Returns all the load balancers for the given identifier.

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
api_instance = harness_python_sdk.CloudCostAutoStoppingLoadBalancersApi(harness_python_sdk.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier for the Entity
cloud_account_id = 'cloud_account_id_example' # str | Connector ID
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity
vpc = 'vpc_example' # str | Virtual Private Cloud (VPC) (optional)
region = 'region_example' # str | Cloud region where access point is installed (optional)

try:
    # Return all the load balancers
    api_response = api_instance.list_load_balancers(account_id, cloud_account_id, account_identifier, vpc=vpc, region=region)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostAutoStoppingLoadBalancersApi->list_load_balancers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier for the Entity | 
 **cloud_account_id** | **str**| Connector ID | 
 **account_identifier** | **str**| Account Identifier for the Entity | 
 **vpc** | **str**| Virtual Private Cloud (VPC) | [optional] 
 **region** | **str**| Cloud region where access point is installed | [optional] 

### Return type

[**ListAccessPointResponse**](ListAccessPointResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_balancer_activity**
> AccessPointActivityResponse load_balancer_activity(account_id, lb_id, account_identifier)

Return last activity details of a load balancer

Returns the last activity details for the given load balancer identifier.

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
api_instance = harness_python_sdk.CloudCostAutoStoppingLoadBalancersApi(harness_python_sdk.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Identifier for the Entity
lb_id = 'lb_id_example' # str | ID of the load balancer for which you want to fetch the most recent activity details
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity

try:
    # Return last activity details of a load balancer
    api_response = api_instance.load_balancer_activity(account_id, lb_id, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostAutoStoppingLoadBalancersApi->load_balancer_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Identifier for the Entity | 
 **lb_id** | **str**| ID of the load balancer for which you want to fetch the most recent activity details | 
 **account_identifier** | **str**| Account Identifier for the Entity | 

### Return type

[**AccessPointActivityResponse**](AccessPointActivityResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

