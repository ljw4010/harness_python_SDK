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

class Apicorev1Event(object):
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
        'metadata': 'V1ObjectMeta',
        'involved_object': 'V1ObjectReference',
        'reason': 'str',
        'message': 'str',
        'source': 'V1EventSource',
        'first_timestamp': 'V1Time',
        'last_timestamp': 'V1Time',
        'count': 'int',
        'type': 'str',
        'event_time': 'V1MicroTime',
        'series': 'V1EventSeries',
        'action': 'str',
        'related': 'V1ObjectReference',
        'reporting_component': 'str',
        'reporting_instance': 'str'
    }

    attribute_map = {
        'metadata': 'metadata',
        'involved_object': 'involvedObject',
        'reason': 'reason',
        'message': 'message',
        'source': 'source',
        'first_timestamp': 'firstTimestamp',
        'last_timestamp': 'lastTimestamp',
        'count': 'count',
        'type': 'type',
        'event_time': 'eventTime',
        'series': 'series',
        'action': 'action',
        'related': 'related',
        'reporting_component': 'reportingComponent',
        'reporting_instance': 'reportingInstance'
    }

    def __init__(self, metadata=None, involved_object=None, reason=None, message=None, source=None, first_timestamp=None, last_timestamp=None, count=None, type=None, event_time=None, series=None, action=None, related=None, reporting_component=None, reporting_instance=None):  # noqa: E501
        """Apicorev1Event - a model defined in Swagger"""  # noqa: E501
        self._metadata = None
        self._involved_object = None
        self._reason = None
        self._message = None
        self._source = None
        self._first_timestamp = None
        self._last_timestamp = None
        self._count = None
        self._type = None
        self._event_time = None
        self._series = None
        self._action = None
        self._related = None
        self._reporting_component = None
        self._reporting_instance = None
        self.discriminator = None
        if metadata is not None:
            self.metadata = metadata
        if involved_object is not None:
            self.involved_object = involved_object
        if reason is not None:
            self.reason = reason
        if message is not None:
            self.message = message
        if source is not None:
            self.source = source
        if first_timestamp is not None:
            self.first_timestamp = first_timestamp
        if last_timestamp is not None:
            self.last_timestamp = last_timestamp
        if count is not None:
            self.count = count
        if type is not None:
            self.type = type
        if event_time is not None:
            self.event_time = event_time
        if series is not None:
            self.series = series
        if action is not None:
            self.action = action
        if related is not None:
            self.related = related
        if reporting_component is not None:
            self.reporting_component = reporting_component
        if reporting_instance is not None:
            self.reporting_instance = reporting_instance

    @property
    def metadata(self):
        """Gets the metadata of this Apicorev1Event.  # noqa: E501


        :return: The metadata of this Apicorev1Event.  # noqa: E501
        :rtype: V1ObjectMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Apicorev1Event.


        :param metadata: The metadata of this Apicorev1Event.  # noqa: E501
        :type: V1ObjectMeta
        """

        self._metadata = metadata

    @property
    def involved_object(self):
        """Gets the involved_object of this Apicorev1Event.  # noqa: E501


        :return: The involved_object of this Apicorev1Event.  # noqa: E501
        :rtype: V1ObjectReference
        """
        return self._involved_object

    @involved_object.setter
    def involved_object(self, involved_object):
        """Sets the involved_object of this Apicorev1Event.


        :param involved_object: The involved_object of this Apicorev1Event.  # noqa: E501
        :type: V1ObjectReference
        """

        self._involved_object = involved_object

    @property
    def reason(self):
        """Gets the reason of this Apicorev1Event.  # noqa: E501


        :return: The reason of this Apicorev1Event.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this Apicorev1Event.


        :param reason: The reason of this Apicorev1Event.  # noqa: E501
        :type: str
        """

        self._reason = reason

    @property
    def message(self):
        """Gets the message of this Apicorev1Event.  # noqa: E501


        :return: The message of this Apicorev1Event.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this Apicorev1Event.


        :param message: The message of this Apicorev1Event.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def source(self):
        """Gets the source of this Apicorev1Event.  # noqa: E501


        :return: The source of this Apicorev1Event.  # noqa: E501
        :rtype: V1EventSource
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this Apicorev1Event.


        :param source: The source of this Apicorev1Event.  # noqa: E501
        :type: V1EventSource
        """

        self._source = source

    @property
    def first_timestamp(self):
        """Gets the first_timestamp of this Apicorev1Event.  # noqa: E501


        :return: The first_timestamp of this Apicorev1Event.  # noqa: E501
        :rtype: V1Time
        """
        return self._first_timestamp

    @first_timestamp.setter
    def first_timestamp(self, first_timestamp):
        """Sets the first_timestamp of this Apicorev1Event.


        :param first_timestamp: The first_timestamp of this Apicorev1Event.  # noqa: E501
        :type: V1Time
        """

        self._first_timestamp = first_timestamp

    @property
    def last_timestamp(self):
        """Gets the last_timestamp of this Apicorev1Event.  # noqa: E501


        :return: The last_timestamp of this Apicorev1Event.  # noqa: E501
        :rtype: V1Time
        """
        return self._last_timestamp

    @last_timestamp.setter
    def last_timestamp(self, last_timestamp):
        """Sets the last_timestamp of this Apicorev1Event.


        :param last_timestamp: The last_timestamp of this Apicorev1Event.  # noqa: E501
        :type: V1Time
        """

        self._last_timestamp = last_timestamp

    @property
    def count(self):
        """Gets the count of this Apicorev1Event.  # noqa: E501


        :return: The count of this Apicorev1Event.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this Apicorev1Event.


        :param count: The count of this Apicorev1Event.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def type(self):
        """Gets the type of this Apicorev1Event.  # noqa: E501


        :return: The type of this Apicorev1Event.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Apicorev1Event.


        :param type: The type of this Apicorev1Event.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def event_time(self):
        """Gets the event_time of this Apicorev1Event.  # noqa: E501


        :return: The event_time of this Apicorev1Event.  # noqa: E501
        :rtype: V1MicroTime
        """
        return self._event_time

    @event_time.setter
    def event_time(self, event_time):
        """Sets the event_time of this Apicorev1Event.


        :param event_time: The event_time of this Apicorev1Event.  # noqa: E501
        :type: V1MicroTime
        """

        self._event_time = event_time

    @property
    def series(self):
        """Gets the series of this Apicorev1Event.  # noqa: E501


        :return: The series of this Apicorev1Event.  # noqa: E501
        :rtype: V1EventSeries
        """
        return self._series

    @series.setter
    def series(self, series):
        """Sets the series of this Apicorev1Event.


        :param series: The series of this Apicorev1Event.  # noqa: E501
        :type: V1EventSeries
        """

        self._series = series

    @property
    def action(self):
        """Gets the action of this Apicorev1Event.  # noqa: E501


        :return: The action of this Apicorev1Event.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this Apicorev1Event.


        :param action: The action of this Apicorev1Event.  # noqa: E501
        :type: str
        """

        self._action = action

    @property
    def related(self):
        """Gets the related of this Apicorev1Event.  # noqa: E501


        :return: The related of this Apicorev1Event.  # noqa: E501
        :rtype: V1ObjectReference
        """
        return self._related

    @related.setter
    def related(self, related):
        """Sets the related of this Apicorev1Event.


        :param related: The related of this Apicorev1Event.  # noqa: E501
        :type: V1ObjectReference
        """

        self._related = related

    @property
    def reporting_component(self):
        """Gets the reporting_component of this Apicorev1Event.  # noqa: E501


        :return: The reporting_component of this Apicorev1Event.  # noqa: E501
        :rtype: str
        """
        return self._reporting_component

    @reporting_component.setter
    def reporting_component(self, reporting_component):
        """Sets the reporting_component of this Apicorev1Event.


        :param reporting_component: The reporting_component of this Apicorev1Event.  # noqa: E501
        :type: str
        """

        self._reporting_component = reporting_component

    @property
    def reporting_instance(self):
        """Gets the reporting_instance of this Apicorev1Event.  # noqa: E501


        :return: The reporting_instance of this Apicorev1Event.  # noqa: E501
        :rtype: str
        """
        return self._reporting_instance

    @reporting_instance.setter
    def reporting_instance(self, reporting_instance):
        """Sets the reporting_instance of this Apicorev1Event.


        :param reporting_instance: The reporting_instance of this Apicorev1Event.  # noqa: E501
        :type: str
        """

        self._reporting_instance = reporting_instance

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
        if issubclass(Apicorev1Event, dict):
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
        if not isinstance(other, Apicorev1Event):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
