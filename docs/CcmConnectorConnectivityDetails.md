# CcmConnectorConnectivityDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Connectivity status of a Connector. | [optional] 
**error_summary** | **str** | Summary of errors. | [optional] 
**errors** | [**list[CcmErrorDetail]**](CcmErrorDetail.md) | List of errors and their details. | [optional] 
**tested_at** | **int** | Time at which Test Connection was completed  | [optional] 
**last_tested_at** | **int** |  | [optional] 
**last_connected_at** | **int** | This is the last time at which the Connector was successfully connected. | [optional] 
**last_alert_sent** | **int** | Last alert sent time when connector went down | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

