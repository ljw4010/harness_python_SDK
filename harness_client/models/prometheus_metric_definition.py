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

class PrometheusMetricDefinition(object):
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
        'identifier': 'str',
        'metric_name': 'str',
        'risk_profile': 'RiskProfile',
        'analysis': 'AnalysisDTO',
        'sli': 'SLIDTO',
        'query': 'str',
        'group_name': 'str',
        'service_instance_field_name': 'str',
        'prometheus_metric': 'str',
        'service_filter': 'list[PrometheusFilter]',
        'env_filter': 'list[PrometheusFilter]',
        'additional_filters': 'list[PrometheusFilter]',
        'aggregation': 'str',
        'is_manual_query': 'bool'
    }

    attribute_map = {
        'identifier': 'identifier',
        'metric_name': 'metricName',
        'risk_profile': 'riskProfile',
        'analysis': 'analysis',
        'sli': 'sli',
        'query': 'query',
        'group_name': 'groupName',
        'service_instance_field_name': 'serviceInstanceFieldName',
        'prometheus_metric': 'prometheusMetric',
        'service_filter': 'serviceFilter',
        'env_filter': 'envFilter',
        'additional_filters': 'additionalFilters',
        'aggregation': 'aggregation',
        'is_manual_query': 'isManualQuery'
    }

    def __init__(self, identifier=None, metric_name=None, risk_profile=None, analysis=None, sli=None, query=None, group_name=None, service_instance_field_name=None, prometheus_metric=None, service_filter=None, env_filter=None, additional_filters=None, aggregation=None, is_manual_query=None):  # noqa: E501
        """PrometheusMetricDefinition - a model defined in Swagger"""  # noqa: E501
        self._identifier = None
        self._metric_name = None
        self._risk_profile = None
        self._analysis = None
        self._sli = None
        self._query = None
        self._group_name = None
        self._service_instance_field_name = None
        self._prometheus_metric = None
        self._service_filter = None
        self._env_filter = None
        self._additional_filters = None
        self._aggregation = None
        self._is_manual_query = None
        self.discriminator = None
        self.identifier = identifier
        self.metric_name = metric_name
        if risk_profile is not None:
            self.risk_profile = risk_profile
        if analysis is not None:
            self.analysis = analysis
        if sli is not None:
            self.sli = sli
        if query is not None:
            self.query = query
        if group_name is not None:
            self.group_name = group_name
        if service_instance_field_name is not None:
            self.service_instance_field_name = service_instance_field_name
        if prometheus_metric is not None:
            self.prometheus_metric = prometheus_metric
        if service_filter is not None:
            self.service_filter = service_filter
        if env_filter is not None:
            self.env_filter = env_filter
        if additional_filters is not None:
            self.additional_filters = additional_filters
        if aggregation is not None:
            self.aggregation = aggregation
        if is_manual_query is not None:
            self.is_manual_query = is_manual_query

    @property
    def identifier(self):
        """Gets the identifier of this PrometheusMetricDefinition.  # noqa: E501


        :return: The identifier of this PrometheusMetricDefinition.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this PrometheusMetricDefinition.


        :param identifier: The identifier of this PrometheusMetricDefinition.  # noqa: E501
        :type: str
        """
        if identifier is None:
            raise ValueError("Invalid value for `identifier`, must not be `None`")  # noqa: E501

        self._identifier = identifier

    @property
    def metric_name(self):
        """Gets the metric_name of this PrometheusMetricDefinition.  # noqa: E501


        :return: The metric_name of this PrometheusMetricDefinition.  # noqa: E501
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """Sets the metric_name of this PrometheusMetricDefinition.


        :param metric_name: The metric_name of this PrometheusMetricDefinition.  # noqa: E501
        :type: str
        """
        if metric_name is None:
            raise ValueError("Invalid value for `metric_name`, must not be `None`")  # noqa: E501

        self._metric_name = metric_name

    @property
    def risk_profile(self):
        """Gets the risk_profile of this PrometheusMetricDefinition.  # noqa: E501


        :return: The risk_profile of this PrometheusMetricDefinition.  # noqa: E501
        :rtype: RiskProfile
        """
        return self._risk_profile

    @risk_profile.setter
    def risk_profile(self, risk_profile):
        """Sets the risk_profile of this PrometheusMetricDefinition.


        :param risk_profile: The risk_profile of this PrometheusMetricDefinition.  # noqa: E501
        :type: RiskProfile
        """

        self._risk_profile = risk_profile

    @property
    def analysis(self):
        """Gets the analysis of this PrometheusMetricDefinition.  # noqa: E501


        :return: The analysis of this PrometheusMetricDefinition.  # noqa: E501
        :rtype: AnalysisDTO
        """
        return self._analysis

    @analysis.setter
    def analysis(self, analysis):
        """Sets the analysis of this PrometheusMetricDefinition.


        :param analysis: The analysis of this PrometheusMetricDefinition.  # noqa: E501
        :type: AnalysisDTO
        """

        self._analysis = analysis

    @property
    def sli(self):
        """Gets the sli of this PrometheusMetricDefinition.  # noqa: E501


        :return: The sli of this PrometheusMetricDefinition.  # noqa: E501
        :rtype: SLIDTO
        """
        return self._sli

    @sli.setter
    def sli(self, sli):
        """Sets the sli of this PrometheusMetricDefinition.


        :param sli: The sli of this PrometheusMetricDefinition.  # noqa: E501
        :type: SLIDTO
        """

        self._sli = sli

    @property
    def query(self):
        """Gets the query of this PrometheusMetricDefinition.  # noqa: E501


        :return: The query of this PrometheusMetricDefinition.  # noqa: E501
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this PrometheusMetricDefinition.


        :param query: The query of this PrometheusMetricDefinition.  # noqa: E501
        :type: str
        """

        self._query = query

    @property
    def group_name(self):
        """Gets the group_name of this PrometheusMetricDefinition.  # noqa: E501


        :return: The group_name of this PrometheusMetricDefinition.  # noqa: E501
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this PrometheusMetricDefinition.


        :param group_name: The group_name of this PrometheusMetricDefinition.  # noqa: E501
        :type: str
        """

        self._group_name = group_name

    @property
    def service_instance_field_name(self):
        """Gets the service_instance_field_name of this PrometheusMetricDefinition.  # noqa: E501


        :return: The service_instance_field_name of this PrometheusMetricDefinition.  # noqa: E501
        :rtype: str
        """
        return self._service_instance_field_name

    @service_instance_field_name.setter
    def service_instance_field_name(self, service_instance_field_name):
        """Sets the service_instance_field_name of this PrometheusMetricDefinition.


        :param service_instance_field_name: The service_instance_field_name of this PrometheusMetricDefinition.  # noqa: E501
        :type: str
        """

        self._service_instance_field_name = service_instance_field_name

    @property
    def prometheus_metric(self):
        """Gets the prometheus_metric of this PrometheusMetricDefinition.  # noqa: E501


        :return: The prometheus_metric of this PrometheusMetricDefinition.  # noqa: E501
        :rtype: str
        """
        return self._prometheus_metric

    @prometheus_metric.setter
    def prometheus_metric(self, prometheus_metric):
        """Sets the prometheus_metric of this PrometheusMetricDefinition.


        :param prometheus_metric: The prometheus_metric of this PrometheusMetricDefinition.  # noqa: E501
        :type: str
        """

        self._prometheus_metric = prometheus_metric

    @property
    def service_filter(self):
        """Gets the service_filter of this PrometheusMetricDefinition.  # noqa: E501


        :return: The service_filter of this PrometheusMetricDefinition.  # noqa: E501
        :rtype: list[PrometheusFilter]
        """
        return self._service_filter

    @service_filter.setter
    def service_filter(self, service_filter):
        """Sets the service_filter of this PrometheusMetricDefinition.


        :param service_filter: The service_filter of this PrometheusMetricDefinition.  # noqa: E501
        :type: list[PrometheusFilter]
        """

        self._service_filter = service_filter

    @property
    def env_filter(self):
        """Gets the env_filter of this PrometheusMetricDefinition.  # noqa: E501


        :return: The env_filter of this PrometheusMetricDefinition.  # noqa: E501
        :rtype: list[PrometheusFilter]
        """
        return self._env_filter

    @env_filter.setter
    def env_filter(self, env_filter):
        """Sets the env_filter of this PrometheusMetricDefinition.


        :param env_filter: The env_filter of this PrometheusMetricDefinition.  # noqa: E501
        :type: list[PrometheusFilter]
        """

        self._env_filter = env_filter

    @property
    def additional_filters(self):
        """Gets the additional_filters of this PrometheusMetricDefinition.  # noqa: E501


        :return: The additional_filters of this PrometheusMetricDefinition.  # noqa: E501
        :rtype: list[PrometheusFilter]
        """
        return self._additional_filters

    @additional_filters.setter
    def additional_filters(self, additional_filters):
        """Sets the additional_filters of this PrometheusMetricDefinition.


        :param additional_filters: The additional_filters of this PrometheusMetricDefinition.  # noqa: E501
        :type: list[PrometheusFilter]
        """

        self._additional_filters = additional_filters

    @property
    def aggregation(self):
        """Gets the aggregation of this PrometheusMetricDefinition.  # noqa: E501


        :return: The aggregation of this PrometheusMetricDefinition.  # noqa: E501
        :rtype: str
        """
        return self._aggregation

    @aggregation.setter
    def aggregation(self, aggregation):
        """Sets the aggregation of this PrometheusMetricDefinition.


        :param aggregation: The aggregation of this PrometheusMetricDefinition.  # noqa: E501
        :type: str
        """

        self._aggregation = aggregation

    @property
    def is_manual_query(self):
        """Gets the is_manual_query of this PrometheusMetricDefinition.  # noqa: E501


        :return: The is_manual_query of this PrometheusMetricDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._is_manual_query

    @is_manual_query.setter
    def is_manual_query(self, is_manual_query):
        """Sets the is_manual_query of this PrometheusMetricDefinition.


        :param is_manual_query: The is_manual_query of this PrometheusMetricDefinition.  # noqa: E501
        :type: bool
        """

        self._is_manual_query = is_manual_query

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
        if issubclass(PrometheusMetricDefinition, dict):
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
        if not isinstance(other, PrometheusMetricDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
