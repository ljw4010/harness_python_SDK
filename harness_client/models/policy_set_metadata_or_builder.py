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

class PolicySetMetadataOrBuilder(object):
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
        'policy_metadata_list': 'list[PolicyMetadata1]',
        'policy_metadata_count': 'int',
        'policy_metadata_or_builder_list': 'list[PolicyMetadataOrBuilder]',
        'policy_set_name': 'str',
        'policy_set_name_bytes': 'ByteString',
        'description_bytes': 'ByteString',
        'identifier_bytes': 'ByteString',
        'identifier': 'str',
        'description': 'str',
        'status': 'str',
        'status_bytes': 'ByteString',
        'account_id': 'str',
        'account_id_bytes': 'ByteString',
        'org_id': 'str',
        'org_id_bytes': 'ByteString',
        'project_id': 'str',
        'project_id_bytes': 'ByteString',
        'created': 'int',
        'policy_set_id': 'str',
        'policy_set_id_bytes': 'ByteString',
        'deny': 'bool',
        'all_fields': 'dict(str, object)',
        'default_instance_for_type': 'Message',
        'initialization_error_string': 'str',
        'unknown_fields': 'UnknownFieldSet',
        'descriptor_for_type': 'Descriptor',
        'initialized': 'bool'
    }

    attribute_map = {
        'policy_metadata_list': 'policyMetadataList',
        'policy_metadata_count': 'policyMetadataCount',
        'policy_metadata_or_builder_list': 'policyMetadataOrBuilderList',
        'policy_set_name': 'policySetName',
        'policy_set_name_bytes': 'policySetNameBytes',
        'description_bytes': 'descriptionBytes',
        'identifier_bytes': 'identifierBytes',
        'identifier': 'identifier',
        'description': 'description',
        'status': 'status',
        'status_bytes': 'statusBytes',
        'account_id': 'accountId',
        'account_id_bytes': 'accountIdBytes',
        'org_id': 'orgId',
        'org_id_bytes': 'orgIdBytes',
        'project_id': 'projectId',
        'project_id_bytes': 'projectIdBytes',
        'created': 'created',
        'policy_set_id': 'policySetId',
        'policy_set_id_bytes': 'policySetIdBytes',
        'deny': 'deny',
        'all_fields': 'allFields',
        'default_instance_for_type': 'defaultInstanceForType',
        'initialization_error_string': 'initializationErrorString',
        'unknown_fields': 'unknownFields',
        'descriptor_for_type': 'descriptorForType',
        'initialized': 'initialized'
    }

    def __init__(self, policy_metadata_list=None, policy_metadata_count=None, policy_metadata_or_builder_list=None, policy_set_name=None, policy_set_name_bytes=None, description_bytes=None, identifier_bytes=None, identifier=None, description=None, status=None, status_bytes=None, account_id=None, account_id_bytes=None, org_id=None, org_id_bytes=None, project_id=None, project_id_bytes=None, created=None, policy_set_id=None, policy_set_id_bytes=None, deny=None, all_fields=None, default_instance_for_type=None, initialization_error_string=None, unknown_fields=None, descriptor_for_type=None, initialized=None):  # noqa: E501
        """PolicySetMetadataOrBuilder - a model defined in Swagger"""  # noqa: E501
        self._policy_metadata_list = None
        self._policy_metadata_count = None
        self._policy_metadata_or_builder_list = None
        self._policy_set_name = None
        self._policy_set_name_bytes = None
        self._description_bytes = None
        self._identifier_bytes = None
        self._identifier = None
        self._description = None
        self._status = None
        self._status_bytes = None
        self._account_id = None
        self._account_id_bytes = None
        self._org_id = None
        self._org_id_bytes = None
        self._project_id = None
        self._project_id_bytes = None
        self._created = None
        self._policy_set_id = None
        self._policy_set_id_bytes = None
        self._deny = None
        self._all_fields = None
        self._default_instance_for_type = None
        self._initialization_error_string = None
        self._unknown_fields = None
        self._descriptor_for_type = None
        self._initialized = None
        self.discriminator = None
        if policy_metadata_list is not None:
            self.policy_metadata_list = policy_metadata_list
        if policy_metadata_count is not None:
            self.policy_metadata_count = policy_metadata_count
        if policy_metadata_or_builder_list is not None:
            self.policy_metadata_or_builder_list = policy_metadata_or_builder_list
        if policy_set_name is not None:
            self.policy_set_name = policy_set_name
        if policy_set_name_bytes is not None:
            self.policy_set_name_bytes = policy_set_name_bytes
        if description_bytes is not None:
            self.description_bytes = description_bytes
        if identifier_bytes is not None:
            self.identifier_bytes = identifier_bytes
        if identifier is not None:
            self.identifier = identifier
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if status_bytes is not None:
            self.status_bytes = status_bytes
        if account_id is not None:
            self.account_id = account_id
        if account_id_bytes is not None:
            self.account_id_bytes = account_id_bytes
        if org_id is not None:
            self.org_id = org_id
        if org_id_bytes is not None:
            self.org_id_bytes = org_id_bytes
        if project_id is not None:
            self.project_id = project_id
        if project_id_bytes is not None:
            self.project_id_bytes = project_id_bytes
        if created is not None:
            self.created = created
        if policy_set_id is not None:
            self.policy_set_id = policy_set_id
        if policy_set_id_bytes is not None:
            self.policy_set_id_bytes = policy_set_id_bytes
        if deny is not None:
            self.deny = deny
        if all_fields is not None:
            self.all_fields = all_fields
        if default_instance_for_type is not None:
            self.default_instance_for_type = default_instance_for_type
        if initialization_error_string is not None:
            self.initialization_error_string = initialization_error_string
        if unknown_fields is not None:
            self.unknown_fields = unknown_fields
        if descriptor_for_type is not None:
            self.descriptor_for_type = descriptor_for_type
        if initialized is not None:
            self.initialized = initialized

    @property
    def policy_metadata_list(self):
        """Gets the policy_metadata_list of this PolicySetMetadataOrBuilder.  # noqa: E501


        :return: The policy_metadata_list of this PolicySetMetadataOrBuilder.  # noqa: E501
        :rtype: list[PolicyMetadata1]
        """
        return self._policy_metadata_list

    @policy_metadata_list.setter
    def policy_metadata_list(self, policy_metadata_list):
        """Sets the policy_metadata_list of this PolicySetMetadataOrBuilder.


        :param policy_metadata_list: The policy_metadata_list of this PolicySetMetadataOrBuilder.  # noqa: E501
        :type: list[PolicyMetadata1]
        """

        self._policy_metadata_list = policy_metadata_list

    @property
    def policy_metadata_count(self):
        """Gets the policy_metadata_count of this PolicySetMetadataOrBuilder.  # noqa: E501


        :return: The policy_metadata_count of this PolicySetMetadataOrBuilder.  # noqa: E501
        :rtype: int
        """
        return self._policy_metadata_count

    @policy_metadata_count.setter
    def policy_metadata_count(self, policy_metadata_count):
        """Sets the policy_metadata_count of this PolicySetMetadataOrBuilder.


        :param policy_metadata_count: The policy_metadata_count of this PolicySetMetadataOrBuilder.  # noqa: E501
        :type: int
        """

        self._policy_metadata_count = policy_metadata_count

    @property
    def policy_metadata_or_builder_list(self):
        """Gets the policy_metadata_or_builder_list of this PolicySetMetadataOrBuilder.  # noqa: E501


        :return: The policy_metadata_or_builder_list of this PolicySetMetadataOrBuilder.  # noqa: E501
        :rtype: list[PolicyMetadataOrBuilder]
        """
        return self._policy_metadata_or_builder_list

    @policy_metadata_or_builder_list.setter
    def policy_metadata_or_builder_list(self, policy_metadata_or_builder_list):
        """Sets the policy_metadata_or_builder_list of this PolicySetMetadataOrBuilder.


        :param policy_metadata_or_builder_list: The policy_metadata_or_builder_list of this PolicySetMetadataOrBuilder.  # noqa: E501
        :type: list[PolicyMetadataOrBuilder]
        """

        self._policy_metadata_or_builder_list = policy_metadata_or_builder_list

    @property
    def policy_set_name(self):
        """Gets the policy_set_name of this PolicySetMetadataOrBuilder.  # noqa: E501


        :return: The policy_set_name of this PolicySetMetadataOrBuilder.  # noqa: E501
        :rtype: str
        """
        return self._policy_set_name

    @policy_set_name.setter
    def policy_set_name(self, policy_set_name):
        """Sets the policy_set_name of this PolicySetMetadataOrBuilder.


        :param policy_set_name: The policy_set_name of this PolicySetMetadataOrBuilder.  # noqa: E501
        :type: str
        """

        self._policy_set_name = policy_set_name

    @property
    def policy_set_name_bytes(self):
        """Gets the policy_set_name_bytes of this PolicySetMetadataOrBuilder.  # noqa: E501


        :return: The policy_set_name_bytes of this PolicySetMetadataOrBuilder.  # noqa: E501
        :rtype: ByteString
        """
        return self._policy_set_name_bytes

    @policy_set_name_bytes.setter
    def policy_set_name_bytes(self, policy_set_name_bytes):
        """Sets the policy_set_name_bytes of this PolicySetMetadataOrBuilder.


        :param policy_set_name_bytes: The policy_set_name_bytes of this PolicySetMetadataOrBuilder.  # noqa: E501
        :type: ByteString
        """

        self._policy_set_name_bytes = policy_set_name_bytes

    @property
    def description_bytes(self):
        """Gets the description_bytes of this PolicySetMetadataOrBuilder.  # noqa: E501


        :return: The description_bytes of this PolicySetMetadataOrBuilder.  # noqa: E501
        :rtype: ByteString
        """
        return self._description_bytes

    @description_bytes.setter
    def description_bytes(self, description_bytes):
        """Sets the description_bytes of this PolicySetMetadataOrBuilder.


        :param description_bytes: The description_bytes of this PolicySetMetadataOrBuilder.  # noqa: E501
        :type: ByteString
        """

        self._description_bytes = description_bytes

    @property
    def identifier_bytes(self):
        """Gets the identifier_bytes of this PolicySetMetadataOrBuilder.  # noqa: E501


        :return: The identifier_bytes of this PolicySetMetadataOrBuilder.  # noqa: E501
        :rtype: ByteString
        """
        return self._identifier_bytes

    @identifier_bytes.setter
    def identifier_bytes(self, identifier_bytes):
        """Sets the identifier_bytes of this PolicySetMetadataOrBuilder.


        :param identifier_bytes: The identifier_bytes of this PolicySetMetadataOrBuilder.  # noqa: E501
        :type: ByteString
        """

        self._identifier_bytes = identifier_bytes

    @property
    def identifier(self):
        """Gets the identifier of this PolicySetMetadataOrBuilder.  # noqa: E501


        :return: The identifier of this PolicySetMetadataOrBuilder.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this PolicySetMetadataOrBuilder.


        :param identifier: The identifier of this PolicySetMetadataOrBuilder.  # noqa: E501
        :type: str
        """

        self._identifier = identifier

    @property
    def description(self):
        """Gets the description of this PolicySetMetadataOrBuilder.  # noqa: E501


        :return: The description of this PolicySetMetadataOrBuilder.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PolicySetMetadataOrBuilder.


        :param description: The description of this PolicySetMetadataOrBuilder.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def status(self):
        """Gets the status of this PolicySetMetadataOrBuilder.  # noqa: E501


        :return: The status of this PolicySetMetadataOrBuilder.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PolicySetMetadataOrBuilder.


        :param status: The status of this PolicySetMetadataOrBuilder.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def status_bytes(self):
        """Gets the status_bytes of this PolicySetMetadataOrBuilder.  # noqa: E501


        :return: The status_bytes of this PolicySetMetadataOrBuilder.  # noqa: E501
        :rtype: ByteString
        """
        return self._status_bytes

    @status_bytes.setter
    def status_bytes(self, status_bytes):
        """Sets the status_bytes of this PolicySetMetadataOrBuilder.


        :param status_bytes: The status_bytes of this PolicySetMetadataOrBuilder.  # noqa: E501
        :type: ByteString
        """

        self._status_bytes = status_bytes

    @property
    def account_id(self):
        """Gets the account_id of this PolicySetMetadataOrBuilder.  # noqa: E501


        :return: The account_id of this PolicySetMetadataOrBuilder.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this PolicySetMetadataOrBuilder.


        :param account_id: The account_id of this PolicySetMetadataOrBuilder.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def account_id_bytes(self):
        """Gets the account_id_bytes of this PolicySetMetadataOrBuilder.  # noqa: E501


        :return: The account_id_bytes of this PolicySetMetadataOrBuilder.  # noqa: E501
        :rtype: ByteString
        """
        return self._account_id_bytes

    @account_id_bytes.setter
    def account_id_bytes(self, account_id_bytes):
        """Sets the account_id_bytes of this PolicySetMetadataOrBuilder.


        :param account_id_bytes: The account_id_bytes of this PolicySetMetadataOrBuilder.  # noqa: E501
        :type: ByteString
        """

        self._account_id_bytes = account_id_bytes

    @property
    def org_id(self):
        """Gets the org_id of this PolicySetMetadataOrBuilder.  # noqa: E501


        :return: The org_id of this PolicySetMetadataOrBuilder.  # noqa: E501
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this PolicySetMetadataOrBuilder.


        :param org_id: The org_id of this PolicySetMetadataOrBuilder.  # noqa: E501
        :type: str
        """

        self._org_id = org_id

    @property
    def org_id_bytes(self):
        """Gets the org_id_bytes of this PolicySetMetadataOrBuilder.  # noqa: E501


        :return: The org_id_bytes of this PolicySetMetadataOrBuilder.  # noqa: E501
        :rtype: ByteString
        """
        return self._org_id_bytes

    @org_id_bytes.setter
    def org_id_bytes(self, org_id_bytes):
        """Sets the org_id_bytes of this PolicySetMetadataOrBuilder.


        :param org_id_bytes: The org_id_bytes of this PolicySetMetadataOrBuilder.  # noqa: E501
        :type: ByteString
        """

        self._org_id_bytes = org_id_bytes

    @property
    def project_id(self):
        """Gets the project_id of this PolicySetMetadataOrBuilder.  # noqa: E501


        :return: The project_id of this PolicySetMetadataOrBuilder.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this PolicySetMetadataOrBuilder.


        :param project_id: The project_id of this PolicySetMetadataOrBuilder.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def project_id_bytes(self):
        """Gets the project_id_bytes of this PolicySetMetadataOrBuilder.  # noqa: E501


        :return: The project_id_bytes of this PolicySetMetadataOrBuilder.  # noqa: E501
        :rtype: ByteString
        """
        return self._project_id_bytes

    @project_id_bytes.setter
    def project_id_bytes(self, project_id_bytes):
        """Sets the project_id_bytes of this PolicySetMetadataOrBuilder.


        :param project_id_bytes: The project_id_bytes of this PolicySetMetadataOrBuilder.  # noqa: E501
        :type: ByteString
        """

        self._project_id_bytes = project_id_bytes

    @property
    def created(self):
        """Gets the created of this PolicySetMetadataOrBuilder.  # noqa: E501


        :return: The created of this PolicySetMetadataOrBuilder.  # noqa: E501
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this PolicySetMetadataOrBuilder.


        :param created: The created of this PolicySetMetadataOrBuilder.  # noqa: E501
        :type: int
        """

        self._created = created

    @property
    def policy_set_id(self):
        """Gets the policy_set_id of this PolicySetMetadataOrBuilder.  # noqa: E501


        :return: The policy_set_id of this PolicySetMetadataOrBuilder.  # noqa: E501
        :rtype: str
        """
        return self._policy_set_id

    @policy_set_id.setter
    def policy_set_id(self, policy_set_id):
        """Sets the policy_set_id of this PolicySetMetadataOrBuilder.


        :param policy_set_id: The policy_set_id of this PolicySetMetadataOrBuilder.  # noqa: E501
        :type: str
        """

        self._policy_set_id = policy_set_id

    @property
    def policy_set_id_bytes(self):
        """Gets the policy_set_id_bytes of this PolicySetMetadataOrBuilder.  # noqa: E501


        :return: The policy_set_id_bytes of this PolicySetMetadataOrBuilder.  # noqa: E501
        :rtype: ByteString
        """
        return self._policy_set_id_bytes

    @policy_set_id_bytes.setter
    def policy_set_id_bytes(self, policy_set_id_bytes):
        """Sets the policy_set_id_bytes of this PolicySetMetadataOrBuilder.


        :param policy_set_id_bytes: The policy_set_id_bytes of this PolicySetMetadataOrBuilder.  # noqa: E501
        :type: ByteString
        """

        self._policy_set_id_bytes = policy_set_id_bytes

    @property
    def deny(self):
        """Gets the deny of this PolicySetMetadataOrBuilder.  # noqa: E501


        :return: The deny of this PolicySetMetadataOrBuilder.  # noqa: E501
        :rtype: bool
        """
        return self._deny

    @deny.setter
    def deny(self, deny):
        """Sets the deny of this PolicySetMetadataOrBuilder.


        :param deny: The deny of this PolicySetMetadataOrBuilder.  # noqa: E501
        :type: bool
        """

        self._deny = deny

    @property
    def all_fields(self):
        """Gets the all_fields of this PolicySetMetadataOrBuilder.  # noqa: E501


        :return: The all_fields of this PolicySetMetadataOrBuilder.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._all_fields

    @all_fields.setter
    def all_fields(self, all_fields):
        """Sets the all_fields of this PolicySetMetadataOrBuilder.


        :param all_fields: The all_fields of this PolicySetMetadataOrBuilder.  # noqa: E501
        :type: dict(str, object)
        """

        self._all_fields = all_fields

    @property
    def default_instance_for_type(self):
        """Gets the default_instance_for_type of this PolicySetMetadataOrBuilder.  # noqa: E501


        :return: The default_instance_for_type of this PolicySetMetadataOrBuilder.  # noqa: E501
        :rtype: Message
        """
        return self._default_instance_for_type

    @default_instance_for_type.setter
    def default_instance_for_type(self, default_instance_for_type):
        """Sets the default_instance_for_type of this PolicySetMetadataOrBuilder.


        :param default_instance_for_type: The default_instance_for_type of this PolicySetMetadataOrBuilder.  # noqa: E501
        :type: Message
        """

        self._default_instance_for_type = default_instance_for_type

    @property
    def initialization_error_string(self):
        """Gets the initialization_error_string of this PolicySetMetadataOrBuilder.  # noqa: E501


        :return: The initialization_error_string of this PolicySetMetadataOrBuilder.  # noqa: E501
        :rtype: str
        """
        return self._initialization_error_string

    @initialization_error_string.setter
    def initialization_error_string(self, initialization_error_string):
        """Sets the initialization_error_string of this PolicySetMetadataOrBuilder.


        :param initialization_error_string: The initialization_error_string of this PolicySetMetadataOrBuilder.  # noqa: E501
        :type: str
        """

        self._initialization_error_string = initialization_error_string

    @property
    def unknown_fields(self):
        """Gets the unknown_fields of this PolicySetMetadataOrBuilder.  # noqa: E501


        :return: The unknown_fields of this PolicySetMetadataOrBuilder.  # noqa: E501
        :rtype: UnknownFieldSet
        """
        return self._unknown_fields

    @unknown_fields.setter
    def unknown_fields(self, unknown_fields):
        """Sets the unknown_fields of this PolicySetMetadataOrBuilder.


        :param unknown_fields: The unknown_fields of this PolicySetMetadataOrBuilder.  # noqa: E501
        :type: UnknownFieldSet
        """

        self._unknown_fields = unknown_fields

    @property
    def descriptor_for_type(self):
        """Gets the descriptor_for_type of this PolicySetMetadataOrBuilder.  # noqa: E501


        :return: The descriptor_for_type of this PolicySetMetadataOrBuilder.  # noqa: E501
        :rtype: Descriptor
        """
        return self._descriptor_for_type

    @descriptor_for_type.setter
    def descriptor_for_type(self, descriptor_for_type):
        """Sets the descriptor_for_type of this PolicySetMetadataOrBuilder.


        :param descriptor_for_type: The descriptor_for_type of this PolicySetMetadataOrBuilder.  # noqa: E501
        :type: Descriptor
        """

        self._descriptor_for_type = descriptor_for_type

    @property
    def initialized(self):
        """Gets the initialized of this PolicySetMetadataOrBuilder.  # noqa: E501


        :return: The initialized of this PolicySetMetadataOrBuilder.  # noqa: E501
        :rtype: bool
        """
        return self._initialized

    @initialized.setter
    def initialized(self, initialized):
        """Sets the initialized of this PolicySetMetadataOrBuilder.


        :param initialized: The initialized of this PolicySetMetadataOrBuilder.  # noqa: E501
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
        if issubclass(PolicySetMetadataOrBuilder, dict):
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
        if not isinstance(other, PolicySetMetadataOrBuilder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
