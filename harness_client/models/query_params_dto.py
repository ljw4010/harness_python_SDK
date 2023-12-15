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

class QueryParamsDTO(object):
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
        'service_instance_field': 'str',
        'index': 'str',
        'time_stamp_identifier': 'str',
        'time_stamp_format': 'str',
        'message_identifier': 'str',
        'health_source_metric_name': 'str',
        'health_source_metric_namespace': 'str',
        'aggregation_type': 'str',
        'indexes': 'list[str]'
    }

    attribute_map = {
        'service_instance_field': 'serviceInstanceField',
        'index': 'index',
        'time_stamp_identifier': 'timeStampIdentifier',
        'time_stamp_format': 'timeStampFormat',
        'message_identifier': 'messageIdentifier',
        'health_source_metric_name': 'healthSourceMetricName',
        'health_source_metric_namespace': 'healthSourceMetricNamespace',
        'aggregation_type': 'aggregationType',
        'indexes': 'indexes'
    }

    def __init__(self, service_instance_field=None, index=None, time_stamp_identifier=None, time_stamp_format=None, message_identifier=None, health_source_metric_name=None, health_source_metric_namespace=None, aggregation_type=None, indexes=None):  # noqa: E501
        """QueryParamsDTO - a model defined in Swagger"""  # noqa: E501
        self._service_instance_field = None
        self._index = None
        self._time_stamp_identifier = None
        self._time_stamp_format = None
        self._message_identifier = None
        self._health_source_metric_name = None
        self._health_source_metric_namespace = None
        self._aggregation_type = None
        self._indexes = None
        self.discriminator = None
        if service_instance_field is not None:
            self.service_instance_field = service_instance_field
        if index is not None:
            self.index = index
        if time_stamp_identifier is not None:
            self.time_stamp_identifier = time_stamp_identifier
        if time_stamp_format is not None:
            self.time_stamp_format = time_stamp_format
        if message_identifier is not None:
            self.message_identifier = message_identifier
        if health_source_metric_name is not None:
            self.health_source_metric_name = health_source_metric_name
        if health_source_metric_namespace is not None:
            self.health_source_metric_namespace = health_source_metric_namespace
        if aggregation_type is not None:
            self.aggregation_type = aggregation_type
        if indexes is not None:
            self.indexes = indexes

    @property
    def service_instance_field(self):
        """Gets the service_instance_field of this QueryParamsDTO.  # noqa: E501


        :return: The service_instance_field of this QueryParamsDTO.  # noqa: E501
        :rtype: str
        """
        return self._service_instance_field

    @service_instance_field.setter
    def service_instance_field(self, service_instance_field):
        """Sets the service_instance_field of this QueryParamsDTO.


        :param service_instance_field: The service_instance_field of this QueryParamsDTO.  # noqa: E501
        :type: str
        """

        self._service_instance_field = service_instance_field

    @property
    def index(self):
        """Gets the index of this QueryParamsDTO.  # noqa: E501


        :return: The index of this QueryParamsDTO.  # noqa: E501
        :rtype: str
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this QueryParamsDTO.


        :param index: The index of this QueryParamsDTO.  # noqa: E501
        :type: str
        """

        self._index = index

    @property
    def time_stamp_identifier(self):
        """Gets the time_stamp_identifier of this QueryParamsDTO.  # noqa: E501


        :return: The time_stamp_identifier of this QueryParamsDTO.  # noqa: E501
        :rtype: str
        """
        return self._time_stamp_identifier

    @time_stamp_identifier.setter
    def time_stamp_identifier(self, time_stamp_identifier):
        """Sets the time_stamp_identifier of this QueryParamsDTO.


        :param time_stamp_identifier: The time_stamp_identifier of this QueryParamsDTO.  # noqa: E501
        :type: str
        """

        self._time_stamp_identifier = time_stamp_identifier

    @property
    def time_stamp_format(self):
        """Gets the time_stamp_format of this QueryParamsDTO.  # noqa: E501


        :return: The time_stamp_format of this QueryParamsDTO.  # noqa: E501
        :rtype: str
        """
        return self._time_stamp_format

    @time_stamp_format.setter
    def time_stamp_format(self, time_stamp_format):
        """Sets the time_stamp_format of this QueryParamsDTO.


        :param time_stamp_format: The time_stamp_format of this QueryParamsDTO.  # noqa: E501
        :type: str
        """

        self._time_stamp_format = time_stamp_format

    @property
    def message_identifier(self):
        """Gets the message_identifier of this QueryParamsDTO.  # noqa: E501


        :return: The message_identifier of this QueryParamsDTO.  # noqa: E501
        :rtype: str
        """
        return self._message_identifier

    @message_identifier.setter
    def message_identifier(self, message_identifier):
        """Sets the message_identifier of this QueryParamsDTO.


        :param message_identifier: The message_identifier of this QueryParamsDTO.  # noqa: E501
        :type: str
        """

        self._message_identifier = message_identifier

    @property
    def health_source_metric_name(self):
        """Gets the health_source_metric_name of this QueryParamsDTO.  # noqa: E501


        :return: The health_source_metric_name of this QueryParamsDTO.  # noqa: E501
        :rtype: str
        """
        return self._health_source_metric_name

    @health_source_metric_name.setter
    def health_source_metric_name(self, health_source_metric_name):
        """Sets the health_source_metric_name of this QueryParamsDTO.


        :param health_source_metric_name: The health_source_metric_name of this QueryParamsDTO.  # noqa: E501
        :type: str
        """

        self._health_source_metric_name = health_source_metric_name

    @property
    def health_source_metric_namespace(self):
        """Gets the health_source_metric_namespace of this QueryParamsDTO.  # noqa: E501


        :return: The health_source_metric_namespace of this QueryParamsDTO.  # noqa: E501
        :rtype: str
        """
        return self._health_source_metric_namespace

    @health_source_metric_namespace.setter
    def health_source_metric_namespace(self, health_source_metric_namespace):
        """Sets the health_source_metric_namespace of this QueryParamsDTO.


        :param health_source_metric_namespace: The health_source_metric_namespace of this QueryParamsDTO.  # noqa: E501
        :type: str
        """

        self._health_source_metric_namespace = health_source_metric_namespace

    @property
    def aggregation_type(self):
        """Gets the aggregation_type of this QueryParamsDTO.  # noqa: E501


        :return: The aggregation_type of this QueryParamsDTO.  # noqa: E501
        :rtype: str
        """
        return self._aggregation_type

    @aggregation_type.setter
    def aggregation_type(self, aggregation_type):
        """Sets the aggregation_type of this QueryParamsDTO.


        :param aggregation_type: The aggregation_type of this QueryParamsDTO.  # noqa: E501
        :type: str
        """
        allowed_values = ["average", "maximum", "minimum", "total", "count"]  # noqa: E501
        if aggregation_type not in allowed_values:
            raise ValueError(
                "Invalid value for `aggregation_type` ({0}), must be one of {1}"  # noqa: E501
                .format(aggregation_type, allowed_values)
            )

        self._aggregation_type = aggregation_type

    @property
    def indexes(self):
        """Gets the indexes of this QueryParamsDTO.  # noqa: E501


        :return: The indexes of this QueryParamsDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._indexes

    @indexes.setter
    def indexes(self, indexes):
        """Sets the indexes of this QueryParamsDTO.


        :param indexes: The indexes of this QueryParamsDTO.  # noqa: E501
        :type: list[str]
        """

        self._indexes = indexes

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
        if issubclass(QueryParamsDTO, dict):
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
        if not isinstance(other, QueryParamsDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
