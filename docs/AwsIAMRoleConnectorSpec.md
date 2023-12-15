# AwsIAMRoleConnectorSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | This specifies the type of connector | 
**cross_account_role_arn** | **str** | If you want to use one AWS account for the connection, but you want to deploy or build in a different AWS account. In this scenario, the AWS account used for AWS access in Credentials will assume the IAM role you specify in Cross-account role ARN setting. This option uses the AWS Security Token Service (STS) feature. | [optional] 
**external_id** | **str** | If the administrator of the account to which the role belongs provided you with an external ID, then enter that value. | [optional] 
**test_region** | **str** | By default, Harness uses the us-east-1 region to test the credentials for this Connector. If you want to use an AWS GovCloud account for this Connector, select it in Test Region. GovCloud is used by organizations such as government agencies at the federal, state, and local level, as well as contractors, educational institutions. It is also used for regulatory compliance with these organizations. | [optional] 
**delegate_selectors** | **list[str]** | List of unique delegate selectors | [optional] 
**execute_on_delegate** | **bool** | execute on delegate | [optional] [default to True]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

