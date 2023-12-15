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
from swagger_client.models.connector_config import ConnectorConfig  # noqa: F401,E501

class AppDynamicsConnectorDTO(ConnectorConfig):
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
        'username': 'str',
        'accountname': 'str',
        'controller_url': 'str',
        'delegate_selectors': 'list[str]',
        'password_ref': 'str',
        'client_secret_ref': 'str',
        'client_id': 'str',
        'auth_type': 'str'
    }
    if hasattr(ConnectorConfig, "swagger_types"):
        swagger_types.update(ConnectorConfig.swagger_types)

    attribute_map = {
        'username': 'username',
        'accountname': 'accountname',
        'controller_url': 'controllerUrl',
        'delegate_selectors': 'delegateSelectors',
        'password_ref': 'passwordRef',
        'client_secret_ref': 'clientSecretRef',
        'client_id': 'clientId',
        'auth_type': 'authType'
    }
    if hasattr(ConnectorConfig, "attribute_map"):
        attribute_map.update(ConnectorConfig.attribute_map)

    def __init__(self, username=None, accountname=None, controller_url=None, delegate_selectors=None, password_ref=None, client_secret_ref=None, client_id=None, auth_type=None, *args, **kwargs):  # noqa: E501
        """AppDynamicsConnectorDTO - a model defined in Swagger"""  # noqa: E501
        self._username = None
        self._accountname = None
        self._controller_url = None
        self._delegate_selectors = None
        self._password_ref = None
        self._client_secret_ref = None
        self._client_id = None
        self._auth_type = None
        self.discriminator = None
        if username is not None:
            self.username = username
        self.accountname = accountname
        self.controller_url = controller_url
        if delegate_selectors is not None:
            self.delegate_selectors = delegate_selectors
        if password_ref is not None:
            self.password_ref = password_ref
        if client_secret_ref is not None:
            self.client_secret_ref = client_secret_ref
        if client_id is not None:
            self.client_id = client_id
        if auth_type is not None:
            self.auth_type = auth_type
        ConnectorConfig.__init__(self, *args, **kwargs)

    @property
    def username(self):
        """Gets the username of this AppDynamicsConnectorDTO.  # noqa: E501


        :return: The username of this AppDynamicsConnectorDTO.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this AppDynamicsConnectorDTO.


        :param username: The username of this AppDynamicsConnectorDTO.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def accountname(self):
        """Gets the accountname of this AppDynamicsConnectorDTO.  # noqa: E501


        :return: The accountname of this AppDynamicsConnectorDTO.  # noqa: E501
        :rtype: str
        """
        return self._accountname

    @accountname.setter
    def accountname(self, accountname):
        """Sets the accountname of this AppDynamicsConnectorDTO.


        :param accountname: The accountname of this AppDynamicsConnectorDTO.  # noqa: E501
        :type: str
        """
        if accountname is None:
            raise ValueError("Invalid value for `accountname`, must not be `None`")  # noqa: E501

        self._accountname = accountname

    @property
    def controller_url(self):
        """Gets the controller_url of this AppDynamicsConnectorDTO.  # noqa: E501


        :return: The controller_url of this AppDynamicsConnectorDTO.  # noqa: E501
        :rtype: str
        """
        return self._controller_url

    @controller_url.setter
    def controller_url(self, controller_url):
        """Sets the controller_url of this AppDynamicsConnectorDTO.


        :param controller_url: The controller_url of this AppDynamicsConnectorDTO.  # noqa: E501
        :type: str
        """
        if controller_url is None:
            raise ValueError("Invalid value for `controller_url`, must not be `None`")  # noqa: E501

        self._controller_url = controller_url

    @property
    def delegate_selectors(self):
        """Gets the delegate_selectors of this AppDynamicsConnectorDTO.  # noqa: E501


        :return: The delegate_selectors of this AppDynamicsConnectorDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._delegate_selectors

    @delegate_selectors.setter
    def delegate_selectors(self, delegate_selectors):
        """Sets the delegate_selectors of this AppDynamicsConnectorDTO.


        :param delegate_selectors: The delegate_selectors of this AppDynamicsConnectorDTO.  # noqa: E501
        :type: list[str]
        """

        self._delegate_selectors = delegate_selectors

    @property
    def password_ref(self):
        """Gets the password_ref of this AppDynamicsConnectorDTO.  # noqa: E501


        :return: The password_ref of this AppDynamicsConnectorDTO.  # noqa: E501
        :rtype: str
        """
        return self._password_ref

    @password_ref.setter
    def password_ref(self, password_ref):
        """Sets the password_ref of this AppDynamicsConnectorDTO.


        :param password_ref: The password_ref of this AppDynamicsConnectorDTO.  # noqa: E501
        :type: str
        """

        self._password_ref = password_ref

    @property
    def client_secret_ref(self):
        """Gets the client_secret_ref of this AppDynamicsConnectorDTO.  # noqa: E501


        :return: The client_secret_ref of this AppDynamicsConnectorDTO.  # noqa: E501
        :rtype: str
        """
        return self._client_secret_ref

    @client_secret_ref.setter
    def client_secret_ref(self, client_secret_ref):
        """Sets the client_secret_ref of this AppDynamicsConnectorDTO.


        :param client_secret_ref: The client_secret_ref of this AppDynamicsConnectorDTO.  # noqa: E501
        :type: str
        """

        self._client_secret_ref = client_secret_ref

    @property
    def client_id(self):
        """Gets the client_id of this AppDynamicsConnectorDTO.  # noqa: E501


        :return: The client_id of this AppDynamicsConnectorDTO.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this AppDynamicsConnectorDTO.


        :param client_id: The client_id of this AppDynamicsConnectorDTO.  # noqa: E501
        :type: str
        """

        self._client_id = client_id

    @property
    def auth_type(self):
        """Gets the auth_type of this AppDynamicsConnectorDTO.  # noqa: E501


        :return: The auth_type of this AppDynamicsConnectorDTO.  # noqa: E501
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        """Sets the auth_type of this AppDynamicsConnectorDTO.


        :param auth_type: The auth_type of this AppDynamicsConnectorDTO.  # noqa: E501
        :type: str
        """
        allowed_values = ["UsernamePassword", "ApiClientToken"]  # noqa: E501
        if auth_type not in allowed_values:
            raise ValueError(
                "Invalid value for `auth_type` ({0}), must be one of {1}"  # noqa: E501
                .format(auth_type, allowed_values)
            )

        self._auth_type = auth_type

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
        if issubclass(AppDynamicsConnectorDTO, dict):
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
        if not isinstance(other, AppDynamicsConnectorDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
