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

class ASGMinimal(object):
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
        'desired': 'int',
        'min': 'int',
        'max': 'int',
        'on_demand': 'int',
        'spot': 'int',
        'mixed_instance': 'bool',
        'cloud_account_id': 'str',
        'provider_name': 'str',
        'target_groups': 'list[TargetGroupMinimal]',
        'region': 'str',
        'availability_zones': 'list[str]',
        'status': 'str',
        'meta': 'object'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'desired': 'desired',
        'min': 'min',
        'max': 'max',
        'on_demand': 'on_demand',
        'spot': 'spot',
        'mixed_instance': 'mixed_instance',
        'cloud_account_id': 'cloud_account_id',
        'provider_name': 'provider_name',
        'target_groups': 'target_groups',
        'region': 'region',
        'availability_zones': 'availability_zones',
        'status': 'status',
        'meta': 'meta'
    }

    def __init__(self, id=None, name=None, desired=None, min=None, max=None, on_demand=None, spot=None, mixed_instance=None, cloud_account_id=None, provider_name=None, target_groups=None, region=None, availability_zones=None, status=None, meta=None):  # noqa: E501
        """ASGMinimal - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._desired = None
        self._min = None
        self._max = None
        self._on_demand = None
        self._spot = None
        self._mixed_instance = None
        self._cloud_account_id = None
        self._provider_name = None
        self._target_groups = None
        self._region = None
        self._availability_zones = None
        self._status = None
        self._meta = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if desired is not None:
            self.desired = desired
        if min is not None:
            self.min = min
        if max is not None:
            self.max = max
        if on_demand is not None:
            self.on_demand = on_demand
        if spot is not None:
            self.spot = spot
        if mixed_instance is not None:
            self.mixed_instance = mixed_instance
        if cloud_account_id is not None:
            self.cloud_account_id = cloud_account_id
        if provider_name is not None:
            self.provider_name = provider_name
        if target_groups is not None:
            self.target_groups = target_groups
        if region is not None:
            self.region = region
        if availability_zones is not None:
            self.availability_zones = availability_zones
        if status is not None:
            self.status = status
        if meta is not None:
            self.meta = meta

    @property
    def id(self):
        """Gets the id of this ASGMinimal.  # noqa: E501


        :return: The id of this ASGMinimal.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ASGMinimal.


        :param id: The id of this ASGMinimal.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ASGMinimal.  # noqa: E501


        :return: The name of this ASGMinimal.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ASGMinimal.


        :param name: The name of this ASGMinimal.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def desired(self):
        """Gets the desired of this ASGMinimal.  # noqa: E501


        :return: The desired of this ASGMinimal.  # noqa: E501
        :rtype: int
        """
        return self._desired

    @desired.setter
    def desired(self, desired):
        """Sets the desired of this ASGMinimal.


        :param desired: The desired of this ASGMinimal.  # noqa: E501
        :type: int
        """

        self._desired = desired

    @property
    def min(self):
        """Gets the min of this ASGMinimal.  # noqa: E501


        :return: The min of this ASGMinimal.  # noqa: E501
        :rtype: int
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this ASGMinimal.


        :param min: The min of this ASGMinimal.  # noqa: E501
        :type: int
        """

        self._min = min

    @property
    def max(self):
        """Gets the max of this ASGMinimal.  # noqa: E501


        :return: The max of this ASGMinimal.  # noqa: E501
        :rtype: int
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this ASGMinimal.


        :param max: The max of this ASGMinimal.  # noqa: E501
        :type: int
        """

        self._max = max

    @property
    def on_demand(self):
        """Gets the on_demand of this ASGMinimal.  # noqa: E501


        :return: The on_demand of this ASGMinimal.  # noqa: E501
        :rtype: int
        """
        return self._on_demand

    @on_demand.setter
    def on_demand(self, on_demand):
        """Sets the on_demand of this ASGMinimal.


        :param on_demand: The on_demand of this ASGMinimal.  # noqa: E501
        :type: int
        """

        self._on_demand = on_demand

    @property
    def spot(self):
        """Gets the spot of this ASGMinimal.  # noqa: E501


        :return: The spot of this ASGMinimal.  # noqa: E501
        :rtype: int
        """
        return self._spot

    @spot.setter
    def spot(self, spot):
        """Sets the spot of this ASGMinimal.


        :param spot: The spot of this ASGMinimal.  # noqa: E501
        :type: int
        """

        self._spot = spot

    @property
    def mixed_instance(self):
        """Gets the mixed_instance of this ASGMinimal.  # noqa: E501


        :return: The mixed_instance of this ASGMinimal.  # noqa: E501
        :rtype: bool
        """
        return self._mixed_instance

    @mixed_instance.setter
    def mixed_instance(self, mixed_instance):
        """Sets the mixed_instance of this ASGMinimal.


        :param mixed_instance: The mixed_instance of this ASGMinimal.  # noqa: E501
        :type: bool
        """

        self._mixed_instance = mixed_instance

    @property
    def cloud_account_id(self):
        """Gets the cloud_account_id of this ASGMinimal.  # noqa: E501


        :return: The cloud_account_id of this ASGMinimal.  # noqa: E501
        :rtype: str
        """
        return self._cloud_account_id

    @cloud_account_id.setter
    def cloud_account_id(self, cloud_account_id):
        """Sets the cloud_account_id of this ASGMinimal.


        :param cloud_account_id: The cloud_account_id of this ASGMinimal.  # noqa: E501
        :type: str
        """

        self._cloud_account_id = cloud_account_id

    @property
    def provider_name(self):
        """Gets the provider_name of this ASGMinimal.  # noqa: E501


        :return: The provider_name of this ASGMinimal.  # noqa: E501
        :rtype: str
        """
        return self._provider_name

    @provider_name.setter
    def provider_name(self, provider_name):
        """Sets the provider_name of this ASGMinimal.


        :param provider_name: The provider_name of this ASGMinimal.  # noqa: E501
        :type: str
        """

        self._provider_name = provider_name

    @property
    def target_groups(self):
        """Gets the target_groups of this ASGMinimal.  # noqa: E501


        :return: The target_groups of this ASGMinimal.  # noqa: E501
        :rtype: list[TargetGroupMinimal]
        """
        return self._target_groups

    @target_groups.setter
    def target_groups(self, target_groups):
        """Sets the target_groups of this ASGMinimal.


        :param target_groups: The target_groups of this ASGMinimal.  # noqa: E501
        :type: list[TargetGroupMinimal]
        """

        self._target_groups = target_groups

    @property
    def region(self):
        """Gets the region of this ASGMinimal.  # noqa: E501


        :return: The region of this ASGMinimal.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ASGMinimal.


        :param region: The region of this ASGMinimal.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def availability_zones(self):
        """Gets the availability_zones of this ASGMinimal.  # noqa: E501


        :return: The availability_zones of this ASGMinimal.  # noqa: E501
        :rtype: list[str]
        """
        return self._availability_zones

    @availability_zones.setter
    def availability_zones(self, availability_zones):
        """Sets the availability_zones of this ASGMinimal.


        :param availability_zones: The availability_zones of this ASGMinimal.  # noqa: E501
        :type: list[str]
        """

        self._availability_zones = availability_zones

    @property
    def status(self):
        """Gets the status of this ASGMinimal.  # noqa: E501


        :return: The status of this ASGMinimal.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ASGMinimal.


        :param status: The status of this ASGMinimal.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def meta(self):
        """Gets the meta of this ASGMinimal.  # noqa: E501


        :return: The meta of this ASGMinimal.  # noqa: E501
        :rtype: object
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this ASGMinimal.


        :param meta: The meta of this ASGMinimal.  # noqa: E501
        :type: object
        """

        self._meta = meta

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
        if issubclass(ASGMinimal, dict):
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
        if not isinstance(other, ASGMinimal):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
