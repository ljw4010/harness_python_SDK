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

class GitFullSyncConfigRequest(object):
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
        'branch': 'str',
        'repo_identifier': 'str',
        'root_folder': 'str',
        'is_new_branch': 'bool',
        'base_branch': 'str',
        'create_pull_request': 'bool',
        'target_branch': 'str',
        'pr_title': 'str',
        'new_branch': 'bool'
    }

    attribute_map = {
        'branch': 'branch',
        'repo_identifier': 'repoIdentifier',
        'root_folder': 'rootFolder',
        'is_new_branch': 'isNewBranch',
        'base_branch': 'baseBranch',
        'create_pull_request': 'createPullRequest',
        'target_branch': 'targetBranch',
        'pr_title': 'prTitle',
        'new_branch': 'newBranch'
    }

    def __init__(self, branch=None, repo_identifier=None, root_folder=None, is_new_branch=None, base_branch=None, create_pull_request=None, target_branch=None, pr_title=None, new_branch=None):  # noqa: E501
        """GitFullSyncConfigRequest - a model defined in Swagger"""  # noqa: E501
        self._branch = None
        self._repo_identifier = None
        self._root_folder = None
        self._is_new_branch = None
        self._base_branch = None
        self._create_pull_request = None
        self._target_branch = None
        self._pr_title = None
        self._new_branch = None
        self.discriminator = None
        self.branch = branch
        self.repo_identifier = repo_identifier
        self.root_folder = root_folder
        if is_new_branch is not None:
            self.is_new_branch = is_new_branch
        if base_branch is not None:
            self.base_branch = base_branch
        if create_pull_request is not None:
            self.create_pull_request = create_pull_request
        if target_branch is not None:
            self.target_branch = target_branch
        if pr_title is not None:
            self.pr_title = pr_title
        if new_branch is not None:
            self.new_branch = new_branch

    @property
    def branch(self):
        """Gets the branch of this GitFullSyncConfigRequest.  # noqa: E501

        Name of the branch to which the entities will be pushed and from which pull request will be created.  # noqa: E501

        :return: The branch of this GitFullSyncConfigRequest.  # noqa: E501
        :rtype: str
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        """Sets the branch of this GitFullSyncConfigRequest.

        Name of the branch to which the entities will be pushed and from which pull request will be created.  # noqa: E501

        :param branch: The branch of this GitFullSyncConfigRequest.  # noqa: E501
        :type: str
        """
        if branch is None:
            raise ValueError("Invalid value for `branch`, must not be `None`")  # noqa: E501

        self._branch = branch

    @property
    def repo_identifier(self):
        """Gets the repo_identifier of this GitFullSyncConfigRequest.  # noqa: E501

        Git Sync Config Id.  # noqa: E501

        :return: The repo_identifier of this GitFullSyncConfigRequest.  # noqa: E501
        :rtype: str
        """
        return self._repo_identifier

    @repo_identifier.setter
    def repo_identifier(self, repo_identifier):
        """Sets the repo_identifier of this GitFullSyncConfigRequest.

        Git Sync Config Id.  # noqa: E501

        :param repo_identifier: The repo_identifier of this GitFullSyncConfigRequest.  # noqa: E501
        :type: str
        """
        if repo_identifier is None:
            raise ValueError("Invalid value for `repo_identifier`, must not be `None`")  # noqa: E501

        self._repo_identifier = repo_identifier

    @property
    def root_folder(self):
        """Gets the root_folder of this GitFullSyncConfigRequest.  # noqa: E501

        Path of the root folder inside which the entities will be pushed.  # noqa: E501

        :return: The root_folder of this GitFullSyncConfigRequest.  # noqa: E501
        :rtype: str
        """
        return self._root_folder

    @root_folder.setter
    def root_folder(self, root_folder):
        """Sets the root_folder of this GitFullSyncConfigRequest.

        Path of the root folder inside which the entities will be pushed.  # noqa: E501

        :param root_folder: The root_folder of this GitFullSyncConfigRequest.  # noqa: E501
        :type: str
        """
        if root_folder is None:
            raise ValueError("Invalid value for `root_folder`, must not be `None`")  # noqa: E501

        self._root_folder = root_folder

    @property
    def is_new_branch(self):
        """Gets the is_new_branch of this GitFullSyncConfigRequest.  # noqa: E501


        :return: The is_new_branch of this GitFullSyncConfigRequest.  # noqa: E501
        :rtype: bool
        """
        return self._is_new_branch

    @is_new_branch.setter
    def is_new_branch(self, is_new_branch):
        """Sets the is_new_branch of this GitFullSyncConfigRequest.


        :param is_new_branch: The is_new_branch of this GitFullSyncConfigRequest.  # noqa: E501
        :type: bool
        """

        self._is_new_branch = is_new_branch

    @property
    def base_branch(self):
        """Gets the base_branch of this GitFullSyncConfigRequest.  # noqa: E501

        Name of the branch from which new branch will be forked out.  # noqa: E501

        :return: The base_branch of this GitFullSyncConfigRequest.  # noqa: E501
        :rtype: str
        """
        return self._base_branch

    @base_branch.setter
    def base_branch(self, base_branch):
        """Sets the base_branch of this GitFullSyncConfigRequest.

        Name of the branch from which new branch will be forked out.  # noqa: E501

        :param base_branch: The base_branch of this GitFullSyncConfigRequest.  # noqa: E501
        :type: str
        """

        self._base_branch = base_branch

    @property
    def create_pull_request(self):
        """Gets the create_pull_request of this GitFullSyncConfigRequest.  # noqa: E501

        If true a pull request will be created from branch to target branch.Default: false.  # noqa: E501

        :return: The create_pull_request of this GitFullSyncConfigRequest.  # noqa: E501
        :rtype: bool
        """
        return self._create_pull_request

    @create_pull_request.setter
    def create_pull_request(self, create_pull_request):
        """Sets the create_pull_request of this GitFullSyncConfigRequest.

        If true a pull request will be created from branch to target branch.Default: false.  # noqa: E501

        :param create_pull_request: The create_pull_request of this GitFullSyncConfigRequest.  # noqa: E501
        :type: bool
        """

        self._create_pull_request = create_pull_request

    @property
    def target_branch(self):
        """Gets the target_branch of this GitFullSyncConfigRequest.  # noqa: E501

        Name of the branch to which pull request will be merged.  # noqa: E501

        :return: The target_branch of this GitFullSyncConfigRequest.  # noqa: E501
        :rtype: str
        """
        return self._target_branch

    @target_branch.setter
    def target_branch(self, target_branch):
        """Sets the target_branch of this GitFullSyncConfigRequest.

        Name of the branch to which pull request will be merged.  # noqa: E501

        :param target_branch: The target_branch of this GitFullSyncConfigRequest.  # noqa: E501
        :type: str
        """

        self._target_branch = target_branch

    @property
    def pr_title(self):
        """Gets the pr_title of this GitFullSyncConfigRequest.  # noqa: E501

        Title of the pull request.  # noqa: E501

        :return: The pr_title of this GitFullSyncConfigRequest.  # noqa: E501
        :rtype: str
        """
        return self._pr_title

    @pr_title.setter
    def pr_title(self, pr_title):
        """Sets the pr_title of this GitFullSyncConfigRequest.

        Title of the pull request.  # noqa: E501

        :param pr_title: The pr_title of this GitFullSyncConfigRequest.  # noqa: E501
        :type: str
        """

        self._pr_title = pr_title

    @property
    def new_branch(self):
        """Gets the new_branch of this GitFullSyncConfigRequest.  # noqa: E501


        :return: The new_branch of this GitFullSyncConfigRequest.  # noqa: E501
        :rtype: bool
        """
        return self._new_branch

    @new_branch.setter
    def new_branch(self, new_branch):
        """Sets the new_branch of this GitFullSyncConfigRequest.


        :param new_branch: The new_branch of this GitFullSyncConfigRequest.  # noqa: E501
        :type: bool
        """

        self._new_branch = new_branch

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
        if issubclass(GitFullSyncConfigRequest, dict):
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
        if not isinstance(other, GitFullSyncConfigRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
