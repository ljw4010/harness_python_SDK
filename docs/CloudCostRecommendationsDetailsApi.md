# harness_python_sdk.CloudCostRecommendationsDetailsApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**azure_vm_recommendation_detail**](CloudCostRecommendationsDetailsApi.md#azure_vm_recommendation_detail) | **GET** /ccm/api/recommendation/details/azure-vm | Return Azure VM Recommendation
[**ec2_recommendation_detail**](CloudCostRecommendationsDetailsApi.md#ec2_recommendation_detail) | **GET** /ccm/api/recommendation/details/ec2-instance | Return EC2 Recommendation
[**ecs_recommendation_detail**](CloudCostRecommendationsDetailsApi.md#ecs_recommendation_detail) | **GET** /ccm/api/recommendation/details/ecs-service | Return ECS Recommendation
[**node_recommendation_detail**](CloudCostRecommendationsDetailsApi.md#node_recommendation_detail) | **GET** /ccm/api/recommendation/details/node-pool | Return node pool Recommendation
[**workload_recommendation_detail**](CloudCostRecommendationsDetailsApi.md#workload_recommendation_detail) | **GET** /ccm/api/recommendation/details/workload | Return workload Recommendation

# **azure_vm_recommendation_detail**
> ResponseDTOAzureVmRecommendation azure_vm_recommendation_detail(account_identifier, id)

Return Azure VM Recommendation

Returns Azure VM Recommendation details for the given Recommendation identifier.

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
api_instance = harness_python_sdk.CloudCostRecommendationsDetailsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
id = 'id_example' # str | Azure VM Recommendation identifier.

try:
    # Return Azure VM Recommendation
    api_response = api_instance.azure_vm_recommendation_detail(account_identifier, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostRecommendationsDetailsApi->azure_vm_recommendation_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **id** | **str**| Azure VM Recommendation identifier. | 

### Return type

[**ResponseDTOAzureVmRecommendation**](ResponseDTOAzureVmRecommendation.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ec2_recommendation_detail**
> ResponseDTOEC2InstanceRecommendation ec2_recommendation_detail(account_identifier, id)

Return EC2 Recommendation

Returns EC2 Recommendation details for the given Recommendation identifier.

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
api_instance = harness_python_sdk.CloudCostRecommendationsDetailsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
id = 'id_example' # str | EC2 Recommendation identifier.

try:
    # Return EC2 Recommendation
    api_response = api_instance.ec2_recommendation_detail(account_identifier, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostRecommendationsDetailsApi->ec2_recommendation_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **id** | **str**| EC2 Recommendation identifier. | 

### Return type

[**ResponseDTOEC2InstanceRecommendation**](ResponseDTOEC2InstanceRecommendation.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ecs_recommendation_detail**
> ResponseDTOECSRecommendationDTO ecs_recommendation_detail(account_identifier, id, _from=_from, to=to, buffer_percentage=buffer_percentage)

Return ECS Recommendation

Returns ECS Recommendation details for the given Recommendation identifier.

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
api_instance = harness_python_sdk.CloudCostRecommendationsDetailsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
id = 'id_example' # str | ECS Recommendation identifier.
_from = '_from_example' # str | Should use org.joda.time.DateTime parsable format. Example, '2022-01-31', '2022-01-31T07:54Z' or '2022-01-31T07:54:51.264Z' Defaults to Today-7days (optional)
to = 'to_example' # str | Should use org.joda.time.DateTime parsable format. Example, '2022-01-31', '2022-01-31T07:54Z' or '2022-01-31T07:54:51.264Z' Defaults to Today (optional)
buffer_percentage = 789 # int | Buffer Percentage defaults to zero (optional)

try:
    # Return ECS Recommendation
    api_response = api_instance.ecs_recommendation_detail(account_identifier, id, _from=_from, to=to, buffer_percentage=buffer_percentage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostRecommendationsDetailsApi->ecs_recommendation_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **id** | **str**| ECS Recommendation identifier. | 
 **_from** | **str**| Should use org.joda.time.DateTime parsable format. Example, &#x27;2022-01-31&#x27;, &#x27;2022-01-31T07:54Z&#x27; or &#x27;2022-01-31T07:54:51.264Z&#x27; Defaults to Today-7days | [optional] 
 **to** | **str**| Should use org.joda.time.DateTime parsable format. Example, &#x27;2022-01-31&#x27;, &#x27;2022-01-31T07:54Z&#x27; or &#x27;2022-01-31T07:54:51.264Z&#x27; Defaults to Today | [optional] 
 **buffer_percentage** | **int**| Buffer Percentage defaults to zero | [optional] 

### Return type

[**ResponseDTOECSRecommendationDTO**](ResponseDTOECSRecommendationDTO.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **node_recommendation_detail**
> ResponseDTONodeRecommendationDTO node_recommendation_detail(account_identifier, id)

Return node pool Recommendation

Returns node pool Recommendation details for the given identifier.

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
api_instance = harness_python_sdk.CloudCostRecommendationsDetailsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
id = 'id_example' # str | Node pool Recommendation identifier

try:
    # Return node pool Recommendation
    api_response = api_instance.node_recommendation_detail(account_identifier, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostRecommendationsDetailsApi->node_recommendation_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **id** | **str**| Node pool Recommendation identifier | 

### Return type

[**ResponseDTONodeRecommendationDTO**](ResponseDTONodeRecommendationDTO.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workload_recommendation_detail**
> ResponseDTOWorkloadRecommendationDTO workload_recommendation_detail(account_identifier, id, _from=_from, to=to)

Return workload Recommendation

Returns workload Recommendation details for the given Recommendation identifier.

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
api_instance = harness_python_sdk.CloudCostRecommendationsDetailsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
id = 'id_example' # str | Workload Recommendation identifier.
_from = '_from_example' # str | Should use org.joda.time.DateTime parsable format. Example, '2022-01-31', '2022-01-31T07:54Z' or '2022-01-31T07:54:51.264Z' Defaults to Today-7days (optional)
to = 'to_example' # str | Should use org.joda.time.DateTime parsable format. Example, '2022-01-31', '2022-01-31T07:54Z' or '2022-01-31T07:54:51.264Z' Defaults to Today (optional)

try:
    # Return workload Recommendation
    api_response = api_instance.workload_recommendation_detail(account_identifier, id, _from=_from, to=to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostRecommendationsDetailsApi->workload_recommendation_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **id** | **str**| Workload Recommendation identifier. | 
 **_from** | **str**| Should use org.joda.time.DateTime parsable format. Example, &#x27;2022-01-31&#x27;, &#x27;2022-01-31T07:54Z&#x27; or &#x27;2022-01-31T07:54:51.264Z&#x27; Defaults to Today-7days | [optional] 
 **to** | **str**| Should use org.joda.time.DateTime parsable format. Example, &#x27;2022-01-31&#x27;, &#x27;2022-01-31T07:54Z&#x27; or &#x27;2022-01-31T07:54:51.264Z&#x27; Defaults to Today | [optional] 

### Return type

[**ResponseDTOWorkloadRecommendationDTO**](ResponseDTOWorkloadRecommendationDTO.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

