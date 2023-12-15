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

class SLODashboardWidget(object):
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
        'slo_identifier': 'str',
        'title': 'str',
        'monitored_service_identifier': 'str',
        'monitored_service_name': 'str',
        'health_source_identifier': 'str',
        'health_source_name': 'str',
        'service_identifier': 'str',
        'service_name': 'str',
        'environment_identifier': 'str',
        'environment_name': 'str',
        'monitored_service_details': 'list[MonitoredServiceDetail]',
        'tags': 'dict(str, str)',
        'evaluation_type': 'str',
        'slo_type': 'str',
        'burn_rate': 'BurnRate',
        'time_remaining_days': 'int',
        'error_budget_remaining_percentage': 'float',
        'error_budget_remaining': 'int',
        'total_error_budget': 'int',
        'slo_target_type': 'str',
        'current_period_length_days': 'int',
        'current_period_start_time': 'int',
        'current_period_end_time': 'int',
        'slo_target_percentage': 'float',
        'error_budget_burndown': 'list[Point]',
        'slo_performance_trend': 'list[Point]',
        'is_total_error_budget_applicable': 'bool',
        'is_recalculating_sli': 'bool',
        'is_calculating_sli': 'bool',
        'slo_error': 'SLOError',
        'recalculating_sli': 'bool',
        'error_budget_risk': 'str',
        'calculating_sli': 'bool',
        'total_error_budget_applicable': 'bool'
    }

    attribute_map = {
        'slo_identifier': 'sloIdentifier',
        'title': 'title',
        'monitored_service_identifier': 'monitoredServiceIdentifier',
        'monitored_service_name': 'monitoredServiceName',
        'health_source_identifier': 'healthSourceIdentifier',
        'health_source_name': 'healthSourceName',
        'service_identifier': 'serviceIdentifier',
        'service_name': 'serviceName',
        'environment_identifier': 'environmentIdentifier',
        'environment_name': 'environmentName',
        'monitored_service_details': 'monitoredServiceDetails',
        'tags': 'tags',
        'evaluation_type': 'evaluationType',
        'slo_type': 'sloType',
        'burn_rate': 'burnRate',
        'time_remaining_days': 'timeRemainingDays',
        'error_budget_remaining_percentage': 'errorBudgetRemainingPercentage',
        'error_budget_remaining': 'errorBudgetRemaining',
        'total_error_budget': 'totalErrorBudget',
        'slo_target_type': 'sloTargetType',
        'current_period_length_days': 'currentPeriodLengthDays',
        'current_period_start_time': 'currentPeriodStartTime',
        'current_period_end_time': 'currentPeriodEndTime',
        'slo_target_percentage': 'sloTargetPercentage',
        'error_budget_burndown': 'errorBudgetBurndown',
        'slo_performance_trend': 'sloPerformanceTrend',
        'is_total_error_budget_applicable': 'isTotalErrorBudgetApplicable',
        'is_recalculating_sli': 'isRecalculatingSLI',
        'is_calculating_sli': 'isCalculatingSLI',
        'slo_error': 'sloError',
        'recalculating_sli': 'recalculatingSLI',
        'error_budget_risk': 'errorBudgetRisk',
        'calculating_sli': 'calculatingSLI',
        'total_error_budget_applicable': 'totalErrorBudgetApplicable'
    }

    def __init__(self, slo_identifier=None, title=None, monitored_service_identifier=None, monitored_service_name=None, health_source_identifier=None, health_source_name=None, service_identifier=None, service_name=None, environment_identifier=None, environment_name=None, monitored_service_details=None, tags=None, evaluation_type=None, slo_type=None, burn_rate=None, time_remaining_days=None, error_budget_remaining_percentage=None, error_budget_remaining=None, total_error_budget=None, slo_target_type=None, current_period_length_days=None, current_period_start_time=None, current_period_end_time=None, slo_target_percentage=None, error_budget_burndown=None, slo_performance_trend=None, is_total_error_budget_applicable=None, is_recalculating_sli=None, is_calculating_sli=None, slo_error=None, recalculating_sli=None, error_budget_risk=None, calculating_sli=None, total_error_budget_applicable=None):  # noqa: E501
        """SLODashboardWidget - a model defined in Swagger"""  # noqa: E501
        self._slo_identifier = None
        self._title = None
        self._monitored_service_identifier = None
        self._monitored_service_name = None
        self._health_source_identifier = None
        self._health_source_name = None
        self._service_identifier = None
        self._service_name = None
        self._environment_identifier = None
        self._environment_name = None
        self._monitored_service_details = None
        self._tags = None
        self._evaluation_type = None
        self._slo_type = None
        self._burn_rate = None
        self._time_remaining_days = None
        self._error_budget_remaining_percentage = None
        self._error_budget_remaining = None
        self._total_error_budget = None
        self._slo_target_type = None
        self._current_period_length_days = None
        self._current_period_start_time = None
        self._current_period_end_time = None
        self._slo_target_percentage = None
        self._error_budget_burndown = None
        self._slo_performance_trend = None
        self._is_total_error_budget_applicable = None
        self._is_recalculating_sli = None
        self._is_calculating_sli = None
        self._slo_error = None
        self._recalculating_sli = None
        self._error_budget_risk = None
        self._calculating_sli = None
        self._total_error_budget_applicable = None
        self.discriminator = None
        self.slo_identifier = slo_identifier
        self.title = title
        if monitored_service_identifier is not None:
            self.monitored_service_identifier = monitored_service_identifier
        if monitored_service_name is not None:
            self.monitored_service_name = monitored_service_name
        if health_source_identifier is not None:
            self.health_source_identifier = health_source_identifier
        if health_source_name is not None:
            self.health_source_name = health_source_name
        if service_identifier is not None:
            self.service_identifier = service_identifier
        if service_name is not None:
            self.service_name = service_name
        if environment_identifier is not None:
            self.environment_identifier = environment_identifier
        if environment_name is not None:
            self.environment_name = environment_name
        if monitored_service_details is not None:
            self.monitored_service_details = monitored_service_details
        if tags is not None:
            self.tags = tags
        if evaluation_type is not None:
            self.evaluation_type = evaluation_type
        self.slo_type = slo_type
        self.burn_rate = burn_rate
        self.time_remaining_days = time_remaining_days
        self.error_budget_remaining_percentage = error_budget_remaining_percentage
        self.error_budget_remaining = error_budget_remaining
        self.total_error_budget = total_error_budget
        self.slo_target_type = slo_target_type
        self.current_period_length_days = current_period_length_days
        self.current_period_start_time = current_period_start_time
        self.current_period_end_time = current_period_end_time
        self.slo_target_percentage = slo_target_percentage
        self.error_budget_burndown = error_budget_burndown
        self.slo_performance_trend = slo_performance_trend
        if is_total_error_budget_applicable is not None:
            self.is_total_error_budget_applicable = is_total_error_budget_applicable
        if is_recalculating_sli is not None:
            self.is_recalculating_sli = is_recalculating_sli
        if is_calculating_sli is not None:
            self.is_calculating_sli = is_calculating_sli
        if slo_error is not None:
            self.slo_error = slo_error
        if recalculating_sli is not None:
            self.recalculating_sli = recalculating_sli
        self.error_budget_risk = error_budget_risk
        if calculating_sli is not None:
            self.calculating_sli = calculating_sli
        if total_error_budget_applicable is not None:
            self.total_error_budget_applicable = total_error_budget_applicable

    @property
    def slo_identifier(self):
        """Gets the slo_identifier of this SLODashboardWidget.  # noqa: E501


        :return: The slo_identifier of this SLODashboardWidget.  # noqa: E501
        :rtype: str
        """
        return self._slo_identifier

    @slo_identifier.setter
    def slo_identifier(self, slo_identifier):
        """Sets the slo_identifier of this SLODashboardWidget.


        :param slo_identifier: The slo_identifier of this SLODashboardWidget.  # noqa: E501
        :type: str
        """
        if slo_identifier is None:
            raise ValueError("Invalid value for `slo_identifier`, must not be `None`")  # noqa: E501

        self._slo_identifier = slo_identifier

    @property
    def title(self):
        """Gets the title of this SLODashboardWidget.  # noqa: E501


        :return: The title of this SLODashboardWidget.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this SLODashboardWidget.


        :param title: The title of this SLODashboardWidget.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def monitored_service_identifier(self):
        """Gets the monitored_service_identifier of this SLODashboardWidget.  # noqa: E501


        :return: The monitored_service_identifier of this SLODashboardWidget.  # noqa: E501
        :rtype: str
        """
        return self._monitored_service_identifier

    @monitored_service_identifier.setter
    def monitored_service_identifier(self, monitored_service_identifier):
        """Sets the monitored_service_identifier of this SLODashboardWidget.


        :param monitored_service_identifier: The monitored_service_identifier of this SLODashboardWidget.  # noqa: E501
        :type: str
        """

        self._monitored_service_identifier = monitored_service_identifier

    @property
    def monitored_service_name(self):
        """Gets the monitored_service_name of this SLODashboardWidget.  # noqa: E501


        :return: The monitored_service_name of this SLODashboardWidget.  # noqa: E501
        :rtype: str
        """
        return self._monitored_service_name

    @monitored_service_name.setter
    def monitored_service_name(self, monitored_service_name):
        """Sets the monitored_service_name of this SLODashboardWidget.


        :param monitored_service_name: The monitored_service_name of this SLODashboardWidget.  # noqa: E501
        :type: str
        """

        self._monitored_service_name = monitored_service_name

    @property
    def health_source_identifier(self):
        """Gets the health_source_identifier of this SLODashboardWidget.  # noqa: E501


        :return: The health_source_identifier of this SLODashboardWidget.  # noqa: E501
        :rtype: str
        """
        return self._health_source_identifier

    @health_source_identifier.setter
    def health_source_identifier(self, health_source_identifier):
        """Sets the health_source_identifier of this SLODashboardWidget.


        :param health_source_identifier: The health_source_identifier of this SLODashboardWidget.  # noqa: E501
        :type: str
        """

        self._health_source_identifier = health_source_identifier

    @property
    def health_source_name(self):
        """Gets the health_source_name of this SLODashboardWidget.  # noqa: E501


        :return: The health_source_name of this SLODashboardWidget.  # noqa: E501
        :rtype: str
        """
        return self._health_source_name

    @health_source_name.setter
    def health_source_name(self, health_source_name):
        """Sets the health_source_name of this SLODashboardWidget.


        :param health_source_name: The health_source_name of this SLODashboardWidget.  # noqa: E501
        :type: str
        """

        self._health_source_name = health_source_name

    @property
    def service_identifier(self):
        """Gets the service_identifier of this SLODashboardWidget.  # noqa: E501


        :return: The service_identifier of this SLODashboardWidget.  # noqa: E501
        :rtype: str
        """
        return self._service_identifier

    @service_identifier.setter
    def service_identifier(self, service_identifier):
        """Sets the service_identifier of this SLODashboardWidget.


        :param service_identifier: The service_identifier of this SLODashboardWidget.  # noqa: E501
        :type: str
        """

        self._service_identifier = service_identifier

    @property
    def service_name(self):
        """Gets the service_name of this SLODashboardWidget.  # noqa: E501


        :return: The service_name of this SLODashboardWidget.  # noqa: E501
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """Sets the service_name of this SLODashboardWidget.


        :param service_name: The service_name of this SLODashboardWidget.  # noqa: E501
        :type: str
        """

        self._service_name = service_name

    @property
    def environment_identifier(self):
        """Gets the environment_identifier of this SLODashboardWidget.  # noqa: E501


        :return: The environment_identifier of this SLODashboardWidget.  # noqa: E501
        :rtype: str
        """
        return self._environment_identifier

    @environment_identifier.setter
    def environment_identifier(self, environment_identifier):
        """Sets the environment_identifier of this SLODashboardWidget.


        :param environment_identifier: The environment_identifier of this SLODashboardWidget.  # noqa: E501
        :type: str
        """

        self._environment_identifier = environment_identifier

    @property
    def environment_name(self):
        """Gets the environment_name of this SLODashboardWidget.  # noqa: E501


        :return: The environment_name of this SLODashboardWidget.  # noqa: E501
        :rtype: str
        """
        return self._environment_name

    @environment_name.setter
    def environment_name(self, environment_name):
        """Sets the environment_name of this SLODashboardWidget.


        :param environment_name: The environment_name of this SLODashboardWidget.  # noqa: E501
        :type: str
        """

        self._environment_name = environment_name

    @property
    def monitored_service_details(self):
        """Gets the monitored_service_details of this SLODashboardWidget.  # noqa: E501


        :return: The monitored_service_details of this SLODashboardWidget.  # noqa: E501
        :rtype: list[MonitoredServiceDetail]
        """
        return self._monitored_service_details

    @monitored_service_details.setter
    def monitored_service_details(self, monitored_service_details):
        """Sets the monitored_service_details of this SLODashboardWidget.


        :param monitored_service_details: The monitored_service_details of this SLODashboardWidget.  # noqa: E501
        :type: list[MonitoredServiceDetail]
        """

        self._monitored_service_details = monitored_service_details

    @property
    def tags(self):
        """Gets the tags of this SLODashboardWidget.  # noqa: E501


        :return: The tags of this SLODashboardWidget.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this SLODashboardWidget.


        :param tags: The tags of this SLODashboardWidget.  # noqa: E501
        :type: dict(str, str)
        """

        self._tags = tags

    @property
    def evaluation_type(self):
        """Gets the evaluation_type of this SLODashboardWidget.  # noqa: E501


        :return: The evaluation_type of this SLODashboardWidget.  # noqa: E501
        :rtype: str
        """
        return self._evaluation_type

    @evaluation_type.setter
    def evaluation_type(self, evaluation_type):
        """Sets the evaluation_type of this SLODashboardWidget.


        :param evaluation_type: The evaluation_type of this SLODashboardWidget.  # noqa: E501
        :type: str
        """
        allowed_values = ["Window", "Request", "MetricLess"]  # noqa: E501
        if evaluation_type not in allowed_values:
            raise ValueError(
                "Invalid value for `evaluation_type` ({0}), must be one of {1}"  # noqa: E501
                .format(evaluation_type, allowed_values)
            )

        self._evaluation_type = evaluation_type

    @property
    def slo_type(self):
        """Gets the slo_type of this SLODashboardWidget.  # noqa: E501


        :return: The slo_type of this SLODashboardWidget.  # noqa: E501
        :rtype: str
        """
        return self._slo_type

    @slo_type.setter
    def slo_type(self, slo_type):
        """Sets the slo_type of this SLODashboardWidget.


        :param slo_type: The slo_type of this SLODashboardWidget.  # noqa: E501
        :type: str
        """
        if slo_type is None:
            raise ValueError("Invalid value for `slo_type`, must not be `None`")  # noqa: E501
        allowed_values = ["Simple", "Composite"]  # noqa: E501
        if slo_type not in allowed_values:
            raise ValueError(
                "Invalid value for `slo_type` ({0}), must be one of {1}"  # noqa: E501
                .format(slo_type, allowed_values)
            )

        self._slo_type = slo_type

    @property
    def burn_rate(self):
        """Gets the burn_rate of this SLODashboardWidget.  # noqa: E501


        :return: The burn_rate of this SLODashboardWidget.  # noqa: E501
        :rtype: BurnRate
        """
        return self._burn_rate

    @burn_rate.setter
    def burn_rate(self, burn_rate):
        """Sets the burn_rate of this SLODashboardWidget.


        :param burn_rate: The burn_rate of this SLODashboardWidget.  # noqa: E501
        :type: BurnRate
        """
        if burn_rate is None:
            raise ValueError("Invalid value for `burn_rate`, must not be `None`")  # noqa: E501

        self._burn_rate = burn_rate

    @property
    def time_remaining_days(self):
        """Gets the time_remaining_days of this SLODashboardWidget.  # noqa: E501


        :return: The time_remaining_days of this SLODashboardWidget.  # noqa: E501
        :rtype: int
        """
        return self._time_remaining_days

    @time_remaining_days.setter
    def time_remaining_days(self, time_remaining_days):
        """Sets the time_remaining_days of this SLODashboardWidget.


        :param time_remaining_days: The time_remaining_days of this SLODashboardWidget.  # noqa: E501
        :type: int
        """
        if time_remaining_days is None:
            raise ValueError("Invalid value for `time_remaining_days`, must not be `None`")  # noqa: E501

        self._time_remaining_days = time_remaining_days

    @property
    def error_budget_remaining_percentage(self):
        """Gets the error_budget_remaining_percentage of this SLODashboardWidget.  # noqa: E501


        :return: The error_budget_remaining_percentage of this SLODashboardWidget.  # noqa: E501
        :rtype: float
        """
        return self._error_budget_remaining_percentage

    @error_budget_remaining_percentage.setter
    def error_budget_remaining_percentage(self, error_budget_remaining_percentage):
        """Sets the error_budget_remaining_percentage of this SLODashboardWidget.


        :param error_budget_remaining_percentage: The error_budget_remaining_percentage of this SLODashboardWidget.  # noqa: E501
        :type: float
        """
        if error_budget_remaining_percentage is None:
            raise ValueError("Invalid value for `error_budget_remaining_percentage`, must not be `None`")  # noqa: E501

        self._error_budget_remaining_percentage = error_budget_remaining_percentage

    @property
    def error_budget_remaining(self):
        """Gets the error_budget_remaining of this SLODashboardWidget.  # noqa: E501


        :return: The error_budget_remaining of this SLODashboardWidget.  # noqa: E501
        :rtype: int
        """
        return self._error_budget_remaining

    @error_budget_remaining.setter
    def error_budget_remaining(self, error_budget_remaining):
        """Sets the error_budget_remaining of this SLODashboardWidget.


        :param error_budget_remaining: The error_budget_remaining of this SLODashboardWidget.  # noqa: E501
        :type: int
        """
        if error_budget_remaining is None:
            raise ValueError("Invalid value for `error_budget_remaining`, must not be `None`")  # noqa: E501

        self._error_budget_remaining = error_budget_remaining

    @property
    def total_error_budget(self):
        """Gets the total_error_budget of this SLODashboardWidget.  # noqa: E501


        :return: The total_error_budget of this SLODashboardWidget.  # noqa: E501
        :rtype: int
        """
        return self._total_error_budget

    @total_error_budget.setter
    def total_error_budget(self, total_error_budget):
        """Sets the total_error_budget of this SLODashboardWidget.


        :param total_error_budget: The total_error_budget of this SLODashboardWidget.  # noqa: E501
        :type: int
        """
        if total_error_budget is None:
            raise ValueError("Invalid value for `total_error_budget`, must not be `None`")  # noqa: E501

        self._total_error_budget = total_error_budget

    @property
    def slo_target_type(self):
        """Gets the slo_target_type of this SLODashboardWidget.  # noqa: E501


        :return: The slo_target_type of this SLODashboardWidget.  # noqa: E501
        :rtype: str
        """
        return self._slo_target_type

    @slo_target_type.setter
    def slo_target_type(self, slo_target_type):
        """Sets the slo_target_type of this SLODashboardWidget.


        :param slo_target_type: The slo_target_type of this SLODashboardWidget.  # noqa: E501
        :type: str
        """
        if slo_target_type is None:
            raise ValueError("Invalid value for `slo_target_type`, must not be `None`")  # noqa: E501
        allowed_values = ["Rolling", "Calender"]  # noqa: E501
        if slo_target_type not in allowed_values:
            raise ValueError(
                "Invalid value for `slo_target_type` ({0}), must be one of {1}"  # noqa: E501
                .format(slo_target_type, allowed_values)
            )

        self._slo_target_type = slo_target_type

    @property
    def current_period_length_days(self):
        """Gets the current_period_length_days of this SLODashboardWidget.  # noqa: E501


        :return: The current_period_length_days of this SLODashboardWidget.  # noqa: E501
        :rtype: int
        """
        return self._current_period_length_days

    @current_period_length_days.setter
    def current_period_length_days(self, current_period_length_days):
        """Sets the current_period_length_days of this SLODashboardWidget.


        :param current_period_length_days: The current_period_length_days of this SLODashboardWidget.  # noqa: E501
        :type: int
        """
        if current_period_length_days is None:
            raise ValueError("Invalid value for `current_period_length_days`, must not be `None`")  # noqa: E501

        self._current_period_length_days = current_period_length_days

    @property
    def current_period_start_time(self):
        """Gets the current_period_start_time of this SLODashboardWidget.  # noqa: E501


        :return: The current_period_start_time of this SLODashboardWidget.  # noqa: E501
        :rtype: int
        """
        return self._current_period_start_time

    @current_period_start_time.setter
    def current_period_start_time(self, current_period_start_time):
        """Sets the current_period_start_time of this SLODashboardWidget.


        :param current_period_start_time: The current_period_start_time of this SLODashboardWidget.  # noqa: E501
        :type: int
        """
        if current_period_start_time is None:
            raise ValueError("Invalid value for `current_period_start_time`, must not be `None`")  # noqa: E501

        self._current_period_start_time = current_period_start_time

    @property
    def current_period_end_time(self):
        """Gets the current_period_end_time of this SLODashboardWidget.  # noqa: E501


        :return: The current_period_end_time of this SLODashboardWidget.  # noqa: E501
        :rtype: int
        """
        return self._current_period_end_time

    @current_period_end_time.setter
    def current_period_end_time(self, current_period_end_time):
        """Sets the current_period_end_time of this SLODashboardWidget.


        :param current_period_end_time: The current_period_end_time of this SLODashboardWidget.  # noqa: E501
        :type: int
        """
        if current_period_end_time is None:
            raise ValueError("Invalid value for `current_period_end_time`, must not be `None`")  # noqa: E501

        self._current_period_end_time = current_period_end_time

    @property
    def slo_target_percentage(self):
        """Gets the slo_target_percentage of this SLODashboardWidget.  # noqa: E501


        :return: The slo_target_percentage of this SLODashboardWidget.  # noqa: E501
        :rtype: float
        """
        return self._slo_target_percentage

    @slo_target_percentage.setter
    def slo_target_percentage(self, slo_target_percentage):
        """Sets the slo_target_percentage of this SLODashboardWidget.


        :param slo_target_percentage: The slo_target_percentage of this SLODashboardWidget.  # noqa: E501
        :type: float
        """
        if slo_target_percentage is None:
            raise ValueError("Invalid value for `slo_target_percentage`, must not be `None`")  # noqa: E501

        self._slo_target_percentage = slo_target_percentage

    @property
    def error_budget_burndown(self):
        """Gets the error_budget_burndown of this SLODashboardWidget.  # noqa: E501


        :return: The error_budget_burndown of this SLODashboardWidget.  # noqa: E501
        :rtype: list[Point]
        """
        return self._error_budget_burndown

    @error_budget_burndown.setter
    def error_budget_burndown(self, error_budget_burndown):
        """Sets the error_budget_burndown of this SLODashboardWidget.


        :param error_budget_burndown: The error_budget_burndown of this SLODashboardWidget.  # noqa: E501
        :type: list[Point]
        """
        if error_budget_burndown is None:
            raise ValueError("Invalid value for `error_budget_burndown`, must not be `None`")  # noqa: E501

        self._error_budget_burndown = error_budget_burndown

    @property
    def slo_performance_trend(self):
        """Gets the slo_performance_trend of this SLODashboardWidget.  # noqa: E501


        :return: The slo_performance_trend of this SLODashboardWidget.  # noqa: E501
        :rtype: list[Point]
        """
        return self._slo_performance_trend

    @slo_performance_trend.setter
    def slo_performance_trend(self, slo_performance_trend):
        """Sets the slo_performance_trend of this SLODashboardWidget.


        :param slo_performance_trend: The slo_performance_trend of this SLODashboardWidget.  # noqa: E501
        :type: list[Point]
        """
        if slo_performance_trend is None:
            raise ValueError("Invalid value for `slo_performance_trend`, must not be `None`")  # noqa: E501

        self._slo_performance_trend = slo_performance_trend

    @property
    def is_total_error_budget_applicable(self):
        """Gets the is_total_error_budget_applicable of this SLODashboardWidget.  # noqa: E501


        :return: The is_total_error_budget_applicable of this SLODashboardWidget.  # noqa: E501
        :rtype: bool
        """
        return self._is_total_error_budget_applicable

    @is_total_error_budget_applicable.setter
    def is_total_error_budget_applicable(self, is_total_error_budget_applicable):
        """Sets the is_total_error_budget_applicable of this SLODashboardWidget.


        :param is_total_error_budget_applicable: The is_total_error_budget_applicable of this SLODashboardWidget.  # noqa: E501
        :type: bool
        """

        self._is_total_error_budget_applicable = is_total_error_budget_applicable

    @property
    def is_recalculating_sli(self):
        """Gets the is_recalculating_sli of this SLODashboardWidget.  # noqa: E501


        :return: The is_recalculating_sli of this SLODashboardWidget.  # noqa: E501
        :rtype: bool
        """
        return self._is_recalculating_sli

    @is_recalculating_sli.setter
    def is_recalculating_sli(self, is_recalculating_sli):
        """Sets the is_recalculating_sli of this SLODashboardWidget.


        :param is_recalculating_sli: The is_recalculating_sli of this SLODashboardWidget.  # noqa: E501
        :type: bool
        """

        self._is_recalculating_sli = is_recalculating_sli

    @property
    def is_calculating_sli(self):
        """Gets the is_calculating_sli of this SLODashboardWidget.  # noqa: E501


        :return: The is_calculating_sli of this SLODashboardWidget.  # noqa: E501
        :rtype: bool
        """
        return self._is_calculating_sli

    @is_calculating_sli.setter
    def is_calculating_sli(self, is_calculating_sli):
        """Sets the is_calculating_sli of this SLODashboardWidget.


        :param is_calculating_sli: The is_calculating_sli of this SLODashboardWidget.  # noqa: E501
        :type: bool
        """

        self._is_calculating_sli = is_calculating_sli

    @property
    def slo_error(self):
        """Gets the slo_error of this SLODashboardWidget.  # noqa: E501


        :return: The slo_error of this SLODashboardWidget.  # noqa: E501
        :rtype: SLOError
        """
        return self._slo_error

    @slo_error.setter
    def slo_error(self, slo_error):
        """Sets the slo_error of this SLODashboardWidget.


        :param slo_error: The slo_error of this SLODashboardWidget.  # noqa: E501
        :type: SLOError
        """

        self._slo_error = slo_error

    @property
    def recalculating_sli(self):
        """Gets the recalculating_sli of this SLODashboardWidget.  # noqa: E501


        :return: The recalculating_sli of this SLODashboardWidget.  # noqa: E501
        :rtype: bool
        """
        return self._recalculating_sli

    @recalculating_sli.setter
    def recalculating_sli(self, recalculating_sli):
        """Sets the recalculating_sli of this SLODashboardWidget.


        :param recalculating_sli: The recalculating_sli of this SLODashboardWidget.  # noqa: E501
        :type: bool
        """

        self._recalculating_sli = recalculating_sli

    @property
    def error_budget_risk(self):
        """Gets the error_budget_risk of this SLODashboardWidget.  # noqa: E501


        :return: The error_budget_risk of this SLODashboardWidget.  # noqa: E501
        :rtype: str
        """
        return self._error_budget_risk

    @error_budget_risk.setter
    def error_budget_risk(self, error_budget_risk):
        """Sets the error_budget_risk of this SLODashboardWidget.


        :param error_budget_risk: The error_budget_risk of this SLODashboardWidget.  # noqa: E501
        :type: str
        """
        if error_budget_risk is None:
            raise ValueError("Invalid value for `error_budget_risk`, must not be `None`")  # noqa: E501
        allowed_values = ["EXHAUSTED", "UNHEALTHY", "NEED_ATTENTION", "OBSERVE", "HEALTHY"]  # noqa: E501
        if error_budget_risk not in allowed_values:
            raise ValueError(
                "Invalid value for `error_budget_risk` ({0}), must be one of {1}"  # noqa: E501
                .format(error_budget_risk, allowed_values)
            )

        self._error_budget_risk = error_budget_risk

    @property
    def calculating_sli(self):
        """Gets the calculating_sli of this SLODashboardWidget.  # noqa: E501


        :return: The calculating_sli of this SLODashboardWidget.  # noqa: E501
        :rtype: bool
        """
        return self._calculating_sli

    @calculating_sli.setter
    def calculating_sli(self, calculating_sli):
        """Sets the calculating_sli of this SLODashboardWidget.


        :param calculating_sli: The calculating_sli of this SLODashboardWidget.  # noqa: E501
        :type: bool
        """

        self._calculating_sli = calculating_sli

    @property
    def total_error_budget_applicable(self):
        """Gets the total_error_budget_applicable of this SLODashboardWidget.  # noqa: E501


        :return: The total_error_budget_applicable of this SLODashboardWidget.  # noqa: E501
        :rtype: bool
        """
        return self._total_error_budget_applicable

    @total_error_budget_applicable.setter
    def total_error_budget_applicable(self, total_error_budget_applicable):
        """Sets the total_error_budget_applicable of this SLODashboardWidget.


        :param total_error_budget_applicable: The total_error_budget_applicable of this SLODashboardWidget.  # noqa: E501
        :type: bool
        """

        self._total_error_budget_applicable = total_error_budget_applicable

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
        if issubclass(SLODashboardWidget, dict):
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
        if not isinstance(other, SLODashboardWidget):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
