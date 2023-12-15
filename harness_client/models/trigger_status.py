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

class TriggerStatus(object):
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
        'polling_subscription_status': 'PollingSubscriptionStatus',
        'validation_status': 'ValidationStatus',
        'webhook_auto_registration_status': 'WebhookAutoRegistrationStatus',
        'webhook_info': 'WebhookInfo',
        'status': 'str',
        'detail_messages': 'list[str]',
        'last_polling_update': 'int',
        'last_polled': 'list[str]'
    }

    attribute_map = {
        'polling_subscription_status': 'pollingSubscriptionStatus',
        'validation_status': 'validationStatus',
        'webhook_auto_registration_status': 'webhookAutoRegistrationStatus',
        'webhook_info': 'webhookInfo',
        'status': 'status',
        'detail_messages': 'detailMessages',
        'last_polling_update': 'lastPollingUpdate',
        'last_polled': 'lastPolled'
    }

    def __init__(self, polling_subscription_status=None, validation_status=None, webhook_auto_registration_status=None, webhook_info=None, status=None, detail_messages=None, last_polling_update=None, last_polled=None):  # noqa: E501
        """TriggerStatus - a model defined in Swagger"""  # noqa: E501
        self._polling_subscription_status = None
        self._validation_status = None
        self._webhook_auto_registration_status = None
        self._webhook_info = None
        self._status = None
        self._detail_messages = None
        self._last_polling_update = None
        self._last_polled = None
        self.discriminator = None
        if polling_subscription_status is not None:
            self.polling_subscription_status = polling_subscription_status
        if validation_status is not None:
            self.validation_status = validation_status
        if webhook_auto_registration_status is not None:
            self.webhook_auto_registration_status = webhook_auto_registration_status
        if webhook_info is not None:
            self.webhook_info = webhook_info
        if status is not None:
            self.status = status
        if detail_messages is not None:
            self.detail_messages = detail_messages
        if last_polling_update is not None:
            self.last_polling_update = last_polling_update
        if last_polled is not None:
            self.last_polled = last_polled

    @property
    def polling_subscription_status(self):
        """Gets the polling_subscription_status of this TriggerStatus.  # noqa: E501


        :return: The polling_subscription_status of this TriggerStatus.  # noqa: E501
        :rtype: PollingSubscriptionStatus
        """
        return self._polling_subscription_status

    @polling_subscription_status.setter
    def polling_subscription_status(self, polling_subscription_status):
        """Sets the polling_subscription_status of this TriggerStatus.


        :param polling_subscription_status: The polling_subscription_status of this TriggerStatus.  # noqa: E501
        :type: PollingSubscriptionStatus
        """

        self._polling_subscription_status = polling_subscription_status

    @property
    def validation_status(self):
        """Gets the validation_status of this TriggerStatus.  # noqa: E501


        :return: The validation_status of this TriggerStatus.  # noqa: E501
        :rtype: ValidationStatus
        """
        return self._validation_status

    @validation_status.setter
    def validation_status(self, validation_status):
        """Sets the validation_status of this TriggerStatus.


        :param validation_status: The validation_status of this TriggerStatus.  # noqa: E501
        :type: ValidationStatus
        """

        self._validation_status = validation_status

    @property
    def webhook_auto_registration_status(self):
        """Gets the webhook_auto_registration_status of this TriggerStatus.  # noqa: E501


        :return: The webhook_auto_registration_status of this TriggerStatus.  # noqa: E501
        :rtype: WebhookAutoRegistrationStatus
        """
        return self._webhook_auto_registration_status

    @webhook_auto_registration_status.setter
    def webhook_auto_registration_status(self, webhook_auto_registration_status):
        """Sets the webhook_auto_registration_status of this TriggerStatus.


        :param webhook_auto_registration_status: The webhook_auto_registration_status of this TriggerStatus.  # noqa: E501
        :type: WebhookAutoRegistrationStatus
        """

        self._webhook_auto_registration_status = webhook_auto_registration_status

    @property
    def webhook_info(self):
        """Gets the webhook_info of this TriggerStatus.  # noqa: E501


        :return: The webhook_info of this TriggerStatus.  # noqa: E501
        :rtype: WebhookInfo
        """
        return self._webhook_info

    @webhook_info.setter
    def webhook_info(self, webhook_info):
        """Sets the webhook_info of this TriggerStatus.


        :param webhook_info: The webhook_info of this TriggerStatus.  # noqa: E501
        :type: WebhookInfo
        """

        self._webhook_info = webhook_info

    @property
    def status(self):
        """Gets the status of this TriggerStatus.  # noqa: E501


        :return: The status of this TriggerStatus.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TriggerStatus.


        :param status: The status of this TriggerStatus.  # noqa: E501
        :type: str
        """
        allowed_values = ["SUCCESS", "FAILED", "UNKNOWN", "PENDING"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def detail_messages(self):
        """Gets the detail_messages of this TriggerStatus.  # noqa: E501


        :return: The detail_messages of this TriggerStatus.  # noqa: E501
        :rtype: list[str]
        """
        return self._detail_messages

    @detail_messages.setter
    def detail_messages(self, detail_messages):
        """Sets the detail_messages of this TriggerStatus.


        :param detail_messages: The detail_messages of this TriggerStatus.  # noqa: E501
        :type: list[str]
        """

        self._detail_messages = detail_messages

    @property
    def last_polling_update(self):
        """Gets the last_polling_update of this TriggerStatus.  # noqa: E501


        :return: The last_polling_update of this TriggerStatus.  # noqa: E501
        :rtype: int
        """
        return self._last_polling_update

    @last_polling_update.setter
    def last_polling_update(self, last_polling_update):
        """Sets the last_polling_update of this TriggerStatus.


        :param last_polling_update: The last_polling_update of this TriggerStatus.  # noqa: E501
        :type: int
        """

        self._last_polling_update = last_polling_update

    @property
    def last_polled(self):
        """Gets the last_polled of this TriggerStatus.  # noqa: E501


        :return: The last_polled of this TriggerStatus.  # noqa: E501
        :rtype: list[str]
        """
        return self._last_polled

    @last_polled.setter
    def last_polled(self, last_polled):
        """Sets the last_polled of this TriggerStatus.


        :param last_polled: The last_polled of this TriggerStatus.  # noqa: E501
        :type: list[str]
        """

        self._last_polled = last_polled

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
        if issubclass(TriggerStatus, dict):
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
        if not isinstance(other, TriggerStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
