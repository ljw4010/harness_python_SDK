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

class TemplateFilterProperties(object):
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
        'tags': 'dict(str, str)',
        'filter_type': 'str',
        'template_names': 'list[str]',
        'template_identifiers': 'list[str]',
        'description': 'str',
        'template_entity_types': 'list[str]',
        'child_types': 'list[str]',
        'listing_scope': 'TemplateScope',
        'repo_name': 'str'
    }

    attribute_map = {
        'tags': 'tags',
        'filter_type': 'filterType',
        'template_names': 'templateNames',
        'template_identifiers': 'templateIdentifiers',
        'description': 'description',
        'template_entity_types': 'templateEntityTypes',
        'child_types': 'childTypes',
        'listing_scope': 'listingScope',
        'repo_name': 'repoName'
    }

    def __init__(self, tags=None, filter_type=None, template_names=None, template_identifiers=None, description=None, template_entity_types=None, child_types=None, listing_scope=None, repo_name=None):  # noqa: E501
        """TemplateFilterProperties - a model defined in Swagger"""  # noqa: E501
        self._tags = None
        self._filter_type = None
        self._template_names = None
        self._template_identifiers = None
        self._description = None
        self._template_entity_types = None
        self._child_types = None
        self._listing_scope = None
        self._repo_name = None
        self.discriminator = None
        if tags is not None:
            self.tags = tags
        self.filter_type = filter_type
        if template_names is not None:
            self.template_names = template_names
        if template_identifiers is not None:
            self.template_identifiers = template_identifiers
        if description is not None:
            self.description = description
        if template_entity_types is not None:
            self.template_entity_types = template_entity_types
        if child_types is not None:
            self.child_types = child_types
        if listing_scope is not None:
            self.listing_scope = listing_scope
        if repo_name is not None:
            self.repo_name = repo_name

    @property
    def tags(self):
        """Gets the tags of this TemplateFilterProperties.  # noqa: E501

        Filter tags as a key-value pair.  # noqa: E501

        :return: The tags of this TemplateFilterProperties.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this TemplateFilterProperties.

        Filter tags as a key-value pair.  # noqa: E501

        :param tags: The tags of this TemplateFilterProperties.  # noqa: E501
        :type: dict(str, str)
        """

        self._tags = tags

    @property
    def filter_type(self):
        """Gets the filter_type of this TemplateFilterProperties.  # noqa: E501

        This specifies the corresponding Entity of the filter.  # noqa: E501

        :return: The filter_type of this TemplateFilterProperties.  # noqa: E501
        :rtype: str
        """
        return self._filter_type

    @filter_type.setter
    def filter_type(self, filter_type):
        """Sets the filter_type of this TemplateFilterProperties.

        This specifies the corresponding Entity of the filter.  # noqa: E501

        :param filter_type: The filter_type of this TemplateFilterProperties.  # noqa: E501
        :type: str
        """
        if filter_type is None:
            raise ValueError("Invalid value for `filter_type`, must not be `None`")  # noqa: E501
        allowed_values = ["Connector", "DelegateProfile", "Delegate", "PipelineSetup", "PipelineExecution", "Deployment", "Audit", "Template", "Trigger", "EnvironmentGroup", "FileStore", "CCMRecommendation", "Anomaly", "Environment", "RuleExecution", "Override", "InputSet"]  # noqa: E501
        if filter_type not in allowed_values:
            raise ValueError(
                "Invalid value for `filter_type` ({0}), must be one of {1}"  # noqa: E501
                .format(filter_type, allowed_values)
            )

        self._filter_type = filter_type

    @property
    def template_names(self):
        """Gets the template_names of this TemplateFilterProperties.  # noqa: E501


        :return: The template_names of this TemplateFilterProperties.  # noqa: E501
        :rtype: list[str]
        """
        return self._template_names

    @template_names.setter
    def template_names(self, template_names):
        """Sets the template_names of this TemplateFilterProperties.


        :param template_names: The template_names of this TemplateFilterProperties.  # noqa: E501
        :type: list[str]
        """

        self._template_names = template_names

    @property
    def template_identifiers(self):
        """Gets the template_identifiers of this TemplateFilterProperties.  # noqa: E501


        :return: The template_identifiers of this TemplateFilterProperties.  # noqa: E501
        :rtype: list[str]
        """
        return self._template_identifiers

    @template_identifiers.setter
    def template_identifiers(self, template_identifiers):
        """Sets the template_identifiers of this TemplateFilterProperties.


        :param template_identifiers: The template_identifiers of this TemplateFilterProperties.  # noqa: E501
        :type: list[str]
        """

        self._template_identifiers = template_identifiers

    @property
    def description(self):
        """Gets the description of this TemplateFilterProperties.  # noqa: E501


        :return: The description of this TemplateFilterProperties.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TemplateFilterProperties.


        :param description: The description of this TemplateFilterProperties.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def template_entity_types(self):
        """Gets the template_entity_types of this TemplateFilterProperties.  # noqa: E501


        :return: The template_entity_types of this TemplateFilterProperties.  # noqa: E501
        :rtype: list[str]
        """
        return self._template_entity_types

    @template_entity_types.setter
    def template_entity_types(self, template_entity_types):
        """Sets the template_entity_types of this TemplateFilterProperties.


        :param template_entity_types: The template_entity_types of this TemplateFilterProperties.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["Step", "Stage", "Pipeline", "CustomDeployment", "MonitoredService", "SecretManager", "ArtifactSource", "StepGroup"]  # noqa: E501
        if not set(template_entity_types).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `template_entity_types` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(template_entity_types) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._template_entity_types = template_entity_types

    @property
    def child_types(self):
        """Gets the child_types of this TemplateFilterProperties.  # noqa: E501


        :return: The child_types of this TemplateFilterProperties.  # noqa: E501
        :rtype: list[str]
        """
        return self._child_types

    @child_types.setter
    def child_types(self, child_types):
        """Sets the child_types of this TemplateFilterProperties.


        :param child_types: The child_types of this TemplateFilterProperties.  # noqa: E501
        :type: list[str]
        """

        self._child_types = child_types

    @property
    def listing_scope(self):
        """Gets the listing_scope of this TemplateFilterProperties.  # noqa: E501


        :return: The listing_scope of this TemplateFilterProperties.  # noqa: E501
        :rtype: TemplateScope
        """
        return self._listing_scope

    @listing_scope.setter
    def listing_scope(self, listing_scope):
        """Sets the listing_scope of this TemplateFilterProperties.


        :param listing_scope: The listing_scope of this TemplateFilterProperties.  # noqa: E501
        :type: TemplateScope
        """

        self._listing_scope = listing_scope

    @property
    def repo_name(self):
        """Gets the repo_name of this TemplateFilterProperties.  # noqa: E501


        :return: The repo_name of this TemplateFilterProperties.  # noqa: E501
        :rtype: str
        """
        return self._repo_name

    @repo_name.setter
    def repo_name(self, repo_name):
        """Sets the repo_name of this TemplateFilterProperties.


        :param repo_name: The repo_name of this TemplateFilterProperties.  # noqa: E501
        :type: str
        """

        self._repo_name = repo_name

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
        if issubclass(TemplateFilterProperties, dict):
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
        if not isinstance(other, TemplateFilterProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
