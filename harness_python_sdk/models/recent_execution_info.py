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

class RecentExecutionInfo(object):
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
        'executor_info': 'ExecutorInfo',
        'execution_id': 'str',
        'execution_status': 'str',
        'started': 'int',
        'ended': 'int',
        'run_number': 'int',
        'parent_stage_info': 'ParentStageInfo'
    }

    attribute_map = {
        'executor_info': 'executor_info',
        'execution_id': 'execution_id',
        'execution_status': 'execution_status',
        'started': 'started',
        'ended': 'ended',
        'run_number': 'run_number',
        'parent_stage_info': 'parent_stage_info'
    }

    def __init__(self, executor_info=None, execution_id=None, execution_status=None, started=None, ended=None, run_number=None, parent_stage_info=None):  # noqa: E501
        """RecentExecutionInfo - a model defined in Swagger"""  # noqa: E501
        self._executor_info = None
        self._execution_id = None
        self._execution_status = None
        self._started = None
        self._ended = None
        self._run_number = None
        self._parent_stage_info = None
        self.discriminator = None
        if executor_info is not None:
            self.executor_info = executor_info
        if execution_id is not None:
            self.execution_id = execution_id
        if execution_status is not None:
            self.execution_status = execution_status
        if started is not None:
            self.started = started
        if ended is not None:
            self.ended = ended
        if run_number is not None:
            self.run_number = run_number
        if parent_stage_info is not None:
            self.parent_stage_info = parent_stage_info

    @property
    def executor_info(self):
        """Gets the executor_info of this RecentExecutionInfo.  # noqa: E501


        :return: The executor_info of this RecentExecutionInfo.  # noqa: E501
        :rtype: ExecutorInfo
        """
        return self._executor_info

    @executor_info.setter
    def executor_info(self, executor_info):
        """Sets the executor_info of this RecentExecutionInfo.


        :param executor_info: The executor_info of this RecentExecutionInfo.  # noqa: E501
        :type: ExecutorInfo
        """

        self._executor_info = executor_info

    @property
    def execution_id(self):
        """Gets the execution_id of this RecentExecutionInfo.  # noqa: E501

        Execution identifier  # noqa: E501

        :return: The execution_id of this RecentExecutionInfo.  # noqa: E501
        :rtype: str
        """
        return self._execution_id

    @execution_id.setter
    def execution_id(self, execution_id):
        """Sets the execution_id of this RecentExecutionInfo.

        Execution identifier  # noqa: E501

        :param execution_id: The execution_id of this RecentExecutionInfo.  # noqa: E501
        :type: str
        """

        self._execution_id = execution_id

    @property
    def execution_status(self):
        """Gets the execution_status of this RecentExecutionInfo.  # noqa: E501

        Last Execution status of the Pipeline.  # noqa: E501

        :return: The execution_status of this RecentExecutionInfo.  # noqa: E501
        :rtype: str
        """
        return self._execution_status

    @execution_status.setter
    def execution_status(self, execution_status):
        """Sets the execution_status of this RecentExecutionInfo.

        Last Execution status of the Pipeline.  # noqa: E501

        :param execution_status: The execution_status of this RecentExecutionInfo.  # noqa: E501
        :type: str
        """
        allowed_values = ["Running", "AsyncWaiting", "TaskWaiting", "TimedWaiting", "Failed", "Errored", "IgnoreFailed", "NotStarted", "Expired", "Aborted", "Discontinuing", "Queued", "Paused", "ResourceWaiting", "InterventionWaiting", "ApprovalWaiting", "Success", "Suspended", "Skipped", "Pausing", "ApprovalRejected", "InputWaiting", "NOT_STARTED", "INTERVENTION_WAITING", "APPROVAL_WAITING", "APPROVAL_REJECTED", "Waiting"]  # noqa: E501
        if execution_status not in allowed_values:
            raise ValueError(
                "Invalid value for `execution_status` ({0}), must be one of {1}"  # noqa: E501
                .format(execution_status, allowed_values)
            )

        self._execution_status = execution_status

    @property
    def started(self):
        """Gets the started of this RecentExecutionInfo.  # noqa: E501

        Start timestamp of Execution  # noqa: E501

        :return: The started of this RecentExecutionInfo.  # noqa: E501
        :rtype: int
        """
        return self._started

    @started.setter
    def started(self, started):
        """Sets the started of this RecentExecutionInfo.

        Start timestamp of Execution  # noqa: E501

        :param started: The started of this RecentExecutionInfo.  # noqa: E501
        :type: int
        """

        self._started = started

    @property
    def ended(self):
        """Gets the ended of this RecentExecutionInfo.  # noqa: E501

        End timestamp of Execution  # noqa: E501

        :return: The ended of this RecentExecutionInfo.  # noqa: E501
        :rtype: int
        """
        return self._ended

    @ended.setter
    def ended(self, ended):
        """Sets the ended of this RecentExecutionInfo.

        End timestamp of Execution  # noqa: E501

        :param ended: The ended of this RecentExecutionInfo.  # noqa: E501
        :type: int
        """

        self._ended = ended

    @property
    def run_number(self):
        """Gets the run_number of this RecentExecutionInfo.  # noqa: E501

        The Execution number of this Pipeline.  # noqa: E501

        :return: The run_number of this RecentExecutionInfo.  # noqa: E501
        :rtype: int
        """
        return self._run_number

    @run_number.setter
    def run_number(self, run_number):
        """Sets the run_number of this RecentExecutionInfo.

        The Execution number of this Pipeline.  # noqa: E501

        :param run_number: The run_number of this RecentExecutionInfo.  # noqa: E501
        :type: int
        """

        self._run_number = run_number

    @property
    def parent_stage_info(self):
        """Gets the parent_stage_info of this RecentExecutionInfo.  # noqa: E501


        :return: The parent_stage_info of this RecentExecutionInfo.  # noqa: E501
        :rtype: ParentStageInfo
        """
        return self._parent_stage_info

    @parent_stage_info.setter
    def parent_stage_info(self, parent_stage_info):
        """Sets the parent_stage_info of this RecentExecutionInfo.


        :param parent_stage_info: The parent_stage_info of this RecentExecutionInfo.  # noqa: E501
        :type: ParentStageInfo
        """

        self._parent_stage_info = parent_stage_info

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
        if issubclass(RecentExecutionInfo, dict):
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
        if not isinstance(other, RecentExecutionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
