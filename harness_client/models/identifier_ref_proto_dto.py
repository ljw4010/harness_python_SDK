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

class IdentifierRefProtoDTO(object):
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
        'account_identifier': 'StringValue',
        'org_identifier': 'StringValue',
        'project_identifier': 'StringValue',
        'metadata_map': 'dict(str, str)',
        'metadata_count': 'int',
        'initialized': 'bool',
        'identifier': 'StringValue',
        'scope': 'str',
        'metadata': 'dict(str, str)',
        'org_identifier_or_builder': 'StringValueOrBuilder',
        'account_identifier_or_builder': 'StringValueOrBuilder',
        'identifier_or_builder': 'StringValueOrBuilder',
        'scope_value': 'int',
        'project_identifier_or_builder': 'StringValueOrBuilder',
        'serialized_size': 'int',
        'parser_for_type': 'ParserIdentifierRefProtoDTO',
        'default_instance_for_type': 'IdentifierRefProtoDTO',
        'all_fields': 'dict(str, object)',
        'initialization_error_string': 'str',
        'descriptor_for_type': 'Descriptor',
        'memoized_serialized_size': 'int'
    }

    attribute_map = {
        'unknown_fields': 'unknownFields',
        'account_identifier': 'accountIdentifier',
        'org_identifier': 'orgIdentifier',
        'project_identifier': 'projectIdentifier',
        'metadata_map': 'metadataMap',
        'metadata_count': 'metadataCount',
        'initialized': 'initialized',
        'identifier': 'identifier',
        'scope': 'scope',
        'metadata': 'metadata',
        'org_identifier_or_builder': 'orgIdentifierOrBuilder',
        'account_identifier_or_builder': 'accountIdentifierOrBuilder',
        'identifier_or_builder': 'identifierOrBuilder',
        'scope_value': 'scopeValue',
        'project_identifier_or_builder': 'projectIdentifierOrBuilder',
        'serialized_size': 'serializedSize',
        'parser_for_type': 'parserForType',
        'default_instance_for_type': 'defaultInstanceForType',
        'all_fields': 'allFields',
        'initialization_error_string': 'initializationErrorString',
        'descriptor_for_type': 'descriptorForType',
        'memoized_serialized_size': 'memoizedSerializedSize'
    }

    def __init__(self, unknown_fields=None, account_identifier=None, org_identifier=None, project_identifier=None, metadata_map=None, metadata_count=None, initialized=None, identifier=None, scope=None, metadata=None, org_identifier_or_builder=None, account_identifier_or_builder=None, identifier_or_builder=None, scope_value=None, project_identifier_or_builder=None, serialized_size=None, parser_for_type=None, default_instance_for_type=None, all_fields=None, initialization_error_string=None, descriptor_for_type=None, memoized_serialized_size=None):  # noqa: E501
        """IdentifierRefProtoDTO - a model defined in Swagger"""  # noqa: E501
        self._unknown_fields = None
        self._account_identifier = None
        self._org_identifier = None
        self._project_identifier = None
        self._metadata_map = None
        self._metadata_count = None
        self._initialized = None
        self._identifier = None
        self._scope = None
        self._metadata = None
        self._org_identifier_or_builder = None
        self._account_identifier_or_builder = None
        self._identifier_or_builder = None
        self._scope_value = None
        self._project_identifier_or_builder = None
        self._serialized_size = None
        self._parser_for_type = None
        self._default_instance_for_type = None
        self._all_fields = None
        self._initialization_error_string = None
        self._descriptor_for_type = None
        self._memoized_serialized_size = None
        self.discriminator = None
        if unknown_fields is not None:
            self.unknown_fields = unknown_fields
        if account_identifier is not None:
            self.account_identifier = account_identifier
        if org_identifier is not None:
            self.org_identifier = org_identifier
        if project_identifier is not None:
            self.project_identifier = project_identifier
        if metadata_map is not None:
            self.metadata_map = metadata_map
        if metadata_count is not None:
            self.metadata_count = metadata_count
        if initialized is not None:
            self.initialized = initialized
        if identifier is not None:
            self.identifier = identifier
        if scope is not None:
            self.scope = scope
        if metadata is not None:
            self.metadata = metadata
        if org_identifier_or_builder is not None:
            self.org_identifier_or_builder = org_identifier_or_builder
        if account_identifier_or_builder is not None:
            self.account_identifier_or_builder = account_identifier_or_builder
        if identifier_or_builder is not None:
            self.identifier_or_builder = identifier_or_builder
        if scope_value is not None:
            self.scope_value = scope_value
        if project_identifier_or_builder is not None:
            self.project_identifier_or_builder = project_identifier_or_builder
        if serialized_size is not None:
            self.serialized_size = serialized_size
        if parser_for_type is not None:
            self.parser_for_type = parser_for_type
        if default_instance_for_type is not None:
            self.default_instance_for_type = default_instance_for_type
        if all_fields is not None:
            self.all_fields = all_fields
        if initialization_error_string is not None:
            self.initialization_error_string = initialization_error_string
        if descriptor_for_type is not None:
            self.descriptor_for_type = descriptor_for_type
        if memoized_serialized_size is not None:
            self.memoized_serialized_size = memoized_serialized_size

    @property
    def unknown_fields(self):
        """Gets the unknown_fields of this IdentifierRefProtoDTO.  # noqa: E501


        :return: The unknown_fields of this IdentifierRefProtoDTO.  # noqa: E501
        :rtype: UnknownFieldSet
        """
        return self._unknown_fields

    @unknown_fields.setter
    def unknown_fields(self, unknown_fields):
        """Sets the unknown_fields of this IdentifierRefProtoDTO.


        :param unknown_fields: The unknown_fields of this IdentifierRefProtoDTO.  # noqa: E501
        :type: UnknownFieldSet
        """

        self._unknown_fields = unknown_fields

    @property
    def account_identifier(self):
        """Gets the account_identifier of this IdentifierRefProtoDTO.  # noqa: E501


        :return: The account_identifier of this IdentifierRefProtoDTO.  # noqa: E501
        :rtype: StringValue
        """
        return self._account_identifier

    @account_identifier.setter
    def account_identifier(self, account_identifier):
        """Sets the account_identifier of this IdentifierRefProtoDTO.


        :param account_identifier: The account_identifier of this IdentifierRefProtoDTO.  # noqa: E501
        :type: StringValue
        """

        self._account_identifier = account_identifier

    @property
    def org_identifier(self):
        """Gets the org_identifier of this IdentifierRefProtoDTO.  # noqa: E501


        :return: The org_identifier of this IdentifierRefProtoDTO.  # noqa: E501
        :rtype: StringValue
        """
        return self._org_identifier

    @org_identifier.setter
    def org_identifier(self, org_identifier):
        """Sets the org_identifier of this IdentifierRefProtoDTO.


        :param org_identifier: The org_identifier of this IdentifierRefProtoDTO.  # noqa: E501
        :type: StringValue
        """

        self._org_identifier = org_identifier

    @property
    def project_identifier(self):
        """Gets the project_identifier of this IdentifierRefProtoDTO.  # noqa: E501


        :return: The project_identifier of this IdentifierRefProtoDTO.  # noqa: E501
        :rtype: StringValue
        """
        return self._project_identifier

    @project_identifier.setter
    def project_identifier(self, project_identifier):
        """Sets the project_identifier of this IdentifierRefProtoDTO.


        :param project_identifier: The project_identifier of this IdentifierRefProtoDTO.  # noqa: E501
        :type: StringValue
        """

        self._project_identifier = project_identifier

    @property
    def metadata_map(self):
        """Gets the metadata_map of this IdentifierRefProtoDTO.  # noqa: E501


        :return: The metadata_map of this IdentifierRefProtoDTO.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._metadata_map

    @metadata_map.setter
    def metadata_map(self, metadata_map):
        """Sets the metadata_map of this IdentifierRefProtoDTO.


        :param metadata_map: The metadata_map of this IdentifierRefProtoDTO.  # noqa: E501
        :type: dict(str, str)
        """

        self._metadata_map = metadata_map

    @property
    def metadata_count(self):
        """Gets the metadata_count of this IdentifierRefProtoDTO.  # noqa: E501


        :return: The metadata_count of this IdentifierRefProtoDTO.  # noqa: E501
        :rtype: int
        """
        return self._metadata_count

    @metadata_count.setter
    def metadata_count(self, metadata_count):
        """Sets the metadata_count of this IdentifierRefProtoDTO.


        :param metadata_count: The metadata_count of this IdentifierRefProtoDTO.  # noqa: E501
        :type: int
        """

        self._metadata_count = metadata_count

    @property
    def initialized(self):
        """Gets the initialized of this IdentifierRefProtoDTO.  # noqa: E501


        :return: The initialized of this IdentifierRefProtoDTO.  # noqa: E501
        :rtype: bool
        """
        return self._initialized

    @initialized.setter
    def initialized(self, initialized):
        """Sets the initialized of this IdentifierRefProtoDTO.


        :param initialized: The initialized of this IdentifierRefProtoDTO.  # noqa: E501
        :type: bool
        """

        self._initialized = initialized

    @property
    def identifier(self):
        """Gets the identifier of this IdentifierRefProtoDTO.  # noqa: E501


        :return: The identifier of this IdentifierRefProtoDTO.  # noqa: E501
        :rtype: StringValue
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this IdentifierRefProtoDTO.


        :param identifier: The identifier of this IdentifierRefProtoDTO.  # noqa: E501
        :type: StringValue
        """

        self._identifier = identifier

    @property
    def scope(self):
        """Gets the scope of this IdentifierRefProtoDTO.  # noqa: E501


        :return: The scope of this IdentifierRefProtoDTO.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this IdentifierRefProtoDTO.


        :param scope: The scope of this IdentifierRefProtoDTO.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACCOUNT", "ORG", "PROJECT", "UNKNOWN", "UNRECOGNIZED"]  # noqa: E501
        if scope not in allowed_values:
            raise ValueError(
                "Invalid value for `scope` ({0}), must be one of {1}"  # noqa: E501
                .format(scope, allowed_values)
            )

        self._scope = scope

    @property
    def metadata(self):
        """Gets the metadata of this IdentifierRefProtoDTO.  # noqa: E501


        :return: The metadata of this IdentifierRefProtoDTO.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this IdentifierRefProtoDTO.


        :param metadata: The metadata of this IdentifierRefProtoDTO.  # noqa: E501
        :type: dict(str, str)
        """

        self._metadata = metadata

    @property
    def org_identifier_or_builder(self):
        """Gets the org_identifier_or_builder of this IdentifierRefProtoDTO.  # noqa: E501


        :return: The org_identifier_or_builder of this IdentifierRefProtoDTO.  # noqa: E501
        :rtype: StringValueOrBuilder
        """
        return self._org_identifier_or_builder

    @org_identifier_or_builder.setter
    def org_identifier_or_builder(self, org_identifier_or_builder):
        """Sets the org_identifier_or_builder of this IdentifierRefProtoDTO.


        :param org_identifier_or_builder: The org_identifier_or_builder of this IdentifierRefProtoDTO.  # noqa: E501
        :type: StringValueOrBuilder
        """

        self._org_identifier_or_builder = org_identifier_or_builder

    @property
    def account_identifier_or_builder(self):
        """Gets the account_identifier_or_builder of this IdentifierRefProtoDTO.  # noqa: E501


        :return: The account_identifier_or_builder of this IdentifierRefProtoDTO.  # noqa: E501
        :rtype: StringValueOrBuilder
        """
        return self._account_identifier_or_builder

    @account_identifier_or_builder.setter
    def account_identifier_or_builder(self, account_identifier_or_builder):
        """Sets the account_identifier_or_builder of this IdentifierRefProtoDTO.


        :param account_identifier_or_builder: The account_identifier_or_builder of this IdentifierRefProtoDTO.  # noqa: E501
        :type: StringValueOrBuilder
        """

        self._account_identifier_or_builder = account_identifier_or_builder

    @property
    def identifier_or_builder(self):
        """Gets the identifier_or_builder of this IdentifierRefProtoDTO.  # noqa: E501


        :return: The identifier_or_builder of this IdentifierRefProtoDTO.  # noqa: E501
        :rtype: StringValueOrBuilder
        """
        return self._identifier_or_builder

    @identifier_or_builder.setter
    def identifier_or_builder(self, identifier_or_builder):
        """Sets the identifier_or_builder of this IdentifierRefProtoDTO.


        :param identifier_or_builder: The identifier_or_builder of this IdentifierRefProtoDTO.  # noqa: E501
        :type: StringValueOrBuilder
        """

        self._identifier_or_builder = identifier_or_builder

    @property
    def scope_value(self):
        """Gets the scope_value of this IdentifierRefProtoDTO.  # noqa: E501


        :return: The scope_value of this IdentifierRefProtoDTO.  # noqa: E501
        :rtype: int
        """
        return self._scope_value

    @scope_value.setter
    def scope_value(self, scope_value):
        """Sets the scope_value of this IdentifierRefProtoDTO.


        :param scope_value: The scope_value of this IdentifierRefProtoDTO.  # noqa: E501
        :type: int
        """

        self._scope_value = scope_value

    @property
    def project_identifier_or_builder(self):
        """Gets the project_identifier_or_builder of this IdentifierRefProtoDTO.  # noqa: E501


        :return: The project_identifier_or_builder of this IdentifierRefProtoDTO.  # noqa: E501
        :rtype: StringValueOrBuilder
        """
        return self._project_identifier_or_builder

    @project_identifier_or_builder.setter
    def project_identifier_or_builder(self, project_identifier_or_builder):
        """Sets the project_identifier_or_builder of this IdentifierRefProtoDTO.


        :param project_identifier_or_builder: The project_identifier_or_builder of this IdentifierRefProtoDTO.  # noqa: E501
        :type: StringValueOrBuilder
        """

        self._project_identifier_or_builder = project_identifier_or_builder

    @property
    def serialized_size(self):
        """Gets the serialized_size of this IdentifierRefProtoDTO.  # noqa: E501


        :return: The serialized_size of this IdentifierRefProtoDTO.  # noqa: E501
        :rtype: int
        """
        return self._serialized_size

    @serialized_size.setter
    def serialized_size(self, serialized_size):
        """Sets the serialized_size of this IdentifierRefProtoDTO.


        :param serialized_size: The serialized_size of this IdentifierRefProtoDTO.  # noqa: E501
        :type: int
        """

        self._serialized_size = serialized_size

    @property
    def parser_for_type(self):
        """Gets the parser_for_type of this IdentifierRefProtoDTO.  # noqa: E501


        :return: The parser_for_type of this IdentifierRefProtoDTO.  # noqa: E501
        :rtype: ParserIdentifierRefProtoDTO
        """
        return self._parser_for_type

    @parser_for_type.setter
    def parser_for_type(self, parser_for_type):
        """Sets the parser_for_type of this IdentifierRefProtoDTO.


        :param parser_for_type: The parser_for_type of this IdentifierRefProtoDTO.  # noqa: E501
        :type: ParserIdentifierRefProtoDTO
        """

        self._parser_for_type = parser_for_type

    @property
    def default_instance_for_type(self):
        """Gets the default_instance_for_type of this IdentifierRefProtoDTO.  # noqa: E501


        :return: The default_instance_for_type of this IdentifierRefProtoDTO.  # noqa: E501
        :rtype: IdentifierRefProtoDTO
        """
        return self._default_instance_for_type

    @default_instance_for_type.setter
    def default_instance_for_type(self, default_instance_for_type):
        """Sets the default_instance_for_type of this IdentifierRefProtoDTO.


        :param default_instance_for_type: The default_instance_for_type of this IdentifierRefProtoDTO.  # noqa: E501
        :type: IdentifierRefProtoDTO
        """

        self._default_instance_for_type = default_instance_for_type

    @property
    def all_fields(self):
        """Gets the all_fields of this IdentifierRefProtoDTO.  # noqa: E501


        :return: The all_fields of this IdentifierRefProtoDTO.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._all_fields

    @all_fields.setter
    def all_fields(self, all_fields):
        """Sets the all_fields of this IdentifierRefProtoDTO.


        :param all_fields: The all_fields of this IdentifierRefProtoDTO.  # noqa: E501
        :type: dict(str, object)
        """

        self._all_fields = all_fields

    @property
    def initialization_error_string(self):
        """Gets the initialization_error_string of this IdentifierRefProtoDTO.  # noqa: E501


        :return: The initialization_error_string of this IdentifierRefProtoDTO.  # noqa: E501
        :rtype: str
        """
        return self._initialization_error_string

    @initialization_error_string.setter
    def initialization_error_string(self, initialization_error_string):
        """Sets the initialization_error_string of this IdentifierRefProtoDTO.


        :param initialization_error_string: The initialization_error_string of this IdentifierRefProtoDTO.  # noqa: E501
        :type: str
        """

        self._initialization_error_string = initialization_error_string

    @property
    def descriptor_for_type(self):
        """Gets the descriptor_for_type of this IdentifierRefProtoDTO.  # noqa: E501


        :return: The descriptor_for_type of this IdentifierRefProtoDTO.  # noqa: E501
        :rtype: Descriptor
        """
        return self._descriptor_for_type

    @descriptor_for_type.setter
    def descriptor_for_type(self, descriptor_for_type):
        """Sets the descriptor_for_type of this IdentifierRefProtoDTO.


        :param descriptor_for_type: The descriptor_for_type of this IdentifierRefProtoDTO.  # noqa: E501
        :type: Descriptor
        """

        self._descriptor_for_type = descriptor_for_type

    @property
    def memoized_serialized_size(self):
        """Gets the memoized_serialized_size of this IdentifierRefProtoDTO.  # noqa: E501


        :return: The memoized_serialized_size of this IdentifierRefProtoDTO.  # noqa: E501
        :rtype: int
        """
        return self._memoized_serialized_size

    @memoized_serialized_size.setter
    def memoized_serialized_size(self, memoized_serialized_size):
        """Sets the memoized_serialized_size of this IdentifierRefProtoDTO.


        :param memoized_serialized_size: The memoized_serialized_size of this IdentifierRefProtoDTO.  # noqa: E501
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
        if issubclass(IdentifierRefProtoDTO, dict):
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
        if not isinstance(other, IdentifierRefProtoDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
