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

class RuleRequest(object):
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
        'account_id': 'str',
        'is_ootb': 'bool',
        'org_identifier': 'str',
        'project_identifier': 'str',
        'tags': 'str',
        'cloud_provider': 'str',
        'policy_ids': 'list[str]',
        'is_stable_policy': 'bool',
        'search': 'str',
        'limit': 'int',
        'offset': 'int',
        'order_by': 'list[CCMSort]',
        'resource_type': 'str'
    }

    attribute_map = {
        'account_id': 'accountId',
        'is_ootb': 'isOOTB',
        'org_identifier': 'orgIdentifier',
        'project_identifier': 'projectIdentifier',
        'tags': 'tags',
        'cloud_provider': 'cloudProvider',
        'policy_ids': 'policyIds',
        'is_stable_policy': 'isStablePolicy',
        'search': 'search',
        'limit': 'limit',
        'offset': 'offset',
        'order_by': 'orderBy',
        'resource_type': 'resourceType'
    }

    def __init__(self, account_id=None, is_ootb=None, org_identifier=None, project_identifier=None, tags=None, cloud_provider=None, policy_ids=None, is_stable_policy=None, search=None, limit=None, offset=None, order_by=None, resource_type=None):  # noqa: E501
        """RuleRequest - a model defined in Swagger"""  # noqa: E501
        self._account_id = None
        self._is_ootb = None
        self._org_identifier = None
        self._project_identifier = None
        self._tags = None
        self._cloud_provider = None
        self._policy_ids = None
        self._is_stable_policy = None
        self._search = None
        self._limit = None
        self._offset = None
        self._order_by = None
        self._resource_type = None
        self.discriminator = None
        if account_id is not None:
            self.account_id = account_id
        if is_ootb is not None:
            self.is_ootb = is_ootb
        if org_identifier is not None:
            self.org_identifier = org_identifier
        if project_identifier is not None:
            self.project_identifier = project_identifier
        if tags is not None:
            self.tags = tags
        if cloud_provider is not None:
            self.cloud_provider = cloud_provider
        if policy_ids is not None:
            self.policy_ids = policy_ids
        if is_stable_policy is not None:
            self.is_stable_policy = is_stable_policy
        if search is not None:
            self.search = search
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if order_by is not None:
            self.order_by = order_by
        if resource_type is not None:
            self.resource_type = resource_type

    @property
    def account_id(self):
        """Gets the account_id of this RuleRequest.  # noqa: E501

        account id  # noqa: E501

        :return: The account_id of this RuleRequest.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this RuleRequest.

        account id  # noqa: E501

        :param account_id: The account_id of this RuleRequest.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def is_ootb(self):
        """Gets the is_ootb of this RuleRequest.  # noqa: E501

        isOOTBPolicy  # noqa: E501

        :return: The is_ootb of this RuleRequest.  # noqa: E501
        :rtype: bool
        """
        return self._is_ootb

    @is_ootb.setter
    def is_ootb(self, is_ootb):
        """Sets the is_ootb of this RuleRequest.

        isOOTBPolicy  # noqa: E501

        :param is_ootb: The is_ootb of this RuleRequest.  # noqa: E501
        :type: bool
        """

        self._is_ootb = is_ootb

    @property
    def org_identifier(self):
        """Gets the org_identifier of this RuleRequest.  # noqa: E501

        Organization Identifier for the Entity.  # noqa: E501

        :return: The org_identifier of this RuleRequest.  # noqa: E501
        :rtype: str
        """
        return self._org_identifier

    @org_identifier.setter
    def org_identifier(self, org_identifier):
        """Sets the org_identifier of this RuleRequest.

        Organization Identifier for the Entity.  # noqa: E501

        :param org_identifier: The org_identifier of this RuleRequest.  # noqa: E501
        :type: str
        """

        self._org_identifier = org_identifier

    @property
    def project_identifier(self):
        """Gets the project_identifier of this RuleRequest.  # noqa: E501

        Project Identifier for the Entity.  # noqa: E501

        :return: The project_identifier of this RuleRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_identifier

    @project_identifier.setter
    def project_identifier(self, project_identifier):
        """Sets the project_identifier of this RuleRequest.

        Project Identifier for the Entity.  # noqa: E501

        :param project_identifier: The project_identifier of this RuleRequest.  # noqa: E501
        :type: str
        """

        self._project_identifier = project_identifier

    @property
    def tags(self):
        """Gets the tags of this RuleRequest.  # noqa: E501

        Tags  # noqa: E501

        :return: The tags of this RuleRequest.  # noqa: E501
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this RuleRequest.

        Tags  # noqa: E501

        :param tags: The tags of this RuleRequest.  # noqa: E501
        :type: str
        """

        self._tags = tags

    @property
    def cloud_provider(self):
        """Gets the cloud_provider of this RuleRequest.  # noqa: E501

        cloudProvider  # noqa: E501

        :return: The cloud_provider of this RuleRequest.  # noqa: E501
        :rtype: str
        """
        return self._cloud_provider

    @cloud_provider.setter
    def cloud_provider(self, cloud_provider):
        """Sets the cloud_provider of this RuleRequest.

        cloudProvider  # noqa: E501

        :param cloud_provider: The cloud_provider of this RuleRequest.  # noqa: E501
        :type: str
        """

        self._cloud_provider = cloud_provider

    @property
    def policy_ids(self):
        """Gets the policy_ids of this RuleRequest.  # noqa: E501

        policyIds  # noqa: E501

        :return: The policy_ids of this RuleRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._policy_ids

    @policy_ids.setter
    def policy_ids(self, policy_ids):
        """Sets the policy_ids of this RuleRequest.

        policyIds  # noqa: E501

        :param policy_ids: The policy_ids of this RuleRequest.  # noqa: E501
        :type: list[str]
        """

        self._policy_ids = policy_ids

    @property
    def is_stable_policy(self):
        """Gets the is_stable_policy of this RuleRequest.  # noqa: E501

        isStablePolicy  # noqa: E501

        :return: The is_stable_policy of this RuleRequest.  # noqa: E501
        :rtype: bool
        """
        return self._is_stable_policy

    @is_stable_policy.setter
    def is_stable_policy(self, is_stable_policy):
        """Sets the is_stable_policy of this RuleRequest.

        isStablePolicy  # noqa: E501

        :param is_stable_policy: The is_stable_policy of this RuleRequest.  # noqa: E501
        :type: bool
        """

        self._is_stable_policy = is_stable_policy

    @property
    def search(self):
        """Gets the search of this RuleRequest.  # noqa: E501

        search  # noqa: E501

        :return: The search of this RuleRequest.  # noqa: E501
        :rtype: str
        """
        return self._search

    @search.setter
    def search(self, search):
        """Sets the search of this RuleRequest.

        search  # noqa: E501

        :param search: The search of this RuleRequest.  # noqa: E501
        :type: str
        """

        self._search = search

    @property
    def limit(self):
        """Gets the limit of this RuleRequest.  # noqa: E501

        limit  # noqa: E501

        :return: The limit of this RuleRequest.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this RuleRequest.

        limit  # noqa: E501

        :param limit: The limit of this RuleRequest.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this RuleRequest.  # noqa: E501

        offset  # noqa: E501

        :return: The offset of this RuleRequest.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this RuleRequest.

        offset  # noqa: E501

        :param offset: The offset of this RuleRequest.  # noqa: E501
        :type: int
        """

        self._offset = offset

    @property
    def order_by(self):
        """Gets the order_by of this RuleRequest.  # noqa: E501

        The order by condition for Rule query  # noqa: E501

        :return: The order_by of this RuleRequest.  # noqa: E501
        :rtype: list[CCMSort]
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        """Sets the order_by of this RuleRequest.

        The order by condition for Rule query  # noqa: E501

        :param order_by: The order_by of this RuleRequest.  # noqa: E501
        :type: list[CCMSort]
        """

        self._order_by = order_by

    @property
    def resource_type(self):
        """Gets the resource_type of this RuleRequest.  # noqa: E501

        resourceType  # noqa: E501

        :return: The resource_type of this RuleRequest.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this RuleRequest.

        resourceType  # noqa: E501

        :param resource_type: The resource_type of this RuleRequest.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

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
        if issubclass(RuleRequest, dict):
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
        if not isinstance(other, RuleRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
