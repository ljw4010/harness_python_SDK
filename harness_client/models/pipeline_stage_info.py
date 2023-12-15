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

class PipelineStageInfo(object):
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
        'execution_id_bytes': 'ByteString',
        'stage_node_id_bytes': 'ByteString',
        'identifier': 'str',
        'serialized_size': 'int',
        'parser_for_type': 'ParserPipelineStageInfo',
        'default_instance_for_type': 'PipelineStageInfo',
        'identifier_bytes': 'ByteString',
        'run_sequence': 'int',
        'org_id': 'str',
        'org_id_bytes': 'ByteString',
        'project_id': 'str',
        'project_id_bytes': 'ByteString',
        'has_parent_pipeline': 'bool',
        'stage_node_id': 'str',
        'execution_id': 'str',
        'initialized': 'bool',
        'all_fields': 'dict(str, object)',
        'descriptor_for_type': 'Descriptor',
        'initialization_error_string': 'str',
        'memoized_serialized_size': 'int'
    }

    attribute_map = {
        'unknown_fields': 'unknownFields',
        'execution_id_bytes': 'executionIdBytes',
        'stage_node_id_bytes': 'stageNodeIdBytes',
        'identifier': 'identifier',
        'serialized_size': 'serializedSize',
        'parser_for_type': 'parserForType',
        'default_instance_for_type': 'defaultInstanceForType',
        'identifier_bytes': 'identifierBytes',
        'run_sequence': 'runSequence',
        'org_id': 'orgId',
        'org_id_bytes': 'orgIdBytes',
        'project_id': 'projectId',
        'project_id_bytes': 'projectIdBytes',
        'has_parent_pipeline': 'hasParentPipeline',
        'stage_node_id': 'stageNodeId',
        'execution_id': 'executionId',
        'initialized': 'initialized',
        'all_fields': 'allFields',
        'descriptor_for_type': 'descriptorForType',
        'initialization_error_string': 'initializationErrorString',
        'memoized_serialized_size': 'memoizedSerializedSize'
    }

    def __init__(self, unknown_fields=None, execution_id_bytes=None, stage_node_id_bytes=None, identifier=None, serialized_size=None, parser_for_type=None, default_instance_for_type=None, identifier_bytes=None, run_sequence=None, org_id=None, org_id_bytes=None, project_id=None, project_id_bytes=None, has_parent_pipeline=None, stage_node_id=None, execution_id=None, initialized=None, all_fields=None, descriptor_for_type=None, initialization_error_string=None, memoized_serialized_size=None):  # noqa: E501
        """PipelineStageInfo - a model defined in Swagger"""  # noqa: E501
        self._unknown_fields = None
        self._execution_id_bytes = None
        self._stage_node_id_bytes = None
        self._identifier = None
        self._serialized_size = None
        self._parser_for_type = None
        self._default_instance_for_type = None
        self._identifier_bytes = None
        self._run_sequence = None
        self._org_id = None
        self._org_id_bytes = None
        self._project_id = None
        self._project_id_bytes = None
        self._has_parent_pipeline = None
        self._stage_node_id = None
        self._execution_id = None
        self._initialized = None
        self._all_fields = None
        self._descriptor_for_type = None
        self._initialization_error_string = None
        self._memoized_serialized_size = None
        self.discriminator = None
        if unknown_fields is not None:
            self.unknown_fields = unknown_fields
        if execution_id_bytes is not None:
            self.execution_id_bytes = execution_id_bytes
        if stage_node_id_bytes is not None:
            self.stage_node_id_bytes = stage_node_id_bytes
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
        if run_sequence is not None:
            self.run_sequence = run_sequence
        if org_id is not None:
            self.org_id = org_id
        if org_id_bytes is not None:
            self.org_id_bytes = org_id_bytes
        if project_id is not None:
            self.project_id = project_id
        if project_id_bytes is not None:
            self.project_id_bytes = project_id_bytes
        if has_parent_pipeline is not None:
            self.has_parent_pipeline = has_parent_pipeline
        if stage_node_id is not None:
            self.stage_node_id = stage_node_id
        if execution_id is not None:
            self.execution_id = execution_id
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
        """Gets the unknown_fields of this PipelineStageInfo.  # noqa: E501


        :return: The unknown_fields of this PipelineStageInfo.  # noqa: E501
        :rtype: UnknownFieldSet
        """
        return self._unknown_fields

    @unknown_fields.setter
    def unknown_fields(self, unknown_fields):
        """Sets the unknown_fields of this PipelineStageInfo.


        :param unknown_fields: The unknown_fields of this PipelineStageInfo.  # noqa: E501
        :type: UnknownFieldSet
        """

        self._unknown_fields = unknown_fields

    @property
    def execution_id_bytes(self):
        """Gets the execution_id_bytes of this PipelineStageInfo.  # noqa: E501


        :return: The execution_id_bytes of this PipelineStageInfo.  # noqa: E501
        :rtype: ByteString
        """
        return self._execution_id_bytes

    @execution_id_bytes.setter
    def execution_id_bytes(self, execution_id_bytes):
        """Sets the execution_id_bytes of this PipelineStageInfo.


        :param execution_id_bytes: The execution_id_bytes of this PipelineStageInfo.  # noqa: E501
        :type: ByteString
        """

        self._execution_id_bytes = execution_id_bytes

    @property
    def stage_node_id_bytes(self):
        """Gets the stage_node_id_bytes of this PipelineStageInfo.  # noqa: E501


        :return: The stage_node_id_bytes of this PipelineStageInfo.  # noqa: E501
        :rtype: ByteString
        """
        return self._stage_node_id_bytes

    @stage_node_id_bytes.setter
    def stage_node_id_bytes(self, stage_node_id_bytes):
        """Sets the stage_node_id_bytes of this PipelineStageInfo.


        :param stage_node_id_bytes: The stage_node_id_bytes of this PipelineStageInfo.  # noqa: E501
        :type: ByteString
        """

        self._stage_node_id_bytes = stage_node_id_bytes

    @property
    def identifier(self):
        """Gets the identifier of this PipelineStageInfo.  # noqa: E501


        :return: The identifier of this PipelineStageInfo.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this PipelineStageInfo.


        :param identifier: The identifier of this PipelineStageInfo.  # noqa: E501
        :type: str
        """

        self._identifier = identifier

    @property
    def serialized_size(self):
        """Gets the serialized_size of this PipelineStageInfo.  # noqa: E501


        :return: The serialized_size of this PipelineStageInfo.  # noqa: E501
        :rtype: int
        """
        return self._serialized_size

    @serialized_size.setter
    def serialized_size(self, serialized_size):
        """Sets the serialized_size of this PipelineStageInfo.


        :param serialized_size: The serialized_size of this PipelineStageInfo.  # noqa: E501
        :type: int
        """

        self._serialized_size = serialized_size

    @property
    def parser_for_type(self):
        """Gets the parser_for_type of this PipelineStageInfo.  # noqa: E501


        :return: The parser_for_type of this PipelineStageInfo.  # noqa: E501
        :rtype: ParserPipelineStageInfo
        """
        return self._parser_for_type

    @parser_for_type.setter
    def parser_for_type(self, parser_for_type):
        """Sets the parser_for_type of this PipelineStageInfo.


        :param parser_for_type: The parser_for_type of this PipelineStageInfo.  # noqa: E501
        :type: ParserPipelineStageInfo
        """

        self._parser_for_type = parser_for_type

    @property
    def default_instance_for_type(self):
        """Gets the default_instance_for_type of this PipelineStageInfo.  # noqa: E501


        :return: The default_instance_for_type of this PipelineStageInfo.  # noqa: E501
        :rtype: PipelineStageInfo
        """
        return self._default_instance_for_type

    @default_instance_for_type.setter
    def default_instance_for_type(self, default_instance_for_type):
        """Sets the default_instance_for_type of this PipelineStageInfo.


        :param default_instance_for_type: The default_instance_for_type of this PipelineStageInfo.  # noqa: E501
        :type: PipelineStageInfo
        """

        self._default_instance_for_type = default_instance_for_type

    @property
    def identifier_bytes(self):
        """Gets the identifier_bytes of this PipelineStageInfo.  # noqa: E501


        :return: The identifier_bytes of this PipelineStageInfo.  # noqa: E501
        :rtype: ByteString
        """
        return self._identifier_bytes

    @identifier_bytes.setter
    def identifier_bytes(self, identifier_bytes):
        """Sets the identifier_bytes of this PipelineStageInfo.


        :param identifier_bytes: The identifier_bytes of this PipelineStageInfo.  # noqa: E501
        :type: ByteString
        """

        self._identifier_bytes = identifier_bytes

    @property
    def run_sequence(self):
        """Gets the run_sequence of this PipelineStageInfo.  # noqa: E501


        :return: The run_sequence of this PipelineStageInfo.  # noqa: E501
        :rtype: int
        """
        return self._run_sequence

    @run_sequence.setter
    def run_sequence(self, run_sequence):
        """Sets the run_sequence of this PipelineStageInfo.


        :param run_sequence: The run_sequence of this PipelineStageInfo.  # noqa: E501
        :type: int
        """

        self._run_sequence = run_sequence

    @property
    def org_id(self):
        """Gets the org_id of this PipelineStageInfo.  # noqa: E501


        :return: The org_id of this PipelineStageInfo.  # noqa: E501
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this PipelineStageInfo.


        :param org_id: The org_id of this PipelineStageInfo.  # noqa: E501
        :type: str
        """

        self._org_id = org_id

    @property
    def org_id_bytes(self):
        """Gets the org_id_bytes of this PipelineStageInfo.  # noqa: E501


        :return: The org_id_bytes of this PipelineStageInfo.  # noqa: E501
        :rtype: ByteString
        """
        return self._org_id_bytes

    @org_id_bytes.setter
    def org_id_bytes(self, org_id_bytes):
        """Sets the org_id_bytes of this PipelineStageInfo.


        :param org_id_bytes: The org_id_bytes of this PipelineStageInfo.  # noqa: E501
        :type: ByteString
        """

        self._org_id_bytes = org_id_bytes

    @property
    def project_id(self):
        """Gets the project_id of this PipelineStageInfo.  # noqa: E501


        :return: The project_id of this PipelineStageInfo.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this PipelineStageInfo.


        :param project_id: The project_id of this PipelineStageInfo.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def project_id_bytes(self):
        """Gets the project_id_bytes of this PipelineStageInfo.  # noqa: E501


        :return: The project_id_bytes of this PipelineStageInfo.  # noqa: E501
        :rtype: ByteString
        """
        return self._project_id_bytes

    @project_id_bytes.setter
    def project_id_bytes(self, project_id_bytes):
        """Sets the project_id_bytes of this PipelineStageInfo.


        :param project_id_bytes: The project_id_bytes of this PipelineStageInfo.  # noqa: E501
        :type: ByteString
        """

        self._project_id_bytes = project_id_bytes

    @property
    def has_parent_pipeline(self):
        """Gets the has_parent_pipeline of this PipelineStageInfo.  # noqa: E501


        :return: The has_parent_pipeline of this PipelineStageInfo.  # noqa: E501
        :rtype: bool
        """
        return self._has_parent_pipeline

    @has_parent_pipeline.setter
    def has_parent_pipeline(self, has_parent_pipeline):
        """Sets the has_parent_pipeline of this PipelineStageInfo.


        :param has_parent_pipeline: The has_parent_pipeline of this PipelineStageInfo.  # noqa: E501
        :type: bool
        """

        self._has_parent_pipeline = has_parent_pipeline

    @property
    def stage_node_id(self):
        """Gets the stage_node_id of this PipelineStageInfo.  # noqa: E501


        :return: The stage_node_id of this PipelineStageInfo.  # noqa: E501
        :rtype: str
        """
        return self._stage_node_id

    @stage_node_id.setter
    def stage_node_id(self, stage_node_id):
        """Sets the stage_node_id of this PipelineStageInfo.


        :param stage_node_id: The stage_node_id of this PipelineStageInfo.  # noqa: E501
        :type: str
        """

        self._stage_node_id = stage_node_id

    @property
    def execution_id(self):
        """Gets the execution_id of this PipelineStageInfo.  # noqa: E501


        :return: The execution_id of this PipelineStageInfo.  # noqa: E501
        :rtype: str
        """
        return self._execution_id

    @execution_id.setter
    def execution_id(self, execution_id):
        """Sets the execution_id of this PipelineStageInfo.


        :param execution_id: The execution_id of this PipelineStageInfo.  # noqa: E501
        :type: str
        """

        self._execution_id = execution_id

    @property
    def initialized(self):
        """Gets the initialized of this PipelineStageInfo.  # noqa: E501


        :return: The initialized of this PipelineStageInfo.  # noqa: E501
        :rtype: bool
        """
        return self._initialized

    @initialized.setter
    def initialized(self, initialized):
        """Sets the initialized of this PipelineStageInfo.


        :param initialized: The initialized of this PipelineStageInfo.  # noqa: E501
        :type: bool
        """

        self._initialized = initialized

    @property
    def all_fields(self):
        """Gets the all_fields of this PipelineStageInfo.  # noqa: E501


        :return: The all_fields of this PipelineStageInfo.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._all_fields

    @all_fields.setter
    def all_fields(self, all_fields):
        """Sets the all_fields of this PipelineStageInfo.


        :param all_fields: The all_fields of this PipelineStageInfo.  # noqa: E501
        :type: dict(str, object)
        """

        self._all_fields = all_fields

    @property
    def descriptor_for_type(self):
        """Gets the descriptor_for_type of this PipelineStageInfo.  # noqa: E501


        :return: The descriptor_for_type of this PipelineStageInfo.  # noqa: E501
        :rtype: Descriptor
        """
        return self._descriptor_for_type

    @descriptor_for_type.setter
    def descriptor_for_type(self, descriptor_for_type):
        """Sets the descriptor_for_type of this PipelineStageInfo.


        :param descriptor_for_type: The descriptor_for_type of this PipelineStageInfo.  # noqa: E501
        :type: Descriptor
        """

        self._descriptor_for_type = descriptor_for_type

    @property
    def initialization_error_string(self):
        """Gets the initialization_error_string of this PipelineStageInfo.  # noqa: E501


        :return: The initialization_error_string of this PipelineStageInfo.  # noqa: E501
        :rtype: str
        """
        return self._initialization_error_string

    @initialization_error_string.setter
    def initialization_error_string(self, initialization_error_string):
        """Sets the initialization_error_string of this PipelineStageInfo.


        :param initialization_error_string: The initialization_error_string of this PipelineStageInfo.  # noqa: E501
        :type: str
        """

        self._initialization_error_string = initialization_error_string

    @property
    def memoized_serialized_size(self):
        """Gets the memoized_serialized_size of this PipelineStageInfo.  # noqa: E501


        :return: The memoized_serialized_size of this PipelineStageInfo.  # noqa: E501
        :rtype: int
        """
        return self._memoized_serialized_size

    @memoized_serialized_size.setter
    def memoized_serialized_size(self, memoized_serialized_size):
        """Sets the memoized_serialized_size of this PipelineStageInfo.


        :param memoized_serialized_size: The memoized_serialized_size of this PipelineStageInfo.  # noqa: E501
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
        if issubclass(PipelineStageInfo, dict):
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
        if not isinstance(other, PipelineStageInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
