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

class FileOptionsOrBuilder(object):
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
        'php_metadata_namespace_bytes': 'ByteString',
        'uninterpreted_option_count': 'int',
        'java_package': 'str',
        'java_package_bytes': 'ByteString',
        'java_outer_classname': 'str',
        'java_outer_classname_bytes': 'ByteString',
        'java_multiple_files': 'bool',
        'java_generate_equals_and_hash': 'bool',
        'java_string_check_utf8': 'bool',
        'optimize_for': 'str',
        'go_package': 'str',
        'go_package_bytes': 'ByteString',
        'cc_generic_services': 'bool',
        'java_generic_services': 'bool',
        'py_generic_services': 'bool',
        'php_generic_services': 'bool',
        'deprecated': 'bool',
        'cc_enable_arenas': 'bool',
        'objc_class_prefix': 'str',
        'objc_class_prefix_bytes': 'ByteString',
        'csharp_namespace': 'str',
        'csharp_namespace_bytes': 'ByteString',
        'swift_prefix': 'str',
        'swift_prefix_bytes': 'ByteString',
        'php_class_prefix': 'str',
        'php_class_prefix_bytes': 'ByteString',
        'php_namespace': 'str',
        'php_namespace_bytes': 'ByteString',
        'php_metadata_namespace': 'str',
        'ruby_package': 'str',
        'ruby_package_bytes': 'ByteString',
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
        'php_metadata_namespace_bytes': 'phpMetadataNamespaceBytes',
        'uninterpreted_option_count': 'uninterpretedOptionCount',
        'java_package': 'javaPackage',
        'java_package_bytes': 'javaPackageBytes',
        'java_outer_classname': 'javaOuterClassname',
        'java_outer_classname_bytes': 'javaOuterClassnameBytes',
        'java_multiple_files': 'javaMultipleFiles',
        'java_generate_equals_and_hash': 'javaGenerateEqualsAndHash',
        'java_string_check_utf8': 'javaStringCheckUtf8',
        'optimize_for': 'optimizeFor',
        'go_package': 'goPackage',
        'go_package_bytes': 'goPackageBytes',
        'cc_generic_services': 'ccGenericServices',
        'java_generic_services': 'javaGenericServices',
        'py_generic_services': 'pyGenericServices',
        'php_generic_services': 'phpGenericServices',
        'deprecated': 'deprecated',
        'cc_enable_arenas': 'ccEnableArenas',
        'objc_class_prefix': 'objcClassPrefix',
        'objc_class_prefix_bytes': 'objcClassPrefixBytes',
        'csharp_namespace': 'csharpNamespace',
        'csharp_namespace_bytes': 'csharpNamespaceBytes',
        'swift_prefix': 'swiftPrefix',
        'swift_prefix_bytes': 'swiftPrefixBytes',
        'php_class_prefix': 'phpClassPrefix',
        'php_class_prefix_bytes': 'phpClassPrefixBytes',
        'php_namespace': 'phpNamespace',
        'php_namespace_bytes': 'phpNamespaceBytes',
        'php_metadata_namespace': 'phpMetadataNamespace',
        'ruby_package': 'rubyPackage',
        'ruby_package_bytes': 'rubyPackageBytes',
        'uninterpreted_option_list': 'uninterpretedOptionList',
        'uninterpreted_option_or_builder_list': 'uninterpretedOptionOrBuilderList',
        'default_instance_for_type': 'defaultInstanceForType',
        'all_fields': 'allFields',
        'descriptor_for_type': 'descriptorForType',
        'initialization_error_string': 'initializationErrorString',
        'unknown_fields': 'unknownFields',
        'initialized': 'initialized'
    }

    def __init__(self, php_metadata_namespace_bytes=None, uninterpreted_option_count=None, java_package=None, java_package_bytes=None, java_outer_classname=None, java_outer_classname_bytes=None, java_multiple_files=None, java_generate_equals_and_hash=None, java_string_check_utf8=None, optimize_for=None, go_package=None, go_package_bytes=None, cc_generic_services=None, java_generic_services=None, py_generic_services=None, php_generic_services=None, deprecated=None, cc_enable_arenas=None, objc_class_prefix=None, objc_class_prefix_bytes=None, csharp_namespace=None, csharp_namespace_bytes=None, swift_prefix=None, swift_prefix_bytes=None, php_class_prefix=None, php_class_prefix_bytes=None, php_namespace=None, php_namespace_bytes=None, php_metadata_namespace=None, ruby_package=None, ruby_package_bytes=None, uninterpreted_option_list=None, uninterpreted_option_or_builder_list=None, default_instance_for_type=None, all_fields=None, descriptor_for_type=None, initialization_error_string=None, unknown_fields=None, initialized=None):  # noqa: E501
        """FileOptionsOrBuilder - a model defined in Swagger"""  # noqa: E501
        self._php_metadata_namespace_bytes = None
        self._uninterpreted_option_count = None
        self._java_package = None
        self._java_package_bytes = None
        self._java_outer_classname = None
        self._java_outer_classname_bytes = None
        self._java_multiple_files = None
        self._java_generate_equals_and_hash = None
        self._java_string_check_utf8 = None
        self._optimize_for = None
        self._go_package = None
        self._go_package_bytes = None
        self._cc_generic_services = None
        self._java_generic_services = None
        self._py_generic_services = None
        self._php_generic_services = None
        self._deprecated = None
        self._cc_enable_arenas = None
        self._objc_class_prefix = None
        self._objc_class_prefix_bytes = None
        self._csharp_namespace = None
        self._csharp_namespace_bytes = None
        self._swift_prefix = None
        self._swift_prefix_bytes = None
        self._php_class_prefix = None
        self._php_class_prefix_bytes = None
        self._php_namespace = None
        self._php_namespace_bytes = None
        self._php_metadata_namespace = None
        self._ruby_package = None
        self._ruby_package_bytes = None
        self._uninterpreted_option_list = None
        self._uninterpreted_option_or_builder_list = None
        self._default_instance_for_type = None
        self._all_fields = None
        self._descriptor_for_type = None
        self._initialization_error_string = None
        self._unknown_fields = None
        self._initialized = None
        self.discriminator = None
        if php_metadata_namespace_bytes is not None:
            self.php_metadata_namespace_bytes = php_metadata_namespace_bytes
        if uninterpreted_option_count is not None:
            self.uninterpreted_option_count = uninterpreted_option_count
        if java_package is not None:
            self.java_package = java_package
        if java_package_bytes is not None:
            self.java_package_bytes = java_package_bytes
        if java_outer_classname is not None:
            self.java_outer_classname = java_outer_classname
        if java_outer_classname_bytes is not None:
            self.java_outer_classname_bytes = java_outer_classname_bytes
        if java_multiple_files is not None:
            self.java_multiple_files = java_multiple_files
        if java_generate_equals_and_hash is not None:
            self.java_generate_equals_and_hash = java_generate_equals_and_hash
        if java_string_check_utf8 is not None:
            self.java_string_check_utf8 = java_string_check_utf8
        if optimize_for is not None:
            self.optimize_for = optimize_for
        if go_package is not None:
            self.go_package = go_package
        if go_package_bytes is not None:
            self.go_package_bytes = go_package_bytes
        if cc_generic_services is not None:
            self.cc_generic_services = cc_generic_services
        if java_generic_services is not None:
            self.java_generic_services = java_generic_services
        if py_generic_services is not None:
            self.py_generic_services = py_generic_services
        if php_generic_services is not None:
            self.php_generic_services = php_generic_services
        if deprecated is not None:
            self.deprecated = deprecated
        if cc_enable_arenas is not None:
            self.cc_enable_arenas = cc_enable_arenas
        if objc_class_prefix is not None:
            self.objc_class_prefix = objc_class_prefix
        if objc_class_prefix_bytes is not None:
            self.objc_class_prefix_bytes = objc_class_prefix_bytes
        if csharp_namespace is not None:
            self.csharp_namespace = csharp_namespace
        if csharp_namespace_bytes is not None:
            self.csharp_namespace_bytes = csharp_namespace_bytes
        if swift_prefix is not None:
            self.swift_prefix = swift_prefix
        if swift_prefix_bytes is not None:
            self.swift_prefix_bytes = swift_prefix_bytes
        if php_class_prefix is not None:
            self.php_class_prefix = php_class_prefix
        if php_class_prefix_bytes is not None:
            self.php_class_prefix_bytes = php_class_prefix_bytes
        if php_namespace is not None:
            self.php_namespace = php_namespace
        if php_namespace_bytes is not None:
            self.php_namespace_bytes = php_namespace_bytes
        if php_metadata_namespace is not None:
            self.php_metadata_namespace = php_metadata_namespace
        if ruby_package is not None:
            self.ruby_package = ruby_package
        if ruby_package_bytes is not None:
            self.ruby_package_bytes = ruby_package_bytes
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
    def php_metadata_namespace_bytes(self):
        """Gets the php_metadata_namespace_bytes of this FileOptionsOrBuilder.  # noqa: E501


        :return: The php_metadata_namespace_bytes of this FileOptionsOrBuilder.  # noqa: E501
        :rtype: ByteString
        """
        return self._php_metadata_namespace_bytes

    @php_metadata_namespace_bytes.setter
    def php_metadata_namespace_bytes(self, php_metadata_namespace_bytes):
        """Sets the php_metadata_namespace_bytes of this FileOptionsOrBuilder.


        :param php_metadata_namespace_bytes: The php_metadata_namespace_bytes of this FileOptionsOrBuilder.  # noqa: E501
        :type: ByteString
        """

        self._php_metadata_namespace_bytes = php_metadata_namespace_bytes

    @property
    def uninterpreted_option_count(self):
        """Gets the uninterpreted_option_count of this FileOptionsOrBuilder.  # noqa: E501


        :return: The uninterpreted_option_count of this FileOptionsOrBuilder.  # noqa: E501
        :rtype: int
        """
        return self._uninterpreted_option_count

    @uninterpreted_option_count.setter
    def uninterpreted_option_count(self, uninterpreted_option_count):
        """Sets the uninterpreted_option_count of this FileOptionsOrBuilder.


        :param uninterpreted_option_count: The uninterpreted_option_count of this FileOptionsOrBuilder.  # noqa: E501
        :type: int
        """

        self._uninterpreted_option_count = uninterpreted_option_count

    @property
    def java_package(self):
        """Gets the java_package of this FileOptionsOrBuilder.  # noqa: E501


        :return: The java_package of this FileOptionsOrBuilder.  # noqa: E501
        :rtype: str
        """
        return self._java_package

    @java_package.setter
    def java_package(self, java_package):
        """Sets the java_package of this FileOptionsOrBuilder.


        :param java_package: The java_package of this FileOptionsOrBuilder.  # noqa: E501
        :type: str
        """

        self._java_package = java_package

    @property
    def java_package_bytes(self):
        """Gets the java_package_bytes of this FileOptionsOrBuilder.  # noqa: E501


        :return: The java_package_bytes of this FileOptionsOrBuilder.  # noqa: E501
        :rtype: ByteString
        """
        return self._java_package_bytes

    @java_package_bytes.setter
    def java_package_bytes(self, java_package_bytes):
        """Sets the java_package_bytes of this FileOptionsOrBuilder.


        :param java_package_bytes: The java_package_bytes of this FileOptionsOrBuilder.  # noqa: E501
        :type: ByteString
        """

        self._java_package_bytes = java_package_bytes

    @property
    def java_outer_classname(self):
        """Gets the java_outer_classname of this FileOptionsOrBuilder.  # noqa: E501


        :return: The java_outer_classname of this FileOptionsOrBuilder.  # noqa: E501
        :rtype: str
        """
        return self._java_outer_classname

    @java_outer_classname.setter
    def java_outer_classname(self, java_outer_classname):
        """Sets the java_outer_classname of this FileOptionsOrBuilder.


        :param java_outer_classname: The java_outer_classname of this FileOptionsOrBuilder.  # noqa: E501
        :type: str
        """

        self._java_outer_classname = java_outer_classname

    @property
    def java_outer_classname_bytes(self):
        """Gets the java_outer_classname_bytes of this FileOptionsOrBuilder.  # noqa: E501


        :return: The java_outer_classname_bytes of this FileOptionsOrBuilder.  # noqa: E501
        :rtype: ByteString
        """
        return self._java_outer_classname_bytes

    @java_outer_classname_bytes.setter
    def java_outer_classname_bytes(self, java_outer_classname_bytes):
        """Sets the java_outer_classname_bytes of this FileOptionsOrBuilder.


        :param java_outer_classname_bytes: The java_outer_classname_bytes of this FileOptionsOrBuilder.  # noqa: E501
        :type: ByteString
        """

        self._java_outer_classname_bytes = java_outer_classname_bytes

    @property
    def java_multiple_files(self):
        """Gets the java_multiple_files of this FileOptionsOrBuilder.  # noqa: E501


        :return: The java_multiple_files of this FileOptionsOrBuilder.  # noqa: E501
        :rtype: bool
        """
        return self._java_multiple_files

    @java_multiple_files.setter
    def java_multiple_files(self, java_multiple_files):
        """Sets the java_multiple_files of this FileOptionsOrBuilder.


        :param java_multiple_files: The java_multiple_files of this FileOptionsOrBuilder.  # noqa: E501
        :type: bool
        """

        self._java_multiple_files = java_multiple_files

    @property
    def java_generate_equals_and_hash(self):
        """Gets the java_generate_equals_and_hash of this FileOptionsOrBuilder.  # noqa: E501


        :return: The java_generate_equals_and_hash of this FileOptionsOrBuilder.  # noqa: E501
        :rtype: bool
        """
        return self._java_generate_equals_and_hash

    @java_generate_equals_and_hash.setter
    def java_generate_equals_and_hash(self, java_generate_equals_and_hash):
        """Sets the java_generate_equals_and_hash of this FileOptionsOrBuilder.


        :param java_generate_equals_and_hash: The java_generate_equals_and_hash of this FileOptionsOrBuilder.  # noqa: E501
        :type: bool
        """

        self._java_generate_equals_and_hash = java_generate_equals_and_hash

    @property
    def java_string_check_utf8(self):
        """Gets the java_string_check_utf8 of this FileOptionsOrBuilder.  # noqa: E501


        :return: The java_string_check_utf8 of this FileOptionsOrBuilder.  # noqa: E501
        :rtype: bool
        """
        return self._java_string_check_utf8

    @java_string_check_utf8.setter
    def java_string_check_utf8(self, java_string_check_utf8):
        """Sets the java_string_check_utf8 of this FileOptionsOrBuilder.


        :param java_string_check_utf8: The java_string_check_utf8 of this FileOptionsOrBuilder.  # noqa: E501
        :type: bool
        """

        self._java_string_check_utf8 = java_string_check_utf8

    @property
    def optimize_for(self):
        """Gets the optimize_for of this FileOptionsOrBuilder.  # noqa: E501


        :return: The optimize_for of this FileOptionsOrBuilder.  # noqa: E501
        :rtype: str
        """
        return self._optimize_for

    @optimize_for.setter
    def optimize_for(self, optimize_for):
        """Sets the optimize_for of this FileOptionsOrBuilder.


        :param optimize_for: The optimize_for of this FileOptionsOrBuilder.  # noqa: E501
        :type: str
        """
        allowed_values = ["SPEED", "CODE_SIZE", "LITE_RUNTIME"]  # noqa: E501
        if optimize_for not in allowed_values:
            raise ValueError(
                "Invalid value for `optimize_for` ({0}), must be one of {1}"  # noqa: E501
                .format(optimize_for, allowed_values)
            )

        self._optimize_for = optimize_for

    @property
    def go_package(self):
        """Gets the go_package of this FileOptionsOrBuilder.  # noqa: E501


        :return: The go_package of this FileOptionsOrBuilder.  # noqa: E501
        :rtype: str
        """
        return self._go_package

    @go_package.setter
    def go_package(self, go_package):
        """Sets the go_package of this FileOptionsOrBuilder.


        :param go_package: The go_package of this FileOptionsOrBuilder.  # noqa: E501
        :type: str
        """

        self._go_package = go_package

    @property
    def go_package_bytes(self):
        """Gets the go_package_bytes of this FileOptionsOrBuilder.  # noqa: E501


        :return: The go_package_bytes of this FileOptionsOrBuilder.  # noqa: E501
        :rtype: ByteString
        """
        return self._go_package_bytes

    @go_package_bytes.setter
    def go_package_bytes(self, go_package_bytes):
        """Sets the go_package_bytes of this FileOptionsOrBuilder.


        :param go_package_bytes: The go_package_bytes of this FileOptionsOrBuilder.  # noqa: E501
        :type: ByteString
        """

        self._go_package_bytes = go_package_bytes

    @property
    def cc_generic_services(self):
        """Gets the cc_generic_services of this FileOptionsOrBuilder.  # noqa: E501


        :return: The cc_generic_services of this FileOptionsOrBuilder.  # noqa: E501
        :rtype: bool
        """
        return self._cc_generic_services

    @cc_generic_services.setter
    def cc_generic_services(self, cc_generic_services):
        """Sets the cc_generic_services of this FileOptionsOrBuilder.


        :param cc_generic_services: The cc_generic_services of this FileOptionsOrBuilder.  # noqa: E501
        :type: bool
        """

        self._cc_generic_services = cc_generic_services

    @property
    def java_generic_services(self):
        """Gets the java_generic_services of this FileOptionsOrBuilder.  # noqa: E501


        :return: The java_generic_services of this FileOptionsOrBuilder.  # noqa: E501
        :rtype: bool
        """
        return self._java_generic_services

    @java_generic_services.setter
    def java_generic_services(self, java_generic_services):
        """Sets the java_generic_services of this FileOptionsOrBuilder.


        :param java_generic_services: The java_generic_services of this FileOptionsOrBuilder.  # noqa: E501
        :type: bool
        """

        self._java_generic_services = java_generic_services

    @property
    def py_generic_services(self):
        """Gets the py_generic_services of this FileOptionsOrBuilder.  # noqa: E501


        :return: The py_generic_services of this FileOptionsOrBuilder.  # noqa: E501
        :rtype: bool
        """
        return self._py_generic_services

    @py_generic_services.setter
    def py_generic_services(self, py_generic_services):
        """Sets the py_generic_services of this FileOptionsOrBuilder.


        :param py_generic_services: The py_generic_services of this FileOptionsOrBuilder.  # noqa: E501
        :type: bool
        """

        self._py_generic_services = py_generic_services

    @property
    def php_generic_services(self):
        """Gets the php_generic_services of this FileOptionsOrBuilder.  # noqa: E501


        :return: The php_generic_services of this FileOptionsOrBuilder.  # noqa: E501
        :rtype: bool
        """
        return self._php_generic_services

    @php_generic_services.setter
    def php_generic_services(self, php_generic_services):
        """Sets the php_generic_services of this FileOptionsOrBuilder.


        :param php_generic_services: The php_generic_services of this FileOptionsOrBuilder.  # noqa: E501
        :type: bool
        """

        self._php_generic_services = php_generic_services

    @property
    def deprecated(self):
        """Gets the deprecated of this FileOptionsOrBuilder.  # noqa: E501


        :return: The deprecated of this FileOptionsOrBuilder.  # noqa: E501
        :rtype: bool
        """
        return self._deprecated

    @deprecated.setter
    def deprecated(self, deprecated):
        """Sets the deprecated of this FileOptionsOrBuilder.


        :param deprecated: The deprecated of this FileOptionsOrBuilder.  # noqa: E501
        :type: bool
        """

        self._deprecated = deprecated

    @property
    def cc_enable_arenas(self):
        """Gets the cc_enable_arenas of this FileOptionsOrBuilder.  # noqa: E501


        :return: The cc_enable_arenas of this FileOptionsOrBuilder.  # noqa: E501
        :rtype: bool
        """
        return self._cc_enable_arenas

    @cc_enable_arenas.setter
    def cc_enable_arenas(self, cc_enable_arenas):
        """Sets the cc_enable_arenas of this FileOptionsOrBuilder.


        :param cc_enable_arenas: The cc_enable_arenas of this FileOptionsOrBuilder.  # noqa: E501
        :type: bool
        """

        self._cc_enable_arenas = cc_enable_arenas

    @property
    def objc_class_prefix(self):
        """Gets the objc_class_prefix of this FileOptionsOrBuilder.  # noqa: E501


        :return: The objc_class_prefix of this FileOptionsOrBuilder.  # noqa: E501
        :rtype: str
        """
        return self._objc_class_prefix

    @objc_class_prefix.setter
    def objc_class_prefix(self, objc_class_prefix):
        """Sets the objc_class_prefix of this FileOptionsOrBuilder.


        :param objc_class_prefix: The objc_class_prefix of this FileOptionsOrBuilder.  # noqa: E501
        :type: str
        """

        self._objc_class_prefix = objc_class_prefix

    @property
    def objc_class_prefix_bytes(self):
        """Gets the objc_class_prefix_bytes of this FileOptionsOrBuilder.  # noqa: E501


        :return: The objc_class_prefix_bytes of this FileOptionsOrBuilder.  # noqa: E501
        :rtype: ByteString
        """
        return self._objc_class_prefix_bytes

    @objc_class_prefix_bytes.setter
    def objc_class_prefix_bytes(self, objc_class_prefix_bytes):
        """Sets the objc_class_prefix_bytes of this FileOptionsOrBuilder.


        :param objc_class_prefix_bytes: The objc_class_prefix_bytes of this FileOptionsOrBuilder.  # noqa: E501
        :type: ByteString
        """

        self._objc_class_prefix_bytes = objc_class_prefix_bytes

    @property
    def csharp_namespace(self):
        """Gets the csharp_namespace of this FileOptionsOrBuilder.  # noqa: E501


        :return: The csharp_namespace of this FileOptionsOrBuilder.  # noqa: E501
        :rtype: str
        """
        return self._csharp_namespace

    @csharp_namespace.setter
    def csharp_namespace(self, csharp_namespace):
        """Sets the csharp_namespace of this FileOptionsOrBuilder.


        :param csharp_namespace: The csharp_namespace of this FileOptionsOrBuilder.  # noqa: E501
        :type: str
        """

        self._csharp_namespace = csharp_namespace

    @property
    def csharp_namespace_bytes(self):
        """Gets the csharp_namespace_bytes of this FileOptionsOrBuilder.  # noqa: E501


        :return: The csharp_namespace_bytes of this FileOptionsOrBuilder.  # noqa: E501
        :rtype: ByteString
        """
        return self._csharp_namespace_bytes

    @csharp_namespace_bytes.setter
    def csharp_namespace_bytes(self, csharp_namespace_bytes):
        """Sets the csharp_namespace_bytes of this FileOptionsOrBuilder.


        :param csharp_namespace_bytes: The csharp_namespace_bytes of this FileOptionsOrBuilder.  # noqa: E501
        :type: ByteString
        """

        self._csharp_namespace_bytes = csharp_namespace_bytes

    @property
    def swift_prefix(self):
        """Gets the swift_prefix of this FileOptionsOrBuilder.  # noqa: E501


        :return: The swift_prefix of this FileOptionsOrBuilder.  # noqa: E501
        :rtype: str
        """
        return self._swift_prefix

    @swift_prefix.setter
    def swift_prefix(self, swift_prefix):
        """Sets the swift_prefix of this FileOptionsOrBuilder.


        :param swift_prefix: The swift_prefix of this FileOptionsOrBuilder.  # noqa: E501
        :type: str
        """

        self._swift_prefix = swift_prefix

    @property
    def swift_prefix_bytes(self):
        """Gets the swift_prefix_bytes of this FileOptionsOrBuilder.  # noqa: E501


        :return: The swift_prefix_bytes of this FileOptionsOrBuilder.  # noqa: E501
        :rtype: ByteString
        """
        return self._swift_prefix_bytes

    @swift_prefix_bytes.setter
    def swift_prefix_bytes(self, swift_prefix_bytes):
        """Sets the swift_prefix_bytes of this FileOptionsOrBuilder.


        :param swift_prefix_bytes: The swift_prefix_bytes of this FileOptionsOrBuilder.  # noqa: E501
        :type: ByteString
        """

        self._swift_prefix_bytes = swift_prefix_bytes

    @property
    def php_class_prefix(self):
        """Gets the php_class_prefix of this FileOptionsOrBuilder.  # noqa: E501


        :return: The php_class_prefix of this FileOptionsOrBuilder.  # noqa: E501
        :rtype: str
        """
        return self._php_class_prefix

    @php_class_prefix.setter
    def php_class_prefix(self, php_class_prefix):
        """Sets the php_class_prefix of this FileOptionsOrBuilder.


        :param php_class_prefix: The php_class_prefix of this FileOptionsOrBuilder.  # noqa: E501
        :type: str
        """

        self._php_class_prefix = php_class_prefix

    @property
    def php_class_prefix_bytes(self):
        """Gets the php_class_prefix_bytes of this FileOptionsOrBuilder.  # noqa: E501


        :return: The php_class_prefix_bytes of this FileOptionsOrBuilder.  # noqa: E501
        :rtype: ByteString
        """
        return self._php_class_prefix_bytes

    @php_class_prefix_bytes.setter
    def php_class_prefix_bytes(self, php_class_prefix_bytes):
        """Sets the php_class_prefix_bytes of this FileOptionsOrBuilder.


        :param php_class_prefix_bytes: The php_class_prefix_bytes of this FileOptionsOrBuilder.  # noqa: E501
        :type: ByteString
        """

        self._php_class_prefix_bytes = php_class_prefix_bytes

    @property
    def php_namespace(self):
        """Gets the php_namespace of this FileOptionsOrBuilder.  # noqa: E501


        :return: The php_namespace of this FileOptionsOrBuilder.  # noqa: E501
        :rtype: str
        """
        return self._php_namespace

    @php_namespace.setter
    def php_namespace(self, php_namespace):
        """Sets the php_namespace of this FileOptionsOrBuilder.


        :param php_namespace: The php_namespace of this FileOptionsOrBuilder.  # noqa: E501
        :type: str
        """

        self._php_namespace = php_namespace

    @property
    def php_namespace_bytes(self):
        """Gets the php_namespace_bytes of this FileOptionsOrBuilder.  # noqa: E501


        :return: The php_namespace_bytes of this FileOptionsOrBuilder.  # noqa: E501
        :rtype: ByteString
        """
        return self._php_namespace_bytes

    @php_namespace_bytes.setter
    def php_namespace_bytes(self, php_namespace_bytes):
        """Sets the php_namespace_bytes of this FileOptionsOrBuilder.


        :param php_namespace_bytes: The php_namespace_bytes of this FileOptionsOrBuilder.  # noqa: E501
        :type: ByteString
        """

        self._php_namespace_bytes = php_namespace_bytes

    @property
    def php_metadata_namespace(self):
        """Gets the php_metadata_namespace of this FileOptionsOrBuilder.  # noqa: E501


        :return: The php_metadata_namespace of this FileOptionsOrBuilder.  # noqa: E501
        :rtype: str
        """
        return self._php_metadata_namespace

    @php_metadata_namespace.setter
    def php_metadata_namespace(self, php_metadata_namespace):
        """Sets the php_metadata_namespace of this FileOptionsOrBuilder.


        :param php_metadata_namespace: The php_metadata_namespace of this FileOptionsOrBuilder.  # noqa: E501
        :type: str
        """

        self._php_metadata_namespace = php_metadata_namespace

    @property
    def ruby_package(self):
        """Gets the ruby_package of this FileOptionsOrBuilder.  # noqa: E501


        :return: The ruby_package of this FileOptionsOrBuilder.  # noqa: E501
        :rtype: str
        """
        return self._ruby_package

    @ruby_package.setter
    def ruby_package(self, ruby_package):
        """Sets the ruby_package of this FileOptionsOrBuilder.


        :param ruby_package: The ruby_package of this FileOptionsOrBuilder.  # noqa: E501
        :type: str
        """

        self._ruby_package = ruby_package

    @property
    def ruby_package_bytes(self):
        """Gets the ruby_package_bytes of this FileOptionsOrBuilder.  # noqa: E501


        :return: The ruby_package_bytes of this FileOptionsOrBuilder.  # noqa: E501
        :rtype: ByteString
        """
        return self._ruby_package_bytes

    @ruby_package_bytes.setter
    def ruby_package_bytes(self, ruby_package_bytes):
        """Sets the ruby_package_bytes of this FileOptionsOrBuilder.


        :param ruby_package_bytes: The ruby_package_bytes of this FileOptionsOrBuilder.  # noqa: E501
        :type: ByteString
        """

        self._ruby_package_bytes = ruby_package_bytes

    @property
    def uninterpreted_option_list(self):
        """Gets the uninterpreted_option_list of this FileOptionsOrBuilder.  # noqa: E501


        :return: The uninterpreted_option_list of this FileOptionsOrBuilder.  # noqa: E501
        :rtype: list[UninterpretedOption]
        """
        return self._uninterpreted_option_list

    @uninterpreted_option_list.setter
    def uninterpreted_option_list(self, uninterpreted_option_list):
        """Sets the uninterpreted_option_list of this FileOptionsOrBuilder.


        :param uninterpreted_option_list: The uninterpreted_option_list of this FileOptionsOrBuilder.  # noqa: E501
        :type: list[UninterpretedOption]
        """

        self._uninterpreted_option_list = uninterpreted_option_list

    @property
    def uninterpreted_option_or_builder_list(self):
        """Gets the uninterpreted_option_or_builder_list of this FileOptionsOrBuilder.  # noqa: E501


        :return: The uninterpreted_option_or_builder_list of this FileOptionsOrBuilder.  # noqa: E501
        :rtype: list[UninterpretedOptionOrBuilder]
        """
        return self._uninterpreted_option_or_builder_list

    @uninterpreted_option_or_builder_list.setter
    def uninterpreted_option_or_builder_list(self, uninterpreted_option_or_builder_list):
        """Sets the uninterpreted_option_or_builder_list of this FileOptionsOrBuilder.


        :param uninterpreted_option_or_builder_list: The uninterpreted_option_or_builder_list of this FileOptionsOrBuilder.  # noqa: E501
        :type: list[UninterpretedOptionOrBuilder]
        """

        self._uninterpreted_option_or_builder_list = uninterpreted_option_or_builder_list

    @property
    def default_instance_for_type(self):
        """Gets the default_instance_for_type of this FileOptionsOrBuilder.  # noqa: E501


        :return: The default_instance_for_type of this FileOptionsOrBuilder.  # noqa: E501
        :rtype: Message
        """
        return self._default_instance_for_type

    @default_instance_for_type.setter
    def default_instance_for_type(self, default_instance_for_type):
        """Sets the default_instance_for_type of this FileOptionsOrBuilder.


        :param default_instance_for_type: The default_instance_for_type of this FileOptionsOrBuilder.  # noqa: E501
        :type: Message
        """

        self._default_instance_for_type = default_instance_for_type

    @property
    def all_fields(self):
        """Gets the all_fields of this FileOptionsOrBuilder.  # noqa: E501


        :return: The all_fields of this FileOptionsOrBuilder.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._all_fields

    @all_fields.setter
    def all_fields(self, all_fields):
        """Sets the all_fields of this FileOptionsOrBuilder.


        :param all_fields: The all_fields of this FileOptionsOrBuilder.  # noqa: E501
        :type: dict(str, object)
        """

        self._all_fields = all_fields

    @property
    def descriptor_for_type(self):
        """Gets the descriptor_for_type of this FileOptionsOrBuilder.  # noqa: E501


        :return: The descriptor_for_type of this FileOptionsOrBuilder.  # noqa: E501
        :rtype: Descriptor
        """
        return self._descriptor_for_type

    @descriptor_for_type.setter
    def descriptor_for_type(self, descriptor_for_type):
        """Sets the descriptor_for_type of this FileOptionsOrBuilder.


        :param descriptor_for_type: The descriptor_for_type of this FileOptionsOrBuilder.  # noqa: E501
        :type: Descriptor
        """

        self._descriptor_for_type = descriptor_for_type

    @property
    def initialization_error_string(self):
        """Gets the initialization_error_string of this FileOptionsOrBuilder.  # noqa: E501


        :return: The initialization_error_string of this FileOptionsOrBuilder.  # noqa: E501
        :rtype: str
        """
        return self._initialization_error_string

    @initialization_error_string.setter
    def initialization_error_string(self, initialization_error_string):
        """Sets the initialization_error_string of this FileOptionsOrBuilder.


        :param initialization_error_string: The initialization_error_string of this FileOptionsOrBuilder.  # noqa: E501
        :type: str
        """

        self._initialization_error_string = initialization_error_string

    @property
    def unknown_fields(self):
        """Gets the unknown_fields of this FileOptionsOrBuilder.  # noqa: E501


        :return: The unknown_fields of this FileOptionsOrBuilder.  # noqa: E501
        :rtype: UnknownFieldSet
        """
        return self._unknown_fields

    @unknown_fields.setter
    def unknown_fields(self, unknown_fields):
        """Sets the unknown_fields of this FileOptionsOrBuilder.


        :param unknown_fields: The unknown_fields of this FileOptionsOrBuilder.  # noqa: E501
        :type: UnknownFieldSet
        """

        self._unknown_fields = unknown_fields

    @property
    def initialized(self):
        """Gets the initialized of this FileOptionsOrBuilder.  # noqa: E501


        :return: The initialized of this FileOptionsOrBuilder.  # noqa: E501
        :rtype: bool
        """
        return self._initialized

    @initialized.setter
    def initialized(self, initialized):
        """Sets the initialized of this FileOptionsOrBuilder.


        :param initialized: The initialized of this FileOptionsOrBuilder.  # noqa: E501
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
        if issubclass(FileOptionsOrBuilder, dict):
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
        if not isinstance(other, FileOptionsOrBuilder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
