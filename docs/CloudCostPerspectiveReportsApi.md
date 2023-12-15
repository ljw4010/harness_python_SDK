# swagger_client.CloudCostPerspectiveReportsApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_report_setting**](CloudCostPerspectiveReportsApi.md#create_report_setting) | **POST** /ccm/api/perspectiveReport/{accountIdentifier} | Create a schedule for a Report
[**delete_report_setting**](CloudCostPerspectiveReportsApi.md#delete_report_setting) | **DELETE** /ccm/api/perspectiveReport/{accountIdentifier} | Delete cost Perspective report
[**get_report_setting**](CloudCostPerspectiveReportsApi.md#get_report_setting) | **GET** /ccm/api/perspectiveReport/{accountIdentifier} | Fetch details of a cost Report
[**update_report_setting**](CloudCostPerspectiveReportsApi.md#update_report_setting) | **PUT** /ccm/api/perspectiveReport/{accountIdentifier} | Update a cost Perspective Report

# **create_report_setting**
> ResponseDTOListCEReportSchedule create_report_setting(body, account_identifier)

Create a schedule for a Report

Create a report schedule for the given Report ID or a Perspective ID.

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
api_instance = swagger_client.CloudCostPerspectiveReportsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CEReportSchedule() # CEReportSchedule | CEReportSchedule object to be saved
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Create a schedule for a Report
    api_response = api_instance.create_report_setting(body, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostPerspectiveReportsApi->create_report_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CEReportSchedule**](CEReportSchedule.md)| CEReportSchedule object to be saved | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**ResponseDTOListCEReportSchedule**](ResponseDTOListCEReportSchedule.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_report_setting**
> ResponseDTOString delete_report_setting(account_identifier, report_id=report_id, perspective_id=perspective_id)

Delete cost Perspective report

Delete cost Perspective Report for the given Report ID or a Perspective ID.

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
api_instance = swagger_client.CloudCostPerspectiveReportsApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
report_id = 'report_id_example' # str | Unique identifier for the Report (optional)
perspective_id = 'perspective_id_example' # str | Unique identifier for the Perspective (optional)

try:
    # Delete cost Perspective report
    api_response = api_instance.delete_report_setting(account_identifier, report_id=report_id, perspective_id=perspective_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostPerspectiveReportsApi->delete_report_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **report_id** | **str**| Unique identifier for the Report | [optional] 
 **perspective_id** | **str**| Unique identifier for the Perspective | [optional] 

### Return type

[**ResponseDTOString**](ResponseDTOString.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_setting**
> ResponseDTOListCEReportSchedule get_report_setting(account_identifier, perspective_id=perspective_id, report_id=report_id)

Fetch details of a cost Report

Fetch cost Report details for the given Report ID or a Perspective ID.

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
api_instance = swagger_client.CloudCostPerspectiveReportsApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
perspective_id = 'perspective_id_example' # str | Unique identifier for the Perspective (optional)
report_id = 'report_id_example' # str | Unique identifier for the Report (optional)

try:
    # Fetch details of a cost Report
    api_response = api_instance.get_report_setting(account_identifier, perspective_id=perspective_id, report_id=report_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostPerspectiveReportsApi->get_report_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **perspective_id** | **str**| Unique identifier for the Perspective | [optional] 
 **report_id** | **str**| Unique identifier for the Report | [optional] 

### Return type

[**ResponseDTOListCEReportSchedule**](ResponseDTOListCEReportSchedule.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_report_setting**
> ResponseDTOListCEReportSchedule update_report_setting(body, account_identifier)

Update a cost Perspective Report

Update cost Perspective Reports.

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
api_instance = swagger_client.CloudCostPerspectiveReportsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CEReportSchedule() # CEReportSchedule | CEReportSchedule object to be updated
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Update a cost Perspective Report
    api_response = api_instance.update_report_setting(body, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostPerspectiveReportsApi->update_report_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CEReportSchedule**](CEReportSchedule.md)| CEReportSchedule object to be updated | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**ResponseDTOListCEReportSchedule**](ResponseDTOListCEReportSchedule.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

