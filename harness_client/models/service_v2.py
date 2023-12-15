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

class ServiceV2(object):
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
        'id': 'int',
        'name': 'str',
        'org_id': 'str',
        'account_identifier': 'str',
        'project_id': 'str',
        'fulfilment': 'str',
        'kind': 'str',
        'cloud_account_id': 'str',
        'idle_time_mins': 'int',
        'host_name': 'str',
        'health_check': 'object',
        'custom_domains': 'list[str]',
        'match_all_subdomains': 'bool',
        'disabled': 'bool',
        'routing': 'RoutingDataV2',
        'created_at': 'str',
        'metadata': 'ServiceMetadata',
        'status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'org_id': 'org_id',
        'account_identifier': 'account_identifier',
        'project_id': 'project_id',
        'fulfilment': 'fulfilment',
        'kind': 'kind',
        'cloud_account_id': 'cloud_account_id',
        'idle_time_mins': 'idle_time_mins',
        'host_name': 'host_name',
        'health_check': 'health_check',
        'custom_domains': 'custom_domains',
        'match_all_subdomains': 'match_all_subdomains',
        'disabled': 'disabled',
        'routing': 'routing',
        'created_at': 'created_at',
        'metadata': 'metadata',
        'status': 'status'
    }

    def __init__(self, id=None, name=None, org_id=None, account_identifier=None, project_id=None, fulfilment=None, kind=None, cloud_account_id=None, idle_time_mins=None, host_name=None, health_check=None, custom_domains=None, match_all_subdomains=None, disabled=None, routing=None, created_at=None, metadata=None, status=None):  # noqa: E501
        """ServiceV2 - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._org_id = None
        self._account_identifier = None
        self._project_id = None
        self._fulfilment = None
        self._kind = None
        self._cloud_account_id = None
        self._idle_time_mins = None
        self._host_name = None
        self._health_check = None
        self._custom_domains = None
        self._match_all_subdomains = None
        self._disabled = None
        self._routing = None
        self._created_at = None
        self._metadata = None
        self._status = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.name = name
        self.org_id = org_id
        if account_identifier is not None:
            self.account_identifier = account_identifier
        if project_id is not None:
            self.project_id = project_id
        if fulfilment is not None:
            self.fulfilment = fulfilment
        self.kind = kind
        self.cloud_account_id = cloud_account_id
        if idle_time_mins is not None:
            self.idle_time_mins = idle_time_mins
        if host_name is not None:
            self.host_name = host_name
        if health_check is not None:
            self.health_check = health_check
        if custom_domains is not None:
            self.custom_domains = custom_domains
        if match_all_subdomains is not None:
            self.match_all_subdomains = match_all_subdomains
        if disabled is not None:
            self.disabled = disabled
        if routing is not None:
            self.routing = routing
        if created_at is not None:
            self.created_at = created_at
        if metadata is not None:
            self.metadata = metadata
        if status is not None:
            self.status = status

    @property
    def id(self):
        """Gets the id of this ServiceV2.  # noqa: E501


        :return: The id of this ServiceV2.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ServiceV2.


        :param id: The id of this ServiceV2.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ServiceV2.  # noqa: E501


        :return: The name of this ServiceV2.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ServiceV2.


        :param name: The name of this ServiceV2.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def org_id(self):
        """Gets the org_id of this ServiceV2.  # noqa: E501


        :return: The org_id of this ServiceV2.  # noqa: E501
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this ServiceV2.


        :param org_id: The org_id of this ServiceV2.  # noqa: E501
        :type: str
        """
        if org_id is None:
            raise ValueError("Invalid value for `org_id`, must not be `None`")  # noqa: E501

        self._org_id = org_id

    @property
    def account_identifier(self):
        """Gets the account_identifier of this ServiceV2.  # noqa: E501


        :return: The account_identifier of this ServiceV2.  # noqa: E501
        :rtype: str
        """
        return self._account_identifier

    @account_identifier.setter
    def account_identifier(self, account_identifier):
        """Sets the account_identifier of this ServiceV2.


        :param account_identifier: The account_identifier of this ServiceV2.  # noqa: E501
        :type: str
        """

        self._account_identifier = account_identifier

    @property
    def project_id(self):
        """Gets the project_id of this ServiceV2.  # noqa: E501


        :return: The project_id of this ServiceV2.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ServiceV2.


        :param project_id: The project_id of this ServiceV2.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def fulfilment(self):
        """Gets the fulfilment of this ServiceV2.  # noqa: E501


        :return: The fulfilment of this ServiceV2.  # noqa: E501
        :rtype: str
        """
        return self._fulfilment

    @fulfilment.setter
    def fulfilment(self, fulfilment):
        """Sets the fulfilment of this ServiceV2.


        :param fulfilment: The fulfilment of this ServiceV2.  # noqa: E501
        :type: str
        """

        self._fulfilment = fulfilment

    @property
    def kind(self):
        """Gets the kind of this ServiceV2.  # noqa: E501


        :return: The kind of this ServiceV2.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this ServiceV2.


        :param kind: The kind of this ServiceV2.  # noqa: E501
        :type: str
        """
        if kind is None:
            raise ValueError("Invalid value for `kind`, must not be `None`")  # noqa: E501

        self._kind = kind

    @property
    def cloud_account_id(self):
        """Gets the cloud_account_id of this ServiceV2.  # noqa: E501


        :return: The cloud_account_id of this ServiceV2.  # noqa: E501
        :rtype: str
        """
        return self._cloud_account_id

    @cloud_account_id.setter
    def cloud_account_id(self, cloud_account_id):
        """Sets the cloud_account_id of this ServiceV2.


        :param cloud_account_id: The cloud_account_id of this ServiceV2.  # noqa: E501
        :type: str
        """
        if cloud_account_id is None:
            raise ValueError("Invalid value for `cloud_account_id`, must not be `None`")  # noqa: E501

        self._cloud_account_id = cloud_account_id

    @property
    def idle_time_mins(self):
        """Gets the idle_time_mins of this ServiceV2.  # noqa: E501


        :return: The idle_time_mins of this ServiceV2.  # noqa: E501
        :rtype: int
        """
        return self._idle_time_mins

    @idle_time_mins.setter
    def idle_time_mins(self, idle_time_mins):
        """Sets the idle_time_mins of this ServiceV2.


        :param idle_time_mins: The idle_time_mins of this ServiceV2.  # noqa: E501
        :type: int
        """

        self._idle_time_mins = idle_time_mins

    @property
    def host_name(self):
        """Gets the host_name of this ServiceV2.  # noqa: E501


        :return: The host_name of this ServiceV2.  # noqa: E501
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this ServiceV2.


        :param host_name: The host_name of this ServiceV2.  # noqa: E501
        :type: str
        """

        self._host_name = host_name

    @property
    def health_check(self):
        """Gets the health_check of this ServiceV2.  # noqa: E501


        :return: The health_check of this ServiceV2.  # noqa: E501
        :rtype: object
        """
        return self._health_check

    @health_check.setter
    def health_check(self, health_check):
        """Sets the health_check of this ServiceV2.


        :param health_check: The health_check of this ServiceV2.  # noqa: E501
        :type: object
        """

        self._health_check = health_check

    @property
    def custom_domains(self):
        """Gets the custom_domains of this ServiceV2.  # noqa: E501


        :return: The custom_domains of this ServiceV2.  # noqa: E501
        :rtype: list[str]
        """
        return self._custom_domains

    @custom_domains.setter
    def custom_domains(self, custom_domains):
        """Sets the custom_domains of this ServiceV2.


        :param custom_domains: The custom_domains of this ServiceV2.  # noqa: E501
        :type: list[str]
        """

        self._custom_domains = custom_domains

    @property
    def match_all_subdomains(self):
        """Gets the match_all_subdomains of this ServiceV2.  # noqa: E501


        :return: The match_all_subdomains of this ServiceV2.  # noqa: E501
        :rtype: bool
        """
        return self._match_all_subdomains

    @match_all_subdomains.setter
    def match_all_subdomains(self, match_all_subdomains):
        """Sets the match_all_subdomains of this ServiceV2.


        :param match_all_subdomains: The match_all_subdomains of this ServiceV2.  # noqa: E501
        :type: bool
        """

        self._match_all_subdomains = match_all_subdomains

    @property
    def disabled(self):
        """Gets the disabled of this ServiceV2.  # noqa: E501


        :return: The disabled of this ServiceV2.  # noqa: E501
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this ServiceV2.


        :param disabled: The disabled of this ServiceV2.  # noqa: E501
        :type: bool
        """

        self._disabled = disabled

    @property
    def routing(self):
        """Gets the routing of this ServiceV2.  # noqa: E501


        :return: The routing of this ServiceV2.  # noqa: E501
        :rtype: RoutingDataV2
        """
        return self._routing

    @routing.setter
    def routing(self, routing):
        """Sets the routing of this ServiceV2.


        :param routing: The routing of this ServiceV2.  # noqa: E501
        :type: RoutingDataV2
        """

        self._routing = routing

    @property
    def created_at(self):
        """Gets the created_at of this ServiceV2.  # noqa: E501


        :return: The created_at of this ServiceV2.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ServiceV2.


        :param created_at: The created_at of this ServiceV2.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def metadata(self):
        """Gets the metadata of this ServiceV2.  # noqa: E501


        :return: The metadata of this ServiceV2.  # noqa: E501
        :rtype: ServiceMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this ServiceV2.


        :param metadata: The metadata of this ServiceV2.  # noqa: E501
        :type: ServiceMetadata
        """

        self._metadata = metadata

    @property
    def status(self):
        """Gets the status of this ServiceV2.  # noqa: E501


        :return: The status of this ServiceV2.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ServiceV2.


        :param status: The status of this ServiceV2.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if issubclass(ServiceV2, dict):
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
        if not isinstance(other, ServiceV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
