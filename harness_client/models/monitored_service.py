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

class MonitoredService(object):
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
        'org_identifier': 'str',
        'project_identifier': 'str',
        'identifier': 'str',
        'name': 'str',
        'type': 'str',
        'description': 'str',
        'service_ref': 'str',
        'environment_ref': 'str',
        'environment_ref_list': 'list[str]',
        'tags': 'dict(str, str)',
        'sources': 'Sources',
        'dependencies': 'list[ServiceDependencyDTO]',
        'notification_rule_refs': 'list[NotificationRuleRefDTO]',
        'template': 'TemplateDTO',
        'enabled': 'bool'
    }

    attribute_map = {
        'org_identifier': 'orgIdentifier',
        'project_identifier': 'projectIdentifier',
        'identifier': 'identifier',
        'name': 'name',
        'type': 'type',
        'description': 'description',
        'service_ref': 'serviceRef',
        'environment_ref': 'environmentRef',
        'environment_ref_list': 'environmentRefList',
        'tags': 'tags',
        'sources': 'sources',
        'dependencies': 'dependencies',
        'notification_rule_refs': 'notificationRuleRefs',
        'template': 'template',
        'enabled': 'enabled'
    }

    def __init__(self, org_identifier=None, project_identifier=None, identifier=None, name=None, type=None, description=None, service_ref=None, environment_ref=None, environment_ref_list=None, tags=None, sources=None, dependencies=None, notification_rule_refs=None, template=None, enabled=None):  # noqa: E501
        """MonitoredService - a model defined in Swagger"""  # noqa: E501
        self._org_identifier = None
        self._project_identifier = None
        self._identifier = None
        self._name = None
        self._type = None
        self._description = None
        self._service_ref = None
        self._environment_ref = None
        self._environment_ref_list = None
        self._tags = None
        self._sources = None
        self._dependencies = None
        self._notification_rule_refs = None
        self._template = None
        self._enabled = None
        self.discriminator = None
        self.org_identifier = org_identifier
        self.project_identifier = project_identifier
        self.identifier = identifier
        self.name = name
        self.type = type
        if description is not None:
            self.description = description
        self.service_ref = service_ref
        if environment_ref is not None:
            self.environment_ref = environment_ref
        if environment_ref_list is not None:
            self.environment_ref_list = environment_ref_list
        if tags is not None:
            self.tags = tags
        if sources is not None:
            self.sources = sources
        if dependencies is not None:
            self.dependencies = dependencies
        if notification_rule_refs is not None:
            self.notification_rule_refs = notification_rule_refs
        if template is not None:
            self.template = template
        if enabled is not None:
            self.enabled = enabled

    @property
    def org_identifier(self):
        """Gets the org_identifier of this MonitoredService.  # noqa: E501


        :return: The org_identifier of this MonitoredService.  # noqa: E501
        :rtype: str
        """
        return self._org_identifier

    @org_identifier.setter
    def org_identifier(self, org_identifier):
        """Sets the org_identifier of this MonitoredService.


        :param org_identifier: The org_identifier of this MonitoredService.  # noqa: E501
        :type: str
        """
        if org_identifier is None:
            raise ValueError("Invalid value for `org_identifier`, must not be `None`")  # noqa: E501

        self._org_identifier = org_identifier

    @property
    def project_identifier(self):
        """Gets the project_identifier of this MonitoredService.  # noqa: E501


        :return: The project_identifier of this MonitoredService.  # noqa: E501
        :rtype: str
        """
        return self._project_identifier

    @project_identifier.setter
    def project_identifier(self, project_identifier):
        """Sets the project_identifier of this MonitoredService.


        :param project_identifier: The project_identifier of this MonitoredService.  # noqa: E501
        :type: str
        """
        if project_identifier is None:
            raise ValueError("Invalid value for `project_identifier`, must not be `None`")  # noqa: E501

        self._project_identifier = project_identifier

    @property
    def identifier(self):
        """Gets the identifier of this MonitoredService.  # noqa: E501


        :return: The identifier of this MonitoredService.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this MonitoredService.


        :param identifier: The identifier of this MonitoredService.  # noqa: E501
        :type: str
        """
        if identifier is None:
            raise ValueError("Invalid value for `identifier`, must not be `None`")  # noqa: E501

        self._identifier = identifier

    @property
    def name(self):
        """Gets the name of this MonitoredService.  # noqa: E501


        :return: The name of this MonitoredService.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MonitoredService.


        :param name: The name of this MonitoredService.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def type(self):
        """Gets the type of this MonitoredService.  # noqa: E501


        :return: The type of this MonitoredService.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MonitoredService.


        :param type: The type of this MonitoredService.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["Application", "Infrastructure"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def description(self):
        """Gets the description of this MonitoredService.  # noqa: E501


        :return: The description of this MonitoredService.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this MonitoredService.


        :param description: The description of this MonitoredService.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def service_ref(self):
        """Gets the service_ref of this MonitoredService.  # noqa: E501


        :return: The service_ref of this MonitoredService.  # noqa: E501
        :rtype: str
        """
        return self._service_ref

    @service_ref.setter
    def service_ref(self, service_ref):
        """Sets the service_ref of this MonitoredService.


        :param service_ref: The service_ref of this MonitoredService.  # noqa: E501
        :type: str
        """
        if service_ref is None:
            raise ValueError("Invalid value for `service_ref`, must not be `None`")  # noqa: E501

        self._service_ref = service_ref

    @property
    def environment_ref(self):
        """Gets the environment_ref of this MonitoredService.  # noqa: E501


        :return: The environment_ref of this MonitoredService.  # noqa: E501
        :rtype: str
        """
        return self._environment_ref

    @environment_ref.setter
    def environment_ref(self, environment_ref):
        """Sets the environment_ref of this MonitoredService.


        :param environment_ref: The environment_ref of this MonitoredService.  # noqa: E501
        :type: str
        """

        self._environment_ref = environment_ref

    @property
    def environment_ref_list(self):
        """Gets the environment_ref_list of this MonitoredService.  # noqa: E501


        :return: The environment_ref_list of this MonitoredService.  # noqa: E501
        :rtype: list[str]
        """
        return self._environment_ref_list

    @environment_ref_list.setter
    def environment_ref_list(self, environment_ref_list):
        """Sets the environment_ref_list of this MonitoredService.


        :param environment_ref_list: The environment_ref_list of this MonitoredService.  # noqa: E501
        :type: list[str]
        """

        self._environment_ref_list = environment_ref_list

    @property
    def tags(self):
        """Gets the tags of this MonitoredService.  # noqa: E501


        :return: The tags of this MonitoredService.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this MonitoredService.


        :param tags: The tags of this MonitoredService.  # noqa: E501
        :type: dict(str, str)
        """

        self._tags = tags

    @property
    def sources(self):
        """Gets the sources of this MonitoredService.  # noqa: E501


        :return: The sources of this MonitoredService.  # noqa: E501
        :rtype: Sources
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        """Sets the sources of this MonitoredService.


        :param sources: The sources of this MonitoredService.  # noqa: E501
        :type: Sources
        """

        self._sources = sources

    @property
    def dependencies(self):
        """Gets the dependencies of this MonitoredService.  # noqa: E501


        :return: The dependencies of this MonitoredService.  # noqa: E501
        :rtype: list[ServiceDependencyDTO]
        """
        return self._dependencies

    @dependencies.setter
    def dependencies(self, dependencies):
        """Sets the dependencies of this MonitoredService.


        :param dependencies: The dependencies of this MonitoredService.  # noqa: E501
        :type: list[ServiceDependencyDTO]
        """

        self._dependencies = dependencies

    @property
    def notification_rule_refs(self):
        """Gets the notification_rule_refs of this MonitoredService.  # noqa: E501


        :return: The notification_rule_refs of this MonitoredService.  # noqa: E501
        :rtype: list[NotificationRuleRefDTO]
        """
        return self._notification_rule_refs

    @notification_rule_refs.setter
    def notification_rule_refs(self, notification_rule_refs):
        """Sets the notification_rule_refs of this MonitoredService.


        :param notification_rule_refs: The notification_rule_refs of this MonitoredService.  # noqa: E501
        :type: list[NotificationRuleRefDTO]
        """

        self._notification_rule_refs = notification_rule_refs

    @property
    def template(self):
        """Gets the template of this MonitoredService.  # noqa: E501


        :return: The template of this MonitoredService.  # noqa: E501
        :rtype: TemplateDTO
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this MonitoredService.


        :param template: The template of this MonitoredService.  # noqa: E501
        :type: TemplateDTO
        """

        self._template = template

    @property
    def enabled(self):
        """Gets the enabled of this MonitoredService.  # noqa: E501


        :return: The enabled of this MonitoredService.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this MonitoredService.


        :param enabled: The enabled of this MonitoredService.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

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
        if issubclass(MonitoredService, dict):
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
        if not isinstance(other, MonitoredService):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
