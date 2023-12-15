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

class TemplateResponse(object):
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
        'account': 'str',
        'org': 'str',
        'project': 'str',
        'identifier': 'str',
        'name': 'str',
        'description': 'str',
        'tags': 'dict(str, str)',
        'yaml': 'str',
        'version_label': 'str',
        'entity_type': 'str',
        'child_type': 'str',
        'scope': 'str',
        'version': 'int',
        'git_details': 'EntityGitDetails',
        'updated': 'int',
        'store_type': 'str',
        'connector_ref': 'str',
        'stable_template': 'bool'
    }

    attribute_map = {
        'account': 'account',
        'org': 'org',
        'project': 'project',
        'identifier': 'identifier',
        'name': 'name',
        'description': 'description',
        'tags': 'tags',
        'yaml': 'yaml',
        'version_label': 'version_label',
        'entity_type': 'entity_type',
        'child_type': 'child_type',
        'scope': 'scope',
        'version': 'version',
        'git_details': 'git_details',
        'updated': 'updated',
        'store_type': 'store_type',
        'connector_ref': 'connector_ref',
        'stable_template': 'stable_template'
    }

    def __init__(self, account=None, org=None, project=None, identifier=None, name=None, description=None, tags=None, yaml=None, version_label=None, entity_type=None, child_type=None, scope=None, version=None, git_details=None, updated=None, store_type=None, connector_ref=None, stable_template=None):  # noqa: E501
        """TemplateResponse - a model defined in Swagger"""  # noqa: E501
        self._account = None
        self._org = None
        self._project = None
        self._identifier = None
        self._name = None
        self._description = None
        self._tags = None
        self._yaml = None
        self._version_label = None
        self._entity_type = None
        self._child_type = None
        self._scope = None
        self._version = None
        self._git_details = None
        self._updated = None
        self._store_type = None
        self._connector_ref = None
        self._stable_template = None
        self.discriminator = None
        self.account = account
        if org is not None:
            self.org = org
        if project is not None:
            self.project = project
        self.identifier = identifier
        self.name = name
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags
        self.yaml = yaml
        if version_label is not None:
            self.version_label = version_label
        if entity_type is not None:
            self.entity_type = entity_type
        if child_type is not None:
            self.child_type = child_type
        if scope is not None:
            self.scope = scope
        if version is not None:
            self.version = version
        if git_details is not None:
            self.git_details = git_details
        if updated is not None:
            self.updated = updated
        if store_type is not None:
            self.store_type = store_type
        if connector_ref is not None:
            self.connector_ref = connector_ref
        if stable_template is not None:
            self.stable_template = stable_template

    @property
    def account(self):
        """Gets the account of this TemplateResponse.  # noqa: E501

        Account identifier  # noqa: E501

        :return: The account of this TemplateResponse.  # noqa: E501
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this TemplateResponse.

        Account identifier  # noqa: E501

        :param account: The account of this TemplateResponse.  # noqa: E501
        :type: str
        """
        if account is None:
            raise ValueError("Invalid value for `account`, must not be `None`")  # noqa: E501

        self._account = account

    @property
    def org(self):
        """Gets the org of this TemplateResponse.  # noqa: E501

        Organization identifier  # noqa: E501

        :return: The org of this TemplateResponse.  # noqa: E501
        :rtype: str
        """
        return self._org

    @org.setter
    def org(self, org):
        """Sets the org of this TemplateResponse.

        Organization identifier  # noqa: E501

        :param org: The org of this TemplateResponse.  # noqa: E501
        :type: str
        """

        self._org = org

    @property
    def project(self):
        """Gets the project of this TemplateResponse.  # noqa: E501

        Project identifier  # noqa: E501

        :return: The project of this TemplateResponse.  # noqa: E501
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this TemplateResponse.

        Project identifier  # noqa: E501

        :param project: The project of this TemplateResponse.  # noqa: E501
        :type: str
        """

        self._project = project

    @property
    def identifier(self):
        """Gets the identifier of this TemplateResponse.  # noqa: E501

        Template identifier  # noqa: E501

        :return: The identifier of this TemplateResponse.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this TemplateResponse.

        Template identifier  # noqa: E501

        :param identifier: The identifier of this TemplateResponse.  # noqa: E501
        :type: str
        """
        if identifier is None:
            raise ValueError("Invalid value for `identifier`, must not be `None`")  # noqa: E501

        self._identifier = identifier

    @property
    def name(self):
        """Gets the name of this TemplateResponse.  # noqa: E501

        Template Name  # noqa: E501

        :return: The name of this TemplateResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TemplateResponse.

        Template Name  # noqa: E501

        :param name: The name of this TemplateResponse.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this TemplateResponse.  # noqa: E501

        Template description  # noqa: E501

        :return: The description of this TemplateResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TemplateResponse.

        Template description  # noqa: E501

        :param description: The description of this TemplateResponse.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def tags(self):
        """Gets the tags of this TemplateResponse.  # noqa: E501

        Template tags  # noqa: E501

        :return: The tags of this TemplateResponse.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this TemplateResponse.

        Template tags  # noqa: E501

        :param tags: The tags of this TemplateResponse.  # noqa: E501
        :type: dict(str, str)
        """

        self._tags = tags

    @property
    def yaml(self):
        """Gets the yaml of this TemplateResponse.  # noqa: E501

        Yaml related to template  # noqa: E501

        :return: The yaml of this TemplateResponse.  # noqa: E501
        :rtype: str
        """
        return self._yaml

    @yaml.setter
    def yaml(self, yaml):
        """Sets the yaml of this TemplateResponse.

        Yaml related to template  # noqa: E501

        :param yaml: The yaml of this TemplateResponse.  # noqa: E501
        :type: str
        """
        if yaml is None:
            raise ValueError("Invalid value for `yaml`, must not be `None`")  # noqa: E501

        self._yaml = yaml

    @property
    def version_label(self):
        """Gets the version_label of this TemplateResponse.  # noqa: E501

        Version label of template  # noqa: E501

        :return: The version_label of this TemplateResponse.  # noqa: E501
        :rtype: str
        """
        return self._version_label

    @version_label.setter
    def version_label(self, version_label):
        """Sets the version_label of this TemplateResponse.

        Version label of template  # noqa: E501

        :param version_label: The version_label of this TemplateResponse.  # noqa: E501
        :type: str
        """

        self._version_label = version_label

    @property
    def entity_type(self):
        """Gets the entity_type of this TemplateResponse.  # noqa: E501

        Type of Template   # noqa: E501

        :return: The entity_type of this TemplateResponse.  # noqa: E501
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this TemplateResponse.

        Type of Template   # noqa: E501

        :param entity_type: The entity_type of this TemplateResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["Step", "Stage", "Pipeline", "CustomDeployment", "MonitoredService", "SecretManager"]  # noqa: E501
        if entity_type not in allowed_values:
            raise ValueError(
                "Invalid value for `entity_type` ({0}), must be one of {1}"  # noqa: E501
                .format(entity_type, allowed_values)
            )

        self._entity_type = entity_type

    @property
    def child_type(self):
        """Gets the child_type of this TemplateResponse.  # noqa: E501

        Defines child template type  # noqa: E501

        :return: The child_type of this TemplateResponse.  # noqa: E501
        :rtype: str
        """
        return self._child_type

    @child_type.setter
    def child_type(self, child_type):
        """Sets the child_type of this TemplateResponse.

        Defines child template type  # noqa: E501

        :param child_type: The child_type of this TemplateResponse.  # noqa: E501
        :type: str
        """

        self._child_type = child_type

    @property
    def scope(self):
        """Gets the scope of this TemplateResponse.  # noqa: E501

        Scope of template  # noqa: E501

        :return: The scope of this TemplateResponse.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this TemplateResponse.

        Scope of template  # noqa: E501

        :param scope: The scope of this TemplateResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["org", "project", "account", "unknown"]  # noqa: E501
        if scope not in allowed_values:
            raise ValueError(
                "Invalid value for `scope` ({0}), must be one of {1}"  # noqa: E501
                .format(scope, allowed_values)
            )

        self._scope = scope

    @property
    def version(self):
        """Gets the version of this TemplateResponse.  # noqa: E501

        Version of template  # noqa: E501

        :return: The version of this TemplateResponse.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this TemplateResponse.

        Version of template  # noqa: E501

        :param version: The version of this TemplateResponse.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def git_details(self):
        """Gets the git_details of this TemplateResponse.  # noqa: E501


        :return: The git_details of this TemplateResponse.  # noqa: E501
        :rtype: EntityGitDetails
        """
        return self._git_details

    @git_details.setter
    def git_details(self, git_details):
        """Sets the git_details of this TemplateResponse.


        :param git_details: The git_details of this TemplateResponse.  # noqa: E501
        :type: EntityGitDetails
        """

        self._git_details = git_details

    @property
    def updated(self):
        """Gets the updated of this TemplateResponse.  # noqa: E501

        Last modification timestamp for Service.   # noqa: E501

        :return: The updated of this TemplateResponse.  # noqa: E501
        :rtype: int
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this TemplateResponse.

        Last modification timestamp for Service.   # noqa: E501

        :param updated: The updated of this TemplateResponse.  # noqa: E501
        :type: int
        """

        self._updated = updated

    @property
    def store_type(self):
        """Gets the store_type of this TemplateResponse.  # noqa: E501

        Specifies whether the Entity is to be stored in Git or not (for Git Experience).  # noqa: E501

        :return: The store_type of this TemplateResponse.  # noqa: E501
        :rtype: str
        """
        return self._store_type

    @store_type.setter
    def store_type(self, store_type):
        """Sets the store_type of this TemplateResponse.

        Specifies whether the Entity is to be stored in Git or not (for Git Experience).  # noqa: E501

        :param store_type: The store_type of this TemplateResponse.  # noqa: E501
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
        """Gets the connector_ref of this TemplateResponse.  # noqa: E501

        Identifier of the Harness Connector used for CRUD operations on the Entity (for Git Experience).  # noqa: E501

        :return: The connector_ref of this TemplateResponse.  # noqa: E501
        :rtype: str
        """
        return self._connector_ref

    @connector_ref.setter
    def connector_ref(self, connector_ref):
        """Sets the connector_ref of this TemplateResponse.

        Identifier of the Harness Connector used for CRUD operations on the Entity (for Git Experience).  # noqa: E501

        :param connector_ref: The connector_ref of this TemplateResponse.  # noqa: E501
        :type: str
        """

        self._connector_ref = connector_ref

    @property
    def stable_template(self):
        """Gets the stable_template of this TemplateResponse.  # noqa: E501

        True if this version is stable version of Template  # noqa: E501

        :return: The stable_template of this TemplateResponse.  # noqa: E501
        :rtype: bool
        """
        return self._stable_template

    @stable_template.setter
    def stable_template(self, stable_template):
        """Sets the stable_template of this TemplateResponse.

        True if this version is stable version of Template  # noqa: E501

        :param stable_template: The stable_template of this TemplateResponse.  # noqa: E501
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
        if issubclass(TemplateResponse, dict):
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
        if not isinstance(other, TemplateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
