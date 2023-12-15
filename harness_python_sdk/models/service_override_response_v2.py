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

class ServiceOverrideResponseV2(object):
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
        'account_id': 'str',
        'org_identifier': 'str',
        'project_identifier': 'str',
        'environment_ref': 'str',
        'service_ref': 'str',
        'infra_identifier': 'str',
        'cluster_identifier': 'str',
        'type': 'str',
        'spec': 'ServiceOverrideSpec',
        'is_newly_created': 'bool',
        'yaml_internal': 'str',
        'newly_created': 'bool'
    }

    attribute_map = {
        'identifier': 'identifier',
        'account_id': 'accountId',
        'org_identifier': 'orgIdentifier',
        'project_identifier': 'projectIdentifier',
        'environment_ref': 'environmentRef',
        'service_ref': 'serviceRef',
        'infra_identifier': 'infraIdentifier',
        'cluster_identifier': 'clusterIdentifier',
        'type': 'type',
        'spec': 'spec',
        'is_newly_created': 'isNewlyCreated',
        'yaml_internal': 'yamlInternal',
        'newly_created': 'newlyCreated'
    }

    def __init__(self, identifier=None, account_id=None, org_identifier=None, project_identifier=None, environment_ref=None, service_ref=None, infra_identifier=None, cluster_identifier=None, type=None, spec=None, is_newly_created=None, yaml_internal=None, newly_created=None):  # noqa: E501
        """ServiceOverrideResponseV2 - a model defined in Swagger"""  # noqa: E501
        self._identifier = None
        self._account_id = None
        self._org_identifier = None
        self._project_identifier = None
        self._environment_ref = None
        self._service_ref = None
        self._infra_identifier = None
        self._cluster_identifier = None
        self._type = None
        self._spec = None
        self._is_newly_created = None
        self._yaml_internal = None
        self._newly_created = None
        self.discriminator = None
        if identifier is not None:
            self.identifier = identifier
        if account_id is not None:
            self.account_id = account_id
        if org_identifier is not None:
            self.org_identifier = org_identifier
        if project_identifier is not None:
            self.project_identifier = project_identifier
        if environment_ref is not None:
            self.environment_ref = environment_ref
        if service_ref is not None:
            self.service_ref = service_ref
        if infra_identifier is not None:
            self.infra_identifier = infra_identifier
        if cluster_identifier is not None:
            self.cluster_identifier = cluster_identifier
        if type is not None:
            self.type = type
        if spec is not None:
            self.spec = spec
        if is_newly_created is not None:
            self.is_newly_created = is_newly_created
        if yaml_internal is not None:
            self.yaml_internal = yaml_internal
        if newly_created is not None:
            self.newly_created = newly_created

    @property
    def identifier(self):
        """Gets the identifier of this ServiceOverrideResponseV2.  # noqa: E501


        :return: The identifier of this ServiceOverrideResponseV2.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this ServiceOverrideResponseV2.


        :param identifier: The identifier of this ServiceOverrideResponseV2.  # noqa: E501
        :type: str
        """

        self._identifier = identifier

    @property
    def account_id(self):
        """Gets the account_id of this ServiceOverrideResponseV2.  # noqa: E501


        :return: The account_id of this ServiceOverrideResponseV2.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this ServiceOverrideResponseV2.


        :param account_id: The account_id of this ServiceOverrideResponseV2.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def org_identifier(self):
        """Gets the org_identifier of this ServiceOverrideResponseV2.  # noqa: E501


        :return: The org_identifier of this ServiceOverrideResponseV2.  # noqa: E501
        :rtype: str
        """
        return self._org_identifier

    @org_identifier.setter
    def org_identifier(self, org_identifier):
        """Sets the org_identifier of this ServiceOverrideResponseV2.


        :param org_identifier: The org_identifier of this ServiceOverrideResponseV2.  # noqa: E501
        :type: str
        """

        self._org_identifier = org_identifier

    @property
    def project_identifier(self):
        """Gets the project_identifier of this ServiceOverrideResponseV2.  # noqa: E501


        :return: The project_identifier of this ServiceOverrideResponseV2.  # noqa: E501
        :rtype: str
        """
        return self._project_identifier

    @project_identifier.setter
    def project_identifier(self, project_identifier):
        """Sets the project_identifier of this ServiceOverrideResponseV2.


        :param project_identifier: The project_identifier of this ServiceOverrideResponseV2.  # noqa: E501
        :type: str
        """

        self._project_identifier = project_identifier

    @property
    def environment_ref(self):
        """Gets the environment_ref of this ServiceOverrideResponseV2.  # noqa: E501


        :return: The environment_ref of this ServiceOverrideResponseV2.  # noqa: E501
        :rtype: str
        """
        return self._environment_ref

    @environment_ref.setter
    def environment_ref(self, environment_ref):
        """Sets the environment_ref of this ServiceOverrideResponseV2.


        :param environment_ref: The environment_ref of this ServiceOverrideResponseV2.  # noqa: E501
        :type: str
        """

        self._environment_ref = environment_ref

    @property
    def service_ref(self):
        """Gets the service_ref of this ServiceOverrideResponseV2.  # noqa: E501


        :return: The service_ref of this ServiceOverrideResponseV2.  # noqa: E501
        :rtype: str
        """
        return self._service_ref

    @service_ref.setter
    def service_ref(self, service_ref):
        """Sets the service_ref of this ServiceOverrideResponseV2.


        :param service_ref: The service_ref of this ServiceOverrideResponseV2.  # noqa: E501
        :type: str
        """

        self._service_ref = service_ref

    @property
    def infra_identifier(self):
        """Gets the infra_identifier of this ServiceOverrideResponseV2.  # noqa: E501


        :return: The infra_identifier of this ServiceOverrideResponseV2.  # noqa: E501
        :rtype: str
        """
        return self._infra_identifier

    @infra_identifier.setter
    def infra_identifier(self, infra_identifier):
        """Sets the infra_identifier of this ServiceOverrideResponseV2.


        :param infra_identifier: The infra_identifier of this ServiceOverrideResponseV2.  # noqa: E501
        :type: str
        """

        self._infra_identifier = infra_identifier

    @property
    def cluster_identifier(self):
        """Gets the cluster_identifier of this ServiceOverrideResponseV2.  # noqa: E501


        :return: The cluster_identifier of this ServiceOverrideResponseV2.  # noqa: E501
        :rtype: str
        """
        return self._cluster_identifier

    @cluster_identifier.setter
    def cluster_identifier(self, cluster_identifier):
        """Sets the cluster_identifier of this ServiceOverrideResponseV2.


        :param cluster_identifier: The cluster_identifier of this ServiceOverrideResponseV2.  # noqa: E501
        :type: str
        """

        self._cluster_identifier = cluster_identifier

    @property
    def type(self):
        """Gets the type of this ServiceOverrideResponseV2.  # noqa: E501


        :return: The type of this ServiceOverrideResponseV2.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ServiceOverrideResponseV2.


        :param type: The type of this ServiceOverrideResponseV2.  # noqa: E501
        :type: str
        """
        allowed_values = ["ENV_GLOBAL_OVERRIDE", "ENV_SERVICE_OVERRIDE", "INFRA_GLOBAL_OVERRIDE", "INFRA_SERVICE_OVERRIDE", "CLUSTER_GLOBAL_OVERRIDE", "CLUSTER_SERVICE_OVERRIDE"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def spec(self):
        """Gets the spec of this ServiceOverrideResponseV2.  # noqa: E501


        :return: The spec of this ServiceOverrideResponseV2.  # noqa: E501
        :rtype: ServiceOverrideSpec
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this ServiceOverrideResponseV2.


        :param spec: The spec of this ServiceOverrideResponseV2.  # noqa: E501
        :type: ServiceOverrideSpec
        """

        self._spec = spec

    @property
    def is_newly_created(self):
        """Gets the is_newly_created of this ServiceOverrideResponseV2.  # noqa: E501


        :return: The is_newly_created of this ServiceOverrideResponseV2.  # noqa: E501
        :rtype: bool
        """
        return self._is_newly_created

    @is_newly_created.setter
    def is_newly_created(self, is_newly_created):
        """Sets the is_newly_created of this ServiceOverrideResponseV2.


        :param is_newly_created: The is_newly_created of this ServiceOverrideResponseV2.  # noqa: E501
        :type: bool
        """

        self._is_newly_created = is_newly_created

    @property
    def yaml_internal(self):
        """Gets the yaml_internal of this ServiceOverrideResponseV2.  # noqa: E501


        :return: The yaml_internal of this ServiceOverrideResponseV2.  # noqa: E501
        :rtype: str
        """
        return self._yaml_internal

    @yaml_internal.setter
    def yaml_internal(self, yaml_internal):
        """Sets the yaml_internal of this ServiceOverrideResponseV2.


        :param yaml_internal: The yaml_internal of this ServiceOverrideResponseV2.  # noqa: E501
        :type: str
        """

        self._yaml_internal = yaml_internal

    @property
    def newly_created(self):
        """Gets the newly_created of this ServiceOverrideResponseV2.  # noqa: E501


        :return: The newly_created of this ServiceOverrideResponseV2.  # noqa: E501
        :rtype: bool
        """
        return self._newly_created

    @newly_created.setter
    def newly_created(self, newly_created):
        """Sets the newly_created of this ServiceOverrideResponseV2.


        :param newly_created: The newly_created of this ServiceOverrideResponseV2.  # noqa: E501
        :type: bool
        """

        self._newly_created = newly_created

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
        if issubclass(ServiceOverrideResponseV2, dict):
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
        if not isinstance(other, ServiceOverrideResponseV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
