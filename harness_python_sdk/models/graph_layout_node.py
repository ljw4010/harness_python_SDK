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

class GraphLayoutNode(object):
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
        'node_type': 'str',
        'node_group': 'str',
        'node_identifier': 'str',
        'name': 'str',
        'node_uuid': 'str',
        'status': 'str',
        'module': 'str',
        'module_info': 'dict(str, dict(str, object))',
        'start_ts': 'int',
        'end_ts': 'int',
        'edge_layout_list': 'EdgeLayoutList',
        'skip_info': 'SkipInfo',
        'node_run_info': 'NodeRunInfo',
        'barrier_found': 'bool',
        'failure_info': 'ExecutionErrorInfo',
        'failure_info_dto': 'FailureInfoDTO',
        'step_details': 'dict(str, PmsStepDetails)',
        'hidden': 'bool',
        'node_execution_id': 'str',
        'strategy_metadata': 'StrategyMetadata',
        'execution_input_configured': 'bool',
        'is_rollback_stage_node': 'bool'
    }

    attribute_map = {
        'node_type': 'nodeType',
        'node_group': 'nodeGroup',
        'node_identifier': 'nodeIdentifier',
        'name': 'name',
        'node_uuid': 'nodeUuid',
        'status': 'status',
        'module': 'module',
        'module_info': 'moduleInfo',
        'start_ts': 'startTs',
        'end_ts': 'endTs',
        'edge_layout_list': 'edgeLayoutList',
        'skip_info': 'skipInfo',
        'node_run_info': 'nodeRunInfo',
        'barrier_found': 'barrierFound',
        'failure_info': 'failureInfo',
        'failure_info_dto': 'failureInfoDTO',
        'step_details': 'stepDetails',
        'hidden': 'hidden',
        'node_execution_id': 'nodeExecutionId',
        'strategy_metadata': 'strategyMetadata',
        'execution_input_configured': 'executionInputConfigured',
        'is_rollback_stage_node': 'isRollbackStageNode'
    }

    def __init__(self, node_type=None, node_group=None, node_identifier=None, name=None, node_uuid=None, status=None, module=None, module_info=None, start_ts=None, end_ts=None, edge_layout_list=None, skip_info=None, node_run_info=None, barrier_found=None, failure_info=None, failure_info_dto=None, step_details=None, hidden=None, node_execution_id=None, strategy_metadata=None, execution_input_configured=None, is_rollback_stage_node=None):  # noqa: E501
        """GraphLayoutNode - a model defined in Swagger"""  # noqa: E501
        self._node_type = None
        self._node_group = None
        self._node_identifier = None
        self._name = None
        self._node_uuid = None
        self._status = None
        self._module = None
        self._module_info = None
        self._start_ts = None
        self._end_ts = None
        self._edge_layout_list = None
        self._skip_info = None
        self._node_run_info = None
        self._barrier_found = None
        self._failure_info = None
        self._failure_info_dto = None
        self._step_details = None
        self._hidden = None
        self._node_execution_id = None
        self._strategy_metadata = None
        self._execution_input_configured = None
        self._is_rollback_stage_node = None
        self.discriminator = None
        if node_type is not None:
            self.node_type = node_type
        if node_group is not None:
            self.node_group = node_group
        if node_identifier is not None:
            self.node_identifier = node_identifier
        if name is not None:
            self.name = name
        if node_uuid is not None:
            self.node_uuid = node_uuid
        if status is not None:
            self.status = status
        if module is not None:
            self.module = module
        if module_info is not None:
            self.module_info = module_info
        if start_ts is not None:
            self.start_ts = start_ts
        if end_ts is not None:
            self.end_ts = end_ts
        if edge_layout_list is not None:
            self.edge_layout_list = edge_layout_list
        if skip_info is not None:
            self.skip_info = skip_info
        if node_run_info is not None:
            self.node_run_info = node_run_info
        if barrier_found is not None:
            self.barrier_found = barrier_found
        if failure_info is not None:
            self.failure_info = failure_info
        if failure_info_dto is not None:
            self.failure_info_dto = failure_info_dto
        if step_details is not None:
            self.step_details = step_details
        if hidden is not None:
            self.hidden = hidden
        if node_execution_id is not None:
            self.node_execution_id = node_execution_id
        if strategy_metadata is not None:
            self.strategy_metadata = strategy_metadata
        if execution_input_configured is not None:
            self.execution_input_configured = execution_input_configured
        if is_rollback_stage_node is not None:
            self.is_rollback_stage_node = is_rollback_stage_node

    @property
    def node_type(self):
        """Gets the node_type of this GraphLayoutNode.  # noqa: E501


        :return: The node_type of this GraphLayoutNode.  # noqa: E501
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        """Sets the node_type of this GraphLayoutNode.


        :param node_type: The node_type of this GraphLayoutNode.  # noqa: E501
        :type: str
        """

        self._node_type = node_type

    @property
    def node_group(self):
        """Gets the node_group of this GraphLayoutNode.  # noqa: E501


        :return: The node_group of this GraphLayoutNode.  # noqa: E501
        :rtype: str
        """
        return self._node_group

    @node_group.setter
    def node_group(self, node_group):
        """Sets the node_group of this GraphLayoutNode.


        :param node_group: The node_group of this GraphLayoutNode.  # noqa: E501
        :type: str
        """

        self._node_group = node_group

    @property
    def node_identifier(self):
        """Gets the node_identifier of this GraphLayoutNode.  # noqa: E501


        :return: The node_identifier of this GraphLayoutNode.  # noqa: E501
        :rtype: str
        """
        return self._node_identifier

    @node_identifier.setter
    def node_identifier(self, node_identifier):
        """Sets the node_identifier of this GraphLayoutNode.


        :param node_identifier: The node_identifier of this GraphLayoutNode.  # noqa: E501
        :type: str
        """

        self._node_identifier = node_identifier

    @property
    def name(self):
        """Gets the name of this GraphLayoutNode.  # noqa: E501


        :return: The name of this GraphLayoutNode.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GraphLayoutNode.


        :param name: The name of this GraphLayoutNode.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def node_uuid(self):
        """Gets the node_uuid of this GraphLayoutNode.  # noqa: E501


        :return: The node_uuid of this GraphLayoutNode.  # noqa: E501
        :rtype: str
        """
        return self._node_uuid

    @node_uuid.setter
    def node_uuid(self, node_uuid):
        """Sets the node_uuid of this GraphLayoutNode.


        :param node_uuid: The node_uuid of this GraphLayoutNode.  # noqa: E501
        :type: str
        """

        self._node_uuid = node_uuid

    @property
    def status(self):
        """Gets the status of this GraphLayoutNode.  # noqa: E501

        This is the Execution Status of the entity  # noqa: E501

        :return: The status of this GraphLayoutNode.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GraphLayoutNode.

        This is the Execution Status of the entity  # noqa: E501

        :param status: The status of this GraphLayoutNode.  # noqa: E501
        :type: str
        """
        allowed_values = ["Running", "AsyncWaiting", "TaskWaiting", "TimedWaiting", "Failed", "Errored", "IgnoreFailed", "NotStarted", "Expired", "Aborted", "Discontinuing", "Queued", "Paused", "ResourceWaiting", "InterventionWaiting", "ApprovalWaiting", "WaitStepRunning", "QueuedLicenseLimitReached", "QueuedExecutionConcurrencyReached", "Success", "Suspended", "Skipped", "Pausing", "ApprovalRejected", "InputWaiting", "AbortedByFreeze", "NOT_STARTED", "INTERVENTION_WAITING", "APPROVAL_WAITING", "APPROVAL_REJECTED", "Waiting"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def module(self):
        """Gets the module of this GraphLayoutNode.  # noqa: E501


        :return: The module of this GraphLayoutNode.  # noqa: E501
        :rtype: str
        """
        return self._module

    @module.setter
    def module(self, module):
        """Sets the module of this GraphLayoutNode.


        :param module: The module of this GraphLayoutNode.  # noqa: E501
        :type: str
        """

        self._module = module

    @property
    def module_info(self):
        """Gets the module_info of this GraphLayoutNode.  # noqa: E501


        :return: The module_info of this GraphLayoutNode.  # noqa: E501
        :rtype: dict(str, dict(str, object))
        """
        return self._module_info

    @module_info.setter
    def module_info(self, module_info):
        """Sets the module_info of this GraphLayoutNode.


        :param module_info: The module_info of this GraphLayoutNode.  # noqa: E501
        :type: dict(str, dict(str, object))
        """

        self._module_info = module_info

    @property
    def start_ts(self):
        """Gets the start_ts of this GraphLayoutNode.  # noqa: E501


        :return: The start_ts of this GraphLayoutNode.  # noqa: E501
        :rtype: int
        """
        return self._start_ts

    @start_ts.setter
    def start_ts(self, start_ts):
        """Sets the start_ts of this GraphLayoutNode.


        :param start_ts: The start_ts of this GraphLayoutNode.  # noqa: E501
        :type: int
        """

        self._start_ts = start_ts

    @property
    def end_ts(self):
        """Gets the end_ts of this GraphLayoutNode.  # noqa: E501


        :return: The end_ts of this GraphLayoutNode.  # noqa: E501
        :rtype: int
        """
        return self._end_ts

    @end_ts.setter
    def end_ts(self, end_ts):
        """Sets the end_ts of this GraphLayoutNode.


        :param end_ts: The end_ts of this GraphLayoutNode.  # noqa: E501
        :type: int
        """

        self._end_ts = end_ts

    @property
    def edge_layout_list(self):
        """Gets the edge_layout_list of this GraphLayoutNode.  # noqa: E501


        :return: The edge_layout_list of this GraphLayoutNode.  # noqa: E501
        :rtype: EdgeLayoutList
        """
        return self._edge_layout_list

    @edge_layout_list.setter
    def edge_layout_list(self, edge_layout_list):
        """Sets the edge_layout_list of this GraphLayoutNode.


        :param edge_layout_list: The edge_layout_list of this GraphLayoutNode.  # noqa: E501
        :type: EdgeLayoutList
        """

        self._edge_layout_list = edge_layout_list

    @property
    def skip_info(self):
        """Gets the skip_info of this GraphLayoutNode.  # noqa: E501


        :return: The skip_info of this GraphLayoutNode.  # noqa: E501
        :rtype: SkipInfo
        """
        return self._skip_info

    @skip_info.setter
    def skip_info(self, skip_info):
        """Sets the skip_info of this GraphLayoutNode.


        :param skip_info: The skip_info of this GraphLayoutNode.  # noqa: E501
        :type: SkipInfo
        """

        self._skip_info = skip_info

    @property
    def node_run_info(self):
        """Gets the node_run_info of this GraphLayoutNode.  # noqa: E501


        :return: The node_run_info of this GraphLayoutNode.  # noqa: E501
        :rtype: NodeRunInfo
        """
        return self._node_run_info

    @node_run_info.setter
    def node_run_info(self, node_run_info):
        """Sets the node_run_info of this GraphLayoutNode.


        :param node_run_info: The node_run_info of this GraphLayoutNode.  # noqa: E501
        :type: NodeRunInfo
        """

        self._node_run_info = node_run_info

    @property
    def barrier_found(self):
        """Gets the barrier_found of this GraphLayoutNode.  # noqa: E501


        :return: The barrier_found of this GraphLayoutNode.  # noqa: E501
        :rtype: bool
        """
        return self._barrier_found

    @barrier_found.setter
    def barrier_found(self, barrier_found):
        """Sets the barrier_found of this GraphLayoutNode.


        :param barrier_found: The barrier_found of this GraphLayoutNode.  # noqa: E501
        :type: bool
        """

        self._barrier_found = barrier_found

    @property
    def failure_info(self):
        """Gets the failure_info of this GraphLayoutNode.  # noqa: E501


        :return: The failure_info of this GraphLayoutNode.  # noqa: E501
        :rtype: ExecutionErrorInfo
        """
        return self._failure_info

    @failure_info.setter
    def failure_info(self, failure_info):
        """Sets the failure_info of this GraphLayoutNode.


        :param failure_info: The failure_info of this GraphLayoutNode.  # noqa: E501
        :type: ExecutionErrorInfo
        """

        self._failure_info = failure_info

    @property
    def failure_info_dto(self):
        """Gets the failure_info_dto of this GraphLayoutNode.  # noqa: E501


        :return: The failure_info_dto of this GraphLayoutNode.  # noqa: E501
        :rtype: FailureInfoDTO
        """
        return self._failure_info_dto

    @failure_info_dto.setter
    def failure_info_dto(self, failure_info_dto):
        """Sets the failure_info_dto of this GraphLayoutNode.


        :param failure_info_dto: The failure_info_dto of this GraphLayoutNode.  # noqa: E501
        :type: FailureInfoDTO
        """

        self._failure_info_dto = failure_info_dto

    @property
    def step_details(self):
        """Gets the step_details of this GraphLayoutNode.  # noqa: E501


        :return: The step_details of this GraphLayoutNode.  # noqa: E501
        :rtype: dict(str, PmsStepDetails)
        """
        return self._step_details

    @step_details.setter
    def step_details(self, step_details):
        """Sets the step_details of this GraphLayoutNode.


        :param step_details: The step_details of this GraphLayoutNode.  # noqa: E501
        :type: dict(str, PmsStepDetails)
        """

        self._step_details = step_details

    @property
    def hidden(self):
        """Gets the hidden of this GraphLayoutNode.  # noqa: E501


        :return: The hidden of this GraphLayoutNode.  # noqa: E501
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this GraphLayoutNode.


        :param hidden: The hidden of this GraphLayoutNode.  # noqa: E501
        :type: bool
        """

        self._hidden = hidden

    @property
    def node_execution_id(self):
        """Gets the node_execution_id of this GraphLayoutNode.  # noqa: E501


        :return: The node_execution_id of this GraphLayoutNode.  # noqa: E501
        :rtype: str
        """
        return self._node_execution_id

    @node_execution_id.setter
    def node_execution_id(self, node_execution_id):
        """Sets the node_execution_id of this GraphLayoutNode.


        :param node_execution_id: The node_execution_id of this GraphLayoutNode.  # noqa: E501
        :type: str
        """

        self._node_execution_id = node_execution_id

    @property
    def strategy_metadata(self):
        """Gets the strategy_metadata of this GraphLayoutNode.  # noqa: E501


        :return: The strategy_metadata of this GraphLayoutNode.  # noqa: E501
        :rtype: StrategyMetadata
        """
        return self._strategy_metadata

    @strategy_metadata.setter
    def strategy_metadata(self, strategy_metadata):
        """Sets the strategy_metadata of this GraphLayoutNode.


        :param strategy_metadata: The strategy_metadata of this GraphLayoutNode.  # noqa: E501
        :type: StrategyMetadata
        """

        self._strategy_metadata = strategy_metadata

    @property
    def execution_input_configured(self):
        """Gets the execution_input_configured of this GraphLayoutNode.  # noqa: E501


        :return: The execution_input_configured of this GraphLayoutNode.  # noqa: E501
        :rtype: bool
        """
        return self._execution_input_configured

    @execution_input_configured.setter
    def execution_input_configured(self, execution_input_configured):
        """Sets the execution_input_configured of this GraphLayoutNode.


        :param execution_input_configured: The execution_input_configured of this GraphLayoutNode.  # noqa: E501
        :type: bool
        """

        self._execution_input_configured = execution_input_configured

    @property
    def is_rollback_stage_node(self):
        """Gets the is_rollback_stage_node of this GraphLayoutNode.  # noqa: E501


        :return: The is_rollback_stage_node of this GraphLayoutNode.  # noqa: E501
        :rtype: bool
        """
        return self._is_rollback_stage_node

    @is_rollback_stage_node.setter
    def is_rollback_stage_node(self, is_rollback_stage_node):
        """Sets the is_rollback_stage_node of this GraphLayoutNode.


        :param is_rollback_stage_node: The is_rollback_stage_node of this GraphLayoutNode.  # noqa: E501
        :type: bool
        """

        self._is_rollback_stage_node = is_rollback_stage_node

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
        if issubclass(GraphLayoutNode, dict):
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
        if not isinstance(other, GraphLayoutNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
