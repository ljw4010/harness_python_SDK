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
from harness_python_sdk.models.sli_metric_spec import SLIMetricSpec  # noqa: F401,E501

class RatioSLIMetricSpec(SLIMetricSpec):
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
        'event_type': 'str',
        'metric1': 'str',
        'metric2': 'str',
        'threshold_value': 'float',
        'threshold_type': 'str',
        'consider_consecutive_minutes': 'int',
        'consider_all_consecutive_minutes_from_start_as_bad': 'bool'
    }
    if hasattr(SLIMetricSpec, "swagger_types"):
        swagger_types.update(SLIMetricSpec.swagger_types)

    attribute_map = {
        'event_type': 'eventType',
        'metric1': 'metric1',
        'metric2': 'metric2',
        'threshold_value': 'thresholdValue',
        'threshold_type': 'thresholdType',
        'consider_consecutive_minutes': 'considerConsecutiveMinutes',
        'consider_all_consecutive_minutes_from_start_as_bad': 'considerAllConsecutiveMinutesFromStartAsBad'
    }
    if hasattr(SLIMetricSpec, "attribute_map"):
        attribute_map.update(SLIMetricSpec.attribute_map)

    def __init__(self, event_type=None, metric1=None, metric2=None, threshold_value=None, threshold_type=None, consider_consecutive_minutes=None, consider_all_consecutive_minutes_from_start_as_bad=None, *args, **kwargs):  # noqa: E501
        """RatioSLIMetricSpec - a model defined in Swagger"""  # noqa: E501
        self._event_type = None
        self._metric1 = None
        self._metric2 = None
        self._threshold_value = None
        self._threshold_type = None
        self._consider_consecutive_minutes = None
        self._consider_all_consecutive_minutes_from_start_as_bad = None
        self.discriminator = None
        self.event_type = event_type
        self.metric1 = metric1
        self.metric2 = metric2
        self.threshold_value = threshold_value
        self.threshold_type = threshold_type
        if consider_consecutive_minutes is not None:
            self.consider_consecutive_minutes = consider_consecutive_minutes
        if consider_all_consecutive_minutes_from_start_as_bad is not None:
            self.consider_all_consecutive_minutes_from_start_as_bad = consider_all_consecutive_minutes_from_start_as_bad
        SLIMetricSpec.__init__(self, *args, **kwargs)

    @property
    def event_type(self):
        """Gets the event_type of this RatioSLIMetricSpec.  # noqa: E501


        :return: The event_type of this RatioSLIMetricSpec.  # noqa: E501
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this RatioSLIMetricSpec.


        :param event_type: The event_type of this RatioSLIMetricSpec.  # noqa: E501
        :type: str
        """
        if event_type is None:
            raise ValueError("Invalid value for `event_type`, must not be `None`")  # noqa: E501
        allowed_values = ["Good", "Bad"]  # noqa: E501
        if event_type not in allowed_values:
            raise ValueError(
                "Invalid value for `event_type` ({0}), must be one of {1}"  # noqa: E501
                .format(event_type, allowed_values)
            )

        self._event_type = event_type

    @property
    def metric1(self):
        """Gets the metric1 of this RatioSLIMetricSpec.  # noqa: E501


        :return: The metric1 of this RatioSLIMetricSpec.  # noqa: E501
        :rtype: str
        """
        return self._metric1

    @metric1.setter
    def metric1(self, metric1):
        """Sets the metric1 of this RatioSLIMetricSpec.


        :param metric1: The metric1 of this RatioSLIMetricSpec.  # noqa: E501
        :type: str
        """
        if metric1 is None:
            raise ValueError("Invalid value for `metric1`, must not be `None`")  # noqa: E501

        self._metric1 = metric1

    @property
    def metric2(self):
        """Gets the metric2 of this RatioSLIMetricSpec.  # noqa: E501


        :return: The metric2 of this RatioSLIMetricSpec.  # noqa: E501
        :rtype: str
        """
        return self._metric2

    @metric2.setter
    def metric2(self, metric2):
        """Sets the metric2 of this RatioSLIMetricSpec.


        :param metric2: The metric2 of this RatioSLIMetricSpec.  # noqa: E501
        :type: str
        """
        if metric2 is None:
            raise ValueError("Invalid value for `metric2`, must not be `None`")  # noqa: E501

        self._metric2 = metric2

    @property
    def threshold_value(self):
        """Gets the threshold_value of this RatioSLIMetricSpec.  # noqa: E501


        :return: The threshold_value of this RatioSLIMetricSpec.  # noqa: E501
        :rtype: float
        """
        return self._threshold_value

    @threshold_value.setter
    def threshold_value(self, threshold_value):
        """Sets the threshold_value of this RatioSLIMetricSpec.


        :param threshold_value: The threshold_value of this RatioSLIMetricSpec.  # noqa: E501
        :type: float
        """
        if threshold_value is None:
            raise ValueError("Invalid value for `threshold_value`, must not be `None`")  # noqa: E501

        self._threshold_value = threshold_value

    @property
    def threshold_type(self):
        """Gets the threshold_type of this RatioSLIMetricSpec.  # noqa: E501


        :return: The threshold_type of this RatioSLIMetricSpec.  # noqa: E501
        :rtype: str
        """
        return self._threshold_type

    @threshold_type.setter
    def threshold_type(self, threshold_type):
        """Sets the threshold_type of this RatioSLIMetricSpec.


        :param threshold_type: The threshold_type of this RatioSLIMetricSpec.  # noqa: E501
        :type: str
        """
        if threshold_type is None:
            raise ValueError("Invalid value for `threshold_type`, must not be `None`")  # noqa: E501
        allowed_values = [">", "<", ">=", "<="]  # noqa: E501
        if threshold_type not in allowed_values:
            raise ValueError(
                "Invalid value for `threshold_type` ({0}), must be one of {1}"  # noqa: E501
                .format(threshold_type, allowed_values)
            )

        self._threshold_type = threshold_type

    @property
    def consider_consecutive_minutes(self):
        """Gets the consider_consecutive_minutes of this RatioSLIMetricSpec.  # noqa: E501


        :return: The consider_consecutive_minutes of this RatioSLIMetricSpec.  # noqa: E501
        :rtype: int
        """
        return self._consider_consecutive_minutes

    @consider_consecutive_minutes.setter
    def consider_consecutive_minutes(self, consider_consecutive_minutes):
        """Sets the consider_consecutive_minutes of this RatioSLIMetricSpec.


        :param consider_consecutive_minutes: The consider_consecutive_minutes of this RatioSLIMetricSpec.  # noqa: E501
        :type: int
        """

        self._consider_consecutive_minutes = consider_consecutive_minutes

    @property
    def consider_all_consecutive_minutes_from_start_as_bad(self):
        """Gets the consider_all_consecutive_minutes_from_start_as_bad of this RatioSLIMetricSpec.  # noqa: E501


        :return: The consider_all_consecutive_minutes_from_start_as_bad of this RatioSLIMetricSpec.  # noqa: E501
        :rtype: bool
        """
        return self._consider_all_consecutive_minutes_from_start_as_bad

    @consider_all_consecutive_minutes_from_start_as_bad.setter
    def consider_all_consecutive_minutes_from_start_as_bad(self, consider_all_consecutive_minutes_from_start_as_bad):
        """Sets the consider_all_consecutive_minutes_from_start_as_bad of this RatioSLIMetricSpec.


        :param consider_all_consecutive_minutes_from_start_as_bad: The consider_all_consecutive_minutes_from_start_as_bad of this RatioSLIMetricSpec.  # noqa: E501
        :type: bool
        """

        self._consider_all_consecutive_minutes_from_start_as_bad = consider_all_consecutive_minutes_from_start_as_bad

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
        if issubclass(RatioSLIMetricSpec, dict):
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
        if not isinstance(other, RatioSLIMetricSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
