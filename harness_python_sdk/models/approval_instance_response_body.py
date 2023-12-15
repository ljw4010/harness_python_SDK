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

class ApprovalInstanceResponseBody(object):
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
        'type': 'str',
        'status': 'str',
        'deadline': 'int',
        'created': 'int',
        'updated': 'int',
        'error_message': 'str',
        'details': 'object'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'status': 'status',
        'deadline': 'deadline',
        'created': 'created',
        'updated': 'updated',
        'error_message': 'error_message',
        'details': 'details'
    }

    def __init__(self, id=None, type=None, status=None, deadline=None, created=None, updated=None, error_message=None, details=None):  # noqa: E501
        """ApprovalInstanceResponseBody - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._type = None
        self._status = None
        self._deadline = None
        self._created = None
        self._updated = None
        self._error_message = None
        self._details = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        if deadline is not None:
            self.deadline = deadline
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated
        if error_message is not None:
            self.error_message = error_message
        if details is not None:
            self.details = details

    @property
    def id(self):
        """Gets the id of this ApprovalInstanceResponseBody.  # noqa: E501

        Approval Instance identifier  # noqa: E501

        :return: The id of this ApprovalInstanceResponseBody.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApprovalInstanceResponseBody.

        Approval Instance identifier  # noqa: E501

        :param id: The id of this ApprovalInstanceResponseBody.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this ApprovalInstanceResponseBody.  # noqa: E501

        Tells the type of Approval  # noqa: E501

        :return: The type of this ApprovalInstanceResponseBody.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ApprovalInstanceResponseBody.

        Tells the type of Approval  # noqa: E501

        :param type: The type of this ApprovalInstanceResponseBody.  # noqa: E501
        :type: str
        """
        allowed_values = ["HarnessApproval", "JiraApproval", "CustomApproval", "ServiceNowApproval"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def status(self):
        """Gets the status of this ApprovalInstanceResponseBody.  # noqa: E501

        Tells the status of Approval  # noqa: E501

        :return: The status of this ApprovalInstanceResponseBody.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ApprovalInstanceResponseBody.

        Tells the status of Approval  # noqa: E501

        :param status: The status of this ApprovalInstanceResponseBody.  # noqa: E501
        :type: str
        """
        allowed_values = ["WAITING", "APPROVED", "REJECTED", "FAILED", "ABORTED", "EXPIRED"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def deadline(self):
        """Gets the deadline of this ApprovalInstanceResponseBody.  # noqa: E501

        Deadline timestamp for Approval Instance  # noqa: E501

        :return: The deadline of this ApprovalInstanceResponseBody.  # noqa: E501
        :rtype: int
        """
        return self._deadline

    @deadline.setter
    def deadline(self, deadline):
        """Sets the deadline of this ApprovalInstanceResponseBody.

        Deadline timestamp for Approval Instance  # noqa: E501

        :param deadline: The deadline of this ApprovalInstanceResponseBody.  # noqa: E501
        :type: int
        """

        self._deadline = deadline

    @property
    def created(self):
        """Gets the created of this ApprovalInstanceResponseBody.  # noqa: E501

        Creation timestamp for Approval Instance  # noqa: E501

        :return: The created of this ApprovalInstanceResponseBody.  # noqa: E501
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ApprovalInstanceResponseBody.

        Creation timestamp for Approval Instance  # noqa: E501

        :param created: The created of this ApprovalInstanceResponseBody.  # noqa: E501
        :type: int
        """

        self._created = created

    @property
    def updated(self):
        """Gets the updated of this ApprovalInstanceResponseBody.  # noqa: E501

        Last modification timestamp for Approval Instance  # noqa: E501

        :return: The updated of this ApprovalInstanceResponseBody.  # noqa: E501
        :rtype: int
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this ApprovalInstanceResponseBody.

        Last modification timestamp for Approval Instance  # noqa: E501

        :param updated: The updated of this ApprovalInstanceResponseBody.  # noqa: E501
        :type: int
        """

        self._updated = updated

    @property
    def error_message(self):
        """Gets the error_message of this ApprovalInstanceResponseBody.  # noqa: E501

        Error message for the Approval Instance  # noqa: E501

        :return: The error_message of this ApprovalInstanceResponseBody.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this ApprovalInstanceResponseBody.

        Error message for the Approval Instance  # noqa: E501

        :param error_message: The error_message of this ApprovalInstanceResponseBody.  # noqa: E501
        :type: str
        """

        self._error_message = error_message

    @property
    def details(self):
        """Gets the details of this ApprovalInstanceResponseBody.  # noqa: E501

        Approval Instance response details  # noqa: E501

        :return: The details of this ApprovalInstanceResponseBody.  # noqa: E501
        :rtype: object
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this ApprovalInstanceResponseBody.

        Approval Instance response details  # noqa: E501

        :param details: The details of this ApprovalInstanceResponseBody.  # noqa: E501
        :type: object
        """

        self._details = details

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
        if issubclass(ApprovalInstanceResponseBody, dict):
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
        if not isinstance(other, ApprovalInstanceResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
