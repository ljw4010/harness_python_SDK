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

class CEReportSchedule(object):
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
        'uuid': 'str',
        'name': 'str',
        'enabled': 'bool',
        'description': 'str',
        'views_id': 'list[str]',
        'user_cron': 'str',
        'recipients': 'list[str]',
        'account_id': 'str',
        'created_at': 'int',
        'last_updated_at': 'int',
        'user_cron_time_zone': 'str',
        'created_by': 'EmbeddedUser',
        'last_updated_by': 'EmbeddedUser',
        'next_execution': 'datetime'
    }

    attribute_map = {
        'uuid': 'uuid',
        'name': 'name',
        'enabled': 'enabled',
        'description': 'description',
        'views_id': 'viewsId',
        'user_cron': 'userCron',
        'recipients': 'recipients',
        'account_id': 'accountId',
        'created_at': 'createdAt',
        'last_updated_at': 'lastUpdatedAt',
        'user_cron_time_zone': 'userCronTimeZone',
        'created_by': 'createdBy',
        'last_updated_by': 'lastUpdatedBy',
        'next_execution': 'nextExecution'
    }

    def __init__(self, uuid=None, name=None, enabled=None, description=None, views_id=None, user_cron=None, recipients=None, account_id=None, created_at=None, last_updated_at=None, user_cron_time_zone=None, created_by=None, last_updated_by=None, next_execution=None):  # noqa: E501
        """CEReportSchedule - a model defined in Swagger"""  # noqa: E501
        self._uuid = None
        self._name = None
        self._enabled = None
        self._description = None
        self._views_id = None
        self._user_cron = None
        self._recipients = None
        self._account_id = None
        self._created_at = None
        self._last_updated_at = None
        self._user_cron_time_zone = None
        self._created_by = None
        self._last_updated_by = None
        self._next_execution = None
        self.discriminator = None
        if uuid is not None:
            self.uuid = uuid
        self.name = name
        if enabled is not None:
            self.enabled = enabled
        if description is not None:
            self.description = description
        self.views_id = views_id
        self.user_cron = user_cron
        self.recipients = recipients
        if account_id is not None:
            self.account_id = account_id
        if created_at is not None:
            self.created_at = created_at
        if last_updated_at is not None:
            self.last_updated_at = last_updated_at
        if user_cron_time_zone is not None:
            self.user_cron_time_zone = user_cron_time_zone
        if created_by is not None:
            self.created_by = created_by
        if last_updated_by is not None:
            self.last_updated_by = last_updated_by
        if next_execution is not None:
            self.next_execution = next_execution

    @property
    def uuid(self):
        """Gets the uuid of this CEReportSchedule.  # noqa: E501


        :return: The uuid of this CEReportSchedule.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this CEReportSchedule.


        :param uuid: The uuid of this CEReportSchedule.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def name(self):
        """Gets the name of this CEReportSchedule.  # noqa: E501


        :return: The name of this CEReportSchedule.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CEReportSchedule.


        :param name: The name of this CEReportSchedule.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def enabled(self):
        """Gets the enabled of this CEReportSchedule.  # noqa: E501


        :return: The enabled of this CEReportSchedule.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this CEReportSchedule.


        :param enabled: The enabled of this CEReportSchedule.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def description(self):
        """Gets the description of this CEReportSchedule.  # noqa: E501


        :return: The description of this CEReportSchedule.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CEReportSchedule.


        :param description: The description of this CEReportSchedule.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def views_id(self):
        """Gets the views_id of this CEReportSchedule.  # noqa: E501


        :return: The views_id of this CEReportSchedule.  # noqa: E501
        :rtype: list[str]
        """
        return self._views_id

    @views_id.setter
    def views_id(self, views_id):
        """Sets the views_id of this CEReportSchedule.


        :param views_id: The views_id of this CEReportSchedule.  # noqa: E501
        :type: list[str]
        """
        if views_id is None:
            raise ValueError("Invalid value for `views_id`, must not be `None`")  # noqa: E501

        self._views_id = views_id

    @property
    def user_cron(self):
        """Gets the user_cron of this CEReportSchedule.  # noqa: E501


        :return: The user_cron of this CEReportSchedule.  # noqa: E501
        :rtype: str
        """
        return self._user_cron

    @user_cron.setter
    def user_cron(self, user_cron):
        """Sets the user_cron of this CEReportSchedule.


        :param user_cron: The user_cron of this CEReportSchedule.  # noqa: E501
        :type: str
        """
        if user_cron is None:
            raise ValueError("Invalid value for `user_cron`, must not be `None`")  # noqa: E501

        self._user_cron = user_cron

    @property
    def recipients(self):
        """Gets the recipients of this CEReportSchedule.  # noqa: E501


        :return: The recipients of this CEReportSchedule.  # noqa: E501
        :rtype: list[str]
        """
        return self._recipients

    @recipients.setter
    def recipients(self, recipients):
        """Sets the recipients of this CEReportSchedule.


        :param recipients: The recipients of this CEReportSchedule.  # noqa: E501
        :type: list[str]
        """
        if recipients is None:
            raise ValueError("Invalid value for `recipients`, must not be `None`")  # noqa: E501

        self._recipients = recipients

    @property
    def account_id(self):
        """Gets the account_id of this CEReportSchedule.  # noqa: E501


        :return: The account_id of this CEReportSchedule.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this CEReportSchedule.


        :param account_id: The account_id of this CEReportSchedule.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def created_at(self):
        """Gets the created_at of this CEReportSchedule.  # noqa: E501


        :return: The created_at of this CEReportSchedule.  # noqa: E501
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this CEReportSchedule.


        :param created_at: The created_at of this CEReportSchedule.  # noqa: E501
        :type: int
        """

        self._created_at = created_at

    @property
    def last_updated_at(self):
        """Gets the last_updated_at of this CEReportSchedule.  # noqa: E501


        :return: The last_updated_at of this CEReportSchedule.  # noqa: E501
        :rtype: int
        """
        return self._last_updated_at

    @last_updated_at.setter
    def last_updated_at(self, last_updated_at):
        """Sets the last_updated_at of this CEReportSchedule.


        :param last_updated_at: The last_updated_at of this CEReportSchedule.  # noqa: E501
        :type: int
        """

        self._last_updated_at = last_updated_at

    @property
    def user_cron_time_zone(self):
        """Gets the user_cron_time_zone of this CEReportSchedule.  # noqa: E501


        :return: The user_cron_time_zone of this CEReportSchedule.  # noqa: E501
        :rtype: str
        """
        return self._user_cron_time_zone

    @user_cron_time_zone.setter
    def user_cron_time_zone(self, user_cron_time_zone):
        """Sets the user_cron_time_zone of this CEReportSchedule.


        :param user_cron_time_zone: The user_cron_time_zone of this CEReportSchedule.  # noqa: E501
        :type: str
        """

        self._user_cron_time_zone = user_cron_time_zone

    @property
    def created_by(self):
        """Gets the created_by of this CEReportSchedule.  # noqa: E501


        :return: The created_by of this CEReportSchedule.  # noqa: E501
        :rtype: EmbeddedUser
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this CEReportSchedule.


        :param created_by: The created_by of this CEReportSchedule.  # noqa: E501
        :type: EmbeddedUser
        """

        self._created_by = created_by

    @property
    def last_updated_by(self):
        """Gets the last_updated_by of this CEReportSchedule.  # noqa: E501


        :return: The last_updated_by of this CEReportSchedule.  # noqa: E501
        :rtype: EmbeddedUser
        """
        return self._last_updated_by

    @last_updated_by.setter
    def last_updated_by(self, last_updated_by):
        """Sets the last_updated_by of this CEReportSchedule.


        :param last_updated_by: The last_updated_by of this CEReportSchedule.  # noqa: E501
        :type: EmbeddedUser
        """

        self._last_updated_by = last_updated_by

    @property
    def next_execution(self):
        """Gets the next_execution of this CEReportSchedule.  # noqa: E501


        :return: The next_execution of this CEReportSchedule.  # noqa: E501
        :rtype: datetime
        """
        return self._next_execution

    @next_execution.setter
    def next_execution(self, next_execution):
        """Sets the next_execution of this CEReportSchedule.


        :param next_execution: The next_execution of this CEReportSchedule.  # noqa: E501
        :type: datetime
        """

        self._next_execution = next_execution

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
        if issubclass(CEReportSchedule, dict):
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
        if not isinstance(other, CEReportSchedule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
