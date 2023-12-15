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

class SLODashboardApiFilter(object):
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
        'user_journey_identifiers': 'list[str]',
        'monitored_service_identifier': 'str',
        'target_types': 'list[str]',
        'error_budget_risks': 'list[str]',
        'search_filter': 'str',
        'type': 'str',
        'slo_target_filter_dto': 'SLOTargetFilterDTO',
        'composite_slo_identifier': 'str',
        'evaluation_type': 'str',
        'child_resource': 'bool',
        'env_identifiers': 'list[str]'
    }

    attribute_map = {
        'user_journey_identifiers': 'userJourneyIdentifiers',
        'monitored_service_identifier': 'monitoredServiceIdentifier',
        'target_types': 'targetTypes',
        'error_budget_risks': 'errorBudgetRisks',
        'search_filter': 'searchFilter',
        'type': 'type',
        'slo_target_filter_dto': 'sloTargetFilterDTO',
        'composite_slo_identifier': 'compositeSLOIdentifier',
        'evaluation_type': 'evaluationType',
        'child_resource': 'childResource',
        'env_identifiers': 'envIdentifiers'
    }

    def __init__(self, user_journey_identifiers=None, monitored_service_identifier=None, target_types=None, error_budget_risks=None, search_filter=None, type=None, slo_target_filter_dto=None, composite_slo_identifier=None, evaluation_type=None, child_resource=None, env_identifiers=None):  # noqa: E501
        """SLODashboardApiFilter - a model defined in Swagger"""  # noqa: E501
        self._user_journey_identifiers = None
        self._monitored_service_identifier = None
        self._target_types = None
        self._error_budget_risks = None
        self._search_filter = None
        self._type = None
        self._slo_target_filter_dto = None
        self._composite_slo_identifier = None
        self._evaluation_type = None
        self._child_resource = None
        self._env_identifiers = None
        self.discriminator = None
        if user_journey_identifiers is not None:
            self.user_journey_identifiers = user_journey_identifiers
        if monitored_service_identifier is not None:
            self.monitored_service_identifier = monitored_service_identifier
        if target_types is not None:
            self.target_types = target_types
        if error_budget_risks is not None:
            self.error_budget_risks = error_budget_risks
        if search_filter is not None:
            self.search_filter = search_filter
        if type is not None:
            self.type = type
        if slo_target_filter_dto is not None:
            self.slo_target_filter_dto = slo_target_filter_dto
        if composite_slo_identifier is not None:
            self.composite_slo_identifier = composite_slo_identifier
        if evaluation_type is not None:
            self.evaluation_type = evaluation_type
        if child_resource is not None:
            self.child_resource = child_resource
        if env_identifiers is not None:
            self.env_identifiers = env_identifiers

    @property
    def user_journey_identifiers(self):
        """Gets the user_journey_identifiers of this SLODashboardApiFilter.  # noqa: E501


        :return: The user_journey_identifiers of this SLODashboardApiFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._user_journey_identifiers

    @user_journey_identifiers.setter
    def user_journey_identifiers(self, user_journey_identifiers):
        """Sets the user_journey_identifiers of this SLODashboardApiFilter.


        :param user_journey_identifiers: The user_journey_identifiers of this SLODashboardApiFilter.  # noqa: E501
        :type: list[str]
        """

        self._user_journey_identifiers = user_journey_identifiers

    @property
    def monitored_service_identifier(self):
        """Gets the monitored_service_identifier of this SLODashboardApiFilter.  # noqa: E501


        :return: The monitored_service_identifier of this SLODashboardApiFilter.  # noqa: E501
        :rtype: str
        """
        return self._monitored_service_identifier

    @monitored_service_identifier.setter
    def monitored_service_identifier(self, monitored_service_identifier):
        """Sets the monitored_service_identifier of this SLODashboardApiFilter.


        :param monitored_service_identifier: The monitored_service_identifier of this SLODashboardApiFilter.  # noqa: E501
        :type: str
        """

        self._monitored_service_identifier = monitored_service_identifier

    @property
    def target_types(self):
        """Gets the target_types of this SLODashboardApiFilter.  # noqa: E501


        :return: The target_types of this SLODashboardApiFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._target_types

    @target_types.setter
    def target_types(self, target_types):
        """Sets the target_types of this SLODashboardApiFilter.


        :param target_types: The target_types of this SLODashboardApiFilter.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["Rolling", "Calender"]  # noqa: E501
        if not set(target_types).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `target_types` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(target_types) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._target_types = target_types

    @property
    def error_budget_risks(self):
        """Gets the error_budget_risks of this SLODashboardApiFilter.  # noqa: E501


        :return: The error_budget_risks of this SLODashboardApiFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._error_budget_risks

    @error_budget_risks.setter
    def error_budget_risks(self, error_budget_risks):
        """Sets the error_budget_risks of this SLODashboardApiFilter.


        :param error_budget_risks: The error_budget_risks of this SLODashboardApiFilter.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["EXHAUSTED", "UNHEALTHY", "NEED_ATTENTION", "OBSERVE", "HEALTHY"]  # noqa: E501
        if not set(error_budget_risks).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `error_budget_risks` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(error_budget_risks) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._error_budget_risks = error_budget_risks

    @property
    def search_filter(self):
        """Gets the search_filter of this SLODashboardApiFilter.  # noqa: E501


        :return: The search_filter of this SLODashboardApiFilter.  # noqa: E501
        :rtype: str
        """
        return self._search_filter

    @search_filter.setter
    def search_filter(self, search_filter):
        """Sets the search_filter of this SLODashboardApiFilter.


        :param search_filter: The search_filter of this SLODashboardApiFilter.  # noqa: E501
        :type: str
        """

        self._search_filter = search_filter

    @property
    def type(self):
        """Gets the type of this SLODashboardApiFilter.  # noqa: E501


        :return: The type of this SLODashboardApiFilter.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SLODashboardApiFilter.


        :param type: The type of this SLODashboardApiFilter.  # noqa: E501
        :type: str
        """
        allowed_values = ["Simple", "Composite"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def slo_target_filter_dto(self):
        """Gets the slo_target_filter_dto of this SLODashboardApiFilter.  # noqa: E501


        :return: The slo_target_filter_dto of this SLODashboardApiFilter.  # noqa: E501
        :rtype: SLOTargetFilterDTO
        """
        return self._slo_target_filter_dto

    @slo_target_filter_dto.setter
    def slo_target_filter_dto(self, slo_target_filter_dto):
        """Sets the slo_target_filter_dto of this SLODashboardApiFilter.


        :param slo_target_filter_dto: The slo_target_filter_dto of this SLODashboardApiFilter.  # noqa: E501
        :type: SLOTargetFilterDTO
        """

        self._slo_target_filter_dto = slo_target_filter_dto

    @property
    def composite_slo_identifier(self):
        """Gets the composite_slo_identifier of this SLODashboardApiFilter.  # noqa: E501


        :return: The composite_slo_identifier of this SLODashboardApiFilter.  # noqa: E501
        :rtype: str
        """
        return self._composite_slo_identifier

    @composite_slo_identifier.setter
    def composite_slo_identifier(self, composite_slo_identifier):
        """Sets the composite_slo_identifier of this SLODashboardApiFilter.


        :param composite_slo_identifier: The composite_slo_identifier of this SLODashboardApiFilter.  # noqa: E501
        :type: str
        """

        self._composite_slo_identifier = composite_slo_identifier

    @property
    def evaluation_type(self):
        """Gets the evaluation_type of this SLODashboardApiFilter.  # noqa: E501


        :return: The evaluation_type of this SLODashboardApiFilter.  # noqa: E501
        :rtype: str
        """
        return self._evaluation_type

    @evaluation_type.setter
    def evaluation_type(self, evaluation_type):
        """Sets the evaluation_type of this SLODashboardApiFilter.


        :param evaluation_type: The evaluation_type of this SLODashboardApiFilter.  # noqa: E501
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
    def child_resource(self):
        """Gets the child_resource of this SLODashboardApiFilter.  # noqa: E501


        :return: The child_resource of this SLODashboardApiFilter.  # noqa: E501
        :rtype: bool
        """
        return self._child_resource

    @child_resource.setter
    def child_resource(self, child_resource):
        """Sets the child_resource of this SLODashboardApiFilter.


        :param child_resource: The child_resource of this SLODashboardApiFilter.  # noqa: E501
        :type: bool
        """

        self._child_resource = child_resource

    @property
    def env_identifiers(self):
        """Gets the env_identifiers of this SLODashboardApiFilter.  # noqa: E501


        :return: The env_identifiers of this SLODashboardApiFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._env_identifiers

    @env_identifiers.setter
    def env_identifiers(self, env_identifiers):
        """Sets the env_identifiers of this SLODashboardApiFilter.


        :param env_identifiers: The env_identifiers of this SLODashboardApiFilter.  # noqa: E501
        :type: list[str]
        """

        self._env_identifiers = env_identifiers

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
        if issubclass(SLODashboardApiFilter, dict):
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
        if not isinstance(other, SLODashboardApiFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
