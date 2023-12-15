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

class ClusterCostDetailsQueryParams(object):
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
        'aggregations': 'list[CCMAggregation]',
        'filters': 'list[FieldFilter]',
        'group_by': 'list[str]',
        'time_resolution': 'str',
        'limit': 'int',
        'sort_order': 'str',
        'offset': 'int',
        'skip_round_off': 'bool',
        'selected_labels': 'list[str]'
    }

    attribute_map = {
        'aggregations': 'aggregations',
        'filters': 'filters',
        'group_by': 'groupBy',
        'time_resolution': 'timeResolution',
        'limit': 'limit',
        'sort_order': 'sortOrder',
        'offset': 'offset',
        'skip_round_off': 'skipRoundOff',
        'selected_labels': 'selectedLabels'
    }

    def __init__(self, aggregations=None, filters=None, group_by=None, time_resolution=None, limit=None, sort_order=None, offset=None, skip_round_off=None, selected_labels=None):  # noqa: E501
        """ClusterCostDetailsQueryParams - a model defined in Swagger"""  # noqa: E501
        self._aggregations = None
        self._filters = None
        self._group_by = None
        self._time_resolution = None
        self._limit = None
        self._sort_order = None
        self._offset = None
        self._skip_round_off = None
        self._selected_labels = None
        self.discriminator = None
        if aggregations is not None:
            self.aggregations = aggregations
        if filters is not None:
            self.filters = filters
        if group_by is not None:
            self.group_by = group_by
        if time_resolution is not None:
            self.time_resolution = time_resolution
        if limit is not None:
            self.limit = limit
        if sort_order is not None:
            self.sort_order = sort_order
        if offset is not None:
            self.offset = offset
        if skip_round_off is not None:
            self.skip_round_off = skip_round_off
        if selected_labels is not None:
            self.selected_labels = selected_labels

    @property
    def aggregations(self):
        """Gets the aggregations of this ClusterCostDetailsQueryParams.  # noqa: E501

        Fields which will be aggregated in the response  # noqa: E501

        :return: The aggregations of this ClusterCostDetailsQueryParams.  # noqa: E501
        :rtype: list[CCMAggregation]
        """
        return self._aggregations

    @aggregations.setter
    def aggregations(self, aggregations):
        """Sets the aggregations of this ClusterCostDetailsQueryParams.

        Fields which will be aggregated in the response  # noqa: E501

        :param aggregations: The aggregations of this ClusterCostDetailsQueryParams.  # noqa: E501
        :type: list[CCMAggregation]
        """

        self._aggregations = aggregations

    @property
    def filters(self):
        """Gets the filters of this ClusterCostDetailsQueryParams.  # noqa: E501

        Filters to be applied on the response.  # noqa: E501

        :return: The filters of this ClusterCostDetailsQueryParams.  # noqa: E501
        :rtype: list[FieldFilter]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this ClusterCostDetailsQueryParams.

        Filters to be applied on the response.  # noqa: E501

        :param filters: The filters of this ClusterCostDetailsQueryParams.  # noqa: E501
        :type: list[FieldFilter]
        """

        self._filters = filters

    @property
    def group_by(self):
        """Gets the group_by of this ClusterCostDetailsQueryParams.  # noqa: E501

        Fields on which the response will be grouped by.  # noqa: E501

        :return: The group_by of this ClusterCostDetailsQueryParams.  # noqa: E501
        :rtype: list[str]
        """
        return self._group_by

    @group_by.setter
    def group_by(self, group_by):
        """Sets the group_by of this ClusterCostDetailsQueryParams.

        Fields on which the response will be grouped by.  # noqa: E501

        :param group_by: The group_by of this ClusterCostDetailsQueryParams.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["PERSPECTIVE_ID", "ANOMALY_ID", "WORKLOAD", "WORKLOAD_TYPE", "CLUSTER_ID", "CLUSTER_NAME", "CLUSTER_NAMESPACE", "CLUSTER_NAMESPACE_ID", "CLUSTER_WORKLOAD", "CLUSTER_WORKLOAD_ID", "CLUSTER_NODE", "CLUSTER_POD", "CLUSTER_PARENT_INSTANCE_ID", "CLUSTER_STORAGE", "CLUSTER_APPLICATION", "CLUSTER_ENVIRONMENT", "CLUSTER_SERVICE", "CLUSTER_CLOUD_PROVIDER", "CLUSTER_ECS_SERVICE", "CLUSTER_ECS_SERVICE_ID", "CLUSTER_ECS_TASK", "CLUSTER_ECS_TASK_ID", "CLUSTER_ECS_LAUNCH_TYPE", "CLUSTER_ECS_LAUNCH_TYPE_ID", "NAMESPACE", "SERVICE", "SERVICE_NAME", "GCP_PRODUCT", "GCP_PROJECT", "GCP_SKU_ID", "GCP_SKU_DESCRIPTION", "AWS_ACCOUNT", "AWS_SERVICE", "AWS_INSTANCE_TYPE", "AWS_USAGE_TYPE", "AWS_BILLING_ENTITY", "AWS_LINE_ITEM_TYPE", "AZURE_SUBSCRIPTION_GUID", "AZURE_METER_NAME", "AZURE_METER_CATEGORY", "AZURE_METER_SUBCATEGORY", "AZURE_RESOURCE_ID", "AZURE_RESOURCE_GROUP_NAME", "AZURE_RESOURCE_TYPE", "AZURE_RESOURCE", "AZURE_SERVICE_NAME", "AZURE_SERVICE_TIER", "AZURE_INSTANCE_ID", "AZURE_SUBSCRIPTION_NAME", "AZURE_PUBLISHER_NAME", "AZURE_PUBLISHER_TYPE", "AZURE_RESERVATION_ID", "AZURE_RESERVATION_NAME", "AZURE_FREQUENCY", "COMMON_PRODUCT", "COMMON_REGION", "COMMON_NONE", "CLOUD_PROVIDER", "STATUS", "REGION", "ANOMALY_TIME", "ACTUAL_COST", "EXPECTED_COST", "ANOMALOUS_SPEND", "COST_IMPACT", "TOTAL_COST", "IDLE_COST", "UNALLOCATED_COST", "ALL", "RULE_NAME", "RULE_SET_NAME"]  # noqa: E501
        if not set(group_by).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `group_by` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(group_by) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._group_by = group_by

    @property
    def time_resolution(self):
        """Gets the time_resolution of this ClusterCostDetailsQueryParams.  # noqa: E501

        Only applicable for Time Series Endpoints, defaults to DAY  # noqa: E501

        :return: The time_resolution of this ClusterCostDetailsQueryParams.  # noqa: E501
        :rtype: str
        """
        return self._time_resolution

    @time_resolution.setter
    def time_resolution(self, time_resolution):
        """Sets the time_resolution of this ClusterCostDetailsQueryParams.

        Only applicable for Time Series Endpoints, defaults to DAY  # noqa: E501

        :param time_resolution: The time_resolution of this ClusterCostDetailsQueryParams.  # noqa: E501
        :type: str
        """
        allowed_values = ["HOUR", "DAY", "MONTH", "WEEK", "QUARTER", "YEAR"]  # noqa: E501
        if time_resolution not in allowed_values:
            raise ValueError(
                "Invalid value for `time_resolution` ({0}), must be one of {1}"  # noqa: E501
                .format(time_resolution, allowed_values)
            )

        self._time_resolution = time_resolution

    @property
    def limit(self):
        """Gets the limit of this ClusterCostDetailsQueryParams.  # noqa: E501

        Limit on the number of cost values returned, 0 by default.  # noqa: E501

        :return: The limit of this ClusterCostDetailsQueryParams.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ClusterCostDetailsQueryParams.

        Limit on the number of cost values returned, 0 by default.  # noqa: E501

        :param limit: The limit of this ClusterCostDetailsQueryParams.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def sort_order(self):
        """Gets the sort_order of this ClusterCostDetailsQueryParams.  # noqa: E501

        Order of sorting on cost, Descending by default.  # noqa: E501

        :return: The sort_order of this ClusterCostDetailsQueryParams.  # noqa: E501
        :rtype: str
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this ClusterCostDetailsQueryParams.

        Order of sorting on cost, Descending by default.  # noqa: E501

        :param sort_order: The sort_order of this ClusterCostDetailsQueryParams.  # noqa: E501
        :type: str
        """
        allowed_values = ["ASCENDING", "DESCENDING"]  # noqa: E501
        if sort_order not in allowed_values:
            raise ValueError(
                "Invalid value for `sort_order` ({0}), must be one of {1}"  # noqa: E501
                .format(sort_order, allowed_values)
            )

        self._sort_order = sort_order

    @property
    def offset(self):
        """Gets the offset of this ClusterCostDetailsQueryParams.  # noqa: E501

        Offset on the cost values returned, 10 by default.  # noqa: E501

        :return: The offset of this ClusterCostDetailsQueryParams.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ClusterCostDetailsQueryParams.

        Offset on the cost values returned, 10 by default.  # noqa: E501

        :param offset: The offset of this ClusterCostDetailsQueryParams.  # noqa: E501
        :type: int
        """

        self._offset = offset

    @property
    def skip_round_off(self):
        """Gets the skip_round_off of this ClusterCostDetailsQueryParams.  # noqa: E501

        Skip Rounding off the cost values returned, false by default.  # noqa: E501

        :return: The skip_round_off of this ClusterCostDetailsQueryParams.  # noqa: E501
        :rtype: bool
        """
        return self._skip_round_off

    @skip_round_off.setter
    def skip_round_off(self, skip_round_off):
        """Sets the skip_round_off of this ClusterCostDetailsQueryParams.

        Skip Rounding off the cost values returned, false by default.  # noqa: E501

        :param skip_round_off: The skip_round_off of this ClusterCostDetailsQueryParams.  # noqa: E501
        :type: bool
        """

        self._skip_round_off = skip_round_off

    @property
    def selected_labels(self):
        """Gets the selected_labels of this ClusterCostDetailsQueryParams.  # noqa: E501

        The response will contain values corresponding to these labels  # noqa: E501

        :return: The selected_labels of this ClusterCostDetailsQueryParams.  # noqa: E501
        :rtype: list[str]
        """
        return self._selected_labels

    @selected_labels.setter
    def selected_labels(self, selected_labels):
        """Sets the selected_labels of this ClusterCostDetailsQueryParams.

        The response will contain values corresponding to these labels  # noqa: E501

        :param selected_labels: The selected_labels of this ClusterCostDetailsQueryParams.  # noqa: E501
        :type: list[str]
        """

        self._selected_labels = selected_labels

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
        if issubclass(ClusterCostDetailsQueryParams, dict):
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
        if not isinstance(other, ClusterCostDetailsQueryParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
