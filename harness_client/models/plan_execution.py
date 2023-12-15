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

class PlanExecution(object):
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
        'created_at': 'int',
        'plan_id': 'str',
        'setup_abstractions': 'dict(str, str)',
        'valid_until': 'datetime',
        'status': 'str',
        'start_ts': 'int',
        'end_ts': 'int',
        'metadata': 'ExecutionMetadata',
        'governance_metadata': 'PipelineGovernanceMetadata',
        'last_updated_at': 'int',
        'version': 'int',
        'next_iteration': 'int',
        'ambiance': 'Ambiance',
        'node_id': 'str',
        'node_type': 'str'
    }

    attribute_map = {
        'uuid': 'uuid',
        'created_at': 'createdAt',
        'plan_id': 'planId',
        'setup_abstractions': 'setupAbstractions',
        'valid_until': 'validUntil',
        'status': 'status',
        'start_ts': 'startTs',
        'end_ts': 'endTs',
        'metadata': 'metadata',
        'governance_metadata': 'governanceMetadata',
        'last_updated_at': 'lastUpdatedAt',
        'version': 'version',
        'next_iteration': 'nextIteration',
        'ambiance': 'ambiance',
        'node_id': 'nodeId',
        'node_type': 'nodeType'
    }

    def __init__(self, uuid=None, created_at=None, plan_id=None, setup_abstractions=None, valid_until=None, status=None, start_ts=None, end_ts=None, metadata=None, governance_metadata=None, last_updated_at=None, version=None, next_iteration=None, ambiance=None, node_id=None, node_type=None):  # noqa: E501
        """PlanExecution - a model defined in Swagger"""  # noqa: E501
        self._uuid = None
        self._created_at = None
        self._plan_id = None
        self._setup_abstractions = None
        self._valid_until = None
        self._status = None
        self._start_ts = None
        self._end_ts = None
        self._metadata = None
        self._governance_metadata = None
        self._last_updated_at = None
        self._version = None
        self._next_iteration = None
        self._ambiance = None
        self._node_id = None
        self._node_type = None
        self.discriminator = None
        if uuid is not None:
            self.uuid = uuid
        if created_at is not None:
            self.created_at = created_at
        if plan_id is not None:
            self.plan_id = plan_id
        if setup_abstractions is not None:
            self.setup_abstractions = setup_abstractions
        if valid_until is not None:
            self.valid_until = valid_until
        if status is not None:
            self.status = status
        if start_ts is not None:
            self.start_ts = start_ts
        if end_ts is not None:
            self.end_ts = end_ts
        if metadata is not None:
            self.metadata = metadata
        if governance_metadata is not None:
            self.governance_metadata = governance_metadata
        if last_updated_at is not None:
            self.last_updated_at = last_updated_at
        if version is not None:
            self.version = version
        if next_iteration is not None:
            self.next_iteration = next_iteration
        if ambiance is not None:
            self.ambiance = ambiance
        if node_id is not None:
            self.node_id = node_id
        if node_type is not None:
            self.node_type = node_type

    @property
    def uuid(self):
        """Gets the uuid of this PlanExecution.  # noqa: E501


        :return: The uuid of this PlanExecution.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this PlanExecution.


        :param uuid: The uuid of this PlanExecution.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def created_at(self):
        """Gets the created_at of this PlanExecution.  # noqa: E501


        :return: The created_at of this PlanExecution.  # noqa: E501
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this PlanExecution.


        :param created_at: The created_at of this PlanExecution.  # noqa: E501
        :type: int
        """

        self._created_at = created_at

    @property
    def plan_id(self):
        """Gets the plan_id of this PlanExecution.  # noqa: E501


        :return: The plan_id of this PlanExecution.  # noqa: E501
        :rtype: str
        """
        return self._plan_id

    @plan_id.setter
    def plan_id(self, plan_id):
        """Sets the plan_id of this PlanExecution.


        :param plan_id: The plan_id of this PlanExecution.  # noqa: E501
        :type: str
        """

        self._plan_id = plan_id

    @property
    def setup_abstractions(self):
        """Gets the setup_abstractions of this PlanExecution.  # noqa: E501


        :return: The setup_abstractions of this PlanExecution.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._setup_abstractions

    @setup_abstractions.setter
    def setup_abstractions(self, setup_abstractions):
        """Sets the setup_abstractions of this PlanExecution.


        :param setup_abstractions: The setup_abstractions of this PlanExecution.  # noqa: E501
        :type: dict(str, str)
        """

        self._setup_abstractions = setup_abstractions

    @property
    def valid_until(self):
        """Gets the valid_until of this PlanExecution.  # noqa: E501


        :return: The valid_until of this PlanExecution.  # noqa: E501
        :rtype: datetime
        """
        return self._valid_until

    @valid_until.setter
    def valid_until(self, valid_until):
        """Sets the valid_until of this PlanExecution.


        :param valid_until: The valid_until of this PlanExecution.  # noqa: E501
        :type: datetime
        """

        self._valid_until = valid_until

    @property
    def status(self):
        """Gets the status of this PlanExecution.  # noqa: E501


        :return: The status of this PlanExecution.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PlanExecution.


        :param status: The status of this PlanExecution.  # noqa: E501
        :type: str
        """
        allowed_values = ["NO_OP", "RUNNING", "INTERVENTION_WAITING", "TIMED_WAITING", "ASYNC_WAITING", "TASK_WAITING", "DISCONTINUING", "PAUSING", "QUEUED", "SKIPPED", "PAUSED", "ABORTED", "ERRORED", "FAILED", "EXPIRED", "SUSPENDED", "SUCCEEDED", "IGNORE_FAILED", "APPROVAL_WAITING", "RESOURCE_WAITING", "APPROVAL_REJECTED", "INPUT_WAITING", "WAIT_STEP_RUNNING", "FREEZE_FAILED", "QUEUED_LICENSE_LIMIT_REACHED", "QUEUED_EXECUTION_CONCURRENCY_REACHED", "UNRECOGNIZED"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def start_ts(self):
        """Gets the start_ts of this PlanExecution.  # noqa: E501


        :return: The start_ts of this PlanExecution.  # noqa: E501
        :rtype: int
        """
        return self._start_ts

    @start_ts.setter
    def start_ts(self, start_ts):
        """Sets the start_ts of this PlanExecution.


        :param start_ts: The start_ts of this PlanExecution.  # noqa: E501
        :type: int
        """

        self._start_ts = start_ts

    @property
    def end_ts(self):
        """Gets the end_ts of this PlanExecution.  # noqa: E501


        :return: The end_ts of this PlanExecution.  # noqa: E501
        :rtype: int
        """
        return self._end_ts

    @end_ts.setter
    def end_ts(self, end_ts):
        """Sets the end_ts of this PlanExecution.


        :param end_ts: The end_ts of this PlanExecution.  # noqa: E501
        :type: int
        """

        self._end_ts = end_ts

    @property
    def metadata(self):
        """Gets the metadata of this PlanExecution.  # noqa: E501


        :return: The metadata of this PlanExecution.  # noqa: E501
        :rtype: ExecutionMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this PlanExecution.


        :param metadata: The metadata of this PlanExecution.  # noqa: E501
        :type: ExecutionMetadata
        """

        self._metadata = metadata

    @property
    def governance_metadata(self):
        """Gets the governance_metadata of this PlanExecution.  # noqa: E501


        :return: The governance_metadata of this PlanExecution.  # noqa: E501
        :rtype: PipelineGovernanceMetadata
        """
        return self._governance_metadata

    @governance_metadata.setter
    def governance_metadata(self, governance_metadata):
        """Sets the governance_metadata of this PlanExecution.


        :param governance_metadata: The governance_metadata of this PlanExecution.  # noqa: E501
        :type: PipelineGovernanceMetadata
        """

        self._governance_metadata = governance_metadata

    @property
    def last_updated_at(self):
        """Gets the last_updated_at of this PlanExecution.  # noqa: E501


        :return: The last_updated_at of this PlanExecution.  # noqa: E501
        :rtype: int
        """
        return self._last_updated_at

    @last_updated_at.setter
    def last_updated_at(self, last_updated_at):
        """Sets the last_updated_at of this PlanExecution.


        :param last_updated_at: The last_updated_at of this PlanExecution.  # noqa: E501
        :type: int
        """

        self._last_updated_at = last_updated_at

    @property
    def version(self):
        """Gets the version of this PlanExecution.  # noqa: E501


        :return: The version of this PlanExecution.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PlanExecution.


        :param version: The version of this PlanExecution.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def next_iteration(self):
        """Gets the next_iteration of this PlanExecution.  # noqa: E501


        :return: The next_iteration of this PlanExecution.  # noqa: E501
        :rtype: int
        """
        return self._next_iteration

    @next_iteration.setter
    def next_iteration(self, next_iteration):
        """Sets the next_iteration of this PlanExecution.


        :param next_iteration: The next_iteration of this PlanExecution.  # noqa: E501
        :type: int
        """

        self._next_iteration = next_iteration

    @property
    def ambiance(self):
        """Gets the ambiance of this PlanExecution.  # noqa: E501


        :return: The ambiance of this PlanExecution.  # noqa: E501
        :rtype: Ambiance
        """
        return self._ambiance

    @ambiance.setter
    def ambiance(self, ambiance):
        """Sets the ambiance of this PlanExecution.


        :param ambiance: The ambiance of this PlanExecution.  # noqa: E501
        :type: Ambiance
        """

        self._ambiance = ambiance

    @property
    def node_id(self):
        """Gets the node_id of this PlanExecution.  # noqa: E501


        :return: The node_id of this PlanExecution.  # noqa: E501
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this PlanExecution.


        :param node_id: The node_id of this PlanExecution.  # noqa: E501
        :type: str
        """

        self._node_id = node_id

    @property
    def node_type(self):
        """Gets the node_type of this PlanExecution.  # noqa: E501


        :return: The node_type of this PlanExecution.  # noqa: E501
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        """Sets the node_type of this PlanExecution.


        :param node_type: The node_type of this PlanExecution.  # noqa: E501
        :type: str
        """
        allowed_values = ["PLAN", "PLAN_NODE", "IDENTITY_PLAN_NODE"]  # noqa: E501
        if node_type not in allowed_values:
            raise ValueError(
                "Invalid value for `node_type` ({0}), must be one of {1}"  # noqa: E501
                .format(node_type, allowed_values)
            )

        self._node_type = node_type

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
        if issubclass(PlanExecution, dict):
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
        if not isinstance(other, PlanExecution):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
