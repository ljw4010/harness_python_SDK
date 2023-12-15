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

class Target(object):
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
        'account': 'str',
        'anonymous': 'bool',
        'attributes': 'object',
        'created_at': 'int',
        'environment': 'str',
        'identifier': 'str',
        'name': 'str',
        'org': 'str',
        'project': 'str',
        'segments': 'list[Segment]'
    }

    attribute_map = {
        'account': 'account',
        'anonymous': 'anonymous',
        'attributes': 'attributes',
        'created_at': 'createdAt',
        'environment': 'environment',
        'identifier': 'identifier',
        'name': 'name',
        'org': 'org',
        'project': 'project',
        'segments': 'segments'
    }

    def __init__(self, account=None, anonymous=None, attributes=None, created_at=None, environment=None, identifier=None, name=None, org=None, project=None, segments=None):  # noqa: E501
        """Target - a model defined in Swagger"""  # noqa: E501
        self._account = None
        self._anonymous = None
        self._attributes = None
        self._created_at = None
        self._environment = None
        self._identifier = None
        self._name = None
        self._org = None
        self._project = None
        self._segments = None
        self.discriminator = None
        self.account = account
        if anonymous is not None:
            self.anonymous = anonymous
        if attributes is not None:
            self.attributes = attributes
        if created_at is not None:
            self.created_at = created_at
        self.environment = environment
        self.identifier = identifier
        self.name = name
        self.org = org
        self.project = project
        if segments is not None:
            self.segments = segments

    @property
    def account(self):
        """Gets the account of this Target.  # noqa: E501

        The account ID that the target belongs to  # noqa: E501

        :return: The account of this Target.  # noqa: E501
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this Target.

        The account ID that the target belongs to  # noqa: E501

        :param account: The account of this Target.  # noqa: E501
        :type: str
        """
        if account is None:
            raise ValueError("Invalid value for `account`, must not be `None`")  # noqa: E501

        self._account = account

    @property
    def anonymous(self):
        """Gets the anonymous of this Target.  # noqa: E501

        Indicates if this target is anonymous  # noqa: E501

        :return: The anonymous of this Target.  # noqa: E501
        :rtype: bool
        """
        return self._anonymous

    @anonymous.setter
    def anonymous(self, anonymous):
        """Sets the anonymous of this Target.

        Indicates if this target is anonymous  # noqa: E501

        :param anonymous: The anonymous of this Target.  # noqa: E501
        :type: bool
        """

        self._anonymous = anonymous

    @property
    def attributes(self):
        """Gets the attributes of this Target.  # noqa: E501

        a JSON representation of the attributes for this target  # noqa: E501

        :return: The attributes of this Target.  # noqa: E501
        :rtype: object
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this Target.

        a JSON representation of the attributes for this target  # noqa: E501

        :param attributes: The attributes of this Target.  # noqa: E501
        :type: object
        """

        self._attributes = attributes

    @property
    def created_at(self):
        """Gets the created_at of this Target.  # noqa: E501

        The date and time in milliseconds when this Target was created  # noqa: E501

        :return: The created_at of this Target.  # noqa: E501
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Target.

        The date and time in milliseconds when this Target was created  # noqa: E501

        :param created_at: The created_at of this Target.  # noqa: E501
        :type: int
        """

        self._created_at = created_at

    @property
    def environment(self):
        """Gets the environment of this Target.  # noqa: E501

        The identifier for the environment that the target belongs to  # noqa: E501

        :return: The environment of this Target.  # noqa: E501
        :rtype: str
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this Target.

        The identifier for the environment that the target belongs to  # noqa: E501

        :param environment: The environment of this Target.  # noqa: E501
        :type: str
        """
        if environment is None:
            raise ValueError("Invalid value for `environment`, must not be `None`")  # noqa: E501

        self._environment = environment

    @property
    def identifier(self):
        """Gets the identifier of this Target.  # noqa: E501

        The unique identifier for this target  # noqa: E501

        :return: The identifier of this Target.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this Target.

        The unique identifier for this target  # noqa: E501

        :param identifier: The identifier of this Target.  # noqa: E501
        :type: str
        """
        if identifier is None:
            raise ValueError("Invalid value for `identifier`, must not be `None`")  # noqa: E501

        self._identifier = identifier

    @property
    def name(self):
        """Gets the name of this Target.  # noqa: E501

        The name of this Target  # noqa: E501

        :return: The name of this Target.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Target.

        The name of this Target  # noqa: E501

        :param name: The name of this Target.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def org(self):
        """Gets the org of this Target.  # noqa: E501

        The identifier for the organization that the target belongs to  # noqa: E501

        :return: The org of this Target.  # noqa: E501
        :rtype: str
        """
        return self._org

    @org.setter
    def org(self, org):
        """Sets the org of this Target.

        The identifier for the organization that the target belongs to  # noqa: E501

        :param org: The org of this Target.  # noqa: E501
        :type: str
        """
        if org is None:
            raise ValueError("Invalid value for `org`, must not be `None`")  # noqa: E501

        self._org = org

    @property
    def project(self):
        """Gets the project of this Target.  # noqa: E501

        The identifier for the project that this target belongs to  # noqa: E501

        :return: The project of this Target.  # noqa: E501
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this Target.

        The identifier for the project that this target belongs to  # noqa: E501

        :param project: The project of this Target.  # noqa: E501
        :type: str
        """
        if project is None:
            raise ValueError("Invalid value for `project`, must not be `None`")  # noqa: E501

        self._project = project

    @property
    def segments(self):
        """Gets the segments of this Target.  # noqa: E501

        A list of Target Groups (Segments) that this Target belongs to  # noqa: E501

        :return: The segments of this Target.  # noqa: E501
        :rtype: list[Segment]
        """
        return self._segments

    @segments.setter
    def segments(self, segments):
        """Sets the segments of this Target.

        A list of Target Groups (Segments) that this Target belongs to  # noqa: E501

        :param segments: The segments of this Target.  # noqa: E501
        :type: list[Segment]
        """

        self._segments = segments

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
        if issubclass(Target, dict):
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
        if not isinstance(other, Target):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
