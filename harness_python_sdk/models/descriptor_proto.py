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

class DescriptorProto(object):
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
        'name': 'str',
        'initialized': 'bool',
        'options': 'MessageOptions',
        'field_count': 'int',
        'reserved_range_list': 'list[ReservedRange]',
        'reserved_name_list': 'list[str]',
        'extension_range_list': 'list[ExtensionRange]',
        'oneof_decl_count': 'int',
        'nested_type_count': 'int',
        'extension_range_count': 'int',
        'serialized_size': 'int',
        'parser_for_type': 'ParserDescriptorProto',
        'enum_type_count': 'int',
        'extension_count': 'int',
        'default_instance_for_type': 'DescriptorProto',
        'enum_type_list': 'list[EnumDescriptorProto]',
        'enum_type_or_builder_list': 'list[EnumDescriptorProtoOrBuilder]',
        'extension_list': 'list[FieldDescriptorProto]',
        'extension_or_builder_list': 'list[FieldDescriptorProtoOrBuilder]',
        'options_or_builder': 'MessageOptionsOrBuilder',
        'name_bytes': 'ByteString',
        'field_list': 'list[FieldDescriptorProto]',
        'field_or_builder_list': 'list[FieldDescriptorProtoOrBuilder]',
        'nested_type_list': 'list[DescriptorProto]',
        'nested_type_or_builder_list': 'list[DescriptorProtoOrBuilder]',
        'extension_range_or_builder_list': 'list[ExtensionRangeOrBuilder]',
        'oneof_decl_list': 'list[OneofDescriptorProto]',
        'oneof_decl_or_builder_list': 'list[OneofDescriptorProtoOrBuilder]',
        'reserved_range_count': 'int',
        'reserved_range_or_builder_list': 'list[ReservedRangeOrBuilder]',
        'reserved_name_count': 'int',
        'all_fields': 'dict(str, object)',
        'descriptor_for_type': 'Descriptor',
        'initialization_error_string': 'str',
        'memoized_serialized_size': 'int'
    }

    attribute_map = {
        'unknown_fields': 'unknownFields',
        'name': 'name',
        'initialized': 'initialized',
        'options': 'options',
        'field_count': 'fieldCount',
        'reserved_range_list': 'reservedRangeList',
        'reserved_name_list': 'reservedNameList',
        'extension_range_list': 'extensionRangeList',
        'oneof_decl_count': 'oneofDeclCount',
        'nested_type_count': 'nestedTypeCount',
        'extension_range_count': 'extensionRangeCount',
        'serialized_size': 'serializedSize',
        'parser_for_type': 'parserForType',
        'enum_type_count': 'enumTypeCount',
        'extension_count': 'extensionCount',
        'default_instance_for_type': 'defaultInstanceForType',
        'enum_type_list': 'enumTypeList',
        'enum_type_or_builder_list': 'enumTypeOrBuilderList',
        'extension_list': 'extensionList',
        'extension_or_builder_list': 'extensionOrBuilderList',
        'options_or_builder': 'optionsOrBuilder',
        'name_bytes': 'nameBytes',
        'field_list': 'fieldList',
        'field_or_builder_list': 'fieldOrBuilderList',
        'nested_type_list': 'nestedTypeList',
        'nested_type_or_builder_list': 'nestedTypeOrBuilderList',
        'extension_range_or_builder_list': 'extensionRangeOrBuilderList',
        'oneof_decl_list': 'oneofDeclList',
        'oneof_decl_or_builder_list': 'oneofDeclOrBuilderList',
        'reserved_range_count': 'reservedRangeCount',
        'reserved_range_or_builder_list': 'reservedRangeOrBuilderList',
        'reserved_name_count': 'reservedNameCount',
        'all_fields': 'allFields',
        'descriptor_for_type': 'descriptorForType',
        'initialization_error_string': 'initializationErrorString',
        'memoized_serialized_size': 'memoizedSerializedSize'
    }

    def __init__(self, unknown_fields=None, name=None, initialized=None, options=None, field_count=None, reserved_range_list=None, reserved_name_list=None, extension_range_list=None, oneof_decl_count=None, nested_type_count=None, extension_range_count=None, serialized_size=None, parser_for_type=None, enum_type_count=None, extension_count=None, default_instance_for_type=None, enum_type_list=None, enum_type_or_builder_list=None, extension_list=None, extension_or_builder_list=None, options_or_builder=None, name_bytes=None, field_list=None, field_or_builder_list=None, nested_type_list=None, nested_type_or_builder_list=None, extension_range_or_builder_list=None, oneof_decl_list=None, oneof_decl_or_builder_list=None, reserved_range_count=None, reserved_range_or_builder_list=None, reserved_name_count=None, all_fields=None, descriptor_for_type=None, initialization_error_string=None, memoized_serialized_size=None):  # noqa: E501
        """DescriptorProto - a model defined in Swagger"""  # noqa: E501
        self._unknown_fields = None
        self._name = None
        self._initialized = None
        self._options = None
        self._field_count = None
        self._reserved_range_list = None
        self._reserved_name_list = None
        self._extension_range_list = None
        self._oneof_decl_count = None
        self._nested_type_count = None
        self._extension_range_count = None
        self._serialized_size = None
        self._parser_for_type = None
        self._enum_type_count = None
        self._extension_count = None
        self._default_instance_for_type = None
        self._enum_type_list = None
        self._enum_type_or_builder_list = None
        self._extension_list = None
        self._extension_or_builder_list = None
        self._options_or_builder = None
        self._name_bytes = None
        self._field_list = None
        self._field_or_builder_list = None
        self._nested_type_list = None
        self._nested_type_or_builder_list = None
        self._extension_range_or_builder_list = None
        self._oneof_decl_list = None
        self._oneof_decl_or_builder_list = None
        self._reserved_range_count = None
        self._reserved_range_or_builder_list = None
        self._reserved_name_count = None
        self._all_fields = None
        self._descriptor_for_type = None
        self._initialization_error_string = None
        self._memoized_serialized_size = None
        self.discriminator = None
        if unknown_fields is not None:
            self.unknown_fields = unknown_fields
        if name is not None:
            self.name = name
        if initialized is not None:
            self.initialized = initialized
        if options is not None:
            self.options = options
        if field_count is not None:
            self.field_count = field_count
        if reserved_range_list is not None:
            self.reserved_range_list = reserved_range_list
        if reserved_name_list is not None:
            self.reserved_name_list = reserved_name_list
        if extension_range_list is not None:
            self.extension_range_list = extension_range_list
        if oneof_decl_count is not None:
            self.oneof_decl_count = oneof_decl_count
        if nested_type_count is not None:
            self.nested_type_count = nested_type_count
        if extension_range_count is not None:
            self.extension_range_count = extension_range_count
        if serialized_size is not None:
            self.serialized_size = serialized_size
        if parser_for_type is not None:
            self.parser_for_type = parser_for_type
        if enum_type_count is not None:
            self.enum_type_count = enum_type_count
        if extension_count is not None:
            self.extension_count = extension_count
        if default_instance_for_type is not None:
            self.default_instance_for_type = default_instance_for_type
        if enum_type_list is not None:
            self.enum_type_list = enum_type_list
        if enum_type_or_builder_list is not None:
            self.enum_type_or_builder_list = enum_type_or_builder_list
        if extension_list is not None:
            self.extension_list = extension_list
        if extension_or_builder_list is not None:
            self.extension_or_builder_list = extension_or_builder_list
        if options_or_builder is not None:
            self.options_or_builder = options_or_builder
        if name_bytes is not None:
            self.name_bytes = name_bytes
        if field_list is not None:
            self.field_list = field_list
        if field_or_builder_list is not None:
            self.field_or_builder_list = field_or_builder_list
        if nested_type_list is not None:
            self.nested_type_list = nested_type_list
        if nested_type_or_builder_list is not None:
            self.nested_type_or_builder_list = nested_type_or_builder_list
        if extension_range_or_builder_list is not None:
            self.extension_range_or_builder_list = extension_range_or_builder_list
        if oneof_decl_list is not None:
            self.oneof_decl_list = oneof_decl_list
        if oneof_decl_or_builder_list is not None:
            self.oneof_decl_or_builder_list = oneof_decl_or_builder_list
        if reserved_range_count is not None:
            self.reserved_range_count = reserved_range_count
        if reserved_range_or_builder_list is not None:
            self.reserved_range_or_builder_list = reserved_range_or_builder_list
        if reserved_name_count is not None:
            self.reserved_name_count = reserved_name_count
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
        """Gets the unknown_fields of this DescriptorProto.  # noqa: E501


        :return: The unknown_fields of this DescriptorProto.  # noqa: E501
        :rtype: UnknownFieldSet
        """
        return self._unknown_fields

    @unknown_fields.setter
    def unknown_fields(self, unknown_fields):
        """Sets the unknown_fields of this DescriptorProto.


        :param unknown_fields: The unknown_fields of this DescriptorProto.  # noqa: E501
        :type: UnknownFieldSet
        """

        self._unknown_fields = unknown_fields

    @property
    def name(self):
        """Gets the name of this DescriptorProto.  # noqa: E501


        :return: The name of this DescriptorProto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DescriptorProto.


        :param name: The name of this DescriptorProto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def initialized(self):
        """Gets the initialized of this DescriptorProto.  # noqa: E501


        :return: The initialized of this DescriptorProto.  # noqa: E501
        :rtype: bool
        """
        return self._initialized

    @initialized.setter
    def initialized(self, initialized):
        """Sets the initialized of this DescriptorProto.


        :param initialized: The initialized of this DescriptorProto.  # noqa: E501
        :type: bool
        """

        self._initialized = initialized

    @property
    def options(self):
        """Gets the options of this DescriptorProto.  # noqa: E501


        :return: The options of this DescriptorProto.  # noqa: E501
        :rtype: MessageOptions
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this DescriptorProto.


        :param options: The options of this DescriptorProto.  # noqa: E501
        :type: MessageOptions
        """

        self._options = options

    @property
    def field_count(self):
        """Gets the field_count of this DescriptorProto.  # noqa: E501


        :return: The field_count of this DescriptorProto.  # noqa: E501
        :rtype: int
        """
        return self._field_count

    @field_count.setter
    def field_count(self, field_count):
        """Sets the field_count of this DescriptorProto.


        :param field_count: The field_count of this DescriptorProto.  # noqa: E501
        :type: int
        """

        self._field_count = field_count

    @property
    def reserved_range_list(self):
        """Gets the reserved_range_list of this DescriptorProto.  # noqa: E501


        :return: The reserved_range_list of this DescriptorProto.  # noqa: E501
        :rtype: list[ReservedRange]
        """
        return self._reserved_range_list

    @reserved_range_list.setter
    def reserved_range_list(self, reserved_range_list):
        """Sets the reserved_range_list of this DescriptorProto.


        :param reserved_range_list: The reserved_range_list of this DescriptorProto.  # noqa: E501
        :type: list[ReservedRange]
        """

        self._reserved_range_list = reserved_range_list

    @property
    def reserved_name_list(self):
        """Gets the reserved_name_list of this DescriptorProto.  # noqa: E501


        :return: The reserved_name_list of this DescriptorProto.  # noqa: E501
        :rtype: list[str]
        """
        return self._reserved_name_list

    @reserved_name_list.setter
    def reserved_name_list(self, reserved_name_list):
        """Sets the reserved_name_list of this DescriptorProto.


        :param reserved_name_list: The reserved_name_list of this DescriptorProto.  # noqa: E501
        :type: list[str]
        """

        self._reserved_name_list = reserved_name_list

    @property
    def extension_range_list(self):
        """Gets the extension_range_list of this DescriptorProto.  # noqa: E501


        :return: The extension_range_list of this DescriptorProto.  # noqa: E501
        :rtype: list[ExtensionRange]
        """
        return self._extension_range_list

    @extension_range_list.setter
    def extension_range_list(self, extension_range_list):
        """Sets the extension_range_list of this DescriptorProto.


        :param extension_range_list: The extension_range_list of this DescriptorProto.  # noqa: E501
        :type: list[ExtensionRange]
        """

        self._extension_range_list = extension_range_list

    @property
    def oneof_decl_count(self):
        """Gets the oneof_decl_count of this DescriptorProto.  # noqa: E501


        :return: The oneof_decl_count of this DescriptorProto.  # noqa: E501
        :rtype: int
        """
        return self._oneof_decl_count

    @oneof_decl_count.setter
    def oneof_decl_count(self, oneof_decl_count):
        """Sets the oneof_decl_count of this DescriptorProto.


        :param oneof_decl_count: The oneof_decl_count of this DescriptorProto.  # noqa: E501
        :type: int
        """

        self._oneof_decl_count = oneof_decl_count

    @property
    def nested_type_count(self):
        """Gets the nested_type_count of this DescriptorProto.  # noqa: E501


        :return: The nested_type_count of this DescriptorProto.  # noqa: E501
        :rtype: int
        """
        return self._nested_type_count

    @nested_type_count.setter
    def nested_type_count(self, nested_type_count):
        """Sets the nested_type_count of this DescriptorProto.


        :param nested_type_count: The nested_type_count of this DescriptorProto.  # noqa: E501
        :type: int
        """

        self._nested_type_count = nested_type_count

    @property
    def extension_range_count(self):
        """Gets the extension_range_count of this DescriptorProto.  # noqa: E501


        :return: The extension_range_count of this DescriptorProto.  # noqa: E501
        :rtype: int
        """
        return self._extension_range_count

    @extension_range_count.setter
    def extension_range_count(self, extension_range_count):
        """Sets the extension_range_count of this DescriptorProto.


        :param extension_range_count: The extension_range_count of this DescriptorProto.  # noqa: E501
        :type: int
        """

        self._extension_range_count = extension_range_count

    @property
    def serialized_size(self):
        """Gets the serialized_size of this DescriptorProto.  # noqa: E501


        :return: The serialized_size of this DescriptorProto.  # noqa: E501
        :rtype: int
        """
        return self._serialized_size

    @serialized_size.setter
    def serialized_size(self, serialized_size):
        """Sets the serialized_size of this DescriptorProto.


        :param serialized_size: The serialized_size of this DescriptorProto.  # noqa: E501
        :type: int
        """

        self._serialized_size = serialized_size

    @property
    def parser_for_type(self):
        """Gets the parser_for_type of this DescriptorProto.  # noqa: E501


        :return: The parser_for_type of this DescriptorProto.  # noqa: E501
        :rtype: ParserDescriptorProto
        """
        return self._parser_for_type

    @parser_for_type.setter
    def parser_for_type(self, parser_for_type):
        """Sets the parser_for_type of this DescriptorProto.


        :param parser_for_type: The parser_for_type of this DescriptorProto.  # noqa: E501
        :type: ParserDescriptorProto
        """

        self._parser_for_type = parser_for_type

    @property
    def enum_type_count(self):
        """Gets the enum_type_count of this DescriptorProto.  # noqa: E501


        :return: The enum_type_count of this DescriptorProto.  # noqa: E501
        :rtype: int
        """
        return self._enum_type_count

    @enum_type_count.setter
    def enum_type_count(self, enum_type_count):
        """Sets the enum_type_count of this DescriptorProto.


        :param enum_type_count: The enum_type_count of this DescriptorProto.  # noqa: E501
        :type: int
        """

        self._enum_type_count = enum_type_count

    @property
    def extension_count(self):
        """Gets the extension_count of this DescriptorProto.  # noqa: E501


        :return: The extension_count of this DescriptorProto.  # noqa: E501
        :rtype: int
        """
        return self._extension_count

    @extension_count.setter
    def extension_count(self, extension_count):
        """Sets the extension_count of this DescriptorProto.


        :param extension_count: The extension_count of this DescriptorProto.  # noqa: E501
        :type: int
        """

        self._extension_count = extension_count

    @property
    def default_instance_for_type(self):
        """Gets the default_instance_for_type of this DescriptorProto.  # noqa: E501


        :return: The default_instance_for_type of this DescriptorProto.  # noqa: E501
        :rtype: DescriptorProto
        """
        return self._default_instance_for_type

    @default_instance_for_type.setter
    def default_instance_for_type(self, default_instance_for_type):
        """Sets the default_instance_for_type of this DescriptorProto.


        :param default_instance_for_type: The default_instance_for_type of this DescriptorProto.  # noqa: E501
        :type: DescriptorProto
        """

        self._default_instance_for_type = default_instance_for_type

    @property
    def enum_type_list(self):
        """Gets the enum_type_list of this DescriptorProto.  # noqa: E501


        :return: The enum_type_list of this DescriptorProto.  # noqa: E501
        :rtype: list[EnumDescriptorProto]
        """
        return self._enum_type_list

    @enum_type_list.setter
    def enum_type_list(self, enum_type_list):
        """Sets the enum_type_list of this DescriptorProto.


        :param enum_type_list: The enum_type_list of this DescriptorProto.  # noqa: E501
        :type: list[EnumDescriptorProto]
        """

        self._enum_type_list = enum_type_list

    @property
    def enum_type_or_builder_list(self):
        """Gets the enum_type_or_builder_list of this DescriptorProto.  # noqa: E501


        :return: The enum_type_or_builder_list of this DescriptorProto.  # noqa: E501
        :rtype: list[EnumDescriptorProtoOrBuilder]
        """
        return self._enum_type_or_builder_list

    @enum_type_or_builder_list.setter
    def enum_type_or_builder_list(self, enum_type_or_builder_list):
        """Sets the enum_type_or_builder_list of this DescriptorProto.


        :param enum_type_or_builder_list: The enum_type_or_builder_list of this DescriptorProto.  # noqa: E501
        :type: list[EnumDescriptorProtoOrBuilder]
        """

        self._enum_type_or_builder_list = enum_type_or_builder_list

    @property
    def extension_list(self):
        """Gets the extension_list of this DescriptorProto.  # noqa: E501


        :return: The extension_list of this DescriptorProto.  # noqa: E501
        :rtype: list[FieldDescriptorProto]
        """
        return self._extension_list

    @extension_list.setter
    def extension_list(self, extension_list):
        """Sets the extension_list of this DescriptorProto.


        :param extension_list: The extension_list of this DescriptorProto.  # noqa: E501
        :type: list[FieldDescriptorProto]
        """

        self._extension_list = extension_list

    @property
    def extension_or_builder_list(self):
        """Gets the extension_or_builder_list of this DescriptorProto.  # noqa: E501


        :return: The extension_or_builder_list of this DescriptorProto.  # noqa: E501
        :rtype: list[FieldDescriptorProtoOrBuilder]
        """
        return self._extension_or_builder_list

    @extension_or_builder_list.setter
    def extension_or_builder_list(self, extension_or_builder_list):
        """Sets the extension_or_builder_list of this DescriptorProto.


        :param extension_or_builder_list: The extension_or_builder_list of this DescriptorProto.  # noqa: E501
        :type: list[FieldDescriptorProtoOrBuilder]
        """

        self._extension_or_builder_list = extension_or_builder_list

    @property
    def options_or_builder(self):
        """Gets the options_or_builder of this DescriptorProto.  # noqa: E501


        :return: The options_or_builder of this DescriptorProto.  # noqa: E501
        :rtype: MessageOptionsOrBuilder
        """
        return self._options_or_builder

    @options_or_builder.setter
    def options_or_builder(self, options_or_builder):
        """Sets the options_or_builder of this DescriptorProto.


        :param options_or_builder: The options_or_builder of this DescriptorProto.  # noqa: E501
        :type: MessageOptionsOrBuilder
        """

        self._options_or_builder = options_or_builder

    @property
    def name_bytes(self):
        """Gets the name_bytes of this DescriptorProto.  # noqa: E501


        :return: The name_bytes of this DescriptorProto.  # noqa: E501
        :rtype: ByteString
        """
        return self._name_bytes

    @name_bytes.setter
    def name_bytes(self, name_bytes):
        """Sets the name_bytes of this DescriptorProto.


        :param name_bytes: The name_bytes of this DescriptorProto.  # noqa: E501
        :type: ByteString
        """

        self._name_bytes = name_bytes

    @property
    def field_list(self):
        """Gets the field_list of this DescriptorProto.  # noqa: E501


        :return: The field_list of this DescriptorProto.  # noqa: E501
        :rtype: list[FieldDescriptorProto]
        """
        return self._field_list

    @field_list.setter
    def field_list(self, field_list):
        """Sets the field_list of this DescriptorProto.


        :param field_list: The field_list of this DescriptorProto.  # noqa: E501
        :type: list[FieldDescriptorProto]
        """

        self._field_list = field_list

    @property
    def field_or_builder_list(self):
        """Gets the field_or_builder_list of this DescriptorProto.  # noqa: E501


        :return: The field_or_builder_list of this DescriptorProto.  # noqa: E501
        :rtype: list[FieldDescriptorProtoOrBuilder]
        """
        return self._field_or_builder_list

    @field_or_builder_list.setter
    def field_or_builder_list(self, field_or_builder_list):
        """Sets the field_or_builder_list of this DescriptorProto.


        :param field_or_builder_list: The field_or_builder_list of this DescriptorProto.  # noqa: E501
        :type: list[FieldDescriptorProtoOrBuilder]
        """

        self._field_or_builder_list = field_or_builder_list

    @property
    def nested_type_list(self):
        """Gets the nested_type_list of this DescriptorProto.  # noqa: E501


        :return: The nested_type_list of this DescriptorProto.  # noqa: E501
        :rtype: list[DescriptorProto]
        """
        return self._nested_type_list

    @nested_type_list.setter
    def nested_type_list(self, nested_type_list):
        """Sets the nested_type_list of this DescriptorProto.


        :param nested_type_list: The nested_type_list of this DescriptorProto.  # noqa: E501
        :type: list[DescriptorProto]
        """

        self._nested_type_list = nested_type_list

    @property
    def nested_type_or_builder_list(self):
        """Gets the nested_type_or_builder_list of this DescriptorProto.  # noqa: E501


        :return: The nested_type_or_builder_list of this DescriptorProto.  # noqa: E501
        :rtype: list[DescriptorProtoOrBuilder]
        """
        return self._nested_type_or_builder_list

    @nested_type_or_builder_list.setter
    def nested_type_or_builder_list(self, nested_type_or_builder_list):
        """Sets the nested_type_or_builder_list of this DescriptorProto.


        :param nested_type_or_builder_list: The nested_type_or_builder_list of this DescriptorProto.  # noqa: E501
        :type: list[DescriptorProtoOrBuilder]
        """

        self._nested_type_or_builder_list = nested_type_or_builder_list

    @property
    def extension_range_or_builder_list(self):
        """Gets the extension_range_or_builder_list of this DescriptorProto.  # noqa: E501


        :return: The extension_range_or_builder_list of this DescriptorProto.  # noqa: E501
        :rtype: list[ExtensionRangeOrBuilder]
        """
        return self._extension_range_or_builder_list

    @extension_range_or_builder_list.setter
    def extension_range_or_builder_list(self, extension_range_or_builder_list):
        """Sets the extension_range_or_builder_list of this DescriptorProto.


        :param extension_range_or_builder_list: The extension_range_or_builder_list of this DescriptorProto.  # noqa: E501
        :type: list[ExtensionRangeOrBuilder]
        """

        self._extension_range_or_builder_list = extension_range_or_builder_list

    @property
    def oneof_decl_list(self):
        """Gets the oneof_decl_list of this DescriptorProto.  # noqa: E501


        :return: The oneof_decl_list of this DescriptorProto.  # noqa: E501
        :rtype: list[OneofDescriptorProto]
        """
        return self._oneof_decl_list

    @oneof_decl_list.setter
    def oneof_decl_list(self, oneof_decl_list):
        """Sets the oneof_decl_list of this DescriptorProto.


        :param oneof_decl_list: The oneof_decl_list of this DescriptorProto.  # noqa: E501
        :type: list[OneofDescriptorProto]
        """

        self._oneof_decl_list = oneof_decl_list

    @property
    def oneof_decl_or_builder_list(self):
        """Gets the oneof_decl_or_builder_list of this DescriptorProto.  # noqa: E501


        :return: The oneof_decl_or_builder_list of this DescriptorProto.  # noqa: E501
        :rtype: list[OneofDescriptorProtoOrBuilder]
        """
        return self._oneof_decl_or_builder_list

    @oneof_decl_or_builder_list.setter
    def oneof_decl_or_builder_list(self, oneof_decl_or_builder_list):
        """Sets the oneof_decl_or_builder_list of this DescriptorProto.


        :param oneof_decl_or_builder_list: The oneof_decl_or_builder_list of this DescriptorProto.  # noqa: E501
        :type: list[OneofDescriptorProtoOrBuilder]
        """

        self._oneof_decl_or_builder_list = oneof_decl_or_builder_list

    @property
    def reserved_range_count(self):
        """Gets the reserved_range_count of this DescriptorProto.  # noqa: E501


        :return: The reserved_range_count of this DescriptorProto.  # noqa: E501
        :rtype: int
        """
        return self._reserved_range_count

    @reserved_range_count.setter
    def reserved_range_count(self, reserved_range_count):
        """Sets the reserved_range_count of this DescriptorProto.


        :param reserved_range_count: The reserved_range_count of this DescriptorProto.  # noqa: E501
        :type: int
        """

        self._reserved_range_count = reserved_range_count

    @property
    def reserved_range_or_builder_list(self):
        """Gets the reserved_range_or_builder_list of this DescriptorProto.  # noqa: E501


        :return: The reserved_range_or_builder_list of this DescriptorProto.  # noqa: E501
        :rtype: list[ReservedRangeOrBuilder]
        """
        return self._reserved_range_or_builder_list

    @reserved_range_or_builder_list.setter
    def reserved_range_or_builder_list(self, reserved_range_or_builder_list):
        """Sets the reserved_range_or_builder_list of this DescriptorProto.


        :param reserved_range_or_builder_list: The reserved_range_or_builder_list of this DescriptorProto.  # noqa: E501
        :type: list[ReservedRangeOrBuilder]
        """

        self._reserved_range_or_builder_list = reserved_range_or_builder_list

    @property
    def reserved_name_count(self):
        """Gets the reserved_name_count of this DescriptorProto.  # noqa: E501


        :return: The reserved_name_count of this DescriptorProto.  # noqa: E501
        :rtype: int
        """
        return self._reserved_name_count

    @reserved_name_count.setter
    def reserved_name_count(self, reserved_name_count):
        """Sets the reserved_name_count of this DescriptorProto.


        :param reserved_name_count: The reserved_name_count of this DescriptorProto.  # noqa: E501
        :type: int
        """

        self._reserved_name_count = reserved_name_count

    @property
    def all_fields(self):
        """Gets the all_fields of this DescriptorProto.  # noqa: E501


        :return: The all_fields of this DescriptorProto.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._all_fields

    @all_fields.setter
    def all_fields(self, all_fields):
        """Sets the all_fields of this DescriptorProto.


        :param all_fields: The all_fields of this DescriptorProto.  # noqa: E501
        :type: dict(str, object)
        """

        self._all_fields = all_fields

    @property
    def descriptor_for_type(self):
        """Gets the descriptor_for_type of this DescriptorProto.  # noqa: E501


        :return: The descriptor_for_type of this DescriptorProto.  # noqa: E501
        :rtype: Descriptor
        """
        return self._descriptor_for_type

    @descriptor_for_type.setter
    def descriptor_for_type(self, descriptor_for_type):
        """Sets the descriptor_for_type of this DescriptorProto.


        :param descriptor_for_type: The descriptor_for_type of this DescriptorProto.  # noqa: E501
        :type: Descriptor
        """

        self._descriptor_for_type = descriptor_for_type

    @property
    def initialization_error_string(self):
        """Gets the initialization_error_string of this DescriptorProto.  # noqa: E501


        :return: The initialization_error_string of this DescriptorProto.  # noqa: E501
        :rtype: str
        """
        return self._initialization_error_string

    @initialization_error_string.setter
    def initialization_error_string(self, initialization_error_string):
        """Sets the initialization_error_string of this DescriptorProto.


        :param initialization_error_string: The initialization_error_string of this DescriptorProto.  # noqa: E501
        :type: str
        """

        self._initialization_error_string = initialization_error_string

    @property
    def memoized_serialized_size(self):
        """Gets the memoized_serialized_size of this DescriptorProto.  # noqa: E501


        :return: The memoized_serialized_size of this DescriptorProto.  # noqa: E501
        :rtype: int
        """
        return self._memoized_serialized_size

    @memoized_serialized_size.setter
    def memoized_serialized_size(self, memoized_serialized_size):
        """Sets the memoized_serialized_size of this DescriptorProto.


        :param memoized_serialized_size: The memoized_serialized_size of this DescriptorProto.  # noqa: E501
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
        if issubclass(DescriptorProto, dict):
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
        if not isinstance(other, DescriptorProto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
