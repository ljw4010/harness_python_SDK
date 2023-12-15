# IPAllowlistConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the IP Config defined in Harness | 
**identifier** | **str** | Identifier of the IP Config | 
**description** | **str** | Description of the entity | [optional] 
**enabled** | **bool** | If true, it will allow all the IPs that are part of the config and block others. | [optional] [default to False]
**tags** | **dict(str, str)** | IP Allowlist tags | [optional] 
**allowed_source_type** | [**list[AllowedSourceType]**](AllowedSourceType.md) |  | [optional] 
**ip_address** | **str** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

