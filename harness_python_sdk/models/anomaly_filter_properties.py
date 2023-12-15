# coding: utf-8

"""
    Harness NextGen Software Delivery Platform API Reference

    The Harness Software Delivery Platform uses OpenAPI Specification v3.0. Harness constantly improves these APIs. Please be aware that some improvements could cause breaking changes. # Introduction     The Harness API allows you to integrate and use all the services and modules we provide on the Harness Platform. If you use client-side SDKs, Harness functionality can be integrated with your client-side automation, helping you reduce manual efforts and deploy code faster.    For more information about how Harness works, read our [documentation](https://developer.harness.io/docs/getting-started) or visit the [Harness Developer Hub](https://developer.harness.io/).  ## How it works    The Harness API is a RESTful API that uses standard HTTP verbs. You can send requests in JSON, YAML, or form-data format. The format of the response matches the format of your request. You must send a single request at a time and ensure that you include your authentication key. For more information about this, go to [Authentication](#section/Introduction/Authentication).  ## Get started    Before you start integrating, get to know our API better by reading the following topics:    * [Harness key concepts](https://developer.harness.io/docs/getting-started/learn-harness-key-concepts/)   * [Authentication](#section/Introduction/Authentication)   * [Requests and responses](#section/Introduction/Requests-and-Responses)   * [Common Parameters](#section/Introduction/Common-Parameters-Beta)   * [Status Codes](#section/Introduction/Status-Codes)   * [Errors](#tag/Error-Response)   * [Versioning](#section/Introduction/Versioning-Beta)   * [Pagination](/#section/Introduction/Pagination-Beta)    The methods you need to integrate with depend on the functionality you want to use. Work with  your Harness Solutions Engineer to determine which methods you need.  ## Authentication  To authenticate with the Harness API, you need to:   1. Generate an API token on the Harness Platform.   2. Send the API token you generate in the `x-api-key` header in each request.  ### Generate an API token  To generate an API token, complete the following steps:   1. Go to the [Harness Platform](https://app.harness.io/).   2. On the left-hand navigation, click **My Profile**.   3. Click **+API Key**, enter a name for your key and then click **Save**.   4. Within the API Key tile, click **+Token**.   5. Enter a name for your token and click **Generate Token**. **Important**: Make sure to save your token securely. Harness does not store the API token for future reference, so make sure to save your token securely before you leave the page.  ### Send the API token in your requests  Send the token you created in the Harness Platform in the x-api-key header. For example:   `x-api-key: YOUR_API_KEY_HERE`  ## Requests and Responses    The structure for each request and response is outlined in the API documentation. We have examples in JSON and YAML for every request and response. You can use our online editor to test the examples.  ## Common Parameters [Beta]  | Field Name | Type    | Default | Description    | |------------|---------|---------|----------------| | identifier | string  | none    | URL-friendly version of the name, used to identify a resource within it's scope and so needs to be unique within the scope.                                                                                                            | | name       | string  | none    | Human-friendly name for the resource.                                                                                       | | org        | string  | none    | Limit to provided org identifiers.                                                                                                                     | | project    | string  | none    | Limit to provided project identifiers.                                                                                                                 | | description| string  | none    | More information about the specific resource.                                                                                    | | tags       | map[string]string  | none    | List of labels applied to the resource.                                                                                                                         | | order      | string  | desc    | Order to use when sorting the specified fields. Type: enum(asc,desc).                                                                                                                                     | | sort       | string  | none    | Fields on which to sort. Note: Specify the fields that you want to use for sorting. When doing so, consider the operational overhead of sorting fields. | | limit      | int     | 30      | Pagination: Number of items to return.                                                                                                                 | | page       | int     | 1       | Pagination page number strategy: Specify the page number within the paginated collection related to the number of items in each page.                  | | created    | int64   | none    | Unix timestamp that shows when the resource was created (in milliseconds).                                                               | | updated    | int64   | none    | Unix timestamp that shows when the resource was last edited (in milliseconds).                                                           |   ## Status Codes    Harness uses conventional HTTP status codes to indicate the status of an API request.    Generally, 2xx responses are reserved for success and 4xx status codes are reserved for failures. A 5xx response code indicates an error on the Harness server.    | Error Code  | Description |   |-------------|-------------|   | 200         |     OK      |   | 201         |   Created   |   | 202         |   Accepted  |   | 204         |  No Content |   | 400         | Bad Request |   | 401         | Unauthorized |   | 403         | Forbidden |   | 412         | Precondition Failed |   | 415         | Unsupported Media Type |   | 500         | Server Error |    To view our error response structures, go [here](#tag/Error-Response).  ## Versioning [Beta]  ### Harness Version   The current version of our Beta APIs is yet to be announced. The version number will use the date-header format and will be valid only for our Beta APIs.  ### Generation   All our beta APIs are versioned as a Generation, and this version is included in the path to every API resource. For example, v1 beta APIs begin with `app.harness.io/v1/`, where v1 is the API Generation.    The version number represents the core API and does not change frequently. The version number changes only if there is a significant departure from the basic underpinnings of the existing API. For example, when Harness performs a system-wide refactoring of core concepts or resources.  ## Pagination [Beta]  We use pagination to place limits on the number of responses associated with list endpoints. Pagination is achieved by the use of limit query parameters. The limit defaults to 30. Its maximum value is 100.  Following are the pagination headers supported in the response bodies of paginated APIs:   1. X-Total-Elements : Indicates the total number of entries in a paginated response.   2. X-Page-Number : Indicates the page number currently returned for a paginated response.   3. X-Page-Size : Indicates the number of entries per page for a paginated response.  For example:    ``` X-Total-Elements : 30 X-Page-Number : 0 X-Page-Size : 10   ```   # noqa: E501

    OpenAPI spec version: 1.0
    Contact: contact@harness.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AnomalyFilterProperties(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'k8s_cluster_names': 'list[str]',
        'k8s_namespaces': 'list[str]',
        'k8s_workload_names': 'list[str]',
        'k8s_service_names': 'list[str]',
        'gcp_projects': 'list[str]',
        'gcp_products': 'list[str]',
        'gcp_sku_descriptions': 'list[str]',
        'aws_accounts': 'list[str]',
        'aws_services': 'list[str]',
        'aws_usage_types': 'list[str]',
        'azure_subscription_guids': 'list[str]',
        'azure_resource_groups': 'list[str]',
        'azure_meter_categories': 'list[str]',
        'min_actual_amount': 'float',
        'min_anomalous_spend': 'float',
        'time_filters': 'list[CCMTimeFilter]',
        'order_by': 'list[CCMSort]',
        'group_by': 'list[CCMGroupBy]',
        'aggregations': 'list[CCMAggregation]',
        'search_text': 'list[str]',
        'offset': 'int',
        'limit': 'int',
        'tags': 'dict(str, str)',
        'filter_type': 'str'
    }

    attribute_map = {
        'k8s_cluster_names': 'k8sClusterNames',
        'k8s_namespaces': 'k8sNamespaces',
        'k8s_workload_names': 'k8sWorkloadNames',
        'k8s_service_names': 'k8sServiceNames',
        'gcp_projects': 'gcpProjects',
        'gcp_products': 'gcpProducts',
        'gcp_sku_descriptions': 'gcpSKUDescriptions',
        'aws_accounts': 'awsAccounts',
        'aws_services': 'awsServices',
        'aws_usage_types': 'awsUsageTypes',
        'azure_subscription_guids': 'azureSubscriptionGuids',
        'azure_resource_groups': 'azureResourceGroups',
        'azure_meter_categories': 'azureMeterCategories',
        'min_actual_amount': 'minActualAmount',
        'min_anomalous_spend': 'minAnomalousSpend',
        'time_filters': 'timeFilters',
        'order_by': 'orderBy',
        'group_by': 'groupBy',
        'aggregations': 'aggregations',
        'search_text': 'searchText',
        'offset': 'offset',
        'limit': 'limit',
        'tags': 'tags',
        'filter_type': 'filterType'
    }

    def __init__(self, k8s_cluster_names=None, k8s_namespaces=None, k8s_workload_names=None, k8s_service_names=None, gcp_projects=None, gcp_products=None, gcp_sku_descriptions=None, aws_accounts=None, aws_services=None, aws_usage_types=None, azure_subscription_guids=None, azure_resource_groups=None, azure_meter_categories=None, min_actual_amount=None, min_anomalous_spend=None, time_filters=None, order_by=None, group_by=None, aggregations=None, search_text=None, offset=None, limit=None, tags=None, filter_type=None):  # noqa: E501
        """AnomalyFilterProperties - a model defined in Swagger"""  # noqa: E501
        self._k8s_cluster_names = None
        self._k8s_namespaces = None
        self._k8s_workload_names = None
        self._k8s_service_names = None
        self._gcp_projects = None
        self._gcp_products = None
        self._gcp_sku_descriptions = None
        self._aws_accounts = None
        self._aws_services = None
        self._aws_usage_types = None
        self._azure_subscription_guids = None
        self._azure_resource_groups = None
        self._azure_meter_categories = None
        self._min_actual_amount = None
        self._min_anomalous_spend = None
        self._time_filters = None
        self._order_by = None
        self._group_by = None
        self._aggregations = None
        self._search_text = None
        self._offset = None
        self._limit = None
        self._tags = None
        self._filter_type = None
        self.discriminator = None
        if k8s_cluster_names is not None:
            self.k8s_cluster_names = k8s_cluster_names
        if k8s_namespaces is not None:
            self.k8s_namespaces = k8s_namespaces
        if k8s_workload_names is not None:
            self.k8s_workload_names = k8s_workload_names
        if k8s_service_names is not None:
            self.k8s_service_names = k8s_service_names
        if gcp_projects is not None:
            self.gcp_projects = gcp_projects
        if gcp_products is not None:
            self.gcp_products = gcp_products
        if gcp_sku_descriptions is not None:
            self.gcp_sku_descriptions = gcp_sku_descriptions
        if aws_accounts is not None:
            self.aws_accounts = aws_accounts
        if aws_services is not None:
            self.aws_services = aws_services
        if aws_usage_types is not None:
            self.aws_usage_types = aws_usage_types
        if azure_subscription_guids is not None:
            self.azure_subscription_guids = azure_subscription_guids
        if azure_resource_groups is not None:
            self.azure_resource_groups = azure_resource_groups
        if azure_meter_categories is not None:
            self.azure_meter_categories = azure_meter_categories
        if min_actual_amount is not None:
            self.min_actual_amount = min_actual_amount
        if min_anomalous_spend is not None:
            self.min_anomalous_spend = min_anomalous_spend
        if time_filters is not None:
            self.time_filters = time_filters
        if order_by is not None:
            self.order_by = order_by
        if group_by is not None:
            self.group_by = group_by
        if aggregations is not None:
            self.aggregations = aggregations
        if search_text is not None:
            self.search_text = search_text
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if tags is not None:
            self.tags = tags
        if filter_type is not None:
            self.filter_type = filter_type

    @property
    def k8s_cluster_names(self):
        """Gets the k8s_cluster_names of this AnomalyFilterProperties.  # noqa: E501

        This is the list of Cluster Names on which filter will be applied.  # noqa: E501

        :return: The k8s_cluster_names of this AnomalyFilterProperties.  # noqa: E501
        :rtype: list[str]
        """
        return self._k8s_cluster_names

    @k8s_cluster_names.setter
    def k8s_cluster_names(self, k8s_cluster_names):
        """Sets the k8s_cluster_names of this AnomalyFilterProperties.

        This is the list of Cluster Names on which filter will be applied.  # noqa: E501

        :param k8s_cluster_names: The k8s_cluster_names of this AnomalyFilterProperties.  # noqa: E501
        :type: list[str]
        """

        self._k8s_cluster_names = k8s_cluster_names

    @property
    def k8s_namespaces(self):
        """Gets the k8s_namespaces of this AnomalyFilterProperties.  # noqa: E501

        This is the list of Namespaces on which filter will be applied.  # noqa: E501

        :return: The k8s_namespaces of this AnomalyFilterProperties.  # noqa: E501
        :rtype: list[str]
        """
        return self._k8s_namespaces

    @k8s_namespaces.setter
    def k8s_namespaces(self, k8s_namespaces):
        """Sets the k8s_namespaces of this AnomalyFilterProperties.

        This is the list of Namespaces on which filter will be applied.  # noqa: E501

        :param k8s_namespaces: The k8s_namespaces of this AnomalyFilterProperties.  # noqa: E501
        :type: list[str]
        """

        self._k8s_namespaces = k8s_namespaces

    @property
    def k8s_workload_names(self):
        """Gets the k8s_workload_names of this AnomalyFilterProperties.  # noqa: E501

        This is the list of Workload Names on which filter will be applied.  # noqa: E501

        :return: The k8s_workload_names of this AnomalyFilterProperties.  # noqa: E501
        :rtype: list[str]
        """
        return self._k8s_workload_names

    @k8s_workload_names.setter
    def k8s_workload_names(self, k8s_workload_names):
        """Sets the k8s_workload_names of this AnomalyFilterProperties.

        This is the list of Workload Names on which filter will be applied.  # noqa: E501

        :param k8s_workload_names: The k8s_workload_names of this AnomalyFilterProperties.  # noqa: E501
        :type: list[str]
        """

        self._k8s_workload_names = k8s_workload_names

    @property
    def k8s_service_names(self):
        """Gets the k8s_service_names of this AnomalyFilterProperties.  # noqa: E501

        This is the list of Service Names on which filter will be applied.  # noqa: E501

        :return: The k8s_service_names of this AnomalyFilterProperties.  # noqa: E501
        :rtype: list[str]
        """
        return self._k8s_service_names

    @k8s_service_names.setter
    def k8s_service_names(self, k8s_service_names):
        """Sets the k8s_service_names of this AnomalyFilterProperties.

        This is the list of Service Names on which filter will be applied.  # noqa: E501

        :param k8s_service_names: The k8s_service_names of this AnomalyFilterProperties.  # noqa: E501
        :type: list[str]
        """

        self._k8s_service_names = k8s_service_names

    @property
    def gcp_projects(self):
        """Gets the gcp_projects of this AnomalyFilterProperties.  # noqa: E501

        This is the list of GCP Projects on which filter will be applied.  # noqa: E501

        :return: The gcp_projects of this AnomalyFilterProperties.  # noqa: E501
        :rtype: list[str]
        """
        return self._gcp_projects

    @gcp_projects.setter
    def gcp_projects(self, gcp_projects):
        """Sets the gcp_projects of this AnomalyFilterProperties.

        This is the list of GCP Projects on which filter will be applied.  # noqa: E501

        :param gcp_projects: The gcp_projects of this AnomalyFilterProperties.  # noqa: E501
        :type: list[str]
        """

        self._gcp_projects = gcp_projects

    @property
    def gcp_products(self):
        """Gets the gcp_products of this AnomalyFilterProperties.  # noqa: E501

        This is the list of GCP Products on which filter will be applied.  # noqa: E501

        :return: The gcp_products of this AnomalyFilterProperties.  # noqa: E501
        :rtype: list[str]
        """
        return self._gcp_products

    @gcp_products.setter
    def gcp_products(self, gcp_products):
        """Sets the gcp_products of this AnomalyFilterProperties.

        This is the list of GCP Products on which filter will be applied.  # noqa: E501

        :param gcp_products: The gcp_products of this AnomalyFilterProperties.  # noqa: E501
        :type: list[str]
        """

        self._gcp_products = gcp_products

    @property
    def gcp_sku_descriptions(self):
        """Gets the gcp_sku_descriptions of this AnomalyFilterProperties.  # noqa: E501

        This is the list of GCP SKU Descriptions on which filter will be applied.  # noqa: E501

        :return: The gcp_sku_descriptions of this AnomalyFilterProperties.  # noqa: E501
        :rtype: list[str]
        """
        return self._gcp_sku_descriptions

    @gcp_sku_descriptions.setter
    def gcp_sku_descriptions(self, gcp_sku_descriptions):
        """Sets the gcp_sku_descriptions of this AnomalyFilterProperties.

        This is the list of GCP SKU Descriptions on which filter will be applied.  # noqa: E501

        :param gcp_sku_descriptions: The gcp_sku_descriptions of this AnomalyFilterProperties.  # noqa: E501
        :type: list[str]
        """

        self._gcp_sku_descriptions = gcp_sku_descriptions

    @property
    def aws_accounts(self):
        """Gets the aws_accounts of this AnomalyFilterProperties.  # noqa: E501

        This is the list of AWS Accounts on which filter will be applied.  # noqa: E501

        :return: The aws_accounts of this AnomalyFilterProperties.  # noqa: E501
        :rtype: list[str]
        """
        return self._aws_accounts

    @aws_accounts.setter
    def aws_accounts(self, aws_accounts):
        """Sets the aws_accounts of this AnomalyFilterProperties.

        This is the list of AWS Accounts on which filter will be applied.  # noqa: E501

        :param aws_accounts: The aws_accounts of this AnomalyFilterProperties.  # noqa: E501
        :type: list[str]
        """

        self._aws_accounts = aws_accounts

    @property
    def aws_services(self):
        """Gets the aws_services of this AnomalyFilterProperties.  # noqa: E501

        This is the list of AWS Services on which filter will be applied.  # noqa: E501

        :return: The aws_services of this AnomalyFilterProperties.  # noqa: E501
        :rtype: list[str]
        """
        return self._aws_services

    @aws_services.setter
    def aws_services(self, aws_services):
        """Sets the aws_services of this AnomalyFilterProperties.

        This is the list of AWS Services on which filter will be applied.  # noqa: E501

        :param aws_services: The aws_services of this AnomalyFilterProperties.  # noqa: E501
        :type: list[str]
        """

        self._aws_services = aws_services

    @property
    def aws_usage_types(self):
        """Gets the aws_usage_types of this AnomalyFilterProperties.  # noqa: E501

        This is the list of AWS Usage Types on which filter will be applied.  # noqa: E501

        :return: The aws_usage_types of this AnomalyFilterProperties.  # noqa: E501
        :rtype: list[str]
        """
        return self._aws_usage_types

    @aws_usage_types.setter
    def aws_usage_types(self, aws_usage_types):
        """Sets the aws_usage_types of this AnomalyFilterProperties.

        This is the list of AWS Usage Types on which filter will be applied.  # noqa: E501

        :param aws_usage_types: The aws_usage_types of this AnomalyFilterProperties.  # noqa: E501
        :type: list[str]
        """

        self._aws_usage_types = aws_usage_types

    @property
    def azure_subscription_guids(self):
        """Gets the azure_subscription_guids of this AnomalyFilterProperties.  # noqa: E501

        This is the list of Azure Subscription Guids on which filter will be applied.  # noqa: E501

        :return: The azure_subscription_guids of this AnomalyFilterProperties.  # noqa: E501
        :rtype: list[str]
        """
        return self._azure_subscription_guids

    @azure_subscription_guids.setter
    def azure_subscription_guids(self, azure_subscription_guids):
        """Sets the azure_subscription_guids of this AnomalyFilterProperties.

        This is the list of Azure Subscription Guids on which filter will be applied.  # noqa: E501

        :param azure_subscription_guids: The azure_subscription_guids of this AnomalyFilterProperties.  # noqa: E501
        :type: list[str]
        """

        self._azure_subscription_guids = azure_subscription_guids

    @property
    def azure_resource_groups(self):
        """Gets the azure_resource_groups of this AnomalyFilterProperties.  # noqa: E501

        This is the list of Azure Resource Groups on which filter will be applied.  # noqa: E501

        :return: The azure_resource_groups of this AnomalyFilterProperties.  # noqa: E501
        :rtype: list[str]
        """
        return self._azure_resource_groups

    @azure_resource_groups.setter
    def azure_resource_groups(self, azure_resource_groups):
        """Sets the azure_resource_groups of this AnomalyFilterProperties.

        This is the list of Azure Resource Groups on which filter will be applied.  # noqa: E501

        :param azure_resource_groups: The azure_resource_groups of this AnomalyFilterProperties.  # noqa: E501
        :type: list[str]
        """

        self._azure_resource_groups = azure_resource_groups

    @property
    def azure_meter_categories(self):
        """Gets the azure_meter_categories of this AnomalyFilterProperties.  # noqa: E501

        This is the list of Azure Meter Categories on which filter will be applied.  # noqa: E501

        :return: The azure_meter_categories of this AnomalyFilterProperties.  # noqa: E501
        :rtype: list[str]
        """
        return self._azure_meter_categories

    @azure_meter_categories.setter
    def azure_meter_categories(self, azure_meter_categories):
        """Sets the azure_meter_categories of this AnomalyFilterProperties.

        This is the list of Azure Meter Categories on which filter will be applied.  # noqa: E501

        :param azure_meter_categories: The azure_meter_categories of this AnomalyFilterProperties.  # noqa: E501
        :type: list[str]
        """

        self._azure_meter_categories = azure_meter_categories

    @property
    def min_actual_amount(self):
        """Gets the min_actual_amount of this AnomalyFilterProperties.  # noqa: E501

        Fetch anomalies with Actual Amount greater-than or equal-to minActualAmount  # noqa: E501

        :return: The min_actual_amount of this AnomalyFilterProperties.  # noqa: E501
        :rtype: float
        """
        return self._min_actual_amount

    @min_actual_amount.setter
    def min_actual_amount(self, min_actual_amount):
        """Sets the min_actual_amount of this AnomalyFilterProperties.

        Fetch anomalies with Actual Amount greater-than or equal-to minActualAmount  # noqa: E501

        :param min_actual_amount: The min_actual_amount of this AnomalyFilterProperties.  # noqa: E501
        :type: float
        """

        self._min_actual_amount = min_actual_amount

    @property
    def min_anomalous_spend(self):
        """Gets the min_anomalous_spend of this AnomalyFilterProperties.  # noqa: E501

        Fetch anomalies with Anomalous Spend greater-than or equal-to minAnomalousSpend  # noqa: E501

        :return: The min_anomalous_spend of this AnomalyFilterProperties.  # noqa: E501
        :rtype: float
        """
        return self._min_anomalous_spend

    @min_anomalous_spend.setter
    def min_anomalous_spend(self, min_anomalous_spend):
        """Sets the min_anomalous_spend of this AnomalyFilterProperties.

        Fetch anomalies with Anomalous Spend greater-than or equal-to minAnomalousSpend  # noqa: E501

        :param min_anomalous_spend: The min_anomalous_spend of this AnomalyFilterProperties.  # noqa: E501
        :type: float
        """

        self._min_anomalous_spend = min_anomalous_spend

    @property
    def time_filters(self):
        """Gets the time_filters of this AnomalyFilterProperties.  # noqa: E501

        List of filters to be applied on Anomaly Time  # noqa: E501

        :return: The time_filters of this AnomalyFilterProperties.  # noqa: E501
        :rtype: list[CCMTimeFilter]
        """
        return self._time_filters

    @time_filters.setter
    def time_filters(self, time_filters):
        """Sets the time_filters of this AnomalyFilterProperties.

        List of filters to be applied on Anomaly Time  # noqa: E501

        :param time_filters: The time_filters of this AnomalyFilterProperties.  # noqa: E501
        :type: list[CCMTimeFilter]
        """

        self._time_filters = time_filters

    @property
    def order_by(self):
        """Gets the order_by of this AnomalyFilterProperties.  # noqa: E501

        The order by condition for anomaly query  # noqa: E501

        :return: The order_by of this AnomalyFilterProperties.  # noqa: E501
        :rtype: list[CCMSort]
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        """Sets the order_by of this AnomalyFilterProperties.

        The order by condition for anomaly query  # noqa: E501

        :param order_by: The order_by of this AnomalyFilterProperties.  # noqa: E501
        :type: list[CCMSort]
        """

        self._order_by = order_by

    @property
    def group_by(self):
        """Gets the group_by of this AnomalyFilterProperties.  # noqa: E501

        The group by clause for anomaly query  # noqa: E501

        :return: The group_by of this AnomalyFilterProperties.  # noqa: E501
        :rtype: list[CCMGroupBy]
        """
        return self._group_by

    @group_by.setter
    def group_by(self, group_by):
        """Sets the group_by of this AnomalyFilterProperties.

        The group by clause for anomaly query  # noqa: E501

        :param group_by: The group_by of this AnomalyFilterProperties.  # noqa: E501
        :type: list[CCMGroupBy]
        """

        self._group_by = group_by

    @property
    def aggregations(self):
        """Gets the aggregations of this AnomalyFilterProperties.  # noqa: E501

        The aggregations for anomaly query  # noqa: E501

        :return: The aggregations of this AnomalyFilterProperties.  # noqa: E501
        :rtype: list[CCMAggregation]
        """
        return self._aggregations

    @aggregations.setter
    def aggregations(self, aggregations):
        """Sets the aggregations of this AnomalyFilterProperties.

        The aggregations for anomaly query  # noqa: E501

        :param aggregations: The aggregations of this AnomalyFilterProperties.  # noqa: E501
        :type: list[CCMAggregation]
        """

        self._aggregations = aggregations

    @property
    def search_text(self):
        """Gets the search_text of this AnomalyFilterProperties.  # noqa: E501

        The search text entered to filter out rows  # noqa: E501

        :return: The search_text of this AnomalyFilterProperties.  # noqa: E501
        :rtype: list[str]
        """
        return self._search_text

    @search_text.setter
    def search_text(self, search_text):
        """Sets the search_text of this AnomalyFilterProperties.

        The search text entered to filter out rows  # noqa: E501

        :param search_text: The search_text of this AnomalyFilterProperties.  # noqa: E501
        :type: list[str]
        """

        self._search_text = search_text

    @property
    def offset(self):
        """Gets the offset of this AnomalyFilterProperties.  # noqa: E501

        Query Offset  # noqa: E501

        :return: The offset of this AnomalyFilterProperties.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this AnomalyFilterProperties.

        Query Offset  # noqa: E501

        :param offset: The offset of this AnomalyFilterProperties.  # noqa: E501
        :type: int
        """

        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this AnomalyFilterProperties.  # noqa: E501

        Query Limit  # noqa: E501

        :return: The limit of this AnomalyFilterProperties.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this AnomalyFilterProperties.

        Query Limit  # noqa: E501

        :param limit: The limit of this AnomalyFilterProperties.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def tags(self):
        """Gets the tags of this AnomalyFilterProperties.  # noqa: E501

        Filter tags as a key-value pair.  # noqa: E501

        :return: The tags of this AnomalyFilterProperties.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this AnomalyFilterProperties.

        Filter tags as a key-value pair.  # noqa: E501

        :param tags: The tags of this AnomalyFilterProperties.  # noqa: E501
        :type: dict(str, str)
        """

        self._tags = tags

    @property
    def filter_type(self):
        """Gets the filter_type of this AnomalyFilterProperties.  # noqa: E501


        :return: The filter_type of this AnomalyFilterProperties.  # noqa: E501
        :rtype: str
        """
        return self._filter_type

    @filter_type.setter
    def filter_type(self, filter_type):
        """Sets the filter_type of this AnomalyFilterProperties.


        :param filter_type: The filter_type of this AnomalyFilterProperties.  # noqa: E501
        :type: str
        """
        allowed_values = ["Anomaly"]  # noqa: E501
        if filter_type not in allowed_values:
            raise ValueError(
                "Invalid value for `filter_type` ({0}), must be one of {1}"  # noqa: E501
                .format(filter_type, allowed_values)
            )

        self._filter_type = filter_type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(AnomalyFilterProperties, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AnomalyFilterProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
