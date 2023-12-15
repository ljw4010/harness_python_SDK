# AwsKmsAssumeSTSConnectorSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | This specifies the type of connector | 
**kms_arn** | **str** | Amazon Resource Name (ARN) | 
**region** | **str** | AWS Region for kms | 
**default** | **bool** | Boolean value to indicate if the Secret Manager is your default Secret Manager | [optional] 
**delegate_selectors** | **list[str]** | List of Delegate Selectors that belong to the same Delegate and are used to connect to the Secret Manager | 
**role_arn** | **str** | Role ARN for the Delegate with STS Role | [optional] 
**external_id** | **str** | If the administrator of the account to which the role belongs provided you with an external ID, then enter that value. | [optional] 
**assume_sts_role_duration** | **str** | This is the AssumeRole Session Duration | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

