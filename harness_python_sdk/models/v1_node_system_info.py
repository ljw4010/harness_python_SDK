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

class V1NodeSystemInfo(object):
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
        'machine_id': 'str',
        'system_uuid': 'str',
        'boot_id': 'str',
        'kernel_version': 'str',
        'os_image': 'str',
        'container_runtime_version': 'str',
        'kubelet_version': 'str',
        'kube_proxy_version': 'str',
        'operating_system': 'str',
        'architecture': 'str'
    }

    attribute_map = {
        'machine_id': 'machineID',
        'system_uuid': 'systemUUID',
        'boot_id': 'bootID',
        'kernel_version': 'kernelVersion',
        'os_image': 'osImage',
        'container_runtime_version': 'containerRuntimeVersion',
        'kubelet_version': 'kubeletVersion',
        'kube_proxy_version': 'kubeProxyVersion',
        'operating_system': 'operatingSystem',
        'architecture': 'architecture'
    }

    def __init__(self, machine_id=None, system_uuid=None, boot_id=None, kernel_version=None, os_image=None, container_runtime_version=None, kubelet_version=None, kube_proxy_version=None, operating_system=None, architecture=None):  # noqa: E501
        """V1NodeSystemInfo - a model defined in Swagger"""  # noqa: E501
        self._machine_id = None
        self._system_uuid = None
        self._boot_id = None
        self._kernel_version = None
        self._os_image = None
        self._container_runtime_version = None
        self._kubelet_version = None
        self._kube_proxy_version = None
        self._operating_system = None
        self._architecture = None
        self.discriminator = None
        if machine_id is not None:
            self.machine_id = machine_id
        if system_uuid is not None:
            self.system_uuid = system_uuid
        if boot_id is not None:
            self.boot_id = boot_id
        if kernel_version is not None:
            self.kernel_version = kernel_version
        if os_image is not None:
            self.os_image = os_image
        if container_runtime_version is not None:
            self.container_runtime_version = container_runtime_version
        if kubelet_version is not None:
            self.kubelet_version = kubelet_version
        if kube_proxy_version is not None:
            self.kube_proxy_version = kube_proxy_version
        if operating_system is not None:
            self.operating_system = operating_system
        if architecture is not None:
            self.architecture = architecture

    @property
    def machine_id(self):
        """Gets the machine_id of this V1NodeSystemInfo.  # noqa: E501


        :return: The machine_id of this V1NodeSystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._machine_id

    @machine_id.setter
    def machine_id(self, machine_id):
        """Sets the machine_id of this V1NodeSystemInfo.


        :param machine_id: The machine_id of this V1NodeSystemInfo.  # noqa: E501
        :type: str
        """

        self._machine_id = machine_id

    @property
    def system_uuid(self):
        """Gets the system_uuid of this V1NodeSystemInfo.  # noqa: E501


        :return: The system_uuid of this V1NodeSystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._system_uuid

    @system_uuid.setter
    def system_uuid(self, system_uuid):
        """Sets the system_uuid of this V1NodeSystemInfo.


        :param system_uuid: The system_uuid of this V1NodeSystemInfo.  # noqa: E501
        :type: str
        """

        self._system_uuid = system_uuid

    @property
    def boot_id(self):
        """Gets the boot_id of this V1NodeSystemInfo.  # noqa: E501

        Boot ID reported by the node.  # noqa: E501

        :return: The boot_id of this V1NodeSystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._boot_id

    @boot_id.setter
    def boot_id(self, boot_id):
        """Sets the boot_id of this V1NodeSystemInfo.

        Boot ID reported by the node.  # noqa: E501

        :param boot_id: The boot_id of this V1NodeSystemInfo.  # noqa: E501
        :type: str
        """

        self._boot_id = boot_id

    @property
    def kernel_version(self):
        """Gets the kernel_version of this V1NodeSystemInfo.  # noqa: E501

        Kernel Version reported by the node from 'uname -r' (e.g. 3.16.0-0.bpo.4-amd64).  # noqa: E501

        :return: The kernel_version of this V1NodeSystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._kernel_version

    @kernel_version.setter
    def kernel_version(self, kernel_version):
        """Sets the kernel_version of this V1NodeSystemInfo.

        Kernel Version reported by the node from 'uname -r' (e.g. 3.16.0-0.bpo.4-amd64).  # noqa: E501

        :param kernel_version: The kernel_version of this V1NodeSystemInfo.  # noqa: E501
        :type: str
        """

        self._kernel_version = kernel_version

    @property
    def os_image(self):
        """Gets the os_image of this V1NodeSystemInfo.  # noqa: E501

        OS Image reported by the node from /etc/os-release (e.g. Debian GNU/Linux 7 (wheezy)).  # noqa: E501

        :return: The os_image of this V1NodeSystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._os_image

    @os_image.setter
    def os_image(self, os_image):
        """Sets the os_image of this V1NodeSystemInfo.

        OS Image reported by the node from /etc/os-release (e.g. Debian GNU/Linux 7 (wheezy)).  # noqa: E501

        :param os_image: The os_image of this V1NodeSystemInfo.  # noqa: E501
        :type: str
        """

        self._os_image = os_image

    @property
    def container_runtime_version(self):
        """Gets the container_runtime_version of this V1NodeSystemInfo.  # noqa: E501

        ContainerRuntime Version reported by the node through runtime remote API (e.g. docker://1.5.0).  # noqa: E501

        :return: The container_runtime_version of this V1NodeSystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._container_runtime_version

    @container_runtime_version.setter
    def container_runtime_version(self, container_runtime_version):
        """Sets the container_runtime_version of this V1NodeSystemInfo.

        ContainerRuntime Version reported by the node through runtime remote API (e.g. docker://1.5.0).  # noqa: E501

        :param container_runtime_version: The container_runtime_version of this V1NodeSystemInfo.  # noqa: E501
        :type: str
        """

        self._container_runtime_version = container_runtime_version

    @property
    def kubelet_version(self):
        """Gets the kubelet_version of this V1NodeSystemInfo.  # noqa: E501

        Kubelet Version reported by the node.  # noqa: E501

        :return: The kubelet_version of this V1NodeSystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._kubelet_version

    @kubelet_version.setter
    def kubelet_version(self, kubelet_version):
        """Sets the kubelet_version of this V1NodeSystemInfo.

        Kubelet Version reported by the node.  # noqa: E501

        :param kubelet_version: The kubelet_version of this V1NodeSystemInfo.  # noqa: E501
        :type: str
        """

        self._kubelet_version = kubelet_version

    @property
    def kube_proxy_version(self):
        """Gets the kube_proxy_version of this V1NodeSystemInfo.  # noqa: E501

        KubeProxy Version reported by the node.  # noqa: E501

        :return: The kube_proxy_version of this V1NodeSystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._kube_proxy_version

    @kube_proxy_version.setter
    def kube_proxy_version(self, kube_proxy_version):
        """Sets the kube_proxy_version of this V1NodeSystemInfo.

        KubeProxy Version reported by the node.  # noqa: E501

        :param kube_proxy_version: The kube_proxy_version of this V1NodeSystemInfo.  # noqa: E501
        :type: str
        """

        self._kube_proxy_version = kube_proxy_version

    @property
    def operating_system(self):
        """Gets the operating_system of this V1NodeSystemInfo.  # noqa: E501


        :return: The operating_system of this V1NodeSystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._operating_system

    @operating_system.setter
    def operating_system(self, operating_system):
        """Sets the operating_system of this V1NodeSystemInfo.


        :param operating_system: The operating_system of this V1NodeSystemInfo.  # noqa: E501
        :type: str
        """

        self._operating_system = operating_system

    @property
    def architecture(self):
        """Gets the architecture of this V1NodeSystemInfo.  # noqa: E501


        :return: The architecture of this V1NodeSystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._architecture

    @architecture.setter
    def architecture(self, architecture):
        """Sets the architecture of this V1NodeSystemInfo.


        :param architecture: The architecture of this V1NodeSystemInfo.  # noqa: E501
        :type: str
        """

        self._architecture = architecture

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
        if issubclass(V1NodeSystemInfo, dict):
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
        if not isinstance(other, V1NodeSystemInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
