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

class Ambiance(object):
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
        'metadata': 'ExecutionMetadata',
        'plan_execution_id': 'str',
        'serialized_size': 'int',
        'parser_for_type': 'ParserAmbiance',
        'default_instance_for_type': 'Ambiance',
        'setup_abstractions': 'dict(str, str)',
        'setup_abstractions_map': 'dict(str, str)',
        'plan_id': 'str',
        'stage_execution_id': 'str',
        'levels_list': 'list[Level]',
        'start_ts': 'int',
        'expression_functor_token': 'int',
        'levels_count': 'int',
        'metadata_or_builder': 'ExecutionMetadataOrBuilder',
        'plan_id_bytes': 'ByteString',
        'stage_execution_id_bytes': 'ByteString',
        'original_stage_execution_id_for_rollback_mode': 'str',
        'original_stage_execution_id_for_rollback_mode_bytes': 'ByteString',
        'plan_execution_id_bytes': 'ByteString',
        'setup_abstractions_count': 'int',
        'levels_or_builder_list': 'list[LevelOrBuilder]',
        'initialized': 'bool',
        'all_fields': 'dict(str, object)',
        'descriptor_for_type': 'Descriptor',
        'initialization_error_string': 'str',
        'memoized_serialized_size': 'int'
    }

    attribute_map = {
        'unknown_fields': 'unknownFields',
        'metadata': 'metadata',
        'plan_execution_id': 'planExecutionId',
        'serialized_size': 'serializedSize',
        'parser_for_type': 'parserForType',
        'default_instance_for_type': 'defaultInstanceForType',
        'setup_abstractions': 'setupAbstractions',
        'setup_abstractions_map': 'setupAbstractionsMap',
        'plan_id': 'planId',
        'stage_execution_id': 'stageExecutionId',
        'levels_list': 'levelsList',
        'start_ts': 'startTs',
        'expression_functor_token': 'expressionFunctorToken',
        'levels_count': 'levelsCount',
        'metadata_or_builder': 'metadataOrBuilder',
        'plan_id_bytes': 'planIdBytes',
        'stage_execution_id_bytes': 'stageExecutionIdBytes',
        'original_stage_execution_id_for_rollback_mode': 'originalStageExecutionIdForRollbackMode',
        'original_stage_execution_id_for_rollback_mode_bytes': 'originalStageExecutionIdForRollbackModeBytes',
        'plan_execution_id_bytes': 'planExecutionIdBytes',
        'setup_abstractions_count': 'setupAbstractionsCount',
        'levels_or_builder_list': 'levelsOrBuilderList',
        'initialized': 'initialized',
        'all_fields': 'allFields',
        'descriptor_for_type': 'descriptorForType',
        'initialization_error_string': 'initializationErrorString',
        'memoized_serialized_size': 'memoizedSerializedSize'
    }

    def __init__(self, unknown_fields=None, metadata=None, plan_execution_id=None, serialized_size=None, parser_for_type=None, default_instance_for_type=None, setup_abstractions=None, setup_abstractions_map=None, plan_id=None, stage_execution_id=None, levels_list=None, start_ts=None, expression_functor_token=None, levels_count=None, metadata_or_builder=None, plan_id_bytes=None, stage_execution_id_bytes=None, original_stage_execution_id_for_rollback_mode=None, original_stage_execution_id_for_rollback_mode_bytes=None, plan_execution_id_bytes=None, setup_abstractions_count=None, levels_or_builder_list=None, initialized=None, all_fields=None, descriptor_for_type=None, initialization_error_string=None, memoized_serialized_size=None):  # noqa: E501
        """Ambiance - a model defined in Swagger"""  # noqa: E501
        self._unknown_fields = None
        self._metadata = None
        self._plan_execution_id = None
        self._serialized_size = None
        self._parser_for_type = None
        self._default_instance_for_type = None
        self._setup_abstractions = None
        self._setup_abstractions_map = None
        self._plan_id = None
        self._stage_execution_id = None
        self._levels_list = None
        self._start_ts = None
        self._expression_functor_token = None
        self._levels_count = None
        self._metadata_or_builder = None
        self._plan_id_bytes = None
        self._stage_execution_id_bytes = None
        self._original_stage_execution_id_for_rollback_mode = None
        self._original_stage_execution_id_for_rollback_mode_bytes = None
        self._plan_execution_id_bytes = None
        self._setup_abstractions_count = None
        self._levels_or_builder_list = None
        self._initialized = None
        self._all_fields = None
        self._descriptor_for_type = None
        self._initialization_error_string = None
        self._memoized_serialized_size = None
        self.discriminator = None
        if unknown_fields is not None:
            self.unknown_fields = unknown_fields
        if metadata is not None:
            self.metadata = metadata
        if plan_execution_id is not None:
            self.plan_execution_id = plan_execution_id
        if serialized_size is not None:
            self.serialized_size = serialized_size
        if parser_for_type is not None:
            self.parser_for_type = parser_for_type
        if default_instance_for_type is not None:
            self.default_instance_for_type = default_instance_for_type
        if setup_abstractions is not None:
            self.setup_abstractions = setup_abstractions
        if setup_abstractions_map is not None:
            self.setup_abstractions_map = setup_abstractions_map
        if plan_id is not None:
            self.plan_id = plan_id
        if stage_execution_id is not None:
            self.stage_execution_id = stage_execution_id
        if levels_list is not None:
            self.levels_list = levels_list
        if start_ts is not None:
            self.start_ts = start_ts
        if expression_functor_token is not None:
            self.expression_functor_token = expression_functor_token
        if levels_count is not None:
            self.levels_count = levels_count
        if metadata_or_builder is not None:
            self.metadata_or_builder = metadata_or_builder
        if plan_id_bytes is not None:
            self.plan_id_bytes = plan_id_bytes
        if stage_execution_id_bytes is not None:
            self.stage_execution_id_bytes = stage_execution_id_bytes
        if original_stage_execution_id_for_rollback_mode is not None:
            self.original_stage_execution_id_for_rollback_mode = original_stage_execution_id_for_rollback_mode
        if original_stage_execution_id_for_rollback_mode_bytes is not None:
            self.original_stage_execution_id_for_rollback_mode_bytes = original_stage_execution_id_for_rollback_mode_bytes
        if plan_execution_id_bytes is not None:
            self.plan_execution_id_bytes = plan_execution_id_bytes
        if setup_abstractions_count is not None:
            self.setup_abstractions_count = setup_abstractions_count
        if levels_or_builder_list is not None:
            self.levels_or_builder_list = levels_or_builder_list
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
        """Gets the unknown_fields of this Ambiance.  # noqa: E501


        :return: The unknown_fields of this Ambiance.  # noqa: E501
        :rtype: UnknownFieldSet
        """
        return self._unknown_fields

    @unknown_fields.setter
    def unknown_fields(self, unknown_fields):
        """Sets the unknown_fields of this Ambiance.


        :param unknown_fields: The unknown_fields of this Ambiance.  # noqa: E501
        :type: UnknownFieldSet
        """

        self._unknown_fields = unknown_fields

    @property
    def metadata(self):
        """Gets the metadata of this Ambiance.  # noqa: E501


        :return: The metadata of this Ambiance.  # noqa: E501
        :rtype: ExecutionMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Ambiance.


        :param metadata: The metadata of this Ambiance.  # noqa: E501
        :type: ExecutionMetadata
        """

        self._metadata = metadata

    @property
    def plan_execution_id(self):
        """Gets the plan_execution_id of this Ambiance.  # noqa: E501


        :return: The plan_execution_id of this Ambiance.  # noqa: E501
        :rtype: str
        """
        return self._plan_execution_id

    @plan_execution_id.setter
    def plan_execution_id(self, plan_execution_id):
        """Sets the plan_execution_id of this Ambiance.


        :param plan_execution_id: The plan_execution_id of this Ambiance.  # noqa: E501
        :type: str
        """

        self._plan_execution_id = plan_execution_id

    @property
    def serialized_size(self):
        """Gets the serialized_size of this Ambiance.  # noqa: E501


        :return: The serialized_size of this Ambiance.  # noqa: E501
        :rtype: int
        """
        return self._serialized_size

    @serialized_size.setter
    def serialized_size(self, serialized_size):
        """Sets the serialized_size of this Ambiance.


        :param serialized_size: The serialized_size of this Ambiance.  # noqa: E501
        :type: int
        """

        self._serialized_size = serialized_size

    @property
    def parser_for_type(self):
        """Gets the parser_for_type of this Ambiance.  # noqa: E501


        :return: The parser_for_type of this Ambiance.  # noqa: E501
        :rtype: ParserAmbiance
        """
        return self._parser_for_type

    @parser_for_type.setter
    def parser_for_type(self, parser_for_type):
        """Sets the parser_for_type of this Ambiance.


        :param parser_for_type: The parser_for_type of this Ambiance.  # noqa: E501
        :type: ParserAmbiance
        """

        self._parser_for_type = parser_for_type

    @property
    def default_instance_for_type(self):
        """Gets the default_instance_for_type of this Ambiance.  # noqa: E501


        :return: The default_instance_for_type of this Ambiance.  # noqa: E501
        :rtype: Ambiance
        """
        return self._default_instance_for_type

    @default_instance_for_type.setter
    def default_instance_for_type(self, default_instance_for_type):
        """Sets the default_instance_for_type of this Ambiance.


        :param default_instance_for_type: The default_instance_for_type of this Ambiance.  # noqa: E501
        :type: Ambiance
        """

        self._default_instance_for_type = default_instance_for_type

    @property
    def setup_abstractions(self):
        """Gets the setup_abstractions of this Ambiance.  # noqa: E501


        :return: The setup_abstractions of this Ambiance.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._setup_abstractions

    @setup_abstractions.setter
    def setup_abstractions(self, setup_abstractions):
        """Sets the setup_abstractions of this Ambiance.


        :param setup_abstractions: The setup_abstractions of this Ambiance.  # noqa: E501
        :type: dict(str, str)
        """

        self._setup_abstractions = setup_abstractions

    @property
    def setup_abstractions_map(self):
        """Gets the setup_abstractions_map of this Ambiance.  # noqa: E501


        :return: The setup_abstractions_map of this Ambiance.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._setup_abstractions_map

    @setup_abstractions_map.setter
    def setup_abstractions_map(self, setup_abstractions_map):
        """Sets the setup_abstractions_map of this Ambiance.


        :param setup_abstractions_map: The setup_abstractions_map of this Ambiance.  # noqa: E501
        :type: dict(str, str)
        """

        self._setup_abstractions_map = setup_abstractions_map

    @property
    def plan_id(self):
        """Gets the plan_id of this Ambiance.  # noqa: E501


        :return: The plan_id of this Ambiance.  # noqa: E501
        :rtype: str
        """
        return self._plan_id

    @plan_id.setter
    def plan_id(self, plan_id):
        """Sets the plan_id of this Ambiance.


        :param plan_id: The plan_id of this Ambiance.  # noqa: E501
        :type: str
        """

        self._plan_id = plan_id

    @property
    def stage_execution_id(self):
        """Gets the stage_execution_id of this Ambiance.  # noqa: E501


        :return: The stage_execution_id of this Ambiance.  # noqa: E501
        :rtype: str
        """
        return self._stage_execution_id

    @stage_execution_id.setter
    def stage_execution_id(self, stage_execution_id):
        """Sets the stage_execution_id of this Ambiance.


        :param stage_execution_id: The stage_execution_id of this Ambiance.  # noqa: E501
        :type: str
        """

        self._stage_execution_id = stage_execution_id

    @property
    def levels_list(self):
        """Gets the levels_list of this Ambiance.  # noqa: E501


        :return: The levels_list of this Ambiance.  # noqa: E501
        :rtype: list[Level]
        """
        return self._levels_list

    @levels_list.setter
    def levels_list(self, levels_list):
        """Sets the levels_list of this Ambiance.


        :param levels_list: The levels_list of this Ambiance.  # noqa: E501
        :type: list[Level]
        """

        self._levels_list = levels_list

    @property
    def start_ts(self):
        """Gets the start_ts of this Ambiance.  # noqa: E501


        :return: The start_ts of this Ambiance.  # noqa: E501
        :rtype: int
        """
        return self._start_ts

    @start_ts.setter
    def start_ts(self, start_ts):
        """Sets the start_ts of this Ambiance.


        :param start_ts: The start_ts of this Ambiance.  # noqa: E501
        :type: int
        """

        self._start_ts = start_ts

    @property
    def expression_functor_token(self):
        """Gets the expression_functor_token of this Ambiance.  # noqa: E501


        :return: The expression_functor_token of this Ambiance.  # noqa: E501
        :rtype: int
        """
        return self._expression_functor_token

    @expression_functor_token.setter
    def expression_functor_token(self, expression_functor_token):
        """Sets the expression_functor_token of this Ambiance.


        :param expression_functor_token: The expression_functor_token of this Ambiance.  # noqa: E501
        :type: int
        """

        self._expression_functor_token = expression_functor_token

    @property
    def levels_count(self):
        """Gets the levels_count of this Ambiance.  # noqa: E501


        :return: The levels_count of this Ambiance.  # noqa: E501
        :rtype: int
        """
        return self._levels_count

    @levels_count.setter
    def levels_count(self, levels_count):
        """Sets the levels_count of this Ambiance.


        :param levels_count: The levels_count of this Ambiance.  # noqa: E501
        :type: int
        """

        self._levels_count = levels_count

    @property
    def metadata_or_builder(self):
        """Gets the metadata_or_builder of this Ambiance.  # noqa: E501


        :return: The metadata_or_builder of this Ambiance.  # noqa: E501
        :rtype: ExecutionMetadataOrBuilder
        """
        return self._metadata_or_builder

    @metadata_or_builder.setter
    def metadata_or_builder(self, metadata_or_builder):
        """Sets the metadata_or_builder of this Ambiance.


        :param metadata_or_builder: The metadata_or_builder of this Ambiance.  # noqa: E501
        :type: ExecutionMetadataOrBuilder
        """

        self._metadata_or_builder = metadata_or_builder

    @property
    def plan_id_bytes(self):
        """Gets the plan_id_bytes of this Ambiance.  # noqa: E501


        :return: The plan_id_bytes of this Ambiance.  # noqa: E501
        :rtype: ByteString
        """
        return self._plan_id_bytes

    @plan_id_bytes.setter
    def plan_id_bytes(self, plan_id_bytes):
        """Sets the plan_id_bytes of this Ambiance.


        :param plan_id_bytes: The plan_id_bytes of this Ambiance.  # noqa: E501
        :type: ByteString
        """

        self._plan_id_bytes = plan_id_bytes

    @property
    def stage_execution_id_bytes(self):
        """Gets the stage_execution_id_bytes of this Ambiance.  # noqa: E501


        :return: The stage_execution_id_bytes of this Ambiance.  # noqa: E501
        :rtype: ByteString
        """
        return self._stage_execution_id_bytes

    @stage_execution_id_bytes.setter
    def stage_execution_id_bytes(self, stage_execution_id_bytes):
        """Sets the stage_execution_id_bytes of this Ambiance.


        :param stage_execution_id_bytes: The stage_execution_id_bytes of this Ambiance.  # noqa: E501
        :type: ByteString
        """

        self._stage_execution_id_bytes = stage_execution_id_bytes

    @property
    def original_stage_execution_id_for_rollback_mode(self):
        """Gets the original_stage_execution_id_for_rollback_mode of this Ambiance.  # noqa: E501


        :return: The original_stage_execution_id_for_rollback_mode of this Ambiance.  # noqa: E501
        :rtype: str
        """
        return self._original_stage_execution_id_for_rollback_mode

    @original_stage_execution_id_for_rollback_mode.setter
    def original_stage_execution_id_for_rollback_mode(self, original_stage_execution_id_for_rollback_mode):
        """Sets the original_stage_execution_id_for_rollback_mode of this Ambiance.


        :param original_stage_execution_id_for_rollback_mode: The original_stage_execution_id_for_rollback_mode of this Ambiance.  # noqa: E501
        :type: str
        """

        self._original_stage_execution_id_for_rollback_mode = original_stage_execution_id_for_rollback_mode

    @property
    def original_stage_execution_id_for_rollback_mode_bytes(self):
        """Gets the original_stage_execution_id_for_rollback_mode_bytes of this Ambiance.  # noqa: E501


        :return: The original_stage_execution_id_for_rollback_mode_bytes of this Ambiance.  # noqa: E501
        :rtype: ByteString
        """
        return self._original_stage_execution_id_for_rollback_mode_bytes

    @original_stage_execution_id_for_rollback_mode_bytes.setter
    def original_stage_execution_id_for_rollback_mode_bytes(self, original_stage_execution_id_for_rollback_mode_bytes):
        """Sets the original_stage_execution_id_for_rollback_mode_bytes of this Ambiance.


        :param original_stage_execution_id_for_rollback_mode_bytes: The original_stage_execution_id_for_rollback_mode_bytes of this Ambiance.  # noqa: E501
        :type: ByteString
        """

        self._original_stage_execution_id_for_rollback_mode_bytes = original_stage_execution_id_for_rollback_mode_bytes

    @property
    def plan_execution_id_bytes(self):
        """Gets the plan_execution_id_bytes of this Ambiance.  # noqa: E501


        :return: The plan_execution_id_bytes of this Ambiance.  # noqa: E501
        :rtype: ByteString
        """
        return self._plan_execution_id_bytes

    @plan_execution_id_bytes.setter
    def plan_execution_id_bytes(self, plan_execution_id_bytes):
        """Sets the plan_execution_id_bytes of this Ambiance.


        :param plan_execution_id_bytes: The plan_execution_id_bytes of this Ambiance.  # noqa: E501
        :type: ByteString
        """

        self._plan_execution_id_bytes = plan_execution_id_bytes

    @property
    def setup_abstractions_count(self):
        """Gets the setup_abstractions_count of this Ambiance.  # noqa: E501


        :return: The setup_abstractions_count of this Ambiance.  # noqa: E501
        :rtype: int
        """
        return self._setup_abstractions_count

    @setup_abstractions_count.setter
    def setup_abstractions_count(self, setup_abstractions_count):
        """Sets the setup_abstractions_count of this Ambiance.


        :param setup_abstractions_count: The setup_abstractions_count of this Ambiance.  # noqa: E501
        :type: int
        """

        self._setup_abstractions_count = setup_abstractions_count

    @property
    def levels_or_builder_list(self):
        """Gets the levels_or_builder_list of this Ambiance.  # noqa: E501


        :return: The levels_or_builder_list of this Ambiance.  # noqa: E501
        :rtype: list[LevelOrBuilder]
        """
        return self._levels_or_builder_list

    @levels_or_builder_list.setter
    def levels_or_builder_list(self, levels_or_builder_list):
        """Sets the levels_or_builder_list of this Ambiance.


        :param levels_or_builder_list: The levels_or_builder_list of this Ambiance.  # noqa: E501
        :type: list[LevelOrBuilder]
        """

        self._levels_or_builder_list = levels_or_builder_list

    @property
    def initialized(self):
        """Gets the initialized of this Ambiance.  # noqa: E501


        :return: The initialized of this Ambiance.  # noqa: E501
        :rtype: bool
        """
        return self._initialized

    @initialized.setter
    def initialized(self, initialized):
        """Sets the initialized of this Ambiance.


        :param initialized: The initialized of this Ambiance.  # noqa: E501
        :type: bool
        """

        self._initialized = initialized

    @property
    def all_fields(self):
        """Gets the all_fields of this Ambiance.  # noqa: E501


        :return: The all_fields of this Ambiance.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._all_fields

    @all_fields.setter
    def all_fields(self, all_fields):
        """Sets the all_fields of this Ambiance.


        :param all_fields: The all_fields of this Ambiance.  # noqa: E501
        :type: dict(str, object)
        """

        self._all_fields = all_fields

    @property
    def descriptor_for_type(self):
        """Gets the descriptor_for_type of this Ambiance.  # noqa: E501


        :return: The descriptor_for_type of this Ambiance.  # noqa: E501
        :rtype: Descriptor
        """
        return self._descriptor_for_type

    @descriptor_for_type.setter
    def descriptor_for_type(self, descriptor_for_type):
        """Sets the descriptor_for_type of this Ambiance.


        :param descriptor_for_type: The descriptor_for_type of this Ambiance.  # noqa: E501
        :type: Descriptor
        """

        self._descriptor_for_type = descriptor_for_type

    @property
    def initialization_error_string(self):
        """Gets the initialization_error_string of this Ambiance.  # noqa: E501


        :return: The initialization_error_string of this Ambiance.  # noqa: E501
        :rtype: str
        """
        return self._initialization_error_string

    @initialization_error_string.setter
    def initialization_error_string(self, initialization_error_string):
        """Sets the initialization_error_string of this Ambiance.


        :param initialization_error_string: The initialization_error_string of this Ambiance.  # noqa: E501
        :type: str
        """

        self._initialization_error_string = initialization_error_string

    @property
    def memoized_serialized_size(self):
        """Gets the memoized_serialized_size of this Ambiance.  # noqa: E501


        :return: The memoized_serialized_size of this Ambiance.  # noqa: E501
        :rtype: int
        """
        return self._memoized_serialized_size

    @memoized_serialized_size.setter
    def memoized_serialized_size(self, memoized_serialized_size):
        """Sets the memoized_serialized_size of this Ambiance.


        :param memoized_serialized_size: The memoized_serialized_size of this Ambiance.  # noqa: E501
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
        if issubclass(Ambiance, dict):
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
        if not isinstance(other, Ambiance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
