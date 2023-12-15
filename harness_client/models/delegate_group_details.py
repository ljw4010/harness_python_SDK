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

class DelegateGroupDetails(object):
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
        'group_id': 'str',
        'delegate_group_identifier': 'str',
        'delegate_type': 'str',
        'group_name': 'str',
        'delegate_description': 'str',
        'delegate_configuration_id': 'str',
        'group_implicit_selectors': 'dict(str, str)',
        'group_custom_selectors': 'list[str]',
        'last_heart_beat': 'int',
        'connectivity_status': 'str',
        'actively_connected': 'bool',
        'grpc_active': 'bool',
        'delegate_instance_details': 'list[DelegateInner]',
        'token_active': 'bool',
        'auto_upgrade': 'str',
        'delegate_group_expiration_time': 'int',
        'delegate_version': 'str',
        'upgrader_last_updated': 'int',
        'immutable': 'bool',
        'group_version': 'str'
    }

    attribute_map = {
        'group_id': 'groupId',
        'delegate_group_identifier': 'delegateGroupIdentifier',
        'delegate_type': 'delegateType',
        'group_name': 'groupName',
        'delegate_description': 'delegateDescription',
        'delegate_configuration_id': 'delegateConfigurationId',
        'group_implicit_selectors': 'groupImplicitSelectors',
        'group_custom_selectors': 'groupCustomSelectors',
        'last_heart_beat': 'lastHeartBeat',
        'connectivity_status': 'connectivityStatus',
        'actively_connected': 'activelyConnected',
        'grpc_active': 'grpcActive',
        'delegate_instance_details': 'delegateInstanceDetails',
        'token_active': 'tokenActive',
        'auto_upgrade': 'autoUpgrade',
        'delegate_group_expiration_time': 'delegateGroupExpirationTime',
        'delegate_version': 'delegateVersion',
        'upgrader_last_updated': 'upgraderLastUpdated',
        'immutable': 'immutable',
        'group_version': 'groupVersion'
    }

    def __init__(self, group_id=None, delegate_group_identifier=None, delegate_type=None, group_name=None, delegate_description=None, delegate_configuration_id=None, group_implicit_selectors=None, group_custom_selectors=None, last_heart_beat=None, connectivity_status=None, actively_connected=None, grpc_active=None, delegate_instance_details=None, token_active=None, auto_upgrade=None, delegate_group_expiration_time=None, delegate_version=None, upgrader_last_updated=None, immutable=None, group_version=None):  # noqa: E501
        """DelegateGroupDetails - a model defined in Swagger"""  # noqa: E501
        self._group_id = None
        self._delegate_group_identifier = None
        self._delegate_type = None
        self._group_name = None
        self._delegate_description = None
        self._delegate_configuration_id = None
        self._group_implicit_selectors = None
        self._group_custom_selectors = None
        self._last_heart_beat = None
        self._connectivity_status = None
        self._actively_connected = None
        self._grpc_active = None
        self._delegate_instance_details = None
        self._token_active = None
        self._auto_upgrade = None
        self._delegate_group_expiration_time = None
        self._delegate_version = None
        self._upgrader_last_updated = None
        self._immutable = None
        self._group_version = None
        self.discriminator = None
        if group_id is not None:
            self.group_id = group_id
        if delegate_group_identifier is not None:
            self.delegate_group_identifier = delegate_group_identifier
        if delegate_type is not None:
            self.delegate_type = delegate_type
        if group_name is not None:
            self.group_name = group_name
        if delegate_description is not None:
            self.delegate_description = delegate_description
        if delegate_configuration_id is not None:
            self.delegate_configuration_id = delegate_configuration_id
        if group_implicit_selectors is not None:
            self.group_implicit_selectors = group_implicit_selectors
        if group_custom_selectors is not None:
            self.group_custom_selectors = group_custom_selectors
        if last_heart_beat is not None:
            self.last_heart_beat = last_heart_beat
        if connectivity_status is not None:
            self.connectivity_status = connectivity_status
        if actively_connected is not None:
            self.actively_connected = actively_connected
        if grpc_active is not None:
            self.grpc_active = grpc_active
        if delegate_instance_details is not None:
            self.delegate_instance_details = delegate_instance_details
        if token_active is not None:
            self.token_active = token_active
        if auto_upgrade is not None:
            self.auto_upgrade = auto_upgrade
        if delegate_group_expiration_time is not None:
            self.delegate_group_expiration_time = delegate_group_expiration_time
        if delegate_version is not None:
            self.delegate_version = delegate_version
        if upgrader_last_updated is not None:
            self.upgrader_last_updated = upgrader_last_updated
        if immutable is not None:
            self.immutable = immutable
        if group_version is not None:
            self.group_version = group_version

    @property
    def group_id(self):
        """Gets the group_id of this DelegateGroupDetails.  # noqa: E501


        :return: The group_id of this DelegateGroupDetails.  # noqa: E501
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this DelegateGroupDetails.


        :param group_id: The group_id of this DelegateGroupDetails.  # noqa: E501
        :type: str
        """

        self._group_id = group_id

    @property
    def delegate_group_identifier(self):
        """Gets the delegate_group_identifier of this DelegateGroupDetails.  # noqa: E501


        :return: The delegate_group_identifier of this DelegateGroupDetails.  # noqa: E501
        :rtype: str
        """
        return self._delegate_group_identifier

    @delegate_group_identifier.setter
    def delegate_group_identifier(self, delegate_group_identifier):
        """Sets the delegate_group_identifier of this DelegateGroupDetails.


        :param delegate_group_identifier: The delegate_group_identifier of this DelegateGroupDetails.  # noqa: E501
        :type: str
        """

        self._delegate_group_identifier = delegate_group_identifier

    @property
    def delegate_type(self):
        """Gets the delegate_type of this DelegateGroupDetails.  # noqa: E501


        :return: The delegate_type of this DelegateGroupDetails.  # noqa: E501
        :rtype: str
        """
        return self._delegate_type

    @delegate_type.setter
    def delegate_type(self, delegate_type):
        """Sets the delegate_type of this DelegateGroupDetails.


        :param delegate_type: The delegate_type of this DelegateGroupDetails.  # noqa: E501
        :type: str
        """

        self._delegate_type = delegate_type

    @property
    def group_name(self):
        """Gets the group_name of this DelegateGroupDetails.  # noqa: E501


        :return: The group_name of this DelegateGroupDetails.  # noqa: E501
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this DelegateGroupDetails.


        :param group_name: The group_name of this DelegateGroupDetails.  # noqa: E501
        :type: str
        """

        self._group_name = group_name

    @property
    def delegate_description(self):
        """Gets the delegate_description of this DelegateGroupDetails.  # noqa: E501


        :return: The delegate_description of this DelegateGroupDetails.  # noqa: E501
        :rtype: str
        """
        return self._delegate_description

    @delegate_description.setter
    def delegate_description(self, delegate_description):
        """Sets the delegate_description of this DelegateGroupDetails.


        :param delegate_description: The delegate_description of this DelegateGroupDetails.  # noqa: E501
        :type: str
        """

        self._delegate_description = delegate_description

    @property
    def delegate_configuration_id(self):
        """Gets the delegate_configuration_id of this DelegateGroupDetails.  # noqa: E501


        :return: The delegate_configuration_id of this DelegateGroupDetails.  # noqa: E501
        :rtype: str
        """
        return self._delegate_configuration_id

    @delegate_configuration_id.setter
    def delegate_configuration_id(self, delegate_configuration_id):
        """Sets the delegate_configuration_id of this DelegateGroupDetails.


        :param delegate_configuration_id: The delegate_configuration_id of this DelegateGroupDetails.  # noqa: E501
        :type: str
        """

        self._delegate_configuration_id = delegate_configuration_id

    @property
    def group_implicit_selectors(self):
        """Gets the group_implicit_selectors of this DelegateGroupDetails.  # noqa: E501


        :return: The group_implicit_selectors of this DelegateGroupDetails.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._group_implicit_selectors

    @group_implicit_selectors.setter
    def group_implicit_selectors(self, group_implicit_selectors):
        """Sets the group_implicit_selectors of this DelegateGroupDetails.


        :param group_implicit_selectors: The group_implicit_selectors of this DelegateGroupDetails.  # noqa: E501
        :type: dict(str, str)
        """
        allowed_values = ["PROFILE_NAME", "DELEGATE_NAME", "HOST_NAME", "GROUP_NAME", "GROUP_SELECTORS", "PROFILE_SELECTORS"]  # noqa: E501
        if not set(group_implicit_selectors.keys()).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid keys in `group_implicit_selectors` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(group_implicit_selectors.keys()) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._group_implicit_selectors = group_implicit_selectors

    @property
    def group_custom_selectors(self):
        """Gets the group_custom_selectors of this DelegateGroupDetails.  # noqa: E501


        :return: The group_custom_selectors of this DelegateGroupDetails.  # noqa: E501
        :rtype: list[str]
        """
        return self._group_custom_selectors

    @group_custom_selectors.setter
    def group_custom_selectors(self, group_custom_selectors):
        """Sets the group_custom_selectors of this DelegateGroupDetails.


        :param group_custom_selectors: The group_custom_selectors of this DelegateGroupDetails.  # noqa: E501
        :type: list[str]
        """

        self._group_custom_selectors = group_custom_selectors

    @property
    def last_heart_beat(self):
        """Gets the last_heart_beat of this DelegateGroupDetails.  # noqa: E501


        :return: The last_heart_beat of this DelegateGroupDetails.  # noqa: E501
        :rtype: int
        """
        return self._last_heart_beat

    @last_heart_beat.setter
    def last_heart_beat(self, last_heart_beat):
        """Sets the last_heart_beat of this DelegateGroupDetails.


        :param last_heart_beat: The last_heart_beat of this DelegateGroupDetails.  # noqa: E501
        :type: int
        """

        self._last_heart_beat = last_heart_beat

    @property
    def connectivity_status(self):
        """Gets the connectivity_status of this DelegateGroupDetails.  # noqa: E501


        :return: The connectivity_status of this DelegateGroupDetails.  # noqa: E501
        :rtype: str
        """
        return self._connectivity_status

    @connectivity_status.setter
    def connectivity_status(self, connectivity_status):
        """Sets the connectivity_status of this DelegateGroupDetails.


        :param connectivity_status: The connectivity_status of this DelegateGroupDetails.  # noqa: E501
        :type: str
        """

        self._connectivity_status = connectivity_status

    @property
    def actively_connected(self):
        """Gets the actively_connected of this DelegateGroupDetails.  # noqa: E501


        :return: The actively_connected of this DelegateGroupDetails.  # noqa: E501
        :rtype: bool
        """
        return self._actively_connected

    @actively_connected.setter
    def actively_connected(self, actively_connected):
        """Sets the actively_connected of this DelegateGroupDetails.


        :param actively_connected: The actively_connected of this DelegateGroupDetails.  # noqa: E501
        :type: bool
        """

        self._actively_connected = actively_connected

    @property
    def grpc_active(self):
        """Gets the grpc_active of this DelegateGroupDetails.  # noqa: E501


        :return: The grpc_active of this DelegateGroupDetails.  # noqa: E501
        :rtype: bool
        """
        return self._grpc_active

    @grpc_active.setter
    def grpc_active(self, grpc_active):
        """Sets the grpc_active of this DelegateGroupDetails.


        :param grpc_active: The grpc_active of this DelegateGroupDetails.  # noqa: E501
        :type: bool
        """

        self._grpc_active = grpc_active

    @property
    def delegate_instance_details(self):
        """Gets the delegate_instance_details of this DelegateGroupDetails.  # noqa: E501


        :return: The delegate_instance_details of this DelegateGroupDetails.  # noqa: E501
        :rtype: list[DelegateInner]
        """
        return self._delegate_instance_details

    @delegate_instance_details.setter
    def delegate_instance_details(self, delegate_instance_details):
        """Sets the delegate_instance_details of this DelegateGroupDetails.


        :param delegate_instance_details: The delegate_instance_details of this DelegateGroupDetails.  # noqa: E501
        :type: list[DelegateInner]
        """

        self._delegate_instance_details = delegate_instance_details

    @property
    def token_active(self):
        """Gets the token_active of this DelegateGroupDetails.  # noqa: E501


        :return: The token_active of this DelegateGroupDetails.  # noqa: E501
        :rtype: bool
        """
        return self._token_active

    @token_active.setter
    def token_active(self, token_active):
        """Sets the token_active of this DelegateGroupDetails.


        :param token_active: The token_active of this DelegateGroupDetails.  # noqa: E501
        :type: bool
        """

        self._token_active = token_active

    @property
    def auto_upgrade(self):
        """Gets the auto_upgrade of this DelegateGroupDetails.  # noqa: E501


        :return: The auto_upgrade of this DelegateGroupDetails.  # noqa: E501
        :rtype: str
        """
        return self._auto_upgrade

    @auto_upgrade.setter
    def auto_upgrade(self, auto_upgrade):
        """Sets the auto_upgrade of this DelegateGroupDetails.


        :param auto_upgrade: The auto_upgrade of this DelegateGroupDetails.  # noqa: E501
        :type: str
        """
        allowed_values = ["ON", "OFF", "DETECTING"]  # noqa: E501
        if auto_upgrade not in allowed_values:
            raise ValueError(
                "Invalid value for `auto_upgrade` ({0}), must be one of {1}"  # noqa: E501
                .format(auto_upgrade, allowed_values)
            )

        self._auto_upgrade = auto_upgrade

    @property
    def delegate_group_expiration_time(self):
        """Gets the delegate_group_expiration_time of this DelegateGroupDetails.  # noqa: E501


        :return: The delegate_group_expiration_time of this DelegateGroupDetails.  # noqa: E501
        :rtype: int
        """
        return self._delegate_group_expiration_time

    @delegate_group_expiration_time.setter
    def delegate_group_expiration_time(self, delegate_group_expiration_time):
        """Sets the delegate_group_expiration_time of this DelegateGroupDetails.


        :param delegate_group_expiration_time: The delegate_group_expiration_time of this DelegateGroupDetails.  # noqa: E501
        :type: int
        """

        self._delegate_group_expiration_time = delegate_group_expiration_time

    @property
    def delegate_version(self):
        """Gets the delegate_version of this DelegateGroupDetails.  # noqa: E501


        :return: The delegate_version of this DelegateGroupDetails.  # noqa: E501
        :rtype: str
        """
        return self._delegate_version

    @delegate_version.setter
    def delegate_version(self, delegate_version):
        """Sets the delegate_version of this DelegateGroupDetails.


        :param delegate_version: The delegate_version of this DelegateGroupDetails.  # noqa: E501
        :type: str
        """

        self._delegate_version = delegate_version

    @property
    def upgrader_last_updated(self):
        """Gets the upgrader_last_updated of this DelegateGroupDetails.  # noqa: E501


        :return: The upgrader_last_updated of this DelegateGroupDetails.  # noqa: E501
        :rtype: int
        """
        return self._upgrader_last_updated

    @upgrader_last_updated.setter
    def upgrader_last_updated(self, upgrader_last_updated):
        """Sets the upgrader_last_updated of this DelegateGroupDetails.


        :param upgrader_last_updated: The upgrader_last_updated of this DelegateGroupDetails.  # noqa: E501
        :type: int
        """

        self._upgrader_last_updated = upgrader_last_updated

    @property
    def immutable(self):
        """Gets the immutable of this DelegateGroupDetails.  # noqa: E501


        :return: The immutable of this DelegateGroupDetails.  # noqa: E501
        :rtype: bool
        """
        return self._immutable

    @immutable.setter
    def immutable(self, immutable):
        """Sets the immutable of this DelegateGroupDetails.


        :param immutable: The immutable of this DelegateGroupDetails.  # noqa: E501
        :type: bool
        """

        self._immutable = immutable

    @property
    def group_version(self):
        """Gets the group_version of this DelegateGroupDetails.  # noqa: E501


        :return: The group_version of this DelegateGroupDetails.  # noqa: E501
        :rtype: str
        """
        return self._group_version

    @group_version.setter
    def group_version(self, group_version):
        """Sets the group_version of this DelegateGroupDetails.


        :param group_version: The group_version of this DelegateGroupDetails.  # noqa: E501
        :type: str
        """

        self._group_version = group_version

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
        if issubclass(DelegateGroupDetails, dict):
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
        if not isinstance(other, DelegateGroupDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
