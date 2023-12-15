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

class AlertThreshold(object):
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
        'percentage': 'float',
        'based_on': 'str',
        'email_addresses': 'list[str]',
        'user_group_ids': 'list[str]',
        'slack_webhooks': 'list[str]',
        'alerts_sent': 'int',
        'crossed_at': 'int'
    }

    attribute_map = {
        'percentage': 'percentage',
        'based_on': 'basedOn',
        'email_addresses': 'emailAddresses',
        'user_group_ids': 'userGroupIds',
        'slack_webhooks': 'slackWebhooks',
        'alerts_sent': 'alertsSent',
        'crossed_at': 'crossedAt'
    }

    def __init__(self, percentage=None, based_on=None, email_addresses=None, user_group_ids=None, slack_webhooks=None, alerts_sent=None, crossed_at=None):  # noqa: E501
        """AlertThreshold - a model defined in Swagger"""  # noqa: E501
        self._percentage = None
        self._based_on = None
        self._email_addresses = None
        self._user_group_ids = None
        self._slack_webhooks = None
        self._alerts_sent = None
        self._crossed_at = None
        self.discriminator = None
        if percentage is not None:
            self.percentage = percentage
        if based_on is not None:
            self.based_on = based_on
        if email_addresses is not None:
            self.email_addresses = email_addresses
        if user_group_ids is not None:
            self.user_group_ids = user_group_ids
        if slack_webhooks is not None:
            self.slack_webhooks = slack_webhooks
        if alerts_sent is not None:
            self.alerts_sent = alerts_sent
        if crossed_at is not None:
            self.crossed_at = crossed_at

    @property
    def percentage(self):
        """Gets the percentage of this AlertThreshold.  # noqa: E501


        :return: The percentage of this AlertThreshold.  # noqa: E501
        :rtype: float
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        """Sets the percentage of this AlertThreshold.


        :param percentage: The percentage of this AlertThreshold.  # noqa: E501
        :type: float
        """

        self._percentage = percentage

    @property
    def based_on(self):
        """Gets the based_on of this AlertThreshold.  # noqa: E501

        Whether the alert is based on Actual cost or next 30 days Forecasted Cost  # noqa: E501

        :return: The based_on of this AlertThreshold.  # noqa: E501
        :rtype: str
        """
        return self._based_on

    @based_on.setter
    def based_on(self, based_on):
        """Sets the based_on of this AlertThreshold.

        Whether the alert is based on Actual cost or next 30 days Forecasted Cost  # noqa: E501

        :param based_on: The based_on of this AlertThreshold.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACTUAL_COST", "FORECASTED_COST"]  # noqa: E501
        if based_on not in allowed_values:
            raise ValueError(
                "Invalid value for `based_on` ({0}), must be one of {1}"  # noqa: E501
                .format(based_on, allowed_values)
            )

        self._based_on = based_on

    @property
    def email_addresses(self):
        """Gets the email_addresses of this AlertThreshold.  # noqa: E501


        :return: The email_addresses of this AlertThreshold.  # noqa: E501
        :rtype: list[str]
        """
        return self._email_addresses

    @email_addresses.setter
    def email_addresses(self, email_addresses):
        """Sets the email_addresses of this AlertThreshold.


        :param email_addresses: The email_addresses of this AlertThreshold.  # noqa: E501
        :type: list[str]
        """

        self._email_addresses = email_addresses

    @property
    def user_group_ids(self):
        """Gets the user_group_ids of this AlertThreshold.  # noqa: E501


        :return: The user_group_ids of this AlertThreshold.  # noqa: E501
        :rtype: list[str]
        """
        return self._user_group_ids

    @user_group_ids.setter
    def user_group_ids(self, user_group_ids):
        """Sets the user_group_ids of this AlertThreshold.


        :param user_group_ids: The user_group_ids of this AlertThreshold.  # noqa: E501
        :type: list[str]
        """

        self._user_group_ids = user_group_ids

    @property
    def slack_webhooks(self):
        """Gets the slack_webhooks of this AlertThreshold.  # noqa: E501


        :return: The slack_webhooks of this AlertThreshold.  # noqa: E501
        :rtype: list[str]
        """
        return self._slack_webhooks

    @slack_webhooks.setter
    def slack_webhooks(self, slack_webhooks):
        """Sets the slack_webhooks of this AlertThreshold.


        :param slack_webhooks: The slack_webhooks of this AlertThreshold.  # noqa: E501
        :type: list[str]
        """

        self._slack_webhooks = slack_webhooks

    @property
    def alerts_sent(self):
        """Gets the alerts_sent of this AlertThreshold.  # noqa: E501


        :return: The alerts_sent of this AlertThreshold.  # noqa: E501
        :rtype: int
        """
        return self._alerts_sent

    @alerts_sent.setter
    def alerts_sent(self, alerts_sent):
        """Sets the alerts_sent of this AlertThreshold.


        :param alerts_sent: The alerts_sent of this AlertThreshold.  # noqa: E501
        :type: int
        """

        self._alerts_sent = alerts_sent

    @property
    def crossed_at(self):
        """Gets the crossed_at of this AlertThreshold.  # noqa: E501


        :return: The crossed_at of this AlertThreshold.  # noqa: E501
        :rtype: int
        """
        return self._crossed_at

    @crossed_at.setter
    def crossed_at(self, crossed_at):
        """Sets the crossed_at of this AlertThreshold.


        :param crossed_at: The crossed_at of this AlertThreshold.  # noqa: E501
        :type: int
        """

        self._crossed_at = crossed_at

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
        if issubclass(AlertThreshold, dict):
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
        if not isinstance(other, AlertThreshold):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
