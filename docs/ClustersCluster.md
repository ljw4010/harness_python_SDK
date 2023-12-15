# ClustersCluster

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**config** | [**ClustersClusterConfig**](ClustersClusterConfig.md) |  | [optional] 
**connection_state** | [**CommonsConnectionState**](CommonsConnectionState.md) |  | [optional] 
**server_version** | **str** |  | [optional] 
**namespaces** | **list[str]** | Holds list of namespaces which are accessible in that cluster. Cluster level resources will be ignored if namespace list is not empty. | [optional] 
**refresh_requested_at** | [**V1Time**](V1Time.md) |  | [optional] 
**info** | [**ClustersClusterInfo**](ClustersClusterInfo.md) |  | [optional] 
**shard** | **str** | Shard contains optional shard number. Calculated on the fly by the application controller if not specified. | [optional] 
**cluster_resources** | **bool** | Indicates if cluster level resources should be managed. This setting is used only if cluster is connected in a namespaced mode. | [optional] 
**project** | **str** |  | [optional] 
**labels** | **dict(str, str)** |  | [optional] 
**annotations** | **dict(str, str)** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

