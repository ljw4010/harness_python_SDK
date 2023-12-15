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

class DelegateFilterPropertiesDTO(object):
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
        'status': 'str',
        'description': 'str',
        'host_name': 'str',
        'delegate_name': 'str',
        'delegate_type': 'str',
        'delegate_group_identifier': 'str',
        'delegate_tags': 'list[str]',
        'delegate_instance_filter': 'str',
        'tags': 'dict(str, str)',
        'filter_type': 'str'
    }

    attribute_map = {
        'status': 'status',
        'description': 'description',
        'host_name': 'hostName',
        'delegate_name': 'delegateName',
        'delegate_type': 'delegateType',
        'delegate_group_identifier': 'delegateGroupIdentifier',
        'delegate_tags': 'delegateTags',
        'delegate_instance_filter': 'delegateInstanceFilter',
        'tags': 'tags',
        'filter_type': 'filterType'
    }

    def __init__(self, status=None, description=None, host_name=None, delegate_name=None, delegate_type=None, delegate_group_identifier=None, delegate_tags=None, delegate_instance_filter=None, tags=None, filter_type=None):  # noqa: E501
        """DelegateFilterPropertiesDTO - a model defined in Swagger"""  # noqa: E501
        self._status = None
        self._description = None
        self._host_name = None
        self._delegate_name = None
        self._delegate_type = None
        self._delegate_group_identifier = None
        self._delegate_tags = None
        self._delegate_instance_filter = None
        self._tags = None
        self._filter_type = None
        self.discriminator = None
        if status is not None:
            self.status = status
        if description is not None:
            self.description = description
        if host_name is not None:
            self.host_name = host_name
        if delegate_name is not None:
            self.delegate_name = delegate_name
        if delegate_type is not None:
            self.delegate_type = delegate_type
        if delegate_group_identifier is not None:
            self.delegate_group_identifier = delegate_group_identifier
        if delegate_tags is not None:
            self.delegate_tags = delegate_tags
        if delegate_instance_filter is not None:
            self.delegate_instance_filter = delegate_instance_filter
        if tags is not None:
            self.tags = tags
        self.filter_type = filter_type

    @property
    def status(self):
        """Gets the status of this DelegateFilterPropertiesDTO.  # noqa: E501

        Filter on delegate connectivity  # noqa: E501

        :return: The status of this DelegateFilterPropertiesDTO.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DelegateFilterPropertiesDTO.

        Filter on delegate connectivity  # noqa: E501

        :param status: The status of this DelegateFilterPropertiesDTO.  # noqa: E501
        :type: str
        """
        allowed_values = ["CONNECTED", "DISCONNECTED", "ENABLED", "WAITING_FOR_APPROVAL", "DISABLED", "DELETED"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def description(self):
        """Gets the description of this DelegateFilterPropertiesDTO.  # noqa: E501

        Filter on delegate description  # noqa: E501

        :return: The description of this DelegateFilterPropertiesDTO.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DelegateFilterPropertiesDTO.

        Filter on delegate description  # noqa: E501

        :param description: The description of this DelegateFilterPropertiesDTO.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def host_name(self):
        """Gets the host_name of this DelegateFilterPropertiesDTO.  # noqa: E501

        Filter on delegate hostName  # noqa: E501

        :return: The host_name of this DelegateFilterPropertiesDTO.  # noqa: E501
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this DelegateFilterPropertiesDTO.

        Filter on delegate hostName  # noqa: E501

        :param host_name: The host_name of this DelegateFilterPropertiesDTO.  # noqa: E501
        :type: str
        """

        self._host_name = host_name

    @property
    def delegate_name(self):
        """Gets the delegate_name of this DelegateFilterPropertiesDTO.  # noqa: E501

        Filter on delegate name  # noqa: E501

        :return: The delegate_name of this DelegateFilterPropertiesDTO.  # noqa: E501
        :rtype: str
        """
        return self._delegate_name

    @delegate_name.setter
    def delegate_name(self, delegate_name):
        """Sets the delegate_name of this DelegateFilterPropertiesDTO.

        Filter on delegate name  # noqa: E501

        :param delegate_name: The delegate_name of this DelegateFilterPropertiesDTO.  # noqa: E501
        :type: str
        """

        self._delegate_name = delegate_name

    @property
    def delegate_type(self):
        """Gets the delegate_type of this DelegateFilterPropertiesDTO.  # noqa: E501

        Filter on delegate type  # noqa: E501

        :return: The delegate_type of this DelegateFilterPropertiesDTO.  # noqa: E501
        :rtype: str
        """
        return self._delegate_type

    @delegate_type.setter
    def delegate_type(self, delegate_type):
        """Sets the delegate_type of this DelegateFilterPropertiesDTO.

        Filter on delegate type  # noqa: E501

        :param delegate_type: The delegate_type of this DelegateFilterPropertiesDTO.  # noqa: E501
        :type: str
        """

        self._delegate_type = delegate_type

    @property
    def delegate_group_identifier(self):
        """Gets the delegate_group_identifier of this DelegateFilterPropertiesDTO.  # noqa: E501

        Filter on delegate group id  # noqa: E501

        :return: The delegate_group_identifier of this DelegateFilterPropertiesDTO.  # noqa: E501
        :rtype: str
        """
        return self._delegate_group_identifier

    @delegate_group_identifier.setter
    def delegate_group_identifier(self, delegate_group_identifier):
        """Sets the delegate_group_identifier of this DelegateFilterPropertiesDTO.

        Filter on delegate group id  # noqa: E501

        :param delegate_group_identifier: The delegate_group_identifier of this DelegateFilterPropertiesDTO.  # noqa: E501
        :type: str
        """

        self._delegate_group_identifier = delegate_group_identifier

    @property
    def delegate_tags(self):
        """Gets the delegate_tags of this DelegateFilterPropertiesDTO.  # noqa: E501

        Filter on delegate tags  # noqa: E501

        :return: The delegate_tags of this DelegateFilterPropertiesDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._delegate_tags

    @delegate_tags.setter
    def delegate_tags(self, delegate_tags):
        """Sets the delegate_tags of this DelegateFilterPropertiesDTO.

        Filter on delegate tags  # noqa: E501

        :param delegate_tags: The delegate_tags of this DelegateFilterPropertiesDTO.  # noqa: E501
        :type: list[str]
        """

        self._delegate_tags = delegate_tags

    @property
    def delegate_instance_filter(self):
        """Gets the delegate_instance_filter of this DelegateFilterPropertiesDTO.  # noqa: E501

        Filter on delegate instance status  # noqa: E501

        :return: The delegate_instance_filter of this DelegateFilterPropertiesDTO.  # noqa: E501
        :rtype: str
        """
        return self._delegate_instance_filter

    @delegate_instance_filter.setter
    def delegate_instance_filter(self, delegate_instance_filter):
        """Sets the delegate_instance_filter of this DelegateFilterPropertiesDTO.

        Filter on delegate instance status  # noqa: E501

        :param delegate_instance_filter: The delegate_instance_filter of this DelegateFilterPropertiesDTO.  # noqa: E501
        :type: str
        """
        allowed_values = ["EXPIRED", "AVAILABLE"]  # noqa: E501
        if delegate_instance_filter not in allowed_values:
            raise ValueError(
                "Invalid value for `delegate_instance_filter` ({0}), must be one of {1}"  # noqa: E501
                .format(delegate_instance_filter, allowed_values)
            )

        self._delegate_instance_filter = delegate_instance_filter

    @property
    def tags(self):
        """Gets the tags of this DelegateFilterPropertiesDTO.  # noqa: E501

        Filter tags as a key-value pair.  # noqa: E501

        :return: The tags of this DelegateFilterPropertiesDTO.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this DelegateFilterPropertiesDTO.

        Filter tags as a key-value pair.  # noqa: E501

        :param tags: The tags of this DelegateFilterPropertiesDTO.  # noqa: E501
        :type: dict(str, str)
        """

        self._tags = tags

    @property
    def filter_type(self):
        """Gets the filter_type of this DelegateFilterPropertiesDTO.  # noqa: E501

        This specifies the corresponding Entity of the filter.  # noqa: E501

        :return: The filter_type of this DelegateFilterPropertiesDTO.  # noqa: E501
        :rtype: str
        """
        return self._filter_type

    @filter_type.setter
    def filter_type(self, filter_type):
        """Sets the filter_type of this DelegateFilterPropertiesDTO.

        This specifies the corresponding Entity of the filter.  # noqa: E501

        :param filter_type: The filter_type of this DelegateFilterPropertiesDTO.  # noqa: E501
        :type: str
        """
        if filter_type is None:
            raise ValueError("Invalid value for `filter_type`, must not be `None`")  # noqa: E501
        allowed_values = ["Connector", "DelegateProfile", "Delegate", "PipelineSetup", "PipelineExecution", "Deployment", "Audit", "Template", "Trigger", "EnvironmentGroup", "FileStore", "CCMRecommendation", "Anomaly", "Environment", "RuleExecution", "Override", "InputSet"]  # noqa: E501
        if filter_type not in allowed_values:
            raise ValueError(
                "Invalid value for `filter_type` ({0}), must be one of {1}"  # noqa: E501
                .format(filter_type, allowed_values)
            )

        self._filter_type = filter_type

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
        if issubclass(DelegateFilterPropertiesDTO, dict):
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
        if not isinstance(other, DelegateFilterPropertiesDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
