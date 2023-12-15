# KerberosWinRmConfigDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**principal** | **str** | This is the authorization role, the user/service has in the realm. | 
**realm** | **str** | Name of the Realm. | 
**tgt_generation_method** | **str** |  | [optional] 
**spec** | [**TGTGenerationSpecDTO**](TGTGenerationSpecDTO.md) |  | [optional] 
**use_ssl** | **bool** | This is the Kerberos either to use SSL/https . | [optional] 
**skip_cert_checks** | **bool** | This is the Kerberos either to skip certificate checks . | [optional] 
**use_no_profile** | **bool** | This is the Kerberos powershell runs without loading profile . | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

