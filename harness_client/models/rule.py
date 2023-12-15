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

class Rule(object):
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
        'rules_yaml': 'str',
        'tags': 'list[str]',
        'org_identifier': 'str',
        'project_identifier': 'str',
        'cloud_provider': 'str',
        'version_label': 'str',
        'is_stable_policy': 'bool',
        'store_type': 'str',
        'is_ootb': 'bool',
        'deleted': 'bool',
        'for_recommendation': 'bool',
        'resource_type': 'str',
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
        'rules_yaml': 'rulesYaml',
        'tags': 'tags',
        'org_identifier': 'orgIdentifier',
        'project_identifier': 'projectIdentifier',
        'cloud_provider': 'cloudProvider',
        'version_label': 'versionLabel',
        'is_stable_policy': 'isStablePolicy',
        'store_type': 'storeType',
        'is_ootb': 'isOOTB',
        'deleted': 'deleted',
        'for_recommendation': 'forRecommendation',
        'resource_type': 'resourceType',
        'created_at': 'createdAt',
        'last_updated_at': 'lastUpdatedAt',
        'created_by': 'createdBy',
        'last_updated_by': 'lastUpdatedBy'
    }

    def __init__(self, uuid=None, account_id=None, name=None, description=None, rules_yaml=None, tags=None, org_identifier=None, project_identifier=None, cloud_provider=None, version_label=None, is_stable_policy=None, store_type=None, is_ootb=None, deleted=None, for_recommendation=None, resource_type=None, created_at=None, last_updated_at=None, created_by=None, last_updated_by=None):  # noqa: E501
        """Rule - a model defined in Swagger"""  # noqa: E501
        self._uuid = None
        self._account_id = None
        self._name = None
        self._description = None
        self._rules_yaml = None
        self._tags = None
        self._org_identifier = None
        self._project_identifier = None
        self._cloud_provider = None
        self._version_label = None
        self._is_stable_policy = None
        self._store_type = None
        self._is_ootb = None
        self._deleted = None
        self._for_recommendation = None
        self._resource_type = None
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
        if rules_yaml is not None:
            self.rules_yaml = rules_yaml
        if tags is not None:
            self.tags = tags
        if org_identifier is not None:
            self.org_identifier = org_identifier
        if project_identifier is not None:
            self.project_identifier = project_identifier
        if cloud_provider is not None:
            self.cloud_provider = cloud_provider
        if version_label is not None:
            self.version_label = version_label
        if is_stable_policy is not None:
            self.is_stable_policy = is_stable_policy
        if store_type is not None:
            self.store_type = store_type
        if is_ootb is not None:
            self.is_ootb = is_ootb
        if deleted is not None:
            self.deleted = deleted
        if for_recommendation is not None:
            self.for_recommendation = for_recommendation
        if resource_type is not None:
            self.resource_type = resource_type
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
        """Gets the uuid of this Rule.  # noqa: E501

        unique id  # noqa: E501

        :return: The uuid of this Rule.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this Rule.

        unique id  # noqa: E501

        :param uuid: The uuid of this Rule.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def account_id(self):
        """Gets the account_id of this Rule.  # noqa: E501

        account id  # noqa: E501

        :return: The account_id of this Rule.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this Rule.

        account id  # noqa: E501

        :param account_id: The account_id of this Rule.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def name(self):
        """Gets the name of this Rule.  # noqa: E501

        name  # noqa: E501

        :return: The name of this Rule.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Rule.

        name  # noqa: E501

        :param name: The name of this Rule.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this Rule.  # noqa: E501

        Description of the entity  # noqa: E501

        :return: The description of this Rule.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Rule.

        Description of the entity  # noqa: E501

        :param description: The description of this Rule.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def rules_yaml(self):
        """Gets the rules_yaml of this Rule.  # noqa: E501

        Get YAML of the policy  # noqa: E501

        :return: The rules_yaml of this Rule.  # noqa: E501
        :rtype: str
        """
        return self._rules_yaml

    @rules_yaml.setter
    def rules_yaml(self, rules_yaml):
        """Sets the rules_yaml of this Rule.

        Get YAML of the policy  # noqa: E501

        :param rules_yaml: The rules_yaml of this Rule.  # noqa: E501
        :type: str
        """

        self._rules_yaml = rules_yaml

    @property
    def tags(self):
        """Gets the tags of this Rule.  # noqa: E501

        Tags  # noqa: E501

        :return: The tags of this Rule.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Rule.

        Tags  # noqa: E501

        :param tags: The tags of this Rule.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def org_identifier(self):
        """Gets the org_identifier of this Rule.  # noqa: E501

        Organization Identifier for the Entity.  # noqa: E501

        :return: The org_identifier of this Rule.  # noqa: E501
        :rtype: str
        """
        return self._org_identifier

    @org_identifier.setter
    def org_identifier(self, org_identifier):
        """Sets the org_identifier of this Rule.

        Organization Identifier for the Entity.  # noqa: E501

        :param org_identifier: The org_identifier of this Rule.  # noqa: E501
        :type: str
        """

        self._org_identifier = org_identifier

    @property
    def project_identifier(self):
        """Gets the project_identifier of this Rule.  # noqa: E501

        Project Identifier for the Entity.  # noqa: E501

        :return: The project_identifier of this Rule.  # noqa: E501
        :rtype: str
        """
        return self._project_identifier

    @project_identifier.setter
    def project_identifier(self, project_identifier):
        """Sets the project_identifier of this Rule.

        Project Identifier for the Entity.  # noqa: E501

        :param project_identifier: The project_identifier of this Rule.  # noqa: E501
        :type: str
        """

        self._project_identifier = project_identifier

    @property
    def cloud_provider(self):
        """Gets the cloud_provider of this Rule.  # noqa: E501

        cloudProvider  # noqa: E501

        :return: The cloud_provider of this Rule.  # noqa: E501
        :rtype: str
        """
        return self._cloud_provider

    @cloud_provider.setter
    def cloud_provider(self, cloud_provider):
        """Sets the cloud_provider of this Rule.

        cloudProvider  # noqa: E501

        :param cloud_provider: The cloud_provider of this Rule.  # noqa: E501
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
    def version_label(self):
        """Gets the version_label of this Rule.  # noqa: E501

        versionLabel  # noqa: E501

        :return: The version_label of this Rule.  # noqa: E501
        :rtype: str
        """
        return self._version_label

    @version_label.setter
    def version_label(self, version_label):
        """Sets the version_label of this Rule.

        versionLabel  # noqa: E501

        :param version_label: The version_label of this Rule.  # noqa: E501
        :type: str
        """

        self._version_label = version_label

    @property
    def is_stable_policy(self):
        """Gets the is_stable_policy of this Rule.  # noqa: E501

        isStablePolicy  # noqa: E501

        :return: The is_stable_policy of this Rule.  # noqa: E501
        :rtype: bool
        """
        return self._is_stable_policy

    @is_stable_policy.setter
    def is_stable_policy(self, is_stable_policy):
        """Sets the is_stable_policy of this Rule.

        isStablePolicy  # noqa: E501

        :param is_stable_policy: The is_stable_policy of this Rule.  # noqa: E501
        :type: bool
        """

        self._is_stable_policy = is_stable_policy

    @property
    def store_type(self):
        """Gets the store_type of this Rule.  # noqa: E501

        storeType  # noqa: E501

        :return: The store_type of this Rule.  # noqa: E501
        :rtype: str
        """
        return self._store_type

    @store_type.setter
    def store_type(self, store_type):
        """Sets the store_type of this Rule.

        storeType  # noqa: E501

        :param store_type: The store_type of this Rule.  # noqa: E501
        :type: str
        """
        allowed_values = ["INLINE", "REMOTE"]  # noqa: E501
        if store_type not in allowed_values:
            raise ValueError(
                "Invalid value for `store_type` ({0}), must be one of {1}"  # noqa: E501
                .format(store_type, allowed_values)
            )

        self._store_type = store_type

    @property
    def is_ootb(self):
        """Gets the is_ootb of this Rule.  # noqa: E501

        isOOTB  # noqa: E501

        :return: The is_ootb of this Rule.  # noqa: E501
        :rtype: bool
        """
        return self._is_ootb

    @is_ootb.setter
    def is_ootb(self, is_ootb):
        """Sets the is_ootb of this Rule.

        isOOTB  # noqa: E501

        :param is_ootb: The is_ootb of this Rule.  # noqa: E501
        :type: bool
        """

        self._is_ootb = is_ootb

    @property
    def deleted(self):
        """Gets the deleted of this Rule.  # noqa: E501

        deleted  # noqa: E501

        :return: The deleted of this Rule.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this Rule.

        deleted  # noqa: E501

        :param deleted: The deleted of this Rule.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def for_recommendation(self):
        """Gets the for_recommendation of this Rule.  # noqa: E501

        forRecommendation  # noqa: E501

        :return: The for_recommendation of this Rule.  # noqa: E501
        :rtype: bool
        """
        return self._for_recommendation

    @for_recommendation.setter
    def for_recommendation(self, for_recommendation):
        """Sets the for_recommendation of this Rule.

        forRecommendation  # noqa: E501

        :param for_recommendation: The for_recommendation of this Rule.  # noqa: E501
        :type: bool
        """

        self._for_recommendation = for_recommendation

    @property
    def resource_type(self):
        """Gets the resource_type of this Rule.  # noqa: E501

        resourceType  # noqa: E501

        :return: The resource_type of this Rule.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this Rule.

        resourceType  # noqa: E501

        :param resource_type: The resource_type of this Rule.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

    @property
    def created_at(self):
        """Gets the created_at of this Rule.  # noqa: E501

        Time at which the entity was created  # noqa: E501

        :return: The created_at of this Rule.  # noqa: E501
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Rule.

        Time at which the entity was created  # noqa: E501

        :param created_at: The created_at of this Rule.  # noqa: E501
        :type: int
        """

        self._created_at = created_at

    @property
    def last_updated_at(self):
        """Gets the last_updated_at of this Rule.  # noqa: E501

        Time at which the entity was last updated  # noqa: E501

        :return: The last_updated_at of this Rule.  # noqa: E501
        :rtype: int
        """
        return self._last_updated_at

    @last_updated_at.setter
    def last_updated_at(self, last_updated_at):
        """Sets the last_updated_at of this Rule.

        Time at which the entity was last updated  # noqa: E501

        :param last_updated_at: The last_updated_at of this Rule.  # noqa: E501
        :type: int
        """

        self._last_updated_at = last_updated_at

    @property
    def created_by(self):
        """Gets the created_by of this Rule.  # noqa: E501


        :return: The created_by of this Rule.  # noqa: E501
        :rtype: EmbeddedUser
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Rule.


        :param created_by: The created_by of this Rule.  # noqa: E501
        :type: EmbeddedUser
        """

        self._created_by = created_by

    @property
    def last_updated_by(self):
        """Gets the last_updated_by of this Rule.  # noqa: E501


        :return: The last_updated_by of this Rule.  # noqa: E501
        :rtype: EmbeddedUser
        """
        return self._last_updated_by

    @last_updated_by.setter
    def last_updated_by(self, last_updated_by):
        """Sets the last_updated_by of this Rule.


        :param last_updated_by: The last_updated_by of this Rule.  # noqa: E501
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
        if issubclass(Rule, dict):
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
        if not isinstance(other, Rule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
