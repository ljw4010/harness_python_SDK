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

class RecommendClusterRequest(object):
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
        'allow_burst': 'bool',
        'allow_older_gen': 'bool',
        'category': 'list[str]',
        'excludes': 'list[str]',
        'includes': 'list[str]',
        'max_nodes': 'int',
        'min_nodes': 'int',
        'network_perf': 'list[str]',
        'on_demand_pct': 'int',
        'same_size': 'bool',
        'sum_cpu': 'float',
        'sum_gpu': 'int',
        'sum_mem': 'float',
        'zone': 'str',
        'min_cpu': 'float',
        'min_mem': 'float'
    }

    attribute_map = {
        'allow_burst': 'allowBurst',
        'allow_older_gen': 'allowOlderGen',
        'category': 'category',
        'excludes': 'excludes',
        'includes': 'includes',
        'max_nodes': 'maxNodes',
        'min_nodes': 'minNodes',
        'network_perf': 'networkPerf',
        'on_demand_pct': 'onDemandPct',
        'same_size': 'sameSize',
        'sum_cpu': 'sumCpu',
        'sum_gpu': 'sumGpu',
        'sum_mem': 'sumMem',
        'zone': 'zone',
        'min_cpu': 'minCpu',
        'min_mem': 'minMem'
    }

    def __init__(self, allow_burst=None, allow_older_gen=None, category=None, excludes=None, includes=None, max_nodes=None, min_nodes=None, network_perf=None, on_demand_pct=None, same_size=None, sum_cpu=None, sum_gpu=None, sum_mem=None, zone=None, min_cpu=None, min_mem=None):  # noqa: E501
        """RecommendClusterRequest - a model defined in Swagger"""  # noqa: E501
        self._allow_burst = None
        self._allow_older_gen = None
        self._category = None
        self._excludes = None
        self._includes = None
        self._max_nodes = None
        self._min_nodes = None
        self._network_perf = None
        self._on_demand_pct = None
        self._same_size = None
        self._sum_cpu = None
        self._sum_gpu = None
        self._sum_mem = None
        self._zone = None
        self._min_cpu = None
        self._min_mem = None
        self.discriminator = None
        if allow_burst is not None:
            self.allow_burst = allow_burst
        if allow_older_gen is not None:
            self.allow_older_gen = allow_older_gen
        if category is not None:
            self.category = category
        if excludes is not None:
            self.excludes = excludes
        if includes is not None:
            self.includes = includes
        if max_nodes is not None:
            self.max_nodes = max_nodes
        if min_nodes is not None:
            self.min_nodes = min_nodes
        if network_perf is not None:
            self.network_perf = network_perf
        if on_demand_pct is not None:
            self.on_demand_pct = on_demand_pct
        if same_size is not None:
            self.same_size = same_size
        if sum_cpu is not None:
            self.sum_cpu = sum_cpu
        if sum_gpu is not None:
            self.sum_gpu = sum_gpu
        if sum_mem is not None:
            self.sum_mem = sum_mem
        if zone is not None:
            self.zone = zone
        if min_cpu is not None:
            self.min_cpu = min_cpu
        if min_mem is not None:
            self.min_mem = min_mem

    @property
    def allow_burst(self):
        """Gets the allow_burst of this RecommendClusterRequest.  # noqa: E501


        :return: The allow_burst of this RecommendClusterRequest.  # noqa: E501
        :rtype: bool
        """
        return self._allow_burst

    @allow_burst.setter
    def allow_burst(self, allow_burst):
        """Sets the allow_burst of this RecommendClusterRequest.


        :param allow_burst: The allow_burst of this RecommendClusterRequest.  # noqa: E501
        :type: bool
        """

        self._allow_burst = allow_burst

    @property
    def allow_older_gen(self):
        """Gets the allow_older_gen of this RecommendClusterRequest.  # noqa: E501


        :return: The allow_older_gen of this RecommendClusterRequest.  # noqa: E501
        :rtype: bool
        """
        return self._allow_older_gen

    @allow_older_gen.setter
    def allow_older_gen(self, allow_older_gen):
        """Sets the allow_older_gen of this RecommendClusterRequest.


        :param allow_older_gen: The allow_older_gen of this RecommendClusterRequest.  # noqa: E501
        :type: bool
        """

        self._allow_older_gen = allow_older_gen

    @property
    def category(self):
        """Gets the category of this RecommendClusterRequest.  # noqa: E501


        :return: The category of this RecommendClusterRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this RecommendClusterRequest.


        :param category: The category of this RecommendClusterRequest.  # noqa: E501
        :type: list[str]
        """

        self._category = category

    @property
    def excludes(self):
        """Gets the excludes of this RecommendClusterRequest.  # noqa: E501


        :return: The excludes of this RecommendClusterRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._excludes

    @excludes.setter
    def excludes(self, excludes):
        """Sets the excludes of this RecommendClusterRequest.


        :param excludes: The excludes of this RecommendClusterRequest.  # noqa: E501
        :type: list[str]
        """

        self._excludes = excludes

    @property
    def includes(self):
        """Gets the includes of this RecommendClusterRequest.  # noqa: E501


        :return: The includes of this RecommendClusterRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._includes

    @includes.setter
    def includes(self, includes):
        """Sets the includes of this RecommendClusterRequest.


        :param includes: The includes of this RecommendClusterRequest.  # noqa: E501
        :type: list[str]
        """

        self._includes = includes

    @property
    def max_nodes(self):
        """Gets the max_nodes of this RecommendClusterRequest.  # noqa: E501


        :return: The max_nodes of this RecommendClusterRequest.  # noqa: E501
        :rtype: int
        """
        return self._max_nodes

    @max_nodes.setter
    def max_nodes(self, max_nodes):
        """Sets the max_nodes of this RecommendClusterRequest.


        :param max_nodes: The max_nodes of this RecommendClusterRequest.  # noqa: E501
        :type: int
        """

        self._max_nodes = max_nodes

    @property
    def min_nodes(self):
        """Gets the min_nodes of this RecommendClusterRequest.  # noqa: E501


        :return: The min_nodes of this RecommendClusterRequest.  # noqa: E501
        :rtype: int
        """
        return self._min_nodes

    @min_nodes.setter
    def min_nodes(self, min_nodes):
        """Sets the min_nodes of this RecommendClusterRequest.


        :param min_nodes: The min_nodes of this RecommendClusterRequest.  # noqa: E501
        :type: int
        """

        self._min_nodes = min_nodes

    @property
    def network_perf(self):
        """Gets the network_perf of this RecommendClusterRequest.  # noqa: E501


        :return: The network_perf of this RecommendClusterRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._network_perf

    @network_perf.setter
    def network_perf(self, network_perf):
        """Sets the network_perf of this RecommendClusterRequest.


        :param network_perf: The network_perf of this RecommendClusterRequest.  # noqa: E501
        :type: list[str]
        """

        self._network_perf = network_perf

    @property
    def on_demand_pct(self):
        """Gets the on_demand_pct of this RecommendClusterRequest.  # noqa: E501


        :return: The on_demand_pct of this RecommendClusterRequest.  # noqa: E501
        :rtype: int
        """
        return self._on_demand_pct

    @on_demand_pct.setter
    def on_demand_pct(self, on_demand_pct):
        """Sets the on_demand_pct of this RecommendClusterRequest.


        :param on_demand_pct: The on_demand_pct of this RecommendClusterRequest.  # noqa: E501
        :type: int
        """

        self._on_demand_pct = on_demand_pct

    @property
    def same_size(self):
        """Gets the same_size of this RecommendClusterRequest.  # noqa: E501


        :return: The same_size of this RecommendClusterRequest.  # noqa: E501
        :rtype: bool
        """
        return self._same_size

    @same_size.setter
    def same_size(self, same_size):
        """Sets the same_size of this RecommendClusterRequest.


        :param same_size: The same_size of this RecommendClusterRequest.  # noqa: E501
        :type: bool
        """

        self._same_size = same_size

    @property
    def sum_cpu(self):
        """Gets the sum_cpu of this RecommendClusterRequest.  # noqa: E501


        :return: The sum_cpu of this RecommendClusterRequest.  # noqa: E501
        :rtype: float
        """
        return self._sum_cpu

    @sum_cpu.setter
    def sum_cpu(self, sum_cpu):
        """Sets the sum_cpu of this RecommendClusterRequest.


        :param sum_cpu: The sum_cpu of this RecommendClusterRequest.  # noqa: E501
        :type: float
        """

        self._sum_cpu = sum_cpu

    @property
    def sum_gpu(self):
        """Gets the sum_gpu of this RecommendClusterRequest.  # noqa: E501


        :return: The sum_gpu of this RecommendClusterRequest.  # noqa: E501
        :rtype: int
        """
        return self._sum_gpu

    @sum_gpu.setter
    def sum_gpu(self, sum_gpu):
        """Sets the sum_gpu of this RecommendClusterRequest.


        :param sum_gpu: The sum_gpu of this RecommendClusterRequest.  # noqa: E501
        :type: int
        """

        self._sum_gpu = sum_gpu

    @property
    def sum_mem(self):
        """Gets the sum_mem of this RecommendClusterRequest.  # noqa: E501


        :return: The sum_mem of this RecommendClusterRequest.  # noqa: E501
        :rtype: float
        """
        return self._sum_mem

    @sum_mem.setter
    def sum_mem(self, sum_mem):
        """Sets the sum_mem of this RecommendClusterRequest.


        :param sum_mem: The sum_mem of this RecommendClusterRequest.  # noqa: E501
        :type: float
        """

        self._sum_mem = sum_mem

    @property
    def zone(self):
        """Gets the zone of this RecommendClusterRequest.  # noqa: E501


        :return: The zone of this RecommendClusterRequest.  # noqa: E501
        :rtype: str
        """
        return self._zone

    @zone.setter
    def zone(self, zone):
        """Sets the zone of this RecommendClusterRequest.


        :param zone: The zone of this RecommendClusterRequest.  # noqa: E501
        :type: str
        """

        self._zone = zone

    @property
    def min_cpu(self):
        """Gets the min_cpu of this RecommendClusterRequest.  # noqa: E501


        :return: The min_cpu of this RecommendClusterRequest.  # noqa: E501
        :rtype: float
        """
        return self._min_cpu

    @min_cpu.setter
    def min_cpu(self, min_cpu):
        """Sets the min_cpu of this RecommendClusterRequest.


        :param min_cpu: The min_cpu of this RecommendClusterRequest.  # noqa: E501
        :type: float
        """

        self._min_cpu = min_cpu

    @property
    def min_mem(self):
        """Gets the min_mem of this RecommendClusterRequest.  # noqa: E501


        :return: The min_mem of this RecommendClusterRequest.  # noqa: E501
        :rtype: float
        """
        return self._min_mem

    @min_mem.setter
    def min_mem(self, min_mem):
        """Sets the min_mem of this RecommendClusterRequest.


        :param min_mem: The min_mem of this RecommendClusterRequest.  # noqa: E501
        :type: float
        """

        self._min_mem = min_mem

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
        if issubclass(RecommendClusterRequest, dict):
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
        if not isinstance(other, RecommendClusterRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
