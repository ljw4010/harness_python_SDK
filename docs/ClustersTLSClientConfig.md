# ClustersTLSClientConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**insecure** | **bool** | Insecure specifies that the server should be accessed without verifying the TLS certificate. For testing only. | [optional] 
**server_name** | **str** | ServerName is passed to the server for SNI and is used in the client to check server certificates against. If ServerName is empty, the hostname used to contact the server is used. | [optional] 
**cert_data** | **str** |  | [optional] 
**key_data** | **str** |  | [optional] 
**ca_data** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

