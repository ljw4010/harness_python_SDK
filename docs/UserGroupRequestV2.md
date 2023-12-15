# UserGroupRequestV2

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_identifier** | **str** | Account Identifier for the Entity. | [optional] 
**org_identifier** | **str** | Organization Identifier for the Entity. | [optional] 
**project_identifier** | **str** | Project Identifier for the Entity. | [optional] 
**identifier** | **str** | Identifier of the UserGroup. | 
**name** | **str** | Name of the UserGroup. | 
**users** | **list[str]** | List of users emails in the UserGroup. Maximum users can be 5000. | [optional] 
**notification_configs** | [**list[NotificationSettingConfigDTO]**](NotificationSettingConfigDTO.md) | List of notification settings. | [optional] 
**is_sso_linked** | **bool** |  | [optional] 
**linked_sso_id** | **str** | Identifier of the linked SSO. | [optional] 
**linked_sso_display_name** | **str** | Name of the linked SSO. | [optional] 
**sso_group_id** | **str** | Identifier of the userGroup in SSO. | [optional] 
**sso_group_name** | **str** | Name of the SSO userGroup. | [optional] 
**linked_sso_type** | **str** | Type of linked SSO | [optional] 
**externally_managed** | **bool** | Specifies whether or not the userGroup is externally managed. | [optional] 
**description** | **str** | Description of the entity | [optional] 
**tags** | **dict(str, str)** | Tags | [optional] 
**harness_managed** | **bool** | Specifies whether or not the userGroup is managed by harness. | [optional] 
**sso_linked** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

