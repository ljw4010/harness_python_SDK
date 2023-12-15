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

class ApplicationsResourceNode(object):
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
        'resource_ref': 'ApplicationsResourceRef',
        'parent_refs': 'list[ApplicationsResourceRef]',
        'info': 'list[ApplicationsInfoItem]',
        'networking_info': 'ApplicationsResourceNetworkingInfo',
        'resource_version': 'str',
        'images': 'list[str]',
        'health': 'ApplicationsHealthStatus',
        'created_at': 'V1Time'
    }

    attribute_map = {
        'resource_ref': 'resourceRef',
        'parent_refs': 'parentRefs',
        'info': 'info',
        'networking_info': 'networkingInfo',
        'resource_version': 'resourceVersion',
        'images': 'images',
        'health': 'health',
        'created_at': 'createdAt'
    }

    def __init__(self, resource_ref=None, parent_refs=None, info=None, networking_info=None, resource_version=None, images=None, health=None, created_at=None):  # noqa: E501
        """ApplicationsResourceNode - a model defined in Swagger"""  # noqa: E501
        self._resource_ref = None
        self._parent_refs = None
        self._info = None
        self._networking_info = None
        self._resource_version = None
        self._images = None
        self._health = None
        self._created_at = None
        self.discriminator = None
        if resource_ref is not None:
            self.resource_ref = resource_ref
        if parent_refs is not None:
            self.parent_refs = parent_refs
        if info is not None:
            self.info = info
        if networking_info is not None:
            self.networking_info = networking_info
        if resource_version is not None:
            self.resource_version = resource_version
        if images is not None:
            self.images = images
        if health is not None:
            self.health = health
        if created_at is not None:
            self.created_at = created_at

    @property
    def resource_ref(self):
        """Gets the resource_ref of this ApplicationsResourceNode.  # noqa: E501


        :return: The resource_ref of this ApplicationsResourceNode.  # noqa: E501
        :rtype: ApplicationsResourceRef
        """
        return self._resource_ref

    @resource_ref.setter
    def resource_ref(self, resource_ref):
        """Sets the resource_ref of this ApplicationsResourceNode.


        :param resource_ref: The resource_ref of this ApplicationsResourceNode.  # noqa: E501
        :type: ApplicationsResourceRef
        """

        self._resource_ref = resource_ref

    @property
    def parent_refs(self):
        """Gets the parent_refs of this ApplicationsResourceNode.  # noqa: E501


        :return: The parent_refs of this ApplicationsResourceNode.  # noqa: E501
        :rtype: list[ApplicationsResourceRef]
        """
        return self._parent_refs

    @parent_refs.setter
    def parent_refs(self, parent_refs):
        """Sets the parent_refs of this ApplicationsResourceNode.


        :param parent_refs: The parent_refs of this ApplicationsResourceNode.  # noqa: E501
        :type: list[ApplicationsResourceRef]
        """

        self._parent_refs = parent_refs

    @property
    def info(self):
        """Gets the info of this ApplicationsResourceNode.  # noqa: E501


        :return: The info of this ApplicationsResourceNode.  # noqa: E501
        :rtype: list[ApplicationsInfoItem]
        """
        return self._info

    @info.setter
    def info(self, info):
        """Sets the info of this ApplicationsResourceNode.


        :param info: The info of this ApplicationsResourceNode.  # noqa: E501
        :type: list[ApplicationsInfoItem]
        """

        self._info = info

    @property
    def networking_info(self):
        """Gets the networking_info of this ApplicationsResourceNode.  # noqa: E501


        :return: The networking_info of this ApplicationsResourceNode.  # noqa: E501
        :rtype: ApplicationsResourceNetworkingInfo
        """
        return self._networking_info

    @networking_info.setter
    def networking_info(self, networking_info):
        """Sets the networking_info of this ApplicationsResourceNode.


        :param networking_info: The networking_info of this ApplicationsResourceNode.  # noqa: E501
        :type: ApplicationsResourceNetworkingInfo
        """

        self._networking_info = networking_info

    @property
    def resource_version(self):
        """Gets the resource_version of this ApplicationsResourceNode.  # noqa: E501


        :return: The resource_version of this ApplicationsResourceNode.  # noqa: E501
        :rtype: str
        """
        return self._resource_version

    @resource_version.setter
    def resource_version(self, resource_version):
        """Sets the resource_version of this ApplicationsResourceNode.


        :param resource_version: The resource_version of this ApplicationsResourceNode.  # noqa: E501
        :type: str
        """

        self._resource_version = resource_version

    @property
    def images(self):
        """Gets the images of this ApplicationsResourceNode.  # noqa: E501


        :return: The images of this ApplicationsResourceNode.  # noqa: E501
        :rtype: list[str]
        """
        return self._images

    @images.setter
    def images(self, images):
        """Sets the images of this ApplicationsResourceNode.


        :param images: The images of this ApplicationsResourceNode.  # noqa: E501
        :type: list[str]
        """

        self._images = images

    @property
    def health(self):
        """Gets the health of this ApplicationsResourceNode.  # noqa: E501


        :return: The health of this ApplicationsResourceNode.  # noqa: E501
        :rtype: ApplicationsHealthStatus
        """
        return self._health

    @health.setter
    def health(self, health):
        """Sets the health of this ApplicationsResourceNode.


        :param health: The health of this ApplicationsResourceNode.  # noqa: E501
        :type: ApplicationsHealthStatus
        """

        self._health = health

    @property
    def created_at(self):
        """Gets the created_at of this ApplicationsResourceNode.  # noqa: E501


        :return: The created_at of this ApplicationsResourceNode.  # noqa: E501
        :rtype: V1Time
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ApplicationsResourceNode.


        :param created_at: The created_at of this ApplicationsResourceNode.  # noqa: E501
        :type: V1Time
        """

        self._created_at = created_at

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
        if issubclass(ApplicationsResourceNode, dict):
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
        if not isinstance(other, ApplicationsResourceNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
