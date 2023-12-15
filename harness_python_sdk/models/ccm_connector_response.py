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

class CcmConnectorResponse(object):
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
        'connector': 'ConnectorInfo',
        'created_at': 'int',
        'last_modified_at': 'int',
        'status': 'CcmConnectorConnectivityDetails',
        'activity_details': 'ConnectorActivityDetails',
        'harness_managed': 'bool',
        'git_details': 'CcmEntityGitDetails',
        'entity_validity_details': 'CcmEntityGitDetails',
        'governance_metadata': 'CcmGovernanceMetadata',
        'is_favorite': 'bool'
    }

    attribute_map = {
        'connector': 'connector',
        'created_at': 'createdAt',
        'last_modified_at': 'lastModifiedAt',
        'status': 'status',
        'activity_details': 'activityDetails',
        'harness_managed': 'harnessManaged',
        'git_details': 'gitDetails',
        'entity_validity_details': 'entityValidityDetails',
        'governance_metadata': 'governanceMetadata',
        'is_favorite': 'isFavorite'
    }

    def __init__(self, connector=None, created_at=None, last_modified_at=None, status=None, activity_details=None, harness_managed=None, git_details=None, entity_validity_details=None, governance_metadata=None, is_favorite=None):  # noqa: E501
        """CcmConnectorResponse - a model defined in Swagger"""  # noqa: E501
        self._connector = None
        self._created_at = None
        self._last_modified_at = None
        self._status = None
        self._activity_details = None
        self._harness_managed = None
        self._git_details = None
        self._entity_validity_details = None
        self._governance_metadata = None
        self._is_favorite = None
        self.discriminator = None
        if connector is not None:
            self.connector = connector
        if created_at is not None:
            self.created_at = created_at
        if last_modified_at is not None:
            self.last_modified_at = last_modified_at
        if status is not None:
            self.status = status
        if activity_details is not None:
            self.activity_details = activity_details
        if harness_managed is not None:
            self.harness_managed = harness_managed
        if git_details is not None:
            self.git_details = git_details
        if entity_validity_details is not None:
            self.entity_validity_details = entity_validity_details
        if governance_metadata is not None:
            self.governance_metadata = governance_metadata
        if is_favorite is not None:
            self.is_favorite = is_favorite

    @property
    def connector(self):
        """Gets the connector of this CcmConnectorResponse.  # noqa: E501


        :return: The connector of this CcmConnectorResponse.  # noqa: E501
        :rtype: ConnectorInfo
        """
        return self._connector

    @connector.setter
    def connector(self, connector):
        """Sets the connector of this CcmConnectorResponse.


        :param connector: The connector of this CcmConnectorResponse.  # noqa: E501
        :type: ConnectorInfo
        """

        self._connector = connector

    @property
    def created_at(self):
        """Gets the created_at of this CcmConnectorResponse.  # noqa: E501

        This is the time at which the Connector was created.  # noqa: E501

        :return: The created_at of this CcmConnectorResponse.  # noqa: E501
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this CcmConnectorResponse.

        This is the time at which the Connector was created.  # noqa: E501

        :param created_at: The created_at of this CcmConnectorResponse.  # noqa: E501
        :type: int
        """

        self._created_at = created_at

    @property
    def last_modified_at(self):
        """Gets the last_modified_at of this CcmConnectorResponse.  # noqa: E501

        This is the time at which the Connector was last modified.  # noqa: E501

        :return: The last_modified_at of this CcmConnectorResponse.  # noqa: E501
        :rtype: int
        """
        return self._last_modified_at

    @last_modified_at.setter
    def last_modified_at(self, last_modified_at):
        """Sets the last_modified_at of this CcmConnectorResponse.

        This is the time at which the Connector was last modified.  # noqa: E501

        :param last_modified_at: The last_modified_at of this CcmConnectorResponse.  # noqa: E501
        :type: int
        """

        self._last_modified_at = last_modified_at

    @property
    def status(self):
        """Gets the status of this CcmConnectorResponse.  # noqa: E501


        :return: The status of this CcmConnectorResponse.  # noqa: E501
        :rtype: CcmConnectorConnectivityDetails
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CcmConnectorResponse.


        :param status: The status of this CcmConnectorResponse.  # noqa: E501
        :type: CcmConnectorConnectivityDetails
        """

        self._status = status

    @property
    def activity_details(self):
        """Gets the activity_details of this CcmConnectorResponse.  # noqa: E501


        :return: The activity_details of this CcmConnectorResponse.  # noqa: E501
        :rtype: ConnectorActivityDetails
        """
        return self._activity_details

    @activity_details.setter
    def activity_details(self, activity_details):
        """Sets the activity_details of this CcmConnectorResponse.


        :param activity_details: The activity_details of this CcmConnectorResponse.  # noqa: E501
        :type: ConnectorActivityDetails
        """

        self._activity_details = activity_details

    @property
    def harness_managed(self):
        """Gets the harness_managed of this CcmConnectorResponse.  # noqa: E501

        This indicates if this Connector is managed by Harness or not. If True, Harness can manage and modify this Connector.  # noqa: E501

        :return: The harness_managed of this CcmConnectorResponse.  # noqa: E501
        :rtype: bool
        """
        return self._harness_managed

    @harness_managed.setter
    def harness_managed(self, harness_managed):
        """Sets the harness_managed of this CcmConnectorResponse.

        This indicates if this Connector is managed by Harness or not. If True, Harness can manage and modify this Connector.  # noqa: E501

        :param harness_managed: The harness_managed of this CcmConnectorResponse.  # noqa: E501
        :type: bool
        """

        self._harness_managed = harness_managed

    @property
    def git_details(self):
        """Gets the git_details of this CcmConnectorResponse.  # noqa: E501


        :return: The git_details of this CcmConnectorResponse.  # noqa: E501
        :rtype: CcmEntityGitDetails
        """
        return self._git_details

    @git_details.setter
    def git_details(self, git_details):
        """Sets the git_details of this CcmConnectorResponse.


        :param git_details: The git_details of this CcmConnectorResponse.  # noqa: E501
        :type: CcmEntityGitDetails
        """

        self._git_details = git_details

    @property
    def entity_validity_details(self):
        """Gets the entity_validity_details of this CcmConnectorResponse.  # noqa: E501


        :return: The entity_validity_details of this CcmConnectorResponse.  # noqa: E501
        :rtype: CcmEntityGitDetails
        """
        return self._entity_validity_details

    @entity_validity_details.setter
    def entity_validity_details(self, entity_validity_details):
        """Sets the entity_validity_details of this CcmConnectorResponse.


        :param entity_validity_details: The entity_validity_details of this CcmConnectorResponse.  # noqa: E501
        :type: CcmEntityGitDetails
        """

        self._entity_validity_details = entity_validity_details

    @property
    def governance_metadata(self):
        """Gets the governance_metadata of this CcmConnectorResponse.  # noqa: E501


        :return: The governance_metadata of this CcmConnectorResponse.  # noqa: E501
        :rtype: CcmGovernanceMetadata
        """
        return self._governance_metadata

    @governance_metadata.setter
    def governance_metadata(self, governance_metadata):
        """Sets the governance_metadata of this CcmConnectorResponse.


        :param governance_metadata: The governance_metadata of this CcmConnectorResponse.  # noqa: E501
        :type: CcmGovernanceMetadata
        """

        self._governance_metadata = governance_metadata

    @property
    def is_favorite(self):
        """Gets the is_favorite of this CcmConnectorResponse.  # noqa: E501


        :return: The is_favorite of this CcmConnectorResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_favorite

    @is_favorite.setter
    def is_favorite(self, is_favorite):
        """Sets the is_favorite of this CcmConnectorResponse.


        :param is_favorite: The is_favorite of this CcmConnectorResponse.  # noqa: E501
        :type: bool
        """

        self._is_favorite = is_favorite

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
        if issubclass(CcmConnectorResponse, dict):
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
        if not isinstance(other, CcmConnectorResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
