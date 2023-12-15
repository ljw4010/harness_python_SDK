# WinRmNTLMSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | This specifies the type of secret | 
**port** | **int** | WinRm port | [optional] [default to 5986]
**domain** | **str** | This is the NTLM domain name | 
**username** | **str** | This is the NTLM user name | 
**password** | **str** | This is the NTLM password | 
**use_ssl** | **bool** | This is the NTLM either to use SSL/https | [optional] [default to True]
**skip_cert_checks** | **bool** | This is the Kerberos either to skip certificate checks | [optional] [default to True]
**use_no_profile** | **bool** | This is the Kerberos powershell runs without loading profile | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

