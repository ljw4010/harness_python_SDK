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

class NGTriggerEventHistoryDTO(object):
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
        'trigger_identifier': 'str',
        'account_id': 'str',
        'event_correlation_id': 'str',
        'payload': 'str',
        'event_created_at': 'int',
        'final_status': 'str',
        'message': 'str',
        'exception_occurred': 'bool',
        'created_at': 'int',
        'trigger_event_status': 'TriggerEventStatus',
        'org_identifier': 'str',
        'project_identifier': 'str',
        'target_identifier': 'str',
        'target_execution_summary': 'TargetExecutionSummary',
        'type': 'str',
        'ng_trigger_event_info': 'NGTriggerEventInfo'
    }

    attribute_map = {
        'trigger_identifier': 'triggerIdentifier',
        'account_id': 'accountId',
        'event_correlation_id': 'eventCorrelationId',
        'payload': 'payload',
        'event_created_at': 'eventCreatedAt',
        'final_status': 'finalStatus',
        'message': 'message',
        'exception_occurred': 'exceptionOccurred',
        'created_at': 'createdAt',
        'trigger_event_status': 'triggerEventStatus',
        'org_identifier': 'orgIdentifier',
        'project_identifier': 'projectIdentifier',
        'target_identifier': 'targetIdentifier',
        'target_execution_summary': 'targetExecutionSummary',
        'type': 'type',
        'ng_trigger_event_info': 'ngTriggerEventInfo'
    }

    def __init__(self, trigger_identifier=None, account_id=None, event_correlation_id=None, payload=None, event_created_at=None, final_status=None, message=None, exception_occurred=None, created_at=None, trigger_event_status=None, org_identifier=None, project_identifier=None, target_identifier=None, target_execution_summary=None, type=None, ng_trigger_event_info=None):  # noqa: E501
        """NGTriggerEventHistoryDTO - a model defined in Swagger"""  # noqa: E501
        self._trigger_identifier = None
        self._account_id = None
        self._event_correlation_id = None
        self._payload = None
        self._event_created_at = None
        self._final_status = None
        self._message = None
        self._exception_occurred = None
        self._created_at = None
        self._trigger_event_status = None
        self._org_identifier = None
        self._project_identifier = None
        self._target_identifier = None
        self._target_execution_summary = None
        self._type = None
        self._ng_trigger_event_info = None
        self.discriminator = None
        if trigger_identifier is not None:
            self.trigger_identifier = trigger_identifier
        if account_id is not None:
            self.account_id = account_id
        if event_correlation_id is not None:
            self.event_correlation_id = event_correlation_id
        if payload is not None:
            self.payload = payload
        if event_created_at is not None:
            self.event_created_at = event_created_at
        if final_status is not None:
            self.final_status = final_status
        if message is not None:
            self.message = message
        if exception_occurred is not None:
            self.exception_occurred = exception_occurred
        if created_at is not None:
            self.created_at = created_at
        if trigger_event_status is not None:
            self.trigger_event_status = trigger_event_status
        if org_identifier is not None:
            self.org_identifier = org_identifier
        if project_identifier is not None:
            self.project_identifier = project_identifier
        if target_identifier is not None:
            self.target_identifier = target_identifier
        if target_execution_summary is not None:
            self.target_execution_summary = target_execution_summary
        if type is not None:
            self.type = type
        if ng_trigger_event_info is not None:
            self.ng_trigger_event_info = ng_trigger_event_info

    @property
    def trigger_identifier(self):
        """Gets the trigger_identifier of this NGTriggerEventHistoryDTO.  # noqa: E501


        :return: The trigger_identifier of this NGTriggerEventHistoryDTO.  # noqa: E501
        :rtype: str
        """
        return self._trigger_identifier

    @trigger_identifier.setter
    def trigger_identifier(self, trigger_identifier):
        """Sets the trigger_identifier of this NGTriggerEventHistoryDTO.


        :param trigger_identifier: The trigger_identifier of this NGTriggerEventHistoryDTO.  # noqa: E501
        :type: str
        """

        self._trigger_identifier = trigger_identifier

    @property
    def account_id(self):
        """Gets the account_id of this NGTriggerEventHistoryDTO.  # noqa: E501


        :return: The account_id of this NGTriggerEventHistoryDTO.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this NGTriggerEventHistoryDTO.


        :param account_id: The account_id of this NGTriggerEventHistoryDTO.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def event_correlation_id(self):
        """Gets the event_correlation_id of this NGTriggerEventHistoryDTO.  # noqa: E501


        :return: The event_correlation_id of this NGTriggerEventHistoryDTO.  # noqa: E501
        :rtype: str
        """
        return self._event_correlation_id

    @event_correlation_id.setter
    def event_correlation_id(self, event_correlation_id):
        """Sets the event_correlation_id of this NGTriggerEventHistoryDTO.


        :param event_correlation_id: The event_correlation_id of this NGTriggerEventHistoryDTO.  # noqa: E501
        :type: str
        """

        self._event_correlation_id = event_correlation_id

    @property
    def payload(self):
        """Gets the payload of this NGTriggerEventHistoryDTO.  # noqa: E501


        :return: The payload of this NGTriggerEventHistoryDTO.  # noqa: E501
        :rtype: str
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """Sets the payload of this NGTriggerEventHistoryDTO.


        :param payload: The payload of this NGTriggerEventHistoryDTO.  # noqa: E501
        :type: str
        """

        self._payload = payload

    @property
    def event_created_at(self):
        """Gets the event_created_at of this NGTriggerEventHistoryDTO.  # noqa: E501


        :return: The event_created_at of this NGTriggerEventHistoryDTO.  # noqa: E501
        :rtype: int
        """
        return self._event_created_at

    @event_created_at.setter
    def event_created_at(self, event_created_at):
        """Sets the event_created_at of this NGTriggerEventHistoryDTO.


        :param event_created_at: The event_created_at of this NGTriggerEventHistoryDTO.  # noqa: E501
        :type: int
        """

        self._event_created_at = event_created_at

    @property
    def final_status(self):
        """Gets the final_status of this NGTriggerEventHistoryDTO.  # noqa: E501


        :return: The final_status of this NGTriggerEventHistoryDTO.  # noqa: E501
        :rtype: str
        """
        return self._final_status

    @final_status.setter
    def final_status(self, final_status):
        """Sets the final_status of this NGTriggerEventHistoryDTO.


        :param final_status: The final_status of this NGTriggerEventHistoryDTO.  # noqa: E501
        :type: str
        """
        allowed_values = ["SCM_SERVICE_CONNECTION_FAILED", "INVALID_PAYLOAD", "TRIGGER_DID_NOT_MATCH_EVENT_CONDITION", "TRIGGER_DID_NOT_MATCH_METADATA_CONDITION", "TRIGGER_DID_NOT_MATCH_ARTIFACT_JEXL_CONDITION", "NO_MATCHING_TRIGGER_FOR_REPO", "NO_MATCHING_TRIGGER_FOR_EVENT_ACTION", "NO_MATCHING_TRIGGER_FOR_METADATA_CONDITIONS", "NO_MATCHING_TRIGGER_FOR_PAYLOAD_CONDITIONS", "NO_MATCHING_TRIGGER_FOR_JEXL_CONDITIONS", "NO_MATCHING_TRIGGER_FOR_HEADER_CONDITIONS", "INVALID_RUNTIME_INPUT_YAML", "TARGET_DID_NOT_EXECUTE", "TARGET_EXECUTION_REQUESTED", "NO_ENABLED_CUSTOM_TRIGGER_FOUND", "NO_ENABLED_CUSTOM_TRIGGER_FOUND_FOR_ACCOUNT", "NO_ENABLED_TRIGGER_FOR_PROJECT", "NO_ENABLED_TRIGGER_FOR_ACCOUNT", "NO_ENABLED_TRIGGER_FOR_SOURCEREPO_TYPE", "NO_ENABLED_TRIGGER_FOR_ACCOUNT_SOURCE_REPO", "NO_MATCHING_TRIGGER_FOR_FILEPATH_CONDITIONS", "FAILED_TO_FETCH_PR_DETAILS", "EXCEPTION_WHILE_PROCESSING", "TRIGGER_CONFIRMATION_SUCCESSFUL", "TRIGGER_CONFIRMATION_FAILED", "TRIGGER_AUTHENTICATION_FAILED", "VALIDATION_FAILED_FOR_TRIGGER", "ALL_MAPPED_TRIGGER_FAILED_VALIDATION_FOR_POLLING_EVENT", "NO_MATCHING_TRIGGER_FOR_FOR_EVENT_SIGNATURES", "NO_MATCHING_TRIGGER_FOR_FOR_EVENT_CONDITION", "POLLING_EVENT_WITH_NO_VERSIONS", "NEW_ARTIFACT_EVENT_PROCESSED", "NEW_MANIFEST_EVENT_PROCESSED"]  # noqa: E501
        if final_status not in allowed_values:
            raise ValueError(
                "Invalid value for `final_status` ({0}), must be one of {1}"  # noqa: E501
                .format(final_status, allowed_values)
            )

        self._final_status = final_status

    @property
    def message(self):
        """Gets the message of this NGTriggerEventHistoryDTO.  # noqa: E501


        :return: The message of this NGTriggerEventHistoryDTO.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this NGTriggerEventHistoryDTO.


        :param message: The message of this NGTriggerEventHistoryDTO.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def exception_occurred(self):
        """Gets the exception_occurred of this NGTriggerEventHistoryDTO.  # noqa: E501


        :return: The exception_occurred of this NGTriggerEventHistoryDTO.  # noqa: E501
        :rtype: bool
        """
        return self._exception_occurred

    @exception_occurred.setter
    def exception_occurred(self, exception_occurred):
        """Sets the exception_occurred of this NGTriggerEventHistoryDTO.


        :param exception_occurred: The exception_occurred of this NGTriggerEventHistoryDTO.  # noqa: E501
        :type: bool
        """

        self._exception_occurred = exception_occurred

    @property
    def created_at(self):
        """Gets the created_at of this NGTriggerEventHistoryDTO.  # noqa: E501


        :return: The created_at of this NGTriggerEventHistoryDTO.  # noqa: E501
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this NGTriggerEventHistoryDTO.


        :param created_at: The created_at of this NGTriggerEventHistoryDTO.  # noqa: E501
        :type: int
        """

        self._created_at = created_at

    @property
    def trigger_event_status(self):
        """Gets the trigger_event_status of this NGTriggerEventHistoryDTO.  # noqa: E501


        :return: The trigger_event_status of this NGTriggerEventHistoryDTO.  # noqa: E501
        :rtype: TriggerEventStatus
        """
        return self._trigger_event_status

    @trigger_event_status.setter
    def trigger_event_status(self, trigger_event_status):
        """Sets the trigger_event_status of this NGTriggerEventHistoryDTO.


        :param trigger_event_status: The trigger_event_status of this NGTriggerEventHistoryDTO.  # noqa: E501
        :type: TriggerEventStatus
        """

        self._trigger_event_status = trigger_event_status

    @property
    def org_identifier(self):
        """Gets the org_identifier of this NGTriggerEventHistoryDTO.  # noqa: E501


        :return: The org_identifier of this NGTriggerEventHistoryDTO.  # noqa: E501
        :rtype: str
        """
        return self._org_identifier

    @org_identifier.setter
    def org_identifier(self, org_identifier):
        """Sets the org_identifier of this NGTriggerEventHistoryDTO.


        :param org_identifier: The org_identifier of this NGTriggerEventHistoryDTO.  # noqa: E501
        :type: str
        """

        self._org_identifier = org_identifier

    @property
    def project_identifier(self):
        """Gets the project_identifier of this NGTriggerEventHistoryDTO.  # noqa: E501


        :return: The project_identifier of this NGTriggerEventHistoryDTO.  # noqa: E501
        :rtype: str
        """
        return self._project_identifier

    @project_identifier.setter
    def project_identifier(self, project_identifier):
        """Sets the project_identifier of this NGTriggerEventHistoryDTO.


        :param project_identifier: The project_identifier of this NGTriggerEventHistoryDTO.  # noqa: E501
        :type: str
        """

        self._project_identifier = project_identifier

    @property
    def target_identifier(self):
        """Gets the target_identifier of this NGTriggerEventHistoryDTO.  # noqa: E501


        :return: The target_identifier of this NGTriggerEventHistoryDTO.  # noqa: E501
        :rtype: str
        """
        return self._target_identifier

    @target_identifier.setter
    def target_identifier(self, target_identifier):
        """Sets the target_identifier of this NGTriggerEventHistoryDTO.


        :param target_identifier: The target_identifier of this NGTriggerEventHistoryDTO.  # noqa: E501
        :type: str
        """

        self._target_identifier = target_identifier

    @property
    def target_execution_summary(self):
        """Gets the target_execution_summary of this NGTriggerEventHistoryDTO.  # noqa: E501


        :return: The target_execution_summary of this NGTriggerEventHistoryDTO.  # noqa: E501
        :rtype: TargetExecutionSummary
        """
        return self._target_execution_summary

    @target_execution_summary.setter
    def target_execution_summary(self, target_execution_summary):
        """Sets the target_execution_summary of this NGTriggerEventHistoryDTO.


        :param target_execution_summary: The target_execution_summary of this NGTriggerEventHistoryDTO.  # noqa: E501
        :type: TargetExecutionSummary
        """

        self._target_execution_summary = target_execution_summary

    @property
    def type(self):
        """Gets the type of this NGTriggerEventHistoryDTO.  # noqa: E501


        :return: The type of this NGTriggerEventHistoryDTO.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this NGTriggerEventHistoryDTO.


        :param type: The type of this NGTriggerEventHistoryDTO.  # noqa: E501
        :type: str
        """
        allowed_values = ["Webhook", "Artifact", "Manifest", "Scheduled", "MultiRegionArtifact"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def ng_trigger_event_info(self):
        """Gets the ng_trigger_event_info of this NGTriggerEventHistoryDTO.  # noqa: E501


        :return: The ng_trigger_event_info of this NGTriggerEventHistoryDTO.  # noqa: E501
        :rtype: NGTriggerEventInfo
        """
        return self._ng_trigger_event_info

    @ng_trigger_event_info.setter
    def ng_trigger_event_info(self, ng_trigger_event_info):
        """Sets the ng_trigger_event_info of this NGTriggerEventHistoryDTO.


        :param ng_trigger_event_info: The ng_trigger_event_info of this NGTriggerEventHistoryDTO.  # noqa: E501
        :type: NGTriggerEventInfo
        """

        self._ng_trigger_event_info = ng_trigger_event_info

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
        if issubclass(NGTriggerEventHistoryDTO, dict):
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
        if not isinstance(other, NGTriggerEventHistoryDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
