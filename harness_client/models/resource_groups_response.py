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

class ResourceGroupsResponse(object):
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
        'identifier': 'str',
        'name': 'str',
        'color': 'str',
        'tags': 'dict(str, str)',
        'description': 'str',
        'allowed_scope_levels': 'list[str]',
        'included_scope': 'list[ResourceGroupScope]',
        'resource_filter': 'list[ResourceFilter]',
        'include_all_resources': 'bool',
        'harness_managed': 'bool',
        'created': 'int',
        'updated': 'int'
    }

    attribute_map = {
        'identifier': 'identifier',
        'name': 'name',
        'color': 'color',
        'tags': 'tags',
        'description': 'description',
        'allowed_scope_levels': 'allowed_scope_levels',
        'included_scope': 'included_scope',
        'resource_filter': 'resource_filter',
        'include_all_resources': 'include_all_resources',
        'harness_managed': 'harness_managed',
        'created': 'created',
        'updated': 'updated'
    }

    def __init__(self, identifier=None, name=None, color=None, tags=None, description=None, allowed_scope_levels=None, included_scope=None, resource_filter=None, include_all_resources=None, harness_managed=None, created=None, updated=None):  # noqa: E501
        """ResourceGroupsResponse - a model defined in Swagger"""  # noqa: E501
        self._identifier = None
        self._name = None
        self._color = None
        self._tags = None
        self._description = None
        self._allowed_scope_levels = None
        self._included_scope = None
        self._resource_filter = None
        self._include_all_resources = None
        self._harness_managed = None
        self._created = None
        self._updated = None
        self.discriminator = None
        self.identifier = identifier
        self.name = name
        if color is not None:
            self.color = color
        if tags is not None:
            self.tags = tags
        if description is not None:
            self.description = description
        if allowed_scope_levels is not None:
            self.allowed_scope_levels = allowed_scope_levels
        if included_scope is not None:
            self.included_scope = included_scope
        if resource_filter is not None:
            self.resource_filter = resource_filter
        if include_all_resources is not None:
            self.include_all_resources = include_all_resources
        if harness_managed is not None:
            self.harness_managed = harness_managed
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated

    @property
    def identifier(self):
        """Gets the identifier of this ResourceGroupsResponse.  # noqa: E501

        Resource Group Identifier  # noqa: E501

        :return: The identifier of this ResourceGroupsResponse.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this ResourceGroupsResponse.

        Resource Group Identifier  # noqa: E501

        :param identifier: The identifier of this ResourceGroupsResponse.  # noqa: E501
        :type: str
        """
        if identifier is None:
            raise ValueError("Invalid value for `identifier`, must not be `None`")  # noqa: E501

        self._identifier = identifier

    @property
    def name(self):
        """Gets the name of this ResourceGroupsResponse.  # noqa: E501

        Resource Group Name  # noqa: E501

        :return: The name of this ResourceGroupsResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ResourceGroupsResponse.

        Resource Group Name  # noqa: E501

        :param name: The name of this ResourceGroupsResponse.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def color(self):
        """Gets the color of this ResourceGroupsResponse.  # noqa: E501

        Color associated with the Resource Group.  # noqa: E501

        :return: The color of this ResourceGroupsResponse.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this ResourceGroupsResponse.

        Color associated with the Resource Group.  # noqa: E501

        :param color: The color of this ResourceGroupsResponse.  # noqa: E501
        :type: str
        """

        self._color = color

    @property
    def tags(self):
        """Gets the tags of this ResourceGroupsResponse.  # noqa: E501

        Resource Group tags  # noqa: E501

        :return: The tags of this ResourceGroupsResponse.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ResourceGroupsResponse.

        Resource Group tags  # noqa: E501

        :param tags: The tags of this ResourceGroupsResponse.  # noqa: E501
        :type: dict(str, str)
        """

        self._tags = tags

    @property
    def description(self):
        """Gets the description of this ResourceGroupsResponse.  # noqa: E501

        Resource Group description  # noqa: E501

        :return: The description of this ResourceGroupsResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ResourceGroupsResponse.

        Resource Group description  # noqa: E501

        :param description: The description of this ResourceGroupsResponse.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def allowed_scope_levels(self):
        """Gets the allowed_scope_levels of this ResourceGroupsResponse.  # noqa: E501

        Allowed scope levels for this Resource Group.  # noqa: E501

        :return: The allowed_scope_levels of this ResourceGroupsResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._allowed_scope_levels

    @allowed_scope_levels.setter
    def allowed_scope_levels(self, allowed_scope_levels):
        """Sets the allowed_scope_levels of this ResourceGroupsResponse.

        Allowed scope levels for this Resource Group.  # noqa: E501

        :param allowed_scope_levels: The allowed_scope_levels of this ResourceGroupsResponse.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["account", "organization", "project"]  # noqa: E501
        if not set(allowed_scope_levels).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `allowed_scope_levels` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(allowed_scope_levels) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._allowed_scope_levels = allowed_scope_levels

    @property
    def included_scope(self):
        """Gets the included_scope of this ResourceGroupsResponse.  # noqa: E501

        Included scopes for the resources belonging to the Resource Group.  # noqa: E501

        :return: The included_scope of this ResourceGroupsResponse.  # noqa: E501
        :rtype: list[ResourceGroupScope]
        """
        return self._included_scope

    @included_scope.setter
    def included_scope(self, included_scope):
        """Sets the included_scope of this ResourceGroupsResponse.

        Included scopes for the resources belonging to the Resource Group.  # noqa: E501

        :param included_scope: The included_scope of this ResourceGroupsResponse.  # noqa: E501
        :type: list[ResourceGroupScope]
        """

        self._included_scope = included_scope

    @property
    def resource_filter(self):
        """Gets the resource_filter of this ResourceGroupsResponse.  # noqa: E501

        Specifies the actual resources present in the Resource Group.  # noqa: E501

        :return: The resource_filter of this ResourceGroupsResponse.  # noqa: E501
        :rtype: list[ResourceFilter]
        """
        return self._resource_filter

    @resource_filter.setter
    def resource_filter(self, resource_filter):
        """Sets the resource_filter of this ResourceGroupsResponse.

        Specifies the actual resources present in the Resource Group.  # noqa: E501

        :param resource_filter: The resource_filter of this ResourceGroupsResponse.  # noqa: E501
        :type: list[ResourceFilter]
        """

        self._resource_filter = resource_filter

    @property
    def include_all_resources(self):
        """Gets the include_all_resources of this ResourceGroupsResponse.  # noqa: E501

        Boolean value for including all resources in Resource Group.  # noqa: E501

        :return: The include_all_resources of this ResourceGroupsResponse.  # noqa: E501
        :rtype: bool
        """
        return self._include_all_resources

    @include_all_resources.setter
    def include_all_resources(self, include_all_resources):
        """Sets the include_all_resources of this ResourceGroupsResponse.

        Boolean value for including all resources in Resource Group.  # noqa: E501

        :param include_all_resources: The include_all_resources of this ResourceGroupsResponse.  # noqa: E501
        :type: bool
        """

        self._include_all_resources = include_all_resources

    @property
    def harness_managed(self):
        """Gets the harness_managed of this ResourceGroupsResponse.  # noqa: E501

        This indicates if this Resource Group is managed by Harness or not. If true, Harness can manage and modify this Resource Group.  # noqa: E501

        :return: The harness_managed of this ResourceGroupsResponse.  # noqa: E501
        :rtype: bool
        """
        return self._harness_managed

    @harness_managed.setter
    def harness_managed(self, harness_managed):
        """Sets the harness_managed of this ResourceGroupsResponse.

        This indicates if this Resource Group is managed by Harness or not. If true, Harness can manage and modify this Resource Group.  # noqa: E501

        :param harness_managed: The harness_managed of this ResourceGroupsResponse.  # noqa: E501
        :type: bool
        """

        self._harness_managed = harness_managed

    @property
    def created(self):
        """Gets the created of this ResourceGroupsResponse.  # noqa: E501

        Creation timestamp for Resource Group.  # noqa: E501

        :return: The created of this ResourceGroupsResponse.  # noqa: E501
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ResourceGroupsResponse.

        Creation timestamp for Resource Group.  # noqa: E501

        :param created: The created of this ResourceGroupsResponse.  # noqa: E501
        :type: int
        """

        self._created = created

    @property
    def updated(self):
        """Gets the updated of this ResourceGroupsResponse.  # noqa: E501

        Last modification timestamp for Resource Group.  # noqa: E501

        :return: The updated of this ResourceGroupsResponse.  # noqa: E501
        :rtype: int
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this ResourceGroupsResponse.

        Last modification timestamp for Resource Group.  # noqa: E501

        :param updated: The updated of this ResourceGroupsResponse.  # noqa: E501
        :type: int
        """

        self._updated = updated

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
        if issubclass(ResourceGroupsResponse, dict):
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
        if not isinstance(other, ResourceGroupsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
