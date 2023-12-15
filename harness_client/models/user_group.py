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

class UserGroup(object):
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
        'account_identifier': 'str',
        'org_identifier': 'str',
        'project_identifier': 'str',
        'identifier': 'str',
        'name': 'str',
        'users': 'list[str]',
        'notification_configs': 'list[NotificationSettingConfigDTO]',
        'is_sso_linked': 'bool',
        'linked_sso_id': 'str',
        'linked_sso_display_name': 'str',
        'sso_group_id': 'str',
        'sso_group_name': 'str',
        'linked_sso_type': 'str',
        'externally_managed': 'bool',
        'description': 'str',
        'tags': 'dict(str, str)',
        'harness_managed': 'bool',
        'sso_linked': 'bool'
    }

    attribute_map = {
        'account_identifier': 'accountIdentifier',
        'org_identifier': 'orgIdentifier',
        'project_identifier': 'projectIdentifier',
        'identifier': 'identifier',
        'name': 'name',
        'users': 'users',
        'notification_configs': 'notificationConfigs',
        'is_sso_linked': 'isSsoLinked',
        'linked_sso_id': 'linkedSsoId',
        'linked_sso_display_name': 'linkedSsoDisplayName',
        'sso_group_id': 'ssoGroupId',
        'sso_group_name': 'ssoGroupName',
        'linked_sso_type': 'linkedSsoType',
        'externally_managed': 'externallyManaged',
        'description': 'description',
        'tags': 'tags',
        'harness_managed': 'harnessManaged',
        'sso_linked': 'ssoLinked'
    }

    def __init__(self, account_identifier=None, org_identifier=None, project_identifier=None, identifier=None, name=None, users=None, notification_configs=None, is_sso_linked=None, linked_sso_id=None, linked_sso_display_name=None, sso_group_id=None, sso_group_name=None, linked_sso_type=None, externally_managed=None, description=None, tags=None, harness_managed=None, sso_linked=None):  # noqa: E501
        """UserGroup - a model defined in Swagger"""  # noqa: E501
        self._account_identifier = None
        self._org_identifier = None
        self._project_identifier = None
        self._identifier = None
        self._name = None
        self._users = None
        self._notification_configs = None
        self._is_sso_linked = None
        self._linked_sso_id = None
        self._linked_sso_display_name = None
        self._sso_group_id = None
        self._sso_group_name = None
        self._linked_sso_type = None
        self._externally_managed = None
        self._description = None
        self._tags = None
        self._harness_managed = None
        self._sso_linked = None
        self.discriminator = None
        if account_identifier is not None:
            self.account_identifier = account_identifier
        if org_identifier is not None:
            self.org_identifier = org_identifier
        if project_identifier is not None:
            self.project_identifier = project_identifier
        self.identifier = identifier
        self.name = name
        if users is not None:
            self.users = users
        if notification_configs is not None:
            self.notification_configs = notification_configs
        if is_sso_linked is not None:
            self.is_sso_linked = is_sso_linked
        if linked_sso_id is not None:
            self.linked_sso_id = linked_sso_id
        if linked_sso_display_name is not None:
            self.linked_sso_display_name = linked_sso_display_name
        if sso_group_id is not None:
            self.sso_group_id = sso_group_id
        if sso_group_name is not None:
            self.sso_group_name = sso_group_name
        if linked_sso_type is not None:
            self.linked_sso_type = linked_sso_type
        if externally_managed is not None:
            self.externally_managed = externally_managed
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags
        if harness_managed is not None:
            self.harness_managed = harness_managed
        if sso_linked is not None:
            self.sso_linked = sso_linked

    @property
    def account_identifier(self):
        """Gets the account_identifier of this UserGroup.  # noqa: E501

        Account Identifier for the Entity.  # noqa: E501

        :return: The account_identifier of this UserGroup.  # noqa: E501
        :rtype: str
        """
        return self._account_identifier

    @account_identifier.setter
    def account_identifier(self, account_identifier):
        """Sets the account_identifier of this UserGroup.

        Account Identifier for the Entity.  # noqa: E501

        :param account_identifier: The account_identifier of this UserGroup.  # noqa: E501
        :type: str
        """

        self._account_identifier = account_identifier

    @property
    def org_identifier(self):
        """Gets the org_identifier of this UserGroup.  # noqa: E501

        Organization Identifier for the Entity.  # noqa: E501

        :return: The org_identifier of this UserGroup.  # noqa: E501
        :rtype: str
        """
        return self._org_identifier

    @org_identifier.setter
    def org_identifier(self, org_identifier):
        """Sets the org_identifier of this UserGroup.

        Organization Identifier for the Entity.  # noqa: E501

        :param org_identifier: The org_identifier of this UserGroup.  # noqa: E501
        :type: str
        """

        self._org_identifier = org_identifier

    @property
    def project_identifier(self):
        """Gets the project_identifier of this UserGroup.  # noqa: E501

        Project Identifier for the Entity.  # noqa: E501

        :return: The project_identifier of this UserGroup.  # noqa: E501
        :rtype: str
        """
        return self._project_identifier

    @project_identifier.setter
    def project_identifier(self, project_identifier):
        """Sets the project_identifier of this UserGroup.

        Project Identifier for the Entity.  # noqa: E501

        :param project_identifier: The project_identifier of this UserGroup.  # noqa: E501
        :type: str
        """

        self._project_identifier = project_identifier

    @property
    def identifier(self):
        """Gets the identifier of this UserGroup.  # noqa: E501

        Identifier of the UserGroup.  # noqa: E501

        :return: The identifier of this UserGroup.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this UserGroup.

        Identifier of the UserGroup.  # noqa: E501

        :param identifier: The identifier of this UserGroup.  # noqa: E501
        :type: str
        """
        if identifier is None:
            raise ValueError("Invalid value for `identifier`, must not be `None`")  # noqa: E501

        self._identifier = identifier

    @property
    def name(self):
        """Gets the name of this UserGroup.  # noqa: E501

        Name of the UserGroup.  # noqa: E501

        :return: The name of this UserGroup.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UserGroup.

        Name of the UserGroup.  # noqa: E501

        :param name: The name of this UserGroup.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def users(self):
        """Gets the users of this UserGroup.  # noqa: E501

        List of users ids in the UserGroup.  # noqa: E501

        :return: The users of this UserGroup.  # noqa: E501
        :rtype: list[str]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this UserGroup.

        List of users ids in the UserGroup.  # noqa: E501

        :param users: The users of this UserGroup.  # noqa: E501
        :type: list[str]
        """

        self._users = users

    @property
    def notification_configs(self):
        """Gets the notification_configs of this UserGroup.  # noqa: E501

        List of notification settings.  # noqa: E501

        :return: The notification_configs of this UserGroup.  # noqa: E501
        :rtype: list[NotificationSettingConfigDTO]
        """
        return self._notification_configs

    @notification_configs.setter
    def notification_configs(self, notification_configs):
        """Sets the notification_configs of this UserGroup.

        List of notification settings.  # noqa: E501

        :param notification_configs: The notification_configs of this UserGroup.  # noqa: E501
        :type: list[NotificationSettingConfigDTO]
        """

        self._notification_configs = notification_configs

    @property
    def is_sso_linked(self):
        """Gets the is_sso_linked of this UserGroup.  # noqa: E501


        :return: The is_sso_linked of this UserGroup.  # noqa: E501
        :rtype: bool
        """
        return self._is_sso_linked

    @is_sso_linked.setter
    def is_sso_linked(self, is_sso_linked):
        """Sets the is_sso_linked of this UserGroup.


        :param is_sso_linked: The is_sso_linked of this UserGroup.  # noqa: E501
        :type: bool
        """

        self._is_sso_linked = is_sso_linked

    @property
    def linked_sso_id(self):
        """Gets the linked_sso_id of this UserGroup.  # noqa: E501

        Identifier of the linked SSO.  # noqa: E501

        :return: The linked_sso_id of this UserGroup.  # noqa: E501
        :rtype: str
        """
        return self._linked_sso_id

    @linked_sso_id.setter
    def linked_sso_id(self, linked_sso_id):
        """Sets the linked_sso_id of this UserGroup.

        Identifier of the linked SSO.  # noqa: E501

        :param linked_sso_id: The linked_sso_id of this UserGroup.  # noqa: E501
        :type: str
        """

        self._linked_sso_id = linked_sso_id

    @property
    def linked_sso_display_name(self):
        """Gets the linked_sso_display_name of this UserGroup.  # noqa: E501

        Name of the linked SSO.  # noqa: E501

        :return: The linked_sso_display_name of this UserGroup.  # noqa: E501
        :rtype: str
        """
        return self._linked_sso_display_name

    @linked_sso_display_name.setter
    def linked_sso_display_name(self, linked_sso_display_name):
        """Sets the linked_sso_display_name of this UserGroup.

        Name of the linked SSO.  # noqa: E501

        :param linked_sso_display_name: The linked_sso_display_name of this UserGroup.  # noqa: E501
        :type: str
        """

        self._linked_sso_display_name = linked_sso_display_name

    @property
    def sso_group_id(self):
        """Gets the sso_group_id of this UserGroup.  # noqa: E501

        Identifier of the userGroup in SSO.  # noqa: E501

        :return: The sso_group_id of this UserGroup.  # noqa: E501
        :rtype: str
        """
        return self._sso_group_id

    @sso_group_id.setter
    def sso_group_id(self, sso_group_id):
        """Sets the sso_group_id of this UserGroup.

        Identifier of the userGroup in SSO.  # noqa: E501

        :param sso_group_id: The sso_group_id of this UserGroup.  # noqa: E501
        :type: str
        """

        self._sso_group_id = sso_group_id

    @property
    def sso_group_name(self):
        """Gets the sso_group_name of this UserGroup.  # noqa: E501

        Name of the SSO userGroup.  # noqa: E501

        :return: The sso_group_name of this UserGroup.  # noqa: E501
        :rtype: str
        """
        return self._sso_group_name

    @sso_group_name.setter
    def sso_group_name(self, sso_group_name):
        """Sets the sso_group_name of this UserGroup.

        Name of the SSO userGroup.  # noqa: E501

        :param sso_group_name: The sso_group_name of this UserGroup.  # noqa: E501
        :type: str
        """

        self._sso_group_name = sso_group_name

    @property
    def linked_sso_type(self):
        """Gets the linked_sso_type of this UserGroup.  # noqa: E501

        Type of linked SSO  # noqa: E501

        :return: The linked_sso_type of this UserGroup.  # noqa: E501
        :rtype: str
        """
        return self._linked_sso_type

    @linked_sso_type.setter
    def linked_sso_type(self, linked_sso_type):
        """Sets the linked_sso_type of this UserGroup.

        Type of linked SSO  # noqa: E501

        :param linked_sso_type: The linked_sso_type of this UserGroup.  # noqa: E501
        :type: str
        """

        self._linked_sso_type = linked_sso_type

    @property
    def externally_managed(self):
        """Gets the externally_managed of this UserGroup.  # noqa: E501

        Specifies whether or not the userGroup is externally managed.  # noqa: E501

        :return: The externally_managed of this UserGroup.  # noqa: E501
        :rtype: bool
        """
        return self._externally_managed

    @externally_managed.setter
    def externally_managed(self, externally_managed):
        """Sets the externally_managed of this UserGroup.

        Specifies whether or not the userGroup is externally managed.  # noqa: E501

        :param externally_managed: The externally_managed of this UserGroup.  # noqa: E501
        :type: bool
        """

        self._externally_managed = externally_managed

    @property
    def description(self):
        """Gets the description of this UserGroup.  # noqa: E501

        Description of the entity  # noqa: E501

        :return: The description of this UserGroup.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UserGroup.

        Description of the entity  # noqa: E501

        :param description: The description of this UserGroup.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def tags(self):
        """Gets the tags of this UserGroup.  # noqa: E501

        Tags  # noqa: E501

        :return: The tags of this UserGroup.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this UserGroup.

        Tags  # noqa: E501

        :param tags: The tags of this UserGroup.  # noqa: E501
        :type: dict(str, str)
        """

        self._tags = tags

    @property
    def harness_managed(self):
        """Gets the harness_managed of this UserGroup.  # noqa: E501

        Specifies whether or not the userGroup is managed by harness.  # noqa: E501

        :return: The harness_managed of this UserGroup.  # noqa: E501
        :rtype: bool
        """
        return self._harness_managed

    @harness_managed.setter
    def harness_managed(self, harness_managed):
        """Sets the harness_managed of this UserGroup.

        Specifies whether or not the userGroup is managed by harness.  # noqa: E501

        :param harness_managed: The harness_managed of this UserGroup.  # noqa: E501
        :type: bool
        """

        self._harness_managed = harness_managed

    @property
    def sso_linked(self):
        """Gets the sso_linked of this UserGroup.  # noqa: E501


        :return: The sso_linked of this UserGroup.  # noqa: E501
        :rtype: bool
        """
        return self._sso_linked

    @sso_linked.setter
    def sso_linked(self, sso_linked):
        """Sets the sso_linked of this UserGroup.


        :param sso_linked: The sso_linked of this UserGroup.  # noqa: E501
        :type: bool
        """

        self._sso_linked = sso_linked

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
        if issubclass(UserGroup, dict):
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
        if not isinstance(other, UserGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
