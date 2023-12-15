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

class SSORequest(object):
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
        'oauth_provider_type': 'str',
        'idp_redirect_url': 'str',
        'oauth_provider_types': 'list[str]',
        'sso_id': 'str',
        'friendly_saml_name': 'str',
        'saml_provider_type': 'str'
    }

    attribute_map = {
        'oauth_provider_type': 'oauthProviderType',
        'idp_redirect_url': 'idpRedirectUrl',
        'oauth_provider_types': 'oauthProviderTypes',
        'sso_id': 'ssoId',
        'friendly_saml_name': 'friendlySamlName',
        'saml_provider_type': 'samlProviderType'
    }

    def __init__(self, oauth_provider_type=None, idp_redirect_url=None, oauth_provider_types=None, sso_id=None, friendly_saml_name=None, saml_provider_type=None):  # noqa: E501
        """SSORequest - a model defined in Swagger"""  # noqa: E501
        self._oauth_provider_type = None
        self._idp_redirect_url = None
        self._oauth_provider_types = None
        self._sso_id = None
        self._friendly_saml_name = None
        self._saml_provider_type = None
        self.discriminator = None
        if oauth_provider_type is not None:
            self.oauth_provider_type = oauth_provider_type
        if idp_redirect_url is not None:
            self.idp_redirect_url = idp_redirect_url
        if oauth_provider_types is not None:
            self.oauth_provider_types = oauth_provider_types
        if sso_id is not None:
            self.sso_id = sso_id
        if friendly_saml_name is not None:
            self.friendly_saml_name = friendly_saml_name
        if saml_provider_type is not None:
            self.saml_provider_type = saml_provider_type

    @property
    def oauth_provider_type(self):
        """Gets the oauth_provider_type of this SSORequest.  # noqa: E501


        :return: The oauth_provider_type of this SSORequest.  # noqa: E501
        :rtype: str
        """
        return self._oauth_provider_type

    @oauth_provider_type.setter
    def oauth_provider_type(self, oauth_provider_type):
        """Sets the oauth_provider_type of this SSORequest.


        :param oauth_provider_type: The oauth_provider_type of this SSORequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["AZURE", "BITBUCKET", "GITHUB", "GITLAB", "GOOGLE", "LINKEDIN"]  # noqa: E501
        if oauth_provider_type not in allowed_values:
            raise ValueError(
                "Invalid value for `oauth_provider_type` ({0}), must be one of {1}"  # noqa: E501
                .format(oauth_provider_type, allowed_values)
            )

        self._oauth_provider_type = oauth_provider_type

    @property
    def idp_redirect_url(self):
        """Gets the idp_redirect_url of this SSORequest.  # noqa: E501


        :return: The idp_redirect_url of this SSORequest.  # noqa: E501
        :rtype: str
        """
        return self._idp_redirect_url

    @idp_redirect_url.setter
    def idp_redirect_url(self, idp_redirect_url):
        """Sets the idp_redirect_url of this SSORequest.


        :param idp_redirect_url: The idp_redirect_url of this SSORequest.  # noqa: E501
        :type: str
        """

        self._idp_redirect_url = idp_redirect_url

    @property
    def oauth_provider_types(self):
        """Gets the oauth_provider_types of this SSORequest.  # noqa: E501


        :return: The oauth_provider_types of this SSORequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._oauth_provider_types

    @oauth_provider_types.setter
    def oauth_provider_types(self, oauth_provider_types):
        """Sets the oauth_provider_types of this SSORequest.


        :param oauth_provider_types: The oauth_provider_types of this SSORequest.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["AZURE", "BITBUCKET", "GITHUB", "GITLAB", "GOOGLE", "LINKEDIN"]  # noqa: E501
        if not set(oauth_provider_types).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `oauth_provider_types` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(oauth_provider_types) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._oauth_provider_types = oauth_provider_types

    @property
    def sso_id(self):
        """Gets the sso_id of this SSORequest.  # noqa: E501


        :return: The sso_id of this SSORequest.  # noqa: E501
        :rtype: str
        """
        return self._sso_id

    @sso_id.setter
    def sso_id(self, sso_id):
        """Sets the sso_id of this SSORequest.


        :param sso_id: The sso_id of this SSORequest.  # noqa: E501
        :type: str
        """

        self._sso_id = sso_id

    @property
    def friendly_saml_name(self):
        """Gets the friendly_saml_name of this SSORequest.  # noqa: E501


        :return: The friendly_saml_name of this SSORequest.  # noqa: E501
        :rtype: str
        """
        return self._friendly_saml_name

    @friendly_saml_name.setter
    def friendly_saml_name(self, friendly_saml_name):
        """Sets the friendly_saml_name of this SSORequest.


        :param friendly_saml_name: The friendly_saml_name of this SSORequest.  # noqa: E501
        :type: str
        """

        self._friendly_saml_name = friendly_saml_name

    @property
    def saml_provider_type(self):
        """Gets the saml_provider_type of this SSORequest.  # noqa: E501


        :return: The saml_provider_type of this SSORequest.  # noqa: E501
        :rtype: str
        """
        return self._saml_provider_type

    @saml_provider_type.setter
    def saml_provider_type(self, saml_provider_type):
        """Sets the saml_provider_type of this SSORequest.


        :param saml_provider_type: The saml_provider_type of this SSORequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["AZURE", "OKTA", "ONELOGIN", "OTHER"]  # noqa: E501
        if saml_provider_type not in allowed_values:
            raise ValueError(
                "Invalid value for `saml_provider_type` ({0}), must be one of {1}"  # noqa: E501
                .format(saml_provider_type, allowed_values)
            )

        self._saml_provider_type = saml_provider_type

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
        if issubclass(SSORequest, dict):
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
        if not isinstance(other, SSORequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
