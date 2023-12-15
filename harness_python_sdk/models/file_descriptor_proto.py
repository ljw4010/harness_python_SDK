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

class FileDescriptorProto(object):
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
        'package': 'str',
        'initialized': 'bool',
        'options': 'FileOptions',
        'syntax': 'str',
        'serialized_size': 'int',
        'parser_for_type': 'ParserFileDescriptorProto',
        'public_dependency_count': 'int',
        'dependency_count': 'int',
        'message_type_count': 'int',
        'enum_type_count': 'int',
        'service_count': 'int',
        'extension_count': 'int',
        'default_instance_for_type': 'FileDescriptorProto',
        'package_bytes': 'ByteString',
        'dependency_list': 'list[str]',
        'public_dependency_list': 'list[int]',
        'weak_dependency_list': 'list[int]',
        'weak_dependency_count': 'int',
        'message_type_list': 'list[DescriptorProto]',
        'message_type_or_builder_list': 'list[DescriptorProtoOrBuilder]',
        'enum_type_list': 'list[EnumDescriptorProto]',
        'enum_type_or_builder_list': 'list[EnumDescriptorProtoOrBuilder]',
        'service_list': 'list[ServiceDescriptorProto]',
        'service_or_builder_list': 'list[ServiceDescriptorProtoOrBuilder]',
        'extension_list': 'list[FieldDescriptorProto]',
        'extension_or_builder_list': 'list[FieldDescriptorProtoOrBuilder]',
        'options_or_builder': 'FileOptionsOrBuilder',
        'source_code_info': 'SourceCodeInfo',
        'source_code_info_or_builder': 'SourceCodeInfoOrBuilder',
        'syntax_bytes': 'ByteString',
        'name_bytes': 'ByteString',
        'all_fields': 'dict(str, object)',
        'descriptor_for_type': 'Descriptor',
        'initialization_error_string': 'str',
        'memoized_serialized_size': 'int'
    }

    attribute_map = {
        'unknown_fields': 'unknownFields',
        'name': 'name',
        'package': 'package',
        'initialized': 'initialized',
        'options': 'options',
        'syntax': 'syntax',
        'serialized_size': 'serializedSize',
        'parser_for_type': 'parserForType',
        'public_dependency_count': 'publicDependencyCount',
        'dependency_count': 'dependencyCount',
        'message_type_count': 'messageTypeCount',
        'enum_type_count': 'enumTypeCount',
        'service_count': 'serviceCount',
        'extension_count': 'extensionCount',
        'default_instance_for_type': 'defaultInstanceForType',
        'package_bytes': 'packageBytes',
        'dependency_list': 'dependencyList',
        'public_dependency_list': 'publicDependencyList',
        'weak_dependency_list': 'weakDependencyList',
        'weak_dependency_count': 'weakDependencyCount',
        'message_type_list': 'messageTypeList',
        'message_type_or_builder_list': 'messageTypeOrBuilderList',
        'enum_type_list': 'enumTypeList',
        'enum_type_or_builder_list': 'enumTypeOrBuilderList',
        'service_list': 'serviceList',
        'service_or_builder_list': 'serviceOrBuilderList',
        'extension_list': 'extensionList',
        'extension_or_builder_list': 'extensionOrBuilderList',
        'options_or_builder': 'optionsOrBuilder',
        'source_code_info': 'sourceCodeInfo',
        'source_code_info_or_builder': 'sourceCodeInfoOrBuilder',
        'syntax_bytes': 'syntaxBytes',
        'name_bytes': 'nameBytes',
        'all_fields': 'allFields',
        'descriptor_for_type': 'descriptorForType',
        'initialization_error_string': 'initializationErrorString',
        'memoized_serialized_size': 'memoizedSerializedSize'
    }

    def __init__(self, unknown_fields=None, name=None, package=None, initialized=None, options=None, syntax=None, serialized_size=None, parser_for_type=None, public_dependency_count=None, dependency_count=None, message_type_count=None, enum_type_count=None, service_count=None, extension_count=None, default_instance_for_type=None, package_bytes=None, dependency_list=None, public_dependency_list=None, weak_dependency_list=None, weak_dependency_count=None, message_type_list=None, message_type_or_builder_list=None, enum_type_list=None, enum_type_or_builder_list=None, service_list=None, service_or_builder_list=None, extension_list=None, extension_or_builder_list=None, options_or_builder=None, source_code_info=None, source_code_info_or_builder=None, syntax_bytes=None, name_bytes=None, all_fields=None, descriptor_for_type=None, initialization_error_string=None, memoized_serialized_size=None):  # noqa: E501
        """FileDescriptorProto - a model defined in Swagger"""  # noqa: E501
        self._unknown_fields = None
        self._name = None
        self._package = None
        self._initialized = None
        self._options = None
        self._syntax = None
        self._serialized_size = None
        self._parser_for_type = None
        self._public_dependency_count = None
        self._dependency_count = None
        self._message_type_count = None
        self._enum_type_count = None
        self._service_count = None
        self._extension_count = None
        self._default_instance_for_type = None
        self._package_bytes = None
        self._dependency_list = None
        self._public_dependency_list = None
        self._weak_dependency_list = None
        self._weak_dependency_count = None
        self._message_type_list = None
        self._message_type_or_builder_list = None
        self._enum_type_list = None
        self._enum_type_or_builder_list = None
        self._service_list = None
        self._service_or_builder_list = None
        self._extension_list = None
        self._extension_or_builder_list = None
        self._options_or_builder = None
        self._source_code_info = None
        self._source_code_info_or_builder = None
        self._syntax_bytes = None
        self._name_bytes = None
        self._all_fields = None
        self._descriptor_for_type = None
        self._initialization_error_string = None
        self._memoized_serialized_size = None
        self.discriminator = None
        if unknown_fields is not None:
            self.unknown_fields = unknown_fields
        if name is not None:
            self.name = name
        if package is not None:
            self.package = package
        if initialized is not None:
            self.initialized = initialized
        if options is not None:
            self.options = options
        if syntax is not None:
            self.syntax = syntax
        if serialized_size is not None:
            self.serialized_size = serialized_size
        if parser_for_type is not None:
            self.parser_for_type = parser_for_type
        if public_dependency_count is not None:
            self.public_dependency_count = public_dependency_count
        if dependency_count is not None:
            self.dependency_count = dependency_count
        if message_type_count is not None:
            self.message_type_count = message_type_count
        if enum_type_count is not None:
            self.enum_type_count = enum_type_count
        if service_count is not None:
            self.service_count = service_count
        if extension_count is not None:
            self.extension_count = extension_count
        if default_instance_for_type is not None:
            self.default_instance_for_type = default_instance_for_type
        if package_bytes is not None:
            self.package_bytes = package_bytes
        if dependency_list is not None:
            self.dependency_list = dependency_list
        if public_dependency_list is not None:
            self.public_dependency_list = public_dependency_list
        if weak_dependency_list is not None:
            self.weak_dependency_list = weak_dependency_list
        if weak_dependency_count is not None:
            self.weak_dependency_count = weak_dependency_count
        if message_type_list is not None:
            self.message_type_list = message_type_list
        if message_type_or_builder_list is not None:
            self.message_type_or_builder_list = message_type_or_builder_list
        if enum_type_list is not None:
            self.enum_type_list = enum_type_list
        if enum_type_or_builder_list is not None:
            self.enum_type_or_builder_list = enum_type_or_builder_list
        if service_list is not None:
            self.service_list = service_list
        if service_or_builder_list is not None:
            self.service_or_builder_list = service_or_builder_list
        if extension_list is not None:
            self.extension_list = extension_list
        if extension_or_builder_list is not None:
            self.extension_or_builder_list = extension_or_builder_list
        if options_or_builder is not None:
            self.options_or_builder = options_or_builder
        if source_code_info is not None:
            self.source_code_info = source_code_info
        if source_code_info_or_builder is not None:
            self.source_code_info_or_builder = source_code_info_or_builder
        if syntax_bytes is not None:
            self.syntax_bytes = syntax_bytes
        if name_bytes is not None:
            self.name_bytes = name_bytes
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
        """Gets the unknown_fields of this FileDescriptorProto.  # noqa: E501


        :return: The unknown_fields of this FileDescriptorProto.  # noqa: E501
        :rtype: UnknownFieldSet
        """
        return self._unknown_fields

    @unknown_fields.setter
    def unknown_fields(self, unknown_fields):
        """Sets the unknown_fields of this FileDescriptorProto.


        :param unknown_fields: The unknown_fields of this FileDescriptorProto.  # noqa: E501
        :type: UnknownFieldSet
        """

        self._unknown_fields = unknown_fields

    @property
    def name(self):
        """Gets the name of this FileDescriptorProto.  # noqa: E501


        :return: The name of this FileDescriptorProto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FileDescriptorProto.


        :param name: The name of this FileDescriptorProto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def package(self):
        """Gets the package of this FileDescriptorProto.  # noqa: E501


        :return: The package of this FileDescriptorProto.  # noqa: E501
        :rtype: str
        """
        return self._package

    @package.setter
    def package(self, package):
        """Sets the package of this FileDescriptorProto.


        :param package: The package of this FileDescriptorProto.  # noqa: E501
        :type: str
        """

        self._package = package

    @property
    def initialized(self):
        """Gets the initialized of this FileDescriptorProto.  # noqa: E501


        :return: The initialized of this FileDescriptorProto.  # noqa: E501
        :rtype: bool
        """
        return self._initialized

    @initialized.setter
    def initialized(self, initialized):
        """Sets the initialized of this FileDescriptorProto.


        :param initialized: The initialized of this FileDescriptorProto.  # noqa: E501
        :type: bool
        """

        self._initialized = initialized

    @property
    def options(self):
        """Gets the options of this FileDescriptorProto.  # noqa: E501


        :return: The options of this FileDescriptorProto.  # noqa: E501
        :rtype: FileOptions
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this FileDescriptorProto.


        :param options: The options of this FileDescriptorProto.  # noqa: E501
        :type: FileOptions
        """

        self._options = options

    @property
    def syntax(self):
        """Gets the syntax of this FileDescriptorProto.  # noqa: E501


        :return: The syntax of this FileDescriptorProto.  # noqa: E501
        :rtype: str
        """
        return self._syntax

    @syntax.setter
    def syntax(self, syntax):
        """Sets the syntax of this FileDescriptorProto.


        :param syntax: The syntax of this FileDescriptorProto.  # noqa: E501
        :type: str
        """

        self._syntax = syntax

    @property
    def serialized_size(self):
        """Gets the serialized_size of this FileDescriptorProto.  # noqa: E501


        :return: The serialized_size of this FileDescriptorProto.  # noqa: E501
        :rtype: int
        """
        return self._serialized_size

    @serialized_size.setter
    def serialized_size(self, serialized_size):
        """Sets the serialized_size of this FileDescriptorProto.


        :param serialized_size: The serialized_size of this FileDescriptorProto.  # noqa: E501
        :type: int
        """

        self._serialized_size = serialized_size

    @property
    def parser_for_type(self):
        """Gets the parser_for_type of this FileDescriptorProto.  # noqa: E501


        :return: The parser_for_type of this FileDescriptorProto.  # noqa: E501
        :rtype: ParserFileDescriptorProto
        """
        return self._parser_for_type

    @parser_for_type.setter
    def parser_for_type(self, parser_for_type):
        """Sets the parser_for_type of this FileDescriptorProto.


        :param parser_for_type: The parser_for_type of this FileDescriptorProto.  # noqa: E501
        :type: ParserFileDescriptorProto
        """

        self._parser_for_type = parser_for_type

    @property
    def public_dependency_count(self):
        """Gets the public_dependency_count of this FileDescriptorProto.  # noqa: E501


        :return: The public_dependency_count of this FileDescriptorProto.  # noqa: E501
        :rtype: int
        """
        return self._public_dependency_count

    @public_dependency_count.setter
    def public_dependency_count(self, public_dependency_count):
        """Sets the public_dependency_count of this FileDescriptorProto.


        :param public_dependency_count: The public_dependency_count of this FileDescriptorProto.  # noqa: E501
        :type: int
        """

        self._public_dependency_count = public_dependency_count

    @property
    def dependency_count(self):
        """Gets the dependency_count of this FileDescriptorProto.  # noqa: E501


        :return: The dependency_count of this FileDescriptorProto.  # noqa: E501
        :rtype: int
        """
        return self._dependency_count

    @dependency_count.setter
    def dependency_count(self, dependency_count):
        """Sets the dependency_count of this FileDescriptorProto.


        :param dependency_count: The dependency_count of this FileDescriptorProto.  # noqa: E501
        :type: int
        """

        self._dependency_count = dependency_count

    @property
    def message_type_count(self):
        """Gets the message_type_count of this FileDescriptorProto.  # noqa: E501


        :return: The message_type_count of this FileDescriptorProto.  # noqa: E501
        :rtype: int
        """
        return self._message_type_count

    @message_type_count.setter
    def message_type_count(self, message_type_count):
        """Sets the message_type_count of this FileDescriptorProto.


        :param message_type_count: The message_type_count of this FileDescriptorProto.  # noqa: E501
        :type: int
        """

        self._message_type_count = message_type_count

    @property
    def enum_type_count(self):
        """Gets the enum_type_count of this FileDescriptorProto.  # noqa: E501


        :return: The enum_type_count of this FileDescriptorProto.  # noqa: E501
        :rtype: int
        """
        return self._enum_type_count

    @enum_type_count.setter
    def enum_type_count(self, enum_type_count):
        """Sets the enum_type_count of this FileDescriptorProto.


        :param enum_type_count: The enum_type_count of this FileDescriptorProto.  # noqa: E501
        :type: int
        """

        self._enum_type_count = enum_type_count

    @property
    def service_count(self):
        """Gets the service_count of this FileDescriptorProto.  # noqa: E501


        :return: The service_count of this FileDescriptorProto.  # noqa: E501
        :rtype: int
        """
        return self._service_count

    @service_count.setter
    def service_count(self, service_count):
        """Sets the service_count of this FileDescriptorProto.


        :param service_count: The service_count of this FileDescriptorProto.  # noqa: E501
        :type: int
        """

        self._service_count = service_count

    @property
    def extension_count(self):
        """Gets the extension_count of this FileDescriptorProto.  # noqa: E501


        :return: The extension_count of this FileDescriptorProto.  # noqa: E501
        :rtype: int
        """
        return self._extension_count

    @extension_count.setter
    def extension_count(self, extension_count):
        """Sets the extension_count of this FileDescriptorProto.


        :param extension_count: The extension_count of this FileDescriptorProto.  # noqa: E501
        :type: int
        """

        self._extension_count = extension_count

    @property
    def default_instance_for_type(self):
        """Gets the default_instance_for_type of this FileDescriptorProto.  # noqa: E501


        :return: The default_instance_for_type of this FileDescriptorProto.  # noqa: E501
        :rtype: FileDescriptorProto
        """
        return self._default_instance_for_type

    @default_instance_for_type.setter
    def default_instance_for_type(self, default_instance_for_type):
        """Sets the default_instance_for_type of this FileDescriptorProto.


        :param default_instance_for_type: The default_instance_for_type of this FileDescriptorProto.  # noqa: E501
        :type: FileDescriptorProto
        """

        self._default_instance_for_type = default_instance_for_type

    @property
    def package_bytes(self):
        """Gets the package_bytes of this FileDescriptorProto.  # noqa: E501


        :return: The package_bytes of this FileDescriptorProto.  # noqa: E501
        :rtype: ByteString
        """
        return self._package_bytes

    @package_bytes.setter
    def package_bytes(self, package_bytes):
        """Sets the package_bytes of this FileDescriptorProto.


        :param package_bytes: The package_bytes of this FileDescriptorProto.  # noqa: E501
        :type: ByteString
        """

        self._package_bytes = package_bytes

    @property
    def dependency_list(self):
        """Gets the dependency_list of this FileDescriptorProto.  # noqa: E501


        :return: The dependency_list of this FileDescriptorProto.  # noqa: E501
        :rtype: list[str]
        """
        return self._dependency_list

    @dependency_list.setter
    def dependency_list(self, dependency_list):
        """Sets the dependency_list of this FileDescriptorProto.


        :param dependency_list: The dependency_list of this FileDescriptorProto.  # noqa: E501
        :type: list[str]
        """

        self._dependency_list = dependency_list

    @property
    def public_dependency_list(self):
        """Gets the public_dependency_list of this FileDescriptorProto.  # noqa: E501


        :return: The public_dependency_list of this FileDescriptorProto.  # noqa: E501
        :rtype: list[int]
        """
        return self._public_dependency_list

    @public_dependency_list.setter
    def public_dependency_list(self, public_dependency_list):
        """Sets the public_dependency_list of this FileDescriptorProto.


        :param public_dependency_list: The public_dependency_list of this FileDescriptorProto.  # noqa: E501
        :type: list[int]
        """

        self._public_dependency_list = public_dependency_list

    @property
    def weak_dependency_list(self):
        """Gets the weak_dependency_list of this FileDescriptorProto.  # noqa: E501


        :return: The weak_dependency_list of this FileDescriptorProto.  # noqa: E501
        :rtype: list[int]
        """
        return self._weak_dependency_list

    @weak_dependency_list.setter
    def weak_dependency_list(self, weak_dependency_list):
        """Sets the weak_dependency_list of this FileDescriptorProto.


        :param weak_dependency_list: The weak_dependency_list of this FileDescriptorProto.  # noqa: E501
        :type: list[int]
        """

        self._weak_dependency_list = weak_dependency_list

    @property
    def weak_dependency_count(self):
        """Gets the weak_dependency_count of this FileDescriptorProto.  # noqa: E501


        :return: The weak_dependency_count of this FileDescriptorProto.  # noqa: E501
        :rtype: int
        """
        return self._weak_dependency_count

    @weak_dependency_count.setter
    def weak_dependency_count(self, weak_dependency_count):
        """Sets the weak_dependency_count of this FileDescriptorProto.


        :param weak_dependency_count: The weak_dependency_count of this FileDescriptorProto.  # noqa: E501
        :type: int
        """

        self._weak_dependency_count = weak_dependency_count

    @property
    def message_type_list(self):
        """Gets the message_type_list of this FileDescriptorProto.  # noqa: E501


        :return: The message_type_list of this FileDescriptorProto.  # noqa: E501
        :rtype: list[DescriptorProto]
        """
        return self._message_type_list

    @message_type_list.setter
    def message_type_list(self, message_type_list):
        """Sets the message_type_list of this FileDescriptorProto.


        :param message_type_list: The message_type_list of this FileDescriptorProto.  # noqa: E501
        :type: list[DescriptorProto]
        """

        self._message_type_list = message_type_list

    @property
    def message_type_or_builder_list(self):
        """Gets the message_type_or_builder_list of this FileDescriptorProto.  # noqa: E501


        :return: The message_type_or_builder_list of this FileDescriptorProto.  # noqa: E501
        :rtype: list[DescriptorProtoOrBuilder]
        """
        return self._message_type_or_builder_list

    @message_type_or_builder_list.setter
    def message_type_or_builder_list(self, message_type_or_builder_list):
        """Sets the message_type_or_builder_list of this FileDescriptorProto.


        :param message_type_or_builder_list: The message_type_or_builder_list of this FileDescriptorProto.  # noqa: E501
        :type: list[DescriptorProtoOrBuilder]
        """

        self._message_type_or_builder_list = message_type_or_builder_list

    @property
    def enum_type_list(self):
        """Gets the enum_type_list of this FileDescriptorProto.  # noqa: E501


        :return: The enum_type_list of this FileDescriptorProto.  # noqa: E501
        :rtype: list[EnumDescriptorProto]
        """
        return self._enum_type_list

    @enum_type_list.setter
    def enum_type_list(self, enum_type_list):
        """Sets the enum_type_list of this FileDescriptorProto.


        :param enum_type_list: The enum_type_list of this FileDescriptorProto.  # noqa: E501
        :type: list[EnumDescriptorProto]
        """

        self._enum_type_list = enum_type_list

    @property
    def enum_type_or_builder_list(self):
        """Gets the enum_type_or_builder_list of this FileDescriptorProto.  # noqa: E501


        :return: The enum_type_or_builder_list of this FileDescriptorProto.  # noqa: E501
        :rtype: list[EnumDescriptorProtoOrBuilder]
        """
        return self._enum_type_or_builder_list

    @enum_type_or_builder_list.setter
    def enum_type_or_builder_list(self, enum_type_or_builder_list):
        """Sets the enum_type_or_builder_list of this FileDescriptorProto.


        :param enum_type_or_builder_list: The enum_type_or_builder_list of this FileDescriptorProto.  # noqa: E501
        :type: list[EnumDescriptorProtoOrBuilder]
        """

        self._enum_type_or_builder_list = enum_type_or_builder_list

    @property
    def service_list(self):
        """Gets the service_list of this FileDescriptorProto.  # noqa: E501


        :return: The service_list of this FileDescriptorProto.  # noqa: E501
        :rtype: list[ServiceDescriptorProto]
        """
        return self._service_list

    @service_list.setter
    def service_list(self, service_list):
        """Sets the service_list of this FileDescriptorProto.


        :param service_list: The service_list of this FileDescriptorProto.  # noqa: E501
        :type: list[ServiceDescriptorProto]
        """

        self._service_list = service_list

    @property
    def service_or_builder_list(self):
        """Gets the service_or_builder_list of this FileDescriptorProto.  # noqa: E501


        :return: The service_or_builder_list of this FileDescriptorProto.  # noqa: E501
        :rtype: list[ServiceDescriptorProtoOrBuilder]
        """
        return self._service_or_builder_list

    @service_or_builder_list.setter
    def service_or_builder_list(self, service_or_builder_list):
        """Sets the service_or_builder_list of this FileDescriptorProto.


        :param service_or_builder_list: The service_or_builder_list of this FileDescriptorProto.  # noqa: E501
        :type: list[ServiceDescriptorProtoOrBuilder]
        """

        self._service_or_builder_list = service_or_builder_list

    @property
    def extension_list(self):
        """Gets the extension_list of this FileDescriptorProto.  # noqa: E501


        :return: The extension_list of this FileDescriptorProto.  # noqa: E501
        :rtype: list[FieldDescriptorProto]
        """
        return self._extension_list

    @extension_list.setter
    def extension_list(self, extension_list):
        """Sets the extension_list of this FileDescriptorProto.


        :param extension_list: The extension_list of this FileDescriptorProto.  # noqa: E501
        :type: list[FieldDescriptorProto]
        """

        self._extension_list = extension_list

    @property
    def extension_or_builder_list(self):
        """Gets the extension_or_builder_list of this FileDescriptorProto.  # noqa: E501


        :return: The extension_or_builder_list of this FileDescriptorProto.  # noqa: E501
        :rtype: list[FieldDescriptorProtoOrBuilder]
        """
        return self._extension_or_builder_list

    @extension_or_builder_list.setter
    def extension_or_builder_list(self, extension_or_builder_list):
        """Sets the extension_or_builder_list of this FileDescriptorProto.


        :param extension_or_builder_list: The extension_or_builder_list of this FileDescriptorProto.  # noqa: E501
        :type: list[FieldDescriptorProtoOrBuilder]
        """

        self._extension_or_builder_list = extension_or_builder_list

    @property
    def options_or_builder(self):
        """Gets the options_or_builder of this FileDescriptorProto.  # noqa: E501


        :return: The options_or_builder of this FileDescriptorProto.  # noqa: E501
        :rtype: FileOptionsOrBuilder
        """
        return self._options_or_builder

    @options_or_builder.setter
    def options_or_builder(self, options_or_builder):
        """Sets the options_or_builder of this FileDescriptorProto.


        :param options_or_builder: The options_or_builder of this FileDescriptorProto.  # noqa: E501
        :type: FileOptionsOrBuilder
        """

        self._options_or_builder = options_or_builder

    @property
    def source_code_info(self):
        """Gets the source_code_info of this FileDescriptorProto.  # noqa: E501


        :return: The source_code_info of this FileDescriptorProto.  # noqa: E501
        :rtype: SourceCodeInfo
        """
        return self._source_code_info

    @source_code_info.setter
    def source_code_info(self, source_code_info):
        """Sets the source_code_info of this FileDescriptorProto.


        :param source_code_info: The source_code_info of this FileDescriptorProto.  # noqa: E501
        :type: SourceCodeInfo
        """

        self._source_code_info = source_code_info

    @property
    def source_code_info_or_builder(self):
        """Gets the source_code_info_or_builder of this FileDescriptorProto.  # noqa: E501


        :return: The source_code_info_or_builder of this FileDescriptorProto.  # noqa: E501
        :rtype: SourceCodeInfoOrBuilder
        """
        return self._source_code_info_or_builder

    @source_code_info_or_builder.setter
    def source_code_info_or_builder(self, source_code_info_or_builder):
        """Sets the source_code_info_or_builder of this FileDescriptorProto.


        :param source_code_info_or_builder: The source_code_info_or_builder of this FileDescriptorProto.  # noqa: E501
        :type: SourceCodeInfoOrBuilder
        """

        self._source_code_info_or_builder = source_code_info_or_builder

    @property
    def syntax_bytes(self):
        """Gets the syntax_bytes of this FileDescriptorProto.  # noqa: E501


        :return: The syntax_bytes of this FileDescriptorProto.  # noqa: E501
        :rtype: ByteString
        """
        return self._syntax_bytes

    @syntax_bytes.setter
    def syntax_bytes(self, syntax_bytes):
        """Sets the syntax_bytes of this FileDescriptorProto.


        :param syntax_bytes: The syntax_bytes of this FileDescriptorProto.  # noqa: E501
        :type: ByteString
        """

        self._syntax_bytes = syntax_bytes

    @property
    def name_bytes(self):
        """Gets the name_bytes of this FileDescriptorProto.  # noqa: E501


        :return: The name_bytes of this FileDescriptorProto.  # noqa: E501
        :rtype: ByteString
        """
        return self._name_bytes

    @name_bytes.setter
    def name_bytes(self, name_bytes):
        """Sets the name_bytes of this FileDescriptorProto.


        :param name_bytes: The name_bytes of this FileDescriptorProto.  # noqa: E501
        :type: ByteString
        """

        self._name_bytes = name_bytes

    @property
    def all_fields(self):
        """Gets the all_fields of this FileDescriptorProto.  # noqa: E501


        :return: The all_fields of this FileDescriptorProto.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._all_fields

    @all_fields.setter
    def all_fields(self, all_fields):
        """Sets the all_fields of this FileDescriptorProto.


        :param all_fields: The all_fields of this FileDescriptorProto.  # noqa: E501
        :type: dict(str, object)
        """

        self._all_fields = all_fields

    @property
    def descriptor_for_type(self):
        """Gets the descriptor_for_type of this FileDescriptorProto.  # noqa: E501


        :return: The descriptor_for_type of this FileDescriptorProto.  # noqa: E501
        :rtype: Descriptor
        """
        return self._descriptor_for_type

    @descriptor_for_type.setter
    def descriptor_for_type(self, descriptor_for_type):
        """Sets the descriptor_for_type of this FileDescriptorProto.


        :param descriptor_for_type: The descriptor_for_type of this FileDescriptorProto.  # noqa: E501
        :type: Descriptor
        """

        self._descriptor_for_type = descriptor_for_type

    @property
    def initialization_error_string(self):
        """Gets the initialization_error_string of this FileDescriptorProto.  # noqa: E501


        :return: The initialization_error_string of this FileDescriptorProto.  # noqa: E501
        :rtype: str
        """
        return self._initialization_error_string

    @initialization_error_string.setter
    def initialization_error_string(self, initialization_error_string):
        """Sets the initialization_error_string of this FileDescriptorProto.


        :param initialization_error_string: The initialization_error_string of this FileDescriptorProto.  # noqa: E501
        :type: str
        """

        self._initialization_error_string = initialization_error_string

    @property
    def memoized_serialized_size(self):
        """Gets the memoized_serialized_size of this FileDescriptorProto.  # noqa: E501


        :return: The memoized_serialized_size of this FileDescriptorProto.  # noqa: E501
        :rtype: int
        """
        return self._memoized_serialized_size

    @memoized_serialized_size.setter
    def memoized_serialized_size(self, memoized_serialized_size):
        """Sets the memoized_serialized_size of this FileDescriptorProto.


        :param memoized_serialized_size: The memoized_serialized_size of this FileDescriptorProto.  # noqa: E501
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
        if issubclass(FileDescriptorProto, dict):
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
        if not isinstance(other, FileDescriptorProto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
