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

class FileDescriptor(object):
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
        'proto': 'FileDescriptorProto',
        'message_types': 'list[Descriptor]',
        'enum_types': 'list[EnumDescriptor]',
        'services': 'list[ServiceDescriptor]',
        'extensions': 'list[FieldDescriptor]',
        'dependencies': 'list[FileDescriptor]',
        'public_dependencies': 'list[FileDescriptor]',
        'name': 'str',
        'package': 'str',
        'file': 'FileDescriptor',
        'full_name': 'str',
        'options': 'FileOptions',
        'syntax': 'str'
    }

    attribute_map = {
        'proto': 'proto',
        'message_types': 'messageTypes',
        'enum_types': 'enumTypes',
        'services': 'services',
        'extensions': 'extensions',
        'dependencies': 'dependencies',
        'public_dependencies': 'publicDependencies',
        'name': 'name',
        'package': 'package',
        'file': 'file',
        'full_name': 'fullName',
        'options': 'options',
        'syntax': 'syntax'
    }

    def __init__(self, proto=None, message_types=None, enum_types=None, services=None, extensions=None, dependencies=None, public_dependencies=None, name=None, package=None, file=None, full_name=None, options=None, syntax=None):  # noqa: E501
        """FileDescriptor - a model defined in Swagger"""  # noqa: E501
        self._proto = None
        self._message_types = None
        self._enum_types = None
        self._services = None
        self._extensions = None
        self._dependencies = None
        self._public_dependencies = None
        self._name = None
        self._package = None
        self._file = None
        self._full_name = None
        self._options = None
        self._syntax = None
        self.discriminator = None
        if proto is not None:
            self.proto = proto
        if message_types is not None:
            self.message_types = message_types
        if enum_types is not None:
            self.enum_types = enum_types
        if services is not None:
            self.services = services
        if extensions is not None:
            self.extensions = extensions
        if dependencies is not None:
            self.dependencies = dependencies
        if public_dependencies is not None:
            self.public_dependencies = public_dependencies
        if name is not None:
            self.name = name
        if package is not None:
            self.package = package
        if file is not None:
            self.file = file
        if full_name is not None:
            self.full_name = full_name
        if options is not None:
            self.options = options
        if syntax is not None:
            self.syntax = syntax

    @property
    def proto(self):
        """Gets the proto of this FileDescriptor.  # noqa: E501


        :return: The proto of this FileDescriptor.  # noqa: E501
        :rtype: FileDescriptorProto
        """
        return self._proto

    @proto.setter
    def proto(self, proto):
        """Sets the proto of this FileDescriptor.


        :param proto: The proto of this FileDescriptor.  # noqa: E501
        :type: FileDescriptorProto
        """

        self._proto = proto

    @property
    def message_types(self):
        """Gets the message_types of this FileDescriptor.  # noqa: E501


        :return: The message_types of this FileDescriptor.  # noqa: E501
        :rtype: list[Descriptor]
        """
        return self._message_types

    @message_types.setter
    def message_types(self, message_types):
        """Sets the message_types of this FileDescriptor.


        :param message_types: The message_types of this FileDescriptor.  # noqa: E501
        :type: list[Descriptor]
        """

        self._message_types = message_types

    @property
    def enum_types(self):
        """Gets the enum_types of this FileDescriptor.  # noqa: E501


        :return: The enum_types of this FileDescriptor.  # noqa: E501
        :rtype: list[EnumDescriptor]
        """
        return self._enum_types

    @enum_types.setter
    def enum_types(self, enum_types):
        """Sets the enum_types of this FileDescriptor.


        :param enum_types: The enum_types of this FileDescriptor.  # noqa: E501
        :type: list[EnumDescriptor]
        """

        self._enum_types = enum_types

    @property
    def services(self):
        """Gets the services of this FileDescriptor.  # noqa: E501


        :return: The services of this FileDescriptor.  # noqa: E501
        :rtype: list[ServiceDescriptor]
        """
        return self._services

    @services.setter
    def services(self, services):
        """Sets the services of this FileDescriptor.


        :param services: The services of this FileDescriptor.  # noqa: E501
        :type: list[ServiceDescriptor]
        """

        self._services = services

    @property
    def extensions(self):
        """Gets the extensions of this FileDescriptor.  # noqa: E501


        :return: The extensions of this FileDescriptor.  # noqa: E501
        :rtype: list[FieldDescriptor]
        """
        return self._extensions

    @extensions.setter
    def extensions(self, extensions):
        """Sets the extensions of this FileDescriptor.


        :param extensions: The extensions of this FileDescriptor.  # noqa: E501
        :type: list[FieldDescriptor]
        """

        self._extensions = extensions

    @property
    def dependencies(self):
        """Gets the dependencies of this FileDescriptor.  # noqa: E501


        :return: The dependencies of this FileDescriptor.  # noqa: E501
        :rtype: list[FileDescriptor]
        """
        return self._dependencies

    @dependencies.setter
    def dependencies(self, dependencies):
        """Sets the dependencies of this FileDescriptor.


        :param dependencies: The dependencies of this FileDescriptor.  # noqa: E501
        :type: list[FileDescriptor]
        """

        self._dependencies = dependencies

    @property
    def public_dependencies(self):
        """Gets the public_dependencies of this FileDescriptor.  # noqa: E501


        :return: The public_dependencies of this FileDescriptor.  # noqa: E501
        :rtype: list[FileDescriptor]
        """
        return self._public_dependencies

    @public_dependencies.setter
    def public_dependencies(self, public_dependencies):
        """Sets the public_dependencies of this FileDescriptor.


        :param public_dependencies: The public_dependencies of this FileDescriptor.  # noqa: E501
        :type: list[FileDescriptor]
        """

        self._public_dependencies = public_dependencies

    @property
    def name(self):
        """Gets the name of this FileDescriptor.  # noqa: E501


        :return: The name of this FileDescriptor.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FileDescriptor.


        :param name: The name of this FileDescriptor.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def package(self):
        """Gets the package of this FileDescriptor.  # noqa: E501


        :return: The package of this FileDescriptor.  # noqa: E501
        :rtype: str
        """
        return self._package

    @package.setter
    def package(self, package):
        """Sets the package of this FileDescriptor.


        :param package: The package of this FileDescriptor.  # noqa: E501
        :type: str
        """

        self._package = package

    @property
    def file(self):
        """Gets the file of this FileDescriptor.  # noqa: E501


        :return: The file of this FileDescriptor.  # noqa: E501
        :rtype: FileDescriptor
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this FileDescriptor.


        :param file: The file of this FileDescriptor.  # noqa: E501
        :type: FileDescriptor
        """

        self._file = file

    @property
    def full_name(self):
        """Gets the full_name of this FileDescriptor.  # noqa: E501


        :return: The full_name of this FileDescriptor.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this FileDescriptor.


        :param full_name: The full_name of this FileDescriptor.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

    @property
    def options(self):
        """Gets the options of this FileDescriptor.  # noqa: E501


        :return: The options of this FileDescriptor.  # noqa: E501
        :rtype: FileOptions
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this FileDescriptor.


        :param options: The options of this FileDescriptor.  # noqa: E501
        :type: FileOptions
        """

        self._options = options

    @property
    def syntax(self):
        """Gets the syntax of this FileDescriptor.  # noqa: E501


        :return: The syntax of this FileDescriptor.  # noqa: E501
        :rtype: str
        """
        return self._syntax

    @syntax.setter
    def syntax(self, syntax):
        """Sets the syntax of this FileDescriptor.


        :param syntax: The syntax of this FileDescriptor.  # noqa: E501
        :type: str
        """
        allowed_values = ["UNKNOWN", "PROTO2", "PROTO3"]  # noqa: E501
        if syntax not in allowed_values:
            raise ValueError(
                "Invalid value for `syntax` ({0}), must be one of {1}"  # noqa: E501
                .format(syntax, allowed_values)
            )

        self._syntax = syntax

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
        if issubclass(FileDescriptor, dict):
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
        if not isinstance(other, FileDescriptor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
