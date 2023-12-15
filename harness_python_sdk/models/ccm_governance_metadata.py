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

class CcmGovernanceMetadata(object):
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
        'message': 'str',
        'id': 'str',
        'type': 'str',
        'timestamp': 'int',
        'account_id': 'str',
        'project_id': 'str',
        'status': 'str',
        'entity': 'str',
        'serialized_size': 'int',
        'default_instance_for_type': 'CcmGovernanceMetadata',
        'parser_for_type': 'ParserGovernanceMetadata',
        'action': 'str',
        'created': 'int',
        'id_bytes': 'ByteString',
        'status_bytes': 'ByteString',
        'account_id_bytes': 'ByteString',
        'org_id_bytes': 'ByteString',
        'project_id_bytes': 'ByteString',
        'entity_bytes': 'ByteString',
        'type_bytes': 'ByteString',
        'action_bytes': 'ByteString',
        'deny': 'bool',
        'details_list': 'list[CcmPolicySetMetadata]',
        'org_id': 'str',
        'details_count': 'int',
        'message_bytes': 'ByteString',
        'details_or_builder_list': 'list[CcmPolicySetMetadataOrBuilder]',
        'initialized': 'bool',
        'descriptor_for_type': 'Descriptor',
        'all_fields': 'dict(str, object)',
        'initialization_error_string': 'str',
        'memoized_serialized_size': 'int'
    }

    attribute_map = {
        'unknown_fields': 'unknownFields',
        'message': 'message',
        'id': 'id',
        'type': 'type',
        'timestamp': 'timestamp',
        'account_id': 'accountId',
        'project_id': 'projectId',
        'status': 'status',
        'entity': 'entity',
        'serialized_size': 'serializedSize',
        'default_instance_for_type': 'defaultInstanceForType',
        'parser_for_type': 'parserForType',
        'action': 'action',
        'created': 'created',
        'id_bytes': 'idBytes',
        'status_bytes': 'statusBytes',
        'account_id_bytes': 'accountIdBytes',
        'org_id_bytes': 'orgIdBytes',
        'project_id_bytes': 'projectIdBytes',
        'entity_bytes': 'entityBytes',
        'type_bytes': 'typeBytes',
        'action_bytes': 'actionBytes',
        'deny': 'deny',
        'details_list': 'detailsList',
        'org_id': 'orgId',
        'details_count': 'detailsCount',
        'message_bytes': 'messageBytes',
        'details_or_builder_list': 'detailsOrBuilderList',
        'initialized': 'initialized',
        'descriptor_for_type': 'descriptorForType',
        'all_fields': 'allFields',
        'initialization_error_string': 'initializationErrorString',
        'memoized_serialized_size': 'memoizedSerializedSize'
    }

    def __init__(self, unknown_fields=None, message=None, id=None, type=None, timestamp=None, account_id=None, project_id=None, status=None, entity=None, serialized_size=None, default_instance_for_type=None, parser_for_type=None, action=None, created=None, id_bytes=None, status_bytes=None, account_id_bytes=None, org_id_bytes=None, project_id_bytes=None, entity_bytes=None, type_bytes=None, action_bytes=None, deny=None, details_list=None, org_id=None, details_count=None, message_bytes=None, details_or_builder_list=None, initialized=None, descriptor_for_type=None, all_fields=None, initialization_error_string=None, memoized_serialized_size=None):  # noqa: E501
        """CcmGovernanceMetadata - a model defined in Swagger"""  # noqa: E501
        self._unknown_fields = None
        self._message = None
        self._id = None
        self._type = None
        self._timestamp = None
        self._account_id = None
        self._project_id = None
        self._status = None
        self._entity = None
        self._serialized_size = None
        self._default_instance_for_type = None
        self._parser_for_type = None
        self._action = None
        self._created = None
        self._id_bytes = None
        self._status_bytes = None
        self._account_id_bytes = None
        self._org_id_bytes = None
        self._project_id_bytes = None
        self._entity_bytes = None
        self._type_bytes = None
        self._action_bytes = None
        self._deny = None
        self._details_list = None
        self._org_id = None
        self._details_count = None
        self._message_bytes = None
        self._details_or_builder_list = None
        self._initialized = None
        self._descriptor_for_type = None
        self._all_fields = None
        self._initialization_error_string = None
        self._memoized_serialized_size = None
        self.discriminator = None
        if unknown_fields is not None:
            self.unknown_fields = unknown_fields
        if message is not None:
            self.message = message
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if timestamp is not None:
            self.timestamp = timestamp
        if account_id is not None:
            self.account_id = account_id
        if project_id is not None:
            self.project_id = project_id
        if status is not None:
            self.status = status
        if entity is not None:
            self.entity = entity
        if serialized_size is not None:
            self.serialized_size = serialized_size
        if default_instance_for_type is not None:
            self.default_instance_for_type = default_instance_for_type
        if parser_for_type is not None:
            self.parser_for_type = parser_for_type
        if action is not None:
            self.action = action
        if created is not None:
            self.created = created
        if id_bytes is not None:
            self.id_bytes = id_bytes
        if status_bytes is not None:
            self.status_bytes = status_bytes
        if account_id_bytes is not None:
            self.account_id_bytes = account_id_bytes
        if org_id_bytes is not None:
            self.org_id_bytes = org_id_bytes
        if project_id_bytes is not None:
            self.project_id_bytes = project_id_bytes
        if entity_bytes is not None:
            self.entity_bytes = entity_bytes
        if type_bytes is not None:
            self.type_bytes = type_bytes
        if action_bytes is not None:
            self.action_bytes = action_bytes
        if deny is not None:
            self.deny = deny
        if details_list is not None:
            self.details_list = details_list
        if org_id is not None:
            self.org_id = org_id
        if details_count is not None:
            self.details_count = details_count
        if message_bytes is not None:
            self.message_bytes = message_bytes
        if details_or_builder_list is not None:
            self.details_or_builder_list = details_or_builder_list
        if initialized is not None:
            self.initialized = initialized
        if descriptor_for_type is not None:
            self.descriptor_for_type = descriptor_for_type
        if all_fields is not None:
            self.all_fields = all_fields
        if initialization_error_string is not None:
            self.initialization_error_string = initialization_error_string
        if memoized_serialized_size is not None:
            self.memoized_serialized_size = memoized_serialized_size

    @property
    def unknown_fields(self):
        """Gets the unknown_fields of this CcmGovernanceMetadata.  # noqa: E501


        :return: The unknown_fields of this CcmGovernanceMetadata.  # noqa: E501
        :rtype: UnknownFieldSet
        """
        return self._unknown_fields

    @unknown_fields.setter
    def unknown_fields(self, unknown_fields):
        """Sets the unknown_fields of this CcmGovernanceMetadata.


        :param unknown_fields: The unknown_fields of this CcmGovernanceMetadata.  # noqa: E501
        :type: UnknownFieldSet
        """

        self._unknown_fields = unknown_fields

    @property
    def message(self):
        """Gets the message of this CcmGovernanceMetadata.  # noqa: E501


        :return: The message of this CcmGovernanceMetadata.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this CcmGovernanceMetadata.


        :param message: The message of this CcmGovernanceMetadata.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def id(self):
        """Gets the id of this CcmGovernanceMetadata.  # noqa: E501


        :return: The id of this CcmGovernanceMetadata.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CcmGovernanceMetadata.


        :param id: The id of this CcmGovernanceMetadata.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this CcmGovernanceMetadata.  # noqa: E501


        :return: The type of this CcmGovernanceMetadata.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CcmGovernanceMetadata.


        :param type: The type of this CcmGovernanceMetadata.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def timestamp(self):
        """Gets the timestamp of this CcmGovernanceMetadata.  # noqa: E501


        :return: The timestamp of this CcmGovernanceMetadata.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this CcmGovernanceMetadata.


        :param timestamp: The timestamp of this CcmGovernanceMetadata.  # noqa: E501
        :type: int
        """

        self._timestamp = timestamp

    @property
    def account_id(self):
        """Gets the account_id of this CcmGovernanceMetadata.  # noqa: E501


        :return: The account_id of this CcmGovernanceMetadata.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this CcmGovernanceMetadata.


        :param account_id: The account_id of this CcmGovernanceMetadata.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def project_id(self):
        """Gets the project_id of this CcmGovernanceMetadata.  # noqa: E501


        :return: The project_id of this CcmGovernanceMetadata.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CcmGovernanceMetadata.


        :param project_id: The project_id of this CcmGovernanceMetadata.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def status(self):
        """Gets the status of this CcmGovernanceMetadata.  # noqa: E501


        :return: The status of this CcmGovernanceMetadata.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CcmGovernanceMetadata.


        :param status: The status of this CcmGovernanceMetadata.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def entity(self):
        """Gets the entity of this CcmGovernanceMetadata.  # noqa: E501


        :return: The entity of this CcmGovernanceMetadata.  # noqa: E501
        :rtype: str
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        """Sets the entity of this CcmGovernanceMetadata.


        :param entity: The entity of this CcmGovernanceMetadata.  # noqa: E501
        :type: str
        """

        self._entity = entity

    @property
    def serialized_size(self):
        """Gets the serialized_size of this CcmGovernanceMetadata.  # noqa: E501


        :return: The serialized_size of this CcmGovernanceMetadata.  # noqa: E501
        :rtype: int
        """
        return self._serialized_size

    @serialized_size.setter
    def serialized_size(self, serialized_size):
        """Sets the serialized_size of this CcmGovernanceMetadata.


        :param serialized_size: The serialized_size of this CcmGovernanceMetadata.  # noqa: E501
        :type: int
        """

        self._serialized_size = serialized_size

    @property
    def default_instance_for_type(self):
        """Gets the default_instance_for_type of this CcmGovernanceMetadata.  # noqa: E501


        :return: The default_instance_for_type of this CcmGovernanceMetadata.  # noqa: E501
        :rtype: CcmGovernanceMetadata
        """
        return self._default_instance_for_type

    @default_instance_for_type.setter
    def default_instance_for_type(self, default_instance_for_type):
        """Sets the default_instance_for_type of this CcmGovernanceMetadata.


        :param default_instance_for_type: The default_instance_for_type of this CcmGovernanceMetadata.  # noqa: E501
        :type: CcmGovernanceMetadata
        """

        self._default_instance_for_type = default_instance_for_type

    @property
    def parser_for_type(self):
        """Gets the parser_for_type of this CcmGovernanceMetadata.  # noqa: E501


        :return: The parser_for_type of this CcmGovernanceMetadata.  # noqa: E501
        :rtype: ParserGovernanceMetadata
        """
        return self._parser_for_type

    @parser_for_type.setter
    def parser_for_type(self, parser_for_type):
        """Sets the parser_for_type of this CcmGovernanceMetadata.


        :param parser_for_type: The parser_for_type of this CcmGovernanceMetadata.  # noqa: E501
        :type: ParserGovernanceMetadata
        """

        self._parser_for_type = parser_for_type

    @property
    def action(self):
        """Gets the action of this CcmGovernanceMetadata.  # noqa: E501


        :return: The action of this CcmGovernanceMetadata.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this CcmGovernanceMetadata.


        :param action: The action of this CcmGovernanceMetadata.  # noqa: E501
        :type: str
        """

        self._action = action

    @property
    def created(self):
        """Gets the created of this CcmGovernanceMetadata.  # noqa: E501


        :return: The created of this CcmGovernanceMetadata.  # noqa: E501
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this CcmGovernanceMetadata.


        :param created: The created of this CcmGovernanceMetadata.  # noqa: E501
        :type: int
        """

        self._created = created

    @property
    def id_bytes(self):
        """Gets the id_bytes of this CcmGovernanceMetadata.  # noqa: E501


        :return: The id_bytes of this CcmGovernanceMetadata.  # noqa: E501
        :rtype: ByteString
        """
        return self._id_bytes

    @id_bytes.setter
    def id_bytes(self, id_bytes):
        """Sets the id_bytes of this CcmGovernanceMetadata.


        :param id_bytes: The id_bytes of this CcmGovernanceMetadata.  # noqa: E501
        :type: ByteString
        """

        self._id_bytes = id_bytes

    @property
    def status_bytes(self):
        """Gets the status_bytes of this CcmGovernanceMetadata.  # noqa: E501


        :return: The status_bytes of this CcmGovernanceMetadata.  # noqa: E501
        :rtype: ByteString
        """
        return self._status_bytes

    @status_bytes.setter
    def status_bytes(self, status_bytes):
        """Sets the status_bytes of this CcmGovernanceMetadata.


        :param status_bytes: The status_bytes of this CcmGovernanceMetadata.  # noqa: E501
        :type: ByteString
        """

        self._status_bytes = status_bytes

    @property
    def account_id_bytes(self):
        """Gets the account_id_bytes of this CcmGovernanceMetadata.  # noqa: E501


        :return: The account_id_bytes of this CcmGovernanceMetadata.  # noqa: E501
        :rtype: ByteString
        """
        return self._account_id_bytes

    @account_id_bytes.setter
    def account_id_bytes(self, account_id_bytes):
        """Sets the account_id_bytes of this CcmGovernanceMetadata.


        :param account_id_bytes: The account_id_bytes of this CcmGovernanceMetadata.  # noqa: E501
        :type: ByteString
        """

        self._account_id_bytes = account_id_bytes

    @property
    def org_id_bytes(self):
        """Gets the org_id_bytes of this CcmGovernanceMetadata.  # noqa: E501


        :return: The org_id_bytes of this CcmGovernanceMetadata.  # noqa: E501
        :rtype: ByteString
        """
        return self._org_id_bytes

    @org_id_bytes.setter
    def org_id_bytes(self, org_id_bytes):
        """Sets the org_id_bytes of this CcmGovernanceMetadata.


        :param org_id_bytes: The org_id_bytes of this CcmGovernanceMetadata.  # noqa: E501
        :type: ByteString
        """

        self._org_id_bytes = org_id_bytes

    @property
    def project_id_bytes(self):
        """Gets the project_id_bytes of this CcmGovernanceMetadata.  # noqa: E501


        :return: The project_id_bytes of this CcmGovernanceMetadata.  # noqa: E501
        :rtype: ByteString
        """
        return self._project_id_bytes

    @project_id_bytes.setter
    def project_id_bytes(self, project_id_bytes):
        """Sets the project_id_bytes of this CcmGovernanceMetadata.


        :param project_id_bytes: The project_id_bytes of this CcmGovernanceMetadata.  # noqa: E501
        :type: ByteString
        """

        self._project_id_bytes = project_id_bytes

    @property
    def entity_bytes(self):
        """Gets the entity_bytes of this CcmGovernanceMetadata.  # noqa: E501


        :return: The entity_bytes of this CcmGovernanceMetadata.  # noqa: E501
        :rtype: ByteString
        """
        return self._entity_bytes

    @entity_bytes.setter
    def entity_bytes(self, entity_bytes):
        """Sets the entity_bytes of this CcmGovernanceMetadata.


        :param entity_bytes: The entity_bytes of this CcmGovernanceMetadata.  # noqa: E501
        :type: ByteString
        """

        self._entity_bytes = entity_bytes

    @property
    def type_bytes(self):
        """Gets the type_bytes of this CcmGovernanceMetadata.  # noqa: E501


        :return: The type_bytes of this CcmGovernanceMetadata.  # noqa: E501
        :rtype: ByteString
        """
        return self._type_bytes

    @type_bytes.setter
    def type_bytes(self, type_bytes):
        """Sets the type_bytes of this CcmGovernanceMetadata.


        :param type_bytes: The type_bytes of this CcmGovernanceMetadata.  # noqa: E501
        :type: ByteString
        """

        self._type_bytes = type_bytes

    @property
    def action_bytes(self):
        """Gets the action_bytes of this CcmGovernanceMetadata.  # noqa: E501


        :return: The action_bytes of this CcmGovernanceMetadata.  # noqa: E501
        :rtype: ByteString
        """
        return self._action_bytes

    @action_bytes.setter
    def action_bytes(self, action_bytes):
        """Sets the action_bytes of this CcmGovernanceMetadata.


        :param action_bytes: The action_bytes of this CcmGovernanceMetadata.  # noqa: E501
        :type: ByteString
        """

        self._action_bytes = action_bytes

    @property
    def deny(self):
        """Gets the deny of this CcmGovernanceMetadata.  # noqa: E501


        :return: The deny of this CcmGovernanceMetadata.  # noqa: E501
        :rtype: bool
        """
        return self._deny

    @deny.setter
    def deny(self, deny):
        """Sets the deny of this CcmGovernanceMetadata.


        :param deny: The deny of this CcmGovernanceMetadata.  # noqa: E501
        :type: bool
        """

        self._deny = deny

    @property
    def details_list(self):
        """Gets the details_list of this CcmGovernanceMetadata.  # noqa: E501


        :return: The details_list of this CcmGovernanceMetadata.  # noqa: E501
        :rtype: list[CcmPolicySetMetadata]
        """
        return self._details_list

    @details_list.setter
    def details_list(self, details_list):
        """Sets the details_list of this CcmGovernanceMetadata.


        :param details_list: The details_list of this CcmGovernanceMetadata.  # noqa: E501
        :type: list[CcmPolicySetMetadata]
        """

        self._details_list = details_list

    @property
    def org_id(self):
        """Gets the org_id of this CcmGovernanceMetadata.  # noqa: E501


        :return: The org_id of this CcmGovernanceMetadata.  # noqa: E501
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this CcmGovernanceMetadata.


        :param org_id: The org_id of this CcmGovernanceMetadata.  # noqa: E501
        :type: str
        """

        self._org_id = org_id

    @property
    def details_count(self):
        """Gets the details_count of this CcmGovernanceMetadata.  # noqa: E501


        :return: The details_count of this CcmGovernanceMetadata.  # noqa: E501
        :rtype: int
        """
        return self._details_count

    @details_count.setter
    def details_count(self, details_count):
        """Sets the details_count of this CcmGovernanceMetadata.


        :param details_count: The details_count of this CcmGovernanceMetadata.  # noqa: E501
        :type: int
        """

        self._details_count = details_count

    @property
    def message_bytes(self):
        """Gets the message_bytes of this CcmGovernanceMetadata.  # noqa: E501


        :return: The message_bytes of this CcmGovernanceMetadata.  # noqa: E501
        :rtype: ByteString
        """
        return self._message_bytes

    @message_bytes.setter
    def message_bytes(self, message_bytes):
        """Sets the message_bytes of this CcmGovernanceMetadata.


        :param message_bytes: The message_bytes of this CcmGovernanceMetadata.  # noqa: E501
        :type: ByteString
        """

        self._message_bytes = message_bytes

    @property
    def details_or_builder_list(self):
        """Gets the details_or_builder_list of this CcmGovernanceMetadata.  # noqa: E501


        :return: The details_or_builder_list of this CcmGovernanceMetadata.  # noqa: E501
        :rtype: list[CcmPolicySetMetadataOrBuilder]
        """
        return self._details_or_builder_list

    @details_or_builder_list.setter
    def details_or_builder_list(self, details_or_builder_list):
        """Sets the details_or_builder_list of this CcmGovernanceMetadata.


        :param details_or_builder_list: The details_or_builder_list of this CcmGovernanceMetadata.  # noqa: E501
        :type: list[CcmPolicySetMetadataOrBuilder]
        """

        self._details_or_builder_list = details_or_builder_list

    @property
    def initialized(self):
        """Gets the initialized of this CcmGovernanceMetadata.  # noqa: E501


        :return: The initialized of this CcmGovernanceMetadata.  # noqa: E501
        :rtype: bool
        """
        return self._initialized

    @initialized.setter
    def initialized(self, initialized):
        """Sets the initialized of this CcmGovernanceMetadata.


        :param initialized: The initialized of this CcmGovernanceMetadata.  # noqa: E501
        :type: bool
        """

        self._initialized = initialized

    @property
    def descriptor_for_type(self):
        """Gets the descriptor_for_type of this CcmGovernanceMetadata.  # noqa: E501


        :return: The descriptor_for_type of this CcmGovernanceMetadata.  # noqa: E501
        :rtype: Descriptor
        """
        return self._descriptor_for_type

    @descriptor_for_type.setter
    def descriptor_for_type(self, descriptor_for_type):
        """Sets the descriptor_for_type of this CcmGovernanceMetadata.


        :param descriptor_for_type: The descriptor_for_type of this CcmGovernanceMetadata.  # noqa: E501
        :type: Descriptor
        """

        self._descriptor_for_type = descriptor_for_type

    @property
    def all_fields(self):
        """Gets the all_fields of this CcmGovernanceMetadata.  # noqa: E501


        :return: The all_fields of this CcmGovernanceMetadata.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._all_fields

    @all_fields.setter
    def all_fields(self, all_fields):
        """Sets the all_fields of this CcmGovernanceMetadata.


        :param all_fields: The all_fields of this CcmGovernanceMetadata.  # noqa: E501
        :type: dict(str, object)
        """

        self._all_fields = all_fields

    @property
    def initialization_error_string(self):
        """Gets the initialization_error_string of this CcmGovernanceMetadata.  # noqa: E501


        :return: The initialization_error_string of this CcmGovernanceMetadata.  # noqa: E501
        :rtype: str
        """
        return self._initialization_error_string

    @initialization_error_string.setter
    def initialization_error_string(self, initialization_error_string):
        """Sets the initialization_error_string of this CcmGovernanceMetadata.


        :param initialization_error_string: The initialization_error_string of this CcmGovernanceMetadata.  # noqa: E501
        :type: str
        """

        self._initialization_error_string = initialization_error_string

    @property
    def memoized_serialized_size(self):
        """Gets the memoized_serialized_size of this CcmGovernanceMetadata.  # noqa: E501


        :return: The memoized_serialized_size of this CcmGovernanceMetadata.  # noqa: E501
        :rtype: int
        """
        return self._memoized_serialized_size

    @memoized_serialized_size.setter
    def memoized_serialized_size(self, memoized_serialized_size):
        """Sets the memoized_serialized_size of this CcmGovernanceMetadata.


        :param memoized_serialized_size: The memoized_serialized_size of this CcmGovernanceMetadata.  # noqa: E501
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
        if issubclass(CcmGovernanceMetadata, dict):
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
        if not isinstance(other, CcmGovernanceMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
