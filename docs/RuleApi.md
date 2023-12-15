# swagger_client.RuleApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clone_rule**](RuleApi.md#clone_rule) | **POST** /ccm/api/governance/ruleClone | Clone a rule
[**delete_rule**](RuleApi.md#delete_rule) | **DELETE** /ccm/api/governance/rule/{ruleID} | Delete a rule
[**enqueue_governance_job**](RuleApi.md#enqueue_governance_job) | **POST** /ccm/api/governance/enqueueAdhoc | Enqueues job for execution
[**get_policies**](RuleApi.md#get_policies) | **POST** /ccm/api/governance/rule/list | Fetch rules for account
[**governance_connector_list**](RuleApi.md#governance_connector_list) | **GET** /ccm/api/governance/connectorList | connectors with governance enabled and valid permission
[**rule_schema**](RuleApi.md#rule_schema) | **GET** /ccm/api/governance/ruleSchema | Get Schema for entity
[**update_rule**](RuleApi.md#update_rule) | **PUT** /ccm/api/governance/rule | Update a Rule
[**validate_rule**](RuleApi.md#validate_rule) | **POST** /ccm/api/governance/ruleValidate | Validate a rule

# **clone_rule**
> ResponseDTORule clone_rule(body, account_identifier)

Clone a rule

Clone a Rule with the given ID.

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
api_instance = swagger_client.RuleApi(swagger_client.ApiClient(configuration))
body = swagger_client.CloneRuleDTO() # CloneRuleDTO | Request body containing Rule uuid
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Clone a rule
    api_response = api_instance.clone_rule(body, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RuleApi->clone_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CloneRuleDTO**](CloneRuleDTO.md)| Request body containing Rule uuid | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**ResponseDTORule**](ResponseDTORule.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_rule**
> ResponseDTOBoolean delete_rule(account_identifier, rule_id)

Delete a rule

Delete a Rule for the given a ID.

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
api_instance = swagger_client.RuleApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
rule_id = 'rule_id_example' # str | Unique identifier for the rule

try:
    # Delete a rule
    api_response = api_instance.delete_rule(account_identifier, rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RuleApi->delete_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **rule_id** | **str**| Unique identifier for the rule | 

### Return type

[**ResponseDTOBoolean**](ResponseDTOBoolean.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enqueue_governance_job**
> ResponseDTOGovernanceEnqueueResponseDTO enqueue_governance_job(body, account_identifier=account_identifier)

Enqueues job for execution

Enqueues job for execution.

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
api_instance = swagger_client.RuleApi(swagger_client.ApiClient(configuration))
body = swagger_client.GovernanceAdhocEnqueueDTO() # GovernanceAdhocEnqueueDTO | Request body for queuing the governance job
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity. (optional)

try:
    # Enqueues job for execution
    api_response = api_instance.enqueue_governance_job(body, account_identifier=account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RuleApi->enqueue_governance_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GovernanceAdhocEnqueueDTO**](GovernanceAdhocEnqueueDTO.md)| Request body for queuing the governance job | 
 **account_identifier** | **str**| Account Identifier for the Entity. | [optional] 

### Return type

[**ResponseDTOGovernanceEnqueueResponseDTO**](ResponseDTOGovernanceEnqueueResponseDTO.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policies**
> ResponseDTORuleList get_policies(body, account_identifier, rule_name_pattern=rule_name_pattern)

Fetch rules for account

Fetch rules 

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
api_instance = swagger_client.RuleApi(swagger_client.ApiClient(configuration))
body = swagger_client.ListDTO() # ListDTO | Request body containing rule object
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
rule_name_pattern = 'rule_name_pattern_example' # str | Search by Rule name pattern (optional)

try:
    # Fetch rules for account
    api_response = api_instance.get_policies(body, account_identifier, rule_name_pattern=rule_name_pattern)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RuleApi->get_policies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ListDTO**](ListDTO.md)| Request body containing rule object | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **rule_name_pattern** | **str**| Search by Rule name pattern | [optional] 

### Return type

[**ResponseDTORuleList**](ResponseDTORuleList.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **governance_connector_list**
> list[CcmConnectorResponse] governance_connector_list(account_identifier, view=view, connector_type=connector_type)

connectors with governance enabled and valid permission

get connectors with governance enabled and valid permission

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
api_instance = swagger_client.RuleApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
view = true # bool | View governance connector list (optional)
connector_type = 'connector_type_example' # str |  (optional)

try:
    # connectors with governance enabled and valid permission
    api_response = api_instance.governance_connector_list(account_identifier, view=view, connector_type=connector_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RuleApi->governance_connector_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **view** | **bool**| View governance connector list | [optional] 
 **connector_type** | **str**|  | [optional] 

### Return type

[**list[CcmConnectorResponse]**](CcmConnectorResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rule_schema**
> ResponseDTOString rule_schema(account_identifier, project_identifier=project_identifier, org_identifier=org_identifier)

Get Schema for entity

Get Schema for entity

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
api_instance = swagger_client.RuleApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | 
project_identifier = 'project_identifier_example' # str |  (optional)
org_identifier = 'org_identifier_example' # str |  (optional)

try:
    # Get Schema for entity
    api_response = api_instance.rule_schema(account_identifier, project_identifier=project_identifier, org_identifier=org_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RuleApi->rule_schema: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**|  | 
 **project_identifier** | **str**|  | [optional] 
 **org_identifier** | **str**|  | [optional] 

### Return type

[**ResponseDTOString**](ResponseDTOString.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_rule**
> ResponseDTORule update_rule(body, account_identifier)

Update a Rule

Update a Rule

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
api_instance = swagger_client.RuleApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateRuleDTO() # CreateRuleDTO | Request body containing rule object
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Update a Rule
    api_response = api_instance.update_rule(body, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RuleApi->update_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateRuleDTO**](CreateRuleDTO.md)| Request body containing rule object | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**ResponseDTORule**](ResponseDTORule.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_rule**
> validate_rule(body, account_identifier)

Validate a rule

Validate a Rule .

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
api_instance = swagger_client.RuleApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateRuleDTO() # CreateRuleDTO | Request body containing Rule uuid
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Validate a rule
    api_instance.validate_rule(body, account_identifier)
except ApiException as e:
    print("Exception when calling RuleApi->validate_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateRuleDTO**](CreateRuleDTO.md)| Request body containing Rule uuid | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

