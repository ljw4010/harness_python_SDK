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

class Feature(object):
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
        'archived': 'bool',
        'created_at': 'int',
        'default_off_variation': 'str',
        'default_on_variation': 'str',
        'description': 'str',
        'env_properties': 'FeatureEnvProperties',
        'evaluation': 'str',
        'evaluation_identifier': 'str',
        'identifier': 'str',
        'kind': 'str',
        'modified_at': 'int',
        'name': 'str',
        'owner': 'list[str]',
        'permanent': 'bool',
        'prerequisites': 'list[Prerequisite]',
        'project': 'str',
        'results': 'list[Results]',
        'services': 'list[CfService]',
        'stale': 'bool',
        'stale_reason': 'str',
        'status': 'FeatureStatus',
        'tags': 'list[Tag]',
        'variations': 'list[Variation]'
    }

    attribute_map = {
        'archived': 'archived',
        'created_at': 'createdAt',
        'default_off_variation': 'defaultOffVariation',
        'default_on_variation': 'defaultOnVariation',
        'description': 'description',
        'env_properties': 'envProperties',
        'evaluation': 'evaluation',
        'evaluation_identifier': 'evaluationIdentifier',
        'identifier': 'identifier',
        'kind': 'kind',
        'modified_at': 'modifiedAt',
        'name': 'name',
        'owner': 'owner',
        'permanent': 'permanent',
        'prerequisites': 'prerequisites',
        'project': 'project',
        'results': 'results',
        'services': 'services',
        'stale': 'stale',
        'stale_reason': 'staleReason',
        'status': 'status',
        'tags': 'tags',
        'variations': 'variations'
    }

    def __init__(self, archived=None, created_at=None, default_off_variation=None, default_on_variation=None, description=None, env_properties=None, evaluation=None, evaluation_identifier=None, identifier=None, kind=None, modified_at=None, name=None, owner=None, permanent=None, prerequisites=None, project=None, results=None, services=None, stale=None, stale_reason=None, status=None, tags=None, variations=None):  # noqa: E501
        """Feature - a model defined in Swagger"""  # noqa: E501
        self._archived = None
        self._created_at = None
        self._default_off_variation = None
        self._default_on_variation = None
        self._description = None
        self._env_properties = None
        self._evaluation = None
        self._evaluation_identifier = None
        self._identifier = None
        self._kind = None
        self._modified_at = None
        self._name = None
        self._owner = None
        self._permanent = None
        self._prerequisites = None
        self._project = None
        self._results = None
        self._services = None
        self._stale = None
        self._stale_reason = None
        self._status = None
        self._tags = None
        self._variations = None
        self.discriminator = None
        if archived is not None:
            self.archived = archived
        self.created_at = created_at
        self.default_off_variation = default_off_variation
        self.default_on_variation = default_on_variation
        if description is not None:
            self.description = description
        if env_properties is not None:
            self.env_properties = env_properties
        if evaluation is not None:
            self.evaluation = evaluation
        if evaluation_identifier is not None:
            self.evaluation_identifier = evaluation_identifier
        self.identifier = identifier
        self.kind = kind
        if modified_at is not None:
            self.modified_at = modified_at
        self.name = name
        if owner is not None:
            self.owner = owner
        if permanent is not None:
            self.permanent = permanent
        if prerequisites is not None:
            self.prerequisites = prerequisites
        self.project = project
        if results is not None:
            self.results = results
        if services is not None:
            self.services = services
        if stale is not None:
            self.stale = stale
        if stale_reason is not None:
            self.stale_reason = stale_reason
        if status is not None:
            self.status = status
        if tags is not None:
            self.tags = tags
        self.variations = variations

    @property
    def archived(self):
        """Gets the archived of this Feature.  # noqa: E501

        Indicates if the flag has been archived and is no longer used  # noqa: E501

        :return: The archived of this Feature.  # noqa: E501
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        """Sets the archived of this Feature.

        Indicates if the flag has been archived and is no longer used  # noqa: E501

        :param archived: The archived of this Feature.  # noqa: E501
        :type: bool
        """

        self._archived = archived

    @property
    def created_at(self):
        """Gets the created_at of this Feature.  # noqa: E501

        The date the flag was created in milliseconds  # noqa: E501

        :return: The created_at of this Feature.  # noqa: E501
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Feature.

        The date the flag was created in milliseconds  # noqa: E501

        :param created_at: The created_at of this Feature.  # noqa: E501
        :type: int
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def default_off_variation(self):
        """Gets the default_off_variation of this Feature.  # noqa: E501

        The default value returned when a flag is off  # noqa: E501

        :return: The default_off_variation of this Feature.  # noqa: E501
        :rtype: str
        """
        return self._default_off_variation

    @default_off_variation.setter
    def default_off_variation(self, default_off_variation):
        """Sets the default_off_variation of this Feature.

        The default value returned when a flag is off  # noqa: E501

        :param default_off_variation: The default_off_variation of this Feature.  # noqa: E501
        :type: str
        """
        if default_off_variation is None:
            raise ValueError("Invalid value for `default_off_variation`, must not be `None`")  # noqa: E501

        self._default_off_variation = default_off_variation

    @property
    def default_on_variation(self):
        """Gets the default_on_variation of this Feature.  # noqa: E501

        The default value returned when a flag is on  # noqa: E501

        :return: The default_on_variation of this Feature.  # noqa: E501
        :rtype: str
        """
        return self._default_on_variation

    @default_on_variation.setter
    def default_on_variation(self, default_on_variation):
        """Sets the default_on_variation of this Feature.

        The default value returned when a flag is on  # noqa: E501

        :param default_on_variation: The default_on_variation of this Feature.  # noqa: E501
        :type: str
        """
        if default_on_variation is None:
            raise ValueError("Invalid value for `default_on_variation`, must not be `None`")  # noqa: E501

        self._default_on_variation = default_on_variation

    @property
    def description(self):
        """Gets the description of this Feature.  # noqa: E501

        A description for this flag  # noqa: E501

        :return: The description of this Feature.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Feature.

        A description for this flag  # noqa: E501

        :param description: The description of this Feature.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def env_properties(self):
        """Gets the env_properties of this Feature.  # noqa: E501


        :return: The env_properties of this Feature.  # noqa: E501
        :rtype: FeatureEnvProperties
        """
        return self._env_properties

    @env_properties.setter
    def env_properties(self, env_properties):
        """Sets the env_properties of this Feature.


        :param env_properties: The env_properties of this Feature.  # noqa: E501
        :type: FeatureEnvProperties
        """

        self._env_properties = env_properties

    @property
    def evaluation(self):
        """Gets the evaluation of this Feature.  # noqa: E501

        The value that the flag will return for the current user  # noqa: E501

        :return: The evaluation of this Feature.  # noqa: E501
        :rtype: str
        """
        return self._evaluation

    @evaluation.setter
    def evaluation(self, evaluation):
        """Sets the evaluation of this Feature.

        The value that the flag will return for the current user  # noqa: E501

        :param evaluation: The evaluation of this Feature.  # noqa: E501
        :type: str
        """

        self._evaluation = evaluation

    @property
    def evaluation_identifier(self):
        """Gets the evaluation_identifier of this Feature.  # noqa: E501

        The identifier for the returned evaluation  # noqa: E501

        :return: The evaluation_identifier of this Feature.  # noqa: E501
        :rtype: str
        """
        return self._evaluation_identifier

    @evaluation_identifier.setter
    def evaluation_identifier(self, evaluation_identifier):
        """Sets the evaluation_identifier of this Feature.

        The identifier for the returned evaluation  # noqa: E501

        :param evaluation_identifier: The evaluation_identifier of this Feature.  # noqa: E501
        :type: str
        """

        self._evaluation_identifier = evaluation_identifier

    @property
    def identifier(self):
        """Gets the identifier of this Feature.  # noqa: E501

        The Feature Flag identifier  # noqa: E501

        :return: The identifier of this Feature.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this Feature.

        The Feature Flag identifier  # noqa: E501

        :param identifier: The identifier of this Feature.  # noqa: E501
        :type: str
        """
        if identifier is None:
            raise ValueError("Invalid value for `identifier`, must not be `None`")  # noqa: E501

        self._identifier = identifier

    @property
    def kind(self):
        """Gets the kind of this Feature.  # noqa: E501

        The type of Feature flag  # noqa: E501

        :return: The kind of this Feature.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this Feature.

        The type of Feature flag  # noqa: E501

        :param kind: The kind of this Feature.  # noqa: E501
        :type: str
        """
        if kind is None:
            raise ValueError("Invalid value for `kind`, must not be `None`")  # noqa: E501
        allowed_values = ["boolean", "int", "string", "json"]  # noqa: E501
        if kind not in allowed_values:
            raise ValueError(
                "Invalid value for `kind` ({0}), must be one of {1}"  # noqa: E501
                .format(kind, allowed_values)
            )

        self._kind = kind

    @property
    def modified_at(self):
        """Gets the modified_at of this Feature.  # noqa: E501

        The date the flag was last modified in milliseconds  # noqa: E501

        :return: The modified_at of this Feature.  # noqa: E501
        :rtype: int
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """Sets the modified_at of this Feature.

        The date the flag was last modified in milliseconds  # noqa: E501

        :param modified_at: The modified_at of this Feature.  # noqa: E501
        :type: int
        """

        self._modified_at = modified_at

    @property
    def name(self):
        """Gets the name of this Feature.  # noqa: E501

        The name of the Feature Flag  # noqa: E501

        :return: The name of this Feature.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Feature.

        The name of the Feature Flag  # noqa: E501

        :param name: The name of this Feature.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def owner(self):
        """Gets the owner of this Feature.  # noqa: E501

        The user who created the flag  # noqa: E501

        :return: The owner of this Feature.  # noqa: E501
        :rtype: list[str]
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this Feature.

        The user who created the flag  # noqa: E501

        :param owner: The owner of this Feature.  # noqa: E501
        :type: list[str]
        """

        self._owner = owner

    @property
    def permanent(self):
        """Gets the permanent of this Feature.  # noqa: E501

        Indicates if this is a permanent flag, or one that should expire  # noqa: E501

        :return: The permanent of this Feature.  # noqa: E501
        :rtype: bool
        """
        return self._permanent

    @permanent.setter
    def permanent(self, permanent):
        """Sets the permanent of this Feature.

        Indicates if this is a permanent flag, or one that should expire  # noqa: E501

        :param permanent: The permanent of this Feature.  # noqa: E501
        :type: bool
        """

        self._permanent = permanent

    @property
    def prerequisites(self):
        """Gets the prerequisites of this Feature.  # noqa: E501


        :return: The prerequisites of this Feature.  # noqa: E501
        :rtype: list[Prerequisite]
        """
        return self._prerequisites

    @prerequisites.setter
    def prerequisites(self, prerequisites):
        """Sets the prerequisites of this Feature.


        :param prerequisites: The prerequisites of this Feature.  # noqa: E501
        :type: list[Prerequisite]
        """

        self._prerequisites = prerequisites

    @property
    def project(self):
        """Gets the project of this Feature.  # noqa: E501

        The project this Feature belongs to  # noqa: E501

        :return: The project of this Feature.  # noqa: E501
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this Feature.

        The project this Feature belongs to  # noqa: E501

        :param project: The project of this Feature.  # noqa: E501
        :type: str
        """
        if project is None:
            raise ValueError("Invalid value for `project`, must not be `None`")  # noqa: E501

        self._project = project

    @property
    def results(self):
        """Gets the results of this Feature.  # noqa: E501

        The results shows which variations have been evaluated, and how many times each of these have been evaluated.  # noqa: E501

        :return: The results of this Feature.  # noqa: E501
        :rtype: list[Results]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this Feature.

        The results shows which variations have been evaluated, and how many times each of these have been evaluated.  # noqa: E501

        :param results: The results of this Feature.  # noqa: E501
        :type: list[Results]
        """

        self._results = results

    @property
    def services(self):
        """Gets the services of this Feature.  # noqa: E501

        A list of services linked to this Feature Flag  # noqa: E501

        :return: The services of this Feature.  # noqa: E501
        :rtype: list[CfService]
        """
        return self._services

    @services.setter
    def services(self, services):
        """Sets the services of this Feature.

        A list of services linked to this Feature Flag  # noqa: E501

        :param services: The services of this Feature.  # noqa: E501
        :type: list[CfService]
        """

        self._services = services

    @property
    def stale(self):
        """Gets the stale of this Feature.  # noqa: E501

        Whether the flag is stale or not  # noqa: E501

        :return: The stale of this Feature.  # noqa: E501
        :rtype: bool
        """
        return self._stale

    @stale.setter
    def stale(self, stale):
        """Sets the stale of this Feature.

        Whether the flag is stale or not  # noqa: E501

        :param stale: The stale of this Feature.  # noqa: E501
        :type: bool
        """

        self._stale = stale

    @property
    def stale_reason(self):
        """Gets the stale_reason of this Feature.  # noqa: E501

        The reason that the flag was marked as stale  # noqa: E501

        :return: The stale_reason of this Feature.  # noqa: E501
        :rtype: str
        """
        return self._stale_reason

    @stale_reason.setter
    def stale_reason(self, stale_reason):
        """Sets the stale_reason of this Feature.

        The reason that the flag was marked as stale  # noqa: E501

        :param stale_reason: The stale_reason of this Feature.  # noqa: E501
        :type: str
        """

        self._stale_reason = stale_reason

    @property
    def status(self):
        """Gets the status of this Feature.  # noqa: E501


        :return: The status of this Feature.  # noqa: E501
        :rtype: FeatureStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Feature.


        :param status: The status of this Feature.  # noqa: E501
        :type: FeatureStatus
        """

        self._status = status

    @property
    def tags(self):
        """Gets the tags of this Feature.  # noqa: E501

        A list of tags for this Feature Flag  # noqa: E501

        :return: The tags of this Feature.  # noqa: E501
        :rtype: list[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Feature.

        A list of tags for this Feature Flag  # noqa: E501

        :param tags: The tags of this Feature.  # noqa: E501
        :type: list[Tag]
        """

        self._tags = tags

    @property
    def variations(self):
        """Gets the variations of this Feature.  # noqa: E501

        The variations that can be returned for this flag  # noqa: E501

        :return: The variations of this Feature.  # noqa: E501
        :rtype: list[Variation]
        """
        return self._variations

    @variations.setter
    def variations(self, variations):
        """Sets the variations of this Feature.

        The variations that can be returned for this flag  # noqa: E501

        :param variations: The variations of this Feature.  # noqa: E501
        :type: list[Variation]
        """
        if variations is None:
            raise ValueError("Invalid value for `variations`, must not be `None`")  # noqa: E501

        self._variations = variations

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
        if issubclass(Feature, dict):
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
        if not isinstance(other, Feature):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
