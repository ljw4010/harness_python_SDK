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

class GitSyncSettings(object):
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
        'project_identifier': 'str',
        'org_identifier': 'str',
        'execute_on_delegate': 'bool',
        'is_git_simplification_enabled': 'bool',
        'is_enabled_only_for_ff': 'bool',
        'git_simplification_enabled': 'bool',
        'enabled_only_for_ff': 'bool'
    }

    attribute_map = {
        'project_identifier': 'projectIdentifier',
        'org_identifier': 'orgIdentifier',
        'execute_on_delegate': 'executeOnDelegate',
        'is_git_simplification_enabled': 'isGitSimplificationEnabled',
        'is_enabled_only_for_ff': 'isEnabledOnlyForFF',
        'git_simplification_enabled': 'gitSimplificationEnabled',
        'enabled_only_for_ff': 'enabledOnlyForFF'
    }

    def __init__(self, project_identifier=None, org_identifier=None, execute_on_delegate=None, is_git_simplification_enabled=None, is_enabled_only_for_ff=None, git_simplification_enabled=None, enabled_only_for_ff=None):  # noqa: E501
        """GitSyncSettings - a model defined in Swagger"""  # noqa: E501
        self._project_identifier = None
        self._org_identifier = None
        self._execute_on_delegate = None
        self._is_git_simplification_enabled = None
        self._is_enabled_only_for_ff = None
        self._git_simplification_enabled = None
        self._enabled_only_for_ff = None
        self.discriminator = None
        self.project_identifier = project_identifier
        self.org_identifier = org_identifier
        self.execute_on_delegate = execute_on_delegate
        if is_git_simplification_enabled is not None:
            self.is_git_simplification_enabled = is_git_simplification_enabled
        if is_enabled_only_for_ff is not None:
            self.is_enabled_only_for_ff = is_enabled_only_for_ff
        if git_simplification_enabled is not None:
            self.git_simplification_enabled = git_simplification_enabled
        if enabled_only_for_ff is not None:
            self.enabled_only_for_ff = enabled_only_for_ff

    @property
    def project_identifier(self):
        """Gets the project_identifier of this GitSyncSettings.  # noqa: E501

        Project Identifier for the Entity.  # noqa: E501

        :return: The project_identifier of this GitSyncSettings.  # noqa: E501
        :rtype: str
        """
        return self._project_identifier

    @project_identifier.setter
    def project_identifier(self, project_identifier):
        """Sets the project_identifier of this GitSyncSettings.

        Project Identifier for the Entity.  # noqa: E501

        :param project_identifier: The project_identifier of this GitSyncSettings.  # noqa: E501
        :type: str
        """
        if project_identifier is None:
            raise ValueError("Invalid value for `project_identifier`, must not be `None`")  # noqa: E501

        self._project_identifier = project_identifier

    @property
    def org_identifier(self):
        """Gets the org_identifier of this GitSyncSettings.  # noqa: E501

        Organization Identifier for the Entity.  # noqa: E501

        :return: The org_identifier of this GitSyncSettings.  # noqa: E501
        :rtype: str
        """
        return self._org_identifier

    @org_identifier.setter
    def org_identifier(self, org_identifier):
        """Sets the org_identifier of this GitSyncSettings.

        Organization Identifier for the Entity.  # noqa: E501

        :param org_identifier: The org_identifier of this GitSyncSettings.  # noqa: E501
        :type: str
        """
        if org_identifier is None:
            raise ValueError("Invalid value for `org_identifier`, must not be `None`")  # noqa: E501

        self._org_identifier = org_identifier

    @property
    def execute_on_delegate(self):
        """Gets the execute_on_delegate of this GitSyncSettings.  # noqa: E501

        Specifies Connectivity Mode for Git Sync. If True, executes through Delegate, else executes through Platform. The default value is True  # noqa: E501

        :return: The execute_on_delegate of this GitSyncSettings.  # noqa: E501
        :rtype: bool
        """
        return self._execute_on_delegate

    @execute_on_delegate.setter
    def execute_on_delegate(self, execute_on_delegate):
        """Sets the execute_on_delegate of this GitSyncSettings.

        Specifies Connectivity Mode for Git Sync. If True, executes through Delegate, else executes through Platform. The default value is True  # noqa: E501

        :param execute_on_delegate: The execute_on_delegate of this GitSyncSettings.  # noqa: E501
        :type: bool
        """
        if execute_on_delegate is None:
            raise ValueError("Invalid value for `execute_on_delegate`, must not be `None`")  # noqa: E501

        self._execute_on_delegate = execute_on_delegate

    @property
    def is_git_simplification_enabled(self):
        """Gets the is_git_simplification_enabled of this GitSyncSettings.  # noqa: E501


        :return: The is_git_simplification_enabled of this GitSyncSettings.  # noqa: E501
        :rtype: bool
        """
        return self._is_git_simplification_enabled

    @is_git_simplification_enabled.setter
    def is_git_simplification_enabled(self, is_git_simplification_enabled):
        """Sets the is_git_simplification_enabled of this GitSyncSettings.


        :param is_git_simplification_enabled: The is_git_simplification_enabled of this GitSyncSettings.  # noqa: E501
        :type: bool
        """

        self._is_git_simplification_enabled = is_git_simplification_enabled

    @property
    def is_enabled_only_for_ff(self):
        """Gets the is_enabled_only_for_ff of this GitSyncSettings.  # noqa: E501


        :return: The is_enabled_only_for_ff of this GitSyncSettings.  # noqa: E501
        :rtype: bool
        """
        return self._is_enabled_only_for_ff

    @is_enabled_only_for_ff.setter
    def is_enabled_only_for_ff(self, is_enabled_only_for_ff):
        """Sets the is_enabled_only_for_ff of this GitSyncSettings.


        :param is_enabled_only_for_ff: The is_enabled_only_for_ff of this GitSyncSettings.  # noqa: E501
        :type: bool
        """

        self._is_enabled_only_for_ff = is_enabled_only_for_ff

    @property
    def git_simplification_enabled(self):
        """Gets the git_simplification_enabled of this GitSyncSettings.  # noqa: E501


        :return: The git_simplification_enabled of this GitSyncSettings.  # noqa: E501
        :rtype: bool
        """
        return self._git_simplification_enabled

    @git_simplification_enabled.setter
    def git_simplification_enabled(self, git_simplification_enabled):
        """Sets the git_simplification_enabled of this GitSyncSettings.


        :param git_simplification_enabled: The git_simplification_enabled of this GitSyncSettings.  # noqa: E501
        :type: bool
        """

        self._git_simplification_enabled = git_simplification_enabled

    @property
    def enabled_only_for_ff(self):
        """Gets the enabled_only_for_ff of this GitSyncSettings.  # noqa: E501


        :return: The enabled_only_for_ff of this GitSyncSettings.  # noqa: E501
        :rtype: bool
        """
        return self._enabled_only_for_ff

    @enabled_only_for_ff.setter
    def enabled_only_for_ff(self, enabled_only_for_ff):
        """Sets the enabled_only_for_ff of this GitSyncSettings.


        :param enabled_only_for_ff: The enabled_only_for_ff of this GitSyncSettings.  # noqa: E501
        :type: bool
        """

        self._enabled_only_for_ff = enabled_only_for_ff

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
        if issubclass(GitSyncSettings, dict):
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
        if not isinstance(other, GitSyncSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
