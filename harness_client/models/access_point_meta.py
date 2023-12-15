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

class AccessPointMeta(object):
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
        'error': 'str',
        'certificate_id': 'str',
        'security_groups': 'list[str]',
        'dns': 'AccessPointMetaDns',
        'alb_arn': 'str',
        'resource_group': 'str',
        'fe_ip_id': 'str',
        'subnet_id': 'str',
        'size': 'str',
        'app_gateway_id': 'str',
        'subnet_name': 'str',
        'fe_ip_name': 'str',
        'certificate': 'CertificateData',
        'func_region': 'str'
    }

    attribute_map = {
        'error': 'error',
        'certificate_id': 'certificate_id',
        'security_groups': 'security_groups',
        'dns': 'dns',
        'alb_arn': 'albArn',
        'resource_group': 'resource_group',
        'fe_ip_id': 'fe_ip_id',
        'subnet_id': 'subnet_id',
        'size': 'size',
        'app_gateway_id': 'app_gateway_id',
        'subnet_name': 'subnet_name',
        'fe_ip_name': 'fe_ip_name',
        'certificate': 'certificate',
        'func_region': 'func_region'
    }

    def __init__(self, error=None, certificate_id=None, security_groups=None, dns=None, alb_arn=None, resource_group=None, fe_ip_id=None, subnet_id=None, size=None, app_gateway_id=None, subnet_name=None, fe_ip_name=None, certificate=None, func_region=None):  # noqa: E501
        """AccessPointMeta - a model defined in Swagger"""  # noqa: E501
        self._error = None
        self._certificate_id = None
        self._security_groups = None
        self._dns = None
        self._alb_arn = None
        self._resource_group = None
        self._fe_ip_id = None
        self._subnet_id = None
        self._size = None
        self._app_gateway_id = None
        self._subnet_name = None
        self._fe_ip_name = None
        self._certificate = None
        self._func_region = None
        self.discriminator = None
        if error is not None:
            self.error = error
        if certificate_id is not None:
            self.certificate_id = certificate_id
        if security_groups is not None:
            self.security_groups = security_groups
        if dns is not None:
            self.dns = dns
        if alb_arn is not None:
            self.alb_arn = alb_arn
        if resource_group is not None:
            self.resource_group = resource_group
        if fe_ip_id is not None:
            self.fe_ip_id = fe_ip_id
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if size is not None:
            self.size = size
        if app_gateway_id is not None:
            self.app_gateway_id = app_gateway_id
        if subnet_name is not None:
            self.subnet_name = subnet_name
        if fe_ip_name is not None:
            self.fe_ip_name = fe_ip_name
        if certificate is not None:
            self.certificate = certificate
        if func_region is not None:
            self.func_region = func_region

    @property
    def error(self):
        """Gets the error of this AccessPointMeta.  # noqa: E501


        :return: The error of this AccessPointMeta.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this AccessPointMeta.


        :param error: The error of this AccessPointMeta.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def certificate_id(self):
        """Gets the certificate_id of this AccessPointMeta.  # noqa: E501


        :return: The certificate_id of this AccessPointMeta.  # noqa: E501
        :rtype: str
        """
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, certificate_id):
        """Sets the certificate_id of this AccessPointMeta.


        :param certificate_id: The certificate_id of this AccessPointMeta.  # noqa: E501
        :type: str
        """

        self._certificate_id = certificate_id

    @property
    def security_groups(self):
        """Gets the security_groups of this AccessPointMeta.  # noqa: E501


        :return: The security_groups of this AccessPointMeta.  # noqa: E501
        :rtype: list[str]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        """Sets the security_groups of this AccessPointMeta.


        :param security_groups: The security_groups of this AccessPointMeta.  # noqa: E501
        :type: list[str]
        """

        self._security_groups = security_groups

    @property
    def dns(self):
        """Gets the dns of this AccessPointMeta.  # noqa: E501


        :return: The dns of this AccessPointMeta.  # noqa: E501
        :rtype: AccessPointMetaDns
        """
        return self._dns

    @dns.setter
    def dns(self, dns):
        """Sets the dns of this AccessPointMeta.


        :param dns: The dns of this AccessPointMeta.  # noqa: E501
        :type: AccessPointMetaDns
        """

        self._dns = dns

    @property
    def alb_arn(self):
        """Gets the alb_arn of this AccessPointMeta.  # noqa: E501


        :return: The alb_arn of this AccessPointMeta.  # noqa: E501
        :rtype: str
        """
        return self._alb_arn

    @alb_arn.setter
    def alb_arn(self, alb_arn):
        """Sets the alb_arn of this AccessPointMeta.


        :param alb_arn: The alb_arn of this AccessPointMeta.  # noqa: E501
        :type: str
        """

        self._alb_arn = alb_arn

    @property
    def resource_group(self):
        """Gets the resource_group of this AccessPointMeta.  # noqa: E501


        :return: The resource_group of this AccessPointMeta.  # noqa: E501
        :rtype: str
        """
        return self._resource_group

    @resource_group.setter
    def resource_group(self, resource_group):
        """Sets the resource_group of this AccessPointMeta.


        :param resource_group: The resource_group of this AccessPointMeta.  # noqa: E501
        :type: str
        """

        self._resource_group = resource_group

    @property
    def fe_ip_id(self):
        """Gets the fe_ip_id of this AccessPointMeta.  # noqa: E501


        :return: The fe_ip_id of this AccessPointMeta.  # noqa: E501
        :rtype: str
        """
        return self._fe_ip_id

    @fe_ip_id.setter
    def fe_ip_id(self, fe_ip_id):
        """Sets the fe_ip_id of this AccessPointMeta.


        :param fe_ip_id: The fe_ip_id of this AccessPointMeta.  # noqa: E501
        :type: str
        """

        self._fe_ip_id = fe_ip_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this AccessPointMeta.  # noqa: E501


        :return: The subnet_id of this AccessPointMeta.  # noqa: E501
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this AccessPointMeta.


        :param subnet_id: The subnet_id of this AccessPointMeta.  # noqa: E501
        :type: str
        """

        self._subnet_id = subnet_id

    @property
    def size(self):
        """Gets the size of this AccessPointMeta.  # noqa: E501


        :return: The size of this AccessPointMeta.  # noqa: E501
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this AccessPointMeta.


        :param size: The size of this AccessPointMeta.  # noqa: E501
        :type: str
        """

        self._size = size

    @property
    def app_gateway_id(self):
        """Gets the app_gateway_id of this AccessPointMeta.  # noqa: E501


        :return: The app_gateway_id of this AccessPointMeta.  # noqa: E501
        :rtype: str
        """
        return self._app_gateway_id

    @app_gateway_id.setter
    def app_gateway_id(self, app_gateway_id):
        """Sets the app_gateway_id of this AccessPointMeta.


        :param app_gateway_id: The app_gateway_id of this AccessPointMeta.  # noqa: E501
        :type: str
        """

        self._app_gateway_id = app_gateway_id

    @property
    def subnet_name(self):
        """Gets the subnet_name of this AccessPointMeta.  # noqa: E501


        :return: The subnet_name of this AccessPointMeta.  # noqa: E501
        :rtype: str
        """
        return self._subnet_name

    @subnet_name.setter
    def subnet_name(self, subnet_name):
        """Sets the subnet_name of this AccessPointMeta.


        :param subnet_name: The subnet_name of this AccessPointMeta.  # noqa: E501
        :type: str
        """

        self._subnet_name = subnet_name

    @property
    def fe_ip_name(self):
        """Gets the fe_ip_name of this AccessPointMeta.  # noqa: E501


        :return: The fe_ip_name of this AccessPointMeta.  # noqa: E501
        :rtype: str
        """
        return self._fe_ip_name

    @fe_ip_name.setter
    def fe_ip_name(self, fe_ip_name):
        """Sets the fe_ip_name of this AccessPointMeta.


        :param fe_ip_name: The fe_ip_name of this AccessPointMeta.  # noqa: E501
        :type: str
        """

        self._fe_ip_name = fe_ip_name

    @property
    def certificate(self):
        """Gets the certificate of this AccessPointMeta.  # noqa: E501


        :return: The certificate of this AccessPointMeta.  # noqa: E501
        :rtype: CertificateData
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """Sets the certificate of this AccessPointMeta.


        :param certificate: The certificate of this AccessPointMeta.  # noqa: E501
        :type: CertificateData
        """

        self._certificate = certificate

    @property
    def func_region(self):
        """Gets the func_region of this AccessPointMeta.  # noqa: E501


        :return: The func_region of this AccessPointMeta.  # noqa: E501
        :rtype: str
        """
        return self._func_region

    @func_region.setter
    def func_region(self, func_region):
        """Sets the func_region of this AccessPointMeta.


        :param func_region: The func_region of this AccessPointMeta.  # noqa: E501
        :type: str
        """

        self._func_region = func_region

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
        if issubclass(AccessPointMeta, dict):
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
        if not isinstance(other, AccessPointMeta):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
