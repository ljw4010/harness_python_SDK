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

class V1ObjectMeta(object):
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
        'name': 'str',
        'generate_name': 'str',
        'namespace': 'str',
        'self_link': 'str',
        'uid': 'str',
        'resource_version': 'str',
        'generation': 'str',
        'creation_timestamp': 'V1Time',
        'deletion_timestamp': 'V1Time',
        'deletion_grace_period_seconds': 'str',
        'labels': 'dict(str, str)',
        'annotations': 'dict(str, str)',
        'owner_references': 'list[V1OwnerReference]',
        'finalizers': 'list[str]',
        'cluster_name': 'str',
        'managed_fields': 'list[V1ManagedFieldsEntry]'
    }

    attribute_map = {
        'name': 'name',
        'generate_name': 'generateName',
        'namespace': 'namespace',
        'self_link': 'selfLink',
        'uid': 'uid',
        'resource_version': 'resourceVersion',
        'generation': 'generation',
        'creation_timestamp': 'creationTimestamp',
        'deletion_timestamp': 'deletionTimestamp',
        'deletion_grace_period_seconds': 'deletionGracePeriodSeconds',
        'labels': 'labels',
        'annotations': 'annotations',
        'owner_references': 'ownerReferences',
        'finalizers': 'finalizers',
        'cluster_name': 'clusterName',
        'managed_fields': 'managedFields'
    }

    def __init__(self, name=None, generate_name=None, namespace=None, self_link=None, uid=None, resource_version=None, generation=None, creation_timestamp=None, deletion_timestamp=None, deletion_grace_period_seconds=None, labels=None, annotations=None, owner_references=None, finalizers=None, cluster_name=None, managed_fields=None):  # noqa: E501
        """V1ObjectMeta - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._generate_name = None
        self._namespace = None
        self._self_link = None
        self._uid = None
        self._resource_version = None
        self._generation = None
        self._creation_timestamp = None
        self._deletion_timestamp = None
        self._deletion_grace_period_seconds = None
        self._labels = None
        self._annotations = None
        self._owner_references = None
        self._finalizers = None
        self._cluster_name = None
        self._managed_fields = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if generate_name is not None:
            self.generate_name = generate_name
        if namespace is not None:
            self.namespace = namespace
        if self_link is not None:
            self.self_link = self_link
        if uid is not None:
            self.uid = uid
        if resource_version is not None:
            self.resource_version = resource_version
        if generation is not None:
            self.generation = generation
        if creation_timestamp is not None:
            self.creation_timestamp = creation_timestamp
        if deletion_timestamp is not None:
            self.deletion_timestamp = deletion_timestamp
        if deletion_grace_period_seconds is not None:
            self.deletion_grace_period_seconds = deletion_grace_period_seconds
        if labels is not None:
            self.labels = labels
        if annotations is not None:
            self.annotations = annotations
        if owner_references is not None:
            self.owner_references = owner_references
        if finalizers is not None:
            self.finalizers = finalizers
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if managed_fields is not None:
            self.managed_fields = managed_fields

    @property
    def name(self):
        """Gets the name of this V1ObjectMeta.  # noqa: E501


        :return: The name of this V1ObjectMeta.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1ObjectMeta.


        :param name: The name of this V1ObjectMeta.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def generate_name(self):
        """Gets the generate_name of this V1ObjectMeta.  # noqa: E501

        GenerateName is an optional prefix, used by the server, to generate a unique name ONLY IF the Name field has not been provided. If this field is used, the name returned to the client will be different than the name passed. This value will also be combined with a unique suffix. The provided value has the same validation rules as the Name field, and may be truncated by the length of the suffix required to make the value unique on the server.  If this field is specified and the generated name exists, the server will NOT return a 409 - instead, it will either return 201 Created or 500 with Reason ServerTimeout indicating a unique name could not be found in the time allotted, and the client should retry (optionally after the time indicated in the Retry-After header).  Applied only if Name is not specified. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#idempotency +optional  # noqa: E501

        :return: The generate_name of this V1ObjectMeta.  # noqa: E501
        :rtype: str
        """
        return self._generate_name

    @generate_name.setter
    def generate_name(self, generate_name):
        """Sets the generate_name of this V1ObjectMeta.

        GenerateName is an optional prefix, used by the server, to generate a unique name ONLY IF the Name field has not been provided. If this field is used, the name returned to the client will be different than the name passed. This value will also be combined with a unique suffix. The provided value has the same validation rules as the Name field, and may be truncated by the length of the suffix required to make the value unique on the server.  If this field is specified and the generated name exists, the server will NOT return a 409 - instead, it will either return 201 Created or 500 with Reason ServerTimeout indicating a unique name could not be found in the time allotted, and the client should retry (optionally after the time indicated in the Retry-After header).  Applied only if Name is not specified. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#idempotency +optional  # noqa: E501

        :param generate_name: The generate_name of this V1ObjectMeta.  # noqa: E501
        :type: str
        """

        self._generate_name = generate_name

    @property
    def namespace(self):
        """Gets the namespace of this V1ObjectMeta.  # noqa: E501

        Namespace defines the space within which each name must be unique. An empty namespace is equivalent to the \"default\" namespace, but \"default\" is the canonical representation. Not all objects are required to be scoped to a namespace - the value of this field for those objects will be empty.  Must be a DNS_LABEL. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/namespaces +optional  # noqa: E501

        :return: The namespace of this V1ObjectMeta.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this V1ObjectMeta.

        Namespace defines the space within which each name must be unique. An empty namespace is equivalent to the \"default\" namespace, but \"default\" is the canonical representation. Not all objects are required to be scoped to a namespace - the value of this field for those objects will be empty.  Must be a DNS_LABEL. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/namespaces +optional  # noqa: E501

        :param namespace: The namespace of this V1ObjectMeta.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

    @property
    def self_link(self):
        """Gets the self_link of this V1ObjectMeta.  # noqa: E501

        SelfLink is a URL representing this object. Populated by the system. Read-only.  DEPRECATED Kubernetes will stop propagating this field in 1.20 release and the field is planned to be removed in 1.21 release. +optional  # noqa: E501

        :return: The self_link of this V1ObjectMeta.  # noqa: E501
        :rtype: str
        """
        return self._self_link

    @self_link.setter
    def self_link(self, self_link):
        """Sets the self_link of this V1ObjectMeta.

        SelfLink is a URL representing this object. Populated by the system. Read-only.  DEPRECATED Kubernetes will stop propagating this field in 1.20 release and the field is planned to be removed in 1.21 release. +optional  # noqa: E501

        :param self_link: The self_link of this V1ObjectMeta.  # noqa: E501
        :type: str
        """

        self._self_link = self_link

    @property
    def uid(self):
        """Gets the uid of this V1ObjectMeta.  # noqa: E501

        UID is the unique in time and space value for this object. It is typically generated by the server on successful creation of a resource and is not allowed to change on PUT operations.  Populated by the system. Read-only. More info: http://kubernetes.io/docs/user-guide/identifiers#uids +optional  # noqa: E501

        :return: The uid of this V1ObjectMeta.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this V1ObjectMeta.

        UID is the unique in time and space value for this object. It is typically generated by the server on successful creation of a resource and is not allowed to change on PUT operations.  Populated by the system. Read-only. More info: http://kubernetes.io/docs/user-guide/identifiers#uids +optional  # noqa: E501

        :param uid: The uid of this V1ObjectMeta.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def resource_version(self):
        """Gets the resource_version of this V1ObjectMeta.  # noqa: E501

        An opaque value that represents the internal version of this object that can be used by clients to determine when objects have changed. May be used for optimistic concurrency, change detection, and the watch operation on a resource or set of resources. Clients must treat these values as opaque and passed unmodified back to the server. They may only be valid for a particular resource or set of resources.  Populated by the system. Read-only. Value must be treated as opaque by clients and . More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency +optional  # noqa: E501

        :return: The resource_version of this V1ObjectMeta.  # noqa: E501
        :rtype: str
        """
        return self._resource_version

    @resource_version.setter
    def resource_version(self, resource_version):
        """Sets the resource_version of this V1ObjectMeta.

        An opaque value that represents the internal version of this object that can be used by clients to determine when objects have changed. May be used for optimistic concurrency, change detection, and the watch operation on a resource or set of resources. Clients must treat these values as opaque and passed unmodified back to the server. They may only be valid for a particular resource or set of resources.  Populated by the system. Read-only. Value must be treated as opaque by clients and . More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency +optional  # noqa: E501

        :param resource_version: The resource_version of this V1ObjectMeta.  # noqa: E501
        :type: str
        """

        self._resource_version = resource_version

    @property
    def generation(self):
        """Gets the generation of this V1ObjectMeta.  # noqa: E501


        :return: The generation of this V1ObjectMeta.  # noqa: E501
        :rtype: str
        """
        return self._generation

    @generation.setter
    def generation(self, generation):
        """Sets the generation of this V1ObjectMeta.


        :param generation: The generation of this V1ObjectMeta.  # noqa: E501
        :type: str
        """

        self._generation = generation

    @property
    def creation_timestamp(self):
        """Gets the creation_timestamp of this V1ObjectMeta.  # noqa: E501


        :return: The creation_timestamp of this V1ObjectMeta.  # noqa: E501
        :rtype: V1Time
        """
        return self._creation_timestamp

    @creation_timestamp.setter
    def creation_timestamp(self, creation_timestamp):
        """Sets the creation_timestamp of this V1ObjectMeta.


        :param creation_timestamp: The creation_timestamp of this V1ObjectMeta.  # noqa: E501
        :type: V1Time
        """

        self._creation_timestamp = creation_timestamp

    @property
    def deletion_timestamp(self):
        """Gets the deletion_timestamp of this V1ObjectMeta.  # noqa: E501


        :return: The deletion_timestamp of this V1ObjectMeta.  # noqa: E501
        :rtype: V1Time
        """
        return self._deletion_timestamp

    @deletion_timestamp.setter
    def deletion_timestamp(self, deletion_timestamp):
        """Sets the deletion_timestamp of this V1ObjectMeta.


        :param deletion_timestamp: The deletion_timestamp of this V1ObjectMeta.  # noqa: E501
        :type: V1Time
        """

        self._deletion_timestamp = deletion_timestamp

    @property
    def deletion_grace_period_seconds(self):
        """Gets the deletion_grace_period_seconds of this V1ObjectMeta.  # noqa: E501


        :return: The deletion_grace_period_seconds of this V1ObjectMeta.  # noqa: E501
        :rtype: str
        """
        return self._deletion_grace_period_seconds

    @deletion_grace_period_seconds.setter
    def deletion_grace_period_seconds(self, deletion_grace_period_seconds):
        """Sets the deletion_grace_period_seconds of this V1ObjectMeta.


        :param deletion_grace_period_seconds: The deletion_grace_period_seconds of this V1ObjectMeta.  # noqa: E501
        :type: str
        """

        self._deletion_grace_period_seconds = deletion_grace_period_seconds

    @property
    def labels(self):
        """Gets the labels of this V1ObjectMeta.  # noqa: E501


        :return: The labels of this V1ObjectMeta.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this V1ObjectMeta.


        :param labels: The labels of this V1ObjectMeta.  # noqa: E501
        :type: dict(str, str)
        """

        self._labels = labels

    @property
    def annotations(self):
        """Gets the annotations of this V1ObjectMeta.  # noqa: E501


        :return: The annotations of this V1ObjectMeta.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this V1ObjectMeta.


        :param annotations: The annotations of this V1ObjectMeta.  # noqa: E501
        :type: dict(str, str)
        """

        self._annotations = annotations

    @property
    def owner_references(self):
        """Gets the owner_references of this V1ObjectMeta.  # noqa: E501


        :return: The owner_references of this V1ObjectMeta.  # noqa: E501
        :rtype: list[V1OwnerReference]
        """
        return self._owner_references

    @owner_references.setter
    def owner_references(self, owner_references):
        """Sets the owner_references of this V1ObjectMeta.


        :param owner_references: The owner_references of this V1ObjectMeta.  # noqa: E501
        :type: list[V1OwnerReference]
        """

        self._owner_references = owner_references

    @property
    def finalizers(self):
        """Gets the finalizers of this V1ObjectMeta.  # noqa: E501


        :return: The finalizers of this V1ObjectMeta.  # noqa: E501
        :rtype: list[str]
        """
        return self._finalizers

    @finalizers.setter
    def finalizers(self, finalizers):
        """Sets the finalizers of this V1ObjectMeta.


        :param finalizers: The finalizers of this V1ObjectMeta.  # noqa: E501
        :type: list[str]
        """

        self._finalizers = finalizers

    @property
    def cluster_name(self):
        """Gets the cluster_name of this V1ObjectMeta.  # noqa: E501


        :return: The cluster_name of this V1ObjectMeta.  # noqa: E501
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        """Sets the cluster_name of this V1ObjectMeta.


        :param cluster_name: The cluster_name of this V1ObjectMeta.  # noqa: E501
        :type: str
        """

        self._cluster_name = cluster_name

    @property
    def managed_fields(self):
        """Gets the managed_fields of this V1ObjectMeta.  # noqa: E501

        ManagedFields maps workflow-id and version to the set of fields that are managed by that workflow. This is mostly for internal housekeeping, and users typically shouldn't need to set or understand this field. A workflow can be the user's name, a controller's name, or the name of a specific apply path like \"ci-cd\". The set of fields is always in the version that the workflow used when modifying the object.  +optional  # noqa: E501

        :return: The managed_fields of this V1ObjectMeta.  # noqa: E501
        :rtype: list[V1ManagedFieldsEntry]
        """
        return self._managed_fields

    @managed_fields.setter
    def managed_fields(self, managed_fields):
        """Sets the managed_fields of this V1ObjectMeta.

        ManagedFields maps workflow-id and version to the set of fields that are managed by that workflow. This is mostly for internal housekeeping, and users typically shouldn't need to set or understand this field. A workflow can be the user's name, a controller's name, or the name of a specific apply path like \"ci-cd\". The set of fields is always in the version that the workflow used when modifying the object.  +optional  # noqa: E501

        :param managed_fields: The managed_fields of this V1ObjectMeta.  # noqa: E501
        :type: list[V1ManagedFieldsEntry]
        """

        self._managed_fields = managed_fields

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
        if issubclass(V1ObjectMeta, dict):
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
        if not isinstance(other, V1ObjectMeta):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
