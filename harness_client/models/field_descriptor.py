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

class FieldDescriptor(object):
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
        'index': 'int',
        'proto': 'FieldDescriptorProto',
        'full_name': 'str',
        'json_name': 'str',
        'file': 'FileDescriptor',
        'extension_scope': 'Descriptor',
        'type': 'str',
        'containing_type': 'Descriptor',
        'message_type': 'Descriptor',
        'containing_oneof': 'OneofDescriptor',
        'enum_type': 'EnumDescriptor',
        'default_value': 'object',
        'name': 'str',
        'number': 'int',
        'java_type': 'str',
        'optional': 'bool',
        'options': 'FieldOptions',
        'required': 'bool',
        'repeated': 'bool',
        'map_field': 'bool',
        'extension': 'bool',
        'lite_type': 'str',
        'packed': 'bool',
        'packable': 'bool',
        'real_containing_oneof': 'OneofDescriptor',
        'lite_java_type': 'str'
    }

    attribute_map = {
        'index': 'index',
        'proto': 'proto',
        'full_name': 'fullName',
        'json_name': 'jsonName',
        'file': 'file',
        'extension_scope': 'extensionScope',
        'type': 'type',
        'containing_type': 'containingType',
        'message_type': 'messageType',
        'containing_oneof': 'containingOneof',
        'enum_type': 'enumType',
        'default_value': 'defaultValue',
        'name': 'name',
        'number': 'number',
        'java_type': 'javaType',
        'optional': 'optional',
        'options': 'options',
        'required': 'required',
        'repeated': 'repeated',
        'map_field': 'mapField',
        'extension': 'extension',
        'lite_type': 'liteType',
        'packed': 'packed',
        'packable': 'packable',
        'real_containing_oneof': 'realContainingOneof',
        'lite_java_type': 'liteJavaType'
    }

    def __init__(self, index=None, proto=None, full_name=None, json_name=None, file=None, extension_scope=None, type=None, containing_type=None, message_type=None, containing_oneof=None, enum_type=None, default_value=None, name=None, number=None, java_type=None, optional=None, options=None, required=None, repeated=None, map_field=None, extension=None, lite_type=None, packed=None, packable=None, real_containing_oneof=None, lite_java_type=None):  # noqa: E501
        """FieldDescriptor - a model defined in Swagger"""  # noqa: E501
        self._index = None
        self._proto = None
        self._full_name = None
        self._json_name = None
        self._file = None
        self._extension_scope = None
        self._type = None
        self._containing_type = None
        self._message_type = None
        self._containing_oneof = None
        self._enum_type = None
        self._default_value = None
        self._name = None
        self._number = None
        self._java_type = None
        self._optional = None
        self._options = None
        self._required = None
        self._repeated = None
        self._map_field = None
        self._extension = None
        self._lite_type = None
        self._packed = None
        self._packable = None
        self._real_containing_oneof = None
        self._lite_java_type = None
        self.discriminator = None
        if index is not None:
            self.index = index
        if proto is not None:
            self.proto = proto
        if full_name is not None:
            self.full_name = full_name
        if json_name is not None:
            self.json_name = json_name
        if file is not None:
            self.file = file
        if extension_scope is not None:
            self.extension_scope = extension_scope
        if type is not None:
            self.type = type
        if containing_type is not None:
            self.containing_type = containing_type
        if message_type is not None:
            self.message_type = message_type
        if containing_oneof is not None:
            self.containing_oneof = containing_oneof
        if enum_type is not None:
            self.enum_type = enum_type
        if default_value is not None:
            self.default_value = default_value
        if name is not None:
            self.name = name
        if number is not None:
            self.number = number
        if java_type is not None:
            self.java_type = java_type
        if optional is not None:
            self.optional = optional
        if options is not None:
            self.options = options
        if required is not None:
            self.required = required
        if repeated is not None:
            self.repeated = repeated
        if map_field is not None:
            self.map_field = map_field
        if extension is not None:
            self.extension = extension
        if lite_type is not None:
            self.lite_type = lite_type
        if packed is not None:
            self.packed = packed
        if packable is not None:
            self.packable = packable
        if real_containing_oneof is not None:
            self.real_containing_oneof = real_containing_oneof
        if lite_java_type is not None:
            self.lite_java_type = lite_java_type

    @property
    def index(self):
        """Gets the index of this FieldDescriptor.  # noqa: E501


        :return: The index of this FieldDescriptor.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this FieldDescriptor.


        :param index: The index of this FieldDescriptor.  # noqa: E501
        :type: int
        """

        self._index = index

    @property
    def proto(self):
        """Gets the proto of this FieldDescriptor.  # noqa: E501


        :return: The proto of this FieldDescriptor.  # noqa: E501
        :rtype: FieldDescriptorProto
        """
        return self._proto

    @proto.setter
    def proto(self, proto):
        """Sets the proto of this FieldDescriptor.


        :param proto: The proto of this FieldDescriptor.  # noqa: E501
        :type: FieldDescriptorProto
        """

        self._proto = proto

    @property
    def full_name(self):
        """Gets the full_name of this FieldDescriptor.  # noqa: E501


        :return: The full_name of this FieldDescriptor.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this FieldDescriptor.


        :param full_name: The full_name of this FieldDescriptor.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

    @property
    def json_name(self):
        """Gets the json_name of this FieldDescriptor.  # noqa: E501


        :return: The json_name of this FieldDescriptor.  # noqa: E501
        :rtype: str
        """
        return self._json_name

    @json_name.setter
    def json_name(self, json_name):
        """Sets the json_name of this FieldDescriptor.


        :param json_name: The json_name of this FieldDescriptor.  # noqa: E501
        :type: str
        """

        self._json_name = json_name

    @property
    def file(self):
        """Gets the file of this FieldDescriptor.  # noqa: E501


        :return: The file of this FieldDescriptor.  # noqa: E501
        :rtype: FileDescriptor
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this FieldDescriptor.


        :param file: The file of this FieldDescriptor.  # noqa: E501
        :type: FileDescriptor
        """

        self._file = file

    @property
    def extension_scope(self):
        """Gets the extension_scope of this FieldDescriptor.  # noqa: E501


        :return: The extension_scope of this FieldDescriptor.  # noqa: E501
        :rtype: Descriptor
        """
        return self._extension_scope

    @extension_scope.setter
    def extension_scope(self, extension_scope):
        """Sets the extension_scope of this FieldDescriptor.


        :param extension_scope: The extension_scope of this FieldDescriptor.  # noqa: E501
        :type: Descriptor
        """

        self._extension_scope = extension_scope

    @property
    def type(self):
        """Gets the type of this FieldDescriptor.  # noqa: E501


        :return: The type of this FieldDescriptor.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FieldDescriptor.


        :param type: The type of this FieldDescriptor.  # noqa: E501
        :type: str
        """
        allowed_values = ["DOUBLE", "FLOAT", "INT64", "UINT64", "INT32", "FIXED64", "FIXED32", "BOOL", "STRING", "GROUP", "MESSAGE", "BYTES", "UINT32", "ENUM", "SFIXED32", "SFIXED64", "SINT32", "SINT64"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def containing_type(self):
        """Gets the containing_type of this FieldDescriptor.  # noqa: E501


        :return: The containing_type of this FieldDescriptor.  # noqa: E501
        :rtype: Descriptor
        """
        return self._containing_type

    @containing_type.setter
    def containing_type(self, containing_type):
        """Sets the containing_type of this FieldDescriptor.


        :param containing_type: The containing_type of this FieldDescriptor.  # noqa: E501
        :type: Descriptor
        """

        self._containing_type = containing_type

    @property
    def message_type(self):
        """Gets the message_type of this FieldDescriptor.  # noqa: E501


        :return: The message_type of this FieldDescriptor.  # noqa: E501
        :rtype: Descriptor
        """
        return self._message_type

    @message_type.setter
    def message_type(self, message_type):
        """Sets the message_type of this FieldDescriptor.


        :param message_type: The message_type of this FieldDescriptor.  # noqa: E501
        :type: Descriptor
        """

        self._message_type = message_type

    @property
    def containing_oneof(self):
        """Gets the containing_oneof of this FieldDescriptor.  # noqa: E501


        :return: The containing_oneof of this FieldDescriptor.  # noqa: E501
        :rtype: OneofDescriptor
        """
        return self._containing_oneof

    @containing_oneof.setter
    def containing_oneof(self, containing_oneof):
        """Sets the containing_oneof of this FieldDescriptor.


        :param containing_oneof: The containing_oneof of this FieldDescriptor.  # noqa: E501
        :type: OneofDescriptor
        """

        self._containing_oneof = containing_oneof

    @property
    def enum_type(self):
        """Gets the enum_type of this FieldDescriptor.  # noqa: E501


        :return: The enum_type of this FieldDescriptor.  # noqa: E501
        :rtype: EnumDescriptor
        """
        return self._enum_type

    @enum_type.setter
    def enum_type(self, enum_type):
        """Sets the enum_type of this FieldDescriptor.


        :param enum_type: The enum_type of this FieldDescriptor.  # noqa: E501
        :type: EnumDescriptor
        """

        self._enum_type = enum_type

    @property
    def default_value(self):
        """Gets the default_value of this FieldDescriptor.  # noqa: E501


        :return: The default_value of this FieldDescriptor.  # noqa: E501
        :rtype: object
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Sets the default_value of this FieldDescriptor.


        :param default_value: The default_value of this FieldDescriptor.  # noqa: E501
        :type: object
        """

        self._default_value = default_value

    @property
    def name(self):
        """Gets the name of this FieldDescriptor.  # noqa: E501


        :return: The name of this FieldDescriptor.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FieldDescriptor.


        :param name: The name of this FieldDescriptor.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def number(self):
        """Gets the number of this FieldDescriptor.  # noqa: E501


        :return: The number of this FieldDescriptor.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this FieldDescriptor.


        :param number: The number of this FieldDescriptor.  # noqa: E501
        :type: int
        """

        self._number = number

    @property
    def java_type(self):
        """Gets the java_type of this FieldDescriptor.  # noqa: E501


        :return: The java_type of this FieldDescriptor.  # noqa: E501
        :rtype: str
        """
        return self._java_type

    @java_type.setter
    def java_type(self, java_type):
        """Sets the java_type of this FieldDescriptor.


        :param java_type: The java_type of this FieldDescriptor.  # noqa: E501
        :type: str
        """
        allowed_values = ["INT", "LONG", "FLOAT", "DOUBLE", "BOOLEAN", "STRING", "BYTE_STRING", "ENUM", "MESSAGE"]  # noqa: E501
        if java_type not in allowed_values:
            raise ValueError(
                "Invalid value for `java_type` ({0}), must be one of {1}"  # noqa: E501
                .format(java_type, allowed_values)
            )

        self._java_type = java_type

    @property
    def optional(self):
        """Gets the optional of this FieldDescriptor.  # noqa: E501


        :return: The optional of this FieldDescriptor.  # noqa: E501
        :rtype: bool
        """
        return self._optional

    @optional.setter
    def optional(self, optional):
        """Sets the optional of this FieldDescriptor.


        :param optional: The optional of this FieldDescriptor.  # noqa: E501
        :type: bool
        """

        self._optional = optional

    @property
    def options(self):
        """Gets the options of this FieldDescriptor.  # noqa: E501


        :return: The options of this FieldDescriptor.  # noqa: E501
        :rtype: FieldOptions
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this FieldDescriptor.


        :param options: The options of this FieldDescriptor.  # noqa: E501
        :type: FieldOptions
        """

        self._options = options

    @property
    def required(self):
        """Gets the required of this FieldDescriptor.  # noqa: E501


        :return: The required of this FieldDescriptor.  # noqa: E501
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this FieldDescriptor.


        :param required: The required of this FieldDescriptor.  # noqa: E501
        :type: bool
        """

        self._required = required

    @property
    def repeated(self):
        """Gets the repeated of this FieldDescriptor.  # noqa: E501


        :return: The repeated of this FieldDescriptor.  # noqa: E501
        :rtype: bool
        """
        return self._repeated

    @repeated.setter
    def repeated(self, repeated):
        """Sets the repeated of this FieldDescriptor.


        :param repeated: The repeated of this FieldDescriptor.  # noqa: E501
        :type: bool
        """

        self._repeated = repeated

    @property
    def map_field(self):
        """Gets the map_field of this FieldDescriptor.  # noqa: E501


        :return: The map_field of this FieldDescriptor.  # noqa: E501
        :rtype: bool
        """
        return self._map_field

    @map_field.setter
    def map_field(self, map_field):
        """Sets the map_field of this FieldDescriptor.


        :param map_field: The map_field of this FieldDescriptor.  # noqa: E501
        :type: bool
        """

        self._map_field = map_field

    @property
    def extension(self):
        """Gets the extension of this FieldDescriptor.  # noqa: E501


        :return: The extension of this FieldDescriptor.  # noqa: E501
        :rtype: bool
        """
        return self._extension

    @extension.setter
    def extension(self, extension):
        """Sets the extension of this FieldDescriptor.


        :param extension: The extension of this FieldDescriptor.  # noqa: E501
        :type: bool
        """

        self._extension = extension

    @property
    def lite_type(self):
        """Gets the lite_type of this FieldDescriptor.  # noqa: E501


        :return: The lite_type of this FieldDescriptor.  # noqa: E501
        :rtype: str
        """
        return self._lite_type

    @lite_type.setter
    def lite_type(self, lite_type):
        """Sets the lite_type of this FieldDescriptor.


        :param lite_type: The lite_type of this FieldDescriptor.  # noqa: E501
        :type: str
        """
        allowed_values = ["DOUBLE", "FLOAT", "INT64", "UINT64", "INT32", "FIXED64", "FIXED32", "BOOL", "STRING", "GROUP", "MESSAGE", "BYTES", "UINT32", "ENUM", "SFIXED32", "SFIXED64", "SINT32", "SINT64"]  # noqa: E501
        if lite_type not in allowed_values:
            raise ValueError(
                "Invalid value for `lite_type` ({0}), must be one of {1}"  # noqa: E501
                .format(lite_type, allowed_values)
            )

        self._lite_type = lite_type

    @property
    def packed(self):
        """Gets the packed of this FieldDescriptor.  # noqa: E501


        :return: The packed of this FieldDescriptor.  # noqa: E501
        :rtype: bool
        """
        return self._packed

    @packed.setter
    def packed(self, packed):
        """Sets the packed of this FieldDescriptor.


        :param packed: The packed of this FieldDescriptor.  # noqa: E501
        :type: bool
        """

        self._packed = packed

    @property
    def packable(self):
        """Gets the packable of this FieldDescriptor.  # noqa: E501


        :return: The packable of this FieldDescriptor.  # noqa: E501
        :rtype: bool
        """
        return self._packable

    @packable.setter
    def packable(self, packable):
        """Sets the packable of this FieldDescriptor.


        :param packable: The packable of this FieldDescriptor.  # noqa: E501
        :type: bool
        """

        self._packable = packable

    @property
    def real_containing_oneof(self):
        """Gets the real_containing_oneof of this FieldDescriptor.  # noqa: E501


        :return: The real_containing_oneof of this FieldDescriptor.  # noqa: E501
        :rtype: OneofDescriptor
        """
        return self._real_containing_oneof

    @real_containing_oneof.setter
    def real_containing_oneof(self, real_containing_oneof):
        """Sets the real_containing_oneof of this FieldDescriptor.


        :param real_containing_oneof: The real_containing_oneof of this FieldDescriptor.  # noqa: E501
        :type: OneofDescriptor
        """

        self._real_containing_oneof = real_containing_oneof

    @property
    def lite_java_type(self):
        """Gets the lite_java_type of this FieldDescriptor.  # noqa: E501


        :return: The lite_java_type of this FieldDescriptor.  # noqa: E501
        :rtype: str
        """
        return self._lite_java_type

    @lite_java_type.setter
    def lite_java_type(self, lite_java_type):
        """Sets the lite_java_type of this FieldDescriptor.


        :param lite_java_type: The lite_java_type of this FieldDescriptor.  # noqa: E501
        :type: str
        """
        allowed_values = ["INT", "LONG", "FLOAT", "DOUBLE", "BOOLEAN", "STRING", "BYTE_STRING", "ENUM", "MESSAGE"]  # noqa: E501
        if lite_java_type not in allowed_values:
            raise ValueError(
                "Invalid value for `lite_java_type` ({0}), must be one of {1}"  # noqa: E501
                .format(lite_java_type, allowed_values)
            )

        self._lite_java_type = lite_java_type

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
        if issubclass(FieldDescriptor, dict):
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
        if not isinstance(other, FieldDescriptor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
