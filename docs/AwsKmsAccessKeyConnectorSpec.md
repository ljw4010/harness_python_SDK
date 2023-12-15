# AwsKmsAccessKeyConnectorSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | This specifies the type of connector | 
**kms_arn** | **str** | Amazon Resource Name (ARN) | 
**region** | **str** | AWS Region for kms | 
**default** | **bool** | Boolean value to indicate if the Secret Manager is your default Secret Manager | [optional] 
**access_key** | **str** | Access Key for AWS authentication | 
**secret_key** | **str** | Secret Key for AWS authentication | 
**delegate_selectors** | **list[str]** | List of Delegate Selectors that belong to the same Delegate and are used to connect to the Secret Manager | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

