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

class StrategyMetadataOrBuilder(object):
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
        'current_iteration': 'int',
        'total_iterations': 'int',
        'matrix_metadata': 'MatrixMetadata',
        'for_metadata': 'ForMetadata',
        'for_metadata_or_builder': 'ForMetadataOrBuilder',
        'identifier_post_fix': 'str',
        'identifier_post_fix_bytes': 'ByteString',
        'metadata_case': 'str',
        'matrix_metadata_or_builder': 'MatrixMetadataOrBuilder',
        'all_fields': 'dict(str, object)',
        'descriptor_for_type': 'Descriptor',
        'initialization_error_string': 'str',
        'default_instance_for_type': 'Message',
        'unknown_fields': 'UnknownFieldSet',
        'initialized': 'bool'
    }

    attribute_map = {
        'current_iteration': 'currentIteration',
        'total_iterations': 'totalIterations',
        'matrix_metadata': 'matrixMetadata',
        'for_metadata': 'forMetadata',
        'for_metadata_or_builder': 'forMetadataOrBuilder',
        'identifier_post_fix': 'identifierPostFix',
        'identifier_post_fix_bytes': 'identifierPostFixBytes',
        'metadata_case': 'metadataCase',
        'matrix_metadata_or_builder': 'matrixMetadataOrBuilder',
        'all_fields': 'allFields',
        'descriptor_for_type': 'descriptorForType',
        'initialization_error_string': 'initializationErrorString',
        'default_instance_for_type': 'defaultInstanceForType',
        'unknown_fields': 'unknownFields',
        'initialized': 'initialized'
    }

    def __init__(self, current_iteration=None, total_iterations=None, matrix_metadata=None, for_metadata=None, for_metadata_or_builder=None, identifier_post_fix=None, identifier_post_fix_bytes=None, metadata_case=None, matrix_metadata_or_builder=None, all_fields=None, descriptor_for_type=None, initialization_error_string=None, default_instance_for_type=None, unknown_fields=None, initialized=None):  # noqa: E501
        """StrategyMetadataOrBuilder - a model defined in Swagger"""  # noqa: E501
        self._current_iteration = None
        self._total_iterations = None
        self._matrix_metadata = None
        self._for_metadata = None
        self._for_metadata_or_builder = None
        self._identifier_post_fix = None
        self._identifier_post_fix_bytes = None
        self._metadata_case = None
        self._matrix_metadata_or_builder = None
        self._all_fields = None
        self._descriptor_for_type = None
        self._initialization_error_string = None
        self._default_instance_for_type = None
        self._unknown_fields = None
        self._initialized = None
        self.discriminator = None
        if current_iteration is not None:
            self.current_iteration = current_iteration
        if total_iterations is not None:
            self.total_iterations = total_iterations
        if matrix_metadata is not None:
            self.matrix_metadata = matrix_metadata
        if for_metadata is not None:
            self.for_metadata = for_metadata
        if for_metadata_or_builder is not None:
            self.for_metadata_or_builder = for_metadata_or_builder
        if identifier_post_fix is not None:
            self.identifier_post_fix = identifier_post_fix
        if identifier_post_fix_bytes is not None:
            self.identifier_post_fix_bytes = identifier_post_fix_bytes
        if metadata_case is not None:
            self.metadata_case = metadata_case
        if matrix_metadata_or_builder is not None:
            self.matrix_metadata_or_builder = matrix_metadata_or_builder
        if all_fields is not None:
            self.all_fields = all_fields
        if descriptor_for_type is not None:
            self.descriptor_for_type = descriptor_for_type
        if initialization_error_string is not None:
            self.initialization_error_string = initialization_error_string
        if default_instance_for_type is not None:
            self.default_instance_for_type = default_instance_for_type
        if unknown_fields is not None:
            self.unknown_fields = unknown_fields
        if initialized is not None:
            self.initialized = initialized

    @property
    def current_iteration(self):
        """Gets the current_iteration of this StrategyMetadataOrBuilder.  # noqa: E501


        :return: The current_iteration of this StrategyMetadataOrBuilder.  # noqa: E501
        :rtype: int
        """
        return self._current_iteration

    @current_iteration.setter
    def current_iteration(self, current_iteration):
        """Sets the current_iteration of this StrategyMetadataOrBuilder.


        :param current_iteration: The current_iteration of this StrategyMetadataOrBuilder.  # noqa: E501
        :type: int
        """

        self._current_iteration = current_iteration

    @property
    def total_iterations(self):
        """Gets the total_iterations of this StrategyMetadataOrBuilder.  # noqa: E501


        :return: The total_iterations of this StrategyMetadataOrBuilder.  # noqa: E501
        :rtype: int
        """
        return self._total_iterations

    @total_iterations.setter
    def total_iterations(self, total_iterations):
        """Sets the total_iterations of this StrategyMetadataOrBuilder.


        :param total_iterations: The total_iterations of this StrategyMetadataOrBuilder.  # noqa: E501
        :type: int
        """

        self._total_iterations = total_iterations

    @property
    def matrix_metadata(self):
        """Gets the matrix_metadata of this StrategyMetadataOrBuilder.  # noqa: E501


        :return: The matrix_metadata of this StrategyMetadataOrBuilder.  # noqa: E501
        :rtype: MatrixMetadata
        """
        return self._matrix_metadata

    @matrix_metadata.setter
    def matrix_metadata(self, matrix_metadata):
        """Sets the matrix_metadata of this StrategyMetadataOrBuilder.


        :param matrix_metadata: The matrix_metadata of this StrategyMetadataOrBuilder.  # noqa: E501
        :type: MatrixMetadata
        """

        self._matrix_metadata = matrix_metadata

    @property
    def for_metadata(self):
        """Gets the for_metadata of this StrategyMetadataOrBuilder.  # noqa: E501


        :return: The for_metadata of this StrategyMetadataOrBuilder.  # noqa: E501
        :rtype: ForMetadata
        """
        return self._for_metadata

    @for_metadata.setter
    def for_metadata(self, for_metadata):
        """Sets the for_metadata of this StrategyMetadataOrBuilder.


        :param for_metadata: The for_metadata of this StrategyMetadataOrBuilder.  # noqa: E501
        :type: ForMetadata
        """

        self._for_metadata = for_metadata

    @property
    def for_metadata_or_builder(self):
        """Gets the for_metadata_or_builder of this StrategyMetadataOrBuilder.  # noqa: E501


        :return: The for_metadata_or_builder of this StrategyMetadataOrBuilder.  # noqa: E501
        :rtype: ForMetadataOrBuilder
        """
        return self._for_metadata_or_builder

    @for_metadata_or_builder.setter
    def for_metadata_or_builder(self, for_metadata_or_builder):
        """Sets the for_metadata_or_builder of this StrategyMetadataOrBuilder.


        :param for_metadata_or_builder: The for_metadata_or_builder of this StrategyMetadataOrBuilder.  # noqa: E501
        :type: ForMetadataOrBuilder
        """

        self._for_metadata_or_builder = for_metadata_or_builder

    @property
    def identifier_post_fix(self):
        """Gets the identifier_post_fix of this StrategyMetadataOrBuilder.  # noqa: E501


        :return: The identifier_post_fix of this StrategyMetadataOrBuilder.  # noqa: E501
        :rtype: str
        """
        return self._identifier_post_fix

    @identifier_post_fix.setter
    def identifier_post_fix(self, identifier_post_fix):
        """Sets the identifier_post_fix of this StrategyMetadataOrBuilder.


        :param identifier_post_fix: The identifier_post_fix of this StrategyMetadataOrBuilder.  # noqa: E501
        :type: str
        """

        self._identifier_post_fix = identifier_post_fix

    @property
    def identifier_post_fix_bytes(self):
        """Gets the identifier_post_fix_bytes of this StrategyMetadataOrBuilder.  # noqa: E501


        :return: The identifier_post_fix_bytes of this StrategyMetadataOrBuilder.  # noqa: E501
        :rtype: ByteString
        """
        return self._identifier_post_fix_bytes

    @identifier_post_fix_bytes.setter
    def identifier_post_fix_bytes(self, identifier_post_fix_bytes):
        """Sets the identifier_post_fix_bytes of this StrategyMetadataOrBuilder.


        :param identifier_post_fix_bytes: The identifier_post_fix_bytes of this StrategyMetadataOrBuilder.  # noqa: E501
        :type: ByteString
        """

        self._identifier_post_fix_bytes = identifier_post_fix_bytes

    @property
    def metadata_case(self):
        """Gets the metadata_case of this StrategyMetadataOrBuilder.  # noqa: E501


        :return: The metadata_case of this StrategyMetadataOrBuilder.  # noqa: E501
        :rtype: str
        """
        return self._metadata_case

    @metadata_case.setter
    def metadata_case(self, metadata_case):
        """Sets the metadata_case of this StrategyMetadataOrBuilder.


        :param metadata_case: The metadata_case of this StrategyMetadataOrBuilder.  # noqa: E501
        :type: str
        """
        allowed_values = ["MATRIXMETADATA", "FORMETADATA", "METADATA_NOT_SET"]  # noqa: E501
        if metadata_case not in allowed_values:
            raise ValueError(
                "Invalid value for `metadata_case` ({0}), must be one of {1}"  # noqa: E501
                .format(metadata_case, allowed_values)
            )

        self._metadata_case = metadata_case

    @property
    def matrix_metadata_or_builder(self):
        """Gets the matrix_metadata_or_builder of this StrategyMetadataOrBuilder.  # noqa: E501


        :return: The matrix_metadata_or_builder of this StrategyMetadataOrBuilder.  # noqa: E501
        :rtype: MatrixMetadataOrBuilder
        """
        return self._matrix_metadata_or_builder

    @matrix_metadata_or_builder.setter
    def matrix_metadata_or_builder(self, matrix_metadata_or_builder):
        """Sets the matrix_metadata_or_builder of this StrategyMetadataOrBuilder.


        :param matrix_metadata_or_builder: The matrix_metadata_or_builder of this StrategyMetadataOrBuilder.  # noqa: E501
        :type: MatrixMetadataOrBuilder
        """

        self._matrix_metadata_or_builder = matrix_metadata_or_builder

    @property
    def all_fields(self):
        """Gets the all_fields of this StrategyMetadataOrBuilder.  # noqa: E501


        :return: The all_fields of this StrategyMetadataOrBuilder.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._all_fields

    @all_fields.setter
    def all_fields(self, all_fields):
        """Sets the all_fields of this StrategyMetadataOrBuilder.


        :param all_fields: The all_fields of this StrategyMetadataOrBuilder.  # noqa: E501
        :type: dict(str, object)
        """

        self._all_fields = all_fields

    @property
    def descriptor_for_type(self):
        """Gets the descriptor_for_type of this StrategyMetadataOrBuilder.  # noqa: E501


        :return: The descriptor_for_type of this StrategyMetadataOrBuilder.  # noqa: E501
        :rtype: Descriptor
        """
        return self._descriptor_for_type

    @descriptor_for_type.setter
    def descriptor_for_type(self, descriptor_for_type):
        """Sets the descriptor_for_type of this StrategyMetadataOrBuilder.


        :param descriptor_for_type: The descriptor_for_type of this StrategyMetadataOrBuilder.  # noqa: E501
        :type: Descriptor
        """

        self._descriptor_for_type = descriptor_for_type

    @property
    def initialization_error_string(self):
        """Gets the initialization_error_string of this StrategyMetadataOrBuilder.  # noqa: E501


        :return: The initialization_error_string of this StrategyMetadataOrBuilder.  # noqa: E501
        :rtype: str
        """
        return self._initialization_error_string

    @initialization_error_string.setter
    def initialization_error_string(self, initialization_error_string):
        """Sets the initialization_error_string of this StrategyMetadataOrBuilder.


        :param initialization_error_string: The initialization_error_string of this StrategyMetadataOrBuilder.  # noqa: E501
        :type: str
        """

        self._initialization_error_string = initialization_error_string

    @property
    def default_instance_for_type(self):
        """Gets the default_instance_for_type of this StrategyMetadataOrBuilder.  # noqa: E501


        :return: The default_instance_for_type of this StrategyMetadataOrBuilder.  # noqa: E501
        :rtype: Message
        """
        return self._default_instance_for_type

    @default_instance_for_type.setter
    def default_instance_for_type(self, default_instance_for_type):
        """Sets the default_instance_for_type of this StrategyMetadataOrBuilder.


        :param default_instance_for_type: The default_instance_for_type of this StrategyMetadataOrBuilder.  # noqa: E501
        :type: Message
        """

        self._default_instance_for_type = default_instance_for_type

    @property
    def unknown_fields(self):
        """Gets the unknown_fields of this StrategyMetadataOrBuilder.  # noqa: E501


        :return: The unknown_fields of this StrategyMetadataOrBuilder.  # noqa: E501
        :rtype: UnknownFieldSet
        """
        return self._unknown_fields

    @unknown_fields.setter
    def unknown_fields(self, unknown_fields):
        """Sets the unknown_fields of this StrategyMetadataOrBuilder.


        :param unknown_fields: The unknown_fields of this StrategyMetadataOrBuilder.  # noqa: E501
        :type: UnknownFieldSet
        """

        self._unknown_fields = unknown_fields

    @property
    def initialized(self):
        """Gets the initialized of this StrategyMetadataOrBuilder.  # noqa: E501


        :return: The initialized of this StrategyMetadataOrBuilder.  # noqa: E501
        :rtype: bool
        """
        return self._initialized

    @initialized.setter
    def initialized(self, initialized):
        """Sets the initialized of this StrategyMetadataOrBuilder.


        :param initialized: The initialized of this StrategyMetadataOrBuilder.  # noqa: E501
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
        if issubclass(StrategyMetadataOrBuilder, dict):
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
        if not isinstance(other, StrategyMetadataOrBuilder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
