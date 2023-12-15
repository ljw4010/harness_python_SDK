# harness_python_sdk.CloudCostBudgetGroupsApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_budget_group**](CloudCostBudgetGroupsApi.md#create_budget_group) | **POST** /ccm/api/budgetGroups | Create a Budget Group
[**delete_budget_group**](CloudCostBudgetGroupsApi.md#delete_budget_group) | **DELETE** /ccm/api/budgetGroups/{id} | Delete a budget group
[**get_budget_and_budget_groups_list**](CloudCostBudgetGroupsApi.md#get_budget_and_budget_groups_list) | **GET** /ccm/api/budgetGroups/summary | Get list of budget and budget group summaries
[**get_budget_group**](CloudCostBudgetGroupsApi.md#get_budget_group) | **GET** /ccm/api/budgetGroups/{id} | Fetch Budget group details
[**get_last_period_cost**](CloudCostBudgetGroupsApi.md#get_last_period_cost) | **POST** /ccm/api/budgetGroups/aggregatedAmount | Get aggregated amount for given budget groups/budgets
[**list_budget_groups**](CloudCostBudgetGroupsApi.md#list_budget_groups) | **GET** /ccm/api/budgetGroups | List all the Budget groups
[**update_budget_group**](CloudCostBudgetGroupsApi.md#update_budget_group) | **PUT** /ccm/api/budgetGroups/{id} | Update an existing budget group

# **create_budget_group**
> ResponseDTOString create_budget_group(body, account_identifier)

Create a Budget Group

Create a Budget group to set and receive alerts when your costs exceed (or are forecasted to exceed) your budget group amount.

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
api_instance = harness_python_sdk.CloudCostBudgetGroupsApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.BudgetGroup() # BudgetGroup | Budget Group definition
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Create a Budget Group
    api_response = api_instance.create_budget_group(body, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostBudgetGroupsApi->create_budget_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BudgetGroup**](BudgetGroup.md)| Budget Group definition | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**ResponseDTOString**](ResponseDTOString.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_budget_group**
> ResponseDTOBoolean delete_budget_group(account_identifier, id)

Delete a budget group

Delete a Cloud Cost Budget group for the given Budget group ID.

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
api_instance = harness_python_sdk.CloudCostBudgetGroupsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
id = 'id_example' # str | Unique identifier for the budget

try:
    # Delete a budget group
    api_response = api_instance.delete_budget_group(account_identifier, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostBudgetGroupsApi->delete_budget_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **id** | **str**| Unique identifier for the budget | 

### Return type

[**ResponseDTOBoolean**](ResponseDTOBoolean.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_budget_and_budget_groups_list**
> ResponseDTOListBudgetSummary get_budget_and_budget_groups_list(account_identifier, show_all_entities, budget_group_id=budget_group_id, budget_group_sort_type=budget_group_sort_type, sort_order=sort_order)

Get list of budget and budget group summaries

Returns list of budgetSummary

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
api_instance = harness_python_sdk.CloudCostBudgetGroupsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
show_all_entities = true # bool | 
budget_group_id = 'budget_group_id_example' # str |  (optional)
budget_group_sort_type = 'budget_group_sort_type_example' # str | Budget Group List Sort Type (optional)
sort_order = 'sort_order_example' # str | Budget Group List Sort Order (optional)

try:
    # Get list of budget and budget group summaries
    api_response = api_instance.get_budget_and_budget_groups_list(account_identifier, show_all_entities, budget_group_id=budget_group_id, budget_group_sort_type=budget_group_sort_type, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostBudgetGroupsApi->get_budget_and_budget_groups_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **show_all_entities** | **bool**|  | 
 **budget_group_id** | **str**|  | [optional] 
 **budget_group_sort_type** | **str**| Budget Group List Sort Type | [optional] 
 **sort_order** | **str**| Budget Group List Sort Order | [optional] 

### Return type

[**ResponseDTOListBudgetSummary**](ResponseDTOListBudgetSummary.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_budget_group**
> ResponseDTOBudgetGroup get_budget_group(account_identifier, id)

Fetch Budget group details

Fetch details of a Cloud Cost Budget group for the given Budget group ID.

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
api_instance = harness_python_sdk.CloudCostBudgetGroupsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
id = 'id_example' # str | Unique identifier for the budget

try:
    # Fetch Budget group details
    api_response = api_instance.get_budget_group(account_identifier, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostBudgetGroupsApi->get_budget_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **id** | **str**| Unique identifier for the budget | 

### Return type

[**ResponseDTOBudgetGroup**](ResponseDTOBudgetGroup.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_last_period_cost**
> ResponseDTOListValueDataPoint get_last_period_cost(body, account_identifier, are_child_entities_budgets)

Get aggregated amount for given budget groups/budgets

Returns list of value dataPoints specifying aggregated amount

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
api_instance = harness_python_sdk.CloudCostBudgetGroupsApi(harness_python_sdk.ApiClient(configuration))
body = ['body_example'] # list[str] | List of child budgets/budget groups
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
are_child_entities_budgets = true # bool | 

try:
    # Get aggregated amount for given budget groups/budgets
    api_response = api_instance.get_last_period_cost(body, account_identifier, are_child_entities_budgets)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostBudgetGroupsApi->get_last_period_cost: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)| List of child budgets/budget groups | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **are_child_entities_budgets** | **bool**|  | 

### Return type

[**ResponseDTOListValueDataPoint**](ResponseDTOListValueDataPoint.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_budget_groups**
> ResponseDTOListBudgetGroup list_budget_groups(account_identifier, budget_group_sort_type=budget_group_sort_type, sort_order=sort_order)

List all the Budget groups

List all the Cloud Cost Budget Groups for an account.

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
api_instance = harness_python_sdk.CloudCostBudgetGroupsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
budget_group_sort_type = 'budget_group_sort_type_example' # str | Budget Group List Sort Type (optional)
sort_order = 'sort_order_example' # str | Budget Group List Sort Order (optional)

try:
    # List all the Budget groups
    api_response = api_instance.list_budget_groups(account_identifier, budget_group_sort_type=budget_group_sort_type, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostBudgetGroupsApi->list_budget_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **budget_group_sort_type** | **str**| Budget Group List Sort Type | [optional] 
 **sort_order** | **str**| Budget Group List Sort Order | [optional] 

### Return type

[**ResponseDTOListBudgetGroup**](ResponseDTOListBudgetGroup.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_budget_group**
> ResponseDTOString update_budget_group(body, account_identifier, id)

Update an existing budget group

Update an existing Cloud Cost Budget group for the given Budget group ID.

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
api_instance = harness_python_sdk.CloudCostBudgetGroupsApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.BudgetGroup() # BudgetGroup | The Budget object
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
id = 'id_example' # str | Unique identifier for the budget group

try:
    # Update an existing budget group
    api_response = api_instance.update_budget_group(body, account_identifier, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostBudgetGroupsApi->update_budget_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BudgetGroup**](BudgetGroup.md)| The Budget object | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **id** | **str**| Unique identifier for the budget group | 

### Return type

[**ResponseDTOString**](ResponseDTOString.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

