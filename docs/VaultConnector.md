# VaultConnector

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_token** | **str** | This is the authentication token for Vault. | [optional] 
**base_path** | **str** | This is the location of the Vault directory where Secret will be stored. | [optional] 
**vault_url** | **str** | URL of the HashiCorp Vault. | 
**renewal_interval_minutes** | **int** | This is the time interval for token renewal. | 
**secret_engine_manually_configured** | **bool** | Manually entered Secret Engine. | [optional] 
**secret_engine_name** | **str** | Name of the Secret Engine. | [optional] 
**app_role_id** | **str** | ID of App Role. | [optional] 
**secret_id** | **str** | ID of the Secret. | [optional] 
**secret_engine_version** | **int** | Version of Secret Engine. | [optional] 
**delegate_selectors** | **list[str]** | List of Delegate Selectors that belong to the same Delegate and are used to connect to the Secret Manager. | [optional] 
**namespace** | **str** | This is the Vault namespace where Secret will be created. | [optional] 
**sink_path** | **str** | This is the location at which auth token is to be read from. | [optional] 
**use_vault_agent** | **bool** | Boolean value to indicate if Vault Agent is used for authentication. | [optional] 
**use_aws_iam** | **bool** | Boolean value to indicate if Aws Iam is used for authentication. | [optional] 
**aws_region** | **str** | This is the Aws region where aws iam auth will happen. | [optional] 
**vault_aws_iam_role** | **str** | This is the Vault role defined to bind to aws iam account/role being accessed. | [optional] 
**use_k8s_auth** | **bool** | Boolean value to indicate if K8s Auth is used for authentication. | [optional] 
**vault_k8s_auth_role** | **str** | This is the role where K8s auth will happen. | [optional] 
**service_account_token_path** | **str** | This is the SA token path where the token is mounted in the K8s Pod. | [optional] 
**k8s_auth_endpoint** | **str** | This is the path where kubernetes auth is enabled in Vault. | [optional] 
**renew_app_role_token** | **bool** | Boolean value to indicate if appRole token renewal is enabled or not. | [optional] 
**enable_cache** | **bool** | Boolean value to indicate if cache is enabled for App Role Token. | [optional] 
**read_only** | **bool** |  | [optional] 
**default** | **bool** |  | [optional] 
**access_type** | **str** |  | [optional] 
**xvault_aws_iam_server_id** | **str** | This is the Aws Iam Header Server ID that has been configured for this Aws Iam instance. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

