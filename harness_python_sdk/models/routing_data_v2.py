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

class RoutingDataV2(object):
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
        'instance': 'InstanceBasedRoutingDataV2',
        'lb': 'str',
        'k8s': 'RoutingDataK8s',
        'custom_domain_providers': 'object',
        'container_svc': 'ContainerSvc',
        'database': 'RDSDatabase',
        'http': 'HTTPProxy',
        'tcp': 'TCPProxy'
    }

    attribute_map = {
        'instance': 'instance',
        'lb': 'lb',
        'k8s': 'k8s',
        'custom_domain_providers': 'custom_domain_providers',
        'container_svc': 'container_svc',
        'database': 'database',
        'http': 'http',
        'tcp': 'tcp'
    }

    def __init__(self, instance=None, lb=None, k8s=None, custom_domain_providers=None, container_svc=None, database=None, http=None, tcp=None):  # noqa: E501
        """RoutingDataV2 - a model defined in Swagger"""  # noqa: E501
        self._instance = None
        self._lb = None
        self._k8s = None
        self._custom_domain_providers = None
        self._container_svc = None
        self._database = None
        self._http = None
        self._tcp = None
        self.discriminator = None
        if instance is not None:
            self.instance = instance
        if lb is not None:
            self.lb = lb
        if k8s is not None:
            self.k8s = k8s
        if custom_domain_providers is not None:
            self.custom_domain_providers = custom_domain_providers
        if container_svc is not None:
            self.container_svc = container_svc
        if database is not None:
            self.database = database
        if http is not None:
            self.http = http
        if tcp is not None:
            self.tcp = tcp

    @property
    def instance(self):
        """Gets the instance of this RoutingDataV2.  # noqa: E501


        :return: The instance of this RoutingDataV2.  # noqa: E501
        :rtype: InstanceBasedRoutingDataV2
        """
        return self._instance

    @instance.setter
    def instance(self, instance):
        """Sets the instance of this RoutingDataV2.


        :param instance: The instance of this RoutingDataV2.  # noqa: E501
        :type: InstanceBasedRoutingDataV2
        """

        self._instance = instance

    @property
    def lb(self):
        """Gets the lb of this RoutingDataV2.  # noqa: E501


        :return: The lb of this RoutingDataV2.  # noqa: E501
        :rtype: str
        """
        return self._lb

    @lb.setter
    def lb(self, lb):
        """Sets the lb of this RoutingDataV2.


        :param lb: The lb of this RoutingDataV2.  # noqa: E501
        :type: str
        """

        self._lb = lb

    @property
    def k8s(self):
        """Gets the k8s of this RoutingDataV2.  # noqa: E501


        :return: The k8s of this RoutingDataV2.  # noqa: E501
        :rtype: RoutingDataK8s
        """
        return self._k8s

    @k8s.setter
    def k8s(self, k8s):
        """Sets the k8s of this RoutingDataV2.


        :param k8s: The k8s of this RoutingDataV2.  # noqa: E501
        :type: RoutingDataK8s
        """

        self._k8s = k8s

    @property
    def custom_domain_providers(self):
        """Gets the custom_domain_providers of this RoutingDataV2.  # noqa: E501


        :return: The custom_domain_providers of this RoutingDataV2.  # noqa: E501
        :rtype: object
        """
        return self._custom_domain_providers

    @custom_domain_providers.setter
    def custom_domain_providers(self, custom_domain_providers):
        """Sets the custom_domain_providers of this RoutingDataV2.


        :param custom_domain_providers: The custom_domain_providers of this RoutingDataV2.  # noqa: E501
        :type: object
        """

        self._custom_domain_providers = custom_domain_providers

    @property
    def container_svc(self):
        """Gets the container_svc of this RoutingDataV2.  # noqa: E501


        :return: The container_svc of this RoutingDataV2.  # noqa: E501
        :rtype: ContainerSvc
        """
        return self._container_svc

    @container_svc.setter
    def container_svc(self, container_svc):
        """Sets the container_svc of this RoutingDataV2.


        :param container_svc: The container_svc of this RoutingDataV2.  # noqa: E501
        :type: ContainerSvc
        """

        self._container_svc = container_svc

    @property
    def database(self):
        """Gets the database of this RoutingDataV2.  # noqa: E501


        :return: The database of this RoutingDataV2.  # noqa: E501
        :rtype: RDSDatabase
        """
        return self._database

    @database.setter
    def database(self, database):
        """Sets the database of this RoutingDataV2.


        :param database: The database of this RoutingDataV2.  # noqa: E501
        :type: RDSDatabase
        """

        self._database = database

    @property
    def http(self):
        """Gets the http of this RoutingDataV2.  # noqa: E501


        :return: The http of this RoutingDataV2.  # noqa: E501
        :rtype: HTTPProxy
        """
        return self._http

    @http.setter
    def http(self, http):
        """Sets the http of this RoutingDataV2.


        :param http: The http of this RoutingDataV2.  # noqa: E501
        :type: HTTPProxy
        """

        self._http = http

    @property
    def tcp(self):
        """Gets the tcp of this RoutingDataV2.  # noqa: E501


        :return: The tcp of this RoutingDataV2.  # noqa: E501
        :rtype: TCPProxy
        """
        return self._tcp

    @tcp.setter
    def tcp(self, tcp):
        """Sets the tcp of this RoutingDataV2.


        :param tcp: The tcp of this RoutingDataV2.  # noqa: E501
        :type: TCPProxy
        """

        self._tcp = tcp

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
        if issubclass(RoutingDataV2, dict):
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
        if not isinstance(other, RoutingDataV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
