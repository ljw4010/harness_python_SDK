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

class AnomalyData(object):
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
        'time': 'int',
        'anomaly_relative_time': 'str',
        'actual_amount': 'float',
        'expected_amount': 'float',
        'anomalous_spend': 'float',
        'anomalous_spend_percentage': 'float',
        'resource_name': 'str',
        'resource_info': 'str',
        'entity': 'EntityInfo',
        'details': 'str',
        'status': 'str',
        'status_relative_time': 'str',
        'comment': 'str',
        'cloud_provider': 'str',
        'anomaly_score': 'float',
        'user_feedback': 'str',
        'perspective_id': 'str',
        'perspective_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'time': 'time',
        'anomaly_relative_time': 'anomalyRelativeTime',
        'actual_amount': 'actualAmount',
        'expected_amount': 'expectedAmount',
        'anomalous_spend': 'anomalousSpend',
        'anomalous_spend_percentage': 'anomalousSpendPercentage',
        'resource_name': 'resourceName',
        'resource_info': 'resourceInfo',
        'entity': 'entity',
        'details': 'details',
        'status': 'status',
        'status_relative_time': 'statusRelativeTime',
        'comment': 'comment',
        'cloud_provider': 'cloudProvider',
        'anomaly_score': 'anomalyScore',
        'user_feedback': 'userFeedback',
        'perspective_id': 'perspectiveId',
        'perspective_name': 'perspectiveName'
    }

    def __init__(self, id=None, time=None, anomaly_relative_time=None, actual_amount=None, expected_amount=None, anomalous_spend=None, anomalous_spend_percentage=None, resource_name=None, resource_info=None, entity=None, details=None, status=None, status_relative_time=None, comment=None, cloud_provider=None, anomaly_score=None, user_feedback=None, perspective_id=None, perspective_name=None):  # noqa: E501
        """AnomalyData - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._time = None
        self._anomaly_relative_time = None
        self._actual_amount = None
        self._expected_amount = None
        self._anomalous_spend = None
        self._anomalous_spend_percentage = None
        self._resource_name = None
        self._resource_info = None
        self._entity = None
        self._details = None
        self._status = None
        self._status_relative_time = None
        self._comment = None
        self._cloud_provider = None
        self._anomaly_score = None
        self._user_feedback = None
        self._perspective_id = None
        self._perspective_name = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if time is not None:
            self.time = time
        if anomaly_relative_time is not None:
            self.anomaly_relative_time = anomaly_relative_time
        if actual_amount is not None:
            self.actual_amount = actual_amount
        if expected_amount is not None:
            self.expected_amount = expected_amount
        if anomalous_spend is not None:
            self.anomalous_spend = anomalous_spend
        if anomalous_spend_percentage is not None:
            self.anomalous_spend_percentage = anomalous_spend_percentage
        if resource_name is not None:
            self.resource_name = resource_name
        if resource_info is not None:
            self.resource_info = resource_info
        if entity is not None:
            self.entity = entity
        if details is not None:
            self.details = details
        if status is not None:
            self.status = status
        if status_relative_time is not None:
            self.status_relative_time = status_relative_time
        if comment is not None:
            self.comment = comment
        if cloud_provider is not None:
            self.cloud_provider = cloud_provider
        if anomaly_score is not None:
            self.anomaly_score = anomaly_score
        if user_feedback is not None:
            self.user_feedback = user_feedback
        if perspective_id is not None:
            self.perspective_id = perspective_id
        if perspective_name is not None:
            self.perspective_name = perspective_name

    @property
    def id(self):
        """Gets the id of this AnomalyData.  # noqa: E501


        :return: The id of this AnomalyData.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AnomalyData.


        :param id: The id of this AnomalyData.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def time(self):
        """Gets the time of this AnomalyData.  # noqa: E501


        :return: The time of this AnomalyData.  # noqa: E501
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this AnomalyData.


        :param time: The time of this AnomalyData.  # noqa: E501
        :type: int
        """

        self._time = time

    @property
    def anomaly_relative_time(self):
        """Gets the anomaly_relative_time of this AnomalyData.  # noqa: E501


        :return: The anomaly_relative_time of this AnomalyData.  # noqa: E501
        :rtype: str
        """
        return self._anomaly_relative_time

    @anomaly_relative_time.setter
    def anomaly_relative_time(self, anomaly_relative_time):
        """Sets the anomaly_relative_time of this AnomalyData.


        :param anomaly_relative_time: The anomaly_relative_time of this AnomalyData.  # noqa: E501
        :type: str
        """

        self._anomaly_relative_time = anomaly_relative_time

    @property
    def actual_amount(self):
        """Gets the actual_amount of this AnomalyData.  # noqa: E501


        :return: The actual_amount of this AnomalyData.  # noqa: E501
        :rtype: float
        """
        return self._actual_amount

    @actual_amount.setter
    def actual_amount(self, actual_amount):
        """Sets the actual_amount of this AnomalyData.


        :param actual_amount: The actual_amount of this AnomalyData.  # noqa: E501
        :type: float
        """

        self._actual_amount = actual_amount

    @property
    def expected_amount(self):
        """Gets the expected_amount of this AnomalyData.  # noqa: E501


        :return: The expected_amount of this AnomalyData.  # noqa: E501
        :rtype: float
        """
        return self._expected_amount

    @expected_amount.setter
    def expected_amount(self, expected_amount):
        """Sets the expected_amount of this AnomalyData.


        :param expected_amount: The expected_amount of this AnomalyData.  # noqa: E501
        :type: float
        """

        self._expected_amount = expected_amount

    @property
    def anomalous_spend(self):
        """Gets the anomalous_spend of this AnomalyData.  # noqa: E501


        :return: The anomalous_spend of this AnomalyData.  # noqa: E501
        :rtype: float
        """
        return self._anomalous_spend

    @anomalous_spend.setter
    def anomalous_spend(self, anomalous_spend):
        """Sets the anomalous_spend of this AnomalyData.


        :param anomalous_spend: The anomalous_spend of this AnomalyData.  # noqa: E501
        :type: float
        """

        self._anomalous_spend = anomalous_spend

    @property
    def anomalous_spend_percentage(self):
        """Gets the anomalous_spend_percentage of this AnomalyData.  # noqa: E501


        :return: The anomalous_spend_percentage of this AnomalyData.  # noqa: E501
        :rtype: float
        """
        return self._anomalous_spend_percentage

    @anomalous_spend_percentage.setter
    def anomalous_spend_percentage(self, anomalous_spend_percentage):
        """Sets the anomalous_spend_percentage of this AnomalyData.


        :param anomalous_spend_percentage: The anomalous_spend_percentage of this AnomalyData.  # noqa: E501
        :type: float
        """

        self._anomalous_spend_percentage = anomalous_spend_percentage

    @property
    def resource_name(self):
        """Gets the resource_name of this AnomalyData.  # noqa: E501


        :return: The resource_name of this AnomalyData.  # noqa: E501
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this AnomalyData.


        :param resource_name: The resource_name of this AnomalyData.  # noqa: E501
        :type: str
        """

        self._resource_name = resource_name

    @property
    def resource_info(self):
        """Gets the resource_info of this AnomalyData.  # noqa: E501


        :return: The resource_info of this AnomalyData.  # noqa: E501
        :rtype: str
        """
        return self._resource_info

    @resource_info.setter
    def resource_info(self, resource_info):
        """Sets the resource_info of this AnomalyData.


        :param resource_info: The resource_info of this AnomalyData.  # noqa: E501
        :type: str
        """

        self._resource_info = resource_info

    @property
    def entity(self):
        """Gets the entity of this AnomalyData.  # noqa: E501


        :return: The entity of this AnomalyData.  # noqa: E501
        :rtype: EntityInfo
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        """Sets the entity of this AnomalyData.


        :param entity: The entity of this AnomalyData.  # noqa: E501
        :type: EntityInfo
        """

        self._entity = entity

    @property
    def details(self):
        """Gets the details of this AnomalyData.  # noqa: E501


        :return: The details of this AnomalyData.  # noqa: E501
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this AnomalyData.


        :param details: The details of this AnomalyData.  # noqa: E501
        :type: str
        """

        self._details = details

    @property
    def status(self):
        """Gets the status of this AnomalyData.  # noqa: E501


        :return: The status of this AnomalyData.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AnomalyData.


        :param status: The status of this AnomalyData.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def status_relative_time(self):
        """Gets the status_relative_time of this AnomalyData.  # noqa: E501


        :return: The status_relative_time of this AnomalyData.  # noqa: E501
        :rtype: str
        """
        return self._status_relative_time

    @status_relative_time.setter
    def status_relative_time(self, status_relative_time):
        """Sets the status_relative_time of this AnomalyData.


        :param status_relative_time: The status_relative_time of this AnomalyData.  # noqa: E501
        :type: str
        """

        self._status_relative_time = status_relative_time

    @property
    def comment(self):
        """Gets the comment of this AnomalyData.  # noqa: E501


        :return: The comment of this AnomalyData.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this AnomalyData.


        :param comment: The comment of this AnomalyData.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def cloud_provider(self):
        """Gets the cloud_provider of this AnomalyData.  # noqa: E501


        :return: The cloud_provider of this AnomalyData.  # noqa: E501
        :rtype: str
        """
        return self._cloud_provider

    @cloud_provider.setter
    def cloud_provider(self, cloud_provider):
        """Sets the cloud_provider of this AnomalyData.


        :param cloud_provider: The cloud_provider of this AnomalyData.  # noqa: E501
        :type: str
        """

        self._cloud_provider = cloud_provider

    @property
    def anomaly_score(self):
        """Gets the anomaly_score of this AnomalyData.  # noqa: E501


        :return: The anomaly_score of this AnomalyData.  # noqa: E501
        :rtype: float
        """
        return self._anomaly_score

    @anomaly_score.setter
    def anomaly_score(self, anomaly_score):
        """Sets the anomaly_score of this AnomalyData.


        :param anomaly_score: The anomaly_score of this AnomalyData.  # noqa: E501
        :type: float
        """

        self._anomaly_score = anomaly_score

    @property
    def user_feedback(self):
        """Gets the user_feedback of this AnomalyData.  # noqa: E501


        :return: The user_feedback of this AnomalyData.  # noqa: E501
        :rtype: str
        """
        return self._user_feedback

    @user_feedback.setter
    def user_feedback(self, user_feedback):
        """Sets the user_feedback of this AnomalyData.


        :param user_feedback: The user_feedback of this AnomalyData.  # noqa: E501
        :type: str
        """
        allowed_values = ["TRUE_ANOMALY", "FALSE_ANOMALY", "NOT_RESPONDED"]  # noqa: E501
        if user_feedback not in allowed_values:
            raise ValueError(
                "Invalid value for `user_feedback` ({0}), must be one of {1}"  # noqa: E501
                .format(user_feedback, allowed_values)
            )

        self._user_feedback = user_feedback

    @property
    def perspective_id(self):
        """Gets the perspective_id of this AnomalyData.  # noqa: E501


        :return: The perspective_id of this AnomalyData.  # noqa: E501
        :rtype: str
        """
        return self._perspective_id

    @perspective_id.setter
    def perspective_id(self, perspective_id):
        """Sets the perspective_id of this AnomalyData.


        :param perspective_id: The perspective_id of this AnomalyData.  # noqa: E501
        :type: str
        """

        self._perspective_id = perspective_id

    @property
    def perspective_name(self):
        """Gets the perspective_name of this AnomalyData.  # noqa: E501


        :return: The perspective_name of this AnomalyData.  # noqa: E501
        :rtype: str
        """
        return self._perspective_name

    @perspective_name.setter
    def perspective_name(self, perspective_name):
        """Sets the perspective_name of this AnomalyData.


        :param perspective_name: The perspective_name of this AnomalyData.  # noqa: E501
        :type: str
        """

        self._perspective_name = perspective_name

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
        if issubclass(AnomalyData, dict):
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
        if not isinstance(other, AnomalyData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
