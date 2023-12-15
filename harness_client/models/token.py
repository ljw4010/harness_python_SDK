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

class Token(object):
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
        'valid_from': 'int',
        'valid_to': 'int',
        'scheduled_expire_time': 'int',
        'valid': 'bool',
        'account_identifier': 'str',
        'project_identifier': 'str',
        'org_identifier': 'str',
        'api_key_identifier': 'str',
        'parent_identifier': 'str',
        'api_key_type': 'str',
        'description': 'str',
        'tags': 'dict(str, str)',
        'email': 'str',
        'username': 'str',
        'encoded_password': 'str'
    }

    attribute_map = {
        'identifier': 'identifier',
        'name': 'name',
        'valid_from': 'validFrom',
        'valid_to': 'validTo',
        'scheduled_expire_time': 'scheduledExpireTime',
        'valid': 'valid',
        'account_identifier': 'accountIdentifier',
        'project_identifier': 'projectIdentifier',
        'org_identifier': 'orgIdentifier',
        'api_key_identifier': 'apiKeyIdentifier',
        'parent_identifier': 'parentIdentifier',
        'api_key_type': 'apiKeyType',
        'description': 'description',
        'tags': 'tags',
        'email': 'email',
        'username': 'username',
        'encoded_password': 'encodedPassword'
    }

    def __init__(self, identifier=None, name=None, valid_from=None, valid_to=None, scheduled_expire_time=None, valid=None, account_identifier=None, project_identifier=None, org_identifier=None, api_key_identifier=None, parent_identifier=None, api_key_type=None, description=None, tags=None, email=None, username=None, encoded_password=None):  # noqa: E501
        """Token - a model defined in Swagger"""  # noqa: E501
        self._identifier = None
        self._name = None
        self._valid_from = None
        self._valid_to = None
        self._scheduled_expire_time = None
        self._valid = None
        self._account_identifier = None
        self._project_identifier = None
        self._org_identifier = None
        self._api_key_identifier = None
        self._parent_identifier = None
        self._api_key_type = None
        self._description = None
        self._tags = None
        self._email = None
        self._username = None
        self._encoded_password = None
        self.discriminator = None
        if identifier is not None:
            self.identifier = identifier
        self.name = name
        if valid_from is not None:
            self.valid_from = valid_from
        if valid_to is not None:
            self.valid_to = valid_to
        if scheduled_expire_time is not None:
            self.scheduled_expire_time = scheduled_expire_time
        if valid is not None:
            self.valid = valid
        if account_identifier is not None:
            self.account_identifier = account_identifier
        if project_identifier is not None:
            self.project_identifier = project_identifier
        if org_identifier is not None:
            self.org_identifier = org_identifier
        if api_key_identifier is not None:
            self.api_key_identifier = api_key_identifier
        if parent_identifier is not None:
            self.parent_identifier = parent_identifier
        if api_key_type is not None:
            self.api_key_type = api_key_type
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags
        if email is not None:
            self.email = email
        if username is not None:
            self.username = username
        if encoded_password is not None:
            self.encoded_password = encoded_password

    @property
    def identifier(self):
        """Gets the identifier of this Token.  # noqa: E501

        Identifier of the Token  # noqa: E501

        :return: The identifier of this Token.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this Token.

        Identifier of the Token  # noqa: E501

        :param identifier: The identifier of this Token.  # noqa: E501
        :type: str
        """

        self._identifier = identifier

    @property
    def name(self):
        """Gets the name of this Token.  # noqa: E501

        Name of the Token  # noqa: E501

        :return: The name of this Token.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Token.

        Name of the Token  # noqa: E501

        :param name: The name of this Token.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def valid_from(self):
        """Gets the valid_from of this Token.  # noqa: E501

        This is the time from which the Token is valid. The time is in milliseconds.  # noqa: E501

        :return: The valid_from of this Token.  # noqa: E501
        :rtype: int
        """
        return self._valid_from

    @valid_from.setter
    def valid_from(self, valid_from):
        """Sets the valid_from of this Token.

        This is the time from which the Token is valid. The time is in milliseconds.  # noqa: E501

        :param valid_from: The valid_from of this Token.  # noqa: E501
        :type: int
        """

        self._valid_from = valid_from

    @property
    def valid_to(self):
        """Gets the valid_to of this Token.  # noqa: E501

        This is the time till which the Token is valid. The time is in milliseconds.  # noqa: E501

        :return: The valid_to of this Token.  # noqa: E501
        :rtype: int
        """
        return self._valid_to

    @valid_to.setter
    def valid_to(self, valid_to):
        """Sets the valid_to of this Token.

        This is the time till which the Token is valid. The time is in milliseconds.  # noqa: E501

        :param valid_to: The valid_to of this Token.  # noqa: E501
        :type: int
        """

        self._valid_to = valid_to

    @property
    def scheduled_expire_time(self):
        """Gets the scheduled_expire_time of this Token.  # noqa: E501

        Scheduled expiry time in milliseconds.  # noqa: E501

        :return: The scheduled_expire_time of this Token.  # noqa: E501
        :rtype: int
        """
        return self._scheduled_expire_time

    @scheduled_expire_time.setter
    def scheduled_expire_time(self, scheduled_expire_time):
        """Sets the scheduled_expire_time of this Token.

        Scheduled expiry time in milliseconds.  # noqa: E501

        :param scheduled_expire_time: The scheduled_expire_time of this Token.  # noqa: E501
        :type: int
        """

        self._scheduled_expire_time = scheduled_expire_time

    @property
    def valid(self):
        """Gets the valid of this Token.  # noqa: E501

        Boolean value to indicate if Token is valid or not.  # noqa: E501

        :return: The valid of this Token.  # noqa: E501
        :rtype: bool
        """
        return self._valid

    @valid.setter
    def valid(self, valid):
        """Sets the valid of this Token.

        Boolean value to indicate if Token is valid or not.  # noqa: E501

        :param valid: The valid of this Token.  # noqa: E501
        :type: bool
        """

        self._valid = valid

    @property
    def account_identifier(self):
        """Gets the account_identifier of this Token.  # noqa: E501

        Account Identifier for the Entity.  # noqa: E501

        :return: The account_identifier of this Token.  # noqa: E501
        :rtype: str
        """
        return self._account_identifier

    @account_identifier.setter
    def account_identifier(self, account_identifier):
        """Sets the account_identifier of this Token.

        Account Identifier for the Entity.  # noqa: E501

        :param account_identifier: The account_identifier of this Token.  # noqa: E501
        :type: str
        """

        self._account_identifier = account_identifier

    @property
    def project_identifier(self):
        """Gets the project_identifier of this Token.  # noqa: E501

        Project Identifier for the Entity.  # noqa: E501

        :return: The project_identifier of this Token.  # noqa: E501
        :rtype: str
        """
        return self._project_identifier

    @project_identifier.setter
    def project_identifier(self, project_identifier):
        """Sets the project_identifier of this Token.

        Project Identifier for the Entity.  # noqa: E501

        :param project_identifier: The project_identifier of this Token.  # noqa: E501
        :type: str
        """

        self._project_identifier = project_identifier

    @property
    def org_identifier(self):
        """Gets the org_identifier of this Token.  # noqa: E501

        Organization Identifier for the Entity.  # noqa: E501

        :return: The org_identifier of this Token.  # noqa: E501
        :rtype: str
        """
        return self._org_identifier

    @org_identifier.setter
    def org_identifier(self, org_identifier):
        """Sets the org_identifier of this Token.

        Organization Identifier for the Entity.  # noqa: E501

        :param org_identifier: The org_identifier of this Token.  # noqa: E501
        :type: str
        """

        self._org_identifier = org_identifier

    @property
    def api_key_identifier(self):
        """Gets the api_key_identifier of this Token.  # noqa: E501

        This is the API Key Id within which the Token is created.  # noqa: E501

        :return: The api_key_identifier of this Token.  # noqa: E501
        :rtype: str
        """
        return self._api_key_identifier

    @api_key_identifier.setter
    def api_key_identifier(self, api_key_identifier):
        """Sets the api_key_identifier of this Token.

        This is the API Key Id within which the Token is created.  # noqa: E501

        :param api_key_identifier: The api_key_identifier of this Token.  # noqa: E501
        :type: str
        """

        self._api_key_identifier = api_key_identifier

    @property
    def parent_identifier(self):
        """Gets the parent_identifier of this Token.  # noqa: E501

        This is the ID of the Parent entity from which the Token inherits its role bindings.  # noqa: E501

        :return: The parent_identifier of this Token.  # noqa: E501
        :rtype: str
        """
        return self._parent_identifier

    @parent_identifier.setter
    def parent_identifier(self, parent_identifier):
        """Sets the parent_identifier of this Token.

        This is the ID of the Parent entity from which the Token inherits its role bindings.  # noqa: E501

        :param parent_identifier: The parent_identifier of this Token.  # noqa: E501
        :type: str
        """

        self._parent_identifier = parent_identifier

    @property
    def api_key_type(self):
        """Gets the api_key_type of this Token.  # noqa: E501

        Type of the API Key  # noqa: E501

        :return: The api_key_type of this Token.  # noqa: E501
        :rtype: str
        """
        return self._api_key_type

    @api_key_type.setter
    def api_key_type(self, api_key_type):
        """Sets the api_key_type of this Token.

        Type of the API Key  # noqa: E501

        :param api_key_type: The api_key_type of this Token.  # noqa: E501
        :type: str
        """
        allowed_values = ["USER", "SERVICE_ACCOUNT"]  # noqa: E501
        if api_key_type not in allowed_values:
            raise ValueError(
                "Invalid value for `api_key_type` ({0}), must be one of {1}"  # noqa: E501
                .format(api_key_type, allowed_values)
            )

        self._api_key_type = api_key_type

    @property
    def description(self):
        """Gets the description of this Token.  # noqa: E501

        Description of the Token  # noqa: E501

        :return: The description of this Token.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Token.

        Description of the Token  # noqa: E501

        :param description: The description of this Token.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def tags(self):
        """Gets the tags of this Token.  # noqa: E501

        Tags for the Token  # noqa: E501

        :return: The tags of this Token.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Token.

        Tags for the Token  # noqa: E501

        :param tags: The tags of this Token.  # noqa: E501
        :type: dict(str, str)
        """

        self._tags = tags

    @property
    def email(self):
        """Gets the email of this Token.  # noqa: E501

        Email Id of the user who created the Token.  # noqa: E501

        :return: The email of this Token.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Token.

        Email Id of the user who created the Token.  # noqa: E501

        :param email: The email of this Token.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def username(self):
        """Gets the username of this Token.  # noqa: E501

        Name of the user who created the Token.  # noqa: E501

        :return: The username of this Token.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this Token.

        Name of the user who created the Token.  # noqa: E501

        :param username: The username of this Token.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def encoded_password(self):
        """Gets the encoded_password of this Token.  # noqa: E501

        This is the encoded password of the Token.  # noqa: E501

        :return: The encoded_password of this Token.  # noqa: E501
        :rtype: str
        """
        return self._encoded_password

    @encoded_password.setter
    def encoded_password(self, encoded_password):
        """Sets the encoded_password of this Token.

        This is the encoded password of the Token.  # noqa: E501

        :param encoded_password: The encoded_password of this Token.  # noqa: E501
        :type: str
        """

        self._encoded_password = encoded_password

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
        if issubclass(Token, dict):
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
        if not isinstance(other, Token):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
