# harness_python_sdk.UsageApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ccmdownload_active_service_csv_report**](UsageApi.md#ccmdownload_active_service_csv_report) | **GET** /ccm/api/usage/cd/active-services/csv/download | Download CSV Active Services report
[**ccmget_cd_license_usage_for_service_instances**](UsageApi.md#ccmget_cd_license_usage_for_service_instances) | **GET** /ccm/api/usage/CD/serviceInstancesLicense | Gets License Usage By Module, Timestamp, and Account Identifier
[**ccmget_cd_license_usage_for_services**](UsageApi.md#ccmget_cd_license_usage_for_services) | **GET** /ccm/api/usage/CD/servicesLicense | Gets License Usage By Module, Timestamp, and Account Identifier
[**ccmget_license_usage**](UsageApi.md#ccmget_license_usage) | **GET** /ccm/api/usage/{module} | Gets License Usage By Module, Timestamp, and Account Identifier
[**cvget_license_usage**](UsageApi.md#cvget_license_usage) | **GET** /cv/api/usage/CV | 
[**download_active_monitored_service_csv_report**](UsageApi.md#download_active_monitored_service_csv_report) | **GET** /cv/api/usage/SRM/active-monitored-services/csv/download | Download CSV Active Monitored Services report
[**download_active_service_csv_report**](UsageApi.md#download_active_service_csv_report) | **GET** /ng/api/usage/cd/active-services/csv/download | Download CSV Active Services report
[**download_active_service_monitored_csv_report**](UsageApi.md#download_active_service_monitored_csv_report) | **GET** /cv/api/usage/SRM/active-services-monitored/csv/download | Download CSV Active Services Monitored report
[**get_cd_license_usage_for_service_instances**](UsageApi.md#get_cd_license_usage_for_service_instances) | **GET** /ng/api/usage/CD/serviceInstancesLicense | Gets License Usage By Module, Timestamp, and Account Identifier
[**get_cd_license_usage_for_services**](UsageApi.md#get_cd_license_usage_for_services) | **GET** /ng/api/usage/CD/servicesLicense | Gets License Usage By Module, Timestamp, and Account Identifier
[**get_license_usage**](UsageApi.md#get_license_usage) | **GET** /ng/api/usage/{module} | Gets License Usage By Module, Timestamp, and Account Identifier
[**get_srm_license_usage**](UsageApi.md#get_srm_license_usage) | **GET** /cv/api/usage/SRM | 
[**list_srm_active_monitored_services**](UsageApi.md#list_srm_active_monitored_services) | **POST** /cv/api/usage/SRM/active-monitored-services | Returns a List of active monitored services along with identifier,Active Monitored Services Count and other details

# **ccmdownload_active_service_csv_report**
> ccmdownload_active_service_csv_report(account_identifier=account_identifier, timestamp=timestamp)

Download CSV Active Services report

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
api_instance = harness_python_sdk.UsageApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity. (optional)
timestamp = 0 # int |  (optional) (default to 0)

try:
    # Download CSV Active Services report
    api_instance.ccmdownload_active_service_csv_report(account_identifier=account_identifier, timestamp=timestamp)
except ApiException as e:
    print("Exception when calling UsageApi->ccmdownload_active_service_csv_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | [optional] 
 **timestamp** | **int**|  | [optional] [default to 0]

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ccmget_cd_license_usage_for_service_instances**
> ResponseDTOServiceInstanceUsageDTO ccmget_cd_license_usage_for_service_instances(account_identifier=account_identifier, timestamp=timestamp)

Gets License Usage By Module, Timestamp, and Account Identifier

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
api_instance = harness_python_sdk.UsageApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account id to get the license usage. (optional)
timestamp = 789 # int |  (optional)

try:
    # Gets License Usage By Module, Timestamp, and Account Identifier
    api_response = api_instance.ccmget_cd_license_usage_for_service_instances(account_identifier=account_identifier, timestamp=timestamp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsageApi->ccmget_cd_license_usage_for_service_instances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account id to get the license usage. | [optional] 
 **timestamp** | **int**|  | [optional] 

### Return type

[**ResponseDTOServiceInstanceUsageDTO**](ResponseDTOServiceInstanceUsageDTO.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ccmget_cd_license_usage_for_services**
> ResponseDTOServiceUsageDTO ccmget_cd_license_usage_for_services(account_identifier=account_identifier, timestamp=timestamp)

Gets License Usage By Module, Timestamp, and Account Identifier

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
api_instance = harness_python_sdk.UsageApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account id to get the license usage. (optional)
timestamp = 789 # int |  (optional)

try:
    # Gets License Usage By Module, Timestamp, and Account Identifier
    api_response = api_instance.ccmget_cd_license_usage_for_services(account_identifier=account_identifier, timestamp=timestamp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsageApi->ccmget_cd_license_usage_for_services: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account id to get the license usage. | [optional] 
 **timestamp** | **int**|  | [optional] 

### Return type

[**ResponseDTOServiceUsageDTO**](ResponseDTOServiceUsageDTO.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ccmget_license_usage**
> ResponseDTOLicenseUsage ccmget_license_usage(module, account_identifier=account_identifier, timestamp=timestamp, cd_license_type=cd_license_type)

Gets License Usage By Module, Timestamp, and Account Identifier

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
api_instance = harness_python_sdk.UsageApi(harness_python_sdk.ApiClient(configuration))
module = 'module_example' # str | A Harness platform module.
account_identifier = 'account_identifier_example' # str | Account id to get the license usage. (optional)
timestamp = 789 # int |  (optional)
cd_license_type = 'cd_license_type_example' # str |  (optional)

try:
    # Gets License Usage By Module, Timestamp, and Account Identifier
    api_response = api_instance.ccmget_license_usage(module, account_identifier=account_identifier, timestamp=timestamp, cd_license_type=cd_license_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsageApi->ccmget_license_usage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **module** | **str**| A Harness platform module. | 
 **account_identifier** | **str**| Account id to get the license usage. | [optional] 
 **timestamp** | **int**|  | [optional] 
 **cd_license_type** | **str**|  | [optional] 

### Return type

[**ResponseDTOLicenseUsage**](ResponseDTOLicenseUsage.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cvget_license_usage**
> ResponseDTOSRMLicenseUsageDTO cvget_license_usage(account_identifier, timestamp=timestamp)



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
api_instance = harness_python_sdk.UsageApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | 
timestamp = 789 # int |  (optional)

try:
    api_response = api_instance.cvget_license_usage(account_identifier, timestamp=timestamp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsageApi->cvget_license_usage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**|  | 
 **timestamp** | **int**|  | [optional] 

### Return type

[**ResponseDTOSRMLicenseUsageDTO**](ResponseDTOSRMLicenseUsageDTO.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_active_monitored_service_csv_report**
> download_active_monitored_service_csv_report(account_identifier=account_identifier, timestamp=timestamp)

Download CSV Active Monitored Services report

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
api_instance = harness_python_sdk.UsageApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity. (optional)
timestamp = 0 # int |  (optional) (default to 0)

try:
    # Download CSV Active Monitored Services report
    api_instance.download_active_monitored_service_csv_report(account_identifier=account_identifier, timestamp=timestamp)
except ApiException as e:
    print("Exception when calling UsageApi->download_active_monitored_service_csv_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | [optional] 
 **timestamp** | **int**|  | [optional] [default to 0]

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_active_service_csv_report**
> download_active_service_csv_report(account_identifier=account_identifier, timestamp=timestamp)

Download CSV Active Services report

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
api_instance = harness_python_sdk.UsageApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity. (optional)
timestamp = 0 # int |  (optional) (default to 0)

try:
    # Download CSV Active Services report
    api_instance.download_active_service_csv_report(account_identifier=account_identifier, timestamp=timestamp)
except ApiException as e:
    print("Exception when calling UsageApi->download_active_service_csv_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | [optional] 
 **timestamp** | **int**|  | [optional] [default to 0]

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_active_service_monitored_csv_report**
> download_active_service_monitored_csv_report(account_identifier=account_identifier, timestamp=timestamp)

Download CSV Active Services Monitored report

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
api_instance = harness_python_sdk.UsageApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity. (optional)
timestamp = 0 # int |  (optional) (default to 0)

try:
    # Download CSV Active Services Monitored report
    api_instance.download_active_service_monitored_csv_report(account_identifier=account_identifier, timestamp=timestamp)
except ApiException as e:
    print("Exception when calling UsageApi->download_active_service_monitored_csv_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | [optional] 
 **timestamp** | **int**|  | [optional] [default to 0]

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cd_license_usage_for_service_instances**
> ResponseDTOServiceInstanceUsageDTO get_cd_license_usage_for_service_instances(account_identifier=account_identifier, timestamp=timestamp)

Gets License Usage By Module, Timestamp, and Account Identifier

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
api_instance = harness_python_sdk.UsageApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account id to get the license usage. (optional)
timestamp = 789 # int |  (optional)

try:
    # Gets License Usage By Module, Timestamp, and Account Identifier
    api_response = api_instance.get_cd_license_usage_for_service_instances(account_identifier=account_identifier, timestamp=timestamp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsageApi->get_cd_license_usage_for_service_instances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account id to get the license usage. | [optional] 
 **timestamp** | **int**|  | [optional] 

### Return type

[**ResponseDTOServiceInstanceUsageDTO**](ResponseDTOServiceInstanceUsageDTO.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cd_license_usage_for_services**
> ResponseDTOServiceUsageDTO get_cd_license_usage_for_services(account_identifier=account_identifier, timestamp=timestamp)

Gets License Usage By Module, Timestamp, and Account Identifier

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
api_instance = harness_python_sdk.UsageApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account id to get the license usage. (optional)
timestamp = 789 # int |  (optional)

try:
    # Gets License Usage By Module, Timestamp, and Account Identifier
    api_response = api_instance.get_cd_license_usage_for_services(account_identifier=account_identifier, timestamp=timestamp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsageApi->get_cd_license_usage_for_services: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account id to get the license usage. | [optional] 
 **timestamp** | **int**|  | [optional] 

### Return type

[**ResponseDTOServiceUsageDTO**](ResponseDTOServiceUsageDTO.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_license_usage**
> ResponseDTOLicenseUsage get_license_usage(module, account_identifier=account_identifier, timestamp=timestamp, cd_license_type=cd_license_type)

Gets License Usage By Module, Timestamp, and Account Identifier

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
api_instance = harness_python_sdk.UsageApi(harness_python_sdk.ApiClient(configuration))
module = 'module_example' # str | A Harness platform module.
account_identifier = 'account_identifier_example' # str | Account id to get the license usage. (optional)
timestamp = 789 # int |  (optional)
cd_license_type = 'cd_license_type_example' # str |  (optional)

try:
    # Gets License Usage By Module, Timestamp, and Account Identifier
    api_response = api_instance.get_license_usage(module, account_identifier=account_identifier, timestamp=timestamp, cd_license_type=cd_license_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsageApi->get_license_usage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **module** | **str**| A Harness platform module. | 
 **account_identifier** | **str**| Account id to get the license usage. | [optional] 
 **timestamp** | **int**|  | [optional] 
 **cd_license_type** | **str**|  | [optional] 

### Return type

[**ResponseDTOLicenseUsage**](ResponseDTOLicenseUsage.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_srm_license_usage**
> ResponseDTOSRMLicenseUsageDTO get_srm_license_usage(account_identifier, timestamp=timestamp)



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
api_instance = harness_python_sdk.UsageApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | 
timestamp = 789 # int |  (optional)

try:
    api_response = api_instance.get_srm_license_usage(account_identifier, timestamp=timestamp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsageApi->get_srm_license_usage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**|  | 
 **timestamp** | **int**|  | [optional] 

### Return type

[**ResponseDTOSRMLicenseUsageDTO**](ResponseDTOSRMLicenseUsageDTO.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_srm_active_monitored_services**
> ResponseDTOPageActiveMonitoredService list_srm_active_monitored_services(body=body, account_identifier=account_identifier, page=page, size=size, sort=sort, timestamp=timestamp)

Returns a List of active monitored services along with identifier,Active Monitored Services Count and other details

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
api_instance = harness_python_sdk.UsageApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.ActiveServiceMonitoredFilterParams() # ActiveServiceMonitoredFilterParams | Details of the Active Services Monitored Filter (optional)
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity. (optional)
page = 0 # int | Page Index of the results to fetch.Default Value: 0 (optional) (default to 0)
size = 20 # int | Results per page (optional) (default to 20)
sort = ['sort_example'] # list[str] | Sort criteria for the elements. (optional)
timestamp = 0 # int |  (optional) (default to 0)

try:
    # Returns a List of active monitored services along with identifier,Active Monitored Services Count and other details
    api_response = api_instance.list_srm_active_monitored_services(body=body, account_identifier=account_identifier, page=page, size=size, sort=sort, timestamp=timestamp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsageApi->list_srm_active_monitored_services: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ActiveServiceMonitoredFilterParams**](ActiveServiceMonitoredFilterParams.md)| Details of the Active Services Monitored Filter | [optional] 
 **account_identifier** | **str**| Account Identifier for the Entity. | [optional] 
 **page** | **int**| Page Index of the results to fetch.Default Value: 0 | [optional] [default to 0]
 **size** | **int**| Results per page | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Sort criteria for the elements. | [optional] 
 **timestamp** | **int**|  | [optional] [default to 0]

### Return type

[**ResponseDTOPageActiveMonitoredService**](ResponseDTOPageActiveMonitoredService.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

