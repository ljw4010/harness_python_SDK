# AuthenticationSettingsResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ng_auth_settings** | [**list[NGAuthSettings]**](NGAuthSettings.md) | List of Auth Settings configured for an Account. | [optional] 
**whitelisted_domains** | **list[str]** | List of the whitelisted domains. | [optional] 
**authentication_mechanism** | **str** | Indicates if the Authentication Mechanism is SSO or NON-SSO. | [optional] 
**two_factor_enabled** | **bool** | If Two Factor Authentication is enabled, this value is true. Otherwise, it is false. | [optional] 
**session_timeout_in_minutes** | **int** | Any user of this account will be logged out if there is no activity for this number of minutes | [optional] 
**public_access_enabled** | **bool** | If public access is enabled, this value is true. Otherwise, it is false. | [optional] 
**oauth_enabled** | **bool** | If OAUTH is enabled | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

