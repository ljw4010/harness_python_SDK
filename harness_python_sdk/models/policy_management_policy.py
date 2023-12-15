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

class PolicyManagementPolicy(object):
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
        'account_id': 'str',
        'created': 'int',
        'git_commit_sha': 'str',
        'git_connector_ref': 'str',
        'git_default_branch': 'str',
        'git_default_branch_commit_sha': 'str',
        'git_default_branch_file_id': 'str',
        'git_default_branch_file_url': 'str',
        'git_default_branch_update_error': 'GitErrorResult',
        'git_default_branch_updated': 'int',
        'git_file_id': 'str',
        'git_file_url': 'str',
        'git_path': 'str',
        'git_repo': 'str',
        'identifier': 'str',
        'name': 'str',
        'org_id': 'str',
        'project_id': 'str',
        'rego': 'str',
        'updated': 'int'
    }

    attribute_map = {
        'account_id': 'account_id',
        'created': 'created',
        'git_commit_sha': 'git_commit_sha',
        'git_connector_ref': 'git_connector_ref',
        'git_default_branch': 'git_default_branch',
        'git_default_branch_commit_sha': 'git_default_branch_commit_sha',
        'git_default_branch_file_id': 'git_default_branch_file_id',
        'git_default_branch_file_url': 'git_default_branch_file_url',
        'git_default_branch_update_error': 'git_default_branch_update_error',
        'git_default_branch_updated': 'git_default_branch_updated',
        'git_file_id': 'git_file_id',
        'git_file_url': 'git_file_url',
        'git_path': 'git_path',
        'git_repo': 'git_repo',
        'identifier': 'identifier',
        'name': 'name',
        'org_id': 'org_id',
        'project_id': 'project_id',
        'rego': 'rego',
        'updated': 'updated'
    }

    def __init__(self, account_id='', created=None, git_commit_sha=None, git_connector_ref=None, git_default_branch=None, git_default_branch_commit_sha=None, git_default_branch_file_id=None, git_default_branch_file_url=None, git_default_branch_update_error=None, git_default_branch_updated=None, git_file_id=None, git_file_url=None, git_path=None, git_repo=None, identifier=None, name=None, org_id='', project_id='', rego=None, updated=None):  # noqa: E501
        """PolicyManagementPolicy - a model defined in Swagger"""  # noqa: E501
        self._account_id = None
        self._created = None
        self._git_commit_sha = None
        self._git_connector_ref = None
        self._git_default_branch = None
        self._git_default_branch_commit_sha = None
        self._git_default_branch_file_id = None
        self._git_default_branch_file_url = None
        self._git_default_branch_update_error = None
        self._git_default_branch_updated = None
        self._git_file_id = None
        self._git_file_url = None
        self._git_path = None
        self._git_repo = None
        self._identifier = None
        self._name = None
        self._org_id = None
        self._project_id = None
        self._rego = None
        self._updated = None
        self.discriminator = None
        self.account_id = account_id
        self.created = created
        if git_commit_sha is not None:
            self.git_commit_sha = git_commit_sha
        if git_connector_ref is not None:
            self.git_connector_ref = git_connector_ref
        if git_default_branch is not None:
            self.git_default_branch = git_default_branch
        if git_default_branch_commit_sha is not None:
            self.git_default_branch_commit_sha = git_default_branch_commit_sha
        if git_default_branch_file_id is not None:
            self.git_default_branch_file_id = git_default_branch_file_id
        if git_default_branch_file_url is not None:
            self.git_default_branch_file_url = git_default_branch_file_url
        if git_default_branch_update_error is not None:
            self.git_default_branch_update_error = git_default_branch_update_error
        if git_default_branch_updated is not None:
            self.git_default_branch_updated = git_default_branch_updated
        if git_file_id is not None:
            self.git_file_id = git_file_id
        if git_file_url is not None:
            self.git_file_url = git_file_url
        if git_path is not None:
            self.git_path = git_path
        if git_repo is not None:
            self.git_repo = git_repo
        self.identifier = identifier
        self.name = name
        self.org_id = org_id
        self.project_id = project_id
        self.rego = rego
        self.updated = updated

    @property
    def account_id(self):
        """Gets the account_id of this PolicyManagementPolicy.  # noqa: E501

        Harness account ID associated with this policy  # noqa: E501

        :return: The account_id of this PolicyManagementPolicy.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this PolicyManagementPolicy.

        Harness account ID associated with this policy  # noqa: E501

        :param account_id: The account_id of this PolicyManagementPolicy.  # noqa: E501
        :type: str
        """
        if account_id is None:
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def created(self):
        """Gets the created of this PolicyManagementPolicy.  # noqa: E501

        Time the policy was created  # noqa: E501

        :return: The created of this PolicyManagementPolicy.  # noqa: E501
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this PolicyManagementPolicy.

        Time the policy was created  # noqa: E501

        :param created: The created of this PolicyManagementPolicy.  # noqa: E501
        :type: int
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def git_commit_sha(self):
        """Gets the git_commit_sha of this PolicyManagementPolicy.  # noqa: E501

        The commit sha of the commit that last effected the file  # noqa: E501

        :return: The git_commit_sha of this PolicyManagementPolicy.  # noqa: E501
        :rtype: str
        """
        return self._git_commit_sha

    @git_commit_sha.setter
    def git_commit_sha(self, git_commit_sha):
        """Sets the git_commit_sha of this PolicyManagementPolicy.

        The commit sha of the commit that last effected the file  # noqa: E501

        :param git_commit_sha: The git_commit_sha of this PolicyManagementPolicy.  # noqa: E501
        :type: str
        """

        self._git_commit_sha = git_commit_sha

    @property
    def git_connector_ref(self):
        """Gets the git_connector_ref of this PolicyManagementPolicy.  # noqa: E501

        The harness connector used for authenticating on the git provider  # noqa: E501

        :return: The git_connector_ref of this PolicyManagementPolicy.  # noqa: E501
        :rtype: str
        """
        return self._git_connector_ref

    @git_connector_ref.setter
    def git_connector_ref(self, git_connector_ref):
        """Sets the git_connector_ref of this PolicyManagementPolicy.

        The harness connector used for authenticating on the git provider  # noqa: E501

        :param git_connector_ref: The git_connector_ref of this PolicyManagementPolicy.  # noqa: E501
        :type: str
        """

        self._git_connector_ref = git_connector_ref

    @property
    def git_default_branch(self):
        """Gets the git_default_branch of this PolicyManagementPolicy.  # noqa: E501

        The default branch, the service pulls in changes from from this branch for policy evaluation  # noqa: E501

        :return: The git_default_branch of this PolicyManagementPolicy.  # noqa: E501
        :rtype: str
        """
        return self._git_default_branch

    @git_default_branch.setter
    def git_default_branch(self, git_default_branch):
        """Sets the git_default_branch of this PolicyManagementPolicy.

        The default branch, the service pulls in changes from from this branch for policy evaluation  # noqa: E501

        :param git_default_branch: The git_default_branch of this PolicyManagementPolicy.  # noqa: E501
        :type: str
        """

        self._git_default_branch = git_default_branch

    @property
    def git_default_branch_commit_sha(self):
        """Gets the git_default_branch_commit_sha of this PolicyManagementPolicy.  # noqa: E501

        The commit sha of the commit that last effected the file in the default branch  # noqa: E501

        :return: The git_default_branch_commit_sha of this PolicyManagementPolicy.  # noqa: E501
        :rtype: str
        """
        return self._git_default_branch_commit_sha

    @git_default_branch_commit_sha.setter
    def git_default_branch_commit_sha(self, git_default_branch_commit_sha):
        """Sets the git_default_branch_commit_sha of this PolicyManagementPolicy.

        The commit sha of the commit that last effected the file in the default branch  # noqa: E501

        :param git_default_branch_commit_sha: The git_default_branch_commit_sha of this PolicyManagementPolicy.  # noqa: E501
        :type: str
        """

        self._git_default_branch_commit_sha = git_default_branch_commit_sha

    @property
    def git_default_branch_file_id(self):
        """Gets the git_default_branch_file_id of this PolicyManagementPolicy.  # noqa: E501

        The file id of the file in the default branch, may be empty for bitbucket files  # noqa: E501

        :return: The git_default_branch_file_id of this PolicyManagementPolicy.  # noqa: E501
        :rtype: str
        """
        return self._git_default_branch_file_id

    @git_default_branch_file_id.setter
    def git_default_branch_file_id(self, git_default_branch_file_id):
        """Sets the git_default_branch_file_id of this PolicyManagementPolicy.

        The file id of the file in the default branch, may be empty for bitbucket files  # noqa: E501

        :param git_default_branch_file_id: The git_default_branch_file_id of this PolicyManagementPolicy.  # noqa: E501
        :type: str
        """

        self._git_default_branch_file_id = git_default_branch_file_id

    @property
    def git_default_branch_file_url(self):
        """Gets the git_default_branch_file_url of this PolicyManagementPolicy.  # noqa: E501

        The url of the file in the default branch  # noqa: E501

        :return: The git_default_branch_file_url of this PolicyManagementPolicy.  # noqa: E501
        :rtype: str
        """
        return self._git_default_branch_file_url

    @git_default_branch_file_url.setter
    def git_default_branch_file_url(self, git_default_branch_file_url):
        """Sets the git_default_branch_file_url of this PolicyManagementPolicy.

        The url of the file in the default branch  # noqa: E501

        :param git_default_branch_file_url: The git_default_branch_file_url of this PolicyManagementPolicy.  # noqa: E501
        :type: str
        """

        self._git_default_branch_file_url = git_default_branch_file_url

    @property
    def git_default_branch_update_error(self):
        """Gets the git_default_branch_update_error of this PolicyManagementPolicy.  # noqa: E501


        :return: The git_default_branch_update_error of this PolicyManagementPolicy.  # noqa: E501
        :rtype: GitErrorResult
        """
        return self._git_default_branch_update_error

    @git_default_branch_update_error.setter
    def git_default_branch_update_error(self, git_default_branch_update_error):
        """Sets the git_default_branch_update_error of this PolicyManagementPolicy.


        :param git_default_branch_update_error: The git_default_branch_update_error of this PolicyManagementPolicy.  # noqa: E501
        :type: GitErrorResult
        """

        self._git_default_branch_update_error = git_default_branch_update_error

    @property
    def git_default_branch_updated(self):
        """Gets the git_default_branch_updated of this PolicyManagementPolicy.  # noqa: E501

        The last time the service successfully pulled in changes from the default branch  # noqa: E501

        :return: The git_default_branch_updated of this PolicyManagementPolicy.  # noqa: E501
        :rtype: int
        """
        return self._git_default_branch_updated

    @git_default_branch_updated.setter
    def git_default_branch_updated(self, git_default_branch_updated):
        """Sets the git_default_branch_updated of this PolicyManagementPolicy.

        The last time the service successfully pulled in changes from the default branch  # noqa: E501

        :param git_default_branch_updated: The git_default_branch_updated of this PolicyManagementPolicy.  # noqa: E501
        :type: int
        """

        self._git_default_branch_updated = git_default_branch_updated

    @property
    def git_file_id(self):
        """Gets the git_file_id of this PolicyManagementPolicy.  # noqa: E501

        The file id of the file, may be empty for bitbucket files  # noqa: E501

        :return: The git_file_id of this PolicyManagementPolicy.  # noqa: E501
        :rtype: str
        """
        return self._git_file_id

    @git_file_id.setter
    def git_file_id(self, git_file_id):
        """Sets the git_file_id of this PolicyManagementPolicy.

        The file id of the file, may be empty for bitbucket files  # noqa: E501

        :param git_file_id: The git_file_id of this PolicyManagementPolicy.  # noqa: E501
        :type: str
        """

        self._git_file_id = git_file_id

    @property
    def git_file_url(self):
        """Gets the git_file_url of this PolicyManagementPolicy.  # noqa: E501

        The url of the file on the fit provider  # noqa: E501

        :return: The git_file_url of this PolicyManagementPolicy.  # noqa: E501
        :rtype: str
        """
        return self._git_file_url

    @git_file_url.setter
    def git_file_url(self, git_file_url):
        """Sets the git_file_url of this PolicyManagementPolicy.

        The url of the file on the fit provider  # noqa: E501

        :param git_file_url: The git_file_url of this PolicyManagementPolicy.  # noqa: E501
        :type: str
        """

        self._git_file_url = git_file_url

    @property
    def git_path(self):
        """Gets the git_path of this PolicyManagementPolicy.  # noqa: E501

        The path to the file in the git repo  # noqa: E501

        :return: The git_path of this PolicyManagementPolicy.  # noqa: E501
        :rtype: str
        """
        return self._git_path

    @git_path.setter
    def git_path(self, git_path):
        """Sets the git_path of this PolicyManagementPolicy.

        The path to the file in the git repo  # noqa: E501

        :param git_path: The git_path of this PolicyManagementPolicy.  # noqa: E501
        :type: str
        """

        self._git_path = git_path

    @property
    def git_repo(self):
        """Gets the git_repo of this PolicyManagementPolicy.  # noqa: E501

        The git repo the policy resides in  # noqa: E501

        :return: The git_repo of this PolicyManagementPolicy.  # noqa: E501
        :rtype: str
        """
        return self._git_repo

    @git_repo.setter
    def git_repo(self, git_repo):
        """Sets the git_repo of this PolicyManagementPolicy.

        The git repo the policy resides in  # noqa: E501

        :param git_repo: The git_repo of this PolicyManagementPolicy.  # noqa: E501
        :type: str
        """

        self._git_repo = git_repo

    @property
    def identifier(self):
        """Gets the identifier of this PolicyManagementPolicy.  # noqa: E501

        identifier of the policy  # noqa: E501

        :return: The identifier of this PolicyManagementPolicy.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this PolicyManagementPolicy.

        identifier of the policy  # noqa: E501

        :param identifier: The identifier of this PolicyManagementPolicy.  # noqa: E501
        :type: str
        """
        if identifier is None:
            raise ValueError("Invalid value for `identifier`, must not be `None`")  # noqa: E501

        self._identifier = identifier

    @property
    def name(self):
        """Gets the name of this PolicyManagementPolicy.  # noqa: E501

        Name of the policy  # noqa: E501

        :return: The name of this PolicyManagementPolicy.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PolicyManagementPolicy.

        Name of the policy  # noqa: E501

        :param name: The name of this PolicyManagementPolicy.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def org_id(self):
        """Gets the org_id of this PolicyManagementPolicy.  # noqa: E501

        Harness organization ID associated with this policy  # noqa: E501

        :return: The org_id of this PolicyManagementPolicy.  # noqa: E501
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this PolicyManagementPolicy.

        Harness organization ID associated with this policy  # noqa: E501

        :param org_id: The org_id of this PolicyManagementPolicy.  # noqa: E501
        :type: str
        """
        if org_id is None:
            raise ValueError("Invalid value for `org_id`, must not be `None`")  # noqa: E501

        self._org_id = org_id

    @property
    def project_id(self):
        """Gets the project_id of this PolicyManagementPolicy.  # noqa: E501

        Harness project ID associated with this policy  # noqa: E501

        :return: The project_id of this PolicyManagementPolicy.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this PolicyManagementPolicy.

        Harness project ID associated with this policy  # noqa: E501

        :param project_id: The project_id of this PolicyManagementPolicy.  # noqa: E501
        :type: str
        """
        if project_id is None:
            raise ValueError("Invalid value for `project_id`, must not be `None`")  # noqa: E501

        self._project_id = project_id

    @property
    def rego(self):
        """Gets the rego of this PolicyManagementPolicy.  # noqa: E501

        Rego that defines the policy  # noqa: E501

        :return: The rego of this PolicyManagementPolicy.  # noqa: E501
        :rtype: str
        """
        return self._rego

    @rego.setter
    def rego(self, rego):
        """Sets the rego of this PolicyManagementPolicy.

        Rego that defines the policy  # noqa: E501

        :param rego: The rego of this PolicyManagementPolicy.  # noqa: E501
        :type: str
        """
        if rego is None:
            raise ValueError("Invalid value for `rego`, must not be `None`")  # noqa: E501

        self._rego = rego

    @property
    def updated(self):
        """Gets the updated of this PolicyManagementPolicy.  # noqa: E501

        Time the policy was last updated  # noqa: E501

        :return: The updated of this PolicyManagementPolicy.  # noqa: E501
        :rtype: int
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this PolicyManagementPolicy.

        Time the policy was last updated  # noqa: E501

        :param updated: The updated of this PolicyManagementPolicy.  # noqa: E501
        :type: int
        """
        if updated is None:
            raise ValueError("Invalid value for `updated`, must not be `None`")  # noqa: E501

        self._updated = updated

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
        if issubclass(PolicyManagementPolicy, dict):
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
        if not isinstance(other, PolicyManagementPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
