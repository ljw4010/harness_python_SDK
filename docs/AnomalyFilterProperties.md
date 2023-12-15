# AnomalyFilterProperties

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**k8s_cluster_names** | **list[str]** | This is the list of Cluster Names on which filter will be applied. | [optional] 
**k8s_namespaces** | **list[str]** | This is the list of Namespaces on which filter will be applied. | [optional] 
**k8s_workload_names** | **list[str]** | This is the list of Workload Names on which filter will be applied. | [optional] 
**k8s_service_names** | **list[str]** | This is the list of Service Names on which filter will be applied. | [optional] 
**gcp_projects** | **list[str]** | This is the list of GCP Projects on which filter will be applied. | [optional] 
**gcp_products** | **list[str]** | This is the list of GCP Products on which filter will be applied. | [optional] 
**gcp_sku_descriptions** | **list[str]** | This is the list of GCP SKU Descriptions on which filter will be applied. | [optional] 
**aws_accounts** | **list[str]** | This is the list of AWS Accounts on which filter will be applied. | [optional] 
**aws_services** | **list[str]** | This is the list of AWS Services on which filter will be applied. | [optional] 
**aws_usage_types** | **list[str]** | This is the list of AWS Usage Types on which filter will be applied. | [optional] 
**azure_subscription_guids** | **list[str]** | This is the list of Azure Subscription Guids on which filter will be applied. | [optional] 
**azure_resource_groups** | **list[str]** | This is the list of Azure Resource Groups on which filter will be applied. | [optional] 
**azure_meter_categories** | **list[str]** | This is the list of Azure Meter Categories on which filter will be applied. | [optional] 
**min_actual_amount** | **float** | Fetch anomalies with Actual Amount greater-than or equal-to minActualAmount | [optional] 
**min_anomalous_spend** | **float** | Fetch anomalies with Anomalous Spend greater-than or equal-to minAnomalousSpend | [optional] 
**time_filters** | [**list[CCMTimeFilter]**](CCMTimeFilter.md) | List of filters to be applied on Anomaly Time | [optional] 
**order_by** | [**list[CCMSort]**](CCMSort.md) | The order by condition for anomaly query | [optional] 
**group_by** | [**list[CCMGroupBy]**](CCMGroupBy.md) | The group by clause for anomaly query | [optional] 
**aggregations** | [**list[CCMAggregation]**](CCMAggregation.md) | The aggregations for anomaly query | [optional] 
**search_text** | **list[str]** | The search text entered to filter out rows | [optional] 
**offset** | **int** | Query Offset | [optional] 
**limit** | **int** | Query Limit | [optional] 
**tags** | **dict(str, str)** | Filter tags as a key-value pair. | [optional] 
**filter_type** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

