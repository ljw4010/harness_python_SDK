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

class ExecutionTriggerInfo(object):
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
        'is_rerun': 'bool',
        'serialized_size': 'int',
        'parser_for_type': 'ParserExecutionTriggerInfo',
        'default_instance_for_type': 'ExecutionTriggerInfo',
        'trigger_type_value': 'int',
        'trigger_type': 'str',
        'triggered_by': 'TriggeredBy',
        'triggered_by_or_builder': 'TriggeredByOrBuilder',
        'rerun_info': 'RerunInfo',
        'rerun_info_or_builder': 'RerunInfoOrBuilder',
        'build_info': 'BuildInfo',
        'build_info_or_builder': 'BuildInfoOrBuilder',
        'initialized': 'bool',
        'all_fields': 'dict(str, object)',
        'descriptor_for_type': 'Descriptor',
        'initialization_error_string': 'str',
        'memoized_serialized_size': 'int'
    }

    attribute_map = {
        'unknown_fields': 'unknownFields',
        'is_rerun': 'isRerun',
        'serialized_size': 'serializedSize',
        'parser_for_type': 'parserForType',
        'default_instance_for_type': 'defaultInstanceForType',
        'trigger_type_value': 'triggerTypeValue',
        'trigger_type': 'triggerType',
        'triggered_by': 'triggeredBy',
        'triggered_by_or_builder': 'triggeredByOrBuilder',
        'rerun_info': 'rerunInfo',
        'rerun_info_or_builder': 'rerunInfoOrBuilder',
        'build_info': 'buildInfo',
        'build_info_or_builder': 'buildInfoOrBuilder',
        'initialized': 'initialized',
        'all_fields': 'allFields',
        'descriptor_for_type': 'descriptorForType',
        'initialization_error_string': 'initializationErrorString',
        'memoized_serialized_size': 'memoizedSerializedSize'
    }

    def __init__(self, unknown_fields=None, is_rerun=None, serialized_size=None, parser_for_type=None, default_instance_for_type=None, trigger_type_value=None, trigger_type=None, triggered_by=None, triggered_by_or_builder=None, rerun_info=None, rerun_info_or_builder=None, build_info=None, build_info_or_builder=None, initialized=None, all_fields=None, descriptor_for_type=None, initialization_error_string=None, memoized_serialized_size=None):  # noqa: E501
        """ExecutionTriggerInfo - a model defined in Swagger"""  # noqa: E501
        self._unknown_fields = None
        self._is_rerun = None
        self._serialized_size = None
        self._parser_for_type = None
        self._default_instance_for_type = None
        self._trigger_type_value = None
        self._trigger_type = None
        self._triggered_by = None
        self._triggered_by_or_builder = None
        self._rerun_info = None
        self._rerun_info_or_builder = None
        self._build_info = None
        self._build_info_or_builder = None
        self._initialized = None
        self._all_fields = None
        self._descriptor_for_type = None
        self._initialization_error_string = None
        self._memoized_serialized_size = None
        self.discriminator = None
        if unknown_fields is not None:
            self.unknown_fields = unknown_fields
        if is_rerun is not None:
            self.is_rerun = is_rerun
        if serialized_size is not None:
            self.serialized_size = serialized_size
        if parser_for_type is not None:
            self.parser_for_type = parser_for_type
        if default_instance_for_type is not None:
            self.default_instance_for_type = default_instance_for_type
        if trigger_type_value is not None:
            self.trigger_type_value = trigger_type_value
        if trigger_type is not None:
            self.trigger_type = trigger_type
        if triggered_by is not None:
            self.triggered_by = triggered_by
        if triggered_by_or_builder is not None:
            self.triggered_by_or_builder = triggered_by_or_builder
        if rerun_info is not None:
            self.rerun_info = rerun_info
        if rerun_info_or_builder is not None:
            self.rerun_info_or_builder = rerun_info_or_builder
        if build_info is not None:
            self.build_info = build_info
        if build_info_or_builder is not None:
            self.build_info_or_builder = build_info_or_builder
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
        """Gets the unknown_fields of this ExecutionTriggerInfo.  # noqa: E501


        :return: The unknown_fields of this ExecutionTriggerInfo.  # noqa: E501
        :rtype: UnknownFieldSet
        """
        return self._unknown_fields

    @unknown_fields.setter
    def unknown_fields(self, unknown_fields):
        """Sets the unknown_fields of this ExecutionTriggerInfo.


        :param unknown_fields: The unknown_fields of this ExecutionTriggerInfo.  # noqa: E501
        :type: UnknownFieldSet
        """

        self._unknown_fields = unknown_fields

    @property
    def is_rerun(self):
        """Gets the is_rerun of this ExecutionTriggerInfo.  # noqa: E501


        :return: The is_rerun of this ExecutionTriggerInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_rerun

    @is_rerun.setter
    def is_rerun(self, is_rerun):
        """Sets the is_rerun of this ExecutionTriggerInfo.


        :param is_rerun: The is_rerun of this ExecutionTriggerInfo.  # noqa: E501
        :type: bool
        """

        self._is_rerun = is_rerun

    @property
    def serialized_size(self):
        """Gets the serialized_size of this ExecutionTriggerInfo.  # noqa: E501


        :return: The serialized_size of this ExecutionTriggerInfo.  # noqa: E501
        :rtype: int
        """
        return self._serialized_size

    @serialized_size.setter
    def serialized_size(self, serialized_size):
        """Sets the serialized_size of this ExecutionTriggerInfo.


        :param serialized_size: The serialized_size of this ExecutionTriggerInfo.  # noqa: E501
        :type: int
        """

        self._serialized_size = serialized_size

    @property
    def parser_for_type(self):
        """Gets the parser_for_type of this ExecutionTriggerInfo.  # noqa: E501


        :return: The parser_for_type of this ExecutionTriggerInfo.  # noqa: E501
        :rtype: ParserExecutionTriggerInfo
        """
        return self._parser_for_type

    @parser_for_type.setter
    def parser_for_type(self, parser_for_type):
        """Sets the parser_for_type of this ExecutionTriggerInfo.


        :param parser_for_type: The parser_for_type of this ExecutionTriggerInfo.  # noqa: E501
        :type: ParserExecutionTriggerInfo
        """

        self._parser_for_type = parser_for_type

    @property
    def default_instance_for_type(self):
        """Gets the default_instance_for_type of this ExecutionTriggerInfo.  # noqa: E501


        :return: The default_instance_for_type of this ExecutionTriggerInfo.  # noqa: E501
        :rtype: ExecutionTriggerInfo
        """
        return self._default_instance_for_type

    @default_instance_for_type.setter
    def default_instance_for_type(self, default_instance_for_type):
        """Sets the default_instance_for_type of this ExecutionTriggerInfo.


        :param default_instance_for_type: The default_instance_for_type of this ExecutionTriggerInfo.  # noqa: E501
        :type: ExecutionTriggerInfo
        """

        self._default_instance_for_type = default_instance_for_type

    @property
    def trigger_type_value(self):
        """Gets the trigger_type_value of this ExecutionTriggerInfo.  # noqa: E501


        :return: The trigger_type_value of this ExecutionTriggerInfo.  # noqa: E501
        :rtype: int
        """
        return self._trigger_type_value

    @trigger_type_value.setter
    def trigger_type_value(self, trigger_type_value):
        """Sets the trigger_type_value of this ExecutionTriggerInfo.


        :param trigger_type_value: The trigger_type_value of this ExecutionTriggerInfo.  # noqa: E501
        :type: int
        """

        self._trigger_type_value = trigger_type_value

    @property
    def trigger_type(self):
        """Gets the trigger_type of this ExecutionTriggerInfo.  # noqa: E501


        :return: The trigger_type of this ExecutionTriggerInfo.  # noqa: E501
        :rtype: str
        """
        return self._trigger_type

    @trigger_type.setter
    def trigger_type(self, trigger_type):
        """Sets the trigger_type of this ExecutionTriggerInfo.


        :param trigger_type: The trigger_type of this ExecutionTriggerInfo.  # noqa: E501
        :type: str
        """
        allowed_values = ["NOOP", "MANUAL", "WEBHOOK", "WEBHOOK_CUSTOM", "SCHEDULER_CRON", "ARTIFACT", "MANIFEST", "UNRECOGNIZED"]  # noqa: E501
        if trigger_type not in allowed_values:
            raise ValueError(
                "Invalid value for `trigger_type` ({0}), must be one of {1}"  # noqa: E501
                .format(trigger_type, allowed_values)
            )

        self._trigger_type = trigger_type

    @property
    def triggered_by(self):
        """Gets the triggered_by of this ExecutionTriggerInfo.  # noqa: E501


        :return: The triggered_by of this ExecutionTriggerInfo.  # noqa: E501
        :rtype: TriggeredBy
        """
        return self._triggered_by

    @triggered_by.setter
    def triggered_by(self, triggered_by):
        """Sets the triggered_by of this ExecutionTriggerInfo.


        :param triggered_by: The triggered_by of this ExecutionTriggerInfo.  # noqa: E501
        :type: TriggeredBy
        """

        self._triggered_by = triggered_by

    @property
    def triggered_by_or_builder(self):
        """Gets the triggered_by_or_builder of this ExecutionTriggerInfo.  # noqa: E501


        :return: The triggered_by_or_builder of this ExecutionTriggerInfo.  # noqa: E501
        :rtype: TriggeredByOrBuilder
        """
        return self._triggered_by_or_builder

    @triggered_by_or_builder.setter
    def triggered_by_or_builder(self, triggered_by_or_builder):
        """Sets the triggered_by_or_builder of this ExecutionTriggerInfo.


        :param triggered_by_or_builder: The triggered_by_or_builder of this ExecutionTriggerInfo.  # noqa: E501
        :type: TriggeredByOrBuilder
        """

        self._triggered_by_or_builder = triggered_by_or_builder

    @property
    def rerun_info(self):
        """Gets the rerun_info of this ExecutionTriggerInfo.  # noqa: E501


        :return: The rerun_info of this ExecutionTriggerInfo.  # noqa: E501
        :rtype: RerunInfo
        """
        return self._rerun_info

    @rerun_info.setter
    def rerun_info(self, rerun_info):
        """Sets the rerun_info of this ExecutionTriggerInfo.


        :param rerun_info: The rerun_info of this ExecutionTriggerInfo.  # noqa: E501
        :type: RerunInfo
        """

        self._rerun_info = rerun_info

    @property
    def rerun_info_or_builder(self):
        """Gets the rerun_info_or_builder of this ExecutionTriggerInfo.  # noqa: E501


        :return: The rerun_info_or_builder of this ExecutionTriggerInfo.  # noqa: E501
        :rtype: RerunInfoOrBuilder
        """
        return self._rerun_info_or_builder

    @rerun_info_or_builder.setter
    def rerun_info_or_builder(self, rerun_info_or_builder):
        """Sets the rerun_info_or_builder of this ExecutionTriggerInfo.


        :param rerun_info_or_builder: The rerun_info_or_builder of this ExecutionTriggerInfo.  # noqa: E501
        :type: RerunInfoOrBuilder
        """

        self._rerun_info_or_builder = rerun_info_or_builder

    @property
    def build_info(self):
        """Gets the build_info of this ExecutionTriggerInfo.  # noqa: E501


        :return: The build_info of this ExecutionTriggerInfo.  # noqa: E501
        :rtype: BuildInfo
        """
        return self._build_info

    @build_info.setter
    def build_info(self, build_info):
        """Sets the build_info of this ExecutionTriggerInfo.


        :param build_info: The build_info of this ExecutionTriggerInfo.  # noqa: E501
        :type: BuildInfo
        """

        self._build_info = build_info

    @property
    def build_info_or_builder(self):
        """Gets the build_info_or_builder of this ExecutionTriggerInfo.  # noqa: E501


        :return: The build_info_or_builder of this ExecutionTriggerInfo.  # noqa: E501
        :rtype: BuildInfoOrBuilder
        """
        return self._build_info_or_builder

    @build_info_or_builder.setter
    def build_info_or_builder(self, build_info_or_builder):
        """Sets the build_info_or_builder of this ExecutionTriggerInfo.


        :param build_info_or_builder: The build_info_or_builder of this ExecutionTriggerInfo.  # noqa: E501
        :type: BuildInfoOrBuilder
        """

        self._build_info_or_builder = build_info_or_builder

    @property
    def initialized(self):
        """Gets the initialized of this ExecutionTriggerInfo.  # noqa: E501


        :return: The initialized of this ExecutionTriggerInfo.  # noqa: E501
        :rtype: bool
        """
        return self._initialized

    @initialized.setter
    def initialized(self, initialized):
        """Sets the initialized of this ExecutionTriggerInfo.


        :param initialized: The initialized of this ExecutionTriggerInfo.  # noqa: E501
        :type: bool
        """

        self._initialized = initialized

    @property
    def all_fields(self):
        """Gets the all_fields of this ExecutionTriggerInfo.  # noqa: E501


        :return: The all_fields of this ExecutionTriggerInfo.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._all_fields

    @all_fields.setter
    def all_fields(self, all_fields):
        """Sets the all_fields of this ExecutionTriggerInfo.


        :param all_fields: The all_fields of this ExecutionTriggerInfo.  # noqa: E501
        :type: dict(str, object)
        """

        self._all_fields = all_fields

    @property
    def descriptor_for_type(self):
        """Gets the descriptor_for_type of this ExecutionTriggerInfo.  # noqa: E501


        :return: The descriptor_for_type of this ExecutionTriggerInfo.  # noqa: E501
        :rtype: Descriptor
        """
        return self._descriptor_for_type

    @descriptor_for_type.setter
    def descriptor_for_type(self, descriptor_for_type):
        """Sets the descriptor_for_type of this ExecutionTriggerInfo.


        :param descriptor_for_type: The descriptor_for_type of this ExecutionTriggerInfo.  # noqa: E501
        :type: Descriptor
        """

        self._descriptor_for_type = descriptor_for_type

    @property
    def initialization_error_string(self):
        """Gets the initialization_error_string of this ExecutionTriggerInfo.  # noqa: E501


        :return: The initialization_error_string of this ExecutionTriggerInfo.  # noqa: E501
        :rtype: str
        """
        return self._initialization_error_string

    @initialization_error_string.setter
    def initialization_error_string(self, initialization_error_string):
        """Sets the initialization_error_string of this ExecutionTriggerInfo.


        :param initialization_error_string: The initialization_error_string of this ExecutionTriggerInfo.  # noqa: E501
        :type: str
        """

        self._initialization_error_string = initialization_error_string

    @property
    def memoized_serialized_size(self):
        """Gets the memoized_serialized_size of this ExecutionTriggerInfo.  # noqa: E501


        :return: The memoized_serialized_size of this ExecutionTriggerInfo.  # noqa: E501
        :rtype: int
        """
        return self._memoized_serialized_size

    @memoized_serialized_size.setter
    def memoized_serialized_size(self, memoized_serialized_size):
        """Sets the memoized_serialized_size of this ExecutionTriggerInfo.


        :param memoized_serialized_size: The memoized_serialized_size of this ExecutionTriggerInfo.  # noqa: E501
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
        if issubclass(ExecutionTriggerInfo, dict):
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
        if not isinstance(other, ExecutionTriggerInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
