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

class ApplicationsResourceDiff(object):
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
        'group': 'str',
        'kind': 'str',
        'namespace': 'str',
        'name': 'str',
        'target_state': 'str',
        'live_state': 'str',
        'diff': 'str',
        'hook': 'bool',
        'normalized_live_state': 'str',
        'predicted_live_state': 'str',
        'resource_version': 'str',
        'modified': 'bool'
    }

    attribute_map = {
        'group': 'group',
        'kind': 'kind',
        'namespace': 'namespace',
        'name': 'name',
        'target_state': 'targetState',
        'live_state': 'liveState',
        'diff': 'diff',
        'hook': 'hook',
        'normalized_live_state': 'normalizedLiveState',
        'predicted_live_state': 'predictedLiveState',
        'resource_version': 'resourceVersion',
        'modified': 'modified'
    }

    def __init__(self, group=None, kind=None, namespace=None, name=None, target_state=None, live_state=None, diff=None, hook=None, normalized_live_state=None, predicted_live_state=None, resource_version=None, modified=None):  # noqa: E501
        """ApplicationsResourceDiff - a model defined in Swagger"""  # noqa: E501
        self._group = None
        self._kind = None
        self._namespace = None
        self._name = None
        self._target_state = None
        self._live_state = None
        self._diff = None
        self._hook = None
        self._normalized_live_state = None
        self._predicted_live_state = None
        self._resource_version = None
        self._modified = None
        self.discriminator = None
        if group is not None:
            self.group = group
        if kind is not None:
            self.kind = kind
        if namespace is not None:
            self.namespace = namespace
        if name is not None:
            self.name = name
        if target_state is not None:
            self.target_state = target_state
        if live_state is not None:
            self.live_state = live_state
        if diff is not None:
            self.diff = diff
        if hook is not None:
            self.hook = hook
        if normalized_live_state is not None:
            self.normalized_live_state = normalized_live_state
        if predicted_live_state is not None:
            self.predicted_live_state = predicted_live_state
        if resource_version is not None:
            self.resource_version = resource_version
        if modified is not None:
            self.modified = modified

    @property
    def group(self):
        """Gets the group of this ApplicationsResourceDiff.  # noqa: E501


        :return: The group of this ApplicationsResourceDiff.  # noqa: E501
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this ApplicationsResourceDiff.


        :param group: The group of this ApplicationsResourceDiff.  # noqa: E501
        :type: str
        """

        self._group = group

    @property
    def kind(self):
        """Gets the kind of this ApplicationsResourceDiff.  # noqa: E501


        :return: The kind of this ApplicationsResourceDiff.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this ApplicationsResourceDiff.


        :param kind: The kind of this ApplicationsResourceDiff.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def namespace(self):
        """Gets the namespace of this ApplicationsResourceDiff.  # noqa: E501


        :return: The namespace of this ApplicationsResourceDiff.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this ApplicationsResourceDiff.


        :param namespace: The namespace of this ApplicationsResourceDiff.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

    @property
    def name(self):
        """Gets the name of this ApplicationsResourceDiff.  # noqa: E501


        :return: The name of this ApplicationsResourceDiff.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApplicationsResourceDiff.


        :param name: The name of this ApplicationsResourceDiff.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def target_state(self):
        """Gets the target_state of this ApplicationsResourceDiff.  # noqa: E501


        :return: The target_state of this ApplicationsResourceDiff.  # noqa: E501
        :rtype: str
        """
        return self._target_state

    @target_state.setter
    def target_state(self, target_state):
        """Sets the target_state of this ApplicationsResourceDiff.


        :param target_state: The target_state of this ApplicationsResourceDiff.  # noqa: E501
        :type: str
        """

        self._target_state = target_state

    @property
    def live_state(self):
        """Gets the live_state of this ApplicationsResourceDiff.  # noqa: E501


        :return: The live_state of this ApplicationsResourceDiff.  # noqa: E501
        :rtype: str
        """
        return self._live_state

    @live_state.setter
    def live_state(self, live_state):
        """Sets the live_state of this ApplicationsResourceDiff.


        :param live_state: The live_state of this ApplicationsResourceDiff.  # noqa: E501
        :type: str
        """

        self._live_state = live_state

    @property
    def diff(self):
        """Gets the diff of this ApplicationsResourceDiff.  # noqa: E501


        :return: The diff of this ApplicationsResourceDiff.  # noqa: E501
        :rtype: str
        """
        return self._diff

    @diff.setter
    def diff(self, diff):
        """Sets the diff of this ApplicationsResourceDiff.


        :param diff: The diff of this ApplicationsResourceDiff.  # noqa: E501
        :type: str
        """

        self._diff = diff

    @property
    def hook(self):
        """Gets the hook of this ApplicationsResourceDiff.  # noqa: E501


        :return: The hook of this ApplicationsResourceDiff.  # noqa: E501
        :rtype: bool
        """
        return self._hook

    @hook.setter
    def hook(self, hook):
        """Sets the hook of this ApplicationsResourceDiff.


        :param hook: The hook of this ApplicationsResourceDiff.  # noqa: E501
        :type: bool
        """

        self._hook = hook

    @property
    def normalized_live_state(self):
        """Gets the normalized_live_state of this ApplicationsResourceDiff.  # noqa: E501


        :return: The normalized_live_state of this ApplicationsResourceDiff.  # noqa: E501
        :rtype: str
        """
        return self._normalized_live_state

    @normalized_live_state.setter
    def normalized_live_state(self, normalized_live_state):
        """Sets the normalized_live_state of this ApplicationsResourceDiff.


        :param normalized_live_state: The normalized_live_state of this ApplicationsResourceDiff.  # noqa: E501
        :type: str
        """

        self._normalized_live_state = normalized_live_state

    @property
    def predicted_live_state(self):
        """Gets the predicted_live_state of this ApplicationsResourceDiff.  # noqa: E501


        :return: The predicted_live_state of this ApplicationsResourceDiff.  # noqa: E501
        :rtype: str
        """
        return self._predicted_live_state

    @predicted_live_state.setter
    def predicted_live_state(self, predicted_live_state):
        """Sets the predicted_live_state of this ApplicationsResourceDiff.


        :param predicted_live_state: The predicted_live_state of this ApplicationsResourceDiff.  # noqa: E501
        :type: str
        """

        self._predicted_live_state = predicted_live_state

    @property
    def resource_version(self):
        """Gets the resource_version of this ApplicationsResourceDiff.  # noqa: E501


        :return: The resource_version of this ApplicationsResourceDiff.  # noqa: E501
        :rtype: str
        """
        return self._resource_version

    @resource_version.setter
    def resource_version(self, resource_version):
        """Sets the resource_version of this ApplicationsResourceDiff.


        :param resource_version: The resource_version of this ApplicationsResourceDiff.  # noqa: E501
        :type: str
        """

        self._resource_version = resource_version

    @property
    def modified(self):
        """Gets the modified of this ApplicationsResourceDiff.  # noqa: E501


        :return: The modified of this ApplicationsResourceDiff.  # noqa: E501
        :rtype: bool
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this ApplicationsResourceDiff.


        :param modified: The modified of this ApplicationsResourceDiff.  # noqa: E501
        :type: bool
        """

        self._modified = modified

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
        if issubclass(ApplicationsResourceDiff, dict):
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
        if not isinstance(other, ApplicationsResourceDiff):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
