# SettingDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Identifier of the Setting. | 
**name** | **str** | Name of the Setting. | 
**org_identifier** | **str** | Organization Identifier for the Entity. | [optional] 
**project_identifier** | **str** | Project Identifier for the Entity. | [optional] 
**category** | **str** | Category of the Setting. | 
**group_identifier** | **str** | Group Id of the setting | 
**value_type** | **str** | Type of Value of the Setting. | 
**allowed_values** | **list[str]** | Set of Values allowed for the Setting. | [optional] 
**allow_overrides** | **bool** | Allow override of the Setting in sub-scopes. | 
**value** | **str** | Value of the setting | [optional] 
**default_value** | **str** | Default Value of the Setting. | [optional] 
**setting_source** | **str** | Source of the setting value | [optional] 
**is_setting_editable** | **bool** | Is the setting editable at the current scope | 
**allowed_scopes** | **list[str]** | List of scopes where the setting is available | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

