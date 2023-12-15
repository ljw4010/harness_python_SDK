# GcpKmsConnector

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | ID of the project on GCP. | 
**region** | **str** | Region for GCP KMS | 
**key_ring** | **str** | Name of the Key Ring where Google Cloud Symmetric Key is created. | 
**key_name** | **str** | Name of the Google Cloud Symmetric Key. | 
**credentials** | **str** | File Secret which is Service Account Key. | 
**delegate_selectors** | **list[str]** | List of Delegate Selectors that belong to the same Delegate and are used to connect to the Secret Manager. | [optional] 
**default** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

