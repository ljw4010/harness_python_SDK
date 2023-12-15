# Evaluation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | The Harness account in which the evaluation was performed | 
**action** | **str** | The action that triggered evaluation | 
**created** | **int** | The time at which the evaluation was performed in Unix time millseconds | 
**details** | [**list[EvaluationDetail]**](EvaluationDetail.md) | The detailed results of te evaluation | 
**entity** | **str** | An arbtrary user-supplied string that globally identifies the entity under evaluation | 
**entity_metadata** | **str** | Additional arbtrary user-supplied metadta about the entity under evaluation | 
**id** | **int** | The ID of this evaluation | 
**input** | **str** | The input provided at evaluation time | 
**org_id** | **str** | The Harness organisation in which the evaluation was performed | 
**project_id** | **str** | The Harness project in which the evaluation was performed | 
**status** | **str** | The overall status of the evaluation indicating whether it passed | 
**type** | **str** | The types of the entity under evaluation | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

