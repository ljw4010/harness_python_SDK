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

class LDAPSettings(object):
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
        'connection_settings': 'LdapConnectionSettings',
        'identifier': 'str',
        'user_settings_list': 'list[LdapUserSettings]',
        'group_settings_list': 'list[LdapGroupSettings]',
        'display_name': 'str',
        'cron_expression': 'str',
        'next_iterations': 'list[int]',
        'disabled': 'bool',
        'settings_type': 'str'
    }

    attribute_map = {
        'connection_settings': 'connectionSettings',
        'identifier': 'identifier',
        'user_settings_list': 'userSettingsList',
        'group_settings_list': 'groupSettingsList',
        'display_name': 'displayName',
        'cron_expression': 'cronExpression',
        'next_iterations': 'nextIterations',
        'disabled': 'disabled',
        'settings_type': 'settingsType'
    }

    def __init__(self, connection_settings=None, identifier=None, user_settings_list=None, group_settings_list=None, display_name=None, cron_expression=None, next_iterations=None, disabled=None, settings_type=None):  # noqa: E501
        """LDAPSettings - a model defined in Swagger"""  # noqa: E501
        self._connection_settings = None
        self._identifier = None
        self._user_settings_list = None
        self._group_settings_list = None
        self._display_name = None
        self._cron_expression = None
        self._next_iterations = None
        self._disabled = None
        self._settings_type = None
        self.discriminator = None
        self.connection_settings = connection_settings
        self.identifier = identifier
        if user_settings_list is not None:
            self.user_settings_list = user_settings_list
        if group_settings_list is not None:
            self.group_settings_list = group_settings_list
        self.display_name = display_name
        if cron_expression is not None:
            self.cron_expression = cron_expression
        if next_iterations is not None:
            self.next_iterations = next_iterations
        if disabled is not None:
            self.disabled = disabled
        if settings_type is not None:
            self.settings_type = settings_type

    @property
    def connection_settings(self):
        """Gets the connection_settings of this LDAPSettings.  # noqa: E501


        :return: The connection_settings of this LDAPSettings.  # noqa: E501
        :rtype: LdapConnectionSettings
        """
        return self._connection_settings

    @connection_settings.setter
    def connection_settings(self, connection_settings):
        """Sets the connection_settings of this LDAPSettings.


        :param connection_settings: The connection_settings of this LDAPSettings.  # noqa: E501
        :type: LdapConnectionSettings
        """
        if connection_settings is None:
            raise ValueError("Invalid value for `connection_settings`, must not be `None`")  # noqa: E501

        self._connection_settings = connection_settings

    @property
    def identifier(self):
        """Gets the identifier of this LDAPSettings.  # noqa: E501

        This is the LDAP setting identifier.  # noqa: E501

        :return: The identifier of this LDAPSettings.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this LDAPSettings.

        This is the LDAP setting identifier.  # noqa: E501

        :param identifier: The identifier of this LDAPSettings.  # noqa: E501
        :type: str
        """
        if identifier is None:
            raise ValueError("Invalid value for `identifier`, must not be `None`")  # noqa: E501

        self._identifier = identifier

    @property
    def user_settings_list(self):
        """Gets the user_settings_list of this LDAPSettings.  # noqa: E501

        This is the user settings list in LDAP setting.  # noqa: E501

        :return: The user_settings_list of this LDAPSettings.  # noqa: E501
        :rtype: list[LdapUserSettings]
        """
        return self._user_settings_list

    @user_settings_list.setter
    def user_settings_list(self, user_settings_list):
        """Sets the user_settings_list of this LDAPSettings.

        This is the user settings list in LDAP setting.  # noqa: E501

        :param user_settings_list: The user_settings_list of this LDAPSettings.  # noqa: E501
        :type: list[LdapUserSettings]
        """

        self._user_settings_list = user_settings_list

    @property
    def group_settings_list(self):
        """Gets the group_settings_list of this LDAPSettings.  # noqa: E501

        This is the group settings list in LDAP setting.  # noqa: E501

        :return: The group_settings_list of this LDAPSettings.  # noqa: E501
        :rtype: list[LdapGroupSettings]
        """
        return self._group_settings_list

    @group_settings_list.setter
    def group_settings_list(self, group_settings_list):
        """Sets the group_settings_list of this LDAPSettings.

        This is the group settings list in LDAP setting.  # noqa: E501

        :param group_settings_list: The group_settings_list of this LDAPSettings.  # noqa: E501
        :type: list[LdapGroupSettings]
        """

        self._group_settings_list = group_settings_list

    @property
    def display_name(self):
        """Gets the display_name of this LDAPSettings.  # noqa: E501

        This is the LDAP setting display name.  # noqa: E501

        :return: The display_name of this LDAPSettings.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this LDAPSettings.

        This is the LDAP setting display name.  # noqa: E501

        :param display_name: The display_name of this LDAPSettings.  # noqa: E501
        :type: str
        """
        if display_name is None:
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def cron_expression(self):
        """Gets the cron_expression of this LDAPSettings.  # noqa: E501

        This is the cron expression in LDAP Settings.  # noqa: E501

        :return: The cron_expression of this LDAPSettings.  # noqa: E501
        :rtype: str
        """
        return self._cron_expression

    @cron_expression.setter
    def cron_expression(self, cron_expression):
        """Sets the cron_expression of this LDAPSettings.

        This is the cron expression in LDAP Settings.  # noqa: E501

        :param cron_expression: The cron_expression of this LDAPSettings.  # noqa: E501
        :type: str
        """

        self._cron_expression = cron_expression

    @property
    def next_iterations(self):
        """Gets the next_iterations of this LDAPSettings.  # noqa: E501

        This is the list of iterations for next LDAP sync job.  # noqa: E501

        :return: The next_iterations of this LDAPSettings.  # noqa: E501
        :rtype: list[int]
        """
        return self._next_iterations

    @next_iterations.setter
    def next_iterations(self, next_iterations):
        """Sets the next_iterations of this LDAPSettings.

        This is the list of iterations for next LDAP sync job.  # noqa: E501

        :param next_iterations: The next_iterations of this LDAPSettings.  # noqa: E501
        :type: list[int]
        """

        self._next_iterations = next_iterations

    @property
    def disabled(self):
        """Gets the disabled of this LDAPSettings.  # noqa: E501

        This tells if LDAP Settings is disabled or not, LDAP sync won't happen in disabled state.  # noqa: E501

        :return: The disabled of this LDAPSettings.  # noqa: E501
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this LDAPSettings.

        This tells if LDAP Settings is disabled or not, LDAP sync won't happen in disabled state.  # noqa: E501

        :param disabled: The disabled of this LDAPSettings.  # noqa: E501
        :type: bool
        """

        self._disabled = disabled

    @property
    def settings_type(self):
        """Gets the settings_type of this LDAPSettings.  # noqa: E501


        :return: The settings_type of this LDAPSettings.  # noqa: E501
        :rtype: str
        """
        return self._settings_type

    @settings_type.setter
    def settings_type(self, settings_type):
        """Sets the settings_type of this LDAPSettings.


        :param settings_type: The settings_type of this LDAPSettings.  # noqa: E501
        :type: str
        """
        allowed_values = ["USER_PASSWORD", "SAML", "LDAP", "OAUTH"]  # noqa: E501
        if settings_type not in allowed_values:
            raise ValueError(
                "Invalid value for `settings_type` ({0}), must be one of {1}"  # noqa: E501
                .format(settings_type, allowed_values)
            )

        self._settings_type = settings_type

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
        if issubclass(LDAPSettings, dict):
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
        if not isinstance(other, LDAPSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
