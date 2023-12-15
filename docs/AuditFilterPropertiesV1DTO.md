# AuditFilterPropertiesV1DTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter_type** | [**FilterType**](FilterType.md) |  | [optional] 
**tags** | **dict(str, str)** | tags | [optional] 
**start_time** | **int** | Used to specify a start time for retrieving Audit events that occurred at or after the time indicated. | [optional] 
**end_time** | **int** | Used to specify the end time for retrieving Audit events that occurred at or before the time indicated. | [optional] 
**modules** | [**list[ModuleType1]**](ModuleType1.md) | List of Module Types | [optional] 
**actions** | [**list[Action]**](Action.md) | List of Actions | [optional] 
**resources** | [**list[ResourceDTO]**](ResourceDTO.md) | List of Resources | [optional] 
**scopes** | [**list[ResourceScopeDTO]**](ResourceScopeDTO.md) | List of Resource Scopes | [optional] 
**principals** | [**list[Principal1]**](Principal1.md) |  | [optional] 
**static_filter** | [**list[StaticAuditFilter]**](StaticAuditFilter.md) |  | [optional] 
**environments** | [**list[Environment]**](Environment.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

