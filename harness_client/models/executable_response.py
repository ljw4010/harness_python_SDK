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

class ExecutableResponse(object):
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
        'children': 'ChildrenExecutableResponse',
        'task': 'TaskExecutableResponse',
        'child': 'ChildExecutableResponse',
        '_async': 'AsyncExecutableResponse',
        'serialized_size': 'int',
        'parser_for_type': 'ParserExecutableResponse',
        'default_instance_for_type': 'ExecutableResponse',
        'async_or_builder': 'AsyncExecutableResponseOrBuilder',
        'child_or_builder': 'ChildExecutableResponseOrBuilder',
        'children_or_builder': 'ChildrenExecutableResponseOrBuilder',
        'child_chain': 'ChildChainExecutableResponse',
        'child_chain_or_builder': 'ChildChainExecutableResponseOrBuilder',
        'task_or_builder': 'TaskExecutableResponseOrBuilder',
        'task_chain': 'TaskChainExecutableResponse',
        'task_chain_or_builder': 'TaskChainExecutableResponseOrBuilder',
        'sync': 'SyncExecutableResponse',
        'sync_or_builder': 'SyncExecutableResponseOrBuilder',
        'skip_task': 'SkipTaskExecutableResponse',
        'skip_task_or_builder': 'SkipTaskExecutableResponseOrBuilder',
        'async_chain': 'AsyncChainExecutableResponse',
        'async_chain_or_builder': 'AsyncChainExecutableResponseOrBuilder',
        'response_case': 'str',
        'initialized': 'bool',
        'all_fields': 'dict(str, object)',
        'descriptor_for_type': 'Descriptor',
        'initialization_error_string': 'str',
        'memoized_serialized_size': 'int'
    }

    attribute_map = {
        'unknown_fields': 'unknownFields',
        'children': 'children',
        'task': 'task',
        'child': 'child',
        '_async': 'async',
        'serialized_size': 'serializedSize',
        'parser_for_type': 'parserForType',
        'default_instance_for_type': 'defaultInstanceForType',
        'async_or_builder': 'asyncOrBuilder',
        'child_or_builder': 'childOrBuilder',
        'children_or_builder': 'childrenOrBuilder',
        'child_chain': 'childChain',
        'child_chain_or_builder': 'childChainOrBuilder',
        'task_or_builder': 'taskOrBuilder',
        'task_chain': 'taskChain',
        'task_chain_or_builder': 'taskChainOrBuilder',
        'sync': 'sync',
        'sync_or_builder': 'syncOrBuilder',
        'skip_task': 'skipTask',
        'skip_task_or_builder': 'skipTaskOrBuilder',
        'async_chain': 'asyncChain',
        'async_chain_or_builder': 'asyncChainOrBuilder',
        'response_case': 'responseCase',
        'initialized': 'initialized',
        'all_fields': 'allFields',
        'descriptor_for_type': 'descriptorForType',
        'initialization_error_string': 'initializationErrorString',
        'memoized_serialized_size': 'memoizedSerializedSize'
    }

    def __init__(self, unknown_fields=None, children=None, task=None, child=None, _async=None, serialized_size=None, parser_for_type=None, default_instance_for_type=None, async_or_builder=None, child_or_builder=None, children_or_builder=None, child_chain=None, child_chain_or_builder=None, task_or_builder=None, task_chain=None, task_chain_or_builder=None, sync=None, sync_or_builder=None, skip_task=None, skip_task_or_builder=None, async_chain=None, async_chain_or_builder=None, response_case=None, initialized=None, all_fields=None, descriptor_for_type=None, initialization_error_string=None, memoized_serialized_size=None):  # noqa: E501
        """ExecutableResponse - a model defined in Swagger"""  # noqa: E501
        self._unknown_fields = None
        self._children = None
        self._task = None
        self._child = None
        self.__async = None
        self._serialized_size = None
        self._parser_for_type = None
        self._default_instance_for_type = None
        self._async_or_builder = None
        self._child_or_builder = None
        self._children_or_builder = None
        self._child_chain = None
        self._child_chain_or_builder = None
        self._task_or_builder = None
        self._task_chain = None
        self._task_chain_or_builder = None
        self._sync = None
        self._sync_or_builder = None
        self._skip_task = None
        self._skip_task_or_builder = None
        self._async_chain = None
        self._async_chain_or_builder = None
        self._response_case = None
        self._initialized = None
        self._all_fields = None
        self._descriptor_for_type = None
        self._initialization_error_string = None
        self._memoized_serialized_size = None
        self.discriminator = None
        if unknown_fields is not None:
            self.unknown_fields = unknown_fields
        if children is not None:
            self.children = children
        if task is not None:
            self.task = task
        if child is not None:
            self.child = child
        if _async is not None:
            self._async = _async
        if serialized_size is not None:
            self.serialized_size = serialized_size
        if parser_for_type is not None:
            self.parser_for_type = parser_for_type
        if default_instance_for_type is not None:
            self.default_instance_for_type = default_instance_for_type
        if async_or_builder is not None:
            self.async_or_builder = async_or_builder
        if child_or_builder is not None:
            self.child_or_builder = child_or_builder
        if children_or_builder is not None:
            self.children_or_builder = children_or_builder
        if child_chain is not None:
            self.child_chain = child_chain
        if child_chain_or_builder is not None:
            self.child_chain_or_builder = child_chain_or_builder
        if task_or_builder is not None:
            self.task_or_builder = task_or_builder
        if task_chain is not None:
            self.task_chain = task_chain
        if task_chain_or_builder is not None:
            self.task_chain_or_builder = task_chain_or_builder
        if sync is not None:
            self.sync = sync
        if sync_or_builder is not None:
            self.sync_or_builder = sync_or_builder
        if skip_task is not None:
            self.skip_task = skip_task
        if skip_task_or_builder is not None:
            self.skip_task_or_builder = skip_task_or_builder
        if async_chain is not None:
            self.async_chain = async_chain
        if async_chain_or_builder is not None:
            self.async_chain_or_builder = async_chain_or_builder
        if response_case is not None:
            self.response_case = response_case
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
        """Gets the unknown_fields of this ExecutableResponse.  # noqa: E501


        :return: The unknown_fields of this ExecutableResponse.  # noqa: E501
        :rtype: UnknownFieldSet
        """
        return self._unknown_fields

    @unknown_fields.setter
    def unknown_fields(self, unknown_fields):
        """Sets the unknown_fields of this ExecutableResponse.


        :param unknown_fields: The unknown_fields of this ExecutableResponse.  # noqa: E501
        :type: UnknownFieldSet
        """

        self._unknown_fields = unknown_fields

    @property
    def children(self):
        """Gets the children of this ExecutableResponse.  # noqa: E501


        :return: The children of this ExecutableResponse.  # noqa: E501
        :rtype: ChildrenExecutableResponse
        """
        return self._children

    @children.setter
    def children(self, children):
        """Sets the children of this ExecutableResponse.


        :param children: The children of this ExecutableResponse.  # noqa: E501
        :type: ChildrenExecutableResponse
        """

        self._children = children

    @property
    def task(self):
        """Gets the task of this ExecutableResponse.  # noqa: E501


        :return: The task of this ExecutableResponse.  # noqa: E501
        :rtype: TaskExecutableResponse
        """
        return self._task

    @task.setter
    def task(self, task):
        """Sets the task of this ExecutableResponse.


        :param task: The task of this ExecutableResponse.  # noqa: E501
        :type: TaskExecutableResponse
        """

        self._task = task

    @property
    def child(self):
        """Gets the child of this ExecutableResponse.  # noqa: E501


        :return: The child of this ExecutableResponse.  # noqa: E501
        :rtype: ChildExecutableResponse
        """
        return self._child

    @child.setter
    def child(self, child):
        """Sets the child of this ExecutableResponse.


        :param child: The child of this ExecutableResponse.  # noqa: E501
        :type: ChildExecutableResponse
        """

        self._child = child

    @property
    def _async(self):
        """Gets the _async of this ExecutableResponse.  # noqa: E501


        :return: The _async of this ExecutableResponse.  # noqa: E501
        :rtype: AsyncExecutableResponse
        """
        return self.__async

    @_async.setter
    def _async(self, _async):
        """Sets the _async of this ExecutableResponse.


        :param _async: The _async of this ExecutableResponse.  # noqa: E501
        :type: AsyncExecutableResponse
        """

        self.__async = _async

    @property
    def serialized_size(self):
        """Gets the serialized_size of this ExecutableResponse.  # noqa: E501


        :return: The serialized_size of this ExecutableResponse.  # noqa: E501
        :rtype: int
        """
        return self._serialized_size

    @serialized_size.setter
    def serialized_size(self, serialized_size):
        """Sets the serialized_size of this ExecutableResponse.


        :param serialized_size: The serialized_size of this ExecutableResponse.  # noqa: E501
        :type: int
        """

        self._serialized_size = serialized_size

    @property
    def parser_for_type(self):
        """Gets the parser_for_type of this ExecutableResponse.  # noqa: E501


        :return: The parser_for_type of this ExecutableResponse.  # noqa: E501
        :rtype: ParserExecutableResponse
        """
        return self._parser_for_type

    @parser_for_type.setter
    def parser_for_type(self, parser_for_type):
        """Sets the parser_for_type of this ExecutableResponse.


        :param parser_for_type: The parser_for_type of this ExecutableResponse.  # noqa: E501
        :type: ParserExecutableResponse
        """

        self._parser_for_type = parser_for_type

    @property
    def default_instance_for_type(self):
        """Gets the default_instance_for_type of this ExecutableResponse.  # noqa: E501


        :return: The default_instance_for_type of this ExecutableResponse.  # noqa: E501
        :rtype: ExecutableResponse
        """
        return self._default_instance_for_type

    @default_instance_for_type.setter
    def default_instance_for_type(self, default_instance_for_type):
        """Sets the default_instance_for_type of this ExecutableResponse.


        :param default_instance_for_type: The default_instance_for_type of this ExecutableResponse.  # noqa: E501
        :type: ExecutableResponse
        """

        self._default_instance_for_type = default_instance_for_type

    @property
    def async_or_builder(self):
        """Gets the async_or_builder of this ExecutableResponse.  # noqa: E501


        :return: The async_or_builder of this ExecutableResponse.  # noqa: E501
        :rtype: AsyncExecutableResponseOrBuilder
        """
        return self._async_or_builder

    @async_or_builder.setter
    def async_or_builder(self, async_or_builder):
        """Sets the async_or_builder of this ExecutableResponse.


        :param async_or_builder: The async_or_builder of this ExecutableResponse.  # noqa: E501
        :type: AsyncExecutableResponseOrBuilder
        """

        self._async_or_builder = async_or_builder

    @property
    def child_or_builder(self):
        """Gets the child_or_builder of this ExecutableResponse.  # noqa: E501


        :return: The child_or_builder of this ExecutableResponse.  # noqa: E501
        :rtype: ChildExecutableResponseOrBuilder
        """
        return self._child_or_builder

    @child_or_builder.setter
    def child_or_builder(self, child_or_builder):
        """Sets the child_or_builder of this ExecutableResponse.


        :param child_or_builder: The child_or_builder of this ExecutableResponse.  # noqa: E501
        :type: ChildExecutableResponseOrBuilder
        """

        self._child_or_builder = child_or_builder

    @property
    def children_or_builder(self):
        """Gets the children_or_builder of this ExecutableResponse.  # noqa: E501


        :return: The children_or_builder of this ExecutableResponse.  # noqa: E501
        :rtype: ChildrenExecutableResponseOrBuilder
        """
        return self._children_or_builder

    @children_or_builder.setter
    def children_or_builder(self, children_or_builder):
        """Sets the children_or_builder of this ExecutableResponse.


        :param children_or_builder: The children_or_builder of this ExecutableResponse.  # noqa: E501
        :type: ChildrenExecutableResponseOrBuilder
        """

        self._children_or_builder = children_or_builder

    @property
    def child_chain(self):
        """Gets the child_chain of this ExecutableResponse.  # noqa: E501


        :return: The child_chain of this ExecutableResponse.  # noqa: E501
        :rtype: ChildChainExecutableResponse
        """
        return self._child_chain

    @child_chain.setter
    def child_chain(self, child_chain):
        """Sets the child_chain of this ExecutableResponse.


        :param child_chain: The child_chain of this ExecutableResponse.  # noqa: E501
        :type: ChildChainExecutableResponse
        """

        self._child_chain = child_chain

    @property
    def child_chain_or_builder(self):
        """Gets the child_chain_or_builder of this ExecutableResponse.  # noqa: E501


        :return: The child_chain_or_builder of this ExecutableResponse.  # noqa: E501
        :rtype: ChildChainExecutableResponseOrBuilder
        """
        return self._child_chain_or_builder

    @child_chain_or_builder.setter
    def child_chain_or_builder(self, child_chain_or_builder):
        """Sets the child_chain_or_builder of this ExecutableResponse.


        :param child_chain_or_builder: The child_chain_or_builder of this ExecutableResponse.  # noqa: E501
        :type: ChildChainExecutableResponseOrBuilder
        """

        self._child_chain_or_builder = child_chain_or_builder

    @property
    def task_or_builder(self):
        """Gets the task_or_builder of this ExecutableResponse.  # noqa: E501


        :return: The task_or_builder of this ExecutableResponse.  # noqa: E501
        :rtype: TaskExecutableResponseOrBuilder
        """
        return self._task_or_builder

    @task_or_builder.setter
    def task_or_builder(self, task_or_builder):
        """Sets the task_or_builder of this ExecutableResponse.


        :param task_or_builder: The task_or_builder of this ExecutableResponse.  # noqa: E501
        :type: TaskExecutableResponseOrBuilder
        """

        self._task_or_builder = task_or_builder

    @property
    def task_chain(self):
        """Gets the task_chain of this ExecutableResponse.  # noqa: E501


        :return: The task_chain of this ExecutableResponse.  # noqa: E501
        :rtype: TaskChainExecutableResponse
        """
        return self._task_chain

    @task_chain.setter
    def task_chain(self, task_chain):
        """Sets the task_chain of this ExecutableResponse.


        :param task_chain: The task_chain of this ExecutableResponse.  # noqa: E501
        :type: TaskChainExecutableResponse
        """

        self._task_chain = task_chain

    @property
    def task_chain_or_builder(self):
        """Gets the task_chain_or_builder of this ExecutableResponse.  # noqa: E501


        :return: The task_chain_or_builder of this ExecutableResponse.  # noqa: E501
        :rtype: TaskChainExecutableResponseOrBuilder
        """
        return self._task_chain_or_builder

    @task_chain_or_builder.setter
    def task_chain_or_builder(self, task_chain_or_builder):
        """Sets the task_chain_or_builder of this ExecutableResponse.


        :param task_chain_or_builder: The task_chain_or_builder of this ExecutableResponse.  # noqa: E501
        :type: TaskChainExecutableResponseOrBuilder
        """

        self._task_chain_or_builder = task_chain_or_builder

    @property
    def sync(self):
        """Gets the sync of this ExecutableResponse.  # noqa: E501


        :return: The sync of this ExecutableResponse.  # noqa: E501
        :rtype: SyncExecutableResponse
        """
        return self._sync

    @sync.setter
    def sync(self, sync):
        """Sets the sync of this ExecutableResponse.


        :param sync: The sync of this ExecutableResponse.  # noqa: E501
        :type: SyncExecutableResponse
        """

        self._sync = sync

    @property
    def sync_or_builder(self):
        """Gets the sync_or_builder of this ExecutableResponse.  # noqa: E501


        :return: The sync_or_builder of this ExecutableResponse.  # noqa: E501
        :rtype: SyncExecutableResponseOrBuilder
        """
        return self._sync_or_builder

    @sync_or_builder.setter
    def sync_or_builder(self, sync_or_builder):
        """Sets the sync_or_builder of this ExecutableResponse.


        :param sync_or_builder: The sync_or_builder of this ExecutableResponse.  # noqa: E501
        :type: SyncExecutableResponseOrBuilder
        """

        self._sync_or_builder = sync_or_builder

    @property
    def skip_task(self):
        """Gets the skip_task of this ExecutableResponse.  # noqa: E501


        :return: The skip_task of this ExecutableResponse.  # noqa: E501
        :rtype: SkipTaskExecutableResponse
        """
        return self._skip_task

    @skip_task.setter
    def skip_task(self, skip_task):
        """Sets the skip_task of this ExecutableResponse.


        :param skip_task: The skip_task of this ExecutableResponse.  # noqa: E501
        :type: SkipTaskExecutableResponse
        """

        self._skip_task = skip_task

    @property
    def skip_task_or_builder(self):
        """Gets the skip_task_or_builder of this ExecutableResponse.  # noqa: E501


        :return: The skip_task_or_builder of this ExecutableResponse.  # noqa: E501
        :rtype: SkipTaskExecutableResponseOrBuilder
        """
        return self._skip_task_or_builder

    @skip_task_or_builder.setter
    def skip_task_or_builder(self, skip_task_or_builder):
        """Sets the skip_task_or_builder of this ExecutableResponse.


        :param skip_task_or_builder: The skip_task_or_builder of this ExecutableResponse.  # noqa: E501
        :type: SkipTaskExecutableResponseOrBuilder
        """

        self._skip_task_or_builder = skip_task_or_builder

    @property
    def async_chain(self):
        """Gets the async_chain of this ExecutableResponse.  # noqa: E501


        :return: The async_chain of this ExecutableResponse.  # noqa: E501
        :rtype: AsyncChainExecutableResponse
        """
        return self._async_chain

    @async_chain.setter
    def async_chain(self, async_chain):
        """Sets the async_chain of this ExecutableResponse.


        :param async_chain: The async_chain of this ExecutableResponse.  # noqa: E501
        :type: AsyncChainExecutableResponse
        """

        self._async_chain = async_chain

    @property
    def async_chain_or_builder(self):
        """Gets the async_chain_or_builder of this ExecutableResponse.  # noqa: E501


        :return: The async_chain_or_builder of this ExecutableResponse.  # noqa: E501
        :rtype: AsyncChainExecutableResponseOrBuilder
        """
        return self._async_chain_or_builder

    @async_chain_or_builder.setter
    def async_chain_or_builder(self, async_chain_or_builder):
        """Sets the async_chain_or_builder of this ExecutableResponse.


        :param async_chain_or_builder: The async_chain_or_builder of this ExecutableResponse.  # noqa: E501
        :type: AsyncChainExecutableResponseOrBuilder
        """

        self._async_chain_or_builder = async_chain_or_builder

    @property
    def response_case(self):
        """Gets the response_case of this ExecutableResponse.  # noqa: E501


        :return: The response_case of this ExecutableResponse.  # noqa: E501
        :rtype: str
        """
        return self._response_case

    @response_case.setter
    def response_case(self, response_case):
        """Sets the response_case of this ExecutableResponse.


        :param response_case: The response_case of this ExecutableResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["ASYNC", "CHILD", "CHILDREN", "CHILDCHAIN", "TASK", "TASKCHAIN", "SYNC", "SKIPTASK", "ASYNCCHAIN", "RESPONSE_NOT_SET"]  # noqa: E501
        if response_case not in allowed_values:
            raise ValueError(
                "Invalid value for `response_case` ({0}), must be one of {1}"  # noqa: E501
                .format(response_case, allowed_values)
            )

        self._response_case = response_case

    @property
    def initialized(self):
        """Gets the initialized of this ExecutableResponse.  # noqa: E501


        :return: The initialized of this ExecutableResponse.  # noqa: E501
        :rtype: bool
        """
        return self._initialized

    @initialized.setter
    def initialized(self, initialized):
        """Sets the initialized of this ExecutableResponse.


        :param initialized: The initialized of this ExecutableResponse.  # noqa: E501
        :type: bool
        """

        self._initialized = initialized

    @property
    def all_fields(self):
        """Gets the all_fields of this ExecutableResponse.  # noqa: E501


        :return: The all_fields of this ExecutableResponse.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._all_fields

    @all_fields.setter
    def all_fields(self, all_fields):
        """Sets the all_fields of this ExecutableResponse.


        :param all_fields: The all_fields of this ExecutableResponse.  # noqa: E501
        :type: dict(str, object)
        """

        self._all_fields = all_fields

    @property
    def descriptor_for_type(self):
        """Gets the descriptor_for_type of this ExecutableResponse.  # noqa: E501


        :return: The descriptor_for_type of this ExecutableResponse.  # noqa: E501
        :rtype: Descriptor
        """
        return self._descriptor_for_type

    @descriptor_for_type.setter
    def descriptor_for_type(self, descriptor_for_type):
        """Sets the descriptor_for_type of this ExecutableResponse.


        :param descriptor_for_type: The descriptor_for_type of this ExecutableResponse.  # noqa: E501
        :type: Descriptor
        """

        self._descriptor_for_type = descriptor_for_type

    @property
    def initialization_error_string(self):
        """Gets the initialization_error_string of this ExecutableResponse.  # noqa: E501


        :return: The initialization_error_string of this ExecutableResponse.  # noqa: E501
        :rtype: str
        """
        return self._initialization_error_string

    @initialization_error_string.setter
    def initialization_error_string(self, initialization_error_string):
        """Sets the initialization_error_string of this ExecutableResponse.


        :param initialization_error_string: The initialization_error_string of this ExecutableResponse.  # noqa: E501
        :type: str
        """

        self._initialization_error_string = initialization_error_string

    @property
    def memoized_serialized_size(self):
        """Gets the memoized_serialized_size of this ExecutableResponse.  # noqa: E501


        :return: The memoized_serialized_size of this ExecutableResponse.  # noqa: E501
        :rtype: int
        """
        return self._memoized_serialized_size

    @memoized_serialized_size.setter
    def memoized_serialized_size(self, memoized_serialized_size):
        """Sets the memoized_serialized_size of this ExecutableResponse.


        :param memoized_serialized_size: The memoized_serialized_size of this ExecutableResponse.  # noqa: E501
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
        if issubclass(ExecutableResponse, dict):
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
        if not isinstance(other, ExecutableResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
