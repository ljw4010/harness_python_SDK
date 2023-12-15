# harness_python_sdk.ClustersApi

All URIs are relative to *https://app.harness.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**agent_cluster_service_create**](ClustersApi.md#agent_cluster_service_create) | **POST** /gitops/api/v1/agents/{agentIdentifier}/clusters | Create creates a cluster
[**agent_cluster_service_delete**](ClustersApi.md#agent_cluster_service_delete) | **DELETE** /gitops/api/v1/agents/{agentIdentifier}/clusters/{identifier} | Delete deletes a cluster
[**agent_cluster_service_get**](ClustersApi.md#agent_cluster_service_get) | **GET** /gitops/api/v1/agents/{agentIdentifier}/clusters/{identifier} | Get returns a cluster by identifier
[**agent_cluster_service_list**](ClustersApi.md#agent_cluster_service_list) | **GET** /gitops/api/v1/agents/{agentIdentifier}/clusters | List returns list of clusters
[**agent_cluster_service_update**](ClustersApi.md#agent_cluster_service_update) | **PUT** /gitops/api/v1/agents/{agentIdentifier}/clusters/{identifier} | Update updates a cluster
[**agent_gpg_key_service_list**](ClustersApi.md#agent_gpg_key_service_list) | **GET** /gitops/api/v1/agents/{agentIdentifier}/gpgkeys | List all available repository certificates
[**cluster_service_exists**](ClustersApi.md#cluster_service_exists) | **GET** /gitops/api/v1/clusters/exists | Checks for whether the cluster exists
[**cluster_service_list_clusters**](ClustersApi.md#cluster_service_list_clusters) | **POST** /gitops/api/v1/clusters | List returns list of Clusters
[**delete_cluster**](ClustersApi.md#delete_cluster) | **DELETE** /ng/api/gitops/clusters/{identifier} | Delete a Cluster by identifier
[**get_cluster**](ClustersApi.md#get_cluster) | **GET** /ng/api/gitops/clusters/{identifier} | Gets a Cluster by identifier
[**get_cluster_list**](ClustersApi.md#get_cluster_list) | **GET** /ng/api/gitops/clusters | Gets cluster list
[**link_cluster**](ClustersApi.md#link_cluster) | **POST** /ng/api/gitops/clusters | link a Cluster
[**link_clusters**](ClustersApi.md#link_clusters) | **POST** /ng/api/gitops/clusters/batch | Link Clusters
[**unlink_clusters_in_batch**](ClustersApi.md#unlink_clusters_in_batch) | **POST** /ng/api/gitops/clusters/batchunlink | Unlink Clusters

# **agent_cluster_service_create**
> Servicev1Cluster agent_cluster_service_create(body, agent_identifier, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, identifier=identifier)

Create creates a cluster

Create clusters.

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
api_instance = harness_python_sdk.ClustersApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.ClustersClusterCreateRequest() # ClustersClusterCreateRequest | 
agent_identifier = 'agent_identifier_example' # str | Agent identifier for entity.
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity. (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
identifier = 'identifier_example' # str |  (optional)

try:
    # Create creates a cluster
    api_response = api_instance.agent_cluster_service_create(body, agent_identifier, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, identifier=identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersApi->agent_cluster_service_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClustersClusterCreateRequest**](ClustersClusterCreateRequest.md)|  | 
 **agent_identifier** | **str**| Agent identifier for entity. | 
 **account_identifier** | **str**| Account Identifier for the Entity. | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **identifier** | **str**|  | [optional] 

### Return type

[**Servicev1Cluster**](Servicev1Cluster.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_cluster_service_delete**
> ClustersClusterResponse agent_cluster_service_delete(agent_identifier, identifier, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, query_server=query_server, query_name=query_name, query_id_type=query_id_type, query_id_value=query_id_value, query_project=query_project)

Delete deletes a cluster

Delete cluster.

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
api_instance = harness_python_sdk.ClustersApi(harness_python_sdk.ApiClient(configuration))
agent_identifier = 'agent_identifier_example' # str | Agent identifier for entity.
identifier = 'identifier_example' # str | 
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity. (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
query_server = 'query_server_example' # str |  (optional)
query_name = 'query_name_example' # str |  (optional)
query_id_type = 'query_id_type_example' # str | type is the type of the specified cluster identifier ( \"server\" - default, \"name\" ). (optional)
query_id_value = 'query_id_value_example' # str | value holds the cluster server URL or cluster name. (optional)
query_project = 'query_project_example' # str |  (optional)

try:
    # Delete deletes a cluster
    api_response = api_instance.agent_cluster_service_delete(agent_identifier, identifier, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, query_server=query_server, query_name=query_name, query_id_type=query_id_type, query_id_value=query_id_value, query_project=query_project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersApi->agent_cluster_service_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_identifier** | **str**| Agent identifier for entity. | 
 **identifier** | **str**|  | 
 **account_identifier** | **str**| Account Identifier for the Entity. | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **query_server** | **str**|  | [optional] 
 **query_name** | **str**|  | [optional] 
 **query_id_type** | **str**| type is the type of the specified cluster identifier ( \&quot;server\&quot; - default, \&quot;name\&quot; ). | [optional] 
 **query_id_value** | **str**| value holds the cluster server URL or cluster name. | [optional] 
 **query_project** | **str**|  | [optional] 

### Return type

[**ClustersClusterResponse**](ClustersClusterResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_cluster_service_get**
> Servicev1Cluster agent_cluster_service_get(agent_identifier, identifier, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, query_server=query_server, query_name=query_name, query_id_type=query_id_type, query_id_value=query_id_value, query_project=query_project)

Get returns a cluster by identifier

Get cluster.

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
api_instance = harness_python_sdk.ClustersApi(harness_python_sdk.ApiClient(configuration))
agent_identifier = 'agent_identifier_example' # str | Agent identifier for entity.
identifier = 'identifier_example' # str | 
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
query_server = 'query_server_example' # str |  (optional)
query_name = 'query_name_example' # str |  (optional)
query_id_type = 'query_id_type_example' # str | type is the type of the specified cluster identifier ( \"server\" - default, \"name\" ). (optional)
query_id_value = 'query_id_value_example' # str | value holds the cluster server URL or cluster name. (optional)
query_project = 'query_project_example' # str |  (optional)

try:
    # Get returns a cluster by identifier
    api_response = api_instance.agent_cluster_service_get(agent_identifier, identifier, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, query_server=query_server, query_name=query_name, query_id_type=query_id_type, query_id_value=query_id_value, query_project=query_project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersApi->agent_cluster_service_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_identifier** | **str**| Agent identifier for entity. | 
 **identifier** | **str**|  | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **query_server** | **str**|  | [optional] 
 **query_name** | **str**|  | [optional] 
 **query_id_type** | **str**| type is the type of the specified cluster identifier ( \&quot;server\&quot; - default, \&quot;name\&quot; ). | [optional] 
 **query_id_value** | **str**| value holds the cluster server URL or cluster name. | [optional] 
 **query_project** | **str**|  | [optional] 

### Return type

[**Servicev1Cluster**](Servicev1Cluster.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_cluster_service_list**
> ClustersClusterList agent_cluster_service_list(agent_identifier, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, identifier=identifier, query_server=query_server, query_name=query_name, query_id_type=query_id_type, query_id_value=query_id_value, query_project=query_project)

List returns list of clusters

List clusters.

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
api_instance = harness_python_sdk.ClustersApi(harness_python_sdk.ApiClient(configuration))
agent_identifier = 'agent_identifier_example' # str | Agent identifier for entity.
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
identifier = 'identifier_example' # str |  (optional)
query_server = 'query_server_example' # str |  (optional)
query_name = 'query_name_example' # str |  (optional)
query_id_type = 'query_id_type_example' # str | type is the type of the specified cluster identifier ( \"server\" - default, \"name\" ). (optional)
query_id_value = 'query_id_value_example' # str | value holds the cluster server URL or cluster name. (optional)
query_project = 'query_project_example' # str |  (optional)

try:
    # List returns list of clusters
    api_response = api_instance.agent_cluster_service_list(agent_identifier, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, identifier=identifier, query_server=query_server, query_name=query_name, query_id_type=query_id_type, query_id_value=query_id_value, query_project=query_project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersApi->agent_cluster_service_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_identifier** | **str**| Agent identifier for entity. | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **identifier** | **str**|  | [optional] 
 **query_server** | **str**|  | [optional] 
 **query_name** | **str**|  | [optional] 
 **query_id_type** | **str**| type is the type of the specified cluster identifier ( \&quot;server\&quot; - default, \&quot;name\&quot; ). | [optional] 
 **query_id_value** | **str**| value holds the cluster server URL or cluster name. | [optional] 
 **query_project** | **str**|  | [optional] 

### Return type

[**ClustersClusterList**](ClustersClusterList.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_cluster_service_update**
> Servicev1Cluster agent_cluster_service_update(body, agent_identifier, identifier, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)

Update updates a cluster

Update cluster.

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
api_instance = harness_python_sdk.ClustersApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.ClustersClusterUpdateRequest() # ClustersClusterUpdateRequest | 
agent_identifier = 'agent_identifier_example' # str | Agent identifier for entity.
identifier = 'identifier_example' # str | 
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity. (optional)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)

try:
    # Update updates a cluster
    api_response = api_instance.agent_cluster_service_update(body, agent_identifier, identifier, account_identifier=account_identifier, org_identifier=org_identifier, project_identifier=project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersApi->agent_cluster_service_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClustersClusterUpdateRequest**](ClustersClusterUpdateRequest.md)|  | 
 **agent_identifier** | **str**| Agent identifier for entity. | 
 **identifier** | **str**|  | 
 **account_identifier** | **str**| Account Identifier for the Entity. | [optional] 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 

### Return type

[**Servicev1Cluster**](Servicev1Cluster.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_gpg_key_service_list**
> GpgkeysGnuPGPublicKeyList agent_gpg_key_service_list(agent_identifier, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, query_key_id=query_key_id)

List all available repository certificates

List all available repository certificates.

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
api_instance = harness_python_sdk.ClustersApi(harness_python_sdk.ApiClient(configuration))
agent_identifier = 'agent_identifier_example' # str | Agent identifier for entity.
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
query_key_id = 'query_key_id_example' # str | The GPG key ID to query for. (optional)

try:
    # List all available repository certificates
    api_response = api_instance.agent_gpg_key_service_list(agent_identifier, account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, query_key_id=query_key_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersApi->agent_gpg_key_service_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_identifier** | **str**| Agent identifier for entity. | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **query_key_id** | **str**| The GPG key ID to query for. | [optional] 

### Return type

[**GpgkeysGnuPGPublicKeyList**](GpgkeysGnuPGPublicKeyList.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_service_exists**
> bool cluster_service_exists(account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, agent_identifier=agent_identifier, server=server)

Checks for whether the cluster exists

Checks for whether the cluster exists

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
api_instance = harness_python_sdk.ClustersApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
agent_identifier = 'agent_identifier_example' # str | Agent identifier for entity. (optional)
server = 'server_example' # str |  (optional)

try:
    # Checks for whether the cluster exists
    api_response = api_instance.cluster_service_exists(account_identifier, org_identifier=org_identifier, project_identifier=project_identifier, agent_identifier=agent_identifier, server=server)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersApi->cluster_service_exists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **agent_identifier** | **str**| Agent identifier for entity. | [optional] 
 **server** | **str**|  | [optional] 

### Return type

**bool**

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_service_list_clusters**
> V1Clusterlist cluster_service_list_clusters(body)

List returns list of Clusters

List returns list of Clusters

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
api_instance = harness_python_sdk.ClustersApi(harness_python_sdk.ApiClient(configuration))
body = harness_python_sdk.Servicev1ClusterQuery() # Servicev1ClusterQuery | 

try:
    # List returns list of Clusters
    api_response = api_instance.cluster_service_list_clusters(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersApi->cluster_service_list_clusters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Servicev1ClusterQuery**](Servicev1ClusterQuery.md)|  | 

### Return type

[**V1Clusterlist**](V1Clusterlist.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cluster**
> ResponseDTOBoolean delete_cluster(identifier, account_identifier, environment_identifier, org_identifier=org_identifier, project_identifier=project_identifier, scope=scope)

Delete a Cluster by identifier

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
api_instance = harness_python_sdk.ClustersApi(harness_python_sdk.ApiClient(configuration))
identifier = 'identifier_example' # str | Cluster Identifier for the entity
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
environment_identifier = 'environment_identifier_example' # str | environmentIdentifier
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
scope = 'scope_example' # str | Scope for the gitops cluster (optional)

try:
    # Delete a Cluster by identifier
    api_response = api_instance.delete_cluster(identifier, account_identifier, environment_identifier, org_identifier=org_identifier, project_identifier=project_identifier, scope=scope)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersApi->delete_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Cluster Identifier for the entity | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **environment_identifier** | **str**| environmentIdentifier | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **scope** | **str**| Scope for the gitops cluster | [optional] 

### Return type

[**ResponseDTOBoolean**](ResponseDTOBoolean.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster**
> ResponseDTOClusterResponse get_cluster(identifier, account_identifier, environment_identifier, org_identifier=org_identifier, project_identifier=project_identifier, deleted=deleted)

Gets a Cluster by identifier

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
api_instance = harness_python_sdk.ClustersApi(harness_python_sdk.ApiClient(configuration))
identifier = 'identifier_example' # str | Cluster Identifier for the entity
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
environment_identifier = 'environment_identifier_example' # str | environmentIdentifier
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
deleted = false # bool | Specify whether cluster is deleted or not (optional) (default to false)

try:
    # Gets a Cluster by identifier
    api_response = api_instance.get_cluster(identifier, account_identifier, environment_identifier, org_identifier=org_identifier, project_identifier=project_identifier, deleted=deleted)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersApi->get_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Cluster Identifier for the entity | 
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **environment_identifier** | **str**| environmentIdentifier | 
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **deleted** | **bool**| Specify whether cluster is deleted or not | [optional] [default to false]

### Return type

[**ResponseDTOClusterResponse**](ResponseDTOClusterResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_list**
> ResponseDTOPageResponseClusterResponse get_cluster_list(account_identifier, environment_identifier, page=page, size=size, org_identifier=org_identifier, project_identifier=project_identifier, search_term=search_term, identifiers=identifiers, sort=sort)

Gets cluster list

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
api_instance = harness_python_sdk.ClustersApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
environment_identifier = 'environment_identifier_example' # str | Environment Identifier of the clusters
page = 0 # int | Page Index of the results to fetch.Default Value: 0 (optional) (default to 0)
size = 100 # int | Results per page (optional) (default to 100)
org_identifier = 'org_identifier_example' # str | Organization Identifier for the Entity. (optional)
project_identifier = 'project_identifier_example' # str | Project Identifier for the Entity. (optional)
search_term = 'search_term_example' # str | The word to be searched and included in the list response (optional)
identifiers = ['identifiers_example'] # list[str] | List of cluster identifiers (optional)
sort = ['sort_example'] # list[str] | Specifies the sorting criteria of the list. Like sorting based on the last updated entity, alphabetical sorting in an ascending or descending order (optional)

try:
    # Gets cluster list
    api_response = api_instance.get_cluster_list(account_identifier, environment_identifier, page=page, size=size, org_identifier=org_identifier, project_identifier=project_identifier, search_term=search_term, identifiers=identifiers, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersApi->get_cluster_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **environment_identifier** | **str**| Environment Identifier of the clusters | 
 **page** | **int**| Page Index of the results to fetch.Default Value: 0 | [optional] [default to 0]
 **size** | **int**| Results per page | [optional] [default to 100]
 **org_identifier** | **str**| Organization Identifier for the Entity. | [optional] 
 **project_identifier** | **str**| Project Identifier for the Entity. | [optional] 
 **search_term** | **str**| The word to be searched and included in the list response | [optional] 
 **identifiers** | [**list[str]**](str.md)| List of cluster identifiers | [optional] 
 **sort** | [**list[str]**](str.md)| Specifies the sorting criteria of the list. Like sorting based on the last updated entity, alphabetical sorting in an ascending or descending order | [optional] 

### Return type

[**ResponseDTOPageResponseClusterResponse**](ResponseDTOPageResponseClusterResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_cluster**
> ResponseDTOClusterResponse link_cluster(account_identifier, body=body)

link a Cluster

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
api_instance = harness_python_sdk.ClustersApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
body = harness_python_sdk.ClusterRequest() # ClusterRequest | Details of the createCluster to be linked (optional)

try:
    # link a Cluster
    api_response = api_instance.link_cluster(account_identifier, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersApi->link_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **body** | [**ClusterRequest**](ClusterRequest.md)| Details of the createCluster to be linked | [optional] 

### Return type

[**ResponseDTOClusterResponse**](ResponseDTOClusterResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_clusters**
> ResponseDTOClusterBatchResponse link_clusters(account_identifier, body=body)

Link Clusters

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
api_instance = harness_python_sdk.ClustersApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
body = harness_python_sdk.ClusterBatchRequest() # ClusterBatchRequest | Details of the createCluster to be created (optional)

try:
    # Link Clusters
    api_response = api_instance.link_clusters(account_identifier, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersApi->link_clusters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **body** | [**ClusterBatchRequest**](ClusterBatchRequest.md)| Details of the createCluster to be created | [optional] 

### Return type

[**ResponseDTOClusterBatchResponse**](ResponseDTOClusterBatchResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unlink_clusters_in_batch**
> ResponseDTOClusterBatchResponse unlink_clusters_in_batch(account_identifier, body=body)

Unlink Clusters

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
api_instance = harness_python_sdk.ClustersApi(harness_python_sdk.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | Account Identifier for the Entity.
body = harness_python_sdk.ClusterBatchRequest() # ClusterBatchRequest | Details of the createCluster to be created (optional)

try:
    # Unlink Clusters
    api_response = api_instance.unlink_clusters_in_batch(account_identifier, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersApi->unlink_clusters_in_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Account Identifier for the Entity. | 
 **body** | [**ClusterBatchRequest**](ClusterBatchRequest.md)| Details of the createCluster to be created | [optional] 

### Return type

[**ResponseDTOClusterBatchResponse**](ResponseDTOClusterBatchResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

