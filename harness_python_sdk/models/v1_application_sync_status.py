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

class V1ApplicationSyncStatus(object):
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
        'account_identifier': 'str',
        'project_identifier': 'str',
        'org_identifier': 'str',
        'agent_identifier': 'str',
        'application_name': 'str',
        'created_at': 'str',
        'last_modified_at': 'str',
        'operation_state': 'ApplicationsOperationState',
        'req_identifier': 'str',
        'last_known_revision_id': 'str',
        'synced_by': 'V1User'
    }

    attribute_map = {
        'account_identifier': 'accountIdentifier',
        'project_identifier': 'projectIdentifier',
        'org_identifier': 'orgIdentifier',
        'agent_identifier': 'agentIdentifier',
        'application_name': 'applicationName',
        'created_at': 'createdAt',
        'last_modified_at': 'lastModifiedAt',
        'operation_state': 'operationState',
        'req_identifier': 'reqIdentifier',
        'last_known_revision_id': 'lastKnownRevisionId',
        'synced_by': 'syncedBy'
    }

    def __init__(self, account_identifier=None, project_identifier=None, org_identifier=None, agent_identifier=None, application_name=None, created_at=None, last_modified_at=None, operation_state=None, req_identifier=None, last_known_revision_id=None, synced_by=None):  # noqa: E501
        """V1ApplicationSyncStatus - a model defined in Swagger"""  # noqa: E501
        self._account_identifier = None
        self._project_identifier = None
        self._org_identifier = None
        self._agent_identifier = None
        self._application_name = None
        self._created_at = None
        self._last_modified_at = None
        self._operation_state = None
        self._req_identifier = None
        self._last_known_revision_id = None
        self._synced_by = None
        self.discriminator = None
        if account_identifier is not None:
            self.account_identifier = account_identifier
        if project_identifier is not None:
            self.project_identifier = project_identifier
        if org_identifier is not None:
            self.org_identifier = org_identifier
        if agent_identifier is not None:
            self.agent_identifier = agent_identifier
        if application_name is not None:
            self.application_name = application_name
        if created_at is not None:
            self.created_at = created_at
        if last_modified_at is not None:
            self.last_modified_at = last_modified_at
        if operation_state is not None:
            self.operation_state = operation_state
        if req_identifier is not None:
            self.req_identifier = req_identifier
        if last_known_revision_id is not None:
            self.last_known_revision_id = last_known_revision_id
        if synced_by is not None:
            self.synced_by = synced_by

    @property
    def account_identifier(self):
        """Gets the account_identifier of this V1ApplicationSyncStatus.  # noqa: E501

        Account Identifier for the Entity.  # noqa: E501

        :return: The account_identifier of this V1ApplicationSyncStatus.  # noqa: E501
        :rtype: str
        """
        return self._account_identifier

    @account_identifier.setter
    def account_identifier(self, account_identifier):
        """Sets the account_identifier of this V1ApplicationSyncStatus.

        Account Identifier for the Entity.  # noqa: E501

        :param account_identifier: The account_identifier of this V1ApplicationSyncStatus.  # noqa: E501
        :type: str
        """

        self._account_identifier = account_identifier

    @property
    def project_identifier(self):
        """Gets the project_identifier of this V1ApplicationSyncStatus.  # noqa: E501

        Project Identifier for the Entity.  # noqa: E501

        :return: The project_identifier of this V1ApplicationSyncStatus.  # noqa: E501
        :rtype: str
        """
        return self._project_identifier

    @project_identifier.setter
    def project_identifier(self, project_identifier):
        """Sets the project_identifier of this V1ApplicationSyncStatus.

        Project Identifier for the Entity.  # noqa: E501

        :param project_identifier: The project_identifier of this V1ApplicationSyncStatus.  # noqa: E501
        :type: str
        """

        self._project_identifier = project_identifier

    @property
    def org_identifier(self):
        """Gets the org_identifier of this V1ApplicationSyncStatus.  # noqa: E501

        Organization Identifier for the Entity.  # noqa: E501

        :return: The org_identifier of this V1ApplicationSyncStatus.  # noqa: E501
        :rtype: str
        """
        return self._org_identifier

    @org_identifier.setter
    def org_identifier(self, org_identifier):
        """Sets the org_identifier of this V1ApplicationSyncStatus.

        Organization Identifier for the Entity.  # noqa: E501

        :param org_identifier: The org_identifier of this V1ApplicationSyncStatus.  # noqa: E501
        :type: str
        """

        self._org_identifier = org_identifier

    @property
    def agent_identifier(self):
        """Gets the agent_identifier of this V1ApplicationSyncStatus.  # noqa: E501

        Agent identifier for entity.  # noqa: E501

        :return: The agent_identifier of this V1ApplicationSyncStatus.  # noqa: E501
        :rtype: str
        """
        return self._agent_identifier

    @agent_identifier.setter
    def agent_identifier(self, agent_identifier):
        """Sets the agent_identifier of this V1ApplicationSyncStatus.

        Agent identifier for entity.  # noqa: E501

        :param agent_identifier: The agent_identifier of this V1ApplicationSyncStatus.  # noqa: E501
        :type: str
        """

        self._agent_identifier = agent_identifier

    @property
    def application_name(self):
        """Gets the application_name of this V1ApplicationSyncStatus.  # noqa: E501


        :return: The application_name of this V1ApplicationSyncStatus.  # noqa: E501
        :rtype: str
        """
        return self._application_name

    @application_name.setter
    def application_name(self, application_name):
        """Sets the application_name of this V1ApplicationSyncStatus.


        :param application_name: The application_name of this V1ApplicationSyncStatus.  # noqa: E501
        :type: str
        """

        self._application_name = application_name

    @property
    def created_at(self):
        """Gets the created_at of this V1ApplicationSyncStatus.  # noqa: E501


        :return: The created_at of this V1ApplicationSyncStatus.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this V1ApplicationSyncStatus.


        :param created_at: The created_at of this V1ApplicationSyncStatus.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def last_modified_at(self):
        """Gets the last_modified_at of this V1ApplicationSyncStatus.  # noqa: E501


        :return: The last_modified_at of this V1ApplicationSyncStatus.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_at

    @last_modified_at.setter
    def last_modified_at(self, last_modified_at):
        """Sets the last_modified_at of this V1ApplicationSyncStatus.


        :param last_modified_at: The last_modified_at of this V1ApplicationSyncStatus.  # noqa: E501
        :type: str
        """

        self._last_modified_at = last_modified_at

    @property
    def operation_state(self):
        """Gets the operation_state of this V1ApplicationSyncStatus.  # noqa: E501


        :return: The operation_state of this V1ApplicationSyncStatus.  # noqa: E501
        :rtype: ApplicationsOperationState
        """
        return self._operation_state

    @operation_state.setter
    def operation_state(self, operation_state):
        """Sets the operation_state of this V1ApplicationSyncStatus.


        :param operation_state: The operation_state of this V1ApplicationSyncStatus.  # noqa: E501
        :type: ApplicationsOperationState
        """

        self._operation_state = operation_state

    @property
    def req_identifier(self):
        """Gets the req_identifier of this V1ApplicationSyncStatus.  # noqa: E501


        :return: The req_identifier of this V1ApplicationSyncStatus.  # noqa: E501
        :rtype: str
        """
        return self._req_identifier

    @req_identifier.setter
    def req_identifier(self, req_identifier):
        """Sets the req_identifier of this V1ApplicationSyncStatus.


        :param req_identifier: The req_identifier of this V1ApplicationSyncStatus.  # noqa: E501
        :type: str
        """

        self._req_identifier = req_identifier

    @property
    def last_known_revision_id(self):
        """Gets the last_known_revision_id of this V1ApplicationSyncStatus.  # noqa: E501


        :return: The last_known_revision_id of this V1ApplicationSyncStatus.  # noqa: E501
        :rtype: str
        """
        return self._last_known_revision_id

    @last_known_revision_id.setter
    def last_known_revision_id(self, last_known_revision_id):
        """Sets the last_known_revision_id of this V1ApplicationSyncStatus.


        :param last_known_revision_id: The last_known_revision_id of this V1ApplicationSyncStatus.  # noqa: E501
        :type: str
        """

        self._last_known_revision_id = last_known_revision_id

    @property
    def synced_by(self):
        """Gets the synced_by of this V1ApplicationSyncStatus.  # noqa: E501


        :return: The synced_by of this V1ApplicationSyncStatus.  # noqa: E501
        :rtype: V1User
        """
        return self._synced_by

    @synced_by.setter
    def synced_by(self, synced_by):
        """Sets the synced_by of this V1ApplicationSyncStatus.


        :param synced_by: The synced_by of this V1ApplicationSyncStatus.  # noqa: E501
        :type: V1User
        """

        self._synced_by = synced_by

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
        if issubclass(V1ApplicationSyncStatus, dict):
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
        if not isinstance(other, V1ApplicationSyncStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
