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

class RecommendationAdhocDTO(object):
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
        'role_info': 'str',
        'role_id': 'str',
        'tenant_info': 'str',
        'cloud_connector_id': 'str',
        'target_info': 'str',
        'type': 'str'
    }

    attribute_map = {
        'role_info': 'roleInfo',
        'role_id': 'roleId',
        'tenant_info': 'tenantInfo',
        'cloud_connector_id': 'cloudConnectorId',
        'target_info': 'targetInfo',
        'type': 'type'
    }

    discriminator_value_class_map = {
          'AzureRecommendationAdhocDTO': 'AzureRecommendationAdhocDTO',
'AwsRecommendationAdhocDTO': 'AwsRecommendationAdhocDTO'    }

    def __init__(self, role_info=None, role_id=None, tenant_info=None, cloud_connector_id=None, target_info=None, type=None):  # noqa: E501
        """RecommendationAdhocDTO - a model defined in Swagger"""  # noqa: E501
        self._role_info = None
        self._role_id = None
        self._tenant_info = None
        self._cloud_connector_id = None
        self._target_info = None
        self._type = None
        self.discriminator = 'type'
        if role_info is not None:
            self.role_info = role_info
        if role_id is not None:
            self.role_id = role_id
        if tenant_info is not None:
            self.tenant_info = tenant_info
        if cloud_connector_id is not None:
            self.cloud_connector_id = cloud_connector_id
        if target_info is not None:
            self.target_info = target_info
        self.type = type

    @property
    def role_info(self):
        """Gets the role_info of this RecommendationAdhocDTO.  # noqa: E501


        :return: The role_info of this RecommendationAdhocDTO.  # noqa: E501
        :rtype: str
        """
        return self._role_info

    @role_info.setter
    def role_info(self, role_info):
        """Sets the role_info of this RecommendationAdhocDTO.


        :param role_info: The role_info of this RecommendationAdhocDTO.  # noqa: E501
        :type: str
        """

        self._role_info = role_info

    @property
    def role_id(self):
        """Gets the role_id of this RecommendationAdhocDTO.  # noqa: E501


        :return: The role_id of this RecommendationAdhocDTO.  # noqa: E501
        :rtype: str
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        """Sets the role_id of this RecommendationAdhocDTO.


        :param role_id: The role_id of this RecommendationAdhocDTO.  # noqa: E501
        :type: str
        """

        self._role_id = role_id

    @property
    def tenant_info(self):
        """Gets the tenant_info of this RecommendationAdhocDTO.  # noqa: E501


        :return: The tenant_info of this RecommendationAdhocDTO.  # noqa: E501
        :rtype: str
        """
        return self._tenant_info

    @tenant_info.setter
    def tenant_info(self, tenant_info):
        """Sets the tenant_info of this RecommendationAdhocDTO.


        :param tenant_info: The tenant_info of this RecommendationAdhocDTO.  # noqa: E501
        :type: str
        """

        self._tenant_info = tenant_info

    @property
    def cloud_connector_id(self):
        """Gets the cloud_connector_id of this RecommendationAdhocDTO.  # noqa: E501


        :return: The cloud_connector_id of this RecommendationAdhocDTO.  # noqa: E501
        :rtype: str
        """
        return self._cloud_connector_id

    @cloud_connector_id.setter
    def cloud_connector_id(self, cloud_connector_id):
        """Sets the cloud_connector_id of this RecommendationAdhocDTO.


        :param cloud_connector_id: The cloud_connector_id of this RecommendationAdhocDTO.  # noqa: E501
        :type: str
        """

        self._cloud_connector_id = cloud_connector_id

    @property
    def target_info(self):
        """Gets the target_info of this RecommendationAdhocDTO.  # noqa: E501


        :return: The target_info of this RecommendationAdhocDTO.  # noqa: E501
        :rtype: str
        """
        return self._target_info

    @target_info.setter
    def target_info(self, target_info):
        """Sets the target_info of this RecommendationAdhocDTO.


        :param target_info: The target_info of this RecommendationAdhocDTO.  # noqa: E501
        :type: str
        """

        self._target_info = target_info

    @property
    def type(self):
        """Gets the type of this RecommendationAdhocDTO.  # noqa: E501


        :return: The type of this RecommendationAdhocDTO.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RecommendationAdhocDTO.


        :param type: The type of this RecommendationAdhocDTO.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data[self.discriminator].lower()
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if issubclass(RecommendationAdhocDTO, dict):
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
        if not isinstance(other, RecommendationAdhocDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
