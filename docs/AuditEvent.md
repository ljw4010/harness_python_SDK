# AuditEvent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audit_id** | **str** | Identifier of the Audit. | [optional] 
**insert_id** | **str** | Insert Identifier of the Audit. | 
**resource_scope** | [**AuditResourceScope**](AuditResourceScope.md) |  | 
**http_request_info** | [**AuditHttpRequestInfo**](AuditHttpRequestInfo.md) |  | [optional] 
**request_metadata** | [**AuditRequestMetadata**](AuditRequestMetadata.md) |  | [optional] 
**timestamp** | **int** |  | 
**authentication_info** | [**AuthenticationInfo**](AuthenticationInfo.md) |  | 
**module** | **str** | Type of module associated with the Audit. | 
**environment** | [**AuditEnvironment**](AuditEnvironment.md) |  | [optional] 
**resource** | [**AuditResource**](AuditResource.md) |  | 
**yaml_diff_record** | [**YamlDiffRecord**](YamlDiffRecord.md) |  | [optional] 
**action** | **str** | Action type associated with the Audit. | 
**audit_event_data** | [**AuditEventData**](AuditEventData.md) |  | [optional] 
**internal_info** | **dict(str, str)** | Internal information. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

