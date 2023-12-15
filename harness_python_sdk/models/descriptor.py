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

class Descriptor(object):
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
        'proto': 'DescriptorProto',
        'full_name': 'str',
        'file': 'FileDescriptor',
        'containing_type': 'Descriptor',
        'nested_types': 'list[Descriptor]',
        'enum_types': 'list[EnumDescriptor]',
        'fields': 'list[FieldDescriptor]',
        'extensions': 'list[FieldDescriptor]',
        'oneofs': 'list[OneofDescriptor]',
        'name': 'str',
        'options': 'MessageOptions',
        'real_oneofs': 'list[OneofDescriptor]',
        'extendable': 'bool'
    }

    attribute_map = {
        'index': 'index',
        'proto': 'proto',
        'full_name': 'fullName',
        'file': 'file',
        'containing_type': 'containingType',
        'nested_types': 'nestedTypes',
        'enum_types': 'enumTypes',
        'fields': 'fields',
        'extensions': 'extensions',
        'oneofs': 'oneofs',
        'name': 'name',
        'options': 'options',
        'real_oneofs': 'realOneofs',
        'extendable': 'extendable'
    }

    def __init__(self, index=None, proto=None, full_name=None, file=None, containing_type=None, nested_types=None, enum_types=None, fields=None, extensions=None, oneofs=None, name=None, options=None, real_oneofs=None, extendable=None):  # noqa: E501
        """Descriptor - a model defined in Swagger"""  # noqa: E501
        self._index = None
        self._proto = None
        self._full_name = None
        self._file = None
        self._containing_type = None
        self._nested_types = None
        self._enum_types = None
        self._fields = None
        self._extensions = None
        self._oneofs = None
        self._name = None
        self._options = None
        self._real_oneofs = None
        self._extendable = None
        self.discriminator = None
        if index is not None:
            self.index = index
        if proto is not None:
            self.proto = proto
        if full_name is not None:
            self.full_name = full_name
        if file is not None:
            self.file = file
        if containing_type is not None:
            self.containing_type = containing_type
        if nested_types is not None:
            self.nested_types = nested_types
        if enum_types is not None:
            self.enum_types = enum_types
        if fields is not None:
            self.fields = fields
        if extensions is not None:
            self.extensions = extensions
        if oneofs is not None:
            self.oneofs = oneofs
        if name is not None:
            self.name = name
        if options is not None:
            self.options = options
        if real_oneofs is not None:
            self.real_oneofs = real_oneofs
        if extendable is not None:
            self.extendable = extendable

    @property
    def index(self):
        """Gets the index of this Descriptor.  # noqa: E501


        :return: The index of this Descriptor.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this Descriptor.


        :param index: The index of this Descriptor.  # noqa: E501
        :type: int
        """

        self._index = index

    @property
    def proto(self):
        """Gets the proto of this Descriptor.  # noqa: E501


        :return: The proto of this Descriptor.  # noqa: E501
        :rtype: DescriptorProto
        """
        return self._proto

    @proto.setter
    def proto(self, proto):
        """Sets the proto of this Descriptor.


        :param proto: The proto of this Descriptor.  # noqa: E501
        :type: DescriptorProto
        """

        self._proto = proto

    @property
    def full_name(self):
        """Gets the full_name of this Descriptor.  # noqa: E501


        :return: The full_name of this Descriptor.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this Descriptor.


        :param full_name: The full_name of this Descriptor.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

    @property
    def file(self):
        """Gets the file of this Descriptor.  # noqa: E501


        :return: The file of this Descriptor.  # noqa: E501
        :rtype: FileDescriptor
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this Descriptor.


        :param file: The file of this Descriptor.  # noqa: E501
        :type: FileDescriptor
        """

        self._file = file

    @property
    def containing_type(self):
        """Gets the containing_type of this Descriptor.  # noqa: E501


        :return: The containing_type of this Descriptor.  # noqa: E501
        :rtype: Descriptor
        """
        return self._containing_type

    @containing_type.setter
    def containing_type(self, containing_type):
        """Sets the containing_type of this Descriptor.


        :param containing_type: The containing_type of this Descriptor.  # noqa: E501
        :type: Descriptor
        """

        self._containing_type = containing_type

    @property
    def nested_types(self):
        """Gets the nested_types of this Descriptor.  # noqa: E501


        :return: The nested_types of this Descriptor.  # noqa: E501
        :rtype: list[Descriptor]
        """
        return self._nested_types

    @nested_types.setter
    def nested_types(self, nested_types):
        """Sets the nested_types of this Descriptor.


        :param nested_types: The nested_types of this Descriptor.  # noqa: E501
        :type: list[Descriptor]
        """

        self._nested_types = nested_types

    @property
    def enum_types(self):
        """Gets the enum_types of this Descriptor.  # noqa: E501


        :return: The enum_types of this Descriptor.  # noqa: E501
        :rtype: list[EnumDescriptor]
        """
        return self._enum_types

    @enum_types.setter
    def enum_types(self, enum_types):
        """Sets the enum_types of this Descriptor.


        :param enum_types: The enum_types of this Descriptor.  # noqa: E501
        :type: list[EnumDescriptor]
        """

        self._enum_types = enum_types

    @property
    def fields(self):
        """Gets the fields of this Descriptor.  # noqa: E501


        :return: The fields of this Descriptor.  # noqa: E501
        :rtype: list[FieldDescriptor]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this Descriptor.


        :param fields: The fields of this Descriptor.  # noqa: E501
        :type: list[FieldDescriptor]
        """

        self._fields = fields

    @property
    def extensions(self):
        """Gets the extensions of this Descriptor.  # noqa: E501


        :return: The extensions of this Descriptor.  # noqa: E501
        :rtype: list[FieldDescriptor]
        """
        return self._extensions

    @extensions.setter
    def extensions(self, extensions):
        """Sets the extensions of this Descriptor.


        :param extensions: The extensions of this Descriptor.  # noqa: E501
        :type: list[FieldDescriptor]
        """

        self._extensions = extensions

    @property
    def oneofs(self):
        """Gets the oneofs of this Descriptor.  # noqa: E501


        :return: The oneofs of this Descriptor.  # noqa: E501
        :rtype: list[OneofDescriptor]
        """
        return self._oneofs

    @oneofs.setter
    def oneofs(self, oneofs):
        """Sets the oneofs of this Descriptor.


        :param oneofs: The oneofs of this Descriptor.  # noqa: E501
        :type: list[OneofDescriptor]
        """

        self._oneofs = oneofs

    @property
    def name(self):
        """Gets the name of this Descriptor.  # noqa: E501


        :return: The name of this Descriptor.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Descriptor.


        :param name: The name of this Descriptor.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def options(self):
        """Gets the options of this Descriptor.  # noqa: E501


        :return: The options of this Descriptor.  # noqa: E501
        :rtype: MessageOptions
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this Descriptor.


        :param options: The options of this Descriptor.  # noqa: E501
        :type: MessageOptions
        """

        self._options = options

    @property
    def real_oneofs(self):
        """Gets the real_oneofs of this Descriptor.  # noqa: E501


        :return: The real_oneofs of this Descriptor.  # noqa: E501
        :rtype: list[OneofDescriptor]
        """
        return self._real_oneofs

    @real_oneofs.setter
    def real_oneofs(self, real_oneofs):
        """Sets the real_oneofs of this Descriptor.


        :param real_oneofs: The real_oneofs of this Descriptor.  # noqa: E501
        :type: list[OneofDescriptor]
        """

        self._real_oneofs = real_oneofs

    @property
    def extendable(self):
        """Gets the extendable of this Descriptor.  # noqa: E501


        :return: The extendable of this Descriptor.  # noqa: E501
        :rtype: bool
        """
        return self._extendable

    @extendable.setter
    def extendable(self, extendable):
        """Sets the extendable of this Descriptor.


        :param extendable: The extendable of this Descriptor.  # noqa: E501
        :type: bool
        """

        self._extendable = extendable

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
        if issubclass(Descriptor, dict):
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
        if not isinstance(other, Descriptor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
