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

class RuleEnforcement(object):
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
        'uuid': 'str',
        'account_id': 'str',
        'name': 'str',
        'description': 'str',
        'tags': 'list[str]',
        'org_identifier': 'str',
        'project_identifier': 'str',
        'cloud_provider': 'str',
        'rule_ids': 'list[str]',
        'rule_set_ids': 'list[str]',
        'execution_schedule': 'str',
        'execution_timezone': 'str',
        'target_accounts': 'list[str]',
        'target_regions': 'list[str]',
        'is_dry_run': 'bool',
        'deleted': 'bool',
        'run_count': 'int',
        'is_enabled': 'bool',
        'created_at': 'int',
        'last_updated_at': 'int',
        'created_by': 'EmbeddedUser',
        'last_updated_by': 'EmbeddedUser'
    }

    attribute_map = {
        'uuid': 'uuid',
        'account_id': 'accountId',
        'name': 'name',
        'description': 'description',
        'tags': 'tags',
        'org_identifier': 'orgIdentifier',
        'project_identifier': 'projectIdentifier',
        'cloud_provider': 'cloudProvider',
        'rule_ids': 'ruleIds',
        'rule_set_ids': 'ruleSetIDs',
        'execution_schedule': 'executionSchedule',
        'execution_timezone': 'executionTimezone',
        'target_accounts': 'targetAccounts',
        'target_regions': 'targetRegions',
        'is_dry_run': 'isDryRun',
        'deleted': 'deleted',
        'run_count': 'runCount',
        'is_enabled': 'isEnabled',
        'created_at': 'createdAt',
        'last_updated_at': 'lastUpdatedAt',
        'created_by': 'createdBy',
        'last_updated_by': 'lastUpdatedBy'
    }

    def __init__(self, uuid=None, account_id=None, name=None, description=None, tags=None, org_identifier=None, project_identifier=None, cloud_provider=None, rule_ids=None, rule_set_ids=None, execution_schedule=None, execution_timezone=None, target_accounts=None, target_regions=None, is_dry_run=None, deleted=None, run_count=None, is_enabled=None, created_at=None, last_updated_at=None, created_by=None, last_updated_by=None):  # noqa: E501
        """RuleEnforcement - a model defined in Swagger"""  # noqa: E501
        self._uuid = None
        self._account_id = None
        self._name = None
        self._description = None
        self._tags = None
        self._org_identifier = None
        self._project_identifier = None
        self._cloud_provider = None
        self._rule_ids = None
        self._rule_set_ids = None
        self._execution_schedule = None
        self._execution_timezone = None
        self._target_accounts = None
        self._target_regions = None
        self._is_dry_run = None
        self._deleted = None
        self._run_count = None
        self._is_enabled = None
        self._created_at = None
        self._last_updated_at = None
        self._created_by = None
        self._last_updated_by = None
        self.discriminator = None
        if uuid is not None:
            self.uuid = uuid
        if account_id is not None:
            self.account_id = account_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags
        if org_identifier is not None:
            self.org_identifier = org_identifier
        if project_identifier is not None:
            self.project_identifier = project_identifier
        if cloud_provider is not None:
            self.cloud_provider = cloud_provider
        if rule_ids is not None:
            self.rule_ids = rule_ids
        if rule_set_ids is not None:
            self.rule_set_ids = rule_set_ids
        if execution_schedule is not None:
            self.execution_schedule = execution_schedule
        if execution_timezone is not None:
            self.execution_timezone = execution_timezone
        if target_accounts is not None:
            self.target_accounts = target_accounts
        if target_regions is not None:
            self.target_regions = target_regions
        if is_dry_run is not None:
            self.is_dry_run = is_dry_run
        if deleted is not None:
            self.deleted = deleted
        if run_count is not None:
            self.run_count = run_count
        if is_enabled is not None:
            self.is_enabled = is_enabled
        if created_at is not None:
            self.created_at = created_at
        if last_updated_at is not None:
            self.last_updated_at = last_updated_at
        if created_by is not None:
            self.created_by = created_by
        if last_updated_by is not None:
            self.last_updated_by = last_updated_by

    @property
    def uuid(self):
        """Gets the uuid of this RuleEnforcement.  # noqa: E501

        unique id  # noqa: E501

        :return: The uuid of this RuleEnforcement.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this RuleEnforcement.

        unique id  # noqa: E501

        :param uuid: The uuid of this RuleEnforcement.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def account_id(self):
        """Gets the account_id of this RuleEnforcement.  # noqa: E501

        account id  # noqa: E501

        :return: The account_id of this RuleEnforcement.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this RuleEnforcement.

        account id  # noqa: E501

        :param account_id: The account_id of this RuleEnforcement.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def name(self):
        """Gets the name of this RuleEnforcement.  # noqa: E501

        name  # noqa: E501

        :return: The name of this RuleEnforcement.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RuleEnforcement.

        name  # noqa: E501

        :param name: The name of this RuleEnforcement.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this RuleEnforcement.  # noqa: E501

        Description of the entity  # noqa: E501

        :return: The description of this RuleEnforcement.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RuleEnforcement.

        Description of the entity  # noqa: E501

        :param description: The description of this RuleEnforcement.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def tags(self):
        """Gets the tags of this RuleEnforcement.  # noqa: E501

        Tags  # noqa: E501

        :return: The tags of this RuleEnforcement.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this RuleEnforcement.

        Tags  # noqa: E501

        :param tags: The tags of this RuleEnforcement.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def org_identifier(self):
        """Gets the org_identifier of this RuleEnforcement.  # noqa: E501

        Organization Identifier for the Entity.  # noqa: E501

        :return: The org_identifier of this RuleEnforcement.  # noqa: E501
        :rtype: str
        """
        return self._org_identifier

    @org_identifier.setter
    def org_identifier(self, org_identifier):
        """Sets the org_identifier of this RuleEnforcement.

        Organization Identifier for the Entity.  # noqa: E501

        :param org_identifier: The org_identifier of this RuleEnforcement.  # noqa: E501
        :type: str
        """

        self._org_identifier = org_identifier

    @property
    def project_identifier(self):
        """Gets the project_identifier of this RuleEnforcement.  # noqa: E501

        Project Identifier for the Entity.  # noqa: E501

        :return: The project_identifier of this RuleEnforcement.  # noqa: E501
        :rtype: str
        """
        return self._project_identifier

    @project_identifier.setter
    def project_identifier(self, project_identifier):
        """Sets the project_identifier of this RuleEnforcement.

        Project Identifier for the Entity.  # noqa: E501

        :param project_identifier: The project_identifier of this RuleEnforcement.  # noqa: E501
        :type: str
        """

        self._project_identifier = project_identifier

    @property
    def cloud_provider(self):
        """Gets the cloud_provider of this RuleEnforcement.  # noqa: E501

        cloudProvider  # noqa: E501

        :return: The cloud_provider of this RuleEnforcement.  # noqa: E501
        :rtype: str
        """
        return self._cloud_provider

    @cloud_provider.setter
    def cloud_provider(self, cloud_provider):
        """Sets the cloud_provider of this RuleEnforcement.

        cloudProvider  # noqa: E501

        :param cloud_provider: The cloud_provider of this RuleEnforcement.  # noqa: E501
        :type: str
        """
        allowed_values = ["AWS", "AZURE"]  # noqa: E501
        if cloud_provider not in allowed_values:
            raise ValueError(
                "Invalid value for `cloud_provider` ({0}), must be one of {1}"  # noqa: E501
                .format(cloud_provider, allowed_values)
            )

        self._cloud_provider = cloud_provider

    @property
    def rule_ids(self):
        """Gets the rule_ids of this RuleEnforcement.  # noqa: E501

        rulesIds  # noqa: E501

        :return: The rule_ids of this RuleEnforcement.  # noqa: E501
        :rtype: list[str]
        """
        return self._rule_ids

    @rule_ids.setter
    def rule_ids(self, rule_ids):
        """Sets the rule_ids of this RuleEnforcement.

        rulesIds  # noqa: E501

        :param rule_ids: The rule_ids of this RuleEnforcement.  # noqa: E501
        :type: list[str]
        """

        self._rule_ids = rule_ids

    @property
    def rule_set_ids(self):
        """Gets the rule_set_ids of this RuleEnforcement.  # noqa: E501

        ruleSetIDs  # noqa: E501

        :return: The rule_set_ids of this RuleEnforcement.  # noqa: E501
        :rtype: list[str]
        """
        return self._rule_set_ids

    @rule_set_ids.setter
    def rule_set_ids(self, rule_set_ids):
        """Sets the rule_set_ids of this RuleEnforcement.

        ruleSetIDs  # noqa: E501

        :param rule_set_ids: The rule_set_ids of this RuleEnforcement.  # noqa: E501
        :type: list[str]
        """

        self._rule_set_ids = rule_set_ids

    @property
    def execution_schedule(self):
        """Gets the execution_schedule of this RuleEnforcement.  # noqa: E501

        executionSchedule  # noqa: E501

        :return: The execution_schedule of this RuleEnforcement.  # noqa: E501
        :rtype: str
        """
        return self._execution_schedule

    @execution_schedule.setter
    def execution_schedule(self, execution_schedule):
        """Sets the execution_schedule of this RuleEnforcement.

        executionSchedule  # noqa: E501

        :param execution_schedule: The execution_schedule of this RuleEnforcement.  # noqa: E501
        :type: str
        """

        self._execution_schedule = execution_schedule

    @property
    def execution_timezone(self):
        """Gets the execution_timezone of this RuleEnforcement.  # noqa: E501

        executionTimezone  # noqa: E501

        :return: The execution_timezone of this RuleEnforcement.  # noqa: E501
        :rtype: str
        """
        return self._execution_timezone

    @execution_timezone.setter
    def execution_timezone(self, execution_timezone):
        """Sets the execution_timezone of this RuleEnforcement.

        executionTimezone  # noqa: E501

        :param execution_timezone: The execution_timezone of this RuleEnforcement.  # noqa: E501
        :type: str
        """

        self._execution_timezone = execution_timezone

    @property
    def target_accounts(self):
        """Gets the target_accounts of this RuleEnforcement.  # noqa: E501

        targetAccounts  # noqa: E501

        :return: The target_accounts of this RuleEnforcement.  # noqa: E501
        :rtype: list[str]
        """
        return self._target_accounts

    @target_accounts.setter
    def target_accounts(self, target_accounts):
        """Sets the target_accounts of this RuleEnforcement.

        targetAccounts  # noqa: E501

        :param target_accounts: The target_accounts of this RuleEnforcement.  # noqa: E501
        :type: list[str]
        """

        self._target_accounts = target_accounts

    @property
    def target_regions(self):
        """Gets the target_regions of this RuleEnforcement.  # noqa: E501

        targetRegions  # noqa: E501

        :return: The target_regions of this RuleEnforcement.  # noqa: E501
        :rtype: list[str]
        """
        return self._target_regions

    @target_regions.setter
    def target_regions(self, target_regions):
        """Sets the target_regions of this RuleEnforcement.

        targetRegions  # noqa: E501

        :param target_regions: The target_regions of this RuleEnforcement.  # noqa: E501
        :type: list[str]
        """

        self._target_regions = target_regions

    @property
    def is_dry_run(self):
        """Gets the is_dry_run of this RuleEnforcement.  # noqa: E501

        isDryRun  # noqa: E501

        :return: The is_dry_run of this RuleEnforcement.  # noqa: E501
        :rtype: bool
        """
        return self._is_dry_run

    @is_dry_run.setter
    def is_dry_run(self, is_dry_run):
        """Sets the is_dry_run of this RuleEnforcement.

        isDryRun  # noqa: E501

        :param is_dry_run: The is_dry_run of this RuleEnforcement.  # noqa: E501
        :type: bool
        """

        self._is_dry_run = is_dry_run

    @property
    def deleted(self):
        """Gets the deleted of this RuleEnforcement.  # noqa: E501

        deleted  # noqa: E501

        :return: The deleted of this RuleEnforcement.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this RuleEnforcement.

        deleted  # noqa: E501

        :param deleted: The deleted of this RuleEnforcement.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def run_count(self):
        """Gets the run_count of this RuleEnforcement.  # noqa: E501

        runCount  # noqa: E501

        :return: The run_count of this RuleEnforcement.  # noqa: E501
        :rtype: int
        """
        return self._run_count

    @run_count.setter
    def run_count(self, run_count):
        """Sets the run_count of this RuleEnforcement.

        runCount  # noqa: E501

        :param run_count: The run_count of this RuleEnforcement.  # noqa: E501
        :type: int
        """

        self._run_count = run_count

    @property
    def is_enabled(self):
        """Gets the is_enabled of this RuleEnforcement.  # noqa: E501

        isEnabled  # noqa: E501

        :return: The is_enabled of this RuleEnforcement.  # noqa: E501
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """Sets the is_enabled of this RuleEnforcement.

        isEnabled  # noqa: E501

        :param is_enabled: The is_enabled of this RuleEnforcement.  # noqa: E501
        :type: bool
        """

        self._is_enabled = is_enabled

    @property
    def created_at(self):
        """Gets the created_at of this RuleEnforcement.  # noqa: E501

        Time at which the entity was created  # noqa: E501

        :return: The created_at of this RuleEnforcement.  # noqa: E501
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this RuleEnforcement.

        Time at which the entity was created  # noqa: E501

        :param created_at: The created_at of this RuleEnforcement.  # noqa: E501
        :type: int
        """

        self._created_at = created_at

    @property
    def last_updated_at(self):
        """Gets the last_updated_at of this RuleEnforcement.  # noqa: E501

        Time at which the entity was last updated  # noqa: E501

        :return: The last_updated_at of this RuleEnforcement.  # noqa: E501
        :rtype: int
        """
        return self._last_updated_at

    @last_updated_at.setter
    def last_updated_at(self, last_updated_at):
        """Sets the last_updated_at of this RuleEnforcement.

        Time at which the entity was last updated  # noqa: E501

        :param last_updated_at: The last_updated_at of this RuleEnforcement.  # noqa: E501
        :type: int
        """

        self._last_updated_at = last_updated_at

    @property
    def created_by(self):
        """Gets the created_by of this RuleEnforcement.  # noqa: E501


        :return: The created_by of this RuleEnforcement.  # noqa: E501
        :rtype: EmbeddedUser
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this RuleEnforcement.


        :param created_by: The created_by of this RuleEnforcement.  # noqa: E501
        :type: EmbeddedUser
        """

        self._created_by = created_by

    @property
    def last_updated_by(self):
        """Gets the last_updated_by of this RuleEnforcement.  # noqa: E501


        :return: The last_updated_by of this RuleEnforcement.  # noqa: E501
        :rtype: EmbeddedUser
        """
        return self._last_updated_by

    @last_updated_by.setter
    def last_updated_by(self, last_updated_by):
        """Sets the last_updated_by of this RuleEnforcement.


        :param last_updated_by: The last_updated_by of this RuleEnforcement.  # noqa: E501
        :type: EmbeddedUser
        """

        self._last_updated_by = last_updated_by

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
        if issubclass(RuleEnforcement, dict):
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
        if not isinstance(other, RuleEnforcement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
