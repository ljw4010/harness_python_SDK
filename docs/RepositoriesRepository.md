# RepositoriesRepository

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repo** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**ssh_private_key** | **str** | SSHPrivateKey contains the PEM data for authenticating at the repo server. Only used with Git repos. | [optional] 
**connection_state** | [**CommonsConnectionState**](CommonsConnectionState.md) |  | [optional] 
**insecure_ignore_host_key** | **bool** |  | [optional] 
**insecure** | **bool** |  | [optional] 
**enable_lfs** | **bool** | EnableLFS specifies whether git-lfs support should be enabled for this repo. Only valid for Git repositories. | [optional] 
**tls_client_cert_data** | **str** |  | [optional] 
**tls_client_cert_key** | **str** |  | [optional] 
**type** | **str** | Type specifies the type of the repo. Can be either \&quot;git\&quot; or \&quot;helm. \&quot;git\&quot; is assumed if empty or absent. | [optional] 
**name** | **str** |  | [optional] 
**inherited_creds** | **bool** |  | [optional] 
**enable_oci** | **bool** |  | [optional] 
**github_app_private_key** | **str** |  | [optional] 
**github_app_id** | **str** |  | [optional] 
**github_app_installation_id** | **str** |  | [optional] 
**github_app_enterprise_base_url** | **str** |  | [optional] 
**proxy** | **str** |  | [optional] 
**project** | **str** |  | [optional] 
**connection_type** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

