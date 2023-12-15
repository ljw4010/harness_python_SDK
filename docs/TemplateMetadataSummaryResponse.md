# TemplateMetadataSummaryResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** | Account identifier | [optional] 
**org** | **str** | Organization identifier | [optional] 
**project** | **str** | Project identifier | [optional] 
**identifier** | **str** | Template identifier | [optional] 
**name** | **str** | Template Name | [optional] 
**description** | **str** | Template description | [optional] 
**tags** | **dict(str, str)** | Template tags | [optional] 
**version_label** | **str** | Version label of template | [optional] 
**entity_type** | **str** | Type of Template  | [optional] 
**child_type** | **str** | Defines child template type | [optional] 
**scope** | **str** | Scope of template | [optional] 
**version** | **int** | Version of template | [optional] 
**git_details** | [**EntityGitDetails**](EntityGitDetails.md) |  | [optional] 
**updated** | **int** | Last modification timestamp for Service.  | [optional] 
**store_type** | **str** | Specifies whether the Entity is to be stored in Git or not (for Git Experience). | [optional] 
**connector_ref** | **str** | Identifier of the Harness Connector used for CRUD operations on the Entity (for Git Experience). | [optional] 
**stable_template** | **bool** | True if this version is stable version of Template | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

