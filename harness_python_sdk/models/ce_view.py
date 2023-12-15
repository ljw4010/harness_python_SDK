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

class CEView(object):
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
        'uuid': 'str',
        'name': 'str',
        'account_id': 'str',
        'folder_id': 'str',
        'view_version': 'str',
        'view_time_range': 'ViewTimeRange',
        'view_rules': 'list[ViewRule]',
        'data_sources': 'list[str]',
        'view_visualization': 'ViewVisualization',
        'view_preferences': 'ViewPreferences',
        'view_type': 'str',
        'view_state': 'str',
        'total_cost': 'float',
        'created_at': 'int',
        'last_updated_at': 'int',
        'created_by': 'EmbeddedUser',
        'last_updated_by': 'EmbeddedUser'
    }

    attribute_map = {
        'uuid': 'uuid',
        'name': 'name',
        'account_id': 'accountId',
        'folder_id': 'folderId',
        'view_version': 'viewVersion',
        'view_time_range': 'viewTimeRange',
        'view_rules': 'viewRules',
        'data_sources': 'dataSources',
        'view_visualization': 'viewVisualization',
        'view_preferences': 'viewPreferences',
        'view_type': 'viewType',
        'view_state': 'viewState',
        'total_cost': 'totalCost',
        'created_at': 'createdAt',
        'last_updated_at': 'lastUpdatedAt',
        'created_by': 'createdBy',
        'last_updated_by': 'lastUpdatedBy'
    }

    def __init__(self, uuid=None, name=None, account_id=None, folder_id=None, view_version=None, view_time_range=None, view_rules=None, data_sources=None, view_visualization=None, view_preferences=None, view_type=None, view_state=None, total_cost=None, created_at=None, last_updated_at=None, created_by=None, last_updated_by=None):  # noqa: E501
        """CEView - a model defined in Swagger"""  # noqa: E501
        self._uuid = None
        self._name = None
        self._account_id = None
        self._folder_id = None
        self._view_version = None
        self._view_time_range = None
        self._view_rules = None
        self._data_sources = None
        self._view_visualization = None
        self._view_preferences = None
        self._view_type = None
        self._view_state = None
        self._total_cost = None
        self._created_at = None
        self._last_updated_at = None
        self._created_by = None
        self._last_updated_by = None
        self.discriminator = None
        if uuid is not None:
            self.uuid = uuid
        self.name = name
        if account_id is not None:
            self.account_id = account_id
        if folder_id is not None:
            self.folder_id = folder_id
        self.view_version = view_version
        if view_time_range is not None:
            self.view_time_range = view_time_range
        if view_rules is not None:
            self.view_rules = view_rules
        if data_sources is not None:
            self.data_sources = data_sources
        if view_visualization is not None:
            self.view_visualization = view_visualization
        if view_preferences is not None:
            self.view_preferences = view_preferences
        if view_type is not None:
            self.view_type = view_type
        if view_state is not None:
            self.view_state = view_state
        if total_cost is not None:
            self.total_cost = total_cost
        if created_at is not None:
            self.created_at = created_at
        if last_updated_at is not None:
            self.last_updated_at = last_updated_at
        if created_by is not None:
            self.created_by = created_by
        if last_updated_by is not None:
            self.last_updated_by = last_updated_by

    @property
    def uuid(self):
        """Gets the uuid of this CEView.  # noqa: E501


        :return: The uuid of this CEView.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this CEView.


        :param uuid: The uuid of this CEView.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def name(self):
        """Gets the name of this CEView.  # noqa: E501


        :return: The name of this CEView.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CEView.


        :param name: The name of this CEView.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def account_id(self):
        """Gets the account_id of this CEView.  # noqa: E501


        :return: The account_id of this CEView.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this CEView.


        :param account_id: The account_id of this CEView.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def folder_id(self):
        """Gets the folder_id of this CEView.  # noqa: E501


        :return: The folder_id of this CEView.  # noqa: E501
        :rtype: str
        """
        return self._folder_id

    @folder_id.setter
    def folder_id(self, folder_id):
        """Sets the folder_id of this CEView.


        :param folder_id: The folder_id of this CEView.  # noqa: E501
        :type: str
        """

        self._folder_id = folder_id

    @property
    def view_version(self):
        """Gets the view_version of this CEView.  # noqa: E501


        :return: The view_version of this CEView.  # noqa: E501
        :rtype: str
        """
        return self._view_version

    @view_version.setter
    def view_version(self, view_version):
        """Sets the view_version of this CEView.


        :param view_version: The view_version of this CEView.  # noqa: E501
        :type: str
        """
        if view_version is None:
            raise ValueError("Invalid value for `view_version`, must not be `None`")  # noqa: E501

        self._view_version = view_version

    @property
    def view_time_range(self):
        """Gets the view_time_range of this CEView.  # noqa: E501


        :return: The view_time_range of this CEView.  # noqa: E501
        :rtype: ViewTimeRange
        """
        return self._view_time_range

    @view_time_range.setter
    def view_time_range(self, view_time_range):
        """Sets the view_time_range of this CEView.


        :param view_time_range: The view_time_range of this CEView.  # noqa: E501
        :type: ViewTimeRange
        """

        self._view_time_range = view_time_range

    @property
    def view_rules(self):
        """Gets the view_rules of this CEView.  # noqa: E501


        :return: The view_rules of this CEView.  # noqa: E501
        :rtype: list[ViewRule]
        """
        return self._view_rules

    @view_rules.setter
    def view_rules(self, view_rules):
        """Sets the view_rules of this CEView.


        :param view_rules: The view_rules of this CEView.  # noqa: E501
        :type: list[ViewRule]
        """

        self._view_rules = view_rules

    @property
    def data_sources(self):
        """Gets the data_sources of this CEView.  # noqa: E501


        :return: The data_sources of this CEView.  # noqa: E501
        :rtype: list[str]
        """
        return self._data_sources

    @data_sources.setter
    def data_sources(self, data_sources):
        """Sets the data_sources of this CEView.


        :param data_sources: The data_sources of this CEView.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["CLUSTER", "AWS", "GCP", "AZURE", "COMMON", "CUSTOM", "BUSINESS_MAPPING", "LABEL"]  # noqa: E501
        if not set(data_sources).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `data_sources` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(data_sources) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._data_sources = data_sources

    @property
    def view_visualization(self):
        """Gets the view_visualization of this CEView.  # noqa: E501


        :return: The view_visualization of this CEView.  # noqa: E501
        :rtype: ViewVisualization
        """
        return self._view_visualization

    @view_visualization.setter
    def view_visualization(self, view_visualization):
        """Sets the view_visualization of this CEView.


        :param view_visualization: The view_visualization of this CEView.  # noqa: E501
        :type: ViewVisualization
        """

        self._view_visualization = view_visualization

    @property
    def view_preferences(self):
        """Gets the view_preferences of this CEView.  # noqa: E501


        :return: The view_preferences of this CEView.  # noqa: E501
        :rtype: ViewPreferences
        """
        return self._view_preferences

    @view_preferences.setter
    def view_preferences(self, view_preferences):
        """Sets the view_preferences of this CEView.


        :param view_preferences: The view_preferences of this CEView.  # noqa: E501
        :type: ViewPreferences
        """

        self._view_preferences = view_preferences

    @property
    def view_type(self):
        """Gets the view_type of this CEView.  # noqa: E501


        :return: The view_type of this CEView.  # noqa: E501
        :rtype: str
        """
        return self._view_type

    @view_type.setter
    def view_type(self, view_type):
        """Sets the view_type of this CEView.


        :param view_type: The view_type of this CEView.  # noqa: E501
        :type: str
        """
        allowed_values = ["SAMPLE", "CUSTOMER", "DEFAULT"]  # noqa: E501
        if view_type not in allowed_values:
            raise ValueError(
                "Invalid value for `view_type` ({0}), must be one of {1}"  # noqa: E501
                .format(view_type, allowed_values)
            )

        self._view_type = view_type

    @property
    def view_state(self):
        """Gets the view_state of this CEView.  # noqa: E501


        :return: The view_state of this CEView.  # noqa: E501
        :rtype: str
        """
        return self._view_state

    @view_state.setter
    def view_state(self, view_state):
        """Sets the view_state of this CEView.


        :param view_state: The view_state of this CEView.  # noqa: E501
        :type: str
        """
        allowed_values = ["DRAFT", "COMPLETED"]  # noqa: E501
        if view_state not in allowed_values:
            raise ValueError(
                "Invalid value for `view_state` ({0}), must be one of {1}"  # noqa: E501
                .format(view_state, allowed_values)
            )

        self._view_state = view_state

    @property
    def total_cost(self):
        """Gets the total_cost of this CEView.  # noqa: E501


        :return: The total_cost of this CEView.  # noqa: E501
        :rtype: float
        """
        return self._total_cost

    @total_cost.setter
    def total_cost(self, total_cost):
        """Sets the total_cost of this CEView.


        :param total_cost: The total_cost of this CEView.  # noqa: E501
        :type: float
        """

        self._total_cost = total_cost

    @property
    def created_at(self):
        """Gets the created_at of this CEView.  # noqa: E501


        :return: The created_at of this CEView.  # noqa: E501
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this CEView.


        :param created_at: The created_at of this CEView.  # noqa: E501
        :type: int
        """

        self._created_at = created_at

    @property
    def last_updated_at(self):
        """Gets the last_updated_at of this CEView.  # noqa: E501


        :return: The last_updated_at of this CEView.  # noqa: E501
        :rtype: int
        """
        return self._last_updated_at

    @last_updated_at.setter
    def last_updated_at(self, last_updated_at):
        """Sets the last_updated_at of this CEView.


        :param last_updated_at: The last_updated_at of this CEView.  # noqa: E501
        :type: int
        """

        self._last_updated_at = last_updated_at

    @property
    def created_by(self):
        """Gets the created_by of this CEView.  # noqa: E501


        :return: The created_by of this CEView.  # noqa: E501
        :rtype: EmbeddedUser
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this CEView.


        :param created_by: The created_by of this CEView.  # noqa: E501
        :type: EmbeddedUser
        """

        self._created_by = created_by

    @property
    def last_updated_by(self):
        """Gets the last_updated_by of this CEView.  # noqa: E501


        :return: The last_updated_by of this CEView.  # noqa: E501
        :rtype: EmbeddedUser
        """
        return self._last_updated_by

    @last_updated_by.setter
    def last_updated_by(self, last_updated_by):
        """Sets the last_updated_by of this CEView.


        :param last_updated_by: The last_updated_by of this CEView.  # noqa: E501
        :type: EmbeddedUser
        """

        self._last_updated_by = last_updated_by

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
        if issubclass(CEView, dict):
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
        if not isinstance(other, CEView):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
