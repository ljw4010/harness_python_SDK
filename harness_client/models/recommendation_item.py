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

class RecommendationItem(object):
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
        'cluster_name': 'str',
        'namespace': 'str',
        'resource_name': 'str',
        'monthly_saving': 'float',
        'monthly_cost': 'float',
        'is_valid': 'bool',
        'last_processed_at': 'datetime',
        'resource_type': 'str',
        'recommendation_state': 'str',
        'jira_connector_ref': 'str',
        'jira_issue_key': 'str',
        'jira_status': 'str',
        'servicenow_connector_ref': 'str',
        'servicenow_issue_key': 'str',
        'servicenow_issue_status': 'str',
        'recommendation_details': 'RecommendationDetailsDTO',
        'perspective_id': 'str',
        'perspective_name': 'str',
        'cloud_provider': 'str',
        'governance_rule_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'cluster_name': 'clusterName',
        'namespace': 'namespace',
        'resource_name': 'resourceName',
        'monthly_saving': 'monthlySaving',
        'monthly_cost': 'monthlyCost',
        'is_valid': 'isValid',
        'last_processed_at': 'lastProcessedAt',
        'resource_type': 'resourceType',
        'recommendation_state': 'recommendationState',
        'jira_connector_ref': 'jiraConnectorRef',
        'jira_issue_key': 'jiraIssueKey',
        'jira_status': 'jiraStatus',
        'servicenow_connector_ref': 'servicenowConnectorRef',
        'servicenow_issue_key': 'servicenowIssueKey',
        'servicenow_issue_status': 'servicenowIssueStatus',
        'recommendation_details': 'recommendationDetails',
        'perspective_id': 'perspectiveId',
        'perspective_name': 'perspectiveName',
        'cloud_provider': 'cloudProvider',
        'governance_rule_id': 'governanceRuleId'
    }

    def __init__(self, id=None, cluster_name=None, namespace=None, resource_name=None, monthly_saving=None, monthly_cost=None, is_valid=None, last_processed_at=None, resource_type=None, recommendation_state=None, jira_connector_ref=None, jira_issue_key=None, jira_status=None, servicenow_connector_ref=None, servicenow_issue_key=None, servicenow_issue_status=None, recommendation_details=None, perspective_id=None, perspective_name=None, cloud_provider=None, governance_rule_id=None):  # noqa: E501
        """RecommendationItem - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._cluster_name = None
        self._namespace = None
        self._resource_name = None
        self._monthly_saving = None
        self._monthly_cost = None
        self._is_valid = None
        self._last_processed_at = None
        self._resource_type = None
        self._recommendation_state = None
        self._jira_connector_ref = None
        self._jira_issue_key = None
        self._jira_status = None
        self._servicenow_connector_ref = None
        self._servicenow_issue_key = None
        self._servicenow_issue_status = None
        self._recommendation_details = None
        self._perspective_id = None
        self._perspective_name = None
        self._cloud_provider = None
        self._governance_rule_id = None
        self.discriminator = None
        self.id = id
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if namespace is not None:
            self.namespace = namespace
        if resource_name is not None:
            self.resource_name = resource_name
        if monthly_saving is not None:
            self.monthly_saving = monthly_saving
        if monthly_cost is not None:
            self.monthly_cost = monthly_cost
        if is_valid is not None:
            self.is_valid = is_valid
        if last_processed_at is not None:
            self.last_processed_at = last_processed_at
        self.resource_type = resource_type
        if recommendation_state is not None:
            self.recommendation_state = recommendation_state
        if jira_connector_ref is not None:
            self.jira_connector_ref = jira_connector_ref
        if jira_issue_key is not None:
            self.jira_issue_key = jira_issue_key
        if jira_status is not None:
            self.jira_status = jira_status
        if servicenow_connector_ref is not None:
            self.servicenow_connector_ref = servicenow_connector_ref
        if servicenow_issue_key is not None:
            self.servicenow_issue_key = servicenow_issue_key
        if servicenow_issue_status is not None:
            self.servicenow_issue_status = servicenow_issue_status
        if recommendation_details is not None:
            self.recommendation_details = recommendation_details
        if perspective_id is not None:
            self.perspective_id = perspective_id
        if perspective_name is not None:
            self.perspective_name = perspective_name
        if cloud_provider is not None:
            self.cloud_provider = cloud_provider
        if governance_rule_id is not None:
            self.governance_rule_id = governance_rule_id

    @property
    def id(self):
        """Gets the id of this RecommendationItem.  # noqa: E501


        :return: The id of this RecommendationItem.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RecommendationItem.


        :param id: The id of this RecommendationItem.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def cluster_name(self):
        """Gets the cluster_name of this RecommendationItem.  # noqa: E501


        :return: The cluster_name of this RecommendationItem.  # noqa: E501
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        """Sets the cluster_name of this RecommendationItem.


        :param cluster_name: The cluster_name of this RecommendationItem.  # noqa: E501
        :type: str
        """

        self._cluster_name = cluster_name

    @property
    def namespace(self):
        """Gets the namespace of this RecommendationItem.  # noqa: E501


        :return: The namespace of this RecommendationItem.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this RecommendationItem.


        :param namespace: The namespace of this RecommendationItem.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

    @property
    def resource_name(self):
        """Gets the resource_name of this RecommendationItem.  # noqa: E501


        :return: The resource_name of this RecommendationItem.  # noqa: E501
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this RecommendationItem.


        :param resource_name: The resource_name of this RecommendationItem.  # noqa: E501
        :type: str
        """

        self._resource_name = resource_name

    @property
    def monthly_saving(self):
        """Gets the monthly_saving of this RecommendationItem.  # noqa: E501


        :return: The monthly_saving of this RecommendationItem.  # noqa: E501
        :rtype: float
        """
        return self._monthly_saving

    @monthly_saving.setter
    def monthly_saving(self, monthly_saving):
        """Sets the monthly_saving of this RecommendationItem.


        :param monthly_saving: The monthly_saving of this RecommendationItem.  # noqa: E501
        :type: float
        """

        self._monthly_saving = monthly_saving

    @property
    def monthly_cost(self):
        """Gets the monthly_cost of this RecommendationItem.  # noqa: E501


        :return: The monthly_cost of this RecommendationItem.  # noqa: E501
        :rtype: float
        """
        return self._monthly_cost

    @monthly_cost.setter
    def monthly_cost(self, monthly_cost):
        """Sets the monthly_cost of this RecommendationItem.


        :param monthly_cost: The monthly_cost of this RecommendationItem.  # noqa: E501
        :type: float
        """

        self._monthly_cost = monthly_cost

    @property
    def is_valid(self):
        """Gets the is_valid of this RecommendationItem.  # noqa: E501


        :return: The is_valid of this RecommendationItem.  # noqa: E501
        :rtype: bool
        """
        return self._is_valid

    @is_valid.setter
    def is_valid(self, is_valid):
        """Sets the is_valid of this RecommendationItem.


        :param is_valid: The is_valid of this RecommendationItem.  # noqa: E501
        :type: bool
        """

        self._is_valid = is_valid

    @property
    def last_processed_at(self):
        """Gets the last_processed_at of this RecommendationItem.  # noqa: E501


        :return: The last_processed_at of this RecommendationItem.  # noqa: E501
        :rtype: datetime
        """
        return self._last_processed_at

    @last_processed_at.setter
    def last_processed_at(self, last_processed_at):
        """Sets the last_processed_at of this RecommendationItem.


        :param last_processed_at: The last_processed_at of this RecommendationItem.  # noqa: E501
        :type: datetime
        """

        self._last_processed_at = last_processed_at

    @property
    def resource_type(self):
        """Gets the resource_type of this RecommendationItem.  # noqa: E501


        :return: The resource_type of this RecommendationItem.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this RecommendationItem.


        :param resource_type: The resource_type of this RecommendationItem.  # noqa: E501
        :type: str
        """
        if resource_type is None:
            raise ValueError("Invalid value for `resource_type`, must not be `None`")  # noqa: E501
        allowed_values = ["WORKLOAD", "NODE_POOL", "ECS_SERVICE", "EC2_INSTANCE", "GOVERNANCE", "AZURE_INSTANCE"]  # noqa: E501
        if resource_type not in allowed_values:
            raise ValueError(
                "Invalid value for `resource_type` ({0}), must be one of {1}"  # noqa: E501
                .format(resource_type, allowed_values)
            )

        self._resource_type = resource_type

    @property
    def recommendation_state(self):
        """Gets the recommendation_state of this RecommendationItem.  # noqa: E501


        :return: The recommendation_state of this RecommendationItem.  # noqa: E501
        :rtype: str
        """
        return self._recommendation_state

    @recommendation_state.setter
    def recommendation_state(self, recommendation_state):
        """Sets the recommendation_state of this RecommendationItem.


        :param recommendation_state: The recommendation_state of this RecommendationItem.  # noqa: E501
        :type: str
        """
        allowed_values = ["OPEN", "APPLIED", "IGNORED"]  # noqa: E501
        if recommendation_state not in allowed_values:
            raise ValueError(
                "Invalid value for `recommendation_state` ({0}), must be one of {1}"  # noqa: E501
                .format(recommendation_state, allowed_values)
            )

        self._recommendation_state = recommendation_state

    @property
    def jira_connector_ref(self):
        """Gets the jira_connector_ref of this RecommendationItem.  # noqa: E501


        :return: The jira_connector_ref of this RecommendationItem.  # noqa: E501
        :rtype: str
        """
        return self._jira_connector_ref

    @jira_connector_ref.setter
    def jira_connector_ref(self, jira_connector_ref):
        """Sets the jira_connector_ref of this RecommendationItem.


        :param jira_connector_ref: The jira_connector_ref of this RecommendationItem.  # noqa: E501
        :type: str
        """

        self._jira_connector_ref = jira_connector_ref

    @property
    def jira_issue_key(self):
        """Gets the jira_issue_key of this RecommendationItem.  # noqa: E501


        :return: The jira_issue_key of this RecommendationItem.  # noqa: E501
        :rtype: str
        """
        return self._jira_issue_key

    @jira_issue_key.setter
    def jira_issue_key(self, jira_issue_key):
        """Sets the jira_issue_key of this RecommendationItem.


        :param jira_issue_key: The jira_issue_key of this RecommendationItem.  # noqa: E501
        :type: str
        """

        self._jira_issue_key = jira_issue_key

    @property
    def jira_status(self):
        """Gets the jira_status of this RecommendationItem.  # noqa: E501


        :return: The jira_status of this RecommendationItem.  # noqa: E501
        :rtype: str
        """
        return self._jira_status

    @jira_status.setter
    def jira_status(self, jira_status):
        """Sets the jira_status of this RecommendationItem.


        :param jira_status: The jira_status of this RecommendationItem.  # noqa: E501
        :type: str
        """

        self._jira_status = jira_status

    @property
    def servicenow_connector_ref(self):
        """Gets the servicenow_connector_ref of this RecommendationItem.  # noqa: E501


        :return: The servicenow_connector_ref of this RecommendationItem.  # noqa: E501
        :rtype: str
        """
        return self._servicenow_connector_ref

    @servicenow_connector_ref.setter
    def servicenow_connector_ref(self, servicenow_connector_ref):
        """Sets the servicenow_connector_ref of this RecommendationItem.


        :param servicenow_connector_ref: The servicenow_connector_ref of this RecommendationItem.  # noqa: E501
        :type: str
        """

        self._servicenow_connector_ref = servicenow_connector_ref

    @property
    def servicenow_issue_key(self):
        """Gets the servicenow_issue_key of this RecommendationItem.  # noqa: E501


        :return: The servicenow_issue_key of this RecommendationItem.  # noqa: E501
        :rtype: str
        """
        return self._servicenow_issue_key

    @servicenow_issue_key.setter
    def servicenow_issue_key(self, servicenow_issue_key):
        """Sets the servicenow_issue_key of this RecommendationItem.


        :param servicenow_issue_key: The servicenow_issue_key of this RecommendationItem.  # noqa: E501
        :type: str
        """

        self._servicenow_issue_key = servicenow_issue_key

    @property
    def servicenow_issue_status(self):
        """Gets the servicenow_issue_status of this RecommendationItem.  # noqa: E501


        :return: The servicenow_issue_status of this RecommendationItem.  # noqa: E501
        :rtype: str
        """
        return self._servicenow_issue_status

    @servicenow_issue_status.setter
    def servicenow_issue_status(self, servicenow_issue_status):
        """Sets the servicenow_issue_status of this RecommendationItem.


        :param servicenow_issue_status: The servicenow_issue_status of this RecommendationItem.  # noqa: E501
        :type: str
        """

        self._servicenow_issue_status = servicenow_issue_status

    @property
    def recommendation_details(self):
        """Gets the recommendation_details of this RecommendationItem.  # noqa: E501


        :return: The recommendation_details of this RecommendationItem.  # noqa: E501
        :rtype: RecommendationDetailsDTO
        """
        return self._recommendation_details

    @recommendation_details.setter
    def recommendation_details(self, recommendation_details):
        """Sets the recommendation_details of this RecommendationItem.


        :param recommendation_details: The recommendation_details of this RecommendationItem.  # noqa: E501
        :type: RecommendationDetailsDTO
        """

        self._recommendation_details = recommendation_details

    @property
    def perspective_id(self):
        """Gets the perspective_id of this RecommendationItem.  # noqa: E501


        :return: The perspective_id of this RecommendationItem.  # noqa: E501
        :rtype: str
        """
        return self._perspective_id

    @perspective_id.setter
    def perspective_id(self, perspective_id):
        """Sets the perspective_id of this RecommendationItem.


        :param perspective_id: The perspective_id of this RecommendationItem.  # noqa: E501
        :type: str
        """

        self._perspective_id = perspective_id

    @property
    def perspective_name(self):
        """Gets the perspective_name of this RecommendationItem.  # noqa: E501


        :return: The perspective_name of this RecommendationItem.  # noqa: E501
        :rtype: str
        """
        return self._perspective_name

    @perspective_name.setter
    def perspective_name(self, perspective_name):
        """Sets the perspective_name of this RecommendationItem.


        :param perspective_name: The perspective_name of this RecommendationItem.  # noqa: E501
        :type: str
        """

        self._perspective_name = perspective_name

    @property
    def cloud_provider(self):
        """Gets the cloud_provider of this RecommendationItem.  # noqa: E501


        :return: The cloud_provider of this RecommendationItem.  # noqa: E501
        :rtype: str
        """
        return self._cloud_provider

    @cloud_provider.setter
    def cloud_provider(self, cloud_provider):
        """Sets the cloud_provider of this RecommendationItem.


        :param cloud_provider: The cloud_provider of this RecommendationItem.  # noqa: E501
        :type: str
        """

        self._cloud_provider = cloud_provider

    @property
    def governance_rule_id(self):
        """Gets the governance_rule_id of this RecommendationItem.  # noqa: E501


        :return: The governance_rule_id of this RecommendationItem.  # noqa: E501
        :rtype: str
        """
        return self._governance_rule_id

    @governance_rule_id.setter
    def governance_rule_id(self, governance_rule_id):
        """Sets the governance_rule_id of this RecommendationItem.


        :param governance_rule_id: The governance_rule_id of this RecommendationItem.  # noqa: E501
        :type: str
        """

        self._governance_rule_id = governance_rule_id

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
        if issubclass(RecommendationItem, dict):
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
        if not isinstance(other, RecommendationItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
