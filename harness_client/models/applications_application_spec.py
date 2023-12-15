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

class ApplicationsApplicationSpec(object):
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
        'source': 'ApplicationsApplicationSource',
        'destination': 'ApplicationsApplicationDestination',
        'project': 'str',
        'sync_policy': 'ApplicationsSyncPolicy',
        'ignore_differences': 'list[ApplicationsResourceIgnoreDifferences]',
        'info': 'list[ApplicationsInfo]',
        'revision_history_limit': 'str'
    }

    attribute_map = {
        'source': 'source',
        'destination': 'destination',
        'project': 'project',
        'sync_policy': 'syncPolicy',
        'ignore_differences': 'ignoreDifferences',
        'info': 'info',
        'revision_history_limit': 'revisionHistoryLimit'
    }

    def __init__(self, source=None, destination=None, project=None, sync_policy=None, ignore_differences=None, info=None, revision_history_limit=None):  # noqa: E501
        """ApplicationsApplicationSpec - a model defined in Swagger"""  # noqa: E501
        self._source = None
        self._destination = None
        self._project = None
        self._sync_policy = None
        self._ignore_differences = None
        self._info = None
        self._revision_history_limit = None
        self.discriminator = None
        if source is not None:
            self.source = source
        if destination is not None:
            self.destination = destination
        if project is not None:
            self.project = project
        if sync_policy is not None:
            self.sync_policy = sync_policy
        if ignore_differences is not None:
            self.ignore_differences = ignore_differences
        if info is not None:
            self.info = info
        if revision_history_limit is not None:
            self.revision_history_limit = revision_history_limit

    @property
    def source(self):
        """Gets the source of this ApplicationsApplicationSpec.  # noqa: E501


        :return: The source of this ApplicationsApplicationSpec.  # noqa: E501
        :rtype: ApplicationsApplicationSource
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this ApplicationsApplicationSpec.


        :param source: The source of this ApplicationsApplicationSpec.  # noqa: E501
        :type: ApplicationsApplicationSource
        """

        self._source = source

    @property
    def destination(self):
        """Gets the destination of this ApplicationsApplicationSpec.  # noqa: E501


        :return: The destination of this ApplicationsApplicationSpec.  # noqa: E501
        :rtype: ApplicationsApplicationDestination
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this ApplicationsApplicationSpec.


        :param destination: The destination of this ApplicationsApplicationSpec.  # noqa: E501
        :type: ApplicationsApplicationDestination
        """

        self._destination = destination

    @property
    def project(self):
        """Gets the project of this ApplicationsApplicationSpec.  # noqa: E501

        Project is a reference to the project this application belongs to. The empty string means that application belongs to the 'default' project.  # noqa: E501

        :return: The project of this ApplicationsApplicationSpec.  # noqa: E501
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this ApplicationsApplicationSpec.

        Project is a reference to the project this application belongs to. The empty string means that application belongs to the 'default' project.  # noqa: E501

        :param project: The project of this ApplicationsApplicationSpec.  # noqa: E501
        :type: str
        """

        self._project = project

    @property
    def sync_policy(self):
        """Gets the sync_policy of this ApplicationsApplicationSpec.  # noqa: E501


        :return: The sync_policy of this ApplicationsApplicationSpec.  # noqa: E501
        :rtype: ApplicationsSyncPolicy
        """
        return self._sync_policy

    @sync_policy.setter
    def sync_policy(self, sync_policy):
        """Sets the sync_policy of this ApplicationsApplicationSpec.


        :param sync_policy: The sync_policy of this ApplicationsApplicationSpec.  # noqa: E501
        :type: ApplicationsSyncPolicy
        """

        self._sync_policy = sync_policy

    @property
    def ignore_differences(self):
        """Gets the ignore_differences of this ApplicationsApplicationSpec.  # noqa: E501


        :return: The ignore_differences of this ApplicationsApplicationSpec.  # noqa: E501
        :rtype: list[ApplicationsResourceIgnoreDifferences]
        """
        return self._ignore_differences

    @ignore_differences.setter
    def ignore_differences(self, ignore_differences):
        """Sets the ignore_differences of this ApplicationsApplicationSpec.


        :param ignore_differences: The ignore_differences of this ApplicationsApplicationSpec.  # noqa: E501
        :type: list[ApplicationsResourceIgnoreDifferences]
        """

        self._ignore_differences = ignore_differences

    @property
    def info(self):
        """Gets the info of this ApplicationsApplicationSpec.  # noqa: E501


        :return: The info of this ApplicationsApplicationSpec.  # noqa: E501
        :rtype: list[ApplicationsInfo]
        """
        return self._info

    @info.setter
    def info(self, info):
        """Sets the info of this ApplicationsApplicationSpec.


        :param info: The info of this ApplicationsApplicationSpec.  # noqa: E501
        :type: list[ApplicationsInfo]
        """

        self._info = info

    @property
    def revision_history_limit(self):
        """Gets the revision_history_limit of this ApplicationsApplicationSpec.  # noqa: E501

        RevisionHistoryLimit limits the number of items kept in the application's revision history, which is used for informational purposes as well as for rollbacks to previous versions. This should only be changed in exceptional circumstances. Setting to zero will store no history. This will reduce storage used. Increasing will increase the space used to store the history, so we do not recommend increasing it. Default is 10.  # noqa: E501

        :return: The revision_history_limit of this ApplicationsApplicationSpec.  # noqa: E501
        :rtype: str
        """
        return self._revision_history_limit

    @revision_history_limit.setter
    def revision_history_limit(self, revision_history_limit):
        """Sets the revision_history_limit of this ApplicationsApplicationSpec.

        RevisionHistoryLimit limits the number of items kept in the application's revision history, which is used for informational purposes as well as for rollbacks to previous versions. This should only be changed in exceptional circumstances. Setting to zero will store no history. This will reduce storage used. Increasing will increase the space used to store the history, so we do not recommend increasing it. Default is 10.  # noqa: E501

        :param revision_history_limit: The revision_history_limit of this ApplicationsApplicationSpec.  # noqa: E501
        :type: str
        """

        self._revision_history_limit = revision_history_limit

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
        if issubclass(ApplicationsApplicationSpec, dict):
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
        if not isinstance(other, ApplicationsApplicationSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
