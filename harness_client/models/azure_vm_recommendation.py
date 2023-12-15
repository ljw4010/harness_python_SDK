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

class AzureVmRecommendation(object):
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
        'tenant_id': 'str',
        'subscription_id': 'str',
        'resource_group_id': 'str',
        'vm_name': 'str',
        'vm_id': 'str',
        'connector_name': 'str',
        'connector_id': 'str',
        'duration': 'int',
        'current_configurations': 'AzureVmDTO',
        'show_terminated': 'bool',
        'target_configurations': 'AzureVmDTO',
        'jira_details': 'CCMJiraDetails',
        'service_now_details': 'CCMServiceNowDetails'
    }

    attribute_map = {
        'id': 'id',
        'tenant_id': 'tenantId',
        'subscription_id': 'subscriptionId',
        'resource_group_id': 'resourceGroupId',
        'vm_name': 'vmName',
        'vm_id': 'vmId',
        'connector_name': 'connectorName',
        'connector_id': 'connectorId',
        'duration': 'duration',
        'current_configurations': 'CurrentConfigurations',
        'show_terminated': 'showTerminated',
        'target_configurations': 'TargetConfigurations',
        'jira_details': 'jiraDetails',
        'service_now_details': 'serviceNowDetails'
    }

    def __init__(self, id=None, tenant_id=None, subscription_id=None, resource_group_id=None, vm_name=None, vm_id=None, connector_name=None, connector_id=None, duration=None, current_configurations=None, show_terminated=None, target_configurations=None, jira_details=None, service_now_details=None):  # noqa: E501
        """AzureVmRecommendation - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._tenant_id = None
        self._subscription_id = None
        self._resource_group_id = None
        self._vm_name = None
        self._vm_id = None
        self._connector_name = None
        self._connector_id = None
        self._duration = None
        self._current_configurations = None
        self._show_terminated = None
        self._target_configurations = None
        self._jira_details = None
        self._service_now_details = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if subscription_id is not None:
            self.subscription_id = subscription_id
        if resource_group_id is not None:
            self.resource_group_id = resource_group_id
        if vm_name is not None:
            self.vm_name = vm_name
        if vm_id is not None:
            self.vm_id = vm_id
        if connector_name is not None:
            self.connector_name = connector_name
        if connector_id is not None:
            self.connector_id = connector_id
        if duration is not None:
            self.duration = duration
        if current_configurations is not None:
            self.current_configurations = current_configurations
        if show_terminated is not None:
            self.show_terminated = show_terminated
        if target_configurations is not None:
            self.target_configurations = target_configurations
        if jira_details is not None:
            self.jira_details = jira_details
        if service_now_details is not None:
            self.service_now_details = service_now_details

    @property
    def id(self):
        """Gets the id of this AzureVmRecommendation.  # noqa: E501


        :return: The id of this AzureVmRecommendation.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AzureVmRecommendation.


        :param id: The id of this AzureVmRecommendation.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def tenant_id(self):
        """Gets the tenant_id of this AzureVmRecommendation.  # noqa: E501


        :return: The tenant_id of this AzureVmRecommendation.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this AzureVmRecommendation.


        :param tenant_id: The tenant_id of this AzureVmRecommendation.  # noqa: E501
        :type: str
        """

        self._tenant_id = tenant_id

    @property
    def subscription_id(self):
        """Gets the subscription_id of this AzureVmRecommendation.  # noqa: E501


        :return: The subscription_id of this AzureVmRecommendation.  # noqa: E501
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this AzureVmRecommendation.


        :param subscription_id: The subscription_id of this AzureVmRecommendation.  # noqa: E501
        :type: str
        """

        self._subscription_id = subscription_id

    @property
    def resource_group_id(self):
        """Gets the resource_group_id of this AzureVmRecommendation.  # noqa: E501


        :return: The resource_group_id of this AzureVmRecommendation.  # noqa: E501
        :rtype: str
        """
        return self._resource_group_id

    @resource_group_id.setter
    def resource_group_id(self, resource_group_id):
        """Sets the resource_group_id of this AzureVmRecommendation.


        :param resource_group_id: The resource_group_id of this AzureVmRecommendation.  # noqa: E501
        :type: str
        """

        self._resource_group_id = resource_group_id

    @property
    def vm_name(self):
        """Gets the vm_name of this AzureVmRecommendation.  # noqa: E501


        :return: The vm_name of this AzureVmRecommendation.  # noqa: E501
        :rtype: str
        """
        return self._vm_name

    @vm_name.setter
    def vm_name(self, vm_name):
        """Sets the vm_name of this AzureVmRecommendation.


        :param vm_name: The vm_name of this AzureVmRecommendation.  # noqa: E501
        :type: str
        """

        self._vm_name = vm_name

    @property
    def vm_id(self):
        """Gets the vm_id of this AzureVmRecommendation.  # noqa: E501


        :return: The vm_id of this AzureVmRecommendation.  # noqa: E501
        :rtype: str
        """
        return self._vm_id

    @vm_id.setter
    def vm_id(self, vm_id):
        """Sets the vm_id of this AzureVmRecommendation.


        :param vm_id: The vm_id of this AzureVmRecommendation.  # noqa: E501
        :type: str
        """

        self._vm_id = vm_id

    @property
    def connector_name(self):
        """Gets the connector_name of this AzureVmRecommendation.  # noqa: E501


        :return: The connector_name of this AzureVmRecommendation.  # noqa: E501
        :rtype: str
        """
        return self._connector_name

    @connector_name.setter
    def connector_name(self, connector_name):
        """Sets the connector_name of this AzureVmRecommendation.


        :param connector_name: The connector_name of this AzureVmRecommendation.  # noqa: E501
        :type: str
        """

        self._connector_name = connector_name

    @property
    def connector_id(self):
        """Gets the connector_id of this AzureVmRecommendation.  # noqa: E501


        :return: The connector_id of this AzureVmRecommendation.  # noqa: E501
        :rtype: str
        """
        return self._connector_id

    @connector_id.setter
    def connector_id(self, connector_id):
        """Sets the connector_id of this AzureVmRecommendation.


        :param connector_id: The connector_id of this AzureVmRecommendation.  # noqa: E501
        :type: str
        """

        self._connector_id = connector_id

    @property
    def duration(self):
        """Gets the duration of this AzureVmRecommendation.  # noqa: E501


        :return: The duration of this AzureVmRecommendation.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this AzureVmRecommendation.


        :param duration: The duration of this AzureVmRecommendation.  # noqa: E501
        :type: int
        """

        self._duration = duration

    @property
    def current_configurations(self):
        """Gets the current_configurations of this AzureVmRecommendation.  # noqa: E501


        :return: The current_configurations of this AzureVmRecommendation.  # noqa: E501
        :rtype: AzureVmDTO
        """
        return self._current_configurations

    @current_configurations.setter
    def current_configurations(self, current_configurations):
        """Sets the current_configurations of this AzureVmRecommendation.


        :param current_configurations: The current_configurations of this AzureVmRecommendation.  # noqa: E501
        :type: AzureVmDTO
        """

        self._current_configurations = current_configurations

    @property
    def show_terminated(self):
        """Gets the show_terminated of this AzureVmRecommendation.  # noqa: E501


        :return: The show_terminated of this AzureVmRecommendation.  # noqa: E501
        :rtype: bool
        """
        return self._show_terminated

    @show_terminated.setter
    def show_terminated(self, show_terminated):
        """Sets the show_terminated of this AzureVmRecommendation.


        :param show_terminated: The show_terminated of this AzureVmRecommendation.  # noqa: E501
        :type: bool
        """

        self._show_terminated = show_terminated

    @property
    def target_configurations(self):
        """Gets the target_configurations of this AzureVmRecommendation.  # noqa: E501


        :return: The target_configurations of this AzureVmRecommendation.  # noqa: E501
        :rtype: AzureVmDTO
        """
        return self._target_configurations

    @target_configurations.setter
    def target_configurations(self, target_configurations):
        """Sets the target_configurations of this AzureVmRecommendation.


        :param target_configurations: The target_configurations of this AzureVmRecommendation.  # noqa: E501
        :type: AzureVmDTO
        """

        self._target_configurations = target_configurations

    @property
    def jira_details(self):
        """Gets the jira_details of this AzureVmRecommendation.  # noqa: E501


        :return: The jira_details of this AzureVmRecommendation.  # noqa: E501
        :rtype: CCMJiraDetails
        """
        return self._jira_details

    @jira_details.setter
    def jira_details(self, jira_details):
        """Sets the jira_details of this AzureVmRecommendation.


        :param jira_details: The jira_details of this AzureVmRecommendation.  # noqa: E501
        :type: CCMJiraDetails
        """

        self._jira_details = jira_details

    @property
    def service_now_details(self):
        """Gets the service_now_details of this AzureVmRecommendation.  # noqa: E501


        :return: The service_now_details of this AzureVmRecommendation.  # noqa: E501
        :rtype: CCMServiceNowDetails
        """
        return self._service_now_details

    @service_now_details.setter
    def service_now_details(self, service_now_details):
        """Sets the service_now_details of this AzureVmRecommendation.


        :param service_now_details: The service_now_details of this AzureVmRecommendation.  # noqa: E501
        :type: CCMServiceNowDetails
        """

        self._service_now_details = service_now_details

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
        if issubclass(AzureVmRecommendation, dict):
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
        if not isinstance(other, AzureVmRecommendation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
