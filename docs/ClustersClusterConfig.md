# ClustersClusterConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**bearer_token** | **str** | Server requires Bearer authentication. This client will not attempt to use refresh tokens for an OAuth2 flow. TODO: demonstrate an OAuth2 compatible client. | [optional] 
**tls_client_config** | [**ClustersTLSClientConfig**](ClustersTLSClientConfig.md) |  | [optional] 
**aws_auth_config** | [**ClustersAWSAuthConfig**](ClustersAWSAuthConfig.md) |  | [optional] 
**role_arn** | **str** | RoleARN contains optional role ARN. If set then AWS IAM Authenticator assume a role to perform cluster operations instead of the default AWS credential provider chain. | [optional] 
**aws_cluster_name** | **str** | AWS Cluster name. If set then AWS CLI EKS token command will be used to access cluster. | [optional] 
**exec_provider_config** | [**ClustersExecProviderConfig**](ClustersExecProviderConfig.md) |  | [optional] 
**cluster_connection_type** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

