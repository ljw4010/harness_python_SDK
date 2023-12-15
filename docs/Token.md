# Token

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Identifier of the Token | [optional] 
**name** | **str** | Name of the Token | 
**valid_from** | **int** | This is the time from which the Token is valid. The time is in milliseconds. | [optional] 
**valid_to** | **int** | This is the time till which the Token is valid. The time is in milliseconds. | [optional] 
**scheduled_expire_time** | **int** | Scheduled expiry time in milliseconds. | [optional] 
**valid** | **bool** | Boolean value to indicate if Token is valid or not. | [optional] 
**account_identifier** | **str** | Account Identifier for the Entity. | [optional] 
**project_identifier** | **str** | Project Identifier for the Entity. | [optional] 
**org_identifier** | **str** | Organization Identifier for the Entity. | [optional] 
**api_key_identifier** | **str** | This is the API Key Id within which the Token is created. | [optional] 
**parent_identifier** | **str** | This is the ID of the Parent entity from which the Token inherits its role bindings. | [optional] 
**api_key_type** | **str** | Type of the API Key | [optional] 
**description** | **str** | Description of the Token | [optional] 
**tags** | **dict(str, str)** | Tags for the Token | [optional] 
**email** | **str** | Email Id of the user who created the Token. | [optional] 
**username** | **str** | Name of the user who created the Token. | [optional] 
**encoded_password** | **str** | This is the encoded password of the Token. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

