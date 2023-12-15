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

class ExecutionNode(object):
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
        'setup_id': 'str',
        'name': 'str',
        'identifier': 'str',
        'base_fqn': 'str',
        'outcomes': 'dict(str, OrchestrationMap)',
        'step_parameters': 'OrchestrationMap',
        'start_ts': 'int',
        'end_ts': 'int',
        'step_type': 'str',
        'status': 'str',
        'failure_info': 'FailureInfoDTO',
        'skip_info': 'SkipInfo',
        'node_run_info': 'NodeRunInfo',
        'executable_responses': 'list[ExecutableResponse]',
        'unit_progresses': 'list[UnitProgress]',
        'progress_data': 'OrchestrationMap',
        'delegate_info_list': 'list[DelegateInfo]',
        'interrupt_histories': 'list[InterruptEffectDTO]',
        'step_details': 'dict(str, OrchestrationMap)',
        'strategy_metadata': 'StrategyMetadata',
        'execution_input_configured': 'bool',
        'log_base_key': 'str'
    }

    attribute_map = {
        'uuid': 'uuid',
        'setup_id': 'setupId',
        'name': 'name',
        'identifier': 'identifier',
        'base_fqn': 'baseFqn',
        'outcomes': 'outcomes',
        'step_parameters': 'stepParameters',
        'start_ts': 'startTs',
        'end_ts': 'endTs',
        'step_type': 'stepType',
        'status': 'status',
        'failure_info': 'failureInfo',
        'skip_info': 'skipInfo',
        'node_run_info': 'nodeRunInfo',
        'executable_responses': 'executableResponses',
        'unit_progresses': 'unitProgresses',
        'progress_data': 'progressData',
        'delegate_info_list': 'delegateInfoList',
        'interrupt_histories': 'interruptHistories',
        'step_details': 'stepDetails',
        'strategy_metadata': 'strategyMetadata',
        'execution_input_configured': 'executionInputConfigured',
        'log_base_key': 'logBaseKey'
    }

    def __init__(self, uuid=None, setup_id=None, name=None, identifier=None, base_fqn=None, outcomes=None, step_parameters=None, start_ts=None, end_ts=None, step_type=None, status=None, failure_info=None, skip_info=None, node_run_info=None, executable_responses=None, unit_progresses=None, progress_data=None, delegate_info_list=None, interrupt_histories=None, step_details=None, strategy_metadata=None, execution_input_configured=None, log_base_key=None):  # noqa: E501
        """ExecutionNode - a model defined in Swagger"""  # noqa: E501
        self._uuid = None
        self._setup_id = None
        self._name = None
        self._identifier = None
        self._base_fqn = None
        self._outcomes = None
        self._step_parameters = None
        self._start_ts = None
        self._end_ts = None
        self._step_type = None
        self._status = None
        self._failure_info = None
        self._skip_info = None
        self._node_run_info = None
        self._executable_responses = None
        self._unit_progresses = None
        self._progress_data = None
        self._delegate_info_list = None
        self._interrupt_histories = None
        self._step_details = None
        self._strategy_metadata = None
        self._execution_input_configured = None
        self._log_base_key = None
        self.discriminator = None
        if uuid is not None:
            self.uuid = uuid
        if setup_id is not None:
            self.setup_id = setup_id
        if name is not None:
            self.name = name
        if identifier is not None:
            self.identifier = identifier
        if base_fqn is not None:
            self.base_fqn = base_fqn
        if outcomes is not None:
            self.outcomes = outcomes
        if step_parameters is not None:
            self.step_parameters = step_parameters
        if start_ts is not None:
            self.start_ts = start_ts
        if end_ts is not None:
            self.end_ts = end_ts
        if step_type is not None:
            self.step_type = step_type
        if status is not None:
            self.status = status
        if failure_info is not None:
            self.failure_info = failure_info
        if skip_info is not None:
            self.skip_info = skip_info
        if node_run_info is not None:
            self.node_run_info = node_run_info
        if executable_responses is not None:
            self.executable_responses = executable_responses
        if unit_progresses is not None:
            self.unit_progresses = unit_progresses
        if progress_data is not None:
            self.progress_data = progress_data
        if delegate_info_list is not None:
            self.delegate_info_list = delegate_info_list
        if interrupt_histories is not None:
            self.interrupt_histories = interrupt_histories
        if step_details is not None:
            self.step_details = step_details
        if strategy_metadata is not None:
            self.strategy_metadata = strategy_metadata
        if execution_input_configured is not None:
            self.execution_input_configured = execution_input_configured
        if log_base_key is not None:
            self.log_base_key = log_base_key

    @property
    def uuid(self):
        """Gets the uuid of this ExecutionNode.  # noqa: E501


        :return: The uuid of this ExecutionNode.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this ExecutionNode.


        :param uuid: The uuid of this ExecutionNode.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def setup_id(self):
        """Gets the setup_id of this ExecutionNode.  # noqa: E501


        :return: The setup_id of this ExecutionNode.  # noqa: E501
        :rtype: str
        """
        return self._setup_id

    @setup_id.setter
    def setup_id(self, setup_id):
        """Sets the setup_id of this ExecutionNode.


        :param setup_id: The setup_id of this ExecutionNode.  # noqa: E501
        :type: str
        """

        self._setup_id = setup_id

    @property
    def name(self):
        """Gets the name of this ExecutionNode.  # noqa: E501


        :return: The name of this ExecutionNode.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ExecutionNode.


        :param name: The name of this ExecutionNode.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def identifier(self):
        """Gets the identifier of this ExecutionNode.  # noqa: E501


        :return: The identifier of this ExecutionNode.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this ExecutionNode.


        :param identifier: The identifier of this ExecutionNode.  # noqa: E501
        :type: str
        """

        self._identifier = identifier

    @property
    def base_fqn(self):
        """Gets the base_fqn of this ExecutionNode.  # noqa: E501


        :return: The base_fqn of this ExecutionNode.  # noqa: E501
        :rtype: str
        """
        return self._base_fqn

    @base_fqn.setter
    def base_fqn(self, base_fqn):
        """Sets the base_fqn of this ExecutionNode.


        :param base_fqn: The base_fqn of this ExecutionNode.  # noqa: E501
        :type: str
        """

        self._base_fqn = base_fqn

    @property
    def outcomes(self):
        """Gets the outcomes of this ExecutionNode.  # noqa: E501


        :return: The outcomes of this ExecutionNode.  # noqa: E501
        :rtype: dict(str, OrchestrationMap)
        """
        return self._outcomes

    @outcomes.setter
    def outcomes(self, outcomes):
        """Sets the outcomes of this ExecutionNode.


        :param outcomes: The outcomes of this ExecutionNode.  # noqa: E501
        :type: dict(str, OrchestrationMap)
        """

        self._outcomes = outcomes

    @property
    def step_parameters(self):
        """Gets the step_parameters of this ExecutionNode.  # noqa: E501


        :return: The step_parameters of this ExecutionNode.  # noqa: E501
        :rtype: OrchestrationMap
        """
        return self._step_parameters

    @step_parameters.setter
    def step_parameters(self, step_parameters):
        """Sets the step_parameters of this ExecutionNode.


        :param step_parameters: The step_parameters of this ExecutionNode.  # noqa: E501
        :type: OrchestrationMap
        """

        self._step_parameters = step_parameters

    @property
    def start_ts(self):
        """Gets the start_ts of this ExecutionNode.  # noqa: E501


        :return: The start_ts of this ExecutionNode.  # noqa: E501
        :rtype: int
        """
        return self._start_ts

    @start_ts.setter
    def start_ts(self, start_ts):
        """Sets the start_ts of this ExecutionNode.


        :param start_ts: The start_ts of this ExecutionNode.  # noqa: E501
        :type: int
        """

        self._start_ts = start_ts

    @property
    def end_ts(self):
        """Gets the end_ts of this ExecutionNode.  # noqa: E501


        :return: The end_ts of this ExecutionNode.  # noqa: E501
        :rtype: int
        """
        return self._end_ts

    @end_ts.setter
    def end_ts(self, end_ts):
        """Sets the end_ts of this ExecutionNode.


        :param end_ts: The end_ts of this ExecutionNode.  # noqa: E501
        :type: int
        """

        self._end_ts = end_ts

    @property
    def step_type(self):
        """Gets the step_type of this ExecutionNode.  # noqa: E501


        :return: The step_type of this ExecutionNode.  # noqa: E501
        :rtype: str
        """
        return self._step_type

    @step_type.setter
    def step_type(self, step_type):
        """Sets the step_type of this ExecutionNode.


        :param step_type: The step_type of this ExecutionNode.  # noqa: E501
        :type: str
        """

        self._step_type = step_type

    @property
    def status(self):
        """Gets the status of this ExecutionNode.  # noqa: E501

        This is the Execution Status of the entity  # noqa: E501

        :return: The status of this ExecutionNode.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ExecutionNode.

        This is the Execution Status of the entity  # noqa: E501

        :param status: The status of this ExecutionNode.  # noqa: E501
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
    def failure_info(self):
        """Gets the failure_info of this ExecutionNode.  # noqa: E501


        :return: The failure_info of this ExecutionNode.  # noqa: E501
        :rtype: FailureInfoDTO
        """
        return self._failure_info

    @failure_info.setter
    def failure_info(self, failure_info):
        """Sets the failure_info of this ExecutionNode.


        :param failure_info: The failure_info of this ExecutionNode.  # noqa: E501
        :type: FailureInfoDTO
        """

        self._failure_info = failure_info

    @property
    def skip_info(self):
        """Gets the skip_info of this ExecutionNode.  # noqa: E501


        :return: The skip_info of this ExecutionNode.  # noqa: E501
        :rtype: SkipInfo
        """
        return self._skip_info

    @skip_info.setter
    def skip_info(self, skip_info):
        """Sets the skip_info of this ExecutionNode.


        :param skip_info: The skip_info of this ExecutionNode.  # noqa: E501
        :type: SkipInfo
        """

        self._skip_info = skip_info

    @property
    def node_run_info(self):
        """Gets the node_run_info of this ExecutionNode.  # noqa: E501


        :return: The node_run_info of this ExecutionNode.  # noqa: E501
        :rtype: NodeRunInfo
        """
        return self._node_run_info

    @node_run_info.setter
    def node_run_info(self, node_run_info):
        """Sets the node_run_info of this ExecutionNode.


        :param node_run_info: The node_run_info of this ExecutionNode.  # noqa: E501
        :type: NodeRunInfo
        """

        self._node_run_info = node_run_info

    @property
    def executable_responses(self):
        """Gets the executable_responses of this ExecutionNode.  # noqa: E501


        :return: The executable_responses of this ExecutionNode.  # noqa: E501
        :rtype: list[ExecutableResponse]
        """
        return self._executable_responses

    @executable_responses.setter
    def executable_responses(self, executable_responses):
        """Sets the executable_responses of this ExecutionNode.


        :param executable_responses: The executable_responses of this ExecutionNode.  # noqa: E501
        :type: list[ExecutableResponse]
        """

        self._executable_responses = executable_responses

    @property
    def unit_progresses(self):
        """Gets the unit_progresses of this ExecutionNode.  # noqa: E501


        :return: The unit_progresses of this ExecutionNode.  # noqa: E501
        :rtype: list[UnitProgress]
        """
        return self._unit_progresses

    @unit_progresses.setter
    def unit_progresses(self, unit_progresses):
        """Sets the unit_progresses of this ExecutionNode.


        :param unit_progresses: The unit_progresses of this ExecutionNode.  # noqa: E501
        :type: list[UnitProgress]
        """

        self._unit_progresses = unit_progresses

    @property
    def progress_data(self):
        """Gets the progress_data of this ExecutionNode.  # noqa: E501


        :return: The progress_data of this ExecutionNode.  # noqa: E501
        :rtype: OrchestrationMap
        """
        return self._progress_data

    @progress_data.setter
    def progress_data(self, progress_data):
        """Sets the progress_data of this ExecutionNode.


        :param progress_data: The progress_data of this ExecutionNode.  # noqa: E501
        :type: OrchestrationMap
        """

        self._progress_data = progress_data

    @property
    def delegate_info_list(self):
        """Gets the delegate_info_list of this ExecutionNode.  # noqa: E501


        :return: The delegate_info_list of this ExecutionNode.  # noqa: E501
        :rtype: list[DelegateInfo]
        """
        return self._delegate_info_list

    @delegate_info_list.setter
    def delegate_info_list(self, delegate_info_list):
        """Sets the delegate_info_list of this ExecutionNode.


        :param delegate_info_list: The delegate_info_list of this ExecutionNode.  # noqa: E501
        :type: list[DelegateInfo]
        """

        self._delegate_info_list = delegate_info_list

    @property
    def interrupt_histories(self):
        """Gets the interrupt_histories of this ExecutionNode.  # noqa: E501


        :return: The interrupt_histories of this ExecutionNode.  # noqa: E501
        :rtype: list[InterruptEffectDTO]
        """
        return self._interrupt_histories

    @interrupt_histories.setter
    def interrupt_histories(self, interrupt_histories):
        """Sets the interrupt_histories of this ExecutionNode.


        :param interrupt_histories: The interrupt_histories of this ExecutionNode.  # noqa: E501
        :type: list[InterruptEffectDTO]
        """

        self._interrupt_histories = interrupt_histories

    @property
    def step_details(self):
        """Gets the step_details of this ExecutionNode.  # noqa: E501


        :return: The step_details of this ExecutionNode.  # noqa: E501
        :rtype: dict(str, OrchestrationMap)
        """
        return self._step_details

    @step_details.setter
    def step_details(self, step_details):
        """Sets the step_details of this ExecutionNode.


        :param step_details: The step_details of this ExecutionNode.  # noqa: E501
        :type: dict(str, OrchestrationMap)
        """

        self._step_details = step_details

    @property
    def strategy_metadata(self):
        """Gets the strategy_metadata of this ExecutionNode.  # noqa: E501


        :return: The strategy_metadata of this ExecutionNode.  # noqa: E501
        :rtype: StrategyMetadata
        """
        return self._strategy_metadata

    @strategy_metadata.setter
    def strategy_metadata(self, strategy_metadata):
        """Sets the strategy_metadata of this ExecutionNode.


        :param strategy_metadata: The strategy_metadata of this ExecutionNode.  # noqa: E501
        :type: StrategyMetadata
        """

        self._strategy_metadata = strategy_metadata

    @property
    def execution_input_configured(self):
        """Gets the execution_input_configured of this ExecutionNode.  # noqa: E501


        :return: The execution_input_configured of this ExecutionNode.  # noqa: E501
        :rtype: bool
        """
        return self._execution_input_configured

    @execution_input_configured.setter
    def execution_input_configured(self, execution_input_configured):
        """Sets the execution_input_configured of this ExecutionNode.


        :param execution_input_configured: The execution_input_configured of this ExecutionNode.  # noqa: E501
        :type: bool
        """

        self._execution_input_configured = execution_input_configured

    @property
    def log_base_key(self):
        """Gets the log_base_key of this ExecutionNode.  # noqa: E501


        :return: The log_base_key of this ExecutionNode.  # noqa: E501
        :rtype: str
        """
        return self._log_base_key

    @log_base_key.setter
    def log_base_key(self, log_base_key):
        """Sets the log_base_key of this ExecutionNode.


        :param log_base_key: The log_base_key of this ExecutionNode.  # noqa: E501
        :type: str
        """

        self._log_base_key = log_base_key

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
        if issubclass(ExecutionNode, dict):
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
        if not isinstance(other, ExecutionNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
