# swagger_client.OrganizationApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_organization**](OrganizationApi.md#create_organization) | **POST** /v1/orgs | Create an organization [Beta]
[**delete_organization**](OrganizationApi.md#delete_organization) | **DELETE** /v1/orgs/{org} | Delete an organization [Beta]
[**delete_organization_0**](OrganizationApi.md#delete_organization_0) | **DELETE** /ng/api/organizations/{identifier} | Delete an Organization
[**get_organization**](OrganizationApi.md#get_organization) | **GET** /v1/orgs/{org} | Retrieve an organization [Beta]
[**get_organization_0**](OrganizationApi.md#get_organization_0) | **GET** /ng/api/organizations/{identifier} | List Organization details
[**get_organization_list**](OrganizationApi.md#get_organization_list) | **GET** /ng/api/organizations | List Organizations by filter
[**get_organizations**](OrganizationApi.md#get_organizations) | **GET** /v1/orgs | List organizations [Beta]
[**post_organization**](OrganizationApi.md#post_organization) | **POST** /ng/api/organizations | Create an Organization
[**put_organization**](OrganizationApi.md#put_organization) | **PUT** /ng/api/organizations/{identifier} | Update an Organization
[**update_organization**](OrganizationApi.md#update_organization) | **PUT** /v1/orgs/{org} | Update an organization [Beta]

# **create_organization**
> OrganizationResponse create_organization(body, harness_account=harness_account)

Create an organization [Beta]

Creates a new organization.

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
api_instance = swagger_client.OrganizationApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateOrganizationRequest() # CreateOrganizationRequest | Post the necessary fields for the API to create an organization.
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)

try:
    # Create an organization [Beta]
    api_response = api_instance.create_organization(body, harness_account=harness_account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->create_organization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateOrganizationRequest**](CreateOrganizationRequest.md)| Post the necessary fields for the API to create an organization. | 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 

### Return type

[**OrganizationResponse**](OrganizationResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_organization**
> OrganizationResponse delete_organization(org, harness_account=harness_account)

Delete an organization [Beta]

Deletes the information of the organization with the matching organization identifier.

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
api_instance = swagger_client.OrganizationApi(swagger_client.ApiClient(configuration))
org = 'org_example' # str | Organization identifier
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)

try:
    # Delete an organization [Beta]
    api_response = api_instance.delete_organization(org, harness_account=harness_account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->delete_organization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| Organization identifier | 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 

### Return type

[**OrganizationResponse**](OrganizationResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_organization_0**
> ResponseDTOBoolean delete_organization_0(identifier, account_identifier, if_match=if_match)

Delete an Organization

Deletes Organization for the given ID.

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
api_instance = swagger_client.OrganizationApi(swagger_client.ApiClient(configuration))
identifier = 'identifier_example' # str | Organization Identifier for the Entity.
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
if_match = 'if_match_example' # str | Version number of the Organization (optional)

try:
    # Delete an Organization
    api_response = api_instance.delete_organization_0(identifier, account_identifier, if_match=if_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->delete_organization_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Organization Identifier for the Entity. | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **if_match** | **str**| Version number of the Organization | [optional] 

### Return type

[**ResponseDTOBoolean**](ResponseDTOBoolean.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization**
> OrganizationResponse get_organization(org, harness_account=harness_account)

Retrieve an organization [Beta]

Retrieves the information of the organization with the matching organization identifier.

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
api_instance = swagger_client.OrganizationApi(swagger_client.ApiClient(configuration))
org = 'org_example' # str | Organization identifier
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)

try:
    # Retrieve an organization [Beta]
    api_response = api_instance.get_organization(org, harness_account=harness_account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->get_organization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| Organization identifier | 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 

### Return type

[**OrganizationResponse**](OrganizationResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_0**
> ResponseDTOOrganizationResponse get_organization_0(identifier, account_identifier)

List Organization details

Lists Organization details using an Account and Organization ID.

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
api_instance = swagger_client.OrganizationApi(swagger_client.ApiClient(configuration))
identifier = 'identifier_example' # str | Organization Identifier for the Entity.
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # List Organization details
    api_response = api_instance.get_organization_0(identifier, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->get_organization_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Organization Identifier for the Entity. | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**ResponseDTOOrganizationResponse**](ResponseDTOOrganizationResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_list**
> ResponseDTOPageResponseOrganizationResponse get_organization_list(account_identifier, identifiers=identifiers, search_term=search_term, page_index=page_index, page_size=page_size, sort_orders=sort_orders, page_token=page_token)

List Organizations by filter

List all Organizations matching the given search criteria.

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
api_instance = swagger_client.OrganizationApi(swagger_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
identifiers = ['identifiers_example'] # list[str] | This is the list of Org Key IDs. Details specific to these IDs would be fetched. (optional)
search_term = 'search_term_example' # str | This would be used to filter Organizations. Any Organization having the specified string in its Name, ID and Tag would be filtered. (optional)
page_index = 0 # int | Page Index of the results to fetch.Default Value: 0 (optional) (default to 0)
page_size = 50 # int | Results per page(max 100)Default Value: 50 (optional) (default to 50)
sort_orders = [swagger_client.SortOrder()] # list[SortOrder] | Sort criteria for the elements. (optional)
page_token = 'page_token_example' # str | Page Token of the next results to fetch.Default Value: '' (optional)

try:
    # List Organizations by filter
    api_response = api_instance.get_organization_list(account_identifier, identifiers=identifiers, search_term=search_term, page_index=page_index, page_size=page_size, sort_orders=sort_orders, page_token=page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->get_organization_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **identifiers** | [**list[str]**](str.md)| This is the list of Org Key IDs. Details specific to these IDs would be fetched. | [optional] 
 **search_term** | **str**| This would be used to filter Organizations. Any Organization having the specified string in its Name, ID and Tag would be filtered. | [optional] 
 **page_index** | **int**| Page Index of the results to fetch.Default Value: 0 | [optional] [default to 0]
 **page_size** | **int**| Results per page(max 100)Default Value: 50 | [optional] [default to 50]
 **sort_orders** | [**list[SortOrder]**](SortOrder.md)| Sort criteria for the elements. | [optional] 
 **page_token** | **str**| Page Token of the next results to fetch.Default Value: &#x27;&#x27; | [optional] 

### Return type

[**ResponseDTOPageResponseOrganizationResponse**](ResponseDTOPageResponseOrganizationResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organizations**
> list[OrganizationResponse] get_organizations(org=org, search_term=search_term, page=page, limit=limit, harness_account=harness_account, sort=sort, order=order)

List organizations [Beta]

Retrieves the information of the organizations.

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
api_instance = swagger_client.OrganizationApi(swagger_client.ApiClient(configuration))
org = ['org_example'] # list[str] | Identifier field of the organizations the resource is scoped to (optional)
search_term = 'search_term_example' # str | This would be used to filter resources having attributes matching with search term. (optional)
page = 0 # int | Pagination page number strategy: Specify the page number within the paginated collection related to the number of items in each page  (optional) (default to 0)
limit = 30 # int | Number of items to return per page. (optional) (default to 30)
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)
sort = 'sort_example' # str | Parameter on the basis of which sorting is done. (optional)
order = 'order_example' # str | Order on the basis of which sorting is done. (optional)

try:
    # List organizations [Beta]
    api_response = api_instance.get_organizations(org=org, search_term=search_term, page=page, limit=limit, harness_account=harness_account, sort=sort, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->get_organizations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | [**list[str]**](str.md)| Identifier field of the organizations the resource is scoped to | [optional] 
 **search_term** | **str**| This would be used to filter resources having attributes matching with search term. | [optional] 
 **page** | **int**| Pagination page number strategy: Specify the page number within the paginated collection related to the number of items in each page  | [optional] [default to 0]
 **limit** | **int**| Number of items to return per page. | [optional] [default to 30]
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 
 **sort** | **str**| Parameter on the basis of which sorting is done. | [optional] 
 **order** | **str**| Order on the basis of which sorting is done. | [optional] 

### Return type

[**list[OrganizationResponse]**](OrganizationResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_organization**
> ResponseDTOOrganizationResponse post_organization(body, account_identifier)

Create an Organization

Creates a new Organization.

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
api_instance = swagger_client.OrganizationApi(swagger_client.ApiClient(configuration))
body = swagger_client.OrganizationRequest() # OrganizationRequest | Details of the Organization to create
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.

try:
    # Create an Organization
    api_response = api_instance.post_organization(body, account_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->post_organization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrganizationRequest**](OrganizationRequest.md)| Details of the Organization to create | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 

### Return type

[**ResponseDTOOrganizationResponse**](ResponseDTOOrganizationResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_organization**
> ResponseDTOOrganizationResponse put_organization(body, account_identifier, identifier, if_match=if_match)

Update an Organization

Updates Organization settings.

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
api_instance = swagger_client.OrganizationApi(swagger_client.ApiClient(configuration))
body = swagger_client.OrganizationRequest() # OrganizationRequest | This is the updated Organization. Please provide values for all fields, not just the fields you are updating
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
identifier = 'identifier_example' # str | Organization Identifier for the Entity.
if_match = 'if_match_example' # str | Version number of the Organization (optional)

try:
    # Update an Organization
    api_response = api_instance.put_organization(body, account_identifier, identifier, if_match=if_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->put_organization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrganizationRequest**](OrganizationRequest.md)| This is the updated Organization. Please provide values for all fields, not just the fields you are updating | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **identifier** | **str**| Organization Identifier for the Entity. | 
 **if_match** | **str**| Version number of the Organization | [optional] 

### Return type

[**ResponseDTOOrganizationResponse**](ResponseDTOOrganizationResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_organization**
> OrganizationResponse update_organization(body, org, harness_account=harness_account)

Update an organization [Beta]

Updates the information of the organization with the matching organization identifier.

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
api_instance = swagger_client.OrganizationApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateOrganizationRequest() # UpdateOrganizationRequest | Put the necessary fields for the API to update a organization.
org = 'org_example' # str | Organization identifier
harness_account = 'harness_account_example' # str | Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. (optional)

try:
    # Update an organization [Beta]
    api_response = api_instance.update_organization(body, org, harness_account=harness_account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->update_organization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateOrganizationRequest**](UpdateOrganizationRequest.md)| Put the necessary fields for the API to update a organization. | 
 **org** | **str**| Organization identifier | 
 **harness_account** | **str**| Identifier field of the account the resource is scoped to. This is required for Authorization methods other than the x-api-key header. If you are using the x-api-key header, this can be skipped. | [optional] 

### Return type

[**OrganizationResponse**](OrganizationResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

