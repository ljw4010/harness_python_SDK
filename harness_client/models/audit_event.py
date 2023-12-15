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

class AuditEvent(object):
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
        'audit_id': 'str',
        'insert_id': 'str',
        'resource_scope': 'AuditResourceScope',
        'http_request_info': 'AuditHttpRequestInfo',
        'request_metadata': 'AuditRequestMetadata',
        'timestamp': 'int',
        'authentication_info': 'AuthenticationInfo',
        'module': 'str',
        'environment': 'AuditEnvironment',
        'resource': 'AuditResource',
        'yaml_diff_record': 'YamlDiffRecord',
        'action': 'str',
        'audit_event_data': 'AuditEventData',
        'internal_info': 'dict(str, str)'
    }

    attribute_map = {
        'audit_id': 'auditId',
        'insert_id': 'insertId',
        'resource_scope': 'resourceScope',
        'http_request_info': 'httpRequestInfo',
        'request_metadata': 'requestMetadata',
        'timestamp': 'timestamp',
        'authentication_info': 'authenticationInfo',
        'module': 'module',
        'environment': 'environment',
        'resource': 'resource',
        'yaml_diff_record': 'yamlDiffRecord',
        'action': 'action',
        'audit_event_data': 'auditEventData',
        'internal_info': 'internalInfo'
    }

    def __init__(self, audit_id=None, insert_id=None, resource_scope=None, http_request_info=None, request_metadata=None, timestamp=None, authentication_info=None, module=None, environment=None, resource=None, yaml_diff_record=None, action=None, audit_event_data=None, internal_info=None):  # noqa: E501
        """AuditEvent - a model defined in Swagger"""  # noqa: E501
        self._audit_id = None
        self._insert_id = None
        self._resource_scope = None
        self._http_request_info = None
        self._request_metadata = None
        self._timestamp = None
        self._authentication_info = None
        self._module = None
        self._environment = None
        self._resource = None
        self._yaml_diff_record = None
        self._action = None
        self._audit_event_data = None
        self._internal_info = None
        self.discriminator = None
        if audit_id is not None:
            self.audit_id = audit_id
        self.insert_id = insert_id
        self.resource_scope = resource_scope
        if http_request_info is not None:
            self.http_request_info = http_request_info
        if request_metadata is not None:
            self.request_metadata = request_metadata
        self.timestamp = timestamp
        self.authentication_info = authentication_info
        self.module = module
        if environment is not None:
            self.environment = environment
        self.resource = resource
        if yaml_diff_record is not None:
            self.yaml_diff_record = yaml_diff_record
        self.action = action
        if audit_event_data is not None:
            self.audit_event_data = audit_event_data
        if internal_info is not None:
            self.internal_info = internal_info

    @property
    def audit_id(self):
        """Gets the audit_id of this AuditEvent.  # noqa: E501

        Identifier of the Audit.  # noqa: E501

        :return: The audit_id of this AuditEvent.  # noqa: E501
        :rtype: str
        """
        return self._audit_id

    @audit_id.setter
    def audit_id(self, audit_id):
        """Sets the audit_id of this AuditEvent.

        Identifier of the Audit.  # noqa: E501

        :param audit_id: The audit_id of this AuditEvent.  # noqa: E501
        :type: str
        """

        self._audit_id = audit_id

    @property
    def insert_id(self):
        """Gets the insert_id of this AuditEvent.  # noqa: E501

        Insert Identifier of the Audit.  # noqa: E501

        :return: The insert_id of this AuditEvent.  # noqa: E501
        :rtype: str
        """
        return self._insert_id

    @insert_id.setter
    def insert_id(self, insert_id):
        """Sets the insert_id of this AuditEvent.

        Insert Identifier of the Audit.  # noqa: E501

        :param insert_id: The insert_id of this AuditEvent.  # noqa: E501
        :type: str
        """
        if insert_id is None:
            raise ValueError("Invalid value for `insert_id`, must not be `None`")  # noqa: E501

        self._insert_id = insert_id

    @property
    def resource_scope(self):
        """Gets the resource_scope of this AuditEvent.  # noqa: E501


        :return: The resource_scope of this AuditEvent.  # noqa: E501
        :rtype: AuditResourceScope
        """
        return self._resource_scope

    @resource_scope.setter
    def resource_scope(self, resource_scope):
        """Sets the resource_scope of this AuditEvent.


        :param resource_scope: The resource_scope of this AuditEvent.  # noqa: E501
        :type: AuditResourceScope
        """
        if resource_scope is None:
            raise ValueError("Invalid value for `resource_scope`, must not be `None`")  # noqa: E501

        self._resource_scope = resource_scope

    @property
    def http_request_info(self):
        """Gets the http_request_info of this AuditEvent.  # noqa: E501


        :return: The http_request_info of this AuditEvent.  # noqa: E501
        :rtype: AuditHttpRequestInfo
        """
        return self._http_request_info

    @http_request_info.setter
    def http_request_info(self, http_request_info):
        """Sets the http_request_info of this AuditEvent.


        :param http_request_info: The http_request_info of this AuditEvent.  # noqa: E501
        :type: AuditHttpRequestInfo
        """

        self._http_request_info = http_request_info

    @property
    def request_metadata(self):
        """Gets the request_metadata of this AuditEvent.  # noqa: E501


        :return: The request_metadata of this AuditEvent.  # noqa: E501
        :rtype: AuditRequestMetadata
        """
        return self._request_metadata

    @request_metadata.setter
    def request_metadata(self, request_metadata):
        """Sets the request_metadata of this AuditEvent.


        :param request_metadata: The request_metadata of this AuditEvent.  # noqa: E501
        :type: AuditRequestMetadata
        """

        self._request_metadata = request_metadata

    @property
    def timestamp(self):
        """Gets the timestamp of this AuditEvent.  # noqa: E501


        :return: The timestamp of this AuditEvent.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this AuditEvent.


        :param timestamp: The timestamp of this AuditEvent.  # noqa: E501
        :type: int
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def authentication_info(self):
        """Gets the authentication_info of this AuditEvent.  # noqa: E501


        :return: The authentication_info of this AuditEvent.  # noqa: E501
        :rtype: AuthenticationInfo
        """
        return self._authentication_info

    @authentication_info.setter
    def authentication_info(self, authentication_info):
        """Sets the authentication_info of this AuditEvent.


        :param authentication_info: The authentication_info of this AuditEvent.  # noqa: E501
        :type: AuthenticationInfo
        """
        if authentication_info is None:
            raise ValueError("Invalid value for `authentication_info`, must not be `None`")  # noqa: E501

        self._authentication_info = authentication_info

    @property
    def module(self):
        """Gets the module of this AuditEvent.  # noqa: E501

        Type of module associated with the Audit.  # noqa: E501

        :return: The module of this AuditEvent.  # noqa: E501
        :rtype: str
        """
        return self._module

    @module.setter
    def module(self, module):
        """Sets the module of this AuditEvent.

        Type of module associated with the Audit.  # noqa: E501

        :param module: The module of this AuditEvent.  # noqa: E501
        :type: str
        """
        if module is None:
            raise ValueError("Invalid value for `module`, must not be `None`")  # noqa: E501
        allowed_values = ["CD", "CI", "CV", "CF", "CE", "STO", "CHAOS", "SRM", "IACM", "CET", "IDP", "CODE", "CORE", "PMS", "TEMPLATESERVICE", "SSCA", "GOVERNANCE", "SEI"]  # noqa: E501
        if module not in allowed_values:
            raise ValueError(
                "Invalid value for `module` ({0}), must be one of {1}"  # noqa: E501
                .format(module, allowed_values)
            )

        self._module = module

    @property
    def environment(self):
        """Gets the environment of this AuditEvent.  # noqa: E501


        :return: The environment of this AuditEvent.  # noqa: E501
        :rtype: AuditEnvironment
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this AuditEvent.


        :param environment: The environment of this AuditEvent.  # noqa: E501
        :type: AuditEnvironment
        """

        self._environment = environment

    @property
    def resource(self):
        """Gets the resource of this AuditEvent.  # noqa: E501


        :return: The resource of this AuditEvent.  # noqa: E501
        :rtype: AuditResource
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this AuditEvent.


        :param resource: The resource of this AuditEvent.  # noqa: E501
        :type: AuditResource
        """
        if resource is None:
            raise ValueError("Invalid value for `resource`, must not be `None`")  # noqa: E501

        self._resource = resource

    @property
    def yaml_diff_record(self):
        """Gets the yaml_diff_record of this AuditEvent.  # noqa: E501


        :return: The yaml_diff_record of this AuditEvent.  # noqa: E501
        :rtype: YamlDiffRecord
        """
        return self._yaml_diff_record

    @yaml_diff_record.setter
    def yaml_diff_record(self, yaml_diff_record):
        """Sets the yaml_diff_record of this AuditEvent.


        :param yaml_diff_record: The yaml_diff_record of this AuditEvent.  # noqa: E501
        :type: YamlDiffRecord
        """

        self._yaml_diff_record = yaml_diff_record

    @property
    def action(self):
        """Gets the action of this AuditEvent.  # noqa: E501

        Action type associated with the Audit.  # noqa: E501

        :return: The action of this AuditEvent.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this AuditEvent.

        Action type associated with the Audit.  # noqa: E501

        :param action: The action of this AuditEvent.  # noqa: E501
        :type: str
        """
        if action is None:
            raise ValueError("Invalid value for `action`, must not be `None`")  # noqa: E501
        allowed_values = ["CREATE", "UPDATE", "RESTORE", "DELETE", "FORCE_DELETE", "UPSERT", "INVITE", "RESEND_INVITE", "REVOKE_INVITE", "ADD_COLLABORATOR", "REMOVE_COLLABORATOR", "CREATE_TOKEN", "REVOKE_TOKEN", "LOGIN", "LOGIN2FA", "UNSUCCESSFUL_LOGIN", "ADD_MEMBERSHIP", "REMOVE_MEMBERSHIP", "ERROR_BUDGET_RESET", "START", "END", "STAGE_START", "STAGE_END", "PAUSE", "RESUME", "ABORT", "TIMEOUT", "SIGNED_EULA", "ROLE_ASSIGNMENT_CREATED", "ROLE_ASSIGNMENT_UPDATED", "ROLE_ASSIGNMENT_DELETED"]  # noqa: E501
        if action not in allowed_values:
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"  # noqa: E501
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def audit_event_data(self):
        """Gets the audit_event_data of this AuditEvent.  # noqa: E501


        :return: The audit_event_data of this AuditEvent.  # noqa: E501
        :rtype: AuditEventData
        """
        return self._audit_event_data

    @audit_event_data.setter
    def audit_event_data(self, audit_event_data):
        """Sets the audit_event_data of this AuditEvent.


        :param audit_event_data: The audit_event_data of this AuditEvent.  # noqa: E501
        :type: AuditEventData
        """

        self._audit_event_data = audit_event_data

    @property
    def internal_info(self):
        """Gets the internal_info of this AuditEvent.  # noqa: E501

        Internal information.  # noqa: E501

        :return: The internal_info of this AuditEvent.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._internal_info

    @internal_info.setter
    def internal_info(self, internal_info):
        """Sets the internal_info of this AuditEvent.

        Internal information.  # noqa: E501

        :param internal_info: The internal_info of this AuditEvent.  # noqa: E501
        :type: dict(str, str)
        """

        self._internal_info = internal_info

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
        if issubclass(AuditEvent, dict):
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
        if not isinstance(other, AuditEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
