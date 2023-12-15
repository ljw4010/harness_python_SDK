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
from swagger_client.models.service_now_auth_credentials import ServiceNowAuthCredentials  # noqa: F401,E501

class ServiceNowADFS(ServiceNowAuthCredentials):
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
        'certificate_ref': 'str',
        'private_key_ref': 'str',
        'client_id_ref': 'str',
        'resource_id_ref': 'str',
        'adfs_url': 'str'
    }
    if hasattr(ServiceNowAuthCredentials, "swagger_types"):
        swagger_types.update(ServiceNowAuthCredentials.swagger_types)

    attribute_map = {
        'certificate_ref': 'certificateRef',
        'private_key_ref': 'privateKeyRef',
        'client_id_ref': 'clientIdRef',
        'resource_id_ref': 'resourceIdRef',
        'adfs_url': 'adfsUrl'
    }
    if hasattr(ServiceNowAuthCredentials, "attribute_map"):
        attribute_map.update(ServiceNowAuthCredentials.attribute_map)

    def __init__(self, certificate_ref=None, private_key_ref=None, client_id_ref=None, resource_id_ref=None, adfs_url=None, *args, **kwargs):  # noqa: E501
        """ServiceNowADFS - a model defined in Swagger"""  # noqa: E501
        self._certificate_ref = None
        self._private_key_ref = None
        self._client_id_ref = None
        self._resource_id_ref = None
        self._adfs_url = None
        self.discriminator = None
        self.certificate_ref = certificate_ref
        self.private_key_ref = private_key_ref
        self.client_id_ref = client_id_ref
        self.resource_id_ref = resource_id_ref
        self.adfs_url = adfs_url
        ServiceNowAuthCredentials.__init__(self, *args, **kwargs)

    @property
    def certificate_ref(self):
        """Gets the certificate_ref of this ServiceNowADFS.  # noqa: E501


        :return: The certificate_ref of this ServiceNowADFS.  # noqa: E501
        :rtype: str
        """
        return self._certificate_ref

    @certificate_ref.setter
    def certificate_ref(self, certificate_ref):
        """Sets the certificate_ref of this ServiceNowADFS.


        :param certificate_ref: The certificate_ref of this ServiceNowADFS.  # noqa: E501
        :type: str
        """
        if certificate_ref is None:
            raise ValueError("Invalid value for `certificate_ref`, must not be `None`")  # noqa: E501

        self._certificate_ref = certificate_ref

    @property
    def private_key_ref(self):
        """Gets the private_key_ref of this ServiceNowADFS.  # noqa: E501


        :return: The private_key_ref of this ServiceNowADFS.  # noqa: E501
        :rtype: str
        """
        return self._private_key_ref

    @private_key_ref.setter
    def private_key_ref(self, private_key_ref):
        """Sets the private_key_ref of this ServiceNowADFS.


        :param private_key_ref: The private_key_ref of this ServiceNowADFS.  # noqa: E501
        :type: str
        """
        if private_key_ref is None:
            raise ValueError("Invalid value for `private_key_ref`, must not be `None`")  # noqa: E501

        self._private_key_ref = private_key_ref

    @property
    def client_id_ref(self):
        """Gets the client_id_ref of this ServiceNowADFS.  # noqa: E501


        :return: The client_id_ref of this ServiceNowADFS.  # noqa: E501
        :rtype: str
        """
        return self._client_id_ref

    @client_id_ref.setter
    def client_id_ref(self, client_id_ref):
        """Sets the client_id_ref of this ServiceNowADFS.


        :param client_id_ref: The client_id_ref of this ServiceNowADFS.  # noqa: E501
        :type: str
        """
        if client_id_ref is None:
            raise ValueError("Invalid value for `client_id_ref`, must not be `None`")  # noqa: E501

        self._client_id_ref = client_id_ref

    @property
    def resource_id_ref(self):
        """Gets the resource_id_ref of this ServiceNowADFS.  # noqa: E501


        :return: The resource_id_ref of this ServiceNowADFS.  # noqa: E501
        :rtype: str
        """
        return self._resource_id_ref

    @resource_id_ref.setter
    def resource_id_ref(self, resource_id_ref):
        """Sets the resource_id_ref of this ServiceNowADFS.


        :param resource_id_ref: The resource_id_ref of this ServiceNowADFS.  # noqa: E501
        :type: str
        """
        if resource_id_ref is None:
            raise ValueError("Invalid value for `resource_id_ref`, must not be `None`")  # noqa: E501

        self._resource_id_ref = resource_id_ref

    @property
    def adfs_url(self):
        """Gets the adfs_url of this ServiceNowADFS.  # noqa: E501


        :return: The adfs_url of this ServiceNowADFS.  # noqa: E501
        :rtype: str
        """
        return self._adfs_url

    @adfs_url.setter
    def adfs_url(self, adfs_url):
        """Sets the adfs_url of this ServiceNowADFS.


        :param adfs_url: The adfs_url of this ServiceNowADFS.  # noqa: E501
        :type: str
        """
        if adfs_url is None:
            raise ValueError("Invalid value for `adfs_url`, must not be `None`")  # noqa: E501

        self._adfs_url = adfs_url

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
        if issubclass(ServiceNowADFS, dict):
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
        if not isinstance(other, ServiceNowADFS):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
