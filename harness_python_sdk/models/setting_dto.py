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

class SettingDTO(object):
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
        'name': 'str',
        'org_identifier': 'str',
        'project_identifier': 'str',
        'category': 'str',
        'group_identifier': 'str',
        'value_type': 'str',
        'allowed_values': 'list[str]',
        'allow_overrides': 'bool',
        'value': 'str',
        'default_value': 'str',
        'setting_source': 'str',
        'is_setting_editable': 'bool',
        'allowed_scopes': 'list[str]'
    }

    attribute_map = {
        'identifier': 'identifier',
        'name': 'name',
        'org_identifier': 'orgIdentifier',
        'project_identifier': 'projectIdentifier',
        'category': 'category',
        'group_identifier': 'groupIdentifier',
        'value_type': 'valueType',
        'allowed_values': 'allowedValues',
        'allow_overrides': 'allowOverrides',
        'value': 'value',
        'default_value': 'defaultValue',
        'setting_source': 'settingSource',
        'is_setting_editable': 'isSettingEditable',
        'allowed_scopes': 'allowedScopes'
    }

    def __init__(self, identifier=None, name=None, org_identifier=None, project_identifier=None, category=None, group_identifier=None, value_type=None, allowed_values=None, allow_overrides=None, value=None, default_value=None, setting_source=None, is_setting_editable=None, allowed_scopes=None):  # noqa: E501
        """SettingDTO - a model defined in Swagger"""  # noqa: E501
        self._identifier = None
        self._name = None
        self._org_identifier = None
        self._project_identifier = None
        self._category = None
        self._group_identifier = None
        self._value_type = None
        self._allowed_values = None
        self._allow_overrides = None
        self._value = None
        self._default_value = None
        self._setting_source = None
        self._is_setting_editable = None
        self._allowed_scopes = None
        self.discriminator = None
        self.identifier = identifier
        self.name = name
        if org_identifier is not None:
            self.org_identifier = org_identifier
        if project_identifier is not None:
            self.project_identifier = project_identifier
        self.category = category
        self.group_identifier = group_identifier
        self.value_type = value_type
        if allowed_values is not None:
            self.allowed_values = allowed_values
        self.allow_overrides = allow_overrides
        if value is not None:
            self.value = value
        if default_value is not None:
            self.default_value = default_value
        if setting_source is not None:
            self.setting_source = setting_source
        self.is_setting_editable = is_setting_editable
        self.allowed_scopes = allowed_scopes

    @property
    def identifier(self):
        """Gets the identifier of this SettingDTO.  # noqa: E501

        Identifier of the Setting.  # noqa: E501

        :return: The identifier of this SettingDTO.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this SettingDTO.

        Identifier of the Setting.  # noqa: E501

        :param identifier: The identifier of this SettingDTO.  # noqa: E501
        :type: str
        """
        if identifier is None:
            raise ValueError("Invalid value for `identifier`, must not be `None`")  # noqa: E501

        self._identifier = identifier

    @property
    def name(self):
        """Gets the name of this SettingDTO.  # noqa: E501

        Name of the Setting.  # noqa: E501

        :return: The name of this SettingDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SettingDTO.

        Name of the Setting.  # noqa: E501

        :param name: The name of this SettingDTO.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def org_identifier(self):
        """Gets the org_identifier of this SettingDTO.  # noqa: E501

        Organization Identifier for the Entity.  # noqa: E501

        :return: The org_identifier of this SettingDTO.  # noqa: E501
        :rtype: str
        """
        return self._org_identifier

    @org_identifier.setter
    def org_identifier(self, org_identifier):
        """Sets the org_identifier of this SettingDTO.

        Organization Identifier for the Entity.  # noqa: E501

        :param org_identifier: The org_identifier of this SettingDTO.  # noqa: E501
        :type: str
        """

        self._org_identifier = org_identifier

    @property
    def project_identifier(self):
        """Gets the project_identifier of this SettingDTO.  # noqa: E501

        Project Identifier for the Entity.  # noqa: E501

        :return: The project_identifier of this SettingDTO.  # noqa: E501
        :rtype: str
        """
        return self._project_identifier

    @project_identifier.setter
    def project_identifier(self, project_identifier):
        """Sets the project_identifier of this SettingDTO.

        Project Identifier for the Entity.  # noqa: E501

        :param project_identifier: The project_identifier of this SettingDTO.  # noqa: E501
        :type: str
        """

        self._project_identifier = project_identifier

    @property
    def category(self):
        """Gets the category of this SettingDTO.  # noqa: E501

        Category of the Setting.  # noqa: E501

        :return: The category of this SettingDTO.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this SettingDTO.

        Category of the Setting.  # noqa: E501

        :param category: The category of this SettingDTO.  # noqa: E501
        :type: str
        """
        if category is None:
            raise ValueError("Invalid value for `category`, must not be `None`")  # noqa: E501
        allowed_values = ["CD", "CI", "CE", "CV", "CF", "STO", "CORE", "PMS", "TEMPLATESERVICE", "GOVERNANCE", "CHAOS", "SCIM", "GIT_EXPERIENCE", "CONNECTORS", "EULA", "NOTIFICATIONS"]  # noqa: E501
        if category not in allowed_values:
            raise ValueError(
                "Invalid value for `category` ({0}), must be one of {1}"  # noqa: E501
                .format(category, allowed_values)
            )

        self._category = category

    @property
    def group_identifier(self):
        """Gets the group_identifier of this SettingDTO.  # noqa: E501

        Group Id of the setting  # noqa: E501

        :return: The group_identifier of this SettingDTO.  # noqa: E501
        :rtype: str
        """
        return self._group_identifier

    @group_identifier.setter
    def group_identifier(self, group_identifier):
        """Sets the group_identifier of this SettingDTO.

        Group Id of the setting  # noqa: E501

        :param group_identifier: The group_identifier of this SettingDTO.  # noqa: E501
        :type: str
        """
        if group_identifier is None:
            raise ValueError("Invalid value for `group_identifier`, must not be `None`")  # noqa: E501

        self._group_identifier = group_identifier

    @property
    def value_type(self):
        """Gets the value_type of this SettingDTO.  # noqa: E501

        Type of Value of the Setting.  # noqa: E501

        :return: The value_type of this SettingDTO.  # noqa: E501
        :rtype: str
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        """Sets the value_type of this SettingDTO.

        Type of Value of the Setting.  # noqa: E501

        :param value_type: The value_type of this SettingDTO.  # noqa: E501
        :type: str
        """
        if value_type is None:
            raise ValueError("Invalid value for `value_type`, must not be `None`")  # noqa: E501
        allowed_values = ["String", "Boolean", "Number"]  # noqa: E501
        if value_type not in allowed_values:
            raise ValueError(
                "Invalid value for `value_type` ({0}), must be one of {1}"  # noqa: E501
                .format(value_type, allowed_values)
            )

        self._value_type = value_type

    @property
    def allowed_values(self):
        """Gets the allowed_values of this SettingDTO.  # noqa: E501

        Set of Values allowed for the Setting.  # noqa: E501

        :return: The allowed_values of this SettingDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._allowed_values

    @allowed_values.setter
    def allowed_values(self, allowed_values):
        """Sets the allowed_values of this SettingDTO.

        Set of Values allowed for the Setting.  # noqa: E501

        :param allowed_values: The allowed_values of this SettingDTO.  # noqa: E501
        :type: list[str]
        """

        self._allowed_values = allowed_values

    @property
    def allow_overrides(self):
        """Gets the allow_overrides of this SettingDTO.  # noqa: E501

        Allow override of the Setting in sub-scopes.  # noqa: E501

        :return: The allow_overrides of this SettingDTO.  # noqa: E501
        :rtype: bool
        """
        return self._allow_overrides

    @allow_overrides.setter
    def allow_overrides(self, allow_overrides):
        """Sets the allow_overrides of this SettingDTO.

        Allow override of the Setting in sub-scopes.  # noqa: E501

        :param allow_overrides: The allow_overrides of this SettingDTO.  # noqa: E501
        :type: bool
        """
        if allow_overrides is None:
            raise ValueError("Invalid value for `allow_overrides`, must not be `None`")  # noqa: E501

        self._allow_overrides = allow_overrides

    @property
    def value(self):
        """Gets the value of this SettingDTO.  # noqa: E501

        Value of the setting  # noqa: E501

        :return: The value of this SettingDTO.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this SettingDTO.

        Value of the setting  # noqa: E501

        :param value: The value of this SettingDTO.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def default_value(self):
        """Gets the default_value of this SettingDTO.  # noqa: E501

        Default Value of the Setting.  # noqa: E501

        :return: The default_value of this SettingDTO.  # noqa: E501
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Sets the default_value of this SettingDTO.

        Default Value of the Setting.  # noqa: E501

        :param default_value: The default_value of this SettingDTO.  # noqa: E501
        :type: str
        """

        self._default_value = default_value

    @property
    def setting_source(self):
        """Gets the setting_source of this SettingDTO.  # noqa: E501

        Source of the setting value  # noqa: E501

        :return: The setting_source of this SettingDTO.  # noqa: E501
        :rtype: str
        """
        return self._setting_source

    @setting_source.setter
    def setting_source(self, setting_source):
        """Sets the setting_source of this SettingDTO.

        Source of the setting value  # noqa: E501

        :param setting_source: The setting_source of this SettingDTO.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACCOUNT", "ORG", "PROJECT", "DEFAULT"]  # noqa: E501
        if setting_source not in allowed_values:
            raise ValueError(
                "Invalid value for `setting_source` ({0}), must be one of {1}"  # noqa: E501
                .format(setting_source, allowed_values)
            )

        self._setting_source = setting_source

    @property
    def is_setting_editable(self):
        """Gets the is_setting_editable of this SettingDTO.  # noqa: E501

        Is the setting editable at the current scope  # noqa: E501

        :return: The is_setting_editable of this SettingDTO.  # noqa: E501
        :rtype: bool
        """
        return self._is_setting_editable

    @is_setting_editable.setter
    def is_setting_editable(self, is_setting_editable):
        """Sets the is_setting_editable of this SettingDTO.

        Is the setting editable at the current scope  # noqa: E501

        :param is_setting_editable: The is_setting_editable of this SettingDTO.  # noqa: E501
        :type: bool
        """
        if is_setting_editable is None:
            raise ValueError("Invalid value for `is_setting_editable`, must not be `None`")  # noqa: E501

        self._is_setting_editable = is_setting_editable

    @property
    def allowed_scopes(self):
        """Gets the allowed_scopes of this SettingDTO.  # noqa: E501

        List of scopes where the setting is available  # noqa: E501

        :return: The allowed_scopes of this SettingDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._allowed_scopes

    @allowed_scopes.setter
    def allowed_scopes(self, allowed_scopes):
        """Sets the allowed_scopes of this SettingDTO.

        List of scopes where the setting is available  # noqa: E501

        :param allowed_scopes: The allowed_scopes of this SettingDTO.  # noqa: E501
        :type: list[str]
        """
        if allowed_scopes is None:
            raise ValueError("Invalid value for `allowed_scopes`, must not be `None`")  # noqa: E501
        allowed_values = ["ACCOUNT", "ORGANIZATION", "PROJECT"]  # noqa: E501
        if not set(allowed_scopes).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `allowed_scopes` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(allowed_scopes) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._allowed_scopes = allowed_scopes

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
        if issubclass(SettingDTO, dict):
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
        if not isinstance(other, SettingDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
