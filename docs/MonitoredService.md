# MonitoredService

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_identifier** | **str** |  | 
**project_identifier** | **str** |  | 
**identifier** | **str** |  | 
**name** | **str** |  | 
**type** | **str** |  | 
**description** | **str** |  | [optional] 
**service_ref** | **str** |  | 
**environment_ref** | **str** |  | [optional] 
**environment_ref_list** | **list[str]** |  | [optional] 
**tags** | **dict(str, str)** |  | [optional] 
**sources** | [**Sources**](Sources.md) |  | [optional] 
**dependencies** | [**list[ServiceDependencyDTO]**](ServiceDependencyDTO.md) |  | [optional] 
**notification_rule_refs** | [**list[NotificationRuleRefDTO]**](NotificationRuleRefDTO.md) |  | [optional] 
**template** | [**TemplateDTO**](TemplateDTO.md) |  | [optional] 
**enabled** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

