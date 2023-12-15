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

class RepositoriesRepoAccessQuery(object):
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
        'repo': 'str',
        'username': 'str',
        'password': 'str',
        'ssh_private_key': 'str',
        'insecure': 'bool',
        'tls_client_cert_data': 'str',
        'tls_client_cert_key': 'str',
        'type': 'str',
        'name': 'str',
        'enable_oci': 'bool',
        'github_app_private_key': 'str',
        'github_app_id': 'str',
        'github_app_installation_id': 'str',
        'github_app_enterprise_base_url': 'str',
        'proxy': 'str',
        'project': 'str'
    }

    attribute_map = {
        'repo': 'repo',
        'username': 'username',
        'password': 'password',
        'ssh_private_key': 'sshPrivateKey',
        'insecure': 'insecure',
        'tls_client_cert_data': 'tlsClientCertData',
        'tls_client_cert_key': 'tlsClientCertKey',
        'type': 'type',
        'name': 'name',
        'enable_oci': 'enableOci',
        'github_app_private_key': 'githubAppPrivateKey',
        'github_app_id': 'githubAppID',
        'github_app_installation_id': 'githubAppInstallationID',
        'github_app_enterprise_base_url': 'githubAppEnterpriseBaseUrl',
        'proxy': 'proxy',
        'project': 'project'
    }

    def __init__(self, repo=None, username=None, password=None, ssh_private_key=None, insecure=None, tls_client_cert_data=None, tls_client_cert_key=None, type=None, name=None, enable_oci=None, github_app_private_key=None, github_app_id=None, github_app_installation_id=None, github_app_enterprise_base_url=None, proxy=None, project=None):  # noqa: E501
        """RepositoriesRepoAccessQuery - a model defined in Swagger"""  # noqa: E501
        self._repo = None
        self._username = None
        self._password = None
        self._ssh_private_key = None
        self._insecure = None
        self._tls_client_cert_data = None
        self._tls_client_cert_key = None
        self._type = None
        self._name = None
        self._enable_oci = None
        self._github_app_private_key = None
        self._github_app_id = None
        self._github_app_installation_id = None
        self._github_app_enterprise_base_url = None
        self._proxy = None
        self._project = None
        self.discriminator = None
        if repo is not None:
            self.repo = repo
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
        if ssh_private_key is not None:
            self.ssh_private_key = ssh_private_key
        if insecure is not None:
            self.insecure = insecure
        if tls_client_cert_data is not None:
            self.tls_client_cert_data = tls_client_cert_data
        if tls_client_cert_key is not None:
            self.tls_client_cert_key = tls_client_cert_key
        if type is not None:
            self.type = type
        if name is not None:
            self.name = name
        if enable_oci is not None:
            self.enable_oci = enable_oci
        if github_app_private_key is not None:
            self.github_app_private_key = github_app_private_key
        if github_app_id is not None:
            self.github_app_id = github_app_id
        if github_app_installation_id is not None:
            self.github_app_installation_id = github_app_installation_id
        if github_app_enterprise_base_url is not None:
            self.github_app_enterprise_base_url = github_app_enterprise_base_url
        if proxy is not None:
            self.proxy = proxy
        if project is not None:
            self.project = project

    @property
    def repo(self):
        """Gets the repo of this RepositoriesRepoAccessQuery.  # noqa: E501


        :return: The repo of this RepositoriesRepoAccessQuery.  # noqa: E501
        :rtype: str
        """
        return self._repo

    @repo.setter
    def repo(self, repo):
        """Sets the repo of this RepositoriesRepoAccessQuery.


        :param repo: The repo of this RepositoriesRepoAccessQuery.  # noqa: E501
        :type: str
        """

        self._repo = repo

    @property
    def username(self):
        """Gets the username of this RepositoriesRepoAccessQuery.  # noqa: E501


        :return: The username of this RepositoriesRepoAccessQuery.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this RepositoriesRepoAccessQuery.


        :param username: The username of this RepositoriesRepoAccessQuery.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def password(self):
        """Gets the password of this RepositoriesRepoAccessQuery.  # noqa: E501


        :return: The password of this RepositoriesRepoAccessQuery.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this RepositoriesRepoAccessQuery.


        :param password: The password of this RepositoriesRepoAccessQuery.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def ssh_private_key(self):
        """Gets the ssh_private_key of this RepositoriesRepoAccessQuery.  # noqa: E501


        :return: The ssh_private_key of this RepositoriesRepoAccessQuery.  # noqa: E501
        :rtype: str
        """
        return self._ssh_private_key

    @ssh_private_key.setter
    def ssh_private_key(self, ssh_private_key):
        """Sets the ssh_private_key of this RepositoriesRepoAccessQuery.


        :param ssh_private_key: The ssh_private_key of this RepositoriesRepoAccessQuery.  # noqa: E501
        :type: str
        """

        self._ssh_private_key = ssh_private_key

    @property
    def insecure(self):
        """Gets the insecure of this RepositoriesRepoAccessQuery.  # noqa: E501


        :return: The insecure of this RepositoriesRepoAccessQuery.  # noqa: E501
        :rtype: bool
        """
        return self._insecure

    @insecure.setter
    def insecure(self, insecure):
        """Sets the insecure of this RepositoriesRepoAccessQuery.


        :param insecure: The insecure of this RepositoriesRepoAccessQuery.  # noqa: E501
        :type: bool
        """

        self._insecure = insecure

    @property
    def tls_client_cert_data(self):
        """Gets the tls_client_cert_data of this RepositoriesRepoAccessQuery.  # noqa: E501


        :return: The tls_client_cert_data of this RepositoriesRepoAccessQuery.  # noqa: E501
        :rtype: str
        """
        return self._tls_client_cert_data

    @tls_client_cert_data.setter
    def tls_client_cert_data(self, tls_client_cert_data):
        """Sets the tls_client_cert_data of this RepositoriesRepoAccessQuery.


        :param tls_client_cert_data: The tls_client_cert_data of this RepositoriesRepoAccessQuery.  # noqa: E501
        :type: str
        """

        self._tls_client_cert_data = tls_client_cert_data

    @property
    def tls_client_cert_key(self):
        """Gets the tls_client_cert_key of this RepositoriesRepoAccessQuery.  # noqa: E501


        :return: The tls_client_cert_key of this RepositoriesRepoAccessQuery.  # noqa: E501
        :rtype: str
        """
        return self._tls_client_cert_key

    @tls_client_cert_key.setter
    def tls_client_cert_key(self, tls_client_cert_key):
        """Sets the tls_client_cert_key of this RepositoriesRepoAccessQuery.


        :param tls_client_cert_key: The tls_client_cert_key of this RepositoriesRepoAccessQuery.  # noqa: E501
        :type: str
        """

        self._tls_client_cert_key = tls_client_cert_key

    @property
    def type(self):
        """Gets the type of this RepositoriesRepoAccessQuery.  # noqa: E501


        :return: The type of this RepositoriesRepoAccessQuery.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RepositoriesRepoAccessQuery.


        :param type: The type of this RepositoriesRepoAccessQuery.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def name(self):
        """Gets the name of this RepositoriesRepoAccessQuery.  # noqa: E501


        :return: The name of this RepositoriesRepoAccessQuery.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RepositoriesRepoAccessQuery.


        :param name: The name of this RepositoriesRepoAccessQuery.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def enable_oci(self):
        """Gets the enable_oci of this RepositoriesRepoAccessQuery.  # noqa: E501


        :return: The enable_oci of this RepositoriesRepoAccessQuery.  # noqa: E501
        :rtype: bool
        """
        return self._enable_oci

    @enable_oci.setter
    def enable_oci(self, enable_oci):
        """Sets the enable_oci of this RepositoriesRepoAccessQuery.


        :param enable_oci: The enable_oci of this RepositoriesRepoAccessQuery.  # noqa: E501
        :type: bool
        """

        self._enable_oci = enable_oci

    @property
    def github_app_private_key(self):
        """Gets the github_app_private_key of this RepositoriesRepoAccessQuery.  # noqa: E501


        :return: The github_app_private_key of this RepositoriesRepoAccessQuery.  # noqa: E501
        :rtype: str
        """
        return self._github_app_private_key

    @github_app_private_key.setter
    def github_app_private_key(self, github_app_private_key):
        """Sets the github_app_private_key of this RepositoriesRepoAccessQuery.


        :param github_app_private_key: The github_app_private_key of this RepositoriesRepoAccessQuery.  # noqa: E501
        :type: str
        """

        self._github_app_private_key = github_app_private_key

    @property
    def github_app_id(self):
        """Gets the github_app_id of this RepositoriesRepoAccessQuery.  # noqa: E501


        :return: The github_app_id of this RepositoriesRepoAccessQuery.  # noqa: E501
        :rtype: str
        """
        return self._github_app_id

    @github_app_id.setter
    def github_app_id(self, github_app_id):
        """Sets the github_app_id of this RepositoriesRepoAccessQuery.


        :param github_app_id: The github_app_id of this RepositoriesRepoAccessQuery.  # noqa: E501
        :type: str
        """

        self._github_app_id = github_app_id

    @property
    def github_app_installation_id(self):
        """Gets the github_app_installation_id of this RepositoriesRepoAccessQuery.  # noqa: E501


        :return: The github_app_installation_id of this RepositoriesRepoAccessQuery.  # noqa: E501
        :rtype: str
        """
        return self._github_app_installation_id

    @github_app_installation_id.setter
    def github_app_installation_id(self, github_app_installation_id):
        """Sets the github_app_installation_id of this RepositoriesRepoAccessQuery.


        :param github_app_installation_id: The github_app_installation_id of this RepositoriesRepoAccessQuery.  # noqa: E501
        :type: str
        """

        self._github_app_installation_id = github_app_installation_id

    @property
    def github_app_enterprise_base_url(self):
        """Gets the github_app_enterprise_base_url of this RepositoriesRepoAccessQuery.  # noqa: E501


        :return: The github_app_enterprise_base_url of this RepositoriesRepoAccessQuery.  # noqa: E501
        :rtype: str
        """
        return self._github_app_enterprise_base_url

    @github_app_enterprise_base_url.setter
    def github_app_enterprise_base_url(self, github_app_enterprise_base_url):
        """Sets the github_app_enterprise_base_url of this RepositoriesRepoAccessQuery.


        :param github_app_enterprise_base_url: The github_app_enterprise_base_url of this RepositoriesRepoAccessQuery.  # noqa: E501
        :type: str
        """

        self._github_app_enterprise_base_url = github_app_enterprise_base_url

    @property
    def proxy(self):
        """Gets the proxy of this RepositoriesRepoAccessQuery.  # noqa: E501


        :return: The proxy of this RepositoriesRepoAccessQuery.  # noqa: E501
        :rtype: str
        """
        return self._proxy

    @proxy.setter
    def proxy(self, proxy):
        """Sets the proxy of this RepositoriesRepoAccessQuery.


        :param proxy: The proxy of this RepositoriesRepoAccessQuery.  # noqa: E501
        :type: str
        """

        self._proxy = proxy

    @property
    def project(self):
        """Gets the project of this RepositoriesRepoAccessQuery.  # noqa: E501


        :return: The project of this RepositoriesRepoAccessQuery.  # noqa: E501
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this RepositoriesRepoAccessQuery.


        :param project: The project of this RepositoriesRepoAccessQuery.  # noqa: E501
        :type: str
        """

        self._project = project

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
        if issubclass(RepositoriesRepoAccessQuery, dict):
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
        if not isinstance(other, RepositoriesRepoAccessQuery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
