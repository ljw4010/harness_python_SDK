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

class DelegateSetupDetails(object):
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
        'name': 'str',
        'description': 'str',
        'size': 'str',
        'host_name': 'str',
        'delegate_configuration_id': 'str',
        'identifier': 'str',
        'k8s_config_details': 'K8sConfigDetails',
        'tags': 'list[str]',
        'delegate_type': 'str',
        'token_name': 'str',
        'run_as_root': 'bool',
        'version': 'str'
    }

    attribute_map = {
        'org_identifier': 'orgIdentifier',
        'project_identifier': 'projectIdentifier',
        'name': 'name',
        'description': 'description',
        'size': 'size',
        'host_name': 'hostName',
        'delegate_configuration_id': 'delegateConfigurationId',
        'identifier': 'identifier',
        'k8s_config_details': 'k8sConfigDetails',
        'tags': 'tags',
        'delegate_type': 'delegateType',
        'token_name': 'tokenName',
        'run_as_root': 'runAsRoot',
        'version': 'version'
    }

    def __init__(self, org_identifier=None, project_identifier=None, name=None, description=None, size=None, host_name=None, delegate_configuration_id=None, identifier=None, k8s_config_details=None, tags=None, delegate_type=None, token_name=None, run_as_root=None, version=None):  # noqa: E501
        """DelegateSetupDetails - a model defined in Swagger"""  # noqa: E501
        self._org_identifier = None
        self._project_identifier = None
        self._name = None
        self._description = None
        self._size = None
        self._host_name = None
        self._delegate_configuration_id = None
        self._identifier = None
        self._k8s_config_details = None
        self._tags = None
        self._delegate_type = None
        self._token_name = None
        self._run_as_root = None
        self._version = None
        self.discriminator = None
        if org_identifier is not None:
            self.org_identifier = org_identifier
        if project_identifier is not None:
            self.project_identifier = project_identifier
        self.name = name
        if description is not None:
            self.description = description
        if size is not None:
            self.size = size
        if host_name is not None:
            self.host_name = host_name
        if delegate_configuration_id is not None:
            self.delegate_configuration_id = delegate_configuration_id
        if identifier is not None:
            self.identifier = identifier
        if k8s_config_details is not None:
            self.k8s_config_details = k8s_config_details
        if tags is not None:
            self.tags = tags
        self.delegate_type = delegate_type
        if token_name is not None:
            self.token_name = token_name
        if run_as_root is not None:
            self.run_as_root = run_as_root
        if version is not None:
            self.version = version

    @property
    def org_identifier(self):
        """Gets the org_identifier of this DelegateSetupDetails.  # noqa: E501


        :return: The org_identifier of this DelegateSetupDetails.  # noqa: E501
        :rtype: str
        """
        return self._org_identifier

    @org_identifier.setter
    def org_identifier(self, org_identifier):
        """Sets the org_identifier of this DelegateSetupDetails.


        :param org_identifier: The org_identifier of this DelegateSetupDetails.  # noqa: E501
        :type: str
        """

        self._org_identifier = org_identifier

    @property
    def project_identifier(self):
        """Gets the project_identifier of this DelegateSetupDetails.  # noqa: E501


        :return: The project_identifier of this DelegateSetupDetails.  # noqa: E501
        :rtype: str
        """
        return self._project_identifier

    @project_identifier.setter
    def project_identifier(self, project_identifier):
        """Sets the project_identifier of this DelegateSetupDetails.


        :param project_identifier: The project_identifier of this DelegateSetupDetails.  # noqa: E501
        :type: str
        """

        self._project_identifier = project_identifier

    @property
    def name(self):
        """Gets the name of this DelegateSetupDetails.  # noqa: E501


        :return: The name of this DelegateSetupDetails.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DelegateSetupDetails.


        :param name: The name of this DelegateSetupDetails.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this DelegateSetupDetails.  # noqa: E501


        :return: The description of this DelegateSetupDetails.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DelegateSetupDetails.


        :param description: The description of this DelegateSetupDetails.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def size(self):
        """Gets the size of this DelegateSetupDetails.  # noqa: E501


        :return: The size of this DelegateSetupDetails.  # noqa: E501
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this DelegateSetupDetails.


        :param size: The size of this DelegateSetupDetails.  # noqa: E501
        :type: str
        """
        allowed_values = ["LAPTOP", "SMALL", "MEDIUM", "LARGE"]  # noqa: E501
        if size not in allowed_values:
            raise ValueError(
                "Invalid value for `size` ({0}), must be one of {1}"  # noqa: E501
                .format(size, allowed_values)
            )

        self._size = size

    @property
    def host_name(self):
        """Gets the host_name of this DelegateSetupDetails.  # noqa: E501


        :return: The host_name of this DelegateSetupDetails.  # noqa: E501
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this DelegateSetupDetails.


        :param host_name: The host_name of this DelegateSetupDetails.  # noqa: E501
        :type: str
        """

        self._host_name = host_name

    @property
    def delegate_configuration_id(self):
        """Gets the delegate_configuration_id of this DelegateSetupDetails.  # noqa: E501


        :return: The delegate_configuration_id of this DelegateSetupDetails.  # noqa: E501
        :rtype: str
        """
        return self._delegate_configuration_id

    @delegate_configuration_id.setter
    def delegate_configuration_id(self, delegate_configuration_id):
        """Sets the delegate_configuration_id of this DelegateSetupDetails.


        :param delegate_configuration_id: The delegate_configuration_id of this DelegateSetupDetails.  # noqa: E501
        :type: str
        """

        self._delegate_configuration_id = delegate_configuration_id

    @property
    def identifier(self):
        """Gets the identifier of this DelegateSetupDetails.  # noqa: E501


        :return: The identifier of this DelegateSetupDetails.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this DelegateSetupDetails.


        :param identifier: The identifier of this DelegateSetupDetails.  # noqa: E501
        :type: str
        """

        self._identifier = identifier

    @property
    def k8s_config_details(self):
        """Gets the k8s_config_details of this DelegateSetupDetails.  # noqa: E501


        :return: The k8s_config_details of this DelegateSetupDetails.  # noqa: E501
        :rtype: K8sConfigDetails
        """
        return self._k8s_config_details

    @k8s_config_details.setter
    def k8s_config_details(self, k8s_config_details):
        """Sets the k8s_config_details of this DelegateSetupDetails.


        :param k8s_config_details: The k8s_config_details of this DelegateSetupDetails.  # noqa: E501
        :type: K8sConfigDetails
        """

        self._k8s_config_details = k8s_config_details

    @property
    def tags(self):
        """Gets the tags of this DelegateSetupDetails.  # noqa: E501


        :return: The tags of this DelegateSetupDetails.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this DelegateSetupDetails.


        :param tags: The tags of this DelegateSetupDetails.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def delegate_type(self):
        """Gets the delegate_type of this DelegateSetupDetails.  # noqa: E501

        Currently KUBERNETES and HELM_DELEGATE are supported.  # noqa: E501

        :return: The delegate_type of this DelegateSetupDetails.  # noqa: E501
        :rtype: str
        """
        return self._delegate_type

    @delegate_type.setter
    def delegate_type(self, delegate_type):
        """Sets the delegate_type of this DelegateSetupDetails.

        Currently KUBERNETES and HELM_DELEGATE are supported.  # noqa: E501

        :param delegate_type: The delegate_type of this DelegateSetupDetails.  # noqa: E501
        :type: str
        """
        if delegate_type is None:
            raise ValueError("Invalid value for `delegate_type`, must not be `None`")  # noqa: E501

        self._delegate_type = delegate_type

    @property
    def token_name(self):
        """Gets the token_name of this DelegateSetupDetails.  # noqa: E501


        :return: The token_name of this DelegateSetupDetails.  # noqa: E501
        :rtype: str
        """
        return self._token_name

    @token_name.setter
    def token_name(self, token_name):
        """Sets the token_name of this DelegateSetupDetails.


        :param token_name: The token_name of this DelegateSetupDetails.  # noqa: E501
        :type: str
        """

        self._token_name = token_name

    @property
    def run_as_root(self):
        """Gets the run_as_root of this DelegateSetupDetails.  # noqa: E501


        :return: The run_as_root of this DelegateSetupDetails.  # noqa: E501
        :rtype: bool
        """
        return self._run_as_root

    @run_as_root.setter
    def run_as_root(self, run_as_root):
        """Sets the run_as_root of this DelegateSetupDetails.


        :param run_as_root: The run_as_root of this DelegateSetupDetails.  # noqa: E501
        :type: bool
        """

        self._run_as_root = run_as_root

    @property
    def version(self):
        """Gets the version of this DelegateSetupDetails.  # noqa: E501


        :return: The version of this DelegateSetupDetails.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this DelegateSetupDetails.


        :param version: The version of this DelegateSetupDetails.  # noqa: E501
        :type: str
        """

        self._version = version

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
        if issubclass(DelegateSetupDetails, dict):
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
        if not isinstance(other, DelegateSetupDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
