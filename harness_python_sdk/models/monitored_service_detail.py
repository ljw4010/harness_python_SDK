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

class MonitoredServiceDetail(object):
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
        'monitored_service_identifier': 'str',
        'monitored_service_name': 'str',
        'health_source_identifier': 'str',
        'health_source_name': 'str',
        'service_identifier': 'str',
        'service_name': 'str',
        'environment_identifier': 'str',
        'environment_name': 'str',
        'project_params': 'ProjectParams',
        'project_name': 'str',
        'org_name': 'str'
    }

    attribute_map = {
        'monitored_service_identifier': 'monitoredServiceIdentifier',
        'monitored_service_name': 'monitoredServiceName',
        'health_source_identifier': 'healthSourceIdentifier',
        'health_source_name': 'healthSourceName',
        'service_identifier': 'serviceIdentifier',
        'service_name': 'serviceName',
        'environment_identifier': 'environmentIdentifier',
        'environment_name': 'environmentName',
        'project_params': 'projectParams',
        'project_name': 'projectName',
        'org_name': 'orgName'
    }

    def __init__(self, monitored_service_identifier=None, monitored_service_name=None, health_source_identifier=None, health_source_name=None, service_identifier=None, service_name=None, environment_identifier=None, environment_name=None, project_params=None, project_name=None, org_name=None):  # noqa: E501
        """MonitoredServiceDetail - a model defined in Swagger"""  # noqa: E501
        self._monitored_service_identifier = None
        self._monitored_service_name = None
        self._health_source_identifier = None
        self._health_source_name = None
        self._service_identifier = None
        self._service_name = None
        self._environment_identifier = None
        self._environment_name = None
        self._project_params = None
        self._project_name = None
        self._org_name = None
        self.discriminator = None
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
        if project_params is not None:
            self.project_params = project_params
        if project_name is not None:
            self.project_name = project_name
        if org_name is not None:
            self.org_name = org_name

    @property
    def monitored_service_identifier(self):
        """Gets the monitored_service_identifier of this MonitoredServiceDetail.  # noqa: E501


        :return: The monitored_service_identifier of this MonitoredServiceDetail.  # noqa: E501
        :rtype: str
        """
        return self._monitored_service_identifier

    @monitored_service_identifier.setter
    def monitored_service_identifier(self, monitored_service_identifier):
        """Sets the monitored_service_identifier of this MonitoredServiceDetail.


        :param monitored_service_identifier: The monitored_service_identifier of this MonitoredServiceDetail.  # noqa: E501
        :type: str
        """

        self._monitored_service_identifier = monitored_service_identifier

    @property
    def monitored_service_name(self):
        """Gets the monitored_service_name of this MonitoredServiceDetail.  # noqa: E501


        :return: The monitored_service_name of this MonitoredServiceDetail.  # noqa: E501
        :rtype: str
        """
        return self._monitored_service_name

    @monitored_service_name.setter
    def monitored_service_name(self, monitored_service_name):
        """Sets the monitored_service_name of this MonitoredServiceDetail.


        :param monitored_service_name: The monitored_service_name of this MonitoredServiceDetail.  # noqa: E501
        :type: str
        """

        self._monitored_service_name = monitored_service_name

    @property
    def health_source_identifier(self):
        """Gets the health_source_identifier of this MonitoredServiceDetail.  # noqa: E501


        :return: The health_source_identifier of this MonitoredServiceDetail.  # noqa: E501
        :rtype: str
        """
        return self._health_source_identifier

    @health_source_identifier.setter
    def health_source_identifier(self, health_source_identifier):
        """Sets the health_source_identifier of this MonitoredServiceDetail.


        :param health_source_identifier: The health_source_identifier of this MonitoredServiceDetail.  # noqa: E501
        :type: str
        """

        self._health_source_identifier = health_source_identifier

    @property
    def health_source_name(self):
        """Gets the health_source_name of this MonitoredServiceDetail.  # noqa: E501


        :return: The health_source_name of this MonitoredServiceDetail.  # noqa: E501
        :rtype: str
        """
        return self._health_source_name

    @health_source_name.setter
    def health_source_name(self, health_source_name):
        """Sets the health_source_name of this MonitoredServiceDetail.


        :param health_source_name: The health_source_name of this MonitoredServiceDetail.  # noqa: E501
        :type: str
        """

        self._health_source_name = health_source_name

    @property
    def service_identifier(self):
        """Gets the service_identifier of this MonitoredServiceDetail.  # noqa: E501


        :return: The service_identifier of this MonitoredServiceDetail.  # noqa: E501
        :rtype: str
        """
        return self._service_identifier

    @service_identifier.setter
    def service_identifier(self, service_identifier):
        """Sets the service_identifier of this MonitoredServiceDetail.


        :param service_identifier: The service_identifier of this MonitoredServiceDetail.  # noqa: E501
        :type: str
        """

        self._service_identifier = service_identifier

    @property
    def service_name(self):
        """Gets the service_name of this MonitoredServiceDetail.  # noqa: E501


        :return: The service_name of this MonitoredServiceDetail.  # noqa: E501
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """Sets the service_name of this MonitoredServiceDetail.


        :param service_name: The service_name of this MonitoredServiceDetail.  # noqa: E501
        :type: str
        """

        self._service_name = service_name

    @property
    def environment_identifier(self):
        """Gets the environment_identifier of this MonitoredServiceDetail.  # noqa: E501


        :return: The environment_identifier of this MonitoredServiceDetail.  # noqa: E501
        :rtype: str
        """
        return self._environment_identifier

    @environment_identifier.setter
    def environment_identifier(self, environment_identifier):
        """Sets the environment_identifier of this MonitoredServiceDetail.


        :param environment_identifier: The environment_identifier of this MonitoredServiceDetail.  # noqa: E501
        :type: str
        """

        self._environment_identifier = environment_identifier

    @property
    def environment_name(self):
        """Gets the environment_name of this MonitoredServiceDetail.  # noqa: E501


        :return: The environment_name of this MonitoredServiceDetail.  # noqa: E501
        :rtype: str
        """
        return self._environment_name

    @environment_name.setter
    def environment_name(self, environment_name):
        """Sets the environment_name of this MonitoredServiceDetail.


        :param environment_name: The environment_name of this MonitoredServiceDetail.  # noqa: E501
        :type: str
        """

        self._environment_name = environment_name

    @property
    def project_params(self):
        """Gets the project_params of this MonitoredServiceDetail.  # noqa: E501


        :return: The project_params of this MonitoredServiceDetail.  # noqa: E501
        :rtype: ProjectParams
        """
        return self._project_params

    @project_params.setter
    def project_params(self, project_params):
        """Sets the project_params of this MonitoredServiceDetail.


        :param project_params: The project_params of this MonitoredServiceDetail.  # noqa: E501
        :type: ProjectParams
        """

        self._project_params = project_params

    @property
    def project_name(self):
        """Gets the project_name of this MonitoredServiceDetail.  # noqa: E501


        :return: The project_name of this MonitoredServiceDetail.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this MonitoredServiceDetail.


        :param project_name: The project_name of this MonitoredServiceDetail.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def org_name(self):
        """Gets the org_name of this MonitoredServiceDetail.  # noqa: E501


        :return: The org_name of this MonitoredServiceDetail.  # noqa: E501
        :rtype: str
        """
        return self._org_name

    @org_name.setter
    def org_name(self, org_name):
        """Sets the org_name of this MonitoredServiceDetail.


        :param org_name: The org_name of this MonitoredServiceDetail.  # noqa: E501
        :type: str
        """

        self._org_name = org_name

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
        if issubclass(MonitoredServiceDetail, dict):
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
        if not isinstance(other, MonitoredServiceDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
