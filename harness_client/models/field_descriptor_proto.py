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

class FieldDescriptorProto(object):
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
        'type_name': 'str',
        'type': 'str',
        'default_value': 'str',
        'number': 'int',
        'label': 'str',
        'initialized': 'bool',
        'options': 'FieldOptions',
        'type_name_bytes': 'ByteString',
        'serialized_size': 'int',
        'parser_for_type': 'ParserFieldDescriptorProto',
        'default_instance_for_type': 'FieldDescriptorProto',
        'options_or_builder': 'FieldOptionsOrBuilder',
        'name_bytes': 'ByteString',
        'json_name': 'str',
        'proto3_optional': 'bool',
        'oneof_index': 'int',
        'extendee': 'str',
        'extendee_bytes': 'ByteString',
        'default_value_bytes': 'ByteString',
        'json_name_bytes': 'ByteString',
        'all_fields': 'dict(str, object)',
        'descriptor_for_type': 'Descriptor',
        'initialization_error_string': 'str',
        'memoized_serialized_size': 'int'
    }

    attribute_map = {
        'unknown_fields': 'unknownFields',
        'name': 'name',
        'type_name': 'typeName',
        'type': 'type',
        'default_value': 'defaultValue',
        'number': 'number',
        'label': 'label',
        'initialized': 'initialized',
        'options': 'options',
        'type_name_bytes': 'typeNameBytes',
        'serialized_size': 'serializedSize',
        'parser_for_type': 'parserForType',
        'default_instance_for_type': 'defaultInstanceForType',
        'options_or_builder': 'optionsOrBuilder',
        'name_bytes': 'nameBytes',
        'json_name': 'jsonName',
        'proto3_optional': 'proto3Optional',
        'oneof_index': 'oneofIndex',
        'extendee': 'extendee',
        'extendee_bytes': 'extendeeBytes',
        'default_value_bytes': 'defaultValueBytes',
        'json_name_bytes': 'jsonNameBytes',
        'all_fields': 'allFields',
        'descriptor_for_type': 'descriptorForType',
        'initialization_error_string': 'initializationErrorString',
        'memoized_serialized_size': 'memoizedSerializedSize'
    }

    def __init__(self, unknown_fields=None, name=None, type_name=None, type=None, default_value=None, number=None, label=None, initialized=None, options=None, type_name_bytes=None, serialized_size=None, parser_for_type=None, default_instance_for_type=None, options_or_builder=None, name_bytes=None, json_name=None, proto3_optional=None, oneof_index=None, extendee=None, extendee_bytes=None, default_value_bytes=None, json_name_bytes=None, all_fields=None, descriptor_for_type=None, initialization_error_string=None, memoized_serialized_size=None):  # noqa: E501
        """FieldDescriptorProto - a model defined in Swagger"""  # noqa: E501
        self._unknown_fields = None
        self._name = None
        self._type_name = None
        self._type = None
        self._default_value = None
        self._number = None
        self._label = None
        self._initialized = None
        self._options = None
        self._type_name_bytes = None
        self._serialized_size = None
        self._parser_for_type = None
        self._default_instance_for_type = None
        self._options_or_builder = None
        self._name_bytes = None
        self._json_name = None
        self._proto3_optional = None
        self._oneof_index = None
        self._extendee = None
        self._extendee_bytes = None
        self._default_value_bytes = None
        self._json_name_bytes = None
        self._all_fields = None
        self._descriptor_for_type = None
        self._initialization_error_string = None
        self._memoized_serialized_size = None
        self.discriminator = None
        if unknown_fields is not None:
            self.unknown_fields = unknown_fields
        if name is not None:
            self.name = name
        if type_name is not None:
            self.type_name = type_name
        if type is not None:
            self.type = type
        if default_value is not None:
            self.default_value = default_value
        if number is not None:
            self.number = number
        if label is not None:
            self.label = label
        if initialized is not None:
            self.initialized = initialized
        if options is not None:
            self.options = options
        if type_name_bytes is not None:
            self.type_name_bytes = type_name_bytes
        if serialized_size is not None:
            self.serialized_size = serialized_size
        if parser_for_type is not None:
            self.parser_for_type = parser_for_type
        if default_instance_for_type is not None:
            self.default_instance_for_type = default_instance_for_type
        if options_or_builder is not None:
            self.options_or_builder = options_or_builder
        if name_bytes is not None:
            self.name_bytes = name_bytes
        if json_name is not None:
            self.json_name = json_name
        if proto3_optional is not None:
            self.proto3_optional = proto3_optional
        if oneof_index is not None:
            self.oneof_index = oneof_index
        if extendee is not None:
            self.extendee = extendee
        if extendee_bytes is not None:
            self.extendee_bytes = extendee_bytes
        if default_value_bytes is not None:
            self.default_value_bytes = default_value_bytes
        if json_name_bytes is not None:
            self.json_name_bytes = json_name_bytes
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
        """Gets the unknown_fields of this FieldDescriptorProto.  # noqa: E501


        :return: The unknown_fields of this FieldDescriptorProto.  # noqa: E501
        :rtype: UnknownFieldSet
        """
        return self._unknown_fields

    @unknown_fields.setter
    def unknown_fields(self, unknown_fields):
        """Sets the unknown_fields of this FieldDescriptorProto.


        :param unknown_fields: The unknown_fields of this FieldDescriptorProto.  # noqa: E501
        :type: UnknownFieldSet
        """

        self._unknown_fields = unknown_fields

    @property
    def name(self):
        """Gets the name of this FieldDescriptorProto.  # noqa: E501


        :return: The name of this FieldDescriptorProto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FieldDescriptorProto.


        :param name: The name of this FieldDescriptorProto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type_name(self):
        """Gets the type_name of this FieldDescriptorProto.  # noqa: E501


        :return: The type_name of this FieldDescriptorProto.  # noqa: E501
        :rtype: str
        """
        return self._type_name

    @type_name.setter
    def type_name(self, type_name):
        """Sets the type_name of this FieldDescriptorProto.


        :param type_name: The type_name of this FieldDescriptorProto.  # noqa: E501
        :type: str
        """

        self._type_name = type_name

    @property
    def type(self):
        """Gets the type of this FieldDescriptorProto.  # noqa: E501


        :return: The type of this FieldDescriptorProto.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FieldDescriptorProto.


        :param type: The type of this FieldDescriptorProto.  # noqa: E501
        :type: str
        """
        allowed_values = ["TYPE_DOUBLE", "TYPE_FLOAT", "TYPE_INT64", "TYPE_UINT64", "TYPE_INT32", "TYPE_FIXED64", "TYPE_FIXED32", "TYPE_BOOL", "TYPE_STRING", "TYPE_GROUP", "TYPE_MESSAGE", "TYPE_BYTES", "TYPE_UINT32", "TYPE_ENUM", "TYPE_SFIXED32", "TYPE_SFIXED64", "TYPE_SINT32", "TYPE_SINT64"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def default_value(self):
        """Gets the default_value of this FieldDescriptorProto.  # noqa: E501


        :return: The default_value of this FieldDescriptorProto.  # noqa: E501
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Sets the default_value of this FieldDescriptorProto.


        :param default_value: The default_value of this FieldDescriptorProto.  # noqa: E501
        :type: str
        """

        self._default_value = default_value

    @property
    def number(self):
        """Gets the number of this FieldDescriptorProto.  # noqa: E501


        :return: The number of this FieldDescriptorProto.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this FieldDescriptorProto.


        :param number: The number of this FieldDescriptorProto.  # noqa: E501
        :type: int
        """

        self._number = number

    @property
    def label(self):
        """Gets the label of this FieldDescriptorProto.  # noqa: E501


        :return: The label of this FieldDescriptorProto.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this FieldDescriptorProto.


        :param label: The label of this FieldDescriptorProto.  # noqa: E501
        :type: str
        """
        allowed_values = ["LABEL_OPTIONAL", "LABEL_REQUIRED", "LABEL_REPEATED"]  # noqa: E501
        if label not in allowed_values:
            raise ValueError(
                "Invalid value for `label` ({0}), must be one of {1}"  # noqa: E501
                .format(label, allowed_values)
            )

        self._label = label

    @property
    def initialized(self):
        """Gets the initialized of this FieldDescriptorProto.  # noqa: E501


        :return: The initialized of this FieldDescriptorProto.  # noqa: E501
        :rtype: bool
        """
        return self._initialized

    @initialized.setter
    def initialized(self, initialized):
        """Sets the initialized of this FieldDescriptorProto.


        :param initialized: The initialized of this FieldDescriptorProto.  # noqa: E501
        :type: bool
        """

        self._initialized = initialized

    @property
    def options(self):
        """Gets the options of this FieldDescriptorProto.  # noqa: E501


        :return: The options of this FieldDescriptorProto.  # noqa: E501
        :rtype: FieldOptions
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this FieldDescriptorProto.


        :param options: The options of this FieldDescriptorProto.  # noqa: E501
        :type: FieldOptions
        """

        self._options = options

    @property
    def type_name_bytes(self):
        """Gets the type_name_bytes of this FieldDescriptorProto.  # noqa: E501


        :return: The type_name_bytes of this FieldDescriptorProto.  # noqa: E501
        :rtype: ByteString
        """
        return self._type_name_bytes

    @type_name_bytes.setter
    def type_name_bytes(self, type_name_bytes):
        """Sets the type_name_bytes of this FieldDescriptorProto.


        :param type_name_bytes: The type_name_bytes of this FieldDescriptorProto.  # noqa: E501
        :type: ByteString
        """

        self._type_name_bytes = type_name_bytes

    @property
    def serialized_size(self):
        """Gets the serialized_size of this FieldDescriptorProto.  # noqa: E501


        :return: The serialized_size of this FieldDescriptorProto.  # noqa: E501
        :rtype: int
        """
        return self._serialized_size

    @serialized_size.setter
    def serialized_size(self, serialized_size):
        """Sets the serialized_size of this FieldDescriptorProto.


        :param serialized_size: The serialized_size of this FieldDescriptorProto.  # noqa: E501
        :type: int
        """

        self._serialized_size = serialized_size

    @property
    def parser_for_type(self):
        """Gets the parser_for_type of this FieldDescriptorProto.  # noqa: E501


        :return: The parser_for_type of this FieldDescriptorProto.  # noqa: E501
        :rtype: ParserFieldDescriptorProto
        """
        return self._parser_for_type

    @parser_for_type.setter
    def parser_for_type(self, parser_for_type):
        """Sets the parser_for_type of this FieldDescriptorProto.


        :param parser_for_type: The parser_for_type of this FieldDescriptorProto.  # noqa: E501
        :type: ParserFieldDescriptorProto
        """

        self._parser_for_type = parser_for_type

    @property
    def default_instance_for_type(self):
        """Gets the default_instance_for_type of this FieldDescriptorProto.  # noqa: E501


        :return: The default_instance_for_type of this FieldDescriptorProto.  # noqa: E501
        :rtype: FieldDescriptorProto
        """
        return self._default_instance_for_type

    @default_instance_for_type.setter
    def default_instance_for_type(self, default_instance_for_type):
        """Sets the default_instance_for_type of this FieldDescriptorProto.


        :param default_instance_for_type: The default_instance_for_type of this FieldDescriptorProto.  # noqa: E501
        :type: FieldDescriptorProto
        """

        self._default_instance_for_type = default_instance_for_type

    @property
    def options_or_builder(self):
        """Gets the options_or_builder of this FieldDescriptorProto.  # noqa: E501


        :return: The options_or_builder of this FieldDescriptorProto.  # noqa: E501
        :rtype: FieldOptionsOrBuilder
        """
        return self._options_or_builder

    @options_or_builder.setter
    def options_or_builder(self, options_or_builder):
        """Sets the options_or_builder of this FieldDescriptorProto.


        :param options_or_builder: The options_or_builder of this FieldDescriptorProto.  # noqa: E501
        :type: FieldOptionsOrBuilder
        """

        self._options_or_builder = options_or_builder

    @property
    def name_bytes(self):
        """Gets the name_bytes of this FieldDescriptorProto.  # noqa: E501


        :return: The name_bytes of this FieldDescriptorProto.  # noqa: E501
        :rtype: ByteString
        """
        return self._name_bytes

    @name_bytes.setter
    def name_bytes(self, name_bytes):
        """Sets the name_bytes of this FieldDescriptorProto.


        :param name_bytes: The name_bytes of this FieldDescriptorProto.  # noqa: E501
        :type: ByteString
        """

        self._name_bytes = name_bytes

    @property
    def json_name(self):
        """Gets the json_name of this FieldDescriptorProto.  # noqa: E501


        :return: The json_name of this FieldDescriptorProto.  # noqa: E501
        :rtype: str
        """
        return self._json_name

    @json_name.setter
    def json_name(self, json_name):
        """Sets the json_name of this FieldDescriptorProto.


        :param json_name: The json_name of this FieldDescriptorProto.  # noqa: E501
        :type: str
        """

        self._json_name = json_name

    @property
    def proto3_optional(self):
        """Gets the proto3_optional of this FieldDescriptorProto.  # noqa: E501


        :return: The proto3_optional of this FieldDescriptorProto.  # noqa: E501
        :rtype: bool
        """
        return self._proto3_optional

    @proto3_optional.setter
    def proto3_optional(self, proto3_optional):
        """Sets the proto3_optional of this FieldDescriptorProto.


        :param proto3_optional: The proto3_optional of this FieldDescriptorProto.  # noqa: E501
        :type: bool
        """

        self._proto3_optional = proto3_optional

    @property
    def oneof_index(self):
        """Gets the oneof_index of this FieldDescriptorProto.  # noqa: E501


        :return: The oneof_index of this FieldDescriptorProto.  # noqa: E501
        :rtype: int
        """
        return self._oneof_index

    @oneof_index.setter
    def oneof_index(self, oneof_index):
        """Sets the oneof_index of this FieldDescriptorProto.


        :param oneof_index: The oneof_index of this FieldDescriptorProto.  # noqa: E501
        :type: int
        """

        self._oneof_index = oneof_index

    @property
    def extendee(self):
        """Gets the extendee of this FieldDescriptorProto.  # noqa: E501


        :return: The extendee of this FieldDescriptorProto.  # noqa: E501
        :rtype: str
        """
        return self._extendee

    @extendee.setter
    def extendee(self, extendee):
        """Sets the extendee of this FieldDescriptorProto.


        :param extendee: The extendee of this FieldDescriptorProto.  # noqa: E501
        :type: str
        """

        self._extendee = extendee

    @property
    def extendee_bytes(self):
        """Gets the extendee_bytes of this FieldDescriptorProto.  # noqa: E501


        :return: The extendee_bytes of this FieldDescriptorProto.  # noqa: E501
        :rtype: ByteString
        """
        return self._extendee_bytes

    @extendee_bytes.setter
    def extendee_bytes(self, extendee_bytes):
        """Sets the extendee_bytes of this FieldDescriptorProto.


        :param extendee_bytes: The extendee_bytes of this FieldDescriptorProto.  # noqa: E501
        :type: ByteString
        """

        self._extendee_bytes = extendee_bytes

    @property
    def default_value_bytes(self):
        """Gets the default_value_bytes of this FieldDescriptorProto.  # noqa: E501


        :return: The default_value_bytes of this FieldDescriptorProto.  # noqa: E501
        :rtype: ByteString
        """
        return self._default_value_bytes

    @default_value_bytes.setter
    def default_value_bytes(self, default_value_bytes):
        """Sets the default_value_bytes of this FieldDescriptorProto.


        :param default_value_bytes: The default_value_bytes of this FieldDescriptorProto.  # noqa: E501
        :type: ByteString
        """

        self._default_value_bytes = default_value_bytes

    @property
    def json_name_bytes(self):
        """Gets the json_name_bytes of this FieldDescriptorProto.  # noqa: E501


        :return: The json_name_bytes of this FieldDescriptorProto.  # noqa: E501
        :rtype: ByteString
        """
        return self._json_name_bytes

    @json_name_bytes.setter
    def json_name_bytes(self, json_name_bytes):
        """Sets the json_name_bytes of this FieldDescriptorProto.


        :param json_name_bytes: The json_name_bytes of this FieldDescriptorProto.  # noqa: E501
        :type: ByteString
        """

        self._json_name_bytes = json_name_bytes

    @property
    def all_fields(self):
        """Gets the all_fields of this FieldDescriptorProto.  # noqa: E501


        :return: The all_fields of this FieldDescriptorProto.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._all_fields

    @all_fields.setter
    def all_fields(self, all_fields):
        """Sets the all_fields of this FieldDescriptorProto.


        :param all_fields: The all_fields of this FieldDescriptorProto.  # noqa: E501
        :type: dict(str, object)
        """

        self._all_fields = all_fields

    @property
    def descriptor_for_type(self):
        """Gets the descriptor_for_type of this FieldDescriptorProto.  # noqa: E501


        :return: The descriptor_for_type of this FieldDescriptorProto.  # noqa: E501
        :rtype: Descriptor
        """
        return self._descriptor_for_type

    @descriptor_for_type.setter
    def descriptor_for_type(self, descriptor_for_type):
        """Sets the descriptor_for_type of this FieldDescriptorProto.


        :param descriptor_for_type: The descriptor_for_type of this FieldDescriptorProto.  # noqa: E501
        :type: Descriptor
        """

        self._descriptor_for_type = descriptor_for_type

    @property
    def initialization_error_string(self):
        """Gets the initialization_error_string of this FieldDescriptorProto.  # noqa: E501


        :return: The initialization_error_string of this FieldDescriptorProto.  # noqa: E501
        :rtype: str
        """
        return self._initialization_error_string

    @initialization_error_string.setter
    def initialization_error_string(self, initialization_error_string):
        """Sets the initialization_error_string of this FieldDescriptorProto.


        :param initialization_error_string: The initialization_error_string of this FieldDescriptorProto.  # noqa: E501
        :type: str
        """

        self._initialization_error_string = initialization_error_string

    @property
    def memoized_serialized_size(self):
        """Gets the memoized_serialized_size of this FieldDescriptorProto.  # noqa: E501


        :return: The memoized_serialized_size of this FieldDescriptorProto.  # noqa: E501
        :rtype: int
        """
        return self._memoized_serialized_size

    @memoized_serialized_size.setter
    def memoized_serialized_size(self, memoized_serialized_size):
        """Sets the memoized_serialized_size of this FieldDescriptorProto.


        :param memoized_serialized_size: The memoized_serialized_size of this FieldDescriptorProto.  # noqa: E501
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
        if issubclass(FieldDescriptorProto, dict):
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
        if not isinstance(other, FieldDescriptorProto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
