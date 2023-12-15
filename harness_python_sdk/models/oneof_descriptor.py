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

class OneofDescriptor(object):
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
        'proto': 'OneofDescriptorProto',
        'full_name': 'str',
        'file': 'FileDescriptor',
        'containing_type': 'Descriptor',
        'field_count': 'int',
        'fields': 'list[FieldDescriptor]',
        'name': 'str',
        'synthetic': 'bool',
        'options': 'OneofOptions'
    }

    attribute_map = {
        'index': 'index',
        'proto': 'proto',
        'full_name': 'fullName',
        'file': 'file',
        'containing_type': 'containingType',
        'field_count': 'fieldCount',
        'fields': 'fields',
        'name': 'name',
        'synthetic': 'synthetic',
        'options': 'options'
    }

    def __init__(self, index=None, proto=None, full_name=None, file=None, containing_type=None, field_count=None, fields=None, name=None, synthetic=None, options=None):  # noqa: E501
        """OneofDescriptor - a model defined in Swagger"""  # noqa: E501
        self._index = None
        self._proto = None
        self._full_name = None
        self._file = None
        self._containing_type = None
        self._field_count = None
        self._fields = None
        self._name = None
        self._synthetic = None
        self._options = None
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
        if field_count is not None:
            self.field_count = field_count
        if fields is not None:
            self.fields = fields
        if name is not None:
            self.name = name
        if synthetic is not None:
            self.synthetic = synthetic
        if options is not None:
            self.options = options

    @property
    def index(self):
        """Gets the index of this OneofDescriptor.  # noqa: E501


        :return: The index of this OneofDescriptor.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this OneofDescriptor.


        :param index: The index of this OneofDescriptor.  # noqa: E501
        :type: int
        """

        self._index = index

    @property
    def proto(self):
        """Gets the proto of this OneofDescriptor.  # noqa: E501


        :return: The proto of this OneofDescriptor.  # noqa: E501
        :rtype: OneofDescriptorProto
        """
        return self._proto

    @proto.setter
    def proto(self, proto):
        """Sets the proto of this OneofDescriptor.


        :param proto: The proto of this OneofDescriptor.  # noqa: E501
        :type: OneofDescriptorProto
        """

        self._proto = proto

    @property
    def full_name(self):
        """Gets the full_name of this OneofDescriptor.  # noqa: E501


        :return: The full_name of this OneofDescriptor.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this OneofDescriptor.


        :param full_name: The full_name of this OneofDescriptor.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

    @property
    def file(self):
        """Gets the file of this OneofDescriptor.  # noqa: E501


        :return: The file of this OneofDescriptor.  # noqa: E501
        :rtype: FileDescriptor
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this OneofDescriptor.


        :param file: The file of this OneofDescriptor.  # noqa: E501
        :type: FileDescriptor
        """

        self._file = file

    @property
    def containing_type(self):
        """Gets the containing_type of this OneofDescriptor.  # noqa: E501


        :return: The containing_type of this OneofDescriptor.  # noqa: E501
        :rtype: Descriptor
        """
        return self._containing_type

    @containing_type.setter
    def containing_type(self, containing_type):
        """Sets the containing_type of this OneofDescriptor.


        :param containing_type: The containing_type of this OneofDescriptor.  # noqa: E501
        :type: Descriptor
        """

        self._containing_type = containing_type

    @property
    def field_count(self):
        """Gets the field_count of this OneofDescriptor.  # noqa: E501


        :return: The field_count of this OneofDescriptor.  # noqa: E501
        :rtype: int
        """
        return self._field_count

    @field_count.setter
    def field_count(self, field_count):
        """Sets the field_count of this OneofDescriptor.


        :param field_count: The field_count of this OneofDescriptor.  # noqa: E501
        :type: int
        """

        self._field_count = field_count

    @property
    def fields(self):
        """Gets the fields of this OneofDescriptor.  # noqa: E501


        :return: The fields of this OneofDescriptor.  # noqa: E501
        :rtype: list[FieldDescriptor]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this OneofDescriptor.


        :param fields: The fields of this OneofDescriptor.  # noqa: E501
        :type: list[FieldDescriptor]
        """

        self._fields = fields

    @property
    def name(self):
        """Gets the name of this OneofDescriptor.  # noqa: E501


        :return: The name of this OneofDescriptor.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OneofDescriptor.


        :param name: The name of this OneofDescriptor.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def synthetic(self):
        """Gets the synthetic of this OneofDescriptor.  # noqa: E501


        :return: The synthetic of this OneofDescriptor.  # noqa: E501
        :rtype: bool
        """
        return self._synthetic

    @synthetic.setter
    def synthetic(self, synthetic):
        """Sets the synthetic of this OneofDescriptor.


        :param synthetic: The synthetic of this OneofDescriptor.  # noqa: E501
        :type: bool
        """

        self._synthetic = synthetic

    @property
    def options(self):
        """Gets the options of this OneofDescriptor.  # noqa: E501


        :return: The options of this OneofDescriptor.  # noqa: E501
        :rtype: OneofOptions
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this OneofDescriptor.


        :param options: The options of this OneofDescriptor.  # noqa: E501
        :type: OneofOptions
        """

        self._options = options

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
        if issubclass(OneofDescriptor, dict):
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
        if not isinstance(other, OneofDescriptor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other