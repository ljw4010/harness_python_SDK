# Invite

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier of the Invite. | [optional] 
**name** | **str** | Name of the Invite. | [optional] 
**email** | **str** | Email Id associated with the user to be invited. | 
**account_identifier** | **str** | Account Identifier for the Entity. | [optional] 
**org_identifier** | **str** | Organization Identifier for the Entity. | [optional] 
**project_identifier** | **str** | Project Identifier for the Entity. | [optional] 
**role_bindings** | [**list[RoleBinding]**](RoleBinding.md) | Role bindings to be associated with the invited users. | [optional] 
**user_groups** | **list[str]** | List of the userGroups in the invite. | [optional] 
**invite_type** | **str** | Specifies the invite type. | 
**approved** | **bool** | Specifies whether or not the invite is approved. By default this value is set to false. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

