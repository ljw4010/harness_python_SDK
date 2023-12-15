# ApplicationsApplicationTree

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nodes** | [**list[ApplicationsResourceNode]**](ApplicationsResourceNode.md) | Nodes contains list of nodes which either directly managed by the application and children of directly managed nodes. | [optional] 
**orphaned_nodes** | [**list[ApplicationsResourceNode]**](ApplicationsResourceNode.md) | OrphanedNodes contains if or orphaned nodes: nodes which are not managed by the app but in the same namespace. List is populated only if orphaned resources enabled in app project. | [optional] 
**hosts** | [**list[ApplicationsHostInfo]**](ApplicationsHostInfo.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

