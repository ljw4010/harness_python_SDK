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

class WebhookEventProcessingDetails(object):
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
        'event_found': 'bool',
        'event_id': 'str',
        'account_identifier': 'str',
        'org_identifier': 'str',
        'project_identifier': 'str',
        'trigger_identifier': 'str',
        'pipeline_identifier': 'str',
        'pipeline_execution_id': 'str',
        'exception_occured': 'bool',
        'status': 'str',
        'message': 'str',
        'payload': 'str',
        'event_created_at': 'int',
        'runtime_input': 'str',
        'warning_msg': 'str'
    }

    attribute_map = {
        'event_found': 'eventFound',
        'event_id': 'eventId',
        'account_identifier': 'accountIdentifier',
        'org_identifier': 'orgIdentifier',
        'project_identifier': 'projectIdentifier',
        'trigger_identifier': 'triggerIdentifier',
        'pipeline_identifier': 'pipelineIdentifier',
        'pipeline_execution_id': 'pipelineExecutionId',
        'exception_occured': 'exceptionOccured',
        'status': 'status',
        'message': 'message',
        'payload': 'payload',
        'event_created_at': 'eventCreatedAt',
        'runtime_input': 'runtimeInput',
        'warning_msg': 'warningMsg'
    }

    def __init__(self, event_found=None, event_id=None, account_identifier=None, org_identifier=None, project_identifier=None, trigger_identifier=None, pipeline_identifier=None, pipeline_execution_id=None, exception_occured=None, status=None, message=None, payload=None, event_created_at=None, runtime_input=None, warning_msg=None):  # noqa: E501
        """WebhookEventProcessingDetails - a model defined in Swagger"""  # noqa: E501
        self._event_found = None
        self._event_id = None
        self._account_identifier = None
        self._org_identifier = None
        self._project_identifier = None
        self._trigger_identifier = None
        self._pipeline_identifier = None
        self._pipeline_execution_id = None
        self._exception_occured = None
        self._status = None
        self._message = None
        self._payload = None
        self._event_created_at = None
        self._runtime_input = None
        self._warning_msg = None
        self.discriminator = None
        if event_found is not None:
            self.event_found = event_found
        if event_id is not None:
            self.event_id = event_id
        if account_identifier is not None:
            self.account_identifier = account_identifier
        if org_identifier is not None:
            self.org_identifier = org_identifier
        if project_identifier is not None:
            self.project_identifier = project_identifier
        if trigger_identifier is not None:
            self.trigger_identifier = trigger_identifier
        if pipeline_identifier is not None:
            self.pipeline_identifier = pipeline_identifier
        if pipeline_execution_id is not None:
            self.pipeline_execution_id = pipeline_execution_id
        if exception_occured is not None:
            self.exception_occured = exception_occured
        if status is not None:
            self.status = status
        if message is not None:
            self.message = message
        if payload is not None:
            self.payload = payload
        if event_created_at is not None:
            self.event_created_at = event_created_at
        if runtime_input is not None:
            self.runtime_input = runtime_input
        if warning_msg is not None:
            self.warning_msg = warning_msg

    @property
    def event_found(self):
        """Gets the event_found of this WebhookEventProcessingDetails.  # noqa: E501


        :return: The event_found of this WebhookEventProcessingDetails.  # noqa: E501
        :rtype: bool
        """
        return self._event_found

    @event_found.setter
    def event_found(self, event_found):
        """Sets the event_found of this WebhookEventProcessingDetails.


        :param event_found: The event_found of this WebhookEventProcessingDetails.  # noqa: E501
        :type: bool
        """

        self._event_found = event_found

    @property
    def event_id(self):
        """Gets the event_id of this WebhookEventProcessingDetails.  # noqa: E501


        :return: The event_id of this WebhookEventProcessingDetails.  # noqa: E501
        :rtype: str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """Sets the event_id of this WebhookEventProcessingDetails.


        :param event_id: The event_id of this WebhookEventProcessingDetails.  # noqa: E501
        :type: str
        """

        self._event_id = event_id

    @property
    def account_identifier(self):
        """Gets the account_identifier of this WebhookEventProcessingDetails.  # noqa: E501


        :return: The account_identifier of this WebhookEventProcessingDetails.  # noqa: E501
        :rtype: str
        """
        return self._account_identifier

    @account_identifier.setter
    def account_identifier(self, account_identifier):
        """Sets the account_identifier of this WebhookEventProcessingDetails.


        :param account_identifier: The account_identifier of this WebhookEventProcessingDetails.  # noqa: E501
        :type: str
        """

        self._account_identifier = account_identifier

    @property
    def org_identifier(self):
        """Gets the org_identifier of this WebhookEventProcessingDetails.  # noqa: E501


        :return: The org_identifier of this WebhookEventProcessingDetails.  # noqa: E501
        :rtype: str
        """
        return self._org_identifier

    @org_identifier.setter
    def org_identifier(self, org_identifier):
        """Sets the org_identifier of this WebhookEventProcessingDetails.


        :param org_identifier: The org_identifier of this WebhookEventProcessingDetails.  # noqa: E501
        :type: str
        """

        self._org_identifier = org_identifier

    @property
    def project_identifier(self):
        """Gets the project_identifier of this WebhookEventProcessingDetails.  # noqa: E501


        :return: The project_identifier of this WebhookEventProcessingDetails.  # noqa: E501
        :rtype: str
        """
        return self._project_identifier

    @project_identifier.setter
    def project_identifier(self, project_identifier):
        """Sets the project_identifier of this WebhookEventProcessingDetails.


        :param project_identifier: The project_identifier of this WebhookEventProcessingDetails.  # noqa: E501
        :type: str
        """

        self._project_identifier = project_identifier

    @property
    def trigger_identifier(self):
        """Gets the trigger_identifier of this WebhookEventProcessingDetails.  # noqa: E501


        :return: The trigger_identifier of this WebhookEventProcessingDetails.  # noqa: E501
        :rtype: str
        """
        return self._trigger_identifier

    @trigger_identifier.setter
    def trigger_identifier(self, trigger_identifier):
        """Sets the trigger_identifier of this WebhookEventProcessingDetails.


        :param trigger_identifier: The trigger_identifier of this WebhookEventProcessingDetails.  # noqa: E501
        :type: str
        """

        self._trigger_identifier = trigger_identifier

    @property
    def pipeline_identifier(self):
        """Gets the pipeline_identifier of this WebhookEventProcessingDetails.  # noqa: E501


        :return: The pipeline_identifier of this WebhookEventProcessingDetails.  # noqa: E501
        :rtype: str
        """
        return self._pipeline_identifier

    @pipeline_identifier.setter
    def pipeline_identifier(self, pipeline_identifier):
        """Sets the pipeline_identifier of this WebhookEventProcessingDetails.


        :param pipeline_identifier: The pipeline_identifier of this WebhookEventProcessingDetails.  # noqa: E501
        :type: str
        """

        self._pipeline_identifier = pipeline_identifier

    @property
    def pipeline_execution_id(self):
        """Gets the pipeline_execution_id of this WebhookEventProcessingDetails.  # noqa: E501


        :return: The pipeline_execution_id of this WebhookEventProcessingDetails.  # noqa: E501
        :rtype: str
        """
        return self._pipeline_execution_id

    @pipeline_execution_id.setter
    def pipeline_execution_id(self, pipeline_execution_id):
        """Sets the pipeline_execution_id of this WebhookEventProcessingDetails.


        :param pipeline_execution_id: The pipeline_execution_id of this WebhookEventProcessingDetails.  # noqa: E501
        :type: str
        """

        self._pipeline_execution_id = pipeline_execution_id

    @property
    def exception_occured(self):
        """Gets the exception_occured of this WebhookEventProcessingDetails.  # noqa: E501


        :return: The exception_occured of this WebhookEventProcessingDetails.  # noqa: E501
        :rtype: bool
        """
        return self._exception_occured

    @exception_occured.setter
    def exception_occured(self, exception_occured):
        """Sets the exception_occured of this WebhookEventProcessingDetails.


        :param exception_occured: The exception_occured of this WebhookEventProcessingDetails.  # noqa: E501
        :type: bool
        """

        self._exception_occured = exception_occured

    @property
    def status(self):
        """Gets the status of this WebhookEventProcessingDetails.  # noqa: E501


        :return: The status of this WebhookEventProcessingDetails.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this WebhookEventProcessingDetails.


        :param status: The status of this WebhookEventProcessingDetails.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def message(self):
        """Gets the message of this WebhookEventProcessingDetails.  # noqa: E501


        :return: The message of this WebhookEventProcessingDetails.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this WebhookEventProcessingDetails.


        :param message: The message of this WebhookEventProcessingDetails.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def payload(self):
        """Gets the payload of this WebhookEventProcessingDetails.  # noqa: E501


        :return: The payload of this WebhookEventProcessingDetails.  # noqa: E501
        :rtype: str
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """Sets the payload of this WebhookEventProcessingDetails.


        :param payload: The payload of this WebhookEventProcessingDetails.  # noqa: E501
        :type: str
        """

        self._payload = payload

    @property
    def event_created_at(self):
        """Gets the event_created_at of this WebhookEventProcessingDetails.  # noqa: E501


        :return: The event_created_at of this WebhookEventProcessingDetails.  # noqa: E501
        :rtype: int
        """
        return self._event_created_at

    @event_created_at.setter
    def event_created_at(self, event_created_at):
        """Sets the event_created_at of this WebhookEventProcessingDetails.


        :param event_created_at: The event_created_at of this WebhookEventProcessingDetails.  # noqa: E501
        :type: int
        """

        self._event_created_at = event_created_at

    @property
    def runtime_input(self):
        """Gets the runtime_input of this WebhookEventProcessingDetails.  # noqa: E501


        :return: The runtime_input of this WebhookEventProcessingDetails.  # noqa: E501
        :rtype: str
        """
        return self._runtime_input

    @runtime_input.setter
    def runtime_input(self, runtime_input):
        """Sets the runtime_input of this WebhookEventProcessingDetails.


        :param runtime_input: The runtime_input of this WebhookEventProcessingDetails.  # noqa: E501
        :type: str
        """

        self._runtime_input = runtime_input

    @property
    def warning_msg(self):
        """Gets the warning_msg of this WebhookEventProcessingDetails.  # noqa: E501


        :return: The warning_msg of this WebhookEventProcessingDetails.  # noqa: E501
        :rtype: str
        """
        return self._warning_msg

    @warning_msg.setter
    def warning_msg(self, warning_msg):
        """Sets the warning_msg of this WebhookEventProcessingDetails.


        :param warning_msg: The warning_msg of this WebhookEventProcessingDetails.  # noqa: E501
        :type: str
        """

        self._warning_msg = warning_msg

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
        if issubclass(WebhookEventProcessingDetails, dict):
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
        if not isinstance(other, WebhookEventProcessingDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
