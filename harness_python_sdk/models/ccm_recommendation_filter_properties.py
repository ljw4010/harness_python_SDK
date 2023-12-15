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

class CCMRecommendationFilterProperties(object):
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
        'k8s_recommendation_filter_properties_dto': 'K8sRecommendationFilterProperties',
        'perspective_filters': 'list[QLCEViewFilterWrapper]',
        'min_saving': 'float',
        'min_cost': 'float',
        'days_back': 'int',
        'offset': 'int',
        'limit': 'int',
        'tags': 'dict(str, str)',
        'filter_type': 'str'
    }

    attribute_map = {
        'k8s_recommendation_filter_properties_dto': 'k8sRecommendationFilterPropertiesDTO',
        'perspective_filters': 'perspectiveFilters',
        'min_saving': 'minSaving',
        'min_cost': 'minCost',
        'days_back': 'daysBack',
        'offset': 'offset',
        'limit': 'limit',
        'tags': 'tags',
        'filter_type': 'filterType'
    }

    def __init__(self, k8s_recommendation_filter_properties_dto=None, perspective_filters=None, min_saving=None, min_cost=None, days_back=None, offset=None, limit=None, tags=None, filter_type=None):  # noqa: E501
        """CCMRecommendationFilterProperties - a model defined in Swagger"""  # noqa: E501
        self._k8s_recommendation_filter_properties_dto = None
        self._perspective_filters = None
        self._min_saving = None
        self._min_cost = None
        self._days_back = None
        self._offset = None
        self._limit = None
        self._tags = None
        self._filter_type = None
        self.discriminator = None
        if k8s_recommendation_filter_properties_dto is not None:
            self.k8s_recommendation_filter_properties_dto = k8s_recommendation_filter_properties_dto
        if perspective_filters is not None:
            self.perspective_filters = perspective_filters
        if min_saving is not None:
            self.min_saving = min_saving
        if min_cost is not None:
            self.min_cost = min_cost
        if days_back is not None:
            self.days_back = days_back
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if tags is not None:
            self.tags = tags
        if filter_type is not None:
            self.filter_type = filter_type

    @property
    def k8s_recommendation_filter_properties_dto(self):
        """Gets the k8s_recommendation_filter_properties_dto of this CCMRecommendationFilterProperties.  # noqa: E501


        :return: The k8s_recommendation_filter_properties_dto of this CCMRecommendationFilterProperties.  # noqa: E501
        :rtype: K8sRecommendationFilterProperties
        """
        return self._k8s_recommendation_filter_properties_dto

    @k8s_recommendation_filter_properties_dto.setter
    def k8s_recommendation_filter_properties_dto(self, k8s_recommendation_filter_properties_dto):
        """Sets the k8s_recommendation_filter_properties_dto of this CCMRecommendationFilterProperties.


        :param k8s_recommendation_filter_properties_dto: The k8s_recommendation_filter_properties_dto of this CCMRecommendationFilterProperties.  # noqa: E501
        :type: K8sRecommendationFilterProperties
        """

        self._k8s_recommendation_filter_properties_dto = k8s_recommendation_filter_properties_dto

    @property
    def perspective_filters(self):
        """Gets the perspective_filters of this CCMRecommendationFilterProperties.  # noqa: E501

        Get Recommendations for a perspective  # noqa: E501

        :return: The perspective_filters of this CCMRecommendationFilterProperties.  # noqa: E501
        :rtype: list[QLCEViewFilterWrapper]
        """
        return self._perspective_filters

    @perspective_filters.setter
    def perspective_filters(self, perspective_filters):
        """Sets the perspective_filters of this CCMRecommendationFilterProperties.

        Get Recommendations for a perspective  # noqa: E501

        :param perspective_filters: The perspective_filters of this CCMRecommendationFilterProperties.  # noqa: E501
        :type: list[QLCEViewFilterWrapper]
        """

        self._perspective_filters = perspective_filters

    @property
    def min_saving(self):
        """Gets the min_saving of this CCMRecommendationFilterProperties.  # noqa: E501

        Fetch recommendations with Saving more than minSaving  # noqa: E501

        :return: The min_saving of this CCMRecommendationFilterProperties.  # noqa: E501
        :rtype: float
        """
        return self._min_saving

    @min_saving.setter
    def min_saving(self, min_saving):
        """Sets the min_saving of this CCMRecommendationFilterProperties.

        Fetch recommendations with Saving more than minSaving  # noqa: E501

        :param min_saving: The min_saving of this CCMRecommendationFilterProperties.  # noqa: E501
        :type: float
        """

        self._min_saving = min_saving

    @property
    def min_cost(self):
        """Gets the min_cost of this CCMRecommendationFilterProperties.  # noqa: E501

        Fetch recommendations with Cost more than minCost  # noqa: E501

        :return: The min_cost of this CCMRecommendationFilterProperties.  # noqa: E501
        :rtype: float
        """
        return self._min_cost

    @min_cost.setter
    def min_cost(self, min_cost):
        """Sets the min_cost of this CCMRecommendationFilterProperties.

        Fetch recommendations with Cost more than minCost  # noqa: E501

        :param min_cost: The min_cost of this CCMRecommendationFilterProperties.  # noqa: E501
        :type: float
        """

        self._min_cost = min_cost

    @property
    def days_back(self):
        """Gets the days_back of this CCMRecommendationFilterProperties.  # noqa: E501

        Fetch recommendations generated in last daysBack days  # noqa: E501

        :return: The days_back of this CCMRecommendationFilterProperties.  # noqa: E501
        :rtype: int
        """
        return self._days_back

    @days_back.setter
    def days_back(self, days_back):
        """Sets the days_back of this CCMRecommendationFilterProperties.

        Fetch recommendations generated in last daysBack days  # noqa: E501

        :param days_back: The days_back of this CCMRecommendationFilterProperties.  # noqa: E501
        :type: int
        """

        self._days_back = days_back

    @property
    def offset(self):
        """Gets the offset of this CCMRecommendationFilterProperties.  # noqa: E501

        Query Offset  # noqa: E501

        :return: The offset of this CCMRecommendationFilterProperties.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this CCMRecommendationFilterProperties.

        Query Offset  # noqa: E501

        :param offset: The offset of this CCMRecommendationFilterProperties.  # noqa: E501
        :type: int
        """

        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this CCMRecommendationFilterProperties.  # noqa: E501

        Query Limit  # noqa: E501

        :return: The limit of this CCMRecommendationFilterProperties.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this CCMRecommendationFilterProperties.

        Query Limit  # noqa: E501

        :param limit: The limit of this CCMRecommendationFilterProperties.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def tags(self):
        """Gets the tags of this CCMRecommendationFilterProperties.  # noqa: E501

        Filter tags as a key-value pair.  # noqa: E501

        :return: The tags of this CCMRecommendationFilterProperties.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CCMRecommendationFilterProperties.

        Filter tags as a key-value pair.  # noqa: E501

        :param tags: The tags of this CCMRecommendationFilterProperties.  # noqa: E501
        :type: dict(str, str)
        """

        self._tags = tags

    @property
    def filter_type(self):
        """Gets the filter_type of this CCMRecommendationFilterProperties.  # noqa: E501


        :return: The filter_type of this CCMRecommendationFilterProperties.  # noqa: E501
        :rtype: str
        """
        return self._filter_type

    @filter_type.setter
    def filter_type(self, filter_type):
        """Sets the filter_type of this CCMRecommendationFilterProperties.


        :param filter_type: The filter_type of this CCMRecommendationFilterProperties.  # noqa: E501
        :type: str
        """
        allowed_values = ["CCMRecommendation"]  # noqa: E501
        if filter_type not in allowed_values:
            raise ValueError(
                "Invalid value for `filter_type` ({0}), must be one of {1}"  # noqa: E501
                .format(filter_type, allowed_values)
            )

        self._filter_type = filter_type

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
        if issubclass(CCMRecommendationFilterProperties, dict):
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
        if not isinstance(other, CCMRecommendationFilterProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
