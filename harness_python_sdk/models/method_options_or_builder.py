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

class MethodOptionsOrBuilder(object):
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
        'idempotency_level': 'str',
        'uninterpreted_option_count': 'int',
        'deprecated': 'bool',
        'uninterpreted_option_list': 'list[UninterpretedOption]',
        'uninterpreted_option_or_builder_list': 'list[UninterpretedOptionOrBuilder]',
        'default_instance_for_type': 'Message',
        'all_fields': 'dict(str, object)',
        'descriptor_for_type': 'Descriptor',
        'initialization_error_string': 'str',
        'unknown_fields': 'UnknownFieldSet',
        'initialized': 'bool'
    }

    attribute_map = {
        'idempotency_level': 'idempotencyLevel',
        'uninterpreted_option_count': 'uninterpretedOptionCount',
        'deprecated': 'deprecated',
        'uninterpreted_option_list': 'uninterpretedOptionList',
        'uninterpreted_option_or_builder_list': 'uninterpretedOptionOrBuilderList',
        'default_instance_for_type': 'defaultInstanceForType',
        'all_fields': 'allFields',
        'descriptor_for_type': 'descriptorForType',
        'initialization_error_string': 'initializationErrorString',
        'unknown_fields': 'unknownFields',
        'initialized': 'initialized'
    }

    def __init__(self, idempotency_level=None, uninterpreted_option_count=None, deprecated=None, uninterpreted_option_list=None, uninterpreted_option_or_builder_list=None, default_instance_for_type=None, all_fields=None, descriptor_for_type=None, initialization_error_string=None, unknown_fields=None, initialized=None):  # noqa: E501
        """MethodOptionsOrBuilder - a model defined in Swagger"""  # noqa: E501
        self._idempotency_level = None
        self._uninterpreted_option_count = None
        self._deprecated = None
        self._uninterpreted_option_list = None
        self._uninterpreted_option_or_builder_list = None
        self._default_instance_for_type = None
        self._all_fields = None
        self._descriptor_for_type = None
        self._initialization_error_string = None
        self._unknown_fields = None
        self._initialized = None
        self.discriminator = None
        if idempotency_level is not None:
            self.idempotency_level = idempotency_level
        if uninterpreted_option_count is not None:
            self.uninterpreted_option_count = uninterpreted_option_count
        if deprecated is not None:
            self.deprecated = deprecated
        if uninterpreted_option_list is not None:
            self.uninterpreted_option_list = uninterpreted_option_list
        if uninterpreted_option_or_builder_list is not None:
            self.uninterpreted_option_or_builder_list = uninterpreted_option_or_builder_list
        if default_instance_for_type is not None:
            self.default_instance_for_type = default_instance_for_type
        if all_fields is not None:
            self.all_fields = all_fields
        if descriptor_for_type is not None:
            self.descriptor_for_type = descriptor_for_type
        if initialization_error_string is not None:
            self.initialization_error_string = initialization_error_string
        if unknown_fields is not None:
            self.unknown_fields = unknown_fields
        if initialized is not None:
            self.initialized = initialized

    @property
    def idempotency_level(self):
        """Gets the idempotency_level of this MethodOptionsOrBuilder.  # noqa: E501


        :return: The idempotency_level of this MethodOptionsOrBuilder.  # noqa: E501
        :rtype: str
        """
        return self._idempotency_level

    @idempotency_level.setter
    def idempotency_level(self, idempotency_level):
        """Sets the idempotency_level of this MethodOptionsOrBuilder.


        :param idempotency_level: The idempotency_level of this MethodOptionsOrBuilder.  # noqa: E501
        :type: str
        """
        allowed_values = ["IDEMPOTENCY_UNKNOWN", "NO_SIDE_EFFECTS", "IDEMPOTENT"]  # noqa: E501
        if idempotency_level not in allowed_values:
            raise ValueError(
                "Invalid value for `idempotency_level` ({0}), must be one of {1}"  # noqa: E501
                .format(idempotency_level, allowed_values)
            )

        self._idempotency_level = idempotency_level

    @property
    def uninterpreted_option_count(self):
        """Gets the uninterpreted_option_count of this MethodOptionsOrBuilder.  # noqa: E501


        :return: The uninterpreted_option_count of this MethodOptionsOrBuilder.  # noqa: E501
        :rtype: int
        """
        return self._uninterpreted_option_count

    @uninterpreted_option_count.setter
    def uninterpreted_option_count(self, uninterpreted_option_count):
        """Sets the uninterpreted_option_count of this MethodOptionsOrBuilder.


        :param uninterpreted_option_count: The uninterpreted_option_count of this MethodOptionsOrBuilder.  # noqa: E501
        :type: int
        """

        self._uninterpreted_option_count = uninterpreted_option_count

    @property
    def deprecated(self):
        """Gets the deprecated of this MethodOptionsOrBuilder.  # noqa: E501


        :return: The deprecated of this MethodOptionsOrBuilder.  # noqa: E501
        :rtype: bool
        """
        return self._deprecated

    @deprecated.setter
    def deprecated(self, deprecated):
        """Sets the deprecated of this MethodOptionsOrBuilder.


        :param deprecated: The deprecated of this MethodOptionsOrBuilder.  # noqa: E501
        :type: bool
        """

        self._deprecated = deprecated

    @property
    def uninterpreted_option_list(self):
        """Gets the uninterpreted_option_list of this MethodOptionsOrBuilder.  # noqa: E501


        :return: The uninterpreted_option_list of this MethodOptionsOrBuilder.  # noqa: E501
        :rtype: list[UninterpretedOption]
        """
        return self._uninterpreted_option_list

    @uninterpreted_option_list.setter
    def uninterpreted_option_list(self, uninterpreted_option_list):
        """Sets the uninterpreted_option_list of this MethodOptionsOrBuilder.


        :param uninterpreted_option_list: The uninterpreted_option_list of this MethodOptionsOrBuilder.  # noqa: E501
        :type: list[UninterpretedOption]
        """

        self._uninterpreted_option_list = uninterpreted_option_list

    @property
    def uninterpreted_option_or_builder_list(self):
        """Gets the uninterpreted_option_or_builder_list of this MethodOptionsOrBuilder.  # noqa: E501


        :return: The uninterpreted_option_or_builder_list of this MethodOptionsOrBuilder.  # noqa: E501
        :rtype: list[UninterpretedOptionOrBuilder]
        """
        return self._uninterpreted_option_or_builder_list

    @uninterpreted_option_or_builder_list.setter
    def uninterpreted_option_or_builder_list(self, uninterpreted_option_or_builder_list):
        """Sets the uninterpreted_option_or_builder_list of this MethodOptionsOrBuilder.


        :param uninterpreted_option_or_builder_list: The uninterpreted_option_or_builder_list of this MethodOptionsOrBuilder.  # noqa: E501
        :type: list[UninterpretedOptionOrBuilder]
        """

        self._uninterpreted_option_or_builder_list = uninterpreted_option_or_builder_list

    @property
    def default_instance_for_type(self):
        """Gets the default_instance_for_type of this MethodOptionsOrBuilder.  # noqa: E501


        :return: The default_instance_for_type of this MethodOptionsOrBuilder.  # noqa: E501
        :rtype: Message
        """
        return self._default_instance_for_type

    @default_instance_for_type.setter
    def default_instance_for_type(self, default_instance_for_type):
        """Sets the default_instance_for_type of this MethodOptionsOrBuilder.


        :param default_instance_for_type: The default_instance_for_type of this MethodOptionsOrBuilder.  # noqa: E501
        :type: Message
        """

        self._default_instance_for_type = default_instance_for_type

    @property
    def all_fields(self):
        """Gets the all_fields of this MethodOptionsOrBuilder.  # noqa: E501


        :return: The all_fields of this MethodOptionsOrBuilder.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._all_fields

    @all_fields.setter
    def all_fields(self, all_fields):
        """Sets the all_fields of this MethodOptionsOrBuilder.


        :param all_fields: The all_fields of this MethodOptionsOrBuilder.  # noqa: E501
        :type: dict(str, object)
        """

        self._all_fields = all_fields

    @property
    def descriptor_for_type(self):
        """Gets the descriptor_for_type of this MethodOptionsOrBuilder.  # noqa: E501


        :return: The descriptor_for_type of this MethodOptionsOrBuilder.  # noqa: E501
        :rtype: Descriptor
        """
        return self._descriptor_for_type

    @descriptor_for_type.setter
    def descriptor_for_type(self, descriptor_for_type):
        """Sets the descriptor_for_type of this MethodOptionsOrBuilder.


        :param descriptor_for_type: The descriptor_for_type of this MethodOptionsOrBuilder.  # noqa: E501
        :type: Descriptor
        """

        self._descriptor_for_type = descriptor_for_type

    @property
    def initialization_error_string(self):
        """Gets the initialization_error_string of this MethodOptionsOrBuilder.  # noqa: E501


        :return: The initialization_error_string of this MethodOptionsOrBuilder.  # noqa: E501
        :rtype: str
        """
        return self._initialization_error_string

    @initialization_error_string.setter
    def initialization_error_string(self, initialization_error_string):
        """Sets the initialization_error_string of this MethodOptionsOrBuilder.


        :param initialization_error_string: The initialization_error_string of this MethodOptionsOrBuilder.  # noqa: E501
        :type: str
        """

        self._initialization_error_string = initialization_error_string

    @property
    def unknown_fields(self):
        """Gets the unknown_fields of this MethodOptionsOrBuilder.  # noqa: E501


        :return: The unknown_fields of this MethodOptionsOrBuilder.  # noqa: E501
        :rtype: UnknownFieldSet
        """
        return self._unknown_fields

    @unknown_fields.setter
    def unknown_fields(self, unknown_fields):
        """Sets the unknown_fields of this MethodOptionsOrBuilder.


        :param unknown_fields: The unknown_fields of this MethodOptionsOrBuilder.  # noqa: E501
        :type: UnknownFieldSet
        """

        self._unknown_fields = unknown_fields

    @property
    def initialized(self):
        """Gets the initialized of this MethodOptionsOrBuilder.  # noqa: E501


        :return: The initialized of this MethodOptionsOrBuilder.  # noqa: E501
        :rtype: bool
        """
        return self._initialized

    @initialized.setter
    def initialized(self, initialized):
        """Sets the initialized of this MethodOptionsOrBuilder.


        :param initialized: The initialized of this MethodOptionsOrBuilder.  # noqa: E501
        :type: bool
        """

        self._initialized = initialized

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
        if issubclass(MethodOptionsOrBuilder, dict):
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
        if not isinstance(other, MethodOptionsOrBuilder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
