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

class TemplatePolicyMetadata(object):
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
        'unknown_fields': 'UnknownFieldSet',
        'severity': 'str',
        'error': 'str',
        'updated': 'int',
        'created': 'int',
        'status': 'str',
        'policy_id': 'str',
        'account_id': 'str',
        'initialized': 'bool',
        'identifier': 'str',
        'policy_name': 'str',
        'serialized_size': 'int',
        'parser_for_type': 'ParserPolicyMetadata',
        'default_instance_for_type': 'TemplatePolicyMetadata',
        'identifier_bytes': 'ByteString',
        'policy_id_bytes': 'ByteString',
        'policy_name_bytes': 'ByteString',
        'severity_bytes': 'ByteString',
        'deny_messages_list': 'list[str]',
        'deny_messages_count': 'int',
        'status_bytes': 'ByteString',
        'account_id_bytes': 'ByteString',
        'org_id': 'str',
        'org_id_bytes': 'ByteString',
        'project_id': 'str',
        'project_id_bytes': 'ByteString',
        'error_bytes': 'ByteString',
        'all_fields': 'dict(str, object)',
        'descriptor_for_type': 'Descriptor',
        'initialization_error_string': 'str',
        'memoized_serialized_size': 'int'
    }

    attribute_map = {
        'unknown_fields': 'unknownFields',
        'severity': 'severity',
        'error': 'error',
        'updated': 'updated',
        'created': 'created',
        'status': 'status',
        'policy_id': 'policyId',
        'account_id': 'accountId',
        'initialized': 'initialized',
        'identifier': 'identifier',
        'policy_name': 'policyName',
        'serialized_size': 'serializedSize',
        'parser_for_type': 'parserForType',
        'default_instance_for_type': 'defaultInstanceForType',
        'identifier_bytes': 'identifierBytes',
        'policy_id_bytes': 'policyIdBytes',
        'policy_name_bytes': 'policyNameBytes',
        'severity_bytes': 'severityBytes',
        'deny_messages_list': 'denyMessagesList',
        'deny_messages_count': 'denyMessagesCount',
        'status_bytes': 'statusBytes',
        'account_id_bytes': 'accountIdBytes',
        'org_id': 'orgId',
        'org_id_bytes': 'orgIdBytes',
        'project_id': 'projectId',
        'project_id_bytes': 'projectIdBytes',
        'error_bytes': 'errorBytes',
        'all_fields': 'allFields',
        'descriptor_for_type': 'descriptorForType',
        'initialization_error_string': 'initializationErrorString',
        'memoized_serialized_size': 'memoizedSerializedSize'
    }

    def __init__(self, unknown_fields=None, severity=None, error=None, updated=None, created=None, status=None, policy_id=None, account_id=None, initialized=None, identifier=None, policy_name=None, serialized_size=None, parser_for_type=None, default_instance_for_type=None, identifier_bytes=None, policy_id_bytes=None, policy_name_bytes=None, severity_bytes=None, deny_messages_list=None, deny_messages_count=None, status_bytes=None, account_id_bytes=None, org_id=None, org_id_bytes=None, project_id=None, project_id_bytes=None, error_bytes=None, all_fields=None, descriptor_for_type=None, initialization_error_string=None, memoized_serialized_size=None):  # noqa: E501
        """TemplatePolicyMetadata - a model defined in Swagger"""  # noqa: E501
        self._unknown_fields = None
        self._severity = None
        self._error = None
        self._updated = None
        self._created = None
        self._status = None
        self._policy_id = None
        self._account_id = None
        self._initialized = None
        self._identifier = None
        self._policy_name = None
        self._serialized_size = None
        self._parser_for_type = None
        self._default_instance_for_type = None
        self._identifier_bytes = None
        self._policy_id_bytes = None
        self._policy_name_bytes = None
        self._severity_bytes = None
        self._deny_messages_list = None
        self._deny_messages_count = None
        self._status_bytes = None
        self._account_id_bytes = None
        self._org_id = None
        self._org_id_bytes = None
        self._project_id = None
        self._project_id_bytes = None
        self._error_bytes = None
        self._all_fields = None
        self._descriptor_for_type = None
        self._initialization_error_string = None
        self._memoized_serialized_size = None
        self.discriminator = None
        if unknown_fields is not None:
            self.unknown_fields = unknown_fields
        if severity is not None:
            self.severity = severity
        if error is not None:
            self.error = error
        if updated is not None:
            self.updated = updated
        if created is not None:
            self.created = created
        if status is not None:
            self.status = status
        if policy_id is not None:
            self.policy_id = policy_id
        if account_id is not None:
            self.account_id = account_id
        if initialized is not None:
            self.initialized = initialized
        if identifier is not None:
            self.identifier = identifier
        if policy_name is not None:
            self.policy_name = policy_name
        if serialized_size is not None:
            self.serialized_size = serialized_size
        if parser_for_type is not None:
            self.parser_for_type = parser_for_type
        if default_instance_for_type is not None:
            self.default_instance_for_type = default_instance_for_type
        if identifier_bytes is not None:
            self.identifier_bytes = identifier_bytes
        if policy_id_bytes is not None:
            self.policy_id_bytes = policy_id_bytes
        if policy_name_bytes is not None:
            self.policy_name_bytes = policy_name_bytes
        if severity_bytes is not None:
            self.severity_bytes = severity_bytes
        if deny_messages_list is not None:
            self.deny_messages_list = deny_messages_list
        if deny_messages_count is not None:
            self.deny_messages_count = deny_messages_count
        if status_bytes is not None:
            self.status_bytes = status_bytes
        if account_id_bytes is not None:
            self.account_id_bytes = account_id_bytes
        if org_id is not None:
            self.org_id = org_id
        if org_id_bytes is not None:
            self.org_id_bytes = org_id_bytes
        if project_id is not None:
            self.project_id = project_id
        if project_id_bytes is not None:
            self.project_id_bytes = project_id_bytes
        if error_bytes is not None:
            self.error_bytes = error_bytes
        if all_fields is not None:
            self.all_fields = all_fields
        if descriptor_for_type is not None:
            self.descriptor_for_type = descriptor_for_type
        if initialization_error_string is not None:
            self.initialization_error_string = initialization_error_string
        if memoized_serialized_size is not None:
            self.memoized_serialized_size = memoized_serialized_size

    @property
    def unknown_fields(self):
        """Gets the unknown_fields of this TemplatePolicyMetadata.  # noqa: E501


        :return: The unknown_fields of this TemplatePolicyMetadata.  # noqa: E501
        :rtype: UnknownFieldSet
        """
        return self._unknown_fields

    @unknown_fields.setter
    def unknown_fields(self, unknown_fields):
        """Sets the unknown_fields of this TemplatePolicyMetadata.


        :param unknown_fields: The unknown_fields of this TemplatePolicyMetadata.  # noqa: E501
        :type: UnknownFieldSet
        """

        self._unknown_fields = unknown_fields

    @property
    def severity(self):
        """Gets the severity of this TemplatePolicyMetadata.  # noqa: E501


        :return: The severity of this TemplatePolicyMetadata.  # noqa: E501
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this TemplatePolicyMetadata.


        :param severity: The severity of this TemplatePolicyMetadata.  # noqa: E501
        :type: str
        """

        self._severity = severity

    @property
    def error(self):
        """Gets the error of this TemplatePolicyMetadata.  # noqa: E501


        :return: The error of this TemplatePolicyMetadata.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this TemplatePolicyMetadata.


        :param error: The error of this TemplatePolicyMetadata.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def updated(self):
        """Gets the updated of this TemplatePolicyMetadata.  # noqa: E501


        :return: The updated of this TemplatePolicyMetadata.  # noqa: E501
        :rtype: int
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this TemplatePolicyMetadata.


        :param updated: The updated of this TemplatePolicyMetadata.  # noqa: E501
        :type: int
        """

        self._updated = updated

    @property
    def created(self):
        """Gets the created of this TemplatePolicyMetadata.  # noqa: E501


        :return: The created of this TemplatePolicyMetadata.  # noqa: E501
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this TemplatePolicyMetadata.


        :param created: The created of this TemplatePolicyMetadata.  # noqa: E501
        :type: int
        """

        self._created = created

    @property
    def status(self):
        """Gets the status of this TemplatePolicyMetadata.  # noqa: E501


        :return: The status of this TemplatePolicyMetadata.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TemplatePolicyMetadata.


        :param status: The status of this TemplatePolicyMetadata.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def policy_id(self):
        """Gets the policy_id of this TemplatePolicyMetadata.  # noqa: E501


        :return: The policy_id of this TemplatePolicyMetadata.  # noqa: E501
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        """Sets the policy_id of this TemplatePolicyMetadata.


        :param policy_id: The policy_id of this TemplatePolicyMetadata.  # noqa: E501
        :type: str
        """

        self._policy_id = policy_id

    @property
    def account_id(self):
        """Gets the account_id of this TemplatePolicyMetadata.  # noqa: E501


        :return: The account_id of this TemplatePolicyMetadata.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this TemplatePolicyMetadata.


        :param account_id: The account_id of this TemplatePolicyMetadata.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def initialized(self):
        """Gets the initialized of this TemplatePolicyMetadata.  # noqa: E501


        :return: The initialized of this TemplatePolicyMetadata.  # noqa: E501
        :rtype: bool
        """
        return self._initialized

    @initialized.setter
    def initialized(self, initialized):
        """Sets the initialized of this TemplatePolicyMetadata.


        :param initialized: The initialized of this TemplatePolicyMetadata.  # noqa: E501
        :type: bool
        """

        self._initialized = initialized

    @property
    def identifier(self):
        """Gets the identifier of this TemplatePolicyMetadata.  # noqa: E501


        :return: The identifier of this TemplatePolicyMetadata.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this TemplatePolicyMetadata.


        :param identifier: The identifier of this TemplatePolicyMetadata.  # noqa: E501
        :type: str
        """

        self._identifier = identifier

    @property
    def policy_name(self):
        """Gets the policy_name of this TemplatePolicyMetadata.  # noqa: E501


        :return: The policy_name of this TemplatePolicyMetadata.  # noqa: E501
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        """Sets the policy_name of this TemplatePolicyMetadata.


        :param policy_name: The policy_name of this TemplatePolicyMetadata.  # noqa: E501
        :type: str
        """

        self._policy_name = policy_name

    @property
    def serialized_size(self):
        """Gets the serialized_size of this TemplatePolicyMetadata.  # noqa: E501


        :return: The serialized_size of this TemplatePolicyMetadata.  # noqa: E501
        :rtype: int
        """
        return self._serialized_size

    @serialized_size.setter
    def serialized_size(self, serialized_size):
        """Sets the serialized_size of this TemplatePolicyMetadata.


        :param serialized_size: The serialized_size of this TemplatePolicyMetadata.  # noqa: E501
        :type: int
        """

        self._serialized_size = serialized_size

    @property
    def parser_for_type(self):
        """Gets the parser_for_type of this TemplatePolicyMetadata.  # noqa: E501


        :return: The parser_for_type of this TemplatePolicyMetadata.  # noqa: E501
        :rtype: ParserPolicyMetadata
        """
        return self._parser_for_type

    @parser_for_type.setter
    def parser_for_type(self, parser_for_type):
        """Sets the parser_for_type of this TemplatePolicyMetadata.


        :param parser_for_type: The parser_for_type of this TemplatePolicyMetadata.  # noqa: E501
        :type: ParserPolicyMetadata
        """

        self._parser_for_type = parser_for_type

    @property
    def default_instance_for_type(self):
        """Gets the default_instance_for_type of this TemplatePolicyMetadata.  # noqa: E501


        :return: The default_instance_for_type of this TemplatePolicyMetadata.  # noqa: E501
        :rtype: TemplatePolicyMetadata
        """
        return self._default_instance_for_type

    @default_instance_for_type.setter
    def default_instance_for_type(self, default_instance_for_type):
        """Sets the default_instance_for_type of this TemplatePolicyMetadata.


        :param default_instance_for_type: The default_instance_for_type of this TemplatePolicyMetadata.  # noqa: E501
        :type: TemplatePolicyMetadata
        """

        self._default_instance_for_type = default_instance_for_type

    @property
    def identifier_bytes(self):
        """Gets the identifier_bytes of this TemplatePolicyMetadata.  # noqa: E501


        :return: The identifier_bytes of this TemplatePolicyMetadata.  # noqa: E501
        :rtype: ByteString
        """
        return self._identifier_bytes

    @identifier_bytes.setter
    def identifier_bytes(self, identifier_bytes):
        """Sets the identifier_bytes of this TemplatePolicyMetadata.


        :param identifier_bytes: The identifier_bytes of this TemplatePolicyMetadata.  # noqa: E501
        :type: ByteString
        """

        self._identifier_bytes = identifier_bytes

    @property
    def policy_id_bytes(self):
        """Gets the policy_id_bytes of this TemplatePolicyMetadata.  # noqa: E501


        :return: The policy_id_bytes of this TemplatePolicyMetadata.  # noqa: E501
        :rtype: ByteString
        """
        return self._policy_id_bytes

    @policy_id_bytes.setter
    def policy_id_bytes(self, policy_id_bytes):
        """Sets the policy_id_bytes of this TemplatePolicyMetadata.


        :param policy_id_bytes: The policy_id_bytes of this TemplatePolicyMetadata.  # noqa: E501
        :type: ByteString
        """

        self._policy_id_bytes = policy_id_bytes

    @property
    def policy_name_bytes(self):
        """Gets the policy_name_bytes of this TemplatePolicyMetadata.  # noqa: E501


        :return: The policy_name_bytes of this TemplatePolicyMetadata.  # noqa: E501
        :rtype: ByteString
        """
        return self._policy_name_bytes

    @policy_name_bytes.setter
    def policy_name_bytes(self, policy_name_bytes):
        """Sets the policy_name_bytes of this TemplatePolicyMetadata.


        :param policy_name_bytes: The policy_name_bytes of this TemplatePolicyMetadata.  # noqa: E501
        :type: ByteString
        """

        self._policy_name_bytes = policy_name_bytes

    @property
    def severity_bytes(self):
        """Gets the severity_bytes of this TemplatePolicyMetadata.  # noqa: E501


        :return: The severity_bytes of this TemplatePolicyMetadata.  # noqa: E501
        :rtype: ByteString
        """
        return self._severity_bytes

    @severity_bytes.setter
    def severity_bytes(self, severity_bytes):
        """Sets the severity_bytes of this TemplatePolicyMetadata.


        :param severity_bytes: The severity_bytes of this TemplatePolicyMetadata.  # noqa: E501
        :type: ByteString
        """

        self._severity_bytes = severity_bytes

    @property
    def deny_messages_list(self):
        """Gets the deny_messages_list of this TemplatePolicyMetadata.  # noqa: E501


        :return: The deny_messages_list of this TemplatePolicyMetadata.  # noqa: E501
        :rtype: list[str]
        """
        return self._deny_messages_list

    @deny_messages_list.setter
    def deny_messages_list(self, deny_messages_list):
        """Sets the deny_messages_list of this TemplatePolicyMetadata.


        :param deny_messages_list: The deny_messages_list of this TemplatePolicyMetadata.  # noqa: E501
        :type: list[str]
        """

        self._deny_messages_list = deny_messages_list

    @property
    def deny_messages_count(self):
        """Gets the deny_messages_count of this TemplatePolicyMetadata.  # noqa: E501


        :return: The deny_messages_count of this TemplatePolicyMetadata.  # noqa: E501
        :rtype: int
        """
        return self._deny_messages_count

    @deny_messages_count.setter
    def deny_messages_count(self, deny_messages_count):
        """Sets the deny_messages_count of this TemplatePolicyMetadata.


        :param deny_messages_count: The deny_messages_count of this TemplatePolicyMetadata.  # noqa: E501
        :type: int
        """

        self._deny_messages_count = deny_messages_count

    @property
    def status_bytes(self):
        """Gets the status_bytes of this TemplatePolicyMetadata.  # noqa: E501


        :return: The status_bytes of this TemplatePolicyMetadata.  # noqa: E501
        :rtype: ByteString
        """
        return self._status_bytes

    @status_bytes.setter
    def status_bytes(self, status_bytes):
        """Sets the status_bytes of this TemplatePolicyMetadata.


        :param status_bytes: The status_bytes of this TemplatePolicyMetadata.  # noqa: E501
        :type: ByteString
        """

        self._status_bytes = status_bytes

    @property
    def account_id_bytes(self):
        """Gets the account_id_bytes of this TemplatePolicyMetadata.  # noqa: E501


        :return: The account_id_bytes of this TemplatePolicyMetadata.  # noqa: E501
        :rtype: ByteString
        """
        return self._account_id_bytes

    @account_id_bytes.setter
    def account_id_bytes(self, account_id_bytes):
        """Sets the account_id_bytes of this TemplatePolicyMetadata.


        :param account_id_bytes: The account_id_bytes of this TemplatePolicyMetadata.  # noqa: E501
        :type: ByteString
        """

        self._account_id_bytes = account_id_bytes

    @property
    def org_id(self):
        """Gets the org_id of this TemplatePolicyMetadata.  # noqa: E501


        :return: The org_id of this TemplatePolicyMetadata.  # noqa: E501
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this TemplatePolicyMetadata.


        :param org_id: The org_id of this TemplatePolicyMetadata.  # noqa: E501
        :type: str
        """

        self._org_id = org_id

    @property
    def org_id_bytes(self):
        """Gets the org_id_bytes of this TemplatePolicyMetadata.  # noqa: E501


        :return: The org_id_bytes of this TemplatePolicyMetadata.  # noqa: E501
        :rtype: ByteString
        """
        return self._org_id_bytes

    @org_id_bytes.setter
    def org_id_bytes(self, org_id_bytes):
        """Sets the org_id_bytes of this TemplatePolicyMetadata.


        :param org_id_bytes: The org_id_bytes of this TemplatePolicyMetadata.  # noqa: E501
        :type: ByteString
        """

        self._org_id_bytes = org_id_bytes

    @property
    def project_id(self):
        """Gets the project_id of this TemplatePolicyMetadata.  # noqa: E501


        :return: The project_id of this TemplatePolicyMetadata.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this TemplatePolicyMetadata.


        :param project_id: The project_id of this TemplatePolicyMetadata.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def project_id_bytes(self):
        """Gets the project_id_bytes of this TemplatePolicyMetadata.  # noqa: E501


        :return: The project_id_bytes of this TemplatePolicyMetadata.  # noqa: E501
        :rtype: ByteString
        """
        return self._project_id_bytes

    @project_id_bytes.setter
    def project_id_bytes(self, project_id_bytes):
        """Sets the project_id_bytes of this TemplatePolicyMetadata.


        :param project_id_bytes: The project_id_bytes of this TemplatePolicyMetadata.  # noqa: E501
        :type: ByteString
        """

        self._project_id_bytes = project_id_bytes

    @property
    def error_bytes(self):
        """Gets the error_bytes of this TemplatePolicyMetadata.  # noqa: E501


        :return: The error_bytes of this TemplatePolicyMetadata.  # noqa: E501
        :rtype: ByteString
        """
        return self._error_bytes

    @error_bytes.setter
    def error_bytes(self, error_bytes):
        """Sets the error_bytes of this TemplatePolicyMetadata.


        :param error_bytes: The error_bytes of this TemplatePolicyMetadata.  # noqa: E501
        :type: ByteString
        """

        self._error_bytes = error_bytes

    @property
    def all_fields(self):
        """Gets the all_fields of this TemplatePolicyMetadata.  # noqa: E501


        :return: The all_fields of this TemplatePolicyMetadata.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._all_fields

    @all_fields.setter
    def all_fields(self, all_fields):
        """Sets the all_fields of this TemplatePolicyMetadata.


        :param all_fields: The all_fields of this TemplatePolicyMetadata.  # noqa: E501
        :type: dict(str, object)
        """

        self._all_fields = all_fields

    @property
    def descriptor_for_type(self):
        """Gets the descriptor_for_type of this TemplatePolicyMetadata.  # noqa: E501


        :return: The descriptor_for_type of this TemplatePolicyMetadata.  # noqa: E501
        :rtype: Descriptor
        """
        return self._descriptor_for_type

    @descriptor_for_type.setter
    def descriptor_for_type(self, descriptor_for_type):
        """Sets the descriptor_for_type of this TemplatePolicyMetadata.


        :param descriptor_for_type: The descriptor_for_type of this TemplatePolicyMetadata.  # noqa: E501
        :type: Descriptor
        """

        self._descriptor_for_type = descriptor_for_type

    @property
    def initialization_error_string(self):
        """Gets the initialization_error_string of this TemplatePolicyMetadata.  # noqa: E501


        :return: The initialization_error_string of this TemplatePolicyMetadata.  # noqa: E501
        :rtype: str
        """
        return self._initialization_error_string

    @initialization_error_string.setter
    def initialization_error_string(self, initialization_error_string):
        """Sets the initialization_error_string of this TemplatePolicyMetadata.


        :param initialization_error_string: The initialization_error_string of this TemplatePolicyMetadata.  # noqa: E501
        :type: str
        """

        self._initialization_error_string = initialization_error_string

    @property
    def memoized_serialized_size(self):
        """Gets the memoized_serialized_size of this TemplatePolicyMetadata.  # noqa: E501


        :return: The memoized_serialized_size of this TemplatePolicyMetadata.  # noqa: E501
        :rtype: int
        """
        return self._memoized_serialized_size

    @memoized_serialized_size.setter
    def memoized_serialized_size(self, memoized_serialized_size):
        """Sets the memoized_serialized_size of this TemplatePolicyMetadata.


        :param memoized_serialized_size: The memoized_serialized_size of this TemplatePolicyMetadata.  # noqa: E501
        :type: int
        """

        self._memoized_serialized_size = memoized_serialized_size

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
        if issubclass(TemplatePolicyMetadata, dict):
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
        if not isinstance(other, TemplatePolicyMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other