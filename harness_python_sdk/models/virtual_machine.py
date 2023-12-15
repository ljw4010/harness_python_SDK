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

class VirtualMachine(object):
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
        'avg_price': 'float',
        'burst': 'bool',
        'category': 'str',
        'cpus_per_vm': 'float',
        'current_gen': 'bool',
        'gpus_per_vm': 'float',
        'mem_per_vm': 'float',
        'allocatable_cpus_per_vm': 'float',
        'allocatable_mem_per_vm': 'float',
        'network_perf': 'str',
        'network_perf_category': 'str',
        'on_demand_price': 'float',
        'type': 'str',
        'zones': 'list[str]'
    }

    attribute_map = {
        'avg_price': 'avgPrice',
        'burst': 'burst',
        'category': 'category',
        'cpus_per_vm': 'cpusPerVm',
        'current_gen': 'currentGen',
        'gpus_per_vm': 'gpusPerVm',
        'mem_per_vm': 'memPerVm',
        'allocatable_cpus_per_vm': 'allocatableCpusPerVm',
        'allocatable_mem_per_vm': 'allocatableMemPerVm',
        'network_perf': 'networkPerf',
        'network_perf_category': 'networkPerfCategory',
        'on_demand_price': 'onDemandPrice',
        'type': 'type',
        'zones': 'zones'
    }

    def __init__(self, avg_price=None, burst=None, category=None, cpus_per_vm=None, current_gen=None, gpus_per_vm=None, mem_per_vm=None, allocatable_cpus_per_vm=None, allocatable_mem_per_vm=None, network_perf=None, network_perf_category=None, on_demand_price=None, type=None, zones=None):  # noqa: E501
        """VirtualMachine - a model defined in Swagger"""  # noqa: E501
        self._avg_price = None
        self._burst = None
        self._category = None
        self._cpus_per_vm = None
        self._current_gen = None
        self._gpus_per_vm = None
        self._mem_per_vm = None
        self._allocatable_cpus_per_vm = None
        self._allocatable_mem_per_vm = None
        self._network_perf = None
        self._network_perf_category = None
        self._on_demand_price = None
        self._type = None
        self._zones = None
        self.discriminator = None
        if avg_price is not None:
            self.avg_price = avg_price
        if burst is not None:
            self.burst = burst
        if category is not None:
            self.category = category
        if cpus_per_vm is not None:
            self.cpus_per_vm = cpus_per_vm
        if current_gen is not None:
            self.current_gen = current_gen
        if gpus_per_vm is not None:
            self.gpus_per_vm = gpus_per_vm
        if mem_per_vm is not None:
            self.mem_per_vm = mem_per_vm
        if allocatable_cpus_per_vm is not None:
            self.allocatable_cpus_per_vm = allocatable_cpus_per_vm
        if allocatable_mem_per_vm is not None:
            self.allocatable_mem_per_vm = allocatable_mem_per_vm
        if network_perf is not None:
            self.network_perf = network_perf
        if network_perf_category is not None:
            self.network_perf_category = network_perf_category
        if on_demand_price is not None:
            self.on_demand_price = on_demand_price
        if type is not None:
            self.type = type
        if zones is not None:
            self.zones = zones

    @property
    def avg_price(self):
        """Gets the avg_price of this VirtualMachine.  # noqa: E501


        :return: The avg_price of this VirtualMachine.  # noqa: E501
        :rtype: float
        """
        return self._avg_price

    @avg_price.setter
    def avg_price(self, avg_price):
        """Sets the avg_price of this VirtualMachine.


        :param avg_price: The avg_price of this VirtualMachine.  # noqa: E501
        :type: float
        """

        self._avg_price = avg_price

    @property
    def burst(self):
        """Gets the burst of this VirtualMachine.  # noqa: E501


        :return: The burst of this VirtualMachine.  # noqa: E501
        :rtype: bool
        """
        return self._burst

    @burst.setter
    def burst(self, burst):
        """Sets the burst of this VirtualMachine.


        :param burst: The burst of this VirtualMachine.  # noqa: E501
        :type: bool
        """

        self._burst = burst

    @property
    def category(self):
        """Gets the category of this VirtualMachine.  # noqa: E501


        :return: The category of this VirtualMachine.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this VirtualMachine.


        :param category: The category of this VirtualMachine.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def cpus_per_vm(self):
        """Gets the cpus_per_vm of this VirtualMachine.  # noqa: E501


        :return: The cpus_per_vm of this VirtualMachine.  # noqa: E501
        :rtype: float
        """
        return self._cpus_per_vm

    @cpus_per_vm.setter
    def cpus_per_vm(self, cpus_per_vm):
        """Sets the cpus_per_vm of this VirtualMachine.


        :param cpus_per_vm: The cpus_per_vm of this VirtualMachine.  # noqa: E501
        :type: float
        """

        self._cpus_per_vm = cpus_per_vm

    @property
    def current_gen(self):
        """Gets the current_gen of this VirtualMachine.  # noqa: E501


        :return: The current_gen of this VirtualMachine.  # noqa: E501
        :rtype: bool
        """
        return self._current_gen

    @current_gen.setter
    def current_gen(self, current_gen):
        """Sets the current_gen of this VirtualMachine.


        :param current_gen: The current_gen of this VirtualMachine.  # noqa: E501
        :type: bool
        """

        self._current_gen = current_gen

    @property
    def gpus_per_vm(self):
        """Gets the gpus_per_vm of this VirtualMachine.  # noqa: E501


        :return: The gpus_per_vm of this VirtualMachine.  # noqa: E501
        :rtype: float
        """
        return self._gpus_per_vm

    @gpus_per_vm.setter
    def gpus_per_vm(self, gpus_per_vm):
        """Sets the gpus_per_vm of this VirtualMachine.


        :param gpus_per_vm: The gpus_per_vm of this VirtualMachine.  # noqa: E501
        :type: float
        """

        self._gpus_per_vm = gpus_per_vm

    @property
    def mem_per_vm(self):
        """Gets the mem_per_vm of this VirtualMachine.  # noqa: E501


        :return: The mem_per_vm of this VirtualMachine.  # noqa: E501
        :rtype: float
        """
        return self._mem_per_vm

    @mem_per_vm.setter
    def mem_per_vm(self, mem_per_vm):
        """Sets the mem_per_vm of this VirtualMachine.


        :param mem_per_vm: The mem_per_vm of this VirtualMachine.  # noqa: E501
        :type: float
        """

        self._mem_per_vm = mem_per_vm

    @property
    def allocatable_cpus_per_vm(self):
        """Gets the allocatable_cpus_per_vm of this VirtualMachine.  # noqa: E501


        :return: The allocatable_cpus_per_vm of this VirtualMachine.  # noqa: E501
        :rtype: float
        """
        return self._allocatable_cpus_per_vm

    @allocatable_cpus_per_vm.setter
    def allocatable_cpus_per_vm(self, allocatable_cpus_per_vm):
        """Sets the allocatable_cpus_per_vm of this VirtualMachine.


        :param allocatable_cpus_per_vm: The allocatable_cpus_per_vm of this VirtualMachine.  # noqa: E501
        :type: float
        """

        self._allocatable_cpus_per_vm = allocatable_cpus_per_vm

    @property
    def allocatable_mem_per_vm(self):
        """Gets the allocatable_mem_per_vm of this VirtualMachine.  # noqa: E501


        :return: The allocatable_mem_per_vm of this VirtualMachine.  # noqa: E501
        :rtype: float
        """
        return self._allocatable_mem_per_vm

    @allocatable_mem_per_vm.setter
    def allocatable_mem_per_vm(self, allocatable_mem_per_vm):
        """Sets the allocatable_mem_per_vm of this VirtualMachine.


        :param allocatable_mem_per_vm: The allocatable_mem_per_vm of this VirtualMachine.  # noqa: E501
        :type: float
        """

        self._allocatable_mem_per_vm = allocatable_mem_per_vm

    @property
    def network_perf(self):
        """Gets the network_perf of this VirtualMachine.  # noqa: E501


        :return: The network_perf of this VirtualMachine.  # noqa: E501
        :rtype: str
        """
        return self._network_perf

    @network_perf.setter
    def network_perf(self, network_perf):
        """Sets the network_perf of this VirtualMachine.


        :param network_perf: The network_perf of this VirtualMachine.  # noqa: E501
        :type: str
        """

        self._network_perf = network_perf

    @property
    def network_perf_category(self):
        """Gets the network_perf_category of this VirtualMachine.  # noqa: E501


        :return: The network_perf_category of this VirtualMachine.  # noqa: E501
        :rtype: str
        """
        return self._network_perf_category

    @network_perf_category.setter
    def network_perf_category(self, network_perf_category):
        """Sets the network_perf_category of this VirtualMachine.


        :param network_perf_category: The network_perf_category of this VirtualMachine.  # noqa: E501
        :type: str
        """

        self._network_perf_category = network_perf_category

    @property
    def on_demand_price(self):
        """Gets the on_demand_price of this VirtualMachine.  # noqa: E501


        :return: The on_demand_price of this VirtualMachine.  # noqa: E501
        :rtype: float
        """
        return self._on_demand_price

    @on_demand_price.setter
    def on_demand_price(self, on_demand_price):
        """Sets the on_demand_price of this VirtualMachine.


        :param on_demand_price: The on_demand_price of this VirtualMachine.  # noqa: E501
        :type: float
        """

        self._on_demand_price = on_demand_price

    @property
    def type(self):
        """Gets the type of this VirtualMachine.  # noqa: E501


        :return: The type of this VirtualMachine.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this VirtualMachine.


        :param type: The type of this VirtualMachine.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def zones(self):
        """Gets the zones of this VirtualMachine.  # noqa: E501


        :return: The zones of this VirtualMachine.  # noqa: E501
        :rtype: list[str]
        """
        return self._zones

    @zones.setter
    def zones(self, zones):
        """Sets the zones of this VirtualMachine.


        :param zones: The zones of this VirtualMachine.  # noqa: E501
        :type: list[str]
        """

        self._zones = zones

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
        if issubclass(VirtualMachine, dict):
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
        if not isinstance(other, VirtualMachine):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
