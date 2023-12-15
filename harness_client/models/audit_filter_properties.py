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

class AuditFilterProperties(object):
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
        'scopes': 'list[AuditResourceScope]',
        'resources': 'list[AuditResource]',
        'modules': 'list[str]',
        'actions': 'list[str]',
        'environments': 'list[AuditEnvironment]',
        'principals': 'list[AuditPrincipal]',
        'static_filter': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'tags': 'dict(str, str)',
        'filter_type': 'str'
    }

    attribute_map = {
        'scopes': 'scopes',
        'resources': 'resources',
        'modules': 'modules',
        'actions': 'actions',
        'environments': 'environments',
        'principals': 'principals',
        'static_filter': 'staticFilter',
        'start_time': 'startTime',
        'end_time': 'endTime',
        'tags': 'tags',
        'filter_type': 'filterType'
    }

    def __init__(self, scopes=None, resources=None, modules=None, actions=None, environments=None, principals=None, static_filter=None, start_time=None, end_time=None, tags=None, filter_type=None):  # noqa: E501
        """AuditFilterProperties - a model defined in Swagger"""  # noqa: E501
        self._scopes = None
        self._resources = None
        self._modules = None
        self._actions = None
        self._environments = None
        self._principals = None
        self._static_filter = None
        self._start_time = None
        self._end_time = None
        self._tags = None
        self._filter_type = None
        self.discriminator = None
        if scopes is not None:
            self.scopes = scopes
        if resources is not None:
            self.resources = resources
        if modules is not None:
            self.modules = modules
        if actions is not None:
            self.actions = actions
        if environments is not None:
            self.environments = environments
        if principals is not None:
            self.principals = principals
        if static_filter is not None:
            self.static_filter = static_filter
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if tags is not None:
            self.tags = tags
        if filter_type is not None:
            self.filter_type = filter_type

    @property
    def scopes(self):
        """Gets the scopes of this AuditFilterProperties.  # noqa: E501

        List of Resource Scopes  # noqa: E501

        :return: The scopes of this AuditFilterProperties.  # noqa: E501
        :rtype: list[AuditResourceScope]
        """
        return self._scopes

    @scopes.setter
    def scopes(self, scopes):
        """Sets the scopes of this AuditFilterProperties.

        List of Resource Scopes  # noqa: E501

        :param scopes: The scopes of this AuditFilterProperties.  # noqa: E501
        :type: list[AuditResourceScope]
        """

        self._scopes = scopes

    @property
    def resources(self):
        """Gets the resources of this AuditFilterProperties.  # noqa: E501

        List of Resources  # noqa: E501

        :return: The resources of this AuditFilterProperties.  # noqa: E501
        :rtype: list[AuditResource]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this AuditFilterProperties.

        List of Resources  # noqa: E501

        :param resources: The resources of this AuditFilterProperties.  # noqa: E501
        :type: list[AuditResource]
        """

        self._resources = resources

    @property
    def modules(self):
        """Gets the modules of this AuditFilterProperties.  # noqa: E501

        List of Module Types  # noqa: E501

        :return: The modules of this AuditFilterProperties.  # noqa: E501
        :rtype: list[str]
        """
        return self._modules

    @modules.setter
    def modules(self, modules):
        """Sets the modules of this AuditFilterProperties.

        List of Module Types  # noqa: E501

        :param modules: The modules of this AuditFilterProperties.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["CD", "CI", "CV", "CF", "CE", "STO", "CHAOS", "SRM", "IACM", "CET", "IDP", "CODE", "CORE", "PMS", "TEMPLATESERVICE", "SSCA", "GOVERNANCE", "SEI"]  # noqa: E501
        if not set(modules).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `modules` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(modules) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._modules = modules

    @property
    def actions(self):
        """Gets the actions of this AuditFilterProperties.  # noqa: E501

        List of Actions  # noqa: E501

        :return: The actions of this AuditFilterProperties.  # noqa: E501
        :rtype: list[str]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this AuditFilterProperties.

        List of Actions  # noqa: E501

        :param actions: The actions of this AuditFilterProperties.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["CREATE", "UPDATE", "RESTORE", "DELETE", "FORCE_DELETE", "UPSERT", "INVITE", "RESEND_INVITE", "REVOKE_INVITE", "ADD_COLLABORATOR", "REMOVE_COLLABORATOR", "CREATE_TOKEN", "REVOKE_TOKEN", "LOGIN", "LOGIN2FA", "UNSUCCESSFUL_LOGIN", "ADD_MEMBERSHIP", "REMOVE_MEMBERSHIP", "ERROR_BUDGET_RESET", "START", "END", "STAGE_START", "STAGE_END", "PAUSE", "RESUME", "ABORT", "TIMEOUT", "SIGNED_EULA", "ROLE_ASSIGNMENT_CREATED", "ROLE_ASSIGNMENT_UPDATED", "ROLE_ASSIGNMENT_DELETED"]  # noqa: E501
        if not set(actions).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `actions` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(actions) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._actions = actions

    @property
    def environments(self):
        """Gets the environments of this AuditFilterProperties.  # noqa: E501

        List of Environments  # noqa: E501

        :return: The environments of this AuditFilterProperties.  # noqa: E501
        :rtype: list[AuditEnvironment]
        """
        return self._environments

    @environments.setter
    def environments(self, environments):
        """Sets the environments of this AuditFilterProperties.

        List of Environments  # noqa: E501

        :param environments: The environments of this AuditFilterProperties.  # noqa: E501
        :type: list[AuditEnvironment]
        """

        self._environments = environments

    @property
    def principals(self):
        """Gets the principals of this AuditFilterProperties.  # noqa: E501

        List of Principals  # noqa: E501

        :return: The principals of this AuditFilterProperties.  # noqa: E501
        :rtype: list[AuditPrincipal]
        """
        return self._principals

    @principals.setter
    def principals(self, principals):
        """Sets the principals of this AuditFilterProperties.

        List of Principals  # noqa: E501

        :param principals: The principals of this AuditFilterProperties.  # noqa: E501
        :type: list[AuditPrincipal]
        """

        self._principals = principals

    @property
    def static_filter(self):
        """Gets the static_filter of this AuditFilterProperties.  # noqa: E501

        Pre-defined Filter  # noqa: E501

        :return: The static_filter of this AuditFilterProperties.  # noqa: E501
        :rtype: str
        """
        return self._static_filter

    @static_filter.setter
    def static_filter(self, static_filter):
        """Sets the static_filter of this AuditFilterProperties.

        Pre-defined Filter  # noqa: E501

        :param static_filter: The static_filter of this AuditFilterProperties.  # noqa: E501
        :type: str
        """
        allowed_values = ["EXCLUDE_LOGIN_EVENTS", "EXCLUDE_SYSTEM_EVENTS"]  # noqa: E501
        if static_filter not in allowed_values:
            raise ValueError(
                "Invalid value for `static_filter` ({0}), must be one of {1}"  # noqa: E501
                .format(static_filter, allowed_values)
            )

        self._static_filter = static_filter

    @property
    def start_time(self):
        """Gets the start_time of this AuditFilterProperties.  # noqa: E501

        Used to specify a start time for retrieving Audit events that occurred at or after the time indicated.  # noqa: E501

        :return: The start_time of this AuditFilterProperties.  # noqa: E501
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this AuditFilterProperties.

        Used to specify a start time for retrieving Audit events that occurred at or after the time indicated.  # noqa: E501

        :param start_time: The start_time of this AuditFilterProperties.  # noqa: E501
        :type: int
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this AuditFilterProperties.  # noqa: E501

        Used to specify the end time for retrieving Audit events that occurred at or before the time indicated.  # noqa: E501

        :return: The end_time of this AuditFilterProperties.  # noqa: E501
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this AuditFilterProperties.

        Used to specify the end time for retrieving Audit events that occurred at or before the time indicated.  # noqa: E501

        :param end_time: The end_time of this AuditFilterProperties.  # noqa: E501
        :type: int
        """

        self._end_time = end_time

    @property
    def tags(self):
        """Gets the tags of this AuditFilterProperties.  # noqa: E501

        Filter tags as a key-value pair.  # noqa: E501

        :return: The tags of this AuditFilterProperties.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this AuditFilterProperties.

        Filter tags as a key-value pair.  # noqa: E501

        :param tags: The tags of this AuditFilterProperties.  # noqa: E501
        :type: dict(str, str)
        """

        self._tags = tags

    @property
    def filter_type(self):
        """Gets the filter_type of this AuditFilterProperties.  # noqa: E501

        This specifies the corresponding Entity of the filter.  # noqa: E501

        :return: The filter_type of this AuditFilterProperties.  # noqa: E501
        :rtype: str
        """
        return self._filter_type

    @filter_type.setter
    def filter_type(self, filter_type):
        """Sets the filter_type of this AuditFilterProperties.

        This specifies the corresponding Entity of the filter.  # noqa: E501

        :param filter_type: The filter_type of this AuditFilterProperties.  # noqa: E501
        :type: str
        """
        allowed_values = ["Audit"]  # noqa: E501
        if filter_type not in allowed_values:
            raise ValueError(
                "Invalid value for `filter_type` ({0}), must be one of {1}"  # noqa: E501
                .format(filter_type, allowed_values)
            )

        self._filter_type = filter_type

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
        if issubclass(AuditFilterProperties, dict):
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
        if not isinstance(other, AuditFilterProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
