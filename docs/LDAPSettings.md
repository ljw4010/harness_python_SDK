# LDAPSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_settings** | [**LdapConnectionSettings**](LdapConnectionSettings.md) |  | 
**identifier** | **str** | This is the LDAP setting identifier. | 
**user_settings_list** | [**list[LdapUserSettings]**](LdapUserSettings.md) | This is the user settings list in LDAP setting. | [optional] 
**group_settings_list** | [**list[LdapGroupSettings]**](LdapGroupSettings.md) | This is the group settings list in LDAP setting. | [optional] 
**display_name** | **str** | This is the LDAP setting display name. | 
**cron_expression** | **str** | This is the cron expression in LDAP Settings. | [optional] 
**next_iterations** | **list[int]** | This is the list of iterations for next LDAP sync job. | [optional] 
**disabled** | **bool** | This tells if LDAP Settings is disabled or not, LDAP sync won&#x27;t happen in disabled state. | [optional] 
**settings_type** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

