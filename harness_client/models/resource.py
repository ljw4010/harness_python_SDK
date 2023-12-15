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

class Resource(object):
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
        'id': 'str',
        'name': 'str',
        'region': 'str',
        'availability_zone': 'str',
        'status': 'str',
        'type': 'str',
        'launch_time': 'str',
        'ipv4': 'list[str]',
        'private_ipv4': 'list[str]',
        'tags': 'object',
        'resource_type': 'str',
        'provider_name': 'str',
        'is_spot': 'bool',
        'platform': 'str',
        'cloud_account_id': 'float',
        'metadata': 'object',
        'provider_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'region': 'region',
        'availability_zone': 'availability_zone',
        'status': 'status',
        'type': 'type',
        'launch_time': 'launch_time',
        'ipv4': 'ipv4',
        'private_ipv4': 'private_ipv4',
        'tags': 'tags',
        'resource_type': 'resource_type',
        'provider_name': 'provider_name',
        'is_spot': 'is_spot',
        'platform': 'platform',
        'cloud_account_id': 'cloud_account_id',
        'metadata': 'metadata',
        'provider_type': 'provider_type'
    }

    def __init__(self, id=None, name=None, region=None, availability_zone=None, status=None, type=None, launch_time=None, ipv4=None, private_ipv4=None, tags=None, resource_type=None, provider_name=None, is_spot=None, platform=None, cloud_account_id=None, metadata=None, provider_type=None):  # noqa: E501
        """Resource - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._region = None
        self._availability_zone = None
        self._status = None
        self._type = None
        self._launch_time = None
        self._ipv4 = None
        self._private_ipv4 = None
        self._tags = None
        self._resource_type = None
        self._provider_name = None
        self._is_spot = None
        self._platform = None
        self._cloud_account_id = None
        self._metadata = None
        self._provider_type = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if region is not None:
            self.region = region
        if availability_zone is not None:
            self.availability_zone = availability_zone
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type
        if launch_time is not None:
            self.launch_time = launch_time
        if ipv4 is not None:
            self.ipv4 = ipv4
        if private_ipv4 is not None:
            self.private_ipv4 = private_ipv4
        if tags is not None:
            self.tags = tags
        if resource_type is not None:
            self.resource_type = resource_type
        if provider_name is not None:
            self.provider_name = provider_name
        if is_spot is not None:
            self.is_spot = is_spot
        if platform is not None:
            self.platform = platform
        if cloud_account_id is not None:
            self.cloud_account_id = cloud_account_id
        if metadata is not None:
            self.metadata = metadata
        if provider_type is not None:
            self.provider_type = provider_type

    @property
    def id(self):
        """Gets the id of this Resource.  # noqa: E501


        :return: The id of this Resource.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Resource.


        :param id: The id of this Resource.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Resource.  # noqa: E501


        :return: The name of this Resource.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Resource.


        :param name: The name of this Resource.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def region(self):
        """Gets the region of this Resource.  # noqa: E501


        :return: The region of this Resource.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this Resource.


        :param region: The region of this Resource.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def availability_zone(self):
        """Gets the availability_zone of this Resource.  # noqa: E501


        :return: The availability_zone of this Resource.  # noqa: E501
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this Resource.


        :param availability_zone: The availability_zone of this Resource.  # noqa: E501
        :type: str
        """

        self._availability_zone = availability_zone

    @property
    def status(self):
        """Gets the status of this Resource.  # noqa: E501


        :return: The status of this Resource.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Resource.


        :param status: The status of this Resource.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def type(self):
        """Gets the type of this Resource.  # noqa: E501


        :return: The type of this Resource.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Resource.


        :param type: The type of this Resource.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def launch_time(self):
        """Gets the launch_time of this Resource.  # noqa: E501


        :return: The launch_time of this Resource.  # noqa: E501
        :rtype: str
        """
        return self._launch_time

    @launch_time.setter
    def launch_time(self, launch_time):
        """Sets the launch_time of this Resource.


        :param launch_time: The launch_time of this Resource.  # noqa: E501
        :type: str
        """

        self._launch_time = launch_time

    @property
    def ipv4(self):
        """Gets the ipv4 of this Resource.  # noqa: E501


        :return: The ipv4 of this Resource.  # noqa: E501
        :rtype: list[str]
        """
        return self._ipv4

    @ipv4.setter
    def ipv4(self, ipv4):
        """Sets the ipv4 of this Resource.


        :param ipv4: The ipv4 of this Resource.  # noqa: E501
        :type: list[str]
        """

        self._ipv4 = ipv4

    @property
    def private_ipv4(self):
        """Gets the private_ipv4 of this Resource.  # noqa: E501


        :return: The private_ipv4 of this Resource.  # noqa: E501
        :rtype: list[str]
        """
        return self._private_ipv4

    @private_ipv4.setter
    def private_ipv4(self, private_ipv4):
        """Sets the private_ipv4 of this Resource.


        :param private_ipv4: The private_ipv4 of this Resource.  # noqa: E501
        :type: list[str]
        """

        self._private_ipv4 = private_ipv4

    @property
    def tags(self):
        """Gets the tags of this Resource.  # noqa: E501

        tag key as attribute key and tag value as attribute value  # noqa: E501

        :return: The tags of this Resource.  # noqa: E501
        :rtype: object
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Resource.

        tag key as attribute key and tag value as attribute value  # noqa: E501

        :param tags: The tags of this Resource.  # noqa: E501
        :type: object
        """

        self._tags = tags

    @property
    def resource_type(self):
        """Gets the resource_type of this Resource.  # noqa: E501


        :return: The resource_type of this Resource.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this Resource.


        :param resource_type: The resource_type of this Resource.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

    @property
    def provider_name(self):
        """Gets the provider_name of this Resource.  # noqa: E501


        :return: The provider_name of this Resource.  # noqa: E501
        :rtype: str
        """
        return self._provider_name

    @provider_name.setter
    def provider_name(self, provider_name):
        """Sets the provider_name of this Resource.


        :param provider_name: The provider_name of this Resource.  # noqa: E501
        :type: str
        """

        self._provider_name = provider_name

    @property
    def is_spot(self):
        """Gets the is_spot of this Resource.  # noqa: E501


        :return: The is_spot of this Resource.  # noqa: E501
        :rtype: bool
        """
        return self._is_spot

    @is_spot.setter
    def is_spot(self, is_spot):
        """Sets the is_spot of this Resource.


        :param is_spot: The is_spot of this Resource.  # noqa: E501
        :type: bool
        """

        self._is_spot = is_spot

    @property
    def platform(self):
        """Gets the platform of this Resource.  # noqa: E501


        :return: The platform of this Resource.  # noqa: E501
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this Resource.


        :param platform: The platform of this Resource.  # noqa: E501
        :type: str
        """

        self._platform = platform

    @property
    def cloud_account_id(self):
        """Gets the cloud_account_id of this Resource.  # noqa: E501


        :return: The cloud_account_id of this Resource.  # noqa: E501
        :rtype: float
        """
        return self._cloud_account_id

    @cloud_account_id.setter
    def cloud_account_id(self, cloud_account_id):
        """Sets the cloud_account_id of this Resource.


        :param cloud_account_id: The cloud_account_id of this Resource.  # noqa: E501
        :type: float
        """

        self._cloud_account_id = cloud_account_id

    @property
    def metadata(self):
        """Gets the metadata of this Resource.  # noqa: E501


        :return: The metadata of this Resource.  # noqa: E501
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Resource.


        :param metadata: The metadata of this Resource.  # noqa: E501
        :type: object
        """

        self._metadata = metadata

    @property
    def provider_type(self):
        """Gets the provider_type of this Resource.  # noqa: E501


        :return: The provider_type of this Resource.  # noqa: E501
        :rtype: str
        """
        return self._provider_type

    @provider_type.setter
    def provider_type(self, provider_type):
        """Sets the provider_type of this Resource.


        :param provider_type: The provider_type of this Resource.  # noqa: E501
        :type: str
        """

        self._provider_type = provider_type

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
        if issubclass(Resource, dict):
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
        if not isinstance(other, Resource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
