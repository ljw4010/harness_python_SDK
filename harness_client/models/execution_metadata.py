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

class ExecutionMetadata(object):
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
        'principal_info': 'ExecutionPrincipalInfo',
        'serialized_size': 'int',
        'parser_for_type': 'ParserExecutionMetadata',
        'default_instance_for_type': 'ExecutionMetadata',
        'run_sequence': 'int',
        'trigger_info': 'ExecutionTriggerInfo',
        'trigger_info_or_builder': 'ExecutionTriggerInfoOrBuilder',
        'pipeline_identifier': 'str',
        'pipeline_identifier_bytes': 'ByteString',
        'execution_uuid': 'str',
        'execution_uuid_bytes': 'ByteString',
        'principal_info_or_builder': 'ExecutionPrincipalInfoOrBuilder',
        'git_sync_branch_context': 'ByteString',
        'module_type': 'str',
        'module_type_bytes': 'ByteString',
        'retry_info': 'RetryExecutionInfo',
        'retry_info_or_builder': 'RetryExecutionInfoOrBuilder',
        'is_notification_configured': 'bool',
        'pipeline_store_type_value': 'int',
        'pipeline_store_type': 'str',
        'pipeline_connector_ref': 'str',
        'pipeline_connector_ref_bytes': 'ByteString',
        'pipeline_stage_info': 'PipelineStageInfo',
        'pipeline_stage_info_or_builder': 'PipelineStageInfoOrBuilder',
        'harness_version': 'str',
        'harness_version_bytes': 'ByteString',
        'is_debug': 'bool',
        'execution_mode_value': 'int',
        'execution_mode': 'str',
        'post_execution_rollback_info_list': 'list[PostExecutionRollbackInfo]',
        'post_execution_rollback_info_count': 'int',
        'post_execution_rollback_info_or_builder_list': 'list[PostExecutionRollbackInfoOrBuilder]',
        'original_plan_execution_id_for_rollback_mode': 'str',
        'original_plan_execution_id_for_rollback_mode_bytes': 'ByteString',
        'setting_to_value_map_count': 'int',
        'setting_to_value_map': 'dict(str, str)',
        'setting_to_value_map_map': 'dict(str, str)',
        'feature_flag_to_value_map_count': 'int',
        'feature_flag_to_value_map': 'dict(str, bool)',
        'feature_flag_to_value_map_map': 'dict(str, bool)',
        'processed_yaml_version': 'str',
        'processed_yaml_version_bytes': 'ByteString',
        'initialized': 'bool',
        'all_fields': 'dict(str, object)',
        'descriptor_for_type': 'Descriptor',
        'initialization_error_string': 'str',
        'memoized_serialized_size': 'int'
    }

    attribute_map = {
        'unknown_fields': 'unknownFields',
        'principal_info': 'principalInfo',
        'serialized_size': 'serializedSize',
        'parser_for_type': 'parserForType',
        'default_instance_for_type': 'defaultInstanceForType',
        'run_sequence': 'runSequence',
        'trigger_info': 'triggerInfo',
        'trigger_info_or_builder': 'triggerInfoOrBuilder',
        'pipeline_identifier': 'pipelineIdentifier',
        'pipeline_identifier_bytes': 'pipelineIdentifierBytes',
        'execution_uuid': 'executionUuid',
        'execution_uuid_bytes': 'executionUuidBytes',
        'principal_info_or_builder': 'principalInfoOrBuilder',
        'git_sync_branch_context': 'gitSyncBranchContext',
        'module_type': 'moduleType',
        'module_type_bytes': 'moduleTypeBytes',
        'retry_info': 'retryInfo',
        'retry_info_or_builder': 'retryInfoOrBuilder',
        'is_notification_configured': 'isNotificationConfigured',
        'pipeline_store_type_value': 'pipelineStoreTypeValue',
        'pipeline_store_type': 'pipelineStoreType',
        'pipeline_connector_ref': 'pipelineConnectorRef',
        'pipeline_connector_ref_bytes': 'pipelineConnectorRefBytes',
        'pipeline_stage_info': 'pipelineStageInfo',
        'pipeline_stage_info_or_builder': 'pipelineStageInfoOrBuilder',
        'harness_version': 'harnessVersion',
        'harness_version_bytes': 'harnessVersionBytes',
        'is_debug': 'isDebug',
        'execution_mode_value': 'executionModeValue',
        'execution_mode': 'executionMode',
        'post_execution_rollback_info_list': 'postExecutionRollbackInfoList',
        'post_execution_rollback_info_count': 'postExecutionRollbackInfoCount',
        'post_execution_rollback_info_or_builder_list': 'postExecutionRollbackInfoOrBuilderList',
        'original_plan_execution_id_for_rollback_mode': 'originalPlanExecutionIdForRollbackMode',
        'original_plan_execution_id_for_rollback_mode_bytes': 'originalPlanExecutionIdForRollbackModeBytes',
        'setting_to_value_map_count': 'settingToValueMapCount',
        'setting_to_value_map': 'settingToValueMap',
        'setting_to_value_map_map': 'settingToValueMapMap',
        'feature_flag_to_value_map_count': 'featureFlagToValueMapCount',
        'feature_flag_to_value_map': 'featureFlagToValueMap',
        'feature_flag_to_value_map_map': 'featureFlagToValueMapMap',
        'processed_yaml_version': 'processedYamlVersion',
        'processed_yaml_version_bytes': 'processedYamlVersionBytes',
        'initialized': 'initialized',
        'all_fields': 'allFields',
        'descriptor_for_type': 'descriptorForType',
        'initialization_error_string': 'initializationErrorString',
        'memoized_serialized_size': 'memoizedSerializedSize'
    }

    def __init__(self, unknown_fields=None, principal_info=None, serialized_size=None, parser_for_type=None, default_instance_for_type=None, run_sequence=None, trigger_info=None, trigger_info_or_builder=None, pipeline_identifier=None, pipeline_identifier_bytes=None, execution_uuid=None, execution_uuid_bytes=None, principal_info_or_builder=None, git_sync_branch_context=None, module_type=None, module_type_bytes=None, retry_info=None, retry_info_or_builder=None, is_notification_configured=None, pipeline_store_type_value=None, pipeline_store_type=None, pipeline_connector_ref=None, pipeline_connector_ref_bytes=None, pipeline_stage_info=None, pipeline_stage_info_or_builder=None, harness_version=None, harness_version_bytes=None, is_debug=None, execution_mode_value=None, execution_mode=None, post_execution_rollback_info_list=None, post_execution_rollback_info_count=None, post_execution_rollback_info_or_builder_list=None, original_plan_execution_id_for_rollback_mode=None, original_plan_execution_id_for_rollback_mode_bytes=None, setting_to_value_map_count=None, setting_to_value_map=None, setting_to_value_map_map=None, feature_flag_to_value_map_count=None, feature_flag_to_value_map=None, feature_flag_to_value_map_map=None, processed_yaml_version=None, processed_yaml_version_bytes=None, initialized=None, all_fields=None, descriptor_for_type=None, initialization_error_string=None, memoized_serialized_size=None):  # noqa: E501
        """ExecutionMetadata - a model defined in Swagger"""  # noqa: E501
        self._unknown_fields = None
        self._principal_info = None
        self._serialized_size = None
        self._parser_for_type = None
        self._default_instance_for_type = None
        self._run_sequence = None
        self._trigger_info = None
        self._trigger_info_or_builder = None
        self._pipeline_identifier = None
        self._pipeline_identifier_bytes = None
        self._execution_uuid = None
        self._execution_uuid_bytes = None
        self._principal_info_or_builder = None
        self._git_sync_branch_context = None
        self._module_type = None
        self._module_type_bytes = None
        self._retry_info = None
        self._retry_info_or_builder = None
        self._is_notification_configured = None
        self._pipeline_store_type_value = None
        self._pipeline_store_type = None
        self._pipeline_connector_ref = None
        self._pipeline_connector_ref_bytes = None
        self._pipeline_stage_info = None
        self._pipeline_stage_info_or_builder = None
        self._harness_version = None
        self._harness_version_bytes = None
        self._is_debug = None
        self._execution_mode_value = None
        self._execution_mode = None
        self._post_execution_rollback_info_list = None
        self._post_execution_rollback_info_count = None
        self._post_execution_rollback_info_or_builder_list = None
        self._original_plan_execution_id_for_rollback_mode = None
        self._original_plan_execution_id_for_rollback_mode_bytes = None
        self._setting_to_value_map_count = None
        self._setting_to_value_map = None
        self._setting_to_value_map_map = None
        self._feature_flag_to_value_map_count = None
        self._feature_flag_to_value_map = None
        self._feature_flag_to_value_map_map = None
        self._processed_yaml_version = None
        self._processed_yaml_version_bytes = None
        self._initialized = None
        self._all_fields = None
        self._descriptor_for_type = None
        self._initialization_error_string = None
        self._memoized_serialized_size = None
        self.discriminator = None
        if unknown_fields is not None:
            self.unknown_fields = unknown_fields
        if principal_info is not None:
            self.principal_info = principal_info
        if serialized_size is not None:
            self.serialized_size = serialized_size
        if parser_for_type is not None:
            self.parser_for_type = parser_for_type
        if default_instance_for_type is not None:
            self.default_instance_for_type = default_instance_for_type
        if run_sequence is not None:
            self.run_sequence = run_sequence
        if trigger_info is not None:
            self.trigger_info = trigger_info
        if trigger_info_or_builder is not None:
            self.trigger_info_or_builder = trigger_info_or_builder
        if pipeline_identifier is not None:
            self.pipeline_identifier = pipeline_identifier
        if pipeline_identifier_bytes is not None:
            self.pipeline_identifier_bytes = pipeline_identifier_bytes
        if execution_uuid is not None:
            self.execution_uuid = execution_uuid
        if execution_uuid_bytes is not None:
            self.execution_uuid_bytes = execution_uuid_bytes
        if principal_info_or_builder is not None:
            self.principal_info_or_builder = principal_info_or_builder
        if git_sync_branch_context is not None:
            self.git_sync_branch_context = git_sync_branch_context
        if module_type is not None:
            self.module_type = module_type
        if module_type_bytes is not None:
            self.module_type_bytes = module_type_bytes
        if retry_info is not None:
            self.retry_info = retry_info
        if retry_info_or_builder is not None:
            self.retry_info_or_builder = retry_info_or_builder
        if is_notification_configured is not None:
            self.is_notification_configured = is_notification_configured
        if pipeline_store_type_value is not None:
            self.pipeline_store_type_value = pipeline_store_type_value
        if pipeline_store_type is not None:
            self.pipeline_store_type = pipeline_store_type
        if pipeline_connector_ref is not None:
            self.pipeline_connector_ref = pipeline_connector_ref
        if pipeline_connector_ref_bytes is not None:
            self.pipeline_connector_ref_bytes = pipeline_connector_ref_bytes
        if pipeline_stage_info is not None:
            self.pipeline_stage_info = pipeline_stage_info
        if pipeline_stage_info_or_builder is not None:
            self.pipeline_stage_info_or_builder = pipeline_stage_info_or_builder
        if harness_version is not None:
            self.harness_version = harness_version
        if harness_version_bytes is not None:
            self.harness_version_bytes = harness_version_bytes
        if is_debug is not None:
            self.is_debug = is_debug
        if execution_mode_value is not None:
            self.execution_mode_value = execution_mode_value
        if execution_mode is not None:
            self.execution_mode = execution_mode
        if post_execution_rollback_info_list is not None:
            self.post_execution_rollback_info_list = post_execution_rollback_info_list
        if post_execution_rollback_info_count is not None:
            self.post_execution_rollback_info_count = post_execution_rollback_info_count
        if post_execution_rollback_info_or_builder_list is not None:
            self.post_execution_rollback_info_or_builder_list = post_execution_rollback_info_or_builder_list
        if original_plan_execution_id_for_rollback_mode is not None:
            self.original_plan_execution_id_for_rollback_mode = original_plan_execution_id_for_rollback_mode
        if original_plan_execution_id_for_rollback_mode_bytes is not None:
            self.original_plan_execution_id_for_rollback_mode_bytes = original_plan_execution_id_for_rollback_mode_bytes
        if setting_to_value_map_count is not None:
            self.setting_to_value_map_count = setting_to_value_map_count
        if setting_to_value_map is not None:
            self.setting_to_value_map = setting_to_value_map
        if setting_to_value_map_map is not None:
            self.setting_to_value_map_map = setting_to_value_map_map
        if feature_flag_to_value_map_count is not None:
            self.feature_flag_to_value_map_count = feature_flag_to_value_map_count
        if feature_flag_to_value_map is not None:
            self.feature_flag_to_value_map = feature_flag_to_value_map
        if feature_flag_to_value_map_map is not None:
            self.feature_flag_to_value_map_map = feature_flag_to_value_map_map
        if processed_yaml_version is not None:
            self.processed_yaml_version = processed_yaml_version
        if processed_yaml_version_bytes is not None:
            self.processed_yaml_version_bytes = processed_yaml_version_bytes
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
        """Gets the unknown_fields of this ExecutionMetadata.  # noqa: E501


        :return: The unknown_fields of this ExecutionMetadata.  # noqa: E501
        :rtype: UnknownFieldSet
        """
        return self._unknown_fields

    @unknown_fields.setter
    def unknown_fields(self, unknown_fields):
        """Sets the unknown_fields of this ExecutionMetadata.


        :param unknown_fields: The unknown_fields of this ExecutionMetadata.  # noqa: E501
        :type: UnknownFieldSet
        """

        self._unknown_fields = unknown_fields

    @property
    def principal_info(self):
        """Gets the principal_info of this ExecutionMetadata.  # noqa: E501


        :return: The principal_info of this ExecutionMetadata.  # noqa: E501
        :rtype: ExecutionPrincipalInfo
        """
        return self._principal_info

    @principal_info.setter
    def principal_info(self, principal_info):
        """Sets the principal_info of this ExecutionMetadata.


        :param principal_info: The principal_info of this ExecutionMetadata.  # noqa: E501
        :type: ExecutionPrincipalInfo
        """

        self._principal_info = principal_info

    @property
    def serialized_size(self):
        """Gets the serialized_size of this ExecutionMetadata.  # noqa: E501


        :return: The serialized_size of this ExecutionMetadata.  # noqa: E501
        :rtype: int
        """
        return self._serialized_size

    @serialized_size.setter
    def serialized_size(self, serialized_size):
        """Sets the serialized_size of this ExecutionMetadata.


        :param serialized_size: The serialized_size of this ExecutionMetadata.  # noqa: E501
        :type: int
        """

        self._serialized_size = serialized_size

    @property
    def parser_for_type(self):
        """Gets the parser_for_type of this ExecutionMetadata.  # noqa: E501


        :return: The parser_for_type of this ExecutionMetadata.  # noqa: E501
        :rtype: ParserExecutionMetadata
        """
        return self._parser_for_type

    @parser_for_type.setter
    def parser_for_type(self, parser_for_type):
        """Sets the parser_for_type of this ExecutionMetadata.


        :param parser_for_type: The parser_for_type of this ExecutionMetadata.  # noqa: E501
        :type: ParserExecutionMetadata
        """

        self._parser_for_type = parser_for_type

    @property
    def default_instance_for_type(self):
        """Gets the default_instance_for_type of this ExecutionMetadata.  # noqa: E501


        :return: The default_instance_for_type of this ExecutionMetadata.  # noqa: E501
        :rtype: ExecutionMetadata
        """
        return self._default_instance_for_type

    @default_instance_for_type.setter
    def default_instance_for_type(self, default_instance_for_type):
        """Sets the default_instance_for_type of this ExecutionMetadata.


        :param default_instance_for_type: The default_instance_for_type of this ExecutionMetadata.  # noqa: E501
        :type: ExecutionMetadata
        """

        self._default_instance_for_type = default_instance_for_type

    @property
    def run_sequence(self):
        """Gets the run_sequence of this ExecutionMetadata.  # noqa: E501


        :return: The run_sequence of this ExecutionMetadata.  # noqa: E501
        :rtype: int
        """
        return self._run_sequence

    @run_sequence.setter
    def run_sequence(self, run_sequence):
        """Sets the run_sequence of this ExecutionMetadata.


        :param run_sequence: The run_sequence of this ExecutionMetadata.  # noqa: E501
        :type: int
        """

        self._run_sequence = run_sequence

    @property
    def trigger_info(self):
        """Gets the trigger_info of this ExecutionMetadata.  # noqa: E501


        :return: The trigger_info of this ExecutionMetadata.  # noqa: E501
        :rtype: ExecutionTriggerInfo
        """
        return self._trigger_info

    @trigger_info.setter
    def trigger_info(self, trigger_info):
        """Sets the trigger_info of this ExecutionMetadata.


        :param trigger_info: The trigger_info of this ExecutionMetadata.  # noqa: E501
        :type: ExecutionTriggerInfo
        """

        self._trigger_info = trigger_info

    @property
    def trigger_info_or_builder(self):
        """Gets the trigger_info_or_builder of this ExecutionMetadata.  # noqa: E501


        :return: The trigger_info_or_builder of this ExecutionMetadata.  # noqa: E501
        :rtype: ExecutionTriggerInfoOrBuilder
        """
        return self._trigger_info_or_builder

    @trigger_info_or_builder.setter
    def trigger_info_or_builder(self, trigger_info_or_builder):
        """Sets the trigger_info_or_builder of this ExecutionMetadata.


        :param trigger_info_or_builder: The trigger_info_or_builder of this ExecutionMetadata.  # noqa: E501
        :type: ExecutionTriggerInfoOrBuilder
        """

        self._trigger_info_or_builder = trigger_info_or_builder

    @property
    def pipeline_identifier(self):
        """Gets the pipeline_identifier of this ExecutionMetadata.  # noqa: E501


        :return: The pipeline_identifier of this ExecutionMetadata.  # noqa: E501
        :rtype: str
        """
        return self._pipeline_identifier

    @pipeline_identifier.setter
    def pipeline_identifier(self, pipeline_identifier):
        """Sets the pipeline_identifier of this ExecutionMetadata.


        :param pipeline_identifier: The pipeline_identifier of this ExecutionMetadata.  # noqa: E501
        :type: str
        """

        self._pipeline_identifier = pipeline_identifier

    @property
    def pipeline_identifier_bytes(self):
        """Gets the pipeline_identifier_bytes of this ExecutionMetadata.  # noqa: E501


        :return: The pipeline_identifier_bytes of this ExecutionMetadata.  # noqa: E501
        :rtype: ByteString
        """
        return self._pipeline_identifier_bytes

    @pipeline_identifier_bytes.setter
    def pipeline_identifier_bytes(self, pipeline_identifier_bytes):
        """Sets the pipeline_identifier_bytes of this ExecutionMetadata.


        :param pipeline_identifier_bytes: The pipeline_identifier_bytes of this ExecutionMetadata.  # noqa: E501
        :type: ByteString
        """

        self._pipeline_identifier_bytes = pipeline_identifier_bytes

    @property
    def execution_uuid(self):
        """Gets the execution_uuid of this ExecutionMetadata.  # noqa: E501


        :return: The execution_uuid of this ExecutionMetadata.  # noqa: E501
        :rtype: str
        """
        return self._execution_uuid

    @execution_uuid.setter
    def execution_uuid(self, execution_uuid):
        """Sets the execution_uuid of this ExecutionMetadata.


        :param execution_uuid: The execution_uuid of this ExecutionMetadata.  # noqa: E501
        :type: str
        """

        self._execution_uuid = execution_uuid

    @property
    def execution_uuid_bytes(self):
        """Gets the execution_uuid_bytes of this ExecutionMetadata.  # noqa: E501


        :return: The execution_uuid_bytes of this ExecutionMetadata.  # noqa: E501
        :rtype: ByteString
        """
        return self._execution_uuid_bytes

    @execution_uuid_bytes.setter
    def execution_uuid_bytes(self, execution_uuid_bytes):
        """Sets the execution_uuid_bytes of this ExecutionMetadata.


        :param execution_uuid_bytes: The execution_uuid_bytes of this ExecutionMetadata.  # noqa: E501
        :type: ByteString
        """

        self._execution_uuid_bytes = execution_uuid_bytes

    @property
    def principal_info_or_builder(self):
        """Gets the principal_info_or_builder of this ExecutionMetadata.  # noqa: E501


        :return: The principal_info_or_builder of this ExecutionMetadata.  # noqa: E501
        :rtype: ExecutionPrincipalInfoOrBuilder
        """
        return self._principal_info_or_builder

    @principal_info_or_builder.setter
    def principal_info_or_builder(self, principal_info_or_builder):
        """Sets the principal_info_or_builder of this ExecutionMetadata.


        :param principal_info_or_builder: The principal_info_or_builder of this ExecutionMetadata.  # noqa: E501
        :type: ExecutionPrincipalInfoOrBuilder
        """

        self._principal_info_or_builder = principal_info_or_builder

    @property
    def git_sync_branch_context(self):
        """Gets the git_sync_branch_context of this ExecutionMetadata.  # noqa: E501


        :return: The git_sync_branch_context of this ExecutionMetadata.  # noqa: E501
        :rtype: ByteString
        """
        return self._git_sync_branch_context

    @git_sync_branch_context.setter
    def git_sync_branch_context(self, git_sync_branch_context):
        """Sets the git_sync_branch_context of this ExecutionMetadata.


        :param git_sync_branch_context: The git_sync_branch_context of this ExecutionMetadata.  # noqa: E501
        :type: ByteString
        """

        self._git_sync_branch_context = git_sync_branch_context

    @property
    def module_type(self):
        """Gets the module_type of this ExecutionMetadata.  # noqa: E501


        :return: The module_type of this ExecutionMetadata.  # noqa: E501
        :rtype: str
        """
        return self._module_type

    @module_type.setter
    def module_type(self, module_type):
        """Sets the module_type of this ExecutionMetadata.


        :param module_type: The module_type of this ExecutionMetadata.  # noqa: E501
        :type: str
        """

        self._module_type = module_type

    @property
    def module_type_bytes(self):
        """Gets the module_type_bytes of this ExecutionMetadata.  # noqa: E501


        :return: The module_type_bytes of this ExecutionMetadata.  # noqa: E501
        :rtype: ByteString
        """
        return self._module_type_bytes

    @module_type_bytes.setter
    def module_type_bytes(self, module_type_bytes):
        """Sets the module_type_bytes of this ExecutionMetadata.


        :param module_type_bytes: The module_type_bytes of this ExecutionMetadata.  # noqa: E501
        :type: ByteString
        """

        self._module_type_bytes = module_type_bytes

    @property
    def retry_info(self):
        """Gets the retry_info of this ExecutionMetadata.  # noqa: E501


        :return: The retry_info of this ExecutionMetadata.  # noqa: E501
        :rtype: RetryExecutionInfo
        """
        return self._retry_info

    @retry_info.setter
    def retry_info(self, retry_info):
        """Sets the retry_info of this ExecutionMetadata.


        :param retry_info: The retry_info of this ExecutionMetadata.  # noqa: E501
        :type: RetryExecutionInfo
        """

        self._retry_info = retry_info

    @property
    def retry_info_or_builder(self):
        """Gets the retry_info_or_builder of this ExecutionMetadata.  # noqa: E501


        :return: The retry_info_or_builder of this ExecutionMetadata.  # noqa: E501
        :rtype: RetryExecutionInfoOrBuilder
        """
        return self._retry_info_or_builder

    @retry_info_or_builder.setter
    def retry_info_or_builder(self, retry_info_or_builder):
        """Sets the retry_info_or_builder of this ExecutionMetadata.


        :param retry_info_or_builder: The retry_info_or_builder of this ExecutionMetadata.  # noqa: E501
        :type: RetryExecutionInfoOrBuilder
        """

        self._retry_info_or_builder = retry_info_or_builder

    @property
    def is_notification_configured(self):
        """Gets the is_notification_configured of this ExecutionMetadata.  # noqa: E501


        :return: The is_notification_configured of this ExecutionMetadata.  # noqa: E501
        :rtype: bool
        """
        return self._is_notification_configured

    @is_notification_configured.setter
    def is_notification_configured(self, is_notification_configured):
        """Sets the is_notification_configured of this ExecutionMetadata.


        :param is_notification_configured: The is_notification_configured of this ExecutionMetadata.  # noqa: E501
        :type: bool
        """

        self._is_notification_configured = is_notification_configured

    @property
    def pipeline_store_type_value(self):
        """Gets the pipeline_store_type_value of this ExecutionMetadata.  # noqa: E501


        :return: The pipeline_store_type_value of this ExecutionMetadata.  # noqa: E501
        :rtype: int
        """
        return self._pipeline_store_type_value

    @pipeline_store_type_value.setter
    def pipeline_store_type_value(self, pipeline_store_type_value):
        """Sets the pipeline_store_type_value of this ExecutionMetadata.


        :param pipeline_store_type_value: The pipeline_store_type_value of this ExecutionMetadata.  # noqa: E501
        :type: int
        """

        self._pipeline_store_type_value = pipeline_store_type_value

    @property
    def pipeline_store_type(self):
        """Gets the pipeline_store_type of this ExecutionMetadata.  # noqa: E501


        :return: The pipeline_store_type of this ExecutionMetadata.  # noqa: E501
        :rtype: str
        """
        return self._pipeline_store_type

    @pipeline_store_type.setter
    def pipeline_store_type(self, pipeline_store_type):
        """Sets the pipeline_store_type of this ExecutionMetadata.


        :param pipeline_store_type: The pipeline_store_type of this ExecutionMetadata.  # noqa: E501
        :type: str
        """
        allowed_values = ["UNDEFINED", "INLINE", "REMOTE", "UNRECOGNIZED"]  # noqa: E501
        if pipeline_store_type not in allowed_values:
            raise ValueError(
                "Invalid value for `pipeline_store_type` ({0}), must be one of {1}"  # noqa: E501
                .format(pipeline_store_type, allowed_values)
            )

        self._pipeline_store_type = pipeline_store_type

    @property
    def pipeline_connector_ref(self):
        """Gets the pipeline_connector_ref of this ExecutionMetadata.  # noqa: E501


        :return: The pipeline_connector_ref of this ExecutionMetadata.  # noqa: E501
        :rtype: str
        """
        return self._pipeline_connector_ref

    @pipeline_connector_ref.setter
    def pipeline_connector_ref(self, pipeline_connector_ref):
        """Sets the pipeline_connector_ref of this ExecutionMetadata.


        :param pipeline_connector_ref: The pipeline_connector_ref of this ExecutionMetadata.  # noqa: E501
        :type: str
        """

        self._pipeline_connector_ref = pipeline_connector_ref

    @property
    def pipeline_connector_ref_bytes(self):
        """Gets the pipeline_connector_ref_bytes of this ExecutionMetadata.  # noqa: E501


        :return: The pipeline_connector_ref_bytes of this ExecutionMetadata.  # noqa: E501
        :rtype: ByteString
        """
        return self._pipeline_connector_ref_bytes

    @pipeline_connector_ref_bytes.setter
    def pipeline_connector_ref_bytes(self, pipeline_connector_ref_bytes):
        """Sets the pipeline_connector_ref_bytes of this ExecutionMetadata.


        :param pipeline_connector_ref_bytes: The pipeline_connector_ref_bytes of this ExecutionMetadata.  # noqa: E501
        :type: ByteString
        """

        self._pipeline_connector_ref_bytes = pipeline_connector_ref_bytes

    @property
    def pipeline_stage_info(self):
        """Gets the pipeline_stage_info of this ExecutionMetadata.  # noqa: E501


        :return: The pipeline_stage_info of this ExecutionMetadata.  # noqa: E501
        :rtype: PipelineStageInfo
        """
        return self._pipeline_stage_info

    @pipeline_stage_info.setter
    def pipeline_stage_info(self, pipeline_stage_info):
        """Sets the pipeline_stage_info of this ExecutionMetadata.


        :param pipeline_stage_info: The pipeline_stage_info of this ExecutionMetadata.  # noqa: E501
        :type: PipelineStageInfo
        """

        self._pipeline_stage_info = pipeline_stage_info

    @property
    def pipeline_stage_info_or_builder(self):
        """Gets the pipeline_stage_info_or_builder of this ExecutionMetadata.  # noqa: E501


        :return: The pipeline_stage_info_or_builder of this ExecutionMetadata.  # noqa: E501
        :rtype: PipelineStageInfoOrBuilder
        """
        return self._pipeline_stage_info_or_builder

    @pipeline_stage_info_or_builder.setter
    def pipeline_stage_info_or_builder(self, pipeline_stage_info_or_builder):
        """Sets the pipeline_stage_info_or_builder of this ExecutionMetadata.


        :param pipeline_stage_info_or_builder: The pipeline_stage_info_or_builder of this ExecutionMetadata.  # noqa: E501
        :type: PipelineStageInfoOrBuilder
        """

        self._pipeline_stage_info_or_builder = pipeline_stage_info_or_builder

    @property
    def harness_version(self):
        """Gets the harness_version of this ExecutionMetadata.  # noqa: E501


        :return: The harness_version of this ExecutionMetadata.  # noqa: E501
        :rtype: str
        """
        return self._harness_version

    @harness_version.setter
    def harness_version(self, harness_version):
        """Sets the harness_version of this ExecutionMetadata.


        :param harness_version: The harness_version of this ExecutionMetadata.  # noqa: E501
        :type: str
        """

        self._harness_version = harness_version

    @property
    def harness_version_bytes(self):
        """Gets the harness_version_bytes of this ExecutionMetadata.  # noqa: E501


        :return: The harness_version_bytes of this ExecutionMetadata.  # noqa: E501
        :rtype: ByteString
        """
        return self._harness_version_bytes

    @harness_version_bytes.setter
    def harness_version_bytes(self, harness_version_bytes):
        """Sets the harness_version_bytes of this ExecutionMetadata.


        :param harness_version_bytes: The harness_version_bytes of this ExecutionMetadata.  # noqa: E501
        :type: ByteString
        """

        self._harness_version_bytes = harness_version_bytes

    @property
    def is_debug(self):
        """Gets the is_debug of this ExecutionMetadata.  # noqa: E501


        :return: The is_debug of this ExecutionMetadata.  # noqa: E501
        :rtype: bool
        """
        return self._is_debug

    @is_debug.setter
    def is_debug(self, is_debug):
        """Sets the is_debug of this ExecutionMetadata.


        :param is_debug: The is_debug of this ExecutionMetadata.  # noqa: E501
        :type: bool
        """

        self._is_debug = is_debug

    @property
    def execution_mode_value(self):
        """Gets the execution_mode_value of this ExecutionMetadata.  # noqa: E501


        :return: The execution_mode_value of this ExecutionMetadata.  # noqa: E501
        :rtype: int
        """
        return self._execution_mode_value

    @execution_mode_value.setter
    def execution_mode_value(self, execution_mode_value):
        """Sets the execution_mode_value of this ExecutionMetadata.


        :param execution_mode_value: The execution_mode_value of this ExecutionMetadata.  # noqa: E501
        :type: int
        """

        self._execution_mode_value = execution_mode_value

    @property
    def execution_mode(self):
        """Gets the execution_mode of this ExecutionMetadata.  # noqa: E501


        :return: The execution_mode of this ExecutionMetadata.  # noqa: E501
        :rtype: str
        """
        return self._execution_mode

    @execution_mode.setter
    def execution_mode(self, execution_mode):
        """Sets the execution_mode of this ExecutionMetadata.


        :param execution_mode: The execution_mode of this ExecutionMetadata.  # noqa: E501
        :type: str
        """
        allowed_values = ["UNDEFINED_MODE", "NORMAL", "POST_EXECUTION_ROLLBACK", "PIPELINE_ROLLBACK", "UNRECOGNIZED"]  # noqa: E501
        if execution_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `execution_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(execution_mode, allowed_values)
            )

        self._execution_mode = execution_mode

    @property
    def post_execution_rollback_info_list(self):
        """Gets the post_execution_rollback_info_list of this ExecutionMetadata.  # noqa: E501


        :return: The post_execution_rollback_info_list of this ExecutionMetadata.  # noqa: E501
        :rtype: list[PostExecutionRollbackInfo]
        """
        return self._post_execution_rollback_info_list

    @post_execution_rollback_info_list.setter
    def post_execution_rollback_info_list(self, post_execution_rollback_info_list):
        """Sets the post_execution_rollback_info_list of this ExecutionMetadata.


        :param post_execution_rollback_info_list: The post_execution_rollback_info_list of this ExecutionMetadata.  # noqa: E501
        :type: list[PostExecutionRollbackInfo]
        """

        self._post_execution_rollback_info_list = post_execution_rollback_info_list

    @property
    def post_execution_rollback_info_count(self):
        """Gets the post_execution_rollback_info_count of this ExecutionMetadata.  # noqa: E501


        :return: The post_execution_rollback_info_count of this ExecutionMetadata.  # noqa: E501
        :rtype: int
        """
        return self._post_execution_rollback_info_count

    @post_execution_rollback_info_count.setter
    def post_execution_rollback_info_count(self, post_execution_rollback_info_count):
        """Sets the post_execution_rollback_info_count of this ExecutionMetadata.


        :param post_execution_rollback_info_count: The post_execution_rollback_info_count of this ExecutionMetadata.  # noqa: E501
        :type: int
        """

        self._post_execution_rollback_info_count = post_execution_rollback_info_count

    @property
    def post_execution_rollback_info_or_builder_list(self):
        """Gets the post_execution_rollback_info_or_builder_list of this ExecutionMetadata.  # noqa: E501


        :return: The post_execution_rollback_info_or_builder_list of this ExecutionMetadata.  # noqa: E501
        :rtype: list[PostExecutionRollbackInfoOrBuilder]
        """
        return self._post_execution_rollback_info_or_builder_list

    @post_execution_rollback_info_or_builder_list.setter
    def post_execution_rollback_info_or_builder_list(self, post_execution_rollback_info_or_builder_list):
        """Sets the post_execution_rollback_info_or_builder_list of this ExecutionMetadata.


        :param post_execution_rollback_info_or_builder_list: The post_execution_rollback_info_or_builder_list of this ExecutionMetadata.  # noqa: E501
        :type: list[PostExecutionRollbackInfoOrBuilder]
        """

        self._post_execution_rollback_info_or_builder_list = post_execution_rollback_info_or_builder_list

    @property
    def original_plan_execution_id_for_rollback_mode(self):
        """Gets the original_plan_execution_id_for_rollback_mode of this ExecutionMetadata.  # noqa: E501


        :return: The original_plan_execution_id_for_rollback_mode of this ExecutionMetadata.  # noqa: E501
        :rtype: str
        """
        return self._original_plan_execution_id_for_rollback_mode

    @original_plan_execution_id_for_rollback_mode.setter
    def original_plan_execution_id_for_rollback_mode(self, original_plan_execution_id_for_rollback_mode):
        """Sets the original_plan_execution_id_for_rollback_mode of this ExecutionMetadata.


        :param original_plan_execution_id_for_rollback_mode: The original_plan_execution_id_for_rollback_mode of this ExecutionMetadata.  # noqa: E501
        :type: str
        """

        self._original_plan_execution_id_for_rollback_mode = original_plan_execution_id_for_rollback_mode

    @property
    def original_plan_execution_id_for_rollback_mode_bytes(self):
        """Gets the original_plan_execution_id_for_rollback_mode_bytes of this ExecutionMetadata.  # noqa: E501


        :return: The original_plan_execution_id_for_rollback_mode_bytes of this ExecutionMetadata.  # noqa: E501
        :rtype: ByteString
        """
        return self._original_plan_execution_id_for_rollback_mode_bytes

    @original_plan_execution_id_for_rollback_mode_bytes.setter
    def original_plan_execution_id_for_rollback_mode_bytes(self, original_plan_execution_id_for_rollback_mode_bytes):
        """Sets the original_plan_execution_id_for_rollback_mode_bytes of this ExecutionMetadata.


        :param original_plan_execution_id_for_rollback_mode_bytes: The original_plan_execution_id_for_rollback_mode_bytes of this ExecutionMetadata.  # noqa: E501
        :type: ByteString
        """

        self._original_plan_execution_id_for_rollback_mode_bytes = original_plan_execution_id_for_rollback_mode_bytes

    @property
    def setting_to_value_map_count(self):
        """Gets the setting_to_value_map_count of this ExecutionMetadata.  # noqa: E501


        :return: The setting_to_value_map_count of this ExecutionMetadata.  # noqa: E501
        :rtype: int
        """
        return self._setting_to_value_map_count

    @setting_to_value_map_count.setter
    def setting_to_value_map_count(self, setting_to_value_map_count):
        """Sets the setting_to_value_map_count of this ExecutionMetadata.


        :param setting_to_value_map_count: The setting_to_value_map_count of this ExecutionMetadata.  # noqa: E501
        :type: int
        """

        self._setting_to_value_map_count = setting_to_value_map_count

    @property
    def setting_to_value_map(self):
        """Gets the setting_to_value_map of this ExecutionMetadata.  # noqa: E501


        :return: The setting_to_value_map of this ExecutionMetadata.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._setting_to_value_map

    @setting_to_value_map.setter
    def setting_to_value_map(self, setting_to_value_map):
        """Sets the setting_to_value_map of this ExecutionMetadata.


        :param setting_to_value_map: The setting_to_value_map of this ExecutionMetadata.  # noqa: E501
        :type: dict(str, str)
        """

        self._setting_to_value_map = setting_to_value_map

    @property
    def setting_to_value_map_map(self):
        """Gets the setting_to_value_map_map of this ExecutionMetadata.  # noqa: E501


        :return: The setting_to_value_map_map of this ExecutionMetadata.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._setting_to_value_map_map

    @setting_to_value_map_map.setter
    def setting_to_value_map_map(self, setting_to_value_map_map):
        """Sets the setting_to_value_map_map of this ExecutionMetadata.


        :param setting_to_value_map_map: The setting_to_value_map_map of this ExecutionMetadata.  # noqa: E501
        :type: dict(str, str)
        """

        self._setting_to_value_map_map = setting_to_value_map_map

    @property
    def feature_flag_to_value_map_count(self):
        """Gets the feature_flag_to_value_map_count of this ExecutionMetadata.  # noqa: E501


        :return: The feature_flag_to_value_map_count of this ExecutionMetadata.  # noqa: E501
        :rtype: int
        """
        return self._feature_flag_to_value_map_count

    @feature_flag_to_value_map_count.setter
    def feature_flag_to_value_map_count(self, feature_flag_to_value_map_count):
        """Sets the feature_flag_to_value_map_count of this ExecutionMetadata.


        :param feature_flag_to_value_map_count: The feature_flag_to_value_map_count of this ExecutionMetadata.  # noqa: E501
        :type: int
        """

        self._feature_flag_to_value_map_count = feature_flag_to_value_map_count

    @property
    def feature_flag_to_value_map(self):
        """Gets the feature_flag_to_value_map of this ExecutionMetadata.  # noqa: E501


        :return: The feature_flag_to_value_map of this ExecutionMetadata.  # noqa: E501
        :rtype: dict(str, bool)
        """
        return self._feature_flag_to_value_map

    @feature_flag_to_value_map.setter
    def feature_flag_to_value_map(self, feature_flag_to_value_map):
        """Sets the feature_flag_to_value_map of this ExecutionMetadata.


        :param feature_flag_to_value_map: The feature_flag_to_value_map of this ExecutionMetadata.  # noqa: E501
        :type: dict(str, bool)
        """

        self._feature_flag_to_value_map = feature_flag_to_value_map

    @property
    def feature_flag_to_value_map_map(self):
        """Gets the feature_flag_to_value_map_map of this ExecutionMetadata.  # noqa: E501


        :return: The feature_flag_to_value_map_map of this ExecutionMetadata.  # noqa: E501
        :rtype: dict(str, bool)
        """
        return self._feature_flag_to_value_map_map

    @feature_flag_to_value_map_map.setter
    def feature_flag_to_value_map_map(self, feature_flag_to_value_map_map):
        """Sets the feature_flag_to_value_map_map of this ExecutionMetadata.


        :param feature_flag_to_value_map_map: The feature_flag_to_value_map_map of this ExecutionMetadata.  # noqa: E501
        :type: dict(str, bool)
        """

        self._feature_flag_to_value_map_map = feature_flag_to_value_map_map

    @property
    def processed_yaml_version(self):
        """Gets the processed_yaml_version of this ExecutionMetadata.  # noqa: E501


        :return: The processed_yaml_version of this ExecutionMetadata.  # noqa: E501
        :rtype: str
        """
        return self._processed_yaml_version

    @processed_yaml_version.setter
    def processed_yaml_version(self, processed_yaml_version):
        """Sets the processed_yaml_version of this ExecutionMetadata.


        :param processed_yaml_version: The processed_yaml_version of this ExecutionMetadata.  # noqa: E501
        :type: str
        """

        self._processed_yaml_version = processed_yaml_version

    @property
    def processed_yaml_version_bytes(self):
        """Gets the processed_yaml_version_bytes of this ExecutionMetadata.  # noqa: E501


        :return: The processed_yaml_version_bytes of this ExecutionMetadata.  # noqa: E501
        :rtype: ByteString
        """
        return self._processed_yaml_version_bytes

    @processed_yaml_version_bytes.setter
    def processed_yaml_version_bytes(self, processed_yaml_version_bytes):
        """Sets the processed_yaml_version_bytes of this ExecutionMetadata.


        :param processed_yaml_version_bytes: The processed_yaml_version_bytes of this ExecutionMetadata.  # noqa: E501
        :type: ByteString
        """

        self._processed_yaml_version_bytes = processed_yaml_version_bytes

    @property
    def initialized(self):
        """Gets the initialized of this ExecutionMetadata.  # noqa: E501


        :return: The initialized of this ExecutionMetadata.  # noqa: E501
        :rtype: bool
        """
        return self._initialized

    @initialized.setter
    def initialized(self, initialized):
        """Sets the initialized of this ExecutionMetadata.


        :param initialized: The initialized of this ExecutionMetadata.  # noqa: E501
        :type: bool
        """

        self._initialized = initialized

    @property
    def all_fields(self):
        """Gets the all_fields of this ExecutionMetadata.  # noqa: E501


        :return: The all_fields of this ExecutionMetadata.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._all_fields

    @all_fields.setter
    def all_fields(self, all_fields):
        """Sets the all_fields of this ExecutionMetadata.


        :param all_fields: The all_fields of this ExecutionMetadata.  # noqa: E501
        :type: dict(str, object)
        """

        self._all_fields = all_fields

    @property
    def descriptor_for_type(self):
        """Gets the descriptor_for_type of this ExecutionMetadata.  # noqa: E501


        :return: The descriptor_for_type of this ExecutionMetadata.  # noqa: E501
        :rtype: Descriptor
        """
        return self._descriptor_for_type

    @descriptor_for_type.setter
    def descriptor_for_type(self, descriptor_for_type):
        """Sets the descriptor_for_type of this ExecutionMetadata.


        :param descriptor_for_type: The descriptor_for_type of this ExecutionMetadata.  # noqa: E501
        :type: Descriptor
        """

        self._descriptor_for_type = descriptor_for_type

    @property
    def initialization_error_string(self):
        """Gets the initialization_error_string of this ExecutionMetadata.  # noqa: E501


        :return: The initialization_error_string of this ExecutionMetadata.  # noqa: E501
        :rtype: str
        """
        return self._initialization_error_string

    @initialization_error_string.setter
    def initialization_error_string(self, initialization_error_string):
        """Sets the initialization_error_string of this ExecutionMetadata.


        :param initialization_error_string: The initialization_error_string of this ExecutionMetadata.  # noqa: E501
        :type: str
        """

        self._initialization_error_string = initialization_error_string

    @property
    def memoized_serialized_size(self):
        """Gets the memoized_serialized_size of this ExecutionMetadata.  # noqa: E501


        :return: The memoized_serialized_size of this ExecutionMetadata.  # noqa: E501
        :rtype: int
        """
        return self._memoized_serialized_size

    @memoized_serialized_size.setter
    def memoized_serialized_size(self, memoized_serialized_size):
        """Sets the memoized_serialized_size of this ExecutionMetadata.


        :param memoized_serialized_size: The memoized_serialized_size of this ExecutionMetadata.  # noqa: E501
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
        if issubclass(ExecutionMetadata, dict):
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
        if not isinstance(other, ExecutionMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
