# ClusterBatchRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_identifier** | **str** | organization identifier of the cluster | [optional] 
**project_identifier** | **str** | project identifier of the cluster | [optional] 
**env_ref** | **str** | environment identifier of the cluster | 
**link_all_clusters** | **bool** | link all clusters | [optional] 
**unlink_all_clusters** | **bool** | unlink all clusters | [optional] 
**search_term** | **str** | search term if applicable. only valid if linking all clusters | [optional] 
**clusters** | [**list[ClusterBasicDTO]**](ClusterBasicDTO.md) | list of cluster identifiers and names | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

