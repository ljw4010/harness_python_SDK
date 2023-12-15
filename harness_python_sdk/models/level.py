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

class Level(object):
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
        'group': 'str',
        'node_type': 'str',
        'identifier': 'str',
        'serialized_size': 'int',
        'parser_for_type': 'ParserLevel',
        'default_instance_for_type': 'Level',
        'identifier_bytes': 'ByteString',
        'strategy_metadata': 'StrategyMetadata',
        'step_type': 'StepType',
        'start_ts': 'int',
        'runtime_id': 'str',
        'skip_expression_chain': 'bool',
        'runtime_id_bytes': 'ByteString',
        'step_type_or_builder': 'StepTypeOrBuilder',
        'group_bytes': 'ByteString',
        'setup_id_bytes': 'ByteString',
        'setup_id': 'str',
        'retry_index': 'int',
        'node_type_bytes': 'ByteString',
        'strategy_metadata_or_builder': 'StrategyMetadataOrBuilder',
        'original_identifier': 'str',
        'original_identifier_bytes': 'ByteString',
        'initialized': 'bool',
        'all_fields': 'dict(str, object)',
        'descriptor_for_type': 'Descriptor',
        'initialization_error_string': 'str',
        'memoized_serialized_size': 'int'
    }

    attribute_map = {
        'unknown_fields': 'unknownFields',
        'group': 'group',
        'node_type': 'nodeType',
        'identifier': 'identifier',
        'serialized_size': 'serializedSize',
        'parser_for_type': 'parserForType',
        'default_instance_for_type': 'defaultInstanceForType',
        'identifier_bytes': 'identifierBytes',
        'strategy_metadata': 'strategyMetadata',
        'step_type': 'stepType',
        'start_ts': 'startTs',
        'runtime_id': 'runtimeId',
        'skip_expression_chain': 'skipExpressionChain',
        'runtime_id_bytes': 'runtimeIdBytes',
        'step_type_or_builder': 'stepTypeOrBuilder',
        'group_bytes': 'groupBytes',
        'setup_id_bytes': 'setupIdBytes',
        'setup_id': 'setupId',
        'retry_index': 'retryIndex',
        'node_type_bytes': 'nodeTypeBytes',
        'strategy_metadata_or_builder': 'strategyMetadataOrBuilder',
        'original_identifier': 'originalIdentifier',
        'original_identifier_bytes': 'originalIdentifierBytes',
        'initialized': 'initialized',
        'all_fields': 'allFields',
        'descriptor_for_type': 'descriptorForType',
        'initialization_error_string': 'initializationErrorString',
        'memoized_serialized_size': 'memoizedSerializedSize'
    }

    def __init__(self, unknown_fields=None, group=None, node_type=None, identifier=None, serialized_size=None, parser_for_type=None, default_instance_for_type=None, identifier_bytes=None, strategy_metadata=None, step_type=None, start_ts=None, runtime_id=None, skip_expression_chain=None, runtime_id_bytes=None, step_type_or_builder=None, group_bytes=None, setup_id_bytes=None, setup_id=None, retry_index=None, node_type_bytes=None, strategy_metadata_or_builder=None, original_identifier=None, original_identifier_bytes=None, initialized=None, all_fields=None, descriptor_for_type=None, initialization_error_string=None, memoized_serialized_size=None):  # noqa: E501
        """Level - a model defined in Swagger"""  # noqa: E501
        self._unknown_fields = None
        self._group = None
        self._node_type = None
        self._identifier = None
        self._serialized_size = None
        self._parser_for_type = None
        self._default_instance_for_type = None
        self._identifier_bytes = None
        self._strategy_metadata = None
        self._step_type = None
        self._start_ts = None
        self._runtime_id = None
        self._skip_expression_chain = None
        self._runtime_id_bytes = None
        self._step_type_or_builder = None
        self._group_bytes = None
        self._setup_id_bytes = None
        self._setup_id = None
        self._retry_index = None
        self._node_type_bytes = None
        self._strategy_metadata_or_builder = None
        self._original_identifier = None
        self._original_identifier_bytes = None
        self._initialized = None
        self._all_fields = None
        self._descriptor_for_type = None
        self._initialization_error_string = None
        self._memoized_serialized_size = None
        self.discriminator = None
        if unknown_fields is not None:
            self.unknown_fields = unknown_fields
        if group is not None:
            self.group = group
        if node_type is not None:
            self.node_type = node_type
        if identifier is not None:
            self.identifier = identifier
        if serialized_size is not None:
            self.serialized_size = serialized_size
        if parser_for_type is not None:
            self.parser_for_type = parser_for_type
        if default_instance_for_type is not None:
            self.default_instance_for_type = default_instance_for_type
        if identifier_bytes is not None:
            self.identifier_bytes = identifier_bytes
        if strategy_metadata is not None:
            self.strategy_metadata = strategy_metadata
        if step_type is not None:
            self.step_type = step_type
        if start_ts is not None:
            self.start_ts = start_ts
        if runtime_id is not None:
            self.runtime_id = runtime_id
        if skip_expression_chain is not None:
            self.skip_expression_chain = skip_expression_chain
        if runtime_id_bytes is not None:
            self.runtime_id_bytes = runtime_id_bytes
        if step_type_or_builder is not None:
            self.step_type_or_builder = step_type_or_builder
        if group_bytes is not None:
            self.group_bytes = group_bytes
        if setup_id_bytes is not None:
            self.setup_id_bytes = setup_id_bytes
        if setup_id is not None:
            self.setup_id = setup_id
        if retry_index is not None:
            self.retry_index = retry_index
        if node_type_bytes is not None:
            self.node_type_bytes = node_type_bytes
        if strategy_metadata_or_builder is not None:
            self.strategy_metadata_or_builder = strategy_metadata_or_builder
        if original_identifier is not None:
            self.original_identifier = original_identifier
        if original_identifier_bytes is not None:
            self.original_identifier_bytes = original_identifier_bytes
        if initialized is not None:
            self.initialized = initialized
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
        """Gets the unknown_fields of this Level.  # noqa: E501


        :return: The unknown_fields of this Level.  # noqa: E501
        :rtype: UnknownFieldSet
        """
        return self._unknown_fields

    @unknown_fields.setter
    def unknown_fields(self, unknown_fields):
        """Sets the unknown_fields of this Level.


        :param unknown_fields: The unknown_fields of this Level.  # noqa: E501
        :type: UnknownFieldSet
        """

        self._unknown_fields = unknown_fields

    @property
    def group(self):
        """Gets the group of this Level.  # noqa: E501


        :return: The group of this Level.  # noqa: E501
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this Level.


        :param group: The group of this Level.  # noqa: E501
        :type: str
        """

        self._group = group

    @property
    def node_type(self):
        """Gets the node_type of this Level.  # noqa: E501


        :return: The node_type of this Level.  # noqa: E501
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        """Sets the node_type of this Level.


        :param node_type: The node_type of this Level.  # noqa: E501
        :type: str
        """

        self._node_type = node_type

    @property
    def identifier(self):
        """Gets the identifier of this Level.  # noqa: E501


        :return: The identifier of this Level.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this Level.


        :param identifier: The identifier of this Level.  # noqa: E501
        :type: str
        """

        self._identifier = identifier

    @property
    def serialized_size(self):
        """Gets the serialized_size of this Level.  # noqa: E501


        :return: The serialized_size of this Level.  # noqa: E501
        :rtype: int
        """
        return self._serialized_size

    @serialized_size.setter
    def serialized_size(self, serialized_size):
        """Sets the serialized_size of this Level.


        :param serialized_size: The serialized_size of this Level.  # noqa: E501
        :type: int
        """

        self._serialized_size = serialized_size

    @property
    def parser_for_type(self):
        """Gets the parser_for_type of this Level.  # noqa: E501


        :return: The parser_for_type of this Level.  # noqa: E501
        :rtype: ParserLevel
        """
        return self._parser_for_type

    @parser_for_type.setter
    def parser_for_type(self, parser_for_type):
        """Sets the parser_for_type of this Level.


        :param parser_for_type: The parser_for_type of this Level.  # noqa: E501
        :type: ParserLevel
        """

        self._parser_for_type = parser_for_type

    @property
    def default_instance_for_type(self):
        """Gets the default_instance_for_type of this Level.  # noqa: E501


        :return: The default_instance_for_type of this Level.  # noqa: E501
        :rtype: Level
        """
        return self._default_instance_for_type

    @default_instance_for_type.setter
    def default_instance_for_type(self, default_instance_for_type):
        """Sets the default_instance_for_type of this Level.


        :param default_instance_for_type: The default_instance_for_type of this Level.  # noqa: E501
        :type: Level
        """

        self._default_instance_for_type = default_instance_for_type

    @property
    def identifier_bytes(self):
        """Gets the identifier_bytes of this Level.  # noqa: E501


        :return: The identifier_bytes of this Level.  # noqa: E501
        :rtype: ByteString
        """
        return self._identifier_bytes

    @identifier_bytes.setter
    def identifier_bytes(self, identifier_bytes):
        """Sets the identifier_bytes of this Level.


        :param identifier_bytes: The identifier_bytes of this Level.  # noqa: E501
        :type: ByteString
        """

        self._identifier_bytes = identifier_bytes

    @property
    def strategy_metadata(self):
        """Gets the strategy_metadata of this Level.  # noqa: E501


        :return: The strategy_metadata of this Level.  # noqa: E501
        :rtype: StrategyMetadata
        """
        return self._strategy_metadata

    @strategy_metadata.setter
    def strategy_metadata(self, strategy_metadata):
        """Sets the strategy_metadata of this Level.


        :param strategy_metadata: The strategy_metadata of this Level.  # noqa: E501
        :type: StrategyMetadata
        """

        self._strategy_metadata = strategy_metadata

    @property
    def step_type(self):
        """Gets the step_type of this Level.  # noqa: E501


        :return: The step_type of this Level.  # noqa: E501
        :rtype: StepType
        """
        return self._step_type

    @step_type.setter
    def step_type(self, step_type):
        """Sets the step_type of this Level.


        :param step_type: The step_type of this Level.  # noqa: E501
        :type: StepType
        """

        self._step_type = step_type

    @property
    def start_ts(self):
        """Gets the start_ts of this Level.  # noqa: E501


        :return: The start_ts of this Level.  # noqa: E501
        :rtype: int
        """
        return self._start_ts

    @start_ts.setter
    def start_ts(self, start_ts):
        """Sets the start_ts of this Level.


        :param start_ts: The start_ts of this Level.  # noqa: E501
        :type: int
        """

        self._start_ts = start_ts

    @property
    def runtime_id(self):
        """Gets the runtime_id of this Level.  # noqa: E501


        :return: The runtime_id of this Level.  # noqa: E501
        :rtype: str
        """
        return self._runtime_id

    @runtime_id.setter
    def runtime_id(self, runtime_id):
        """Sets the runtime_id of this Level.


        :param runtime_id: The runtime_id of this Level.  # noqa: E501
        :type: str
        """

        self._runtime_id = runtime_id

    @property
    def skip_expression_chain(self):
        """Gets the skip_expression_chain of this Level.  # noqa: E501


        :return: The skip_expression_chain of this Level.  # noqa: E501
        :rtype: bool
        """
        return self._skip_expression_chain

    @skip_expression_chain.setter
    def skip_expression_chain(self, skip_expression_chain):
        """Sets the skip_expression_chain of this Level.


        :param skip_expression_chain: The skip_expression_chain of this Level.  # noqa: E501
        :type: bool
        """

        self._skip_expression_chain = skip_expression_chain

    @property
    def runtime_id_bytes(self):
        """Gets the runtime_id_bytes of this Level.  # noqa: E501


        :return: The runtime_id_bytes of this Level.  # noqa: E501
        :rtype: ByteString
        """
        return self._runtime_id_bytes

    @runtime_id_bytes.setter
    def runtime_id_bytes(self, runtime_id_bytes):
        """Sets the runtime_id_bytes of this Level.


        :param runtime_id_bytes: The runtime_id_bytes of this Level.  # noqa: E501
        :type: ByteString
        """

        self._runtime_id_bytes = runtime_id_bytes

    @property
    def step_type_or_builder(self):
        """Gets the step_type_or_builder of this Level.  # noqa: E501


        :return: The step_type_or_builder of this Level.  # noqa: E501
        :rtype: StepTypeOrBuilder
        """
        return self._step_type_or_builder

    @step_type_or_builder.setter
    def step_type_or_builder(self, step_type_or_builder):
        """Sets the step_type_or_builder of this Level.


        :param step_type_or_builder: The step_type_or_builder of this Level.  # noqa: E501
        :type: StepTypeOrBuilder
        """

        self._step_type_or_builder = step_type_or_builder

    @property
    def group_bytes(self):
        """Gets the group_bytes of this Level.  # noqa: E501


        :return: The group_bytes of this Level.  # noqa: E501
        :rtype: ByteString
        """
        return self._group_bytes

    @group_bytes.setter
    def group_bytes(self, group_bytes):
        """Sets the group_bytes of this Level.


        :param group_bytes: The group_bytes of this Level.  # noqa: E501
        :type: ByteString
        """

        self._group_bytes = group_bytes

    @property
    def setup_id_bytes(self):
        """Gets the setup_id_bytes of this Level.  # noqa: E501


        :return: The setup_id_bytes of this Level.  # noqa: E501
        :rtype: ByteString
        """
        return self._setup_id_bytes

    @setup_id_bytes.setter
    def setup_id_bytes(self, setup_id_bytes):
        """Sets the setup_id_bytes of this Level.


        :param setup_id_bytes: The setup_id_bytes of this Level.  # noqa: E501
        :type: ByteString
        """

        self._setup_id_bytes = setup_id_bytes

    @property
    def setup_id(self):
        """Gets the setup_id of this Level.  # noqa: E501


        :return: The setup_id of this Level.  # noqa: E501
        :rtype: str
        """
        return self._setup_id

    @setup_id.setter
    def setup_id(self, setup_id):
        """Sets the setup_id of this Level.


        :param setup_id: The setup_id of this Level.  # noqa: E501
        :type: str
        """

        self._setup_id = setup_id

    @property
    def retry_index(self):
        """Gets the retry_index of this Level.  # noqa: E501


        :return: The retry_index of this Level.  # noqa: E501
        :rtype: int
        """
        return self._retry_index

    @retry_index.setter
    def retry_index(self, retry_index):
        """Sets the retry_index of this Level.


        :param retry_index: The retry_index of this Level.  # noqa: E501
        :type: int
        """

        self._retry_index = retry_index

    @property
    def node_type_bytes(self):
        """Gets the node_type_bytes of this Level.  # noqa: E501


        :return: The node_type_bytes of this Level.  # noqa: E501
        :rtype: ByteString
        """
        return self._node_type_bytes

    @node_type_bytes.setter
    def node_type_bytes(self, node_type_bytes):
        """Sets the node_type_bytes of this Level.


        :param node_type_bytes: The node_type_bytes of this Level.  # noqa: E501
        :type: ByteString
        """

        self._node_type_bytes = node_type_bytes

    @property
    def strategy_metadata_or_builder(self):
        """Gets the strategy_metadata_or_builder of this Level.  # noqa: E501


        :return: The strategy_metadata_or_builder of this Level.  # noqa: E501
        :rtype: StrategyMetadataOrBuilder
        """
        return self._strategy_metadata_or_builder

    @strategy_metadata_or_builder.setter
    def strategy_metadata_or_builder(self, strategy_metadata_or_builder):
        """Sets the strategy_metadata_or_builder of this Level.


        :param strategy_metadata_or_builder: The strategy_metadata_or_builder of this Level.  # noqa: E501
        :type: StrategyMetadataOrBuilder
        """

        self._strategy_metadata_or_builder = strategy_metadata_or_builder

    @property
    def original_identifier(self):
        """Gets the original_identifier of this Level.  # noqa: E501


        :return: The original_identifier of this Level.  # noqa: E501
        :rtype: str
        """
        return self._original_identifier

    @original_identifier.setter
    def original_identifier(self, original_identifier):
        """Sets the original_identifier of this Level.


        :param original_identifier: The original_identifier of this Level.  # noqa: E501
        :type: str
        """

        self._original_identifier = original_identifier

    @property
    def original_identifier_bytes(self):
        """Gets the original_identifier_bytes of this Level.  # noqa: E501


        :return: The original_identifier_bytes of this Level.  # noqa: E501
        :rtype: ByteString
        """
        return self._original_identifier_bytes

    @original_identifier_bytes.setter
    def original_identifier_bytes(self, original_identifier_bytes):
        """Sets the original_identifier_bytes of this Level.


        :param original_identifier_bytes: The original_identifier_bytes of this Level.  # noqa: E501
        :type: ByteString
        """

        self._original_identifier_bytes = original_identifier_bytes

    @property
    def initialized(self):
        """Gets the initialized of this Level.  # noqa: E501


        :return: The initialized of this Level.  # noqa: E501
        :rtype: bool
        """
        return self._initialized

    @initialized.setter
    def initialized(self, initialized):
        """Sets the initialized of this Level.


        :param initialized: The initialized of this Level.  # noqa: E501
        :type: bool
        """

        self._initialized = initialized

    @property
    def all_fields(self):
        """Gets the all_fields of this Level.  # noqa: E501


        :return: The all_fields of this Level.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._all_fields

    @all_fields.setter
    def all_fields(self, all_fields):
        """Sets the all_fields of this Level.


        :param all_fields: The all_fields of this Level.  # noqa: E501
        :type: dict(str, object)
        """

        self._all_fields = all_fields

    @property
    def descriptor_for_type(self):
        """Gets the descriptor_for_type of this Level.  # noqa: E501


        :return: The descriptor_for_type of this Level.  # noqa: E501
        :rtype: Descriptor
        """
        return self._descriptor_for_type

    @descriptor_for_type.setter
    def descriptor_for_type(self, descriptor_for_type):
        """Sets the descriptor_for_type of this Level.


        :param descriptor_for_type: The descriptor_for_type of this Level.  # noqa: E501
        :type: Descriptor
        """

        self._descriptor_for_type = descriptor_for_type

    @property
    def initialization_error_string(self):
        """Gets the initialization_error_string of this Level.  # noqa: E501


        :return: The initialization_error_string of this Level.  # noqa: E501
        :rtype: str
        """
        return self._initialization_error_string

    @initialization_error_string.setter
    def initialization_error_string(self, initialization_error_string):
        """Sets the initialization_error_string of this Level.


        :param initialization_error_string: The initialization_error_string of this Level.  # noqa: E501
        :type: str
        """

        self._initialization_error_string = initialization_error_string

    @property
    def memoized_serialized_size(self):
        """Gets the memoized_serialized_size of this Level.  # noqa: E501


        :return: The memoized_serialized_size of this Level.  # noqa: E501
        :rtype: int
        """
        return self._memoized_serialized_size

    @memoized_serialized_size.setter
    def memoized_serialized_size(self, memoized_serialized_size):
        """Sets the memoized_serialized_size of this Level.


        :param memoized_serialized_size: The memoized_serialized_size of this Level.  # noqa: E501
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
        if issubclass(Level, dict):
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
        if not isinstance(other, Level):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
