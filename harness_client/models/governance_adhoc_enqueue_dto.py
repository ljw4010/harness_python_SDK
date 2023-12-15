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

class GovernanceAdhocEnqueueDTO(object):
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
        'target_account_details': 'dict(str, RecommendationAdhocDTO)',
        'target_accounts': 'list[str]',
        'target_regions': 'list[str]',
        'rule_id': 'str',
        'policy': 'str',
        'is_dry_run': 'bool',
        'is_ootb': 'bool',
        'rule_cloud_provider_type': 'str'
    }

    attribute_map = {
        'target_account_details': 'targetAccountDetails',
        'target_accounts': 'targetAccounts',
        'target_regions': 'targetRegions',
        'rule_id': 'ruleId',
        'policy': 'policy',
        'is_dry_run': 'isDryRun',
        'is_ootb': 'isOOTB',
        'rule_cloud_provider_type': 'ruleCloudProviderType'
    }

    def __init__(self, target_account_details=None, target_accounts=None, target_regions=None, rule_id=None, policy=None, is_dry_run=None, is_ootb=None, rule_cloud_provider_type=None):  # noqa: E501
        """GovernanceAdhocEnqueueDTO - a model defined in Swagger"""  # noqa: E501
        self._target_account_details = None
        self._target_accounts = None
        self._target_regions = None
        self._rule_id = None
        self._policy = None
        self._is_dry_run = None
        self._is_ootb = None
        self._rule_cloud_provider_type = None
        self.discriminator = None
        if target_account_details is not None:
            self.target_account_details = target_account_details
        if target_accounts is not None:
            self.target_accounts = target_accounts
        if target_regions is not None:
            self.target_regions = target_regions
        if rule_id is not None:
            self.rule_id = rule_id
        if policy is not None:
            self.policy = policy
        if is_dry_run is not None:
            self.is_dry_run = is_dry_run
        if is_ootb is not None:
            self.is_ootb = is_ootb
        if rule_cloud_provider_type is not None:
            self.rule_cloud_provider_type = rule_cloud_provider_type

    @property
    def target_account_details(self):
        """Gets the target_account_details of this GovernanceAdhocEnqueueDTO.  # noqa: E501


        :return: The target_account_details of this GovernanceAdhocEnqueueDTO.  # noqa: E501
        :rtype: dict(str, RecommendationAdhocDTO)
        """
        return self._target_account_details

    @target_account_details.setter
    def target_account_details(self, target_account_details):
        """Sets the target_account_details of this GovernanceAdhocEnqueueDTO.


        :param target_account_details: The target_account_details of this GovernanceAdhocEnqueueDTO.  # noqa: E501
        :type: dict(str, RecommendationAdhocDTO)
        """

        self._target_account_details = target_account_details

    @property
    def target_accounts(self):
        """Gets the target_accounts of this GovernanceAdhocEnqueueDTO.  # noqa: E501


        :return: The target_accounts of this GovernanceAdhocEnqueueDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._target_accounts

    @target_accounts.setter
    def target_accounts(self, target_accounts):
        """Sets the target_accounts of this GovernanceAdhocEnqueueDTO.


        :param target_accounts: The target_accounts of this GovernanceAdhocEnqueueDTO.  # noqa: E501
        :type: list[str]
        """

        self._target_accounts = target_accounts

    @property
    def target_regions(self):
        """Gets the target_regions of this GovernanceAdhocEnqueueDTO.  # noqa: E501


        :return: The target_regions of this GovernanceAdhocEnqueueDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._target_regions

    @target_regions.setter
    def target_regions(self, target_regions):
        """Sets the target_regions of this GovernanceAdhocEnqueueDTO.


        :param target_regions: The target_regions of this GovernanceAdhocEnqueueDTO.  # noqa: E501
        :type: list[str]
        """

        self._target_regions = target_regions

    @property
    def rule_id(self):
        """Gets the rule_id of this GovernanceAdhocEnqueueDTO.  # noqa: E501


        :return: The rule_id of this GovernanceAdhocEnqueueDTO.  # noqa: E501
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        """Sets the rule_id of this GovernanceAdhocEnqueueDTO.


        :param rule_id: The rule_id of this GovernanceAdhocEnqueueDTO.  # noqa: E501
        :type: str
        """

        self._rule_id = rule_id

    @property
    def policy(self):
        """Gets the policy of this GovernanceAdhocEnqueueDTO.  # noqa: E501


        :return: The policy of this GovernanceAdhocEnqueueDTO.  # noqa: E501
        :rtype: str
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this GovernanceAdhocEnqueueDTO.


        :param policy: The policy of this GovernanceAdhocEnqueueDTO.  # noqa: E501
        :type: str
        """

        self._policy = policy

    @property
    def is_dry_run(self):
        """Gets the is_dry_run of this GovernanceAdhocEnqueueDTO.  # noqa: E501


        :return: The is_dry_run of this GovernanceAdhocEnqueueDTO.  # noqa: E501
        :rtype: bool
        """
        return self._is_dry_run

    @is_dry_run.setter
    def is_dry_run(self, is_dry_run):
        """Sets the is_dry_run of this GovernanceAdhocEnqueueDTO.


        :param is_dry_run: The is_dry_run of this GovernanceAdhocEnqueueDTO.  # noqa: E501
        :type: bool
        """

        self._is_dry_run = is_dry_run

    @property
    def is_ootb(self):
        """Gets the is_ootb of this GovernanceAdhocEnqueueDTO.  # noqa: E501


        :return: The is_ootb of this GovernanceAdhocEnqueueDTO.  # noqa: E501
        :rtype: bool
        """
        return self._is_ootb

    @is_ootb.setter
    def is_ootb(self, is_ootb):
        """Sets the is_ootb of this GovernanceAdhocEnqueueDTO.


        :param is_ootb: The is_ootb of this GovernanceAdhocEnqueueDTO.  # noqa: E501
        :type: bool
        """

        self._is_ootb = is_ootb

    @property
    def rule_cloud_provider_type(self):
        """Gets the rule_cloud_provider_type of this GovernanceAdhocEnqueueDTO.  # noqa: E501


        :return: The rule_cloud_provider_type of this GovernanceAdhocEnqueueDTO.  # noqa: E501
        :rtype: str
        """
        return self._rule_cloud_provider_type

    @rule_cloud_provider_type.setter
    def rule_cloud_provider_type(self, rule_cloud_provider_type):
        """Sets the rule_cloud_provider_type of this GovernanceAdhocEnqueueDTO.


        :param rule_cloud_provider_type: The rule_cloud_provider_type of this GovernanceAdhocEnqueueDTO.  # noqa: E501
        :type: str
        """
        allowed_values = ["AWS", "AZURE"]  # noqa: E501
        if rule_cloud_provider_type not in allowed_values:
            raise ValueError(
                "Invalid value for `rule_cloud_provider_type` ({0}), must be one of {1}"  # noqa: E501
                .format(rule_cloud_provider_type, allowed_values)
            )

        self._rule_cloud_provider_type = rule_cloud_provider_type

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
        if issubclass(GovernanceAdhocEnqueueDTO, dict):
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
        if not isinstance(other, GovernanceAdhocEnqueueDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
