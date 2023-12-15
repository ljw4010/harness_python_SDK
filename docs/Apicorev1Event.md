# Apicorev1Event

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional] 
**involved_object** | [**V1ObjectReference**](V1ObjectReference.md) |  | [optional] 
**reason** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**source** | [**V1EventSource**](V1EventSource.md) |  | [optional] 
**first_timestamp** | [**V1Time**](V1Time.md) |  | [optional] 
**last_timestamp** | [**V1Time**](V1Time.md) |  | [optional] 
**count** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**event_time** | [**V1MicroTime**](V1MicroTime.md) |  | [optional] 
**series** | [**V1EventSeries**](V1EventSeries.md) |  | [optional] 
**action** | **str** |  | [optional] 
**related** | [**V1ObjectReference**](V1ObjectReference.md) |  | [optional] 
**reporting_component** | **str** |  | [optional] 
**reporting_instance** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

