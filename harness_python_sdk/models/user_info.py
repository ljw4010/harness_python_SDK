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

class UserInfo(object):
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
        'email': 'str',
        'token': 'str',
        'default_account_id': 'str',
        'intent': 'str',
        'accounts': 'list[GatewayAccountRequest]',
        'admin': 'bool',
        'two_factor_authentication_enabled': 'bool',
        'email_verified': 'bool',
        'locked': 'bool',
        'disabled': 'bool',
        'signup_action': 'str',
        'edition': 'str',
        'billing_frequency': 'str',
        'utm_info': 'UtmInfo',
        'externally_managed': 'bool',
        'given_name': 'str',
        'family_name': 'str',
        'external_id': 'str',
        'created_at': 'int',
        'last_updated_at': 'int'
    }

    attribute_map = {
        'uuid': 'uuid',
        'name': 'name',
        'email': 'email',
        'token': 'token',
        'default_account_id': 'defaultAccountId',
        'intent': 'intent',
        'accounts': 'accounts',
        'admin': 'admin',
        'two_factor_authentication_enabled': 'twoFactorAuthenticationEnabled',
        'email_verified': 'emailVerified',
        'locked': 'locked',
        'disabled': 'disabled',
        'signup_action': 'signupAction',
        'edition': 'edition',
        'billing_frequency': 'billingFrequency',
        'utm_info': 'utmInfo',
        'externally_managed': 'externallyManaged',
        'given_name': 'givenName',
        'family_name': 'familyName',
        'external_id': 'externalId',
        'created_at': 'createdAt',
        'last_updated_at': 'lastUpdatedAt'
    }

    def __init__(self, uuid=None, name=None, email=None, token=None, default_account_id=None, intent=None, accounts=None, admin=None, two_factor_authentication_enabled=None, email_verified=None, locked=None, disabled=None, signup_action=None, edition=None, billing_frequency=None, utm_info=None, externally_managed=None, given_name=None, family_name=None, external_id=None, created_at=None, last_updated_at=None):  # noqa: E501
        """UserInfo - a model defined in Swagger"""  # noqa: E501
        self._uuid = None
        self._name = None
        self._email = None
        self._token = None
        self._default_account_id = None
        self._intent = None
        self._accounts = None
        self._admin = None
        self._two_factor_authentication_enabled = None
        self._email_verified = None
        self._locked = None
        self._disabled = None
        self._signup_action = None
        self._edition = None
        self._billing_frequency = None
        self._utm_info = None
        self._externally_managed = None
        self._given_name = None
        self._family_name = None
        self._external_id = None
        self._created_at = None
        self._last_updated_at = None
        self.discriminator = None
        if uuid is not None:
            self.uuid = uuid
        if name is not None:
            self.name = name
        if email is not None:
            self.email = email
        if token is not None:
            self.token = token
        if default_account_id is not None:
            self.default_account_id = default_account_id
        if intent is not None:
            self.intent = intent
        if accounts is not None:
            self.accounts = accounts
        if admin is not None:
            self.admin = admin
        if two_factor_authentication_enabled is not None:
            self.two_factor_authentication_enabled = two_factor_authentication_enabled
        if email_verified is not None:
            self.email_verified = email_verified
        if locked is not None:
            self.locked = locked
        if disabled is not None:
            self.disabled = disabled
        if signup_action is not None:
            self.signup_action = signup_action
        if edition is not None:
            self.edition = edition
        if billing_frequency is not None:
            self.billing_frequency = billing_frequency
        if utm_info is not None:
            self.utm_info = utm_info
        if externally_managed is not None:
            self.externally_managed = externally_managed
        if given_name is not None:
            self.given_name = given_name
        if family_name is not None:
            self.family_name = family_name
        if external_id is not None:
            self.external_id = external_id
        if created_at is not None:
            self.created_at = created_at
        if last_updated_at is not None:
            self.last_updated_at = last_updated_at

    @property
    def uuid(self):
        """Gets the uuid of this UserInfo.  # noqa: E501


        :return: The uuid of this UserInfo.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this UserInfo.


        :param uuid: The uuid of this UserInfo.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def name(self):
        """Gets the name of this UserInfo.  # noqa: E501


        :return: The name of this UserInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UserInfo.


        :param name: The name of this UserInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def email(self):
        """Gets the email of this UserInfo.  # noqa: E501


        :return: The email of this UserInfo.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserInfo.


        :param email: The email of this UserInfo.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def token(self):
        """Gets the token of this UserInfo.  # noqa: E501


        :return: The token of this UserInfo.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this UserInfo.


        :param token: The token of this UserInfo.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def default_account_id(self):
        """Gets the default_account_id of this UserInfo.  # noqa: E501


        :return: The default_account_id of this UserInfo.  # noqa: E501
        :rtype: str
        """
        return self._default_account_id

    @default_account_id.setter
    def default_account_id(self, default_account_id):
        """Sets the default_account_id of this UserInfo.


        :param default_account_id: The default_account_id of this UserInfo.  # noqa: E501
        :type: str
        """

        self._default_account_id = default_account_id

    @property
    def intent(self):
        """Gets the intent of this UserInfo.  # noqa: E501


        :return: The intent of this UserInfo.  # noqa: E501
        :rtype: str
        """
        return self._intent

    @intent.setter
    def intent(self, intent):
        """Sets the intent of this UserInfo.


        :param intent: The intent of this UserInfo.  # noqa: E501
        :type: str
        """

        self._intent = intent

    @property
    def accounts(self):
        """Gets the accounts of this UserInfo.  # noqa: E501


        :return: The accounts of this UserInfo.  # noqa: E501
        :rtype: list[GatewayAccountRequest]
        """
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        """Sets the accounts of this UserInfo.


        :param accounts: The accounts of this UserInfo.  # noqa: E501
        :type: list[GatewayAccountRequest]
        """

        self._accounts = accounts

    @property
    def admin(self):
        """Gets the admin of this UserInfo.  # noqa: E501


        :return: The admin of this UserInfo.  # noqa: E501
        :rtype: bool
        """
        return self._admin

    @admin.setter
    def admin(self, admin):
        """Sets the admin of this UserInfo.


        :param admin: The admin of this UserInfo.  # noqa: E501
        :type: bool
        """

        self._admin = admin

    @property
    def two_factor_authentication_enabled(self):
        """Gets the two_factor_authentication_enabled of this UserInfo.  # noqa: E501


        :return: The two_factor_authentication_enabled of this UserInfo.  # noqa: E501
        :rtype: bool
        """
        return self._two_factor_authentication_enabled

    @two_factor_authentication_enabled.setter
    def two_factor_authentication_enabled(self, two_factor_authentication_enabled):
        """Sets the two_factor_authentication_enabled of this UserInfo.


        :param two_factor_authentication_enabled: The two_factor_authentication_enabled of this UserInfo.  # noqa: E501
        :type: bool
        """

        self._two_factor_authentication_enabled = two_factor_authentication_enabled

    @property
    def email_verified(self):
        """Gets the email_verified of this UserInfo.  # noqa: E501


        :return: The email_verified of this UserInfo.  # noqa: E501
        :rtype: bool
        """
        return self._email_verified

    @email_verified.setter
    def email_verified(self, email_verified):
        """Sets the email_verified of this UserInfo.


        :param email_verified: The email_verified of this UserInfo.  # noqa: E501
        :type: bool
        """

        self._email_verified = email_verified

    @property
    def locked(self):
        """Gets the locked of this UserInfo.  # noqa: E501


        :return: The locked of this UserInfo.  # noqa: E501
        :rtype: bool
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """Sets the locked of this UserInfo.


        :param locked: The locked of this UserInfo.  # noqa: E501
        :type: bool
        """

        self._locked = locked

    @property
    def disabled(self):
        """Gets the disabled of this UserInfo.  # noqa: E501


        :return: The disabled of this UserInfo.  # noqa: E501
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this UserInfo.


        :param disabled: The disabled of this UserInfo.  # noqa: E501
        :type: bool
        """

        self._disabled = disabled

    @property
    def signup_action(self):
        """Gets the signup_action of this UserInfo.  # noqa: E501


        :return: The signup_action of this UserInfo.  # noqa: E501
        :rtype: str
        """
        return self._signup_action

    @signup_action.setter
    def signup_action(self, signup_action):
        """Sets the signup_action of this UserInfo.


        :param signup_action: The signup_action of this UserInfo.  # noqa: E501
        :type: str
        """

        self._signup_action = signup_action

    @property
    def edition(self):
        """Gets the edition of this UserInfo.  # noqa: E501


        :return: The edition of this UserInfo.  # noqa: E501
        :rtype: str
        """
        return self._edition

    @edition.setter
    def edition(self, edition):
        """Sets the edition of this UserInfo.


        :param edition: The edition of this UserInfo.  # noqa: E501
        :type: str
        """

        self._edition = edition

    @property
    def billing_frequency(self):
        """Gets the billing_frequency of this UserInfo.  # noqa: E501


        :return: The billing_frequency of this UserInfo.  # noqa: E501
        :rtype: str
        """
        return self._billing_frequency

    @billing_frequency.setter
    def billing_frequency(self, billing_frequency):
        """Sets the billing_frequency of this UserInfo.


        :param billing_frequency: The billing_frequency of this UserInfo.  # noqa: E501
        :type: str
        """

        self._billing_frequency = billing_frequency

    @property
    def utm_info(self):
        """Gets the utm_info of this UserInfo.  # noqa: E501


        :return: The utm_info of this UserInfo.  # noqa: E501
        :rtype: UtmInfo
        """
        return self._utm_info

    @utm_info.setter
    def utm_info(self, utm_info):
        """Sets the utm_info of this UserInfo.


        :param utm_info: The utm_info of this UserInfo.  # noqa: E501
        :type: UtmInfo
        """

        self._utm_info = utm_info

    @property
    def externally_managed(self):
        """Gets the externally_managed of this UserInfo.  # noqa: E501


        :return: The externally_managed of this UserInfo.  # noqa: E501
        :rtype: bool
        """
        return self._externally_managed

    @externally_managed.setter
    def externally_managed(self, externally_managed):
        """Sets the externally_managed of this UserInfo.


        :param externally_managed: The externally_managed of this UserInfo.  # noqa: E501
        :type: bool
        """

        self._externally_managed = externally_managed

    @property
    def given_name(self):
        """Gets the given_name of this UserInfo.  # noqa: E501


        :return: The given_name of this UserInfo.  # noqa: E501
        :rtype: str
        """
        return self._given_name

    @given_name.setter
    def given_name(self, given_name):
        """Sets the given_name of this UserInfo.


        :param given_name: The given_name of this UserInfo.  # noqa: E501
        :type: str
        """

        self._given_name = given_name

    @property
    def family_name(self):
        """Gets the family_name of this UserInfo.  # noqa: E501


        :return: The family_name of this UserInfo.  # noqa: E501
        :rtype: str
        """
        return self._family_name

    @family_name.setter
    def family_name(self, family_name):
        """Sets the family_name of this UserInfo.


        :param family_name: The family_name of this UserInfo.  # noqa: E501
        :type: str
        """

        self._family_name = family_name

    @property
    def external_id(self):
        """Gets the external_id of this UserInfo.  # noqa: E501


        :return: The external_id of this UserInfo.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this UserInfo.


        :param external_id: The external_id of this UserInfo.  # noqa: E501
        :type: str
        """

        self._external_id = external_id

    @property
    def created_at(self):
        """Gets the created_at of this UserInfo.  # noqa: E501


        :return: The created_at of this UserInfo.  # noqa: E501
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this UserInfo.


        :param created_at: The created_at of this UserInfo.  # noqa: E501
        :type: int
        """

        self._created_at = created_at

    @property
    def last_updated_at(self):
        """Gets the last_updated_at of this UserInfo.  # noqa: E501


        :return: The last_updated_at of this UserInfo.  # noqa: E501
        :rtype: int
        """
        return self._last_updated_at

    @last_updated_at.setter
    def last_updated_at(self, last_updated_at):
        """Sets the last_updated_at of this UserInfo.


        :param last_updated_at: The last_updated_at of this UserInfo.  # noqa: E501
        :type: int
        """

        self._last_updated_at = last_updated_at

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
        if issubclass(UserInfo, dict):
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
        if not isinstance(other, UserInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
