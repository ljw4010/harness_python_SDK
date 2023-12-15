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
from harness_python_sdk.models.secret_spec import SecretSpec  # noqa: F401,E501

class WinRmTGTPasswordSpec(SecretSpec):
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
        'type': 'str',
        'port': 'int',
        'principal': 'str',
        'realm': 'str',
        'password': 'str',
        'use_ssl': 'bool',
        'skip_cert_checks': 'bool',
        'use_no_profile': 'bool'
    }
    if hasattr(SecretSpec, "swagger_types"):
        swagger_types.update(SecretSpec.swagger_types)

    attribute_map = {
        'type': 'type',
        'port': 'port',
        'principal': 'principal',
        'realm': 'realm',
        'password': 'password',
        'use_ssl': 'use_ssl',
        'skip_cert_checks': 'skip_cert_checks',
        'use_no_profile': 'use_no_profile'
    }
    if hasattr(SecretSpec, "attribute_map"):
        attribute_map.update(SecretSpec.attribute_map)

    def __init__(self, type=None, port=5986, principal=None, realm=None, password=None, use_ssl=True, skip_cert_checks=True, use_no_profile=None, *args, **kwargs):  # noqa: E501
        """WinRmTGTPasswordSpec - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._port = None
        self._principal = None
        self._realm = None
        self._password = None
        self._use_ssl = None
        self._skip_cert_checks = None
        self._use_no_profile = None
        self.discriminator = None
        self.type = type
        if port is not None:
            self.port = port
        if principal is not None:
            self.principal = principal
        if realm is not None:
            self.realm = realm
        if password is not None:
            self.password = password
        if use_ssl is not None:
            self.use_ssl = use_ssl
        if skip_cert_checks is not None:
            self.skip_cert_checks = skip_cert_checks
        if use_no_profile is not None:
            self.use_no_profile = use_no_profile
        SecretSpec.__init__(self, *args, **kwargs)

    @property
    def type(self):
        """Gets the type of this WinRmTGTPasswordSpec.  # noqa: E501

        This specifies the type of secret  # noqa: E501

        :return: The type of this WinRmTGTPasswordSpec.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this WinRmTGTPasswordSpec.

        This specifies the type of secret  # noqa: E501

        :param type: The type of this WinRmTGTPasswordSpec.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["WinRmTGTPassword"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def port(self):
        """Gets the port of this WinRmTGTPasswordSpec.  # noqa: E501

        WinRm port  # noqa: E501

        :return: The port of this WinRmTGTPasswordSpec.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this WinRmTGTPasswordSpec.

        WinRm port  # noqa: E501

        :param port: The port of this WinRmTGTPasswordSpec.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def principal(self):
        """Gets the principal of this WinRmTGTPasswordSpec.  # noqa: E501

        Kerberos principal  # noqa: E501

        :return: The principal of this WinRmTGTPasswordSpec.  # noqa: E501
        :rtype: str
        """
        return self._principal

    @principal.setter
    def principal(self, principal):
        """Sets the principal of this WinRmTGTPasswordSpec.

        Kerberos principal  # noqa: E501

        :param principal: The principal of this WinRmTGTPasswordSpec.  # noqa: E501
        :type: str
        """

        self._principal = principal

    @property
    def realm(self):
        """Gets the realm of this WinRmTGTPasswordSpec.  # noqa: E501

        Kerberos realm  # noqa: E501

        :return: The realm of this WinRmTGTPasswordSpec.  # noqa: E501
        :rtype: str
        """
        return self._realm

    @realm.setter
    def realm(self, realm):
        """Sets the realm of this WinRmTGTPasswordSpec.

        Kerberos realm  # noqa: E501

        :param realm: The realm of this WinRmTGTPasswordSpec.  # noqa: E501
        :type: str
        """

        self._realm = realm

    @property
    def password(self):
        """Gets the password of this WinRmTGTPasswordSpec.  # noqa: E501

        Kerberos password  # noqa: E501

        :return: The password of this WinRmTGTPasswordSpec.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this WinRmTGTPasswordSpec.

        Kerberos password  # noqa: E501

        :param password: The password of this WinRmTGTPasswordSpec.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def use_ssl(self):
        """Gets the use_ssl of this WinRmTGTPasswordSpec.  # noqa: E501

        This is the Kerberos either to use SSL/https  # noqa: E501

        :return: The use_ssl of this WinRmTGTPasswordSpec.  # noqa: E501
        :rtype: bool
        """
        return self._use_ssl

    @use_ssl.setter
    def use_ssl(self, use_ssl):
        """Sets the use_ssl of this WinRmTGTPasswordSpec.

        This is the Kerberos either to use SSL/https  # noqa: E501

        :param use_ssl: The use_ssl of this WinRmTGTPasswordSpec.  # noqa: E501
        :type: bool
        """

        self._use_ssl = use_ssl

    @property
    def skip_cert_checks(self):
        """Gets the skip_cert_checks of this WinRmTGTPasswordSpec.  # noqa: E501

        This is the Kerberos either to skip certificate checks  # noqa: E501

        :return: The skip_cert_checks of this WinRmTGTPasswordSpec.  # noqa: E501
        :rtype: bool
        """
        return self._skip_cert_checks

    @skip_cert_checks.setter
    def skip_cert_checks(self, skip_cert_checks):
        """Sets the skip_cert_checks of this WinRmTGTPasswordSpec.

        This is the Kerberos either to skip certificate checks  # noqa: E501

        :param skip_cert_checks: The skip_cert_checks of this WinRmTGTPasswordSpec.  # noqa: E501
        :type: bool
        """

        self._skip_cert_checks = skip_cert_checks

    @property
    def use_no_profile(self):
        """Gets the use_no_profile of this WinRmTGTPasswordSpec.  # noqa: E501

        This is the Kerberos powershell runs without loading profile  # noqa: E501

        :return: The use_no_profile of this WinRmTGTPasswordSpec.  # noqa: E501
        :rtype: bool
        """
        return self._use_no_profile

    @use_no_profile.setter
    def use_no_profile(self, use_no_profile):
        """Sets the use_no_profile of this WinRmTGTPasswordSpec.

        This is the Kerberos powershell runs without loading profile  # noqa: E501

        :param use_no_profile: The use_no_profile of this WinRmTGTPasswordSpec.  # noqa: E501
        :type: bool
        """

        self._use_no_profile = use_no_profile

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
        if issubclass(WinRmTGTPasswordSpec, dict):
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
        if not isinstance(other, WinRmTGTPasswordSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
