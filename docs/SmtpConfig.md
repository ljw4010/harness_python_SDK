# SmtpConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | This is the host of the SMTP server. | 
**port** | **int** | This is the port of the SMTP server. | 
**from_address** | **str** | From address of the email that needs to be send. | [optional] 
**use_ssl** | **bool** | Specify whether or not to use SSL certificate. | [optional] 
**start_tls** | **bool** | Specify whether or not to use TLS. | [optional] 
**username** | **str** | Username credential to authenticate with SMTP server. | [optional] 
**password** | **list[str]** | Password credential to authenticate with SMTP server. | [optional] 
**delegate_selectors** | **list[str]** | List of delegate selectors of delegates used by SMTP server as connectivity mode. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

