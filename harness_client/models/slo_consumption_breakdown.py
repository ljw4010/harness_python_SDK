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

class SLOConsumptionBreakdown(object):
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
        'slo_name': 'str',
        'monitored_service_identifier': 'str',
        'service_name': 'str',
        'environment_identifier': 'str',
        'weightage_percentage': 'float',
        'slo_target_percentage': 'float',
        'sli_status_percentage': 'float',
        'error_budget_burned': 'int',
        'contributed_error_budget_burned': 'int',
        'project_params': 'ProjectParams',
        'org_name': 'str',
        'project_name': 'str',
        'slo_error': 'SLOError'
    }

    attribute_map = {
        'slo_identifier': 'sloIdentifier',
        'slo_name': 'sloName',
        'monitored_service_identifier': 'monitoredServiceIdentifier',
        'service_name': 'serviceName',
        'environment_identifier': 'environmentIdentifier',
        'weightage_percentage': 'weightagePercentage',
        'slo_target_percentage': 'sloTargetPercentage',
        'sli_status_percentage': 'sliStatusPercentage',
        'error_budget_burned': 'errorBudgetBurned',
        'contributed_error_budget_burned': 'contributedErrorBudgetBurned',
        'project_params': 'projectParams',
        'org_name': 'orgName',
        'project_name': 'projectName',
        'slo_error': 'sloError'
    }

    def __init__(self, slo_identifier=None, slo_name=None, monitored_service_identifier=None, service_name=None, environment_identifier=None, weightage_percentage=None, slo_target_percentage=None, sli_status_percentage=None, error_budget_burned=None, contributed_error_budget_burned=None, project_params=None, org_name=None, project_name=None, slo_error=None):  # noqa: E501
        """SLOConsumptionBreakdown - a model defined in Swagger"""  # noqa: E501
        self._slo_identifier = None
        self._slo_name = None
        self._monitored_service_identifier = None
        self._service_name = None
        self._environment_identifier = None
        self._weightage_percentage = None
        self._slo_target_percentage = None
        self._sli_status_percentage = None
        self._error_budget_burned = None
        self._contributed_error_budget_burned = None
        self._project_params = None
        self._org_name = None
        self._project_name = None
        self._slo_error = None
        self.discriminator = None
        self.slo_identifier = slo_identifier
        self.slo_name = slo_name
        if monitored_service_identifier is not None:
            self.monitored_service_identifier = monitored_service_identifier
        if service_name is not None:
            self.service_name = service_name
        if environment_identifier is not None:
            self.environment_identifier = environment_identifier
        self.weightage_percentage = weightage_percentage
        self.slo_target_percentage = slo_target_percentage
        self.sli_status_percentage = sli_status_percentage
        self.error_budget_burned = error_budget_burned
        if contributed_error_budget_burned is not None:
            self.contributed_error_budget_burned = contributed_error_budget_burned
        self.project_params = project_params
        if org_name is not None:
            self.org_name = org_name
        if project_name is not None:
            self.project_name = project_name
        if slo_error is not None:
            self.slo_error = slo_error

    @property
    def slo_identifier(self):
        """Gets the slo_identifier of this SLOConsumptionBreakdown.  # noqa: E501


        :return: The slo_identifier of this SLOConsumptionBreakdown.  # noqa: E501
        :rtype: str
        """
        return self._slo_identifier

    @slo_identifier.setter
    def slo_identifier(self, slo_identifier):
        """Sets the slo_identifier of this SLOConsumptionBreakdown.


        :param slo_identifier: The slo_identifier of this SLOConsumptionBreakdown.  # noqa: E501
        :type: str
        """
        if slo_identifier is None:
            raise ValueError("Invalid value for `slo_identifier`, must not be `None`")  # noqa: E501

        self._slo_identifier = slo_identifier

    @property
    def slo_name(self):
        """Gets the slo_name of this SLOConsumptionBreakdown.  # noqa: E501


        :return: The slo_name of this SLOConsumptionBreakdown.  # noqa: E501
        :rtype: str
        """
        return self._slo_name

    @slo_name.setter
    def slo_name(self, slo_name):
        """Sets the slo_name of this SLOConsumptionBreakdown.


        :param slo_name: The slo_name of this SLOConsumptionBreakdown.  # noqa: E501
        :type: str
        """
        if slo_name is None:
            raise ValueError("Invalid value for `slo_name`, must not be `None`")  # noqa: E501

        self._slo_name = slo_name

    @property
    def monitored_service_identifier(self):
        """Gets the monitored_service_identifier of this SLOConsumptionBreakdown.  # noqa: E501


        :return: The monitored_service_identifier of this SLOConsumptionBreakdown.  # noqa: E501
        :rtype: str
        """
        return self._monitored_service_identifier

    @monitored_service_identifier.setter
    def monitored_service_identifier(self, monitored_service_identifier):
        """Sets the monitored_service_identifier of this SLOConsumptionBreakdown.


        :param monitored_service_identifier: The monitored_service_identifier of this SLOConsumptionBreakdown.  # noqa: E501
        :type: str
        """

        self._monitored_service_identifier = monitored_service_identifier

    @property
    def service_name(self):
        """Gets the service_name of this SLOConsumptionBreakdown.  # noqa: E501


        :return: The service_name of this SLOConsumptionBreakdown.  # noqa: E501
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """Sets the service_name of this SLOConsumptionBreakdown.


        :param service_name: The service_name of this SLOConsumptionBreakdown.  # noqa: E501
        :type: str
        """

        self._service_name = service_name

    @property
    def environment_identifier(self):
        """Gets the environment_identifier of this SLOConsumptionBreakdown.  # noqa: E501


        :return: The environment_identifier of this SLOConsumptionBreakdown.  # noqa: E501
        :rtype: str
        """
        return self._environment_identifier

    @environment_identifier.setter
    def environment_identifier(self, environment_identifier):
        """Sets the environment_identifier of this SLOConsumptionBreakdown.


        :param environment_identifier: The environment_identifier of this SLOConsumptionBreakdown.  # noqa: E501
        :type: str
        """

        self._environment_identifier = environment_identifier

    @property
    def weightage_percentage(self):
        """Gets the weightage_percentage of this SLOConsumptionBreakdown.  # noqa: E501


        :return: The weightage_percentage of this SLOConsumptionBreakdown.  # noqa: E501
        :rtype: float
        """
        return self._weightage_percentage

    @weightage_percentage.setter
    def weightage_percentage(self, weightage_percentage):
        """Sets the weightage_percentage of this SLOConsumptionBreakdown.


        :param weightage_percentage: The weightage_percentage of this SLOConsumptionBreakdown.  # noqa: E501
        :type: float
        """
        if weightage_percentage is None:
            raise ValueError("Invalid value for `weightage_percentage`, must not be `None`")  # noqa: E501

        self._weightage_percentage = weightage_percentage

    @property
    def slo_target_percentage(self):
        """Gets the slo_target_percentage of this SLOConsumptionBreakdown.  # noqa: E501


        :return: The slo_target_percentage of this SLOConsumptionBreakdown.  # noqa: E501
        :rtype: float
        """
        return self._slo_target_percentage

    @slo_target_percentage.setter
    def slo_target_percentage(self, slo_target_percentage):
        """Sets the slo_target_percentage of this SLOConsumptionBreakdown.


        :param slo_target_percentage: The slo_target_percentage of this SLOConsumptionBreakdown.  # noqa: E501
        :type: float
        """
        if slo_target_percentage is None:
            raise ValueError("Invalid value for `slo_target_percentage`, must not be `None`")  # noqa: E501

        self._slo_target_percentage = slo_target_percentage

    @property
    def sli_status_percentage(self):
        """Gets the sli_status_percentage of this SLOConsumptionBreakdown.  # noqa: E501


        :return: The sli_status_percentage of this SLOConsumptionBreakdown.  # noqa: E501
        :rtype: float
        """
        return self._sli_status_percentage

    @sli_status_percentage.setter
    def sli_status_percentage(self, sli_status_percentage):
        """Sets the sli_status_percentage of this SLOConsumptionBreakdown.


        :param sli_status_percentage: The sli_status_percentage of this SLOConsumptionBreakdown.  # noqa: E501
        :type: float
        """
        if sli_status_percentage is None:
            raise ValueError("Invalid value for `sli_status_percentage`, must not be `None`")  # noqa: E501

        self._sli_status_percentage = sli_status_percentage

    @property
    def error_budget_burned(self):
        """Gets the error_budget_burned of this SLOConsumptionBreakdown.  # noqa: E501


        :return: The error_budget_burned of this SLOConsumptionBreakdown.  # noqa: E501
        :rtype: int
        """
        return self._error_budget_burned

    @error_budget_burned.setter
    def error_budget_burned(self, error_budget_burned):
        """Sets the error_budget_burned of this SLOConsumptionBreakdown.


        :param error_budget_burned: The error_budget_burned of this SLOConsumptionBreakdown.  # noqa: E501
        :type: int
        """
        if error_budget_burned is None:
            raise ValueError("Invalid value for `error_budget_burned`, must not be `None`")  # noqa: E501

        self._error_budget_burned = error_budget_burned

    @property
    def contributed_error_budget_burned(self):
        """Gets the contributed_error_budget_burned of this SLOConsumptionBreakdown.  # noqa: E501


        :return: The contributed_error_budget_burned of this SLOConsumptionBreakdown.  # noqa: E501
        :rtype: int
        """
        return self._contributed_error_budget_burned

    @contributed_error_budget_burned.setter
    def contributed_error_budget_burned(self, contributed_error_budget_burned):
        """Sets the contributed_error_budget_burned of this SLOConsumptionBreakdown.


        :param contributed_error_budget_burned: The contributed_error_budget_burned of this SLOConsumptionBreakdown.  # noqa: E501
        :type: int
        """

        self._contributed_error_budget_burned = contributed_error_budget_burned

    @property
    def project_params(self):
        """Gets the project_params of this SLOConsumptionBreakdown.  # noqa: E501


        :return: The project_params of this SLOConsumptionBreakdown.  # noqa: E501
        :rtype: ProjectParams
        """
        return self._project_params

    @project_params.setter
    def project_params(self, project_params):
        """Sets the project_params of this SLOConsumptionBreakdown.


        :param project_params: The project_params of this SLOConsumptionBreakdown.  # noqa: E501
        :type: ProjectParams
        """
        if project_params is None:
            raise ValueError("Invalid value for `project_params`, must not be `None`")  # noqa: E501

        self._project_params = project_params

    @property
    def org_name(self):
        """Gets the org_name of this SLOConsumptionBreakdown.  # noqa: E501


        :return: The org_name of this SLOConsumptionBreakdown.  # noqa: E501
        :rtype: str
        """
        return self._org_name

    @org_name.setter
    def org_name(self, org_name):
        """Sets the org_name of this SLOConsumptionBreakdown.


        :param org_name: The org_name of this SLOConsumptionBreakdown.  # noqa: E501
        :type: str
        """

        self._org_name = org_name

    @property
    def project_name(self):
        """Gets the project_name of this SLOConsumptionBreakdown.  # noqa: E501


        :return: The project_name of this SLOConsumptionBreakdown.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this SLOConsumptionBreakdown.


        :param project_name: The project_name of this SLOConsumptionBreakdown.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def slo_error(self):
        """Gets the slo_error of this SLOConsumptionBreakdown.  # noqa: E501


        :return: The slo_error of this SLOConsumptionBreakdown.  # noqa: E501
        :rtype: SLOError
        """
        return self._slo_error

    @slo_error.setter
    def slo_error(self, slo_error):
        """Sets the slo_error of this SLOConsumptionBreakdown.


        :param slo_error: The slo_error of this SLOConsumptionBreakdown.  # noqa: E501
        :type: SLOError
        """

        self._slo_error = slo_error

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
        if issubclass(SLOConsumptionBreakdown, dict):
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
        if not isinstance(other, SLOConsumptionBreakdown):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
