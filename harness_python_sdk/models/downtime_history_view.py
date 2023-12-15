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

class DowntimeHistoryView(object):
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
        'identifier': 'str',
        'name': 'str',
        'category': 'str',
        'affected_entities': 'list[AffectedEntity]',
        'duration': 'DowntimeDuration',
        'start_time': 'int',
        'start_date_time': 'str',
        'end_time': 'int',
        'end_date_time': 'str',
        'spec': 'DowntimeSpecDTO',
        'downtime_details': 'DowntimeSpecDTO'
    }

    attribute_map = {
        'identifier': 'identifier',
        'name': 'name',
        'category': 'category',
        'affected_entities': 'affectedEntities',
        'duration': 'duration',
        'start_time': 'startTime',
        'start_date_time': 'startDateTime',
        'end_time': 'endTime',
        'end_date_time': 'endDateTime',
        'spec': 'spec',
        'downtime_details': 'downtimeDetails'
    }

    def __init__(self, identifier=None, name=None, category=None, affected_entities=None, duration=None, start_time=None, start_date_time=None, end_time=None, end_date_time=None, spec=None, downtime_details=None):  # noqa: E501
        """DowntimeHistoryView - a model defined in Swagger"""  # noqa: E501
        self._identifier = None
        self._name = None
        self._category = None
        self._affected_entities = None
        self._duration = None
        self._start_time = None
        self._start_date_time = None
        self._end_time = None
        self._end_date_time = None
        self._spec = None
        self._downtime_details = None
        self.discriminator = None
        if identifier is not None:
            self.identifier = identifier
        if name is not None:
            self.name = name
        if category is not None:
            self.category = category
        if affected_entities is not None:
            self.affected_entities = affected_entities
        if duration is not None:
            self.duration = duration
        if start_time is not None:
            self.start_time = start_time
        if start_date_time is not None:
            self.start_date_time = start_date_time
        if end_time is not None:
            self.end_time = end_time
        if end_date_time is not None:
            self.end_date_time = end_date_time
        if spec is not None:
            self.spec = spec
        if downtime_details is not None:
            self.downtime_details = downtime_details

    @property
    def identifier(self):
        """Gets the identifier of this DowntimeHistoryView.  # noqa: E501


        :return: The identifier of this DowntimeHistoryView.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this DowntimeHistoryView.


        :param identifier: The identifier of this DowntimeHistoryView.  # noqa: E501
        :type: str
        """

        self._identifier = identifier

    @property
    def name(self):
        """Gets the name of this DowntimeHistoryView.  # noqa: E501


        :return: The name of this DowntimeHistoryView.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DowntimeHistoryView.


        :param name: The name of this DowntimeHistoryView.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def category(self):
        """Gets the category of this DowntimeHistoryView.  # noqa: E501


        :return: The category of this DowntimeHistoryView.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this DowntimeHistoryView.


        :param category: The category of this DowntimeHistoryView.  # noqa: E501
        :type: str
        """
        allowed_values = ["ScheduledMaintenance", "Deployment", "Other"]  # noqa: E501
        if category not in allowed_values:
            raise ValueError(
                "Invalid value for `category` ({0}), must be one of {1}"  # noqa: E501
                .format(category, allowed_values)
            )

        self._category = category

    @property
    def affected_entities(self):
        """Gets the affected_entities of this DowntimeHistoryView.  # noqa: E501


        :return: The affected_entities of this DowntimeHistoryView.  # noqa: E501
        :rtype: list[AffectedEntity]
        """
        return self._affected_entities

    @affected_entities.setter
    def affected_entities(self, affected_entities):
        """Sets the affected_entities of this DowntimeHistoryView.


        :param affected_entities: The affected_entities of this DowntimeHistoryView.  # noqa: E501
        :type: list[AffectedEntity]
        """

        self._affected_entities = affected_entities

    @property
    def duration(self):
        """Gets the duration of this DowntimeHistoryView.  # noqa: E501


        :return: The duration of this DowntimeHistoryView.  # noqa: E501
        :rtype: DowntimeDuration
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this DowntimeHistoryView.


        :param duration: The duration of this DowntimeHistoryView.  # noqa: E501
        :type: DowntimeDuration
        """

        self._duration = duration

    @property
    def start_time(self):
        """Gets the start_time of this DowntimeHistoryView.  # noqa: E501


        :return: The start_time of this DowntimeHistoryView.  # noqa: E501
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this DowntimeHistoryView.


        :param start_time: The start_time of this DowntimeHistoryView.  # noqa: E501
        :type: int
        """

        self._start_time = start_time

    @property
    def start_date_time(self):
        """Gets the start_date_time of this DowntimeHistoryView.  # noqa: E501


        :return: The start_date_time of this DowntimeHistoryView.  # noqa: E501
        :rtype: str
        """
        return self._start_date_time

    @start_date_time.setter
    def start_date_time(self, start_date_time):
        """Sets the start_date_time of this DowntimeHistoryView.


        :param start_date_time: The start_date_time of this DowntimeHistoryView.  # noqa: E501
        :type: str
        """

        self._start_date_time = start_date_time

    @property
    def end_time(self):
        """Gets the end_time of this DowntimeHistoryView.  # noqa: E501


        :return: The end_time of this DowntimeHistoryView.  # noqa: E501
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this DowntimeHistoryView.


        :param end_time: The end_time of this DowntimeHistoryView.  # noqa: E501
        :type: int
        """

        self._end_time = end_time

    @property
    def end_date_time(self):
        """Gets the end_date_time of this DowntimeHistoryView.  # noqa: E501


        :return: The end_date_time of this DowntimeHistoryView.  # noqa: E501
        :rtype: str
        """
        return self._end_date_time

    @end_date_time.setter
    def end_date_time(self, end_date_time):
        """Sets the end_date_time of this DowntimeHistoryView.


        :param end_date_time: The end_date_time of this DowntimeHistoryView.  # noqa: E501
        :type: str
        """

        self._end_date_time = end_date_time

    @property
    def spec(self):
        """Gets the spec of this DowntimeHistoryView.  # noqa: E501


        :return: The spec of this DowntimeHistoryView.  # noqa: E501
        :rtype: DowntimeSpecDTO
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this DowntimeHistoryView.


        :param spec: The spec of this DowntimeHistoryView.  # noqa: E501
        :type: DowntimeSpecDTO
        """

        self._spec = spec

    @property
    def downtime_details(self):
        """Gets the downtime_details of this DowntimeHistoryView.  # noqa: E501


        :return: The downtime_details of this DowntimeHistoryView.  # noqa: E501
        :rtype: DowntimeSpecDTO
        """
        return self._downtime_details

    @downtime_details.setter
    def downtime_details(self, downtime_details):
        """Sets the downtime_details of this DowntimeHistoryView.


        :param downtime_details: The downtime_details of this DowntimeHistoryView.  # noqa: E501
        :type: DowntimeSpecDTO
        """

        self._downtime_details = downtime_details

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
        if issubclass(DowntimeHistoryView, dict):
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
        if not isinstance(other, DowntimeHistoryView):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other