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

class EntityInfo(object):
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
        'field': 'str',
        'cluster_name': 'str',
        'cluster_id': 'str',
        'namespace': 'str',
        'workload_name': 'str',
        'workload_type': 'str',
        'service': 'str',
        'service_name': 'str',
        'gcp_project_id': 'str',
        'gcp_product': 'str',
        'gcp_skuid': 'str',
        'gcp_sku_description': 'str',
        'aws_usage_account_id': 'str',
        'aws_service_code': 'str',
        'aws_instancetype': 'str',
        'aws_usage_type': 'str',
        'azure_subscription_guid': 'str',
        'azure_resource_group': 'str',
        'azure_meter_category': 'str',
        'azure_service_name': 'str',
        'azure_instance_id': 'str',
        'cloud_provider': 'str'
    }

    attribute_map = {
        'field': 'field',
        'cluster_name': 'clusterName',
        'cluster_id': 'clusterId',
        'namespace': 'namespace',
        'workload_name': 'workloadName',
        'workload_type': 'workloadType',
        'service': 'service',
        'service_name': 'serviceName',
        'gcp_project_id': 'gcpProjectId',
        'gcp_product': 'gcpProduct',
        'gcp_skuid': 'gcpSKUId',
        'gcp_sku_description': 'gcpSKUDescription',
        'aws_usage_account_id': 'awsUsageAccountId',
        'aws_service_code': 'awsServiceCode',
        'aws_instancetype': 'awsInstancetype',
        'aws_usage_type': 'awsUsageType',
        'azure_subscription_guid': 'azureSubscriptionGuid',
        'azure_resource_group': 'azureResourceGroup',
        'azure_meter_category': 'azureMeterCategory',
        'azure_service_name': 'azureServiceName',
        'azure_instance_id': 'azureInstanceId',
        'cloud_provider': 'cloudProvider'
    }

    def __init__(self, field=None, cluster_name=None, cluster_id=None, namespace=None, workload_name=None, workload_type=None, service=None, service_name=None, gcp_project_id=None, gcp_product=None, gcp_skuid=None, gcp_sku_description=None, aws_usage_account_id=None, aws_service_code=None, aws_instancetype=None, aws_usage_type=None, azure_subscription_guid=None, azure_resource_group=None, azure_meter_category=None, azure_service_name=None, azure_instance_id=None, cloud_provider=None):  # noqa: E501
        """EntityInfo - a model defined in Swagger"""  # noqa: E501
        self._field = None
        self._cluster_name = None
        self._cluster_id = None
        self._namespace = None
        self._workload_name = None
        self._workload_type = None
        self._service = None
        self._service_name = None
        self._gcp_project_id = None
        self._gcp_product = None
        self._gcp_skuid = None
        self._gcp_sku_description = None
        self._aws_usage_account_id = None
        self._aws_service_code = None
        self._aws_instancetype = None
        self._aws_usage_type = None
        self._azure_subscription_guid = None
        self._azure_resource_group = None
        self._azure_meter_category = None
        self._azure_service_name = None
        self._azure_instance_id = None
        self._cloud_provider = None
        self.discriminator = None
        if field is not None:
            self.field = field
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if namespace is not None:
            self.namespace = namespace
        if workload_name is not None:
            self.workload_name = workload_name
        if workload_type is not None:
            self.workload_type = workload_type
        if service is not None:
            self.service = service
        if service_name is not None:
            self.service_name = service_name
        if gcp_project_id is not None:
            self.gcp_project_id = gcp_project_id
        if gcp_product is not None:
            self.gcp_product = gcp_product
        if gcp_skuid is not None:
            self.gcp_skuid = gcp_skuid
        if gcp_sku_description is not None:
            self.gcp_sku_description = gcp_sku_description
        if aws_usage_account_id is not None:
            self.aws_usage_account_id = aws_usage_account_id
        if aws_service_code is not None:
            self.aws_service_code = aws_service_code
        if aws_instancetype is not None:
            self.aws_instancetype = aws_instancetype
        if aws_usage_type is not None:
            self.aws_usage_type = aws_usage_type
        if azure_subscription_guid is not None:
            self.azure_subscription_guid = azure_subscription_guid
        if azure_resource_group is not None:
            self.azure_resource_group = azure_resource_group
        if azure_meter_category is not None:
            self.azure_meter_category = azure_meter_category
        if azure_service_name is not None:
            self.azure_service_name = azure_service_name
        if azure_instance_id is not None:
            self.azure_instance_id = azure_instance_id
        if cloud_provider is not None:
            self.cloud_provider = cloud_provider

    @property
    def field(self):
        """Gets the field of this EntityInfo.  # noqa: E501


        :return: The field of this EntityInfo.  # noqa: E501
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this EntityInfo.


        :param field: The field of this EntityInfo.  # noqa: E501
        :type: str
        """

        self._field = field

    @property
    def cluster_name(self):
        """Gets the cluster_name of this EntityInfo.  # noqa: E501


        :return: The cluster_name of this EntityInfo.  # noqa: E501
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        """Sets the cluster_name of this EntityInfo.


        :param cluster_name: The cluster_name of this EntityInfo.  # noqa: E501
        :type: str
        """

        self._cluster_name = cluster_name

    @property
    def cluster_id(self):
        """Gets the cluster_id of this EntityInfo.  # noqa: E501


        :return: The cluster_id of this EntityInfo.  # noqa: E501
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this EntityInfo.


        :param cluster_id: The cluster_id of this EntityInfo.  # noqa: E501
        :type: str
        """

        self._cluster_id = cluster_id

    @property
    def namespace(self):
        """Gets the namespace of this EntityInfo.  # noqa: E501


        :return: The namespace of this EntityInfo.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this EntityInfo.


        :param namespace: The namespace of this EntityInfo.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

    @property
    def workload_name(self):
        """Gets the workload_name of this EntityInfo.  # noqa: E501


        :return: The workload_name of this EntityInfo.  # noqa: E501
        :rtype: str
        """
        return self._workload_name

    @workload_name.setter
    def workload_name(self, workload_name):
        """Sets the workload_name of this EntityInfo.


        :param workload_name: The workload_name of this EntityInfo.  # noqa: E501
        :type: str
        """

        self._workload_name = workload_name

    @property
    def workload_type(self):
        """Gets the workload_type of this EntityInfo.  # noqa: E501


        :return: The workload_type of this EntityInfo.  # noqa: E501
        :rtype: str
        """
        return self._workload_type

    @workload_type.setter
    def workload_type(self, workload_type):
        """Sets the workload_type of this EntityInfo.


        :param workload_type: The workload_type of this EntityInfo.  # noqa: E501
        :type: str
        """

        self._workload_type = workload_type

    @property
    def service(self):
        """Gets the service of this EntityInfo.  # noqa: E501


        :return: The service of this EntityInfo.  # noqa: E501
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this EntityInfo.


        :param service: The service of this EntityInfo.  # noqa: E501
        :type: str
        """

        self._service = service

    @property
    def service_name(self):
        """Gets the service_name of this EntityInfo.  # noqa: E501


        :return: The service_name of this EntityInfo.  # noqa: E501
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """Sets the service_name of this EntityInfo.


        :param service_name: The service_name of this EntityInfo.  # noqa: E501
        :type: str
        """

        self._service_name = service_name

    @property
    def gcp_project_id(self):
        """Gets the gcp_project_id of this EntityInfo.  # noqa: E501


        :return: The gcp_project_id of this EntityInfo.  # noqa: E501
        :rtype: str
        """
        return self._gcp_project_id

    @gcp_project_id.setter
    def gcp_project_id(self, gcp_project_id):
        """Sets the gcp_project_id of this EntityInfo.


        :param gcp_project_id: The gcp_project_id of this EntityInfo.  # noqa: E501
        :type: str
        """

        self._gcp_project_id = gcp_project_id

    @property
    def gcp_product(self):
        """Gets the gcp_product of this EntityInfo.  # noqa: E501


        :return: The gcp_product of this EntityInfo.  # noqa: E501
        :rtype: str
        """
        return self._gcp_product

    @gcp_product.setter
    def gcp_product(self, gcp_product):
        """Sets the gcp_product of this EntityInfo.


        :param gcp_product: The gcp_product of this EntityInfo.  # noqa: E501
        :type: str
        """

        self._gcp_product = gcp_product

    @property
    def gcp_skuid(self):
        """Gets the gcp_skuid of this EntityInfo.  # noqa: E501


        :return: The gcp_skuid of this EntityInfo.  # noqa: E501
        :rtype: str
        """
        return self._gcp_skuid

    @gcp_skuid.setter
    def gcp_skuid(self, gcp_skuid):
        """Sets the gcp_skuid of this EntityInfo.


        :param gcp_skuid: The gcp_skuid of this EntityInfo.  # noqa: E501
        :type: str
        """

        self._gcp_skuid = gcp_skuid

    @property
    def gcp_sku_description(self):
        """Gets the gcp_sku_description of this EntityInfo.  # noqa: E501


        :return: The gcp_sku_description of this EntityInfo.  # noqa: E501
        :rtype: str
        """
        return self._gcp_sku_description

    @gcp_sku_description.setter
    def gcp_sku_description(self, gcp_sku_description):
        """Sets the gcp_sku_description of this EntityInfo.


        :param gcp_sku_description: The gcp_sku_description of this EntityInfo.  # noqa: E501
        :type: str
        """

        self._gcp_sku_description = gcp_sku_description

    @property
    def aws_usage_account_id(self):
        """Gets the aws_usage_account_id of this EntityInfo.  # noqa: E501


        :return: The aws_usage_account_id of this EntityInfo.  # noqa: E501
        :rtype: str
        """
        return self._aws_usage_account_id

    @aws_usage_account_id.setter
    def aws_usage_account_id(self, aws_usage_account_id):
        """Sets the aws_usage_account_id of this EntityInfo.


        :param aws_usage_account_id: The aws_usage_account_id of this EntityInfo.  # noqa: E501
        :type: str
        """

        self._aws_usage_account_id = aws_usage_account_id

    @property
    def aws_service_code(self):
        """Gets the aws_service_code of this EntityInfo.  # noqa: E501


        :return: The aws_service_code of this EntityInfo.  # noqa: E501
        :rtype: str
        """
        return self._aws_service_code

    @aws_service_code.setter
    def aws_service_code(self, aws_service_code):
        """Sets the aws_service_code of this EntityInfo.


        :param aws_service_code: The aws_service_code of this EntityInfo.  # noqa: E501
        :type: str
        """

        self._aws_service_code = aws_service_code

    @property
    def aws_instancetype(self):
        """Gets the aws_instancetype of this EntityInfo.  # noqa: E501


        :return: The aws_instancetype of this EntityInfo.  # noqa: E501
        :rtype: str
        """
        return self._aws_instancetype

    @aws_instancetype.setter
    def aws_instancetype(self, aws_instancetype):
        """Sets the aws_instancetype of this EntityInfo.


        :param aws_instancetype: The aws_instancetype of this EntityInfo.  # noqa: E501
        :type: str
        """

        self._aws_instancetype = aws_instancetype

    @property
    def aws_usage_type(self):
        """Gets the aws_usage_type of this EntityInfo.  # noqa: E501


        :return: The aws_usage_type of this EntityInfo.  # noqa: E501
        :rtype: str
        """
        return self._aws_usage_type

    @aws_usage_type.setter
    def aws_usage_type(self, aws_usage_type):
        """Sets the aws_usage_type of this EntityInfo.


        :param aws_usage_type: The aws_usage_type of this EntityInfo.  # noqa: E501
        :type: str
        """

        self._aws_usage_type = aws_usage_type

    @property
    def azure_subscription_guid(self):
        """Gets the azure_subscription_guid of this EntityInfo.  # noqa: E501


        :return: The azure_subscription_guid of this EntityInfo.  # noqa: E501
        :rtype: str
        """
        return self._azure_subscription_guid

    @azure_subscription_guid.setter
    def azure_subscription_guid(self, azure_subscription_guid):
        """Sets the azure_subscription_guid of this EntityInfo.


        :param azure_subscription_guid: The azure_subscription_guid of this EntityInfo.  # noqa: E501
        :type: str
        """

        self._azure_subscription_guid = azure_subscription_guid

    @property
    def azure_resource_group(self):
        """Gets the azure_resource_group of this EntityInfo.  # noqa: E501


        :return: The azure_resource_group of this EntityInfo.  # noqa: E501
        :rtype: str
        """
        return self._azure_resource_group

    @azure_resource_group.setter
    def azure_resource_group(self, azure_resource_group):
        """Sets the azure_resource_group of this EntityInfo.


        :param azure_resource_group: The azure_resource_group of this EntityInfo.  # noqa: E501
        :type: str
        """

        self._azure_resource_group = azure_resource_group

    @property
    def azure_meter_category(self):
        """Gets the azure_meter_category of this EntityInfo.  # noqa: E501


        :return: The azure_meter_category of this EntityInfo.  # noqa: E501
        :rtype: str
        """
        return self._azure_meter_category

    @azure_meter_category.setter
    def azure_meter_category(self, azure_meter_category):
        """Sets the azure_meter_category of this EntityInfo.


        :param azure_meter_category: The azure_meter_category of this EntityInfo.  # noqa: E501
        :type: str
        """

        self._azure_meter_category = azure_meter_category

    @property
    def azure_service_name(self):
        """Gets the azure_service_name of this EntityInfo.  # noqa: E501


        :return: The azure_service_name of this EntityInfo.  # noqa: E501
        :rtype: str
        """
        return self._azure_service_name

    @azure_service_name.setter
    def azure_service_name(self, azure_service_name):
        """Sets the azure_service_name of this EntityInfo.


        :param azure_service_name: The azure_service_name of this EntityInfo.  # noqa: E501
        :type: str
        """

        self._azure_service_name = azure_service_name

    @property
    def azure_instance_id(self):
        """Gets the azure_instance_id of this EntityInfo.  # noqa: E501


        :return: The azure_instance_id of this EntityInfo.  # noqa: E501
        :rtype: str
        """
        return self._azure_instance_id

    @azure_instance_id.setter
    def azure_instance_id(self, azure_instance_id):
        """Sets the azure_instance_id of this EntityInfo.


        :param azure_instance_id: The azure_instance_id of this EntityInfo.  # noqa: E501
        :type: str
        """

        self._azure_instance_id = azure_instance_id

    @property
    def cloud_provider(self):
        """Gets the cloud_provider of this EntityInfo.  # noqa: E501


        :return: The cloud_provider of this EntityInfo.  # noqa: E501
        :rtype: str
        """
        return self._cloud_provider

    @cloud_provider.setter
    def cloud_provider(self, cloud_provider):
        """Sets the cloud_provider of this EntityInfo.


        :param cloud_provider: The cloud_provider of this EntityInfo.  # noqa: E501
        :type: str
        """

        self._cloud_provider = cloud_provider

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
        if issubclass(EntityInfo, dict):
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
        if not isinstance(other, EntityInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
