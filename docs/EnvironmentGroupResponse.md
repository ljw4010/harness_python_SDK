# EnvironmentGroupResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | Account Identifier for the Entity. | [optional] 
**org_identifier** | **str** | Organization Identifier for the Entity. | [optional] 
**project_identifier** | **str** | Project Identifier for the Entity. | [optional] 
**identifier** | **str** | Identifier for the Entity. | [optional] 
**name** | **str** | Name of the Entity | [optional] 
**description** | **str** | Description of the entity | [optional] 
**color** | **str** | Color Code for the Entity | [optional] 
**deleted** | **bool** | Deletion status for Entity | [optional] 
**tags** | **dict(str, str)** | Tags | [optional] 
**env_identifiers** | **list[str]** | Environment Identifiers linked with Environment Group Identity | [optional] 
**env_response** | [**list[EnvironmentResponse]**](EnvironmentResponse.md) | Info of Environments linked with Entity | [optional] 
**yaml** | **str** | Yaml of the Environment Group | [optional] 
**git_details** | [**EntityGitDetails1**](EntityGitDetails1.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

