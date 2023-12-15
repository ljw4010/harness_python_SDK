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

class AppprojectsAppProjectSpec(object):
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
        'source_repos': 'list[str]',
        'destinations': 'list[AppprojectsApplicationDestination]',
        'description': 'str',
        'roles': 'list[AppprojectsProjectRole]',
        'cluster_resource_whitelist': 'list[V1GroupKind]',
        'namespace_resource_blacklist': 'list[V1GroupKind]',
        'orphaned_resources': 'AppprojectsOrphanedResourcesMonitorSettings',
        'sync_windows': 'list[AppprojectsSyncWindow]',
        'namespace_resource_whitelist': 'list[V1GroupKind]',
        'signature_keys': 'list[AppprojectsSignatureKey]',
        'cluster_resource_blacklist': 'list[V1GroupKind]'
    }

    attribute_map = {
        'source_repos': 'sourceRepos',
        'destinations': 'destinations',
        'description': 'description',
        'roles': 'roles',
        'cluster_resource_whitelist': 'clusterResourceWhitelist',
        'namespace_resource_blacklist': 'namespaceResourceBlacklist',
        'orphaned_resources': 'orphanedResources',
        'sync_windows': 'syncWindows',
        'namespace_resource_whitelist': 'namespaceResourceWhitelist',
        'signature_keys': 'signatureKeys',
        'cluster_resource_blacklist': 'clusterResourceBlacklist'
    }

    def __init__(self, source_repos=None, destinations=None, description=None, roles=None, cluster_resource_whitelist=None, namespace_resource_blacklist=None, orphaned_resources=None, sync_windows=None, namespace_resource_whitelist=None, signature_keys=None, cluster_resource_blacklist=None):  # noqa: E501
        """AppprojectsAppProjectSpec - a model defined in Swagger"""  # noqa: E501
        self._source_repos = None
        self._destinations = None
        self._description = None
        self._roles = None
        self._cluster_resource_whitelist = None
        self._namespace_resource_blacklist = None
        self._orphaned_resources = None
        self._sync_windows = None
        self._namespace_resource_whitelist = None
        self._signature_keys = None
        self._cluster_resource_blacklist = None
        self.discriminator = None
        if source_repos is not None:
            self.source_repos = source_repos
        if destinations is not None:
            self.destinations = destinations
        if description is not None:
            self.description = description
        if roles is not None:
            self.roles = roles
        if cluster_resource_whitelist is not None:
            self.cluster_resource_whitelist = cluster_resource_whitelist
        if namespace_resource_blacklist is not None:
            self.namespace_resource_blacklist = namespace_resource_blacklist
        if orphaned_resources is not None:
            self.orphaned_resources = orphaned_resources
        if sync_windows is not None:
            self.sync_windows = sync_windows
        if namespace_resource_whitelist is not None:
            self.namespace_resource_whitelist = namespace_resource_whitelist
        if signature_keys is not None:
            self.signature_keys = signature_keys
        if cluster_resource_blacklist is not None:
            self.cluster_resource_blacklist = cluster_resource_blacklist

    @property
    def source_repos(self):
        """Gets the source_repos of this AppprojectsAppProjectSpec.  # noqa: E501


        :return: The source_repos of this AppprojectsAppProjectSpec.  # noqa: E501
        :rtype: list[str]
        """
        return self._source_repos

    @source_repos.setter
    def source_repos(self, source_repos):
        """Sets the source_repos of this AppprojectsAppProjectSpec.


        :param source_repos: The source_repos of this AppprojectsAppProjectSpec.  # noqa: E501
        :type: list[str]
        """

        self._source_repos = source_repos

    @property
    def destinations(self):
        """Gets the destinations of this AppprojectsAppProjectSpec.  # noqa: E501


        :return: The destinations of this AppprojectsAppProjectSpec.  # noqa: E501
        :rtype: list[AppprojectsApplicationDestination]
        """
        return self._destinations

    @destinations.setter
    def destinations(self, destinations):
        """Sets the destinations of this AppprojectsAppProjectSpec.


        :param destinations: The destinations of this AppprojectsAppProjectSpec.  # noqa: E501
        :type: list[AppprojectsApplicationDestination]
        """

        self._destinations = destinations

    @property
    def description(self):
        """Gets the description of this AppprojectsAppProjectSpec.  # noqa: E501


        :return: The description of this AppprojectsAppProjectSpec.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AppprojectsAppProjectSpec.


        :param description: The description of this AppprojectsAppProjectSpec.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def roles(self):
        """Gets the roles of this AppprojectsAppProjectSpec.  # noqa: E501


        :return: The roles of this AppprojectsAppProjectSpec.  # noqa: E501
        :rtype: list[AppprojectsProjectRole]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this AppprojectsAppProjectSpec.


        :param roles: The roles of this AppprojectsAppProjectSpec.  # noqa: E501
        :type: list[AppprojectsProjectRole]
        """

        self._roles = roles

    @property
    def cluster_resource_whitelist(self):
        """Gets the cluster_resource_whitelist of this AppprojectsAppProjectSpec.  # noqa: E501


        :return: The cluster_resource_whitelist of this AppprojectsAppProjectSpec.  # noqa: E501
        :rtype: list[V1GroupKind]
        """
        return self._cluster_resource_whitelist

    @cluster_resource_whitelist.setter
    def cluster_resource_whitelist(self, cluster_resource_whitelist):
        """Sets the cluster_resource_whitelist of this AppprojectsAppProjectSpec.


        :param cluster_resource_whitelist: The cluster_resource_whitelist of this AppprojectsAppProjectSpec.  # noqa: E501
        :type: list[V1GroupKind]
        """

        self._cluster_resource_whitelist = cluster_resource_whitelist

    @property
    def namespace_resource_blacklist(self):
        """Gets the namespace_resource_blacklist of this AppprojectsAppProjectSpec.  # noqa: E501


        :return: The namespace_resource_blacklist of this AppprojectsAppProjectSpec.  # noqa: E501
        :rtype: list[V1GroupKind]
        """
        return self._namespace_resource_blacklist

    @namespace_resource_blacklist.setter
    def namespace_resource_blacklist(self, namespace_resource_blacklist):
        """Sets the namespace_resource_blacklist of this AppprojectsAppProjectSpec.


        :param namespace_resource_blacklist: The namespace_resource_blacklist of this AppprojectsAppProjectSpec.  # noqa: E501
        :type: list[V1GroupKind]
        """

        self._namespace_resource_blacklist = namespace_resource_blacklist

    @property
    def orphaned_resources(self):
        """Gets the orphaned_resources of this AppprojectsAppProjectSpec.  # noqa: E501


        :return: The orphaned_resources of this AppprojectsAppProjectSpec.  # noqa: E501
        :rtype: AppprojectsOrphanedResourcesMonitorSettings
        """
        return self._orphaned_resources

    @orphaned_resources.setter
    def orphaned_resources(self, orphaned_resources):
        """Sets the orphaned_resources of this AppprojectsAppProjectSpec.


        :param orphaned_resources: The orphaned_resources of this AppprojectsAppProjectSpec.  # noqa: E501
        :type: AppprojectsOrphanedResourcesMonitorSettings
        """

        self._orphaned_resources = orphaned_resources

    @property
    def sync_windows(self):
        """Gets the sync_windows of this AppprojectsAppProjectSpec.  # noqa: E501


        :return: The sync_windows of this AppprojectsAppProjectSpec.  # noqa: E501
        :rtype: list[AppprojectsSyncWindow]
        """
        return self._sync_windows

    @sync_windows.setter
    def sync_windows(self, sync_windows):
        """Sets the sync_windows of this AppprojectsAppProjectSpec.


        :param sync_windows: The sync_windows of this AppprojectsAppProjectSpec.  # noqa: E501
        :type: list[AppprojectsSyncWindow]
        """

        self._sync_windows = sync_windows

    @property
    def namespace_resource_whitelist(self):
        """Gets the namespace_resource_whitelist of this AppprojectsAppProjectSpec.  # noqa: E501


        :return: The namespace_resource_whitelist of this AppprojectsAppProjectSpec.  # noqa: E501
        :rtype: list[V1GroupKind]
        """
        return self._namespace_resource_whitelist

    @namespace_resource_whitelist.setter
    def namespace_resource_whitelist(self, namespace_resource_whitelist):
        """Sets the namespace_resource_whitelist of this AppprojectsAppProjectSpec.


        :param namespace_resource_whitelist: The namespace_resource_whitelist of this AppprojectsAppProjectSpec.  # noqa: E501
        :type: list[V1GroupKind]
        """

        self._namespace_resource_whitelist = namespace_resource_whitelist

    @property
    def signature_keys(self):
        """Gets the signature_keys of this AppprojectsAppProjectSpec.  # noqa: E501


        :return: The signature_keys of this AppprojectsAppProjectSpec.  # noqa: E501
        :rtype: list[AppprojectsSignatureKey]
        """
        return self._signature_keys

    @signature_keys.setter
    def signature_keys(self, signature_keys):
        """Sets the signature_keys of this AppprojectsAppProjectSpec.


        :param signature_keys: The signature_keys of this AppprojectsAppProjectSpec.  # noqa: E501
        :type: list[AppprojectsSignatureKey]
        """

        self._signature_keys = signature_keys

    @property
    def cluster_resource_blacklist(self):
        """Gets the cluster_resource_blacklist of this AppprojectsAppProjectSpec.  # noqa: E501


        :return: The cluster_resource_blacklist of this AppprojectsAppProjectSpec.  # noqa: E501
        :rtype: list[V1GroupKind]
        """
        return self._cluster_resource_blacklist

    @cluster_resource_blacklist.setter
    def cluster_resource_blacklist(self, cluster_resource_blacklist):
        """Sets the cluster_resource_blacklist of this AppprojectsAppProjectSpec.


        :param cluster_resource_blacklist: The cluster_resource_blacklist of this AppprojectsAppProjectSpec.  # noqa: E501
        :type: list[V1GroupKind]
        """

        self._cluster_resource_blacklist = cluster_resource_blacklist

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
        if issubclass(AppprojectsAppProjectSpec, dict):
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
        if not isinstance(other, AppprojectsAppProjectSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
