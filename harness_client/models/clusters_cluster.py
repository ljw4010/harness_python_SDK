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

class ClustersCluster(object):
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
        'server': 'str',
        'name': 'str',
        'config': 'ClustersClusterConfig',
        'connection_state': 'CommonsConnectionState',
        'server_version': 'str',
        'namespaces': 'list[str]',
        'refresh_requested_at': 'V1Time',
        'info': 'ClustersClusterInfo',
        'shard': 'str',
        'cluster_resources': 'bool',
        'project': 'str',
        'labels': 'dict(str, str)',
        'annotations': 'dict(str, str)'
    }

    attribute_map = {
        'server': 'server',
        'name': 'name',
        'config': 'config',
        'connection_state': 'connectionState',
        'server_version': 'serverVersion',
        'namespaces': 'namespaces',
        'refresh_requested_at': 'refreshRequestedAt',
        'info': 'info',
        'shard': 'shard',
        'cluster_resources': 'clusterResources',
        'project': 'project',
        'labels': 'labels',
        'annotations': 'annotations'
    }

    def __init__(self, server=None, name=None, config=None, connection_state=None, server_version=None, namespaces=None, refresh_requested_at=None, info=None, shard=None, cluster_resources=None, project=None, labels=None, annotations=None):  # noqa: E501
        """ClustersCluster - a model defined in Swagger"""  # noqa: E501
        self._server = None
        self._name = None
        self._config = None
        self._connection_state = None
        self._server_version = None
        self._namespaces = None
        self._refresh_requested_at = None
        self._info = None
        self._shard = None
        self._cluster_resources = None
        self._project = None
        self._labels = None
        self._annotations = None
        self.discriminator = None
        if server is not None:
            self.server = server
        if name is not None:
            self.name = name
        if config is not None:
            self.config = config
        if connection_state is not None:
            self.connection_state = connection_state
        if server_version is not None:
            self.server_version = server_version
        if namespaces is not None:
            self.namespaces = namespaces
        if refresh_requested_at is not None:
            self.refresh_requested_at = refresh_requested_at
        if info is not None:
            self.info = info
        if shard is not None:
            self.shard = shard
        if cluster_resources is not None:
            self.cluster_resources = cluster_resources
        if project is not None:
            self.project = project
        if labels is not None:
            self.labels = labels
        if annotations is not None:
            self.annotations = annotations

    @property
    def server(self):
        """Gets the server of this ClustersCluster.  # noqa: E501


        :return: The server of this ClustersCluster.  # noqa: E501
        :rtype: str
        """
        return self._server

    @server.setter
    def server(self, server):
        """Sets the server of this ClustersCluster.


        :param server: The server of this ClustersCluster.  # noqa: E501
        :type: str
        """

        self._server = server

    @property
    def name(self):
        """Gets the name of this ClustersCluster.  # noqa: E501


        :return: The name of this ClustersCluster.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ClustersCluster.


        :param name: The name of this ClustersCluster.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def config(self):
        """Gets the config of this ClustersCluster.  # noqa: E501


        :return: The config of this ClustersCluster.  # noqa: E501
        :rtype: ClustersClusterConfig
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this ClustersCluster.


        :param config: The config of this ClustersCluster.  # noqa: E501
        :type: ClustersClusterConfig
        """

        self._config = config

    @property
    def connection_state(self):
        """Gets the connection_state of this ClustersCluster.  # noqa: E501


        :return: The connection_state of this ClustersCluster.  # noqa: E501
        :rtype: CommonsConnectionState
        """
        return self._connection_state

    @connection_state.setter
    def connection_state(self, connection_state):
        """Sets the connection_state of this ClustersCluster.


        :param connection_state: The connection_state of this ClustersCluster.  # noqa: E501
        :type: CommonsConnectionState
        """

        self._connection_state = connection_state

    @property
    def server_version(self):
        """Gets the server_version of this ClustersCluster.  # noqa: E501


        :return: The server_version of this ClustersCluster.  # noqa: E501
        :rtype: str
        """
        return self._server_version

    @server_version.setter
    def server_version(self, server_version):
        """Sets the server_version of this ClustersCluster.


        :param server_version: The server_version of this ClustersCluster.  # noqa: E501
        :type: str
        """

        self._server_version = server_version

    @property
    def namespaces(self):
        """Gets the namespaces of this ClustersCluster.  # noqa: E501

        Holds list of namespaces which are accessible in that cluster. Cluster level resources will be ignored if namespace list is not empty.  # noqa: E501

        :return: The namespaces of this ClustersCluster.  # noqa: E501
        :rtype: list[str]
        """
        return self._namespaces

    @namespaces.setter
    def namespaces(self, namespaces):
        """Sets the namespaces of this ClustersCluster.

        Holds list of namespaces which are accessible in that cluster. Cluster level resources will be ignored if namespace list is not empty.  # noqa: E501

        :param namespaces: The namespaces of this ClustersCluster.  # noqa: E501
        :type: list[str]
        """

        self._namespaces = namespaces

    @property
    def refresh_requested_at(self):
        """Gets the refresh_requested_at of this ClustersCluster.  # noqa: E501


        :return: The refresh_requested_at of this ClustersCluster.  # noqa: E501
        :rtype: V1Time
        """
        return self._refresh_requested_at

    @refresh_requested_at.setter
    def refresh_requested_at(self, refresh_requested_at):
        """Sets the refresh_requested_at of this ClustersCluster.


        :param refresh_requested_at: The refresh_requested_at of this ClustersCluster.  # noqa: E501
        :type: V1Time
        """

        self._refresh_requested_at = refresh_requested_at

    @property
    def info(self):
        """Gets the info of this ClustersCluster.  # noqa: E501


        :return: The info of this ClustersCluster.  # noqa: E501
        :rtype: ClustersClusterInfo
        """
        return self._info

    @info.setter
    def info(self, info):
        """Sets the info of this ClustersCluster.


        :param info: The info of this ClustersCluster.  # noqa: E501
        :type: ClustersClusterInfo
        """

        self._info = info

    @property
    def shard(self):
        """Gets the shard of this ClustersCluster.  # noqa: E501

        Shard contains optional shard number. Calculated on the fly by the application controller if not specified.  # noqa: E501

        :return: The shard of this ClustersCluster.  # noqa: E501
        :rtype: str
        """
        return self._shard

    @shard.setter
    def shard(self, shard):
        """Sets the shard of this ClustersCluster.

        Shard contains optional shard number. Calculated on the fly by the application controller if not specified.  # noqa: E501

        :param shard: The shard of this ClustersCluster.  # noqa: E501
        :type: str
        """

        self._shard = shard

    @property
    def cluster_resources(self):
        """Gets the cluster_resources of this ClustersCluster.  # noqa: E501

        Indicates if cluster level resources should be managed. This setting is used only if cluster is connected in a namespaced mode.  # noqa: E501

        :return: The cluster_resources of this ClustersCluster.  # noqa: E501
        :rtype: bool
        """
        return self._cluster_resources

    @cluster_resources.setter
    def cluster_resources(self, cluster_resources):
        """Sets the cluster_resources of this ClustersCluster.

        Indicates if cluster level resources should be managed. This setting is used only if cluster is connected in a namespaced mode.  # noqa: E501

        :param cluster_resources: The cluster_resources of this ClustersCluster.  # noqa: E501
        :type: bool
        """

        self._cluster_resources = cluster_resources

    @property
    def project(self):
        """Gets the project of this ClustersCluster.  # noqa: E501


        :return: The project of this ClustersCluster.  # noqa: E501
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this ClustersCluster.


        :param project: The project of this ClustersCluster.  # noqa: E501
        :type: str
        """

        self._project = project

    @property
    def labels(self):
        """Gets the labels of this ClustersCluster.  # noqa: E501


        :return: The labels of this ClustersCluster.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this ClustersCluster.


        :param labels: The labels of this ClustersCluster.  # noqa: E501
        :type: dict(str, str)
        """

        self._labels = labels

    @property
    def annotations(self):
        """Gets the annotations of this ClustersCluster.  # noqa: E501


        :return: The annotations of this ClustersCluster.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this ClustersCluster.


        :param annotations: The annotations of this ClustersCluster.  # noqa: E501
        :type: dict(str, str)
        """

        self._annotations = annotations

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
        if issubclass(ClustersCluster, dict):
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
        if not isinstance(other, ClustersCluster):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
