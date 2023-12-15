# IPAllowlistConfigValidateResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_for_custom_block** | **bool** | This indicates if given IP Address lies in range of custome IP block or not. | [optional] 
**allowlisted_configs** | [**list[IPAllowlistConfigResponse]**](IPAllowlistConfigResponse.md) | This is the list of IP configs configured in Harness from which IP address is allowed. This is empty in case of custom IP address block.  | [optional] 
**allowed_for_ui** | **bool** | This indicates if a given IP is allowlisted in Harness for UI requests | [optional] 
**allowed_for_api** | **bool** | This indicates if a given IP is allowlisted in Harness for API requests | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

