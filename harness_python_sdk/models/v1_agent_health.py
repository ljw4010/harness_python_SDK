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

class V1AgentHealth(object):
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
        'last_heartbeat': 'datetime',
        'argo_repo_server': 'V1AgentComponentHealth',
        'argo_app_controller': 'V1AgentComponentHealth',
        'argo_redis_server': 'V1AgentComponentHealth',
        'harness_gitops_agent': 'V1AgentComponentHealth',
        'connection_status': 'V1ConnectedStatus'
    }

    attribute_map = {
        'last_heartbeat': 'lastHeartbeat',
        'argo_repo_server': 'argoRepoServer',
        'argo_app_controller': 'argoAppController',
        'argo_redis_server': 'argoRedisServer',
        'harness_gitops_agent': 'harnessGitopsAgent',
        'connection_status': 'connectionStatus'
    }

    def __init__(self, last_heartbeat=None, argo_repo_server=None, argo_app_controller=None, argo_redis_server=None, harness_gitops_agent=None, connection_status=None):  # noqa: E501
        """V1AgentHealth - a model defined in Swagger"""  # noqa: E501
        self._last_heartbeat = None
        self._argo_repo_server = None
        self._argo_app_controller = None
        self._argo_redis_server = None
        self._harness_gitops_agent = None
        self._connection_status = None
        self.discriminator = None
        if last_heartbeat is not None:
            self.last_heartbeat = last_heartbeat
        if argo_repo_server is not None:
            self.argo_repo_server = argo_repo_server
        if argo_app_controller is not None:
            self.argo_app_controller = argo_app_controller
        if argo_redis_server is not None:
            self.argo_redis_server = argo_redis_server
        if harness_gitops_agent is not None:
            self.harness_gitops_agent = harness_gitops_agent
        if connection_status is not None:
            self.connection_status = connection_status

    @property
    def last_heartbeat(self):
        """Gets the last_heartbeat of this V1AgentHealth.  # noqa: E501


        :return: The last_heartbeat of this V1AgentHealth.  # noqa: E501
        :rtype: datetime
        """
        return self._last_heartbeat

    @last_heartbeat.setter
    def last_heartbeat(self, last_heartbeat):
        """Sets the last_heartbeat of this V1AgentHealth.


        :param last_heartbeat: The last_heartbeat of this V1AgentHealth.  # noqa: E501
        :type: datetime
        """

        self._last_heartbeat = last_heartbeat

    @property
    def argo_repo_server(self):
        """Gets the argo_repo_server of this V1AgentHealth.  # noqa: E501


        :return: The argo_repo_server of this V1AgentHealth.  # noqa: E501
        :rtype: V1AgentComponentHealth
        """
        return self._argo_repo_server

    @argo_repo_server.setter
    def argo_repo_server(self, argo_repo_server):
        """Sets the argo_repo_server of this V1AgentHealth.


        :param argo_repo_server: The argo_repo_server of this V1AgentHealth.  # noqa: E501
        :type: V1AgentComponentHealth
        """

        self._argo_repo_server = argo_repo_server

    @property
    def argo_app_controller(self):
        """Gets the argo_app_controller of this V1AgentHealth.  # noqa: E501


        :return: The argo_app_controller of this V1AgentHealth.  # noqa: E501
        :rtype: V1AgentComponentHealth
        """
        return self._argo_app_controller

    @argo_app_controller.setter
    def argo_app_controller(self, argo_app_controller):
        """Sets the argo_app_controller of this V1AgentHealth.


        :param argo_app_controller: The argo_app_controller of this V1AgentHealth.  # noqa: E501
        :type: V1AgentComponentHealth
        """

        self._argo_app_controller = argo_app_controller

    @property
    def argo_redis_server(self):
        """Gets the argo_redis_server of this V1AgentHealth.  # noqa: E501


        :return: The argo_redis_server of this V1AgentHealth.  # noqa: E501
        :rtype: V1AgentComponentHealth
        """
        return self._argo_redis_server

    @argo_redis_server.setter
    def argo_redis_server(self, argo_redis_server):
        """Sets the argo_redis_server of this V1AgentHealth.


        :param argo_redis_server: The argo_redis_server of this V1AgentHealth.  # noqa: E501
        :type: V1AgentComponentHealth
        """

        self._argo_redis_server = argo_redis_server

    @property
    def harness_gitops_agent(self):
        """Gets the harness_gitops_agent of this V1AgentHealth.  # noqa: E501


        :return: The harness_gitops_agent of this V1AgentHealth.  # noqa: E501
        :rtype: V1AgentComponentHealth
        """
        return self._harness_gitops_agent

    @harness_gitops_agent.setter
    def harness_gitops_agent(self, harness_gitops_agent):
        """Sets the harness_gitops_agent of this V1AgentHealth.


        :param harness_gitops_agent: The harness_gitops_agent of this V1AgentHealth.  # noqa: E501
        :type: V1AgentComponentHealth
        """

        self._harness_gitops_agent = harness_gitops_agent

    @property
    def connection_status(self):
        """Gets the connection_status of this V1AgentHealth.  # noqa: E501


        :return: The connection_status of this V1AgentHealth.  # noqa: E501
        :rtype: V1ConnectedStatus
        """
        return self._connection_status

    @connection_status.setter
    def connection_status(self, connection_status):
        """Sets the connection_status of this V1AgentHealth.


        :param connection_status: The connection_status of this V1AgentHealth.  # noqa: E501
        :type: V1ConnectedStatus
        """

        self._connection_status = connection_status

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
        if issubclass(V1AgentHealth, dict):
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
        if not isinstance(other, V1AgentHealth):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
