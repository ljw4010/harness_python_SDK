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

class MonitoredServiceListItemDTO(object):
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
        'name': 'str',
        'identifier': 'str',
        'service_ref': 'str',
        'environment_ref': 'str',
        'environment_ref_list': 'list[str]',
        'service_name': 'str',
        'environment_name': 'str',
        'type': 'str',
        'health_monitoring_enabled': 'bool',
        'current_health_score': 'RiskData',
        'dependent_health_score': 'list[RiskData]',
        'historical_trend': 'HistoricalTrend',
        'change_summary': 'ChangeSummaryDTO',
        'tags': 'dict(str, str)',
        'service_monitoring_enabled': 'bool',
        'slo_health_indicators': 'list[SloHealthIndicatorDTO]'
    }

    attribute_map = {
        'name': 'name',
        'identifier': 'identifier',
        'service_ref': 'serviceRef',
        'environment_ref': 'environmentRef',
        'environment_ref_list': 'environmentRefList',
        'service_name': 'serviceName',
        'environment_name': 'environmentName',
        'type': 'type',
        'health_monitoring_enabled': 'healthMonitoringEnabled',
        'current_health_score': 'currentHealthScore',
        'dependent_health_score': 'dependentHealthScore',
        'historical_trend': 'historicalTrend',
        'change_summary': 'changeSummary',
        'tags': 'tags',
        'service_monitoring_enabled': 'serviceMonitoringEnabled',
        'slo_health_indicators': 'sloHealthIndicators'
    }

    def __init__(self, name=None, identifier=None, service_ref=None, environment_ref=None, environment_ref_list=None, service_name=None, environment_name=None, type=None, health_monitoring_enabled=None, current_health_score=None, dependent_health_score=None, historical_trend=None, change_summary=None, tags=None, service_monitoring_enabled=None, slo_health_indicators=None):  # noqa: E501
        """MonitoredServiceListItemDTO - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._identifier = None
        self._service_ref = None
        self._environment_ref = None
        self._environment_ref_list = None
        self._service_name = None
        self._environment_name = None
        self._type = None
        self._health_monitoring_enabled = None
        self._current_health_score = None
        self._dependent_health_score = None
        self._historical_trend = None
        self._change_summary = None
        self._tags = None
        self._service_monitoring_enabled = None
        self._slo_health_indicators = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if identifier is not None:
            self.identifier = identifier
        if service_ref is not None:
            self.service_ref = service_ref
        if environment_ref is not None:
            self.environment_ref = environment_ref
        if environment_ref_list is not None:
            self.environment_ref_list = environment_ref_list
        if service_name is not None:
            self.service_name = service_name
        if environment_name is not None:
            self.environment_name = environment_name
        if type is not None:
            self.type = type
        if health_monitoring_enabled is not None:
            self.health_monitoring_enabled = health_monitoring_enabled
        if current_health_score is not None:
            self.current_health_score = current_health_score
        if dependent_health_score is not None:
            self.dependent_health_score = dependent_health_score
        if historical_trend is not None:
            self.historical_trend = historical_trend
        if change_summary is not None:
            self.change_summary = change_summary
        if tags is not None:
            self.tags = tags
        if service_monitoring_enabled is not None:
            self.service_monitoring_enabled = service_monitoring_enabled
        if slo_health_indicators is not None:
            self.slo_health_indicators = slo_health_indicators

    @property
    def name(self):
        """Gets the name of this MonitoredServiceListItemDTO.  # noqa: E501


        :return: The name of this MonitoredServiceListItemDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MonitoredServiceListItemDTO.


        :param name: The name of this MonitoredServiceListItemDTO.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def identifier(self):
        """Gets the identifier of this MonitoredServiceListItemDTO.  # noqa: E501


        :return: The identifier of this MonitoredServiceListItemDTO.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this MonitoredServiceListItemDTO.


        :param identifier: The identifier of this MonitoredServiceListItemDTO.  # noqa: E501
        :type: str
        """

        self._identifier = identifier

    @property
    def service_ref(self):
        """Gets the service_ref of this MonitoredServiceListItemDTO.  # noqa: E501


        :return: The service_ref of this MonitoredServiceListItemDTO.  # noqa: E501
        :rtype: str
        """
        return self._service_ref

    @service_ref.setter
    def service_ref(self, service_ref):
        """Sets the service_ref of this MonitoredServiceListItemDTO.


        :param service_ref: The service_ref of this MonitoredServiceListItemDTO.  # noqa: E501
        :type: str
        """

        self._service_ref = service_ref

    @property
    def environment_ref(self):
        """Gets the environment_ref of this MonitoredServiceListItemDTO.  # noqa: E501


        :return: The environment_ref of this MonitoredServiceListItemDTO.  # noqa: E501
        :rtype: str
        """
        return self._environment_ref

    @environment_ref.setter
    def environment_ref(self, environment_ref):
        """Sets the environment_ref of this MonitoredServiceListItemDTO.


        :param environment_ref: The environment_ref of this MonitoredServiceListItemDTO.  # noqa: E501
        :type: str
        """

        self._environment_ref = environment_ref

    @property
    def environment_ref_list(self):
        """Gets the environment_ref_list of this MonitoredServiceListItemDTO.  # noqa: E501


        :return: The environment_ref_list of this MonitoredServiceListItemDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._environment_ref_list

    @environment_ref_list.setter
    def environment_ref_list(self, environment_ref_list):
        """Sets the environment_ref_list of this MonitoredServiceListItemDTO.


        :param environment_ref_list: The environment_ref_list of this MonitoredServiceListItemDTO.  # noqa: E501
        :type: list[str]
        """

        self._environment_ref_list = environment_ref_list

    @property
    def service_name(self):
        """Gets the service_name of this MonitoredServiceListItemDTO.  # noqa: E501


        :return: The service_name of this MonitoredServiceListItemDTO.  # noqa: E501
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """Sets the service_name of this MonitoredServiceListItemDTO.


        :param service_name: The service_name of this MonitoredServiceListItemDTO.  # noqa: E501
        :type: str
        """

        self._service_name = service_name

    @property
    def environment_name(self):
        """Gets the environment_name of this MonitoredServiceListItemDTO.  # noqa: E501


        :return: The environment_name of this MonitoredServiceListItemDTO.  # noqa: E501
        :rtype: str
        """
        return self._environment_name

    @environment_name.setter
    def environment_name(self, environment_name):
        """Sets the environment_name of this MonitoredServiceListItemDTO.


        :param environment_name: The environment_name of this MonitoredServiceListItemDTO.  # noqa: E501
        :type: str
        """

        self._environment_name = environment_name

    @property
    def type(self):
        """Gets the type of this MonitoredServiceListItemDTO.  # noqa: E501


        :return: The type of this MonitoredServiceListItemDTO.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MonitoredServiceListItemDTO.


        :param type: The type of this MonitoredServiceListItemDTO.  # noqa: E501
        :type: str
        """
        allowed_values = ["Application", "Infrastructure"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def health_monitoring_enabled(self):
        """Gets the health_monitoring_enabled of this MonitoredServiceListItemDTO.  # noqa: E501


        :return: The health_monitoring_enabled of this MonitoredServiceListItemDTO.  # noqa: E501
        :rtype: bool
        """
        return self._health_monitoring_enabled

    @health_monitoring_enabled.setter
    def health_monitoring_enabled(self, health_monitoring_enabled):
        """Sets the health_monitoring_enabled of this MonitoredServiceListItemDTO.


        :param health_monitoring_enabled: The health_monitoring_enabled of this MonitoredServiceListItemDTO.  # noqa: E501
        :type: bool
        """

        self._health_monitoring_enabled = health_monitoring_enabled

    @property
    def current_health_score(self):
        """Gets the current_health_score of this MonitoredServiceListItemDTO.  # noqa: E501


        :return: The current_health_score of this MonitoredServiceListItemDTO.  # noqa: E501
        :rtype: RiskData
        """
        return self._current_health_score

    @current_health_score.setter
    def current_health_score(self, current_health_score):
        """Sets the current_health_score of this MonitoredServiceListItemDTO.


        :param current_health_score: The current_health_score of this MonitoredServiceListItemDTO.  # noqa: E501
        :type: RiskData
        """

        self._current_health_score = current_health_score

    @property
    def dependent_health_score(self):
        """Gets the dependent_health_score of this MonitoredServiceListItemDTO.  # noqa: E501


        :return: The dependent_health_score of this MonitoredServiceListItemDTO.  # noqa: E501
        :rtype: list[RiskData]
        """
        return self._dependent_health_score

    @dependent_health_score.setter
    def dependent_health_score(self, dependent_health_score):
        """Sets the dependent_health_score of this MonitoredServiceListItemDTO.


        :param dependent_health_score: The dependent_health_score of this MonitoredServiceListItemDTO.  # noqa: E501
        :type: list[RiskData]
        """

        self._dependent_health_score = dependent_health_score

    @property
    def historical_trend(self):
        """Gets the historical_trend of this MonitoredServiceListItemDTO.  # noqa: E501


        :return: The historical_trend of this MonitoredServiceListItemDTO.  # noqa: E501
        :rtype: HistoricalTrend
        """
        return self._historical_trend

    @historical_trend.setter
    def historical_trend(self, historical_trend):
        """Sets the historical_trend of this MonitoredServiceListItemDTO.


        :param historical_trend: The historical_trend of this MonitoredServiceListItemDTO.  # noqa: E501
        :type: HistoricalTrend
        """

        self._historical_trend = historical_trend

    @property
    def change_summary(self):
        """Gets the change_summary of this MonitoredServiceListItemDTO.  # noqa: E501


        :return: The change_summary of this MonitoredServiceListItemDTO.  # noqa: E501
        :rtype: ChangeSummaryDTO
        """
        return self._change_summary

    @change_summary.setter
    def change_summary(self, change_summary):
        """Sets the change_summary of this MonitoredServiceListItemDTO.


        :param change_summary: The change_summary of this MonitoredServiceListItemDTO.  # noqa: E501
        :type: ChangeSummaryDTO
        """

        self._change_summary = change_summary

    @property
    def tags(self):
        """Gets the tags of this MonitoredServiceListItemDTO.  # noqa: E501


        :return: The tags of this MonitoredServiceListItemDTO.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this MonitoredServiceListItemDTO.


        :param tags: The tags of this MonitoredServiceListItemDTO.  # noqa: E501
        :type: dict(str, str)
        """

        self._tags = tags

    @property
    def service_monitoring_enabled(self):
        """Gets the service_monitoring_enabled of this MonitoredServiceListItemDTO.  # noqa: E501


        :return: The service_monitoring_enabled of this MonitoredServiceListItemDTO.  # noqa: E501
        :rtype: bool
        """
        return self._service_monitoring_enabled

    @service_monitoring_enabled.setter
    def service_monitoring_enabled(self, service_monitoring_enabled):
        """Sets the service_monitoring_enabled of this MonitoredServiceListItemDTO.


        :param service_monitoring_enabled: The service_monitoring_enabled of this MonitoredServiceListItemDTO.  # noqa: E501
        :type: bool
        """

        self._service_monitoring_enabled = service_monitoring_enabled

    @property
    def slo_health_indicators(self):
        """Gets the slo_health_indicators of this MonitoredServiceListItemDTO.  # noqa: E501


        :return: The slo_health_indicators of this MonitoredServiceListItemDTO.  # noqa: E501
        :rtype: list[SloHealthIndicatorDTO]
        """
        return self._slo_health_indicators

    @slo_health_indicators.setter
    def slo_health_indicators(self, slo_health_indicators):
        """Sets the slo_health_indicators of this MonitoredServiceListItemDTO.


        :param slo_health_indicators: The slo_health_indicators of this MonitoredServiceListItemDTO.  # noqa: E501
        :type: list[SloHealthIndicatorDTO]
        """

        self._slo_health_indicators = slo_health_indicators

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
        if issubclass(MonitoredServiceListItemDTO, dict):
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
        if not isinstance(other, MonitoredServiceListItemDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
