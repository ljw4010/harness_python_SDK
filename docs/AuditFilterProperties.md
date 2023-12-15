# AuditFilterProperties

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scopes** | [**list[AuditResourceScope]**](AuditResourceScope.md) | List of Resource Scopes | [optional] 
**resources** | [**list[AuditResource]**](AuditResource.md) | List of Resources | [optional] 
**modules** | **list[str]** | List of Module Types | [optional] 
**actions** | **list[str]** | List of Actions | [optional] 
**environments** | [**list[AuditEnvironment]**](AuditEnvironment.md) | List of Environments | [optional] 
**principals** | [**list[AuditPrincipal]**](AuditPrincipal.md) | List of Principals | [optional] 
**static_filter** | **str** | Pre-defined Filter | [optional] 
**start_time** | **int** | Used to specify a start time for retrieving Audit events that occurred at or after the time indicated. | [optional] 
**end_time** | **int** | Used to specify the end time for retrieving Audit events that occurred at or before the time indicated. | [optional] 
**tags** | **dict(str, str)** | Filter tags as a key-value pair. | [optional] 
**filter_type** | **str** | This specifies the corresponding Entity of the filter. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

