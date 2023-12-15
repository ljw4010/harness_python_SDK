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

class GovernanceMetadata1(object):
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
        'deny': 'bool',
        'policy_set_metadata': 'list[PolicySetMetadata]',
        'message': 'str',
        'time_stamp': 'int',
        'status': 'str',
        'account_identifier': 'str',
        'org_identifier': 'str',
        'project_identifier': 'str',
        'entity': 'str',
        'type': 'str',
        'action': 'str',
        'created': 'int'
    }

    attribute_map = {
        'identifier': 'identifier',
        'deny': 'deny',
        'policy_set_metadata': 'policy_set_metadata',
        'message': 'message',
        'time_stamp': 'time_stamp',
        'status': 'status',
        'account_identifier': 'account_identifier',
        'org_identifier': 'org_identifier',
        'project_identifier': 'project_identifier',
        'entity': 'entity',
        'type': 'type',
        'action': 'action',
        'created': 'created'
    }

    def __init__(self, identifier=None, deny=None, policy_set_metadata=None, message=None, time_stamp=None, status=None, account_identifier=None, org_identifier=None, project_identifier=None, entity=None, type=None, action=None, created=None):  # noqa: E501
        """GovernanceMetadata1 - a model defined in Swagger"""  # noqa: E501
        self._identifier = None
        self._deny = None
        self._policy_set_metadata = None
        self._message = None
        self._time_stamp = None
        self._status = None
        self._account_identifier = None
        self._org_identifier = None
        self._project_identifier = None
        self._entity = None
        self._type = None
        self._action = None
        self._created = None
        self.discriminator = None
        if identifier is not None:
            self.identifier = identifier
        if deny is not None:
            self.deny = deny
        if policy_set_metadata is not None:
            self.policy_set_metadata = policy_set_metadata
        if message is not None:
            self.message = message
        if time_stamp is not None:
            self.time_stamp = time_stamp
        if status is not None:
            self.status = status
        if account_identifier is not None:
            self.account_identifier = account_identifier
        if org_identifier is not None:
            self.org_identifier = org_identifier
        if project_identifier is not None:
            self.project_identifier = project_identifier
        if entity is not None:
            self.entity = entity
        if type is not None:
            self.type = type
        if action is not None:
            self.action = action
        if created is not None:
            self.created = created

    @property
    def identifier(self):
        """Gets the identifier of this GovernanceMetadata1.  # noqa: E501


        :return: The identifier of this GovernanceMetadata1.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this GovernanceMetadata1.


        :param identifier: The identifier of this GovernanceMetadata1.  # noqa: E501
        :type: str
        """

        self._identifier = identifier

    @property
    def deny(self):
        """Gets the deny of this GovernanceMetadata1.  # noqa: E501


        :return: The deny of this GovernanceMetadata1.  # noqa: E501
        :rtype: bool
        """
        return self._deny

    @deny.setter
    def deny(self, deny):
        """Sets the deny of this GovernanceMetadata1.


        :param deny: The deny of this GovernanceMetadata1.  # noqa: E501
        :type: bool
        """

        self._deny = deny

    @property
    def policy_set_metadata(self):
        """Gets the policy_set_metadata of this GovernanceMetadata1.  # noqa: E501


        :return: The policy_set_metadata of this GovernanceMetadata1.  # noqa: E501
        :rtype: list[PolicySetMetadata]
        """
        return self._policy_set_metadata

    @policy_set_metadata.setter
    def policy_set_metadata(self, policy_set_metadata):
        """Sets the policy_set_metadata of this GovernanceMetadata1.


        :param policy_set_metadata: The policy_set_metadata of this GovernanceMetadata1.  # noqa: E501
        :type: list[PolicySetMetadata]
        """

        self._policy_set_metadata = policy_set_metadata

    @property
    def message(self):
        """Gets the message of this GovernanceMetadata1.  # noqa: E501


        :return: The message of this GovernanceMetadata1.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this GovernanceMetadata1.


        :param message: The message of this GovernanceMetadata1.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def time_stamp(self):
        """Gets the time_stamp of this GovernanceMetadata1.  # noqa: E501


        :return: The time_stamp of this GovernanceMetadata1.  # noqa: E501
        :rtype: int
        """
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, time_stamp):
        """Sets the time_stamp of this GovernanceMetadata1.


        :param time_stamp: The time_stamp of this GovernanceMetadata1.  # noqa: E501
        :type: int
        """

        self._time_stamp = time_stamp

    @property
    def status(self):
        """Gets the status of this GovernanceMetadata1.  # noqa: E501


        :return: The status of this GovernanceMetadata1.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GovernanceMetadata1.


        :param status: The status of this GovernanceMetadata1.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def account_identifier(self):
        """Gets the account_identifier of this GovernanceMetadata1.  # noqa: E501


        :return: The account_identifier of this GovernanceMetadata1.  # noqa: E501
        :rtype: str
        """
        return self._account_identifier

    @account_identifier.setter
    def account_identifier(self, account_identifier):
        """Sets the account_identifier of this GovernanceMetadata1.


        :param account_identifier: The account_identifier of this GovernanceMetadata1.  # noqa: E501
        :type: str
        """

        self._account_identifier = account_identifier

    @property
    def org_identifier(self):
        """Gets the org_identifier of this GovernanceMetadata1.  # noqa: E501


        :return: The org_identifier of this GovernanceMetadata1.  # noqa: E501
        :rtype: str
        """
        return self._org_identifier

    @org_identifier.setter
    def org_identifier(self, org_identifier):
        """Sets the org_identifier of this GovernanceMetadata1.


        :param org_identifier: The org_identifier of this GovernanceMetadata1.  # noqa: E501
        :type: str
        """

        self._org_identifier = org_identifier

    @property
    def project_identifier(self):
        """Gets the project_identifier of this GovernanceMetadata1.  # noqa: E501


        :return: The project_identifier of this GovernanceMetadata1.  # noqa: E501
        :rtype: str
        """
        return self._project_identifier

    @project_identifier.setter
    def project_identifier(self, project_identifier):
        """Sets the project_identifier of this GovernanceMetadata1.


        :param project_identifier: The project_identifier of this GovernanceMetadata1.  # noqa: E501
        :type: str
        """

        self._project_identifier = project_identifier

    @property
    def entity(self):
        """Gets the entity of this GovernanceMetadata1.  # noqa: E501


        :return: The entity of this GovernanceMetadata1.  # noqa: E501
        :rtype: str
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        """Sets the entity of this GovernanceMetadata1.


        :param entity: The entity of this GovernanceMetadata1.  # noqa: E501
        :type: str
        """

        self._entity = entity

    @property
    def type(self):
        """Gets the type of this GovernanceMetadata1.  # noqa: E501


        :return: The type of this GovernanceMetadata1.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GovernanceMetadata1.


        :param type: The type of this GovernanceMetadata1.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def action(self):
        """Gets the action of this GovernanceMetadata1.  # noqa: E501


        :return: The action of this GovernanceMetadata1.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this GovernanceMetadata1.


        :param action: The action of this GovernanceMetadata1.  # noqa: E501
        :type: str
        """

        self._action = action

    @property
    def created(self):
        """Gets the created of this GovernanceMetadata1.  # noqa: E501


        :return: The created of this GovernanceMetadata1.  # noqa: E501
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this GovernanceMetadata1.


        :param created: The created of this GovernanceMetadata1.  # noqa: E501
        :type: int
        """

        self._created = created

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
        if issubclass(GovernanceMetadata1, dict):
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
        if not isinstance(other, GovernanceMetadata1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
