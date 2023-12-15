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

class PipelineTemplateResponse(object):
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
        'org_identifier': 'str',
        'project_identifier': 'str',
        'identifier': 'str',
        'name': 'str',
        'description': 'str',
        'tags': 'dict(str, str)',
        'yaml': 'str',
        'version_label': 'str',
        'is_stable_template': 'bool',
        'template_entity_type': 'str',
        'child_type': 'str',
        'template_scope': 'str',
        'version': 'int',
        'git_details': 'PipelineEntityGitDetails',
        'entity_validity_details': 'PipelineEntityGitDetails',
        'last_updated_at': 'int',
        'store_type': 'str',
        'connector_ref': 'str',
        'icon': 'str',
        'cache_response_metadata': 'CacheResponseMetadata',
        'yaml_version': 'str',
        'stable_template': 'bool'
    }

    attribute_map = {
        'account_id': 'accountId',
        'org_identifier': 'orgIdentifier',
        'project_identifier': 'projectIdentifier',
        'identifier': 'identifier',
        'name': 'name',
        'description': 'description',
        'tags': 'tags',
        'yaml': 'yaml',
        'version_label': 'versionLabel',
        'is_stable_template': 'isStableTemplate',
        'template_entity_type': 'templateEntityType',
        'child_type': 'childType',
        'template_scope': 'templateScope',
        'version': 'version',
        'git_details': 'gitDetails',
        'entity_validity_details': 'entityValidityDetails',
        'last_updated_at': 'lastUpdatedAt',
        'store_type': 'storeType',
        'connector_ref': 'connectorRef',
        'icon': 'icon',
        'cache_response_metadata': 'cacheResponseMetadata',
        'yaml_version': 'yamlVersion',
        'stable_template': 'stableTemplate'
    }

    def __init__(self, account_id=None, org_identifier=None, project_identifier=None, identifier=None, name=None, description=None, tags=None, yaml=None, version_label=None, is_stable_template=None, template_entity_type=None, child_type=None, template_scope=None, version=None, git_details=None, entity_validity_details=None, last_updated_at=None, store_type=None, connector_ref=None, icon=None, cache_response_metadata=None, yaml_version=None, stable_template=None):  # noqa: E501
        """PipelineTemplateResponse - a model defined in Swagger"""  # noqa: E501
        self._account_id = None
        self._org_identifier = None
        self._project_identifier = None
        self._identifier = None
        self._name = None
        self._description = None
        self._tags = None
        self._yaml = None
        self._version_label = None
        self._is_stable_template = None
        self._template_entity_type = None
        self._child_type = None
        self._template_scope = None
        self._version = None
        self._git_details = None
        self._entity_validity_details = None
        self._last_updated_at = None
        self._store_type = None
        self._connector_ref = None
        self._icon = None
        self._cache_response_metadata = None
        self._yaml_version = None
        self._stable_template = None
        self.discriminator = None
        self.account_id = account_id
        if org_identifier is not None:
            self.org_identifier = org_identifier
        if project_identifier is not None:
            self.project_identifier = project_identifier
        self.identifier = identifier
        self.name = name
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags
        self.yaml = yaml
        if version_label is not None:
            self.version_label = version_label
        if is_stable_template is not None:
            self.is_stable_template = is_stable_template
        if template_entity_type is not None:
            self.template_entity_type = template_entity_type
        if child_type is not None:
            self.child_type = child_type
        if template_scope is not None:
            self.template_scope = template_scope
        if version is not None:
            self.version = version
        if git_details is not None:
            self.git_details = git_details
        if entity_validity_details is not None:
            self.entity_validity_details = entity_validity_details
        if last_updated_at is not None:
            self.last_updated_at = last_updated_at
        if store_type is not None:
            self.store_type = store_type
        if connector_ref is not None:
            self.connector_ref = connector_ref
        if icon is not None:
            self.icon = icon
        if cache_response_metadata is not None:
            self.cache_response_metadata = cache_response_metadata
        if yaml_version is not None:
            self.yaml_version = yaml_version
        if stable_template is not None:
            self.stable_template = stable_template

    @property
    def account_id(self):
        """Gets the account_id of this PipelineTemplateResponse.  # noqa: E501


        :return: The account_id of this PipelineTemplateResponse.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this PipelineTemplateResponse.


        :param account_id: The account_id of this PipelineTemplateResponse.  # noqa: E501
        :type: str
        """
        if account_id is None:
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def org_identifier(self):
        """Gets the org_identifier of this PipelineTemplateResponse.  # noqa: E501


        :return: The org_identifier of this PipelineTemplateResponse.  # noqa: E501
        :rtype: str
        """
        return self._org_identifier

    @org_identifier.setter
    def org_identifier(self, org_identifier):
        """Sets the org_identifier of this PipelineTemplateResponse.


        :param org_identifier: The org_identifier of this PipelineTemplateResponse.  # noqa: E501
        :type: str
        """

        self._org_identifier = org_identifier

    @property
    def project_identifier(self):
        """Gets the project_identifier of this PipelineTemplateResponse.  # noqa: E501


        :return: The project_identifier of this PipelineTemplateResponse.  # noqa: E501
        :rtype: str
        """
        return self._project_identifier

    @project_identifier.setter
    def project_identifier(self, project_identifier):
        """Sets the project_identifier of this PipelineTemplateResponse.


        :param project_identifier: The project_identifier of this PipelineTemplateResponse.  # noqa: E501
        :type: str
        """

        self._project_identifier = project_identifier

    @property
    def identifier(self):
        """Gets the identifier of this PipelineTemplateResponse.  # noqa: E501


        :return: The identifier of this PipelineTemplateResponse.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this PipelineTemplateResponse.


        :param identifier: The identifier of this PipelineTemplateResponse.  # noqa: E501
        :type: str
        """
        if identifier is None:
            raise ValueError("Invalid value for `identifier`, must not be `None`")  # noqa: E501

        self._identifier = identifier

    @property
    def name(self):
        """Gets the name of this PipelineTemplateResponse.  # noqa: E501


        :return: The name of this PipelineTemplateResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PipelineTemplateResponse.


        :param name: The name of this PipelineTemplateResponse.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this PipelineTemplateResponse.  # noqa: E501


        :return: The description of this PipelineTemplateResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PipelineTemplateResponse.


        :param description: The description of this PipelineTemplateResponse.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def tags(self):
        """Gets the tags of this PipelineTemplateResponse.  # noqa: E501


        :return: The tags of this PipelineTemplateResponse.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this PipelineTemplateResponse.


        :param tags: The tags of this PipelineTemplateResponse.  # noqa: E501
        :type: dict(str, str)
        """

        self._tags = tags

    @property
    def yaml(self):
        """Gets the yaml of this PipelineTemplateResponse.  # noqa: E501


        :return: The yaml of this PipelineTemplateResponse.  # noqa: E501
        :rtype: str
        """
        return self._yaml

    @yaml.setter
    def yaml(self, yaml):
        """Sets the yaml of this PipelineTemplateResponse.


        :param yaml: The yaml of this PipelineTemplateResponse.  # noqa: E501
        :type: str
        """
        if yaml is None:
            raise ValueError("Invalid value for `yaml`, must not be `None`")  # noqa: E501

        self._yaml = yaml

    @property
    def version_label(self):
        """Gets the version_label of this PipelineTemplateResponse.  # noqa: E501


        :return: The version_label of this PipelineTemplateResponse.  # noqa: E501
        :rtype: str
        """
        return self._version_label

    @version_label.setter
    def version_label(self, version_label):
        """Sets the version_label of this PipelineTemplateResponse.


        :param version_label: The version_label of this PipelineTemplateResponse.  # noqa: E501
        :type: str
        """

        self._version_label = version_label

    @property
    def is_stable_template(self):
        """Gets the is_stable_template of this PipelineTemplateResponse.  # noqa: E501


        :return: The is_stable_template of this PipelineTemplateResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_stable_template

    @is_stable_template.setter
    def is_stable_template(self, is_stable_template):
        """Sets the is_stable_template of this PipelineTemplateResponse.


        :param is_stable_template: The is_stable_template of this PipelineTemplateResponse.  # noqa: E501
        :type: bool
        """

        self._is_stable_template = is_stable_template

    @property
    def template_entity_type(self):
        """Gets the template_entity_type of this PipelineTemplateResponse.  # noqa: E501


        :return: The template_entity_type of this PipelineTemplateResponse.  # noqa: E501
        :rtype: str
        """
        return self._template_entity_type

    @template_entity_type.setter
    def template_entity_type(self, template_entity_type):
        """Sets the template_entity_type of this PipelineTemplateResponse.


        :param template_entity_type: The template_entity_type of this PipelineTemplateResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["Step", "Stage", "Pipeline", "CustomDeployment", "MonitoredService", "SecretManager", "ArtifactSource", "StepGroup"]  # noqa: E501
        if template_entity_type not in allowed_values:
            raise ValueError(
                "Invalid value for `template_entity_type` ({0}), must be one of {1}"  # noqa: E501
                .format(template_entity_type, allowed_values)
            )

        self._template_entity_type = template_entity_type

    @property
    def child_type(self):
        """Gets the child_type of this PipelineTemplateResponse.  # noqa: E501


        :return: The child_type of this PipelineTemplateResponse.  # noqa: E501
        :rtype: str
        """
        return self._child_type

    @child_type.setter
    def child_type(self, child_type):
        """Sets the child_type of this PipelineTemplateResponse.


        :param child_type: The child_type of this PipelineTemplateResponse.  # noqa: E501
        :type: str
        """

        self._child_type = child_type

    @property
    def template_scope(self):
        """Gets the template_scope of this PipelineTemplateResponse.  # noqa: E501


        :return: The template_scope of this PipelineTemplateResponse.  # noqa: E501
        :rtype: str
        """
        return self._template_scope

    @template_scope.setter
    def template_scope(self, template_scope):
        """Sets the template_scope of this PipelineTemplateResponse.


        :param template_scope: The template_scope of this PipelineTemplateResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["account", "org", "project", "unknown"]  # noqa: E501
        if template_scope not in allowed_values:
            raise ValueError(
                "Invalid value for `template_scope` ({0}), must be one of {1}"  # noqa: E501
                .format(template_scope, allowed_values)
            )

        self._template_scope = template_scope

    @property
    def version(self):
        """Gets the version of this PipelineTemplateResponse.  # noqa: E501


        :return: The version of this PipelineTemplateResponse.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PipelineTemplateResponse.


        :param version: The version of this PipelineTemplateResponse.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def git_details(self):
        """Gets the git_details of this PipelineTemplateResponse.  # noqa: E501


        :return: The git_details of this PipelineTemplateResponse.  # noqa: E501
        :rtype: PipelineEntityGitDetails
        """
        return self._git_details

    @git_details.setter
    def git_details(self, git_details):
        """Sets the git_details of this PipelineTemplateResponse.


        :param git_details: The git_details of this PipelineTemplateResponse.  # noqa: E501
        :type: PipelineEntityGitDetails
        """

        self._git_details = git_details

    @property
    def entity_validity_details(self):
        """Gets the entity_validity_details of this PipelineTemplateResponse.  # noqa: E501


        :return: The entity_validity_details of this PipelineTemplateResponse.  # noqa: E501
        :rtype: PipelineEntityGitDetails
        """
        return self._entity_validity_details

    @entity_validity_details.setter
    def entity_validity_details(self, entity_validity_details):
        """Sets the entity_validity_details of this PipelineTemplateResponse.


        :param entity_validity_details: The entity_validity_details of this PipelineTemplateResponse.  # noqa: E501
        :type: PipelineEntityGitDetails
        """

        self._entity_validity_details = entity_validity_details

    @property
    def last_updated_at(self):
        """Gets the last_updated_at of this PipelineTemplateResponse.  # noqa: E501


        :return: The last_updated_at of this PipelineTemplateResponse.  # noqa: E501
        :rtype: int
        """
        return self._last_updated_at

    @last_updated_at.setter
    def last_updated_at(self, last_updated_at):
        """Sets the last_updated_at of this PipelineTemplateResponse.


        :param last_updated_at: The last_updated_at of this PipelineTemplateResponse.  # noqa: E501
        :type: int
        """

        self._last_updated_at = last_updated_at

    @property
    def store_type(self):
        """Gets the store_type of this PipelineTemplateResponse.  # noqa: E501


        :return: The store_type of this PipelineTemplateResponse.  # noqa: E501
        :rtype: str
        """
        return self._store_type

    @store_type.setter
    def store_type(self, store_type):
        """Sets the store_type of this PipelineTemplateResponse.


        :param store_type: The store_type of this PipelineTemplateResponse.  # noqa: E501
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
    def connector_ref(self):
        """Gets the connector_ref of this PipelineTemplateResponse.  # noqa: E501


        :return: The connector_ref of this PipelineTemplateResponse.  # noqa: E501
        :rtype: str
        """
        return self._connector_ref

    @connector_ref.setter
    def connector_ref(self, connector_ref):
        """Sets the connector_ref of this PipelineTemplateResponse.


        :param connector_ref: The connector_ref of this PipelineTemplateResponse.  # noqa: E501
        :type: str
        """

        self._connector_ref = connector_ref

    @property
    def icon(self):
        """Gets the icon of this PipelineTemplateResponse.  # noqa: E501


        :return: The icon of this PipelineTemplateResponse.  # noqa: E501
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this PipelineTemplateResponse.


        :param icon: The icon of this PipelineTemplateResponse.  # noqa: E501
        :type: str
        """

        self._icon = icon

    @property
    def cache_response_metadata(self):
        """Gets the cache_response_metadata of this PipelineTemplateResponse.  # noqa: E501


        :return: The cache_response_metadata of this PipelineTemplateResponse.  # noqa: E501
        :rtype: CacheResponseMetadata
        """
        return self._cache_response_metadata

    @cache_response_metadata.setter
    def cache_response_metadata(self, cache_response_metadata):
        """Sets the cache_response_metadata of this PipelineTemplateResponse.


        :param cache_response_metadata: The cache_response_metadata of this PipelineTemplateResponse.  # noqa: E501
        :type: CacheResponseMetadata
        """

        self._cache_response_metadata = cache_response_metadata

    @property
    def yaml_version(self):
        """Gets the yaml_version of this PipelineTemplateResponse.  # noqa: E501


        :return: The yaml_version of this PipelineTemplateResponse.  # noqa: E501
        :rtype: str
        """
        return self._yaml_version

    @yaml_version.setter
    def yaml_version(self, yaml_version):
        """Sets the yaml_version of this PipelineTemplateResponse.


        :param yaml_version: The yaml_version of this PipelineTemplateResponse.  # noqa: E501
        :type: str
        """

        self._yaml_version = yaml_version

    @property
    def stable_template(self):
        """Gets the stable_template of this PipelineTemplateResponse.  # noqa: E501


        :return: The stable_template of this PipelineTemplateResponse.  # noqa: E501
        :rtype: bool
        """
        return self._stable_template

    @stable_template.setter
    def stable_template(self, stable_template):
        """Sets the stable_template of this PipelineTemplateResponse.


        :param stable_template: The stable_template of this PipelineTemplateResponse.  # noqa: E501
        :type: bool
        """

        self._stable_template = stable_template

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
        if issubclass(PipelineTemplateResponse, dict):
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
        if not isinstance(other, PipelineTemplateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
