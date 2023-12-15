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

class ECSRecommendationDTO(object):
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
        'id': 'str',
        'cluster_name': 'str',
        'service_arn': 'str',
        'service_name': 'str',
        'launch_type': 'str',
        'current': 'dict(str, str)',
        'percentile_based': 'dict(str, dict(str, str))',
        'last_day_cost': 'Cost',
        'cpu_histogram': 'HistogramExp',
        'memory_histogram': 'HistogramExp',
        'jira_details': 'CCMJiraDetails',
        'service_now_details': 'CCMServiceNowDetails'
    }

    attribute_map = {
        'id': 'id',
        'cluster_name': 'clusterName',
        'service_arn': 'serviceArn',
        'service_name': 'serviceName',
        'launch_type': 'launchType',
        'current': 'current',
        'percentile_based': 'percentileBased',
        'last_day_cost': 'lastDayCost',
        'cpu_histogram': 'cpuHistogram',
        'memory_histogram': 'memoryHistogram',
        'jira_details': 'jiraDetails',
        'service_now_details': 'serviceNowDetails'
    }

    def __init__(self, id=None, cluster_name=None, service_arn=None, service_name=None, launch_type=None, current=None, percentile_based=None, last_day_cost=None, cpu_histogram=None, memory_histogram=None, jira_details=None, service_now_details=None):  # noqa: E501
        """ECSRecommendationDTO - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._cluster_name = None
        self._service_arn = None
        self._service_name = None
        self._launch_type = None
        self._current = None
        self._percentile_based = None
        self._last_day_cost = None
        self._cpu_histogram = None
        self._memory_histogram = None
        self._jira_details = None
        self._service_now_details = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if service_arn is not None:
            self.service_arn = service_arn
        if service_name is not None:
            self.service_name = service_name
        if launch_type is not None:
            self.launch_type = launch_type
        if current is not None:
            self.current = current
        if percentile_based is not None:
            self.percentile_based = percentile_based
        if last_day_cost is not None:
            self.last_day_cost = last_day_cost
        if cpu_histogram is not None:
            self.cpu_histogram = cpu_histogram
        if memory_histogram is not None:
            self.memory_histogram = memory_histogram
        if jira_details is not None:
            self.jira_details = jira_details
        if service_now_details is not None:
            self.service_now_details = service_now_details

    @property
    def id(self):
        """Gets the id of this ECSRecommendationDTO.  # noqa: E501


        :return: The id of this ECSRecommendationDTO.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ECSRecommendationDTO.


        :param id: The id of this ECSRecommendationDTO.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def cluster_name(self):
        """Gets the cluster_name of this ECSRecommendationDTO.  # noqa: E501


        :return: The cluster_name of this ECSRecommendationDTO.  # noqa: E501
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        """Sets the cluster_name of this ECSRecommendationDTO.


        :param cluster_name: The cluster_name of this ECSRecommendationDTO.  # noqa: E501
        :type: str
        """

        self._cluster_name = cluster_name

    @property
    def service_arn(self):
        """Gets the service_arn of this ECSRecommendationDTO.  # noqa: E501


        :return: The service_arn of this ECSRecommendationDTO.  # noqa: E501
        :rtype: str
        """
        return self._service_arn

    @service_arn.setter
    def service_arn(self, service_arn):
        """Sets the service_arn of this ECSRecommendationDTO.


        :param service_arn: The service_arn of this ECSRecommendationDTO.  # noqa: E501
        :type: str
        """

        self._service_arn = service_arn

    @property
    def service_name(self):
        """Gets the service_name of this ECSRecommendationDTO.  # noqa: E501


        :return: The service_name of this ECSRecommendationDTO.  # noqa: E501
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """Sets the service_name of this ECSRecommendationDTO.


        :param service_name: The service_name of this ECSRecommendationDTO.  # noqa: E501
        :type: str
        """

        self._service_name = service_name

    @property
    def launch_type(self):
        """Gets the launch_type of this ECSRecommendationDTO.  # noqa: E501


        :return: The launch_type of this ECSRecommendationDTO.  # noqa: E501
        :rtype: str
        """
        return self._launch_type

    @launch_type.setter
    def launch_type(self, launch_type):
        """Sets the launch_type of this ECSRecommendationDTO.


        :param launch_type: The launch_type of this ECSRecommendationDTO.  # noqa: E501
        :type: str
        """
        allowed_values = ["EC2", "FARGATE", "EXTERNAL"]  # noqa: E501
        if launch_type not in allowed_values:
            raise ValueError(
                "Invalid value for `launch_type` ({0}), must be one of {1}"  # noqa: E501
                .format(launch_type, allowed_values)
            )

        self._launch_type = launch_type

    @property
    def current(self):
        """Gets the current of this ECSRecommendationDTO.  # noqa: E501


        :return: The current of this ECSRecommendationDTO.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._current

    @current.setter
    def current(self, current):
        """Sets the current of this ECSRecommendationDTO.


        :param current: The current of this ECSRecommendationDTO.  # noqa: E501
        :type: dict(str, str)
        """

        self._current = current

    @property
    def percentile_based(self):
        """Gets the percentile_based of this ECSRecommendationDTO.  # noqa: E501


        :return: The percentile_based of this ECSRecommendationDTO.  # noqa: E501
        :rtype: dict(str, dict(str, str))
        """
        return self._percentile_based

    @percentile_based.setter
    def percentile_based(self, percentile_based):
        """Sets the percentile_based of this ECSRecommendationDTO.


        :param percentile_based: The percentile_based of this ECSRecommendationDTO.  # noqa: E501
        :type: dict(str, dict(str, str))
        """

        self._percentile_based = percentile_based

    @property
    def last_day_cost(self):
        """Gets the last_day_cost of this ECSRecommendationDTO.  # noqa: E501


        :return: The last_day_cost of this ECSRecommendationDTO.  # noqa: E501
        :rtype: Cost
        """
        return self._last_day_cost

    @last_day_cost.setter
    def last_day_cost(self, last_day_cost):
        """Sets the last_day_cost of this ECSRecommendationDTO.


        :param last_day_cost: The last_day_cost of this ECSRecommendationDTO.  # noqa: E501
        :type: Cost
        """

        self._last_day_cost = last_day_cost

    @property
    def cpu_histogram(self):
        """Gets the cpu_histogram of this ECSRecommendationDTO.  # noqa: E501


        :return: The cpu_histogram of this ECSRecommendationDTO.  # noqa: E501
        :rtype: HistogramExp
        """
        return self._cpu_histogram

    @cpu_histogram.setter
    def cpu_histogram(self, cpu_histogram):
        """Sets the cpu_histogram of this ECSRecommendationDTO.


        :param cpu_histogram: The cpu_histogram of this ECSRecommendationDTO.  # noqa: E501
        :type: HistogramExp
        """

        self._cpu_histogram = cpu_histogram

    @property
    def memory_histogram(self):
        """Gets the memory_histogram of this ECSRecommendationDTO.  # noqa: E501


        :return: The memory_histogram of this ECSRecommendationDTO.  # noqa: E501
        :rtype: HistogramExp
        """
        return self._memory_histogram

    @memory_histogram.setter
    def memory_histogram(self, memory_histogram):
        """Sets the memory_histogram of this ECSRecommendationDTO.


        :param memory_histogram: The memory_histogram of this ECSRecommendationDTO.  # noqa: E501
        :type: HistogramExp
        """

        self._memory_histogram = memory_histogram

    @property
    def jira_details(self):
        """Gets the jira_details of this ECSRecommendationDTO.  # noqa: E501


        :return: The jira_details of this ECSRecommendationDTO.  # noqa: E501
        :rtype: CCMJiraDetails
        """
        return self._jira_details

    @jira_details.setter
    def jira_details(self, jira_details):
        """Sets the jira_details of this ECSRecommendationDTO.


        :param jira_details: The jira_details of this ECSRecommendationDTO.  # noqa: E501
        :type: CCMJiraDetails
        """

        self._jira_details = jira_details

    @property
    def service_now_details(self):
        """Gets the service_now_details of this ECSRecommendationDTO.  # noqa: E501


        :return: The service_now_details of this ECSRecommendationDTO.  # noqa: E501
        :rtype: CCMServiceNowDetails
        """
        return self._service_now_details

    @service_now_details.setter
    def service_now_details(self, service_now_details):
        """Sets the service_now_details of this ECSRecommendationDTO.


        :param service_now_details: The service_now_details of this ECSRecommendationDTO.  # noqa: E501
        :type: CCMServiceNowDetails
        """

        self._service_now_details = service_now_details

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
        if issubclass(ECSRecommendationDTO, dict):
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
        if not isinstance(other, ECSRecommendationDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
