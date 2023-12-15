# harness_python_sdk.CloudCostBudgetsApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clone_budget**](CloudCostBudgetsApi.md#clone_budget) | **POST** /ccm/api/budgets/{id} | Clone a budget
[**create_budget**](CloudCostBudgetsApi.md#create_budget) | **POST** /ccm/api/budgets | Create a Budget
[**delete_budget**](CloudCostBudgetsApi.md#delete_budget) | **DELETE** /ccm/api/budgets/{id} | Delete a budget
[**get_budget**](CloudCostBudgetsApi.md#get_budget) | **GET** /ccm/api/budgets/{id} | Fetch Budget details
[**get_cost_details**](CloudCostBudgetsApi.md#get_cost_details) | **GET** /ccm/api/budgets/{id}/costDetails | Fetch the cost details of a Budget
[**list_budgets**](CloudCostBudgetsApi.md#list_budgets) | **GET** /ccm/api/budgets | List all the Budgets
[**list_budgets_for_perspective**](CloudCostBudgetsApi.md#list_budgets_for_perspective) | **GET** /ccm/api/budgets/perspectiveBudgets | List all the Budgets associated with a Perspective
[**update_budget**](CloudCostBudgetsApi.md#update_budget) | **PUT** /ccm/api/budgets/{id} | Update an existing budget

# **clone_budget**
> ResponseDTOString clone_budget(account_identifier, id, clone_name)

Clone a budget

Clone a Cloud Cost Budget using the given Budget ID.

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
api_instance = harness_python_sdk.CloudCostBudgetsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
id = 'id_example' # str | Unique identifier for the budget
clone_name = 'clone_name_example' # str | Name of the new budget

try:
    # Clone a budget
    api_response = api_instance.clone_budget(account_identifier, id, clone_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostBudgetsApi->clone_budget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **id** | **str**| Unique identifier for the budget | 
 **clone_name** | **str**| Name of the new budget | 

### Return type

[**ResponseDTOString**](ResponseDTOString.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_budget**
> ResponseDTOString create_budget(body, account_identifier)

Create a Budget

Create a Budget to set and receive alerts when your costs exceed (or are forecasted to exceed) your budget amount.

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
api_instance = harness_python_sdk.CloudCostBudgetsApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.Budget() # Budget | Budget definition
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Create a Budget
    api_response = api_instance.create_budget(body, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostBudgetsApi->create_budget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Budget**](Budget.md)| Budget definition | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**ResponseDTOString**](ResponseDTOString.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_budget**
> ResponseDTOString delete_budget(account_identifier, id)

Delete a budget

Delete a Cloud Cost Budget for the given Budget ID.

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
api_instance = harness_python_sdk.CloudCostBudgetsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
id = 'id_example' # str | Unique identifier for the budget

try:
    # Delete a budget
    api_response = api_instance.delete_budget(account_identifier, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostBudgetsApi->delete_budget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **id** | **str**| Unique identifier for the budget | 

### Return type

[**ResponseDTOString**](ResponseDTOString.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_budget**
> ResponseDTOBudget get_budget(account_identifier, id)

Fetch Budget details

Fetch details of a Cloud Cost Budget for the given Budget ID.

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
api_instance = harness_python_sdk.CloudCostBudgetsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
id = 'id_example' # str | Unique identifier for the budget

try:
    # Fetch Budget details
    api_response = api_instance.get_budget(account_identifier, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostBudgetsApi->get_budget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **id** | **str**| Unique identifier for the budget | 

### Return type

[**ResponseDTOBudget**](ResponseDTOBudget.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cost_details**
> ResponseDTOBudgetData get_cost_details(account_identifier, id, breakdown=breakdown)

Fetch the cost details of a Budget

Fetch the cost details of a Cloud Cost Budget for the given Budget ID.

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
api_instance = harness_python_sdk.CloudCostBudgetsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
id = 'id_example' # str | Unique identifier for the Budget
breakdown = 'breakdown_example' # str | MONTHLY/YEARLY breakdown. The default value is YEARLY (optional)

try:
    # Fetch the cost details of a Budget
    api_response = api_instance.get_cost_details(account_identifier, id, breakdown=breakdown)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostBudgetsApi->get_cost_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **id** | **str**| Unique identifier for the Budget | 
 **breakdown** | **str**| MONTHLY/YEARLY breakdown. The default value is YEARLY | [optional] 

### Return type

[**ResponseDTOBudgetData**](ResponseDTOBudgetData.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_budgets**
> ResponseDTOListBudget list_budgets(account_identifier, budget_sort_type=budget_sort_type, sort_order=sort_order)

List all the Budgets

List all the Cloud Cost Budgets.

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
api_instance = harness_python_sdk.CloudCostBudgetsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
budget_sort_type = 'budget_sort_type_example' # str | Budget List Sort Type (optional)
sort_order = 'sort_order_example' # str | Budget List Sort Order (optional)

try:
    # List all the Budgets
    api_response = api_instance.list_budgets(account_identifier, budget_sort_type=budget_sort_type, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostBudgetsApi->list_budgets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **budget_sort_type** | **str**| Budget List Sort Type | [optional] 
 **sort_order** | **str**| Budget List Sort Order | [optional] 

### Return type

[**ResponseDTOListBudget**](ResponseDTOListBudget.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_budgets_for_perspective**
> ResponseDTOListBudget list_budgets_for_perspective(account_identifier, perspective_id)

List all the Budgets associated with a Perspective

List all the Cloud Cost Budgets associated for the given Perspective ID.

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
api_instance = harness_python_sdk.CloudCostBudgetsApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
perspective_id = 'perspective_id_example' # str | Unique identifier for the Perspective

try:
    # List all the Budgets associated with a Perspective
    api_response = api_instance.list_budgets_for_perspective(account_identifier, perspective_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostBudgetsApi->list_budgets_for_perspective: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **perspective_id** | **str**| Unique identifier for the Perspective | 

### Return type

[**ResponseDTOListBudget**](ResponseDTOListBudget.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_budget**
> ResponseDTOString update_budget(body, account_identifier, id)

Update an existing budget

Update an existing Cloud Cost Budget for the given Budget ID.

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
api_instance = harness_python_sdk.CloudCostBudgetsApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.Budget() # Budget | The Budget object
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
id = 'id_example' # str | Unique identifier for the budget

try:
    # Update an existing budget
    api_response = api_instance.update_budget(body, account_identifier, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCostBudgetsApi->update_budget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Budget**](Budget.md)| The Budget object | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **id** | **str**| Unique identifier for the budget | 

### Return type

[**ResponseDTOString**](ResponseDTOString.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

