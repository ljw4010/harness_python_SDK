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

class InputSetSummaryResponse(object):
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
        'identifier': 'str',
        'name': 'str',
        'pipeline_identifier': 'str',
        'description': 'str',
        'input_set_type': 'str',
        'tags': 'dict(str, str)',
        'git_details': 'PipelineEntityGitDetails',
        'created_at': 'int',
        'last_updated_at': 'int',
        'is_outdated': 'bool',
        'input_set_error_details': 'InputSetErrorWrapper',
        'overlay_set_error_details': 'dict(str, str)',
        'entity_validity_details': 'PipelineEntityGitDetails',
        'modules': 'list[str]'
    }

    attribute_map = {
        'identifier': 'identifier',
        'name': 'name',
        'pipeline_identifier': 'pipelineIdentifier',
        'description': 'description',
        'input_set_type': 'inputSetType',
        'tags': 'tags',
        'git_details': 'gitDetails',
        'created_at': 'createdAt',
        'last_updated_at': 'lastUpdatedAt',
        'is_outdated': 'isOutdated',
        'input_set_error_details': 'inputSetErrorDetails',
        'overlay_set_error_details': 'overlaySetErrorDetails',
        'entity_validity_details': 'entityValidityDetails',
        'modules': 'modules'
    }

    def __init__(self, identifier=None, name=None, pipeline_identifier=None, description=None, input_set_type=None, tags=None, git_details=None, created_at=None, last_updated_at=None, is_outdated=None, input_set_error_details=None, overlay_set_error_details=None, entity_validity_details=None, modules=None):  # noqa: E501
        """InputSetSummaryResponse - a model defined in Swagger"""  # noqa: E501
        self._identifier = None
        self._name = None
        self._pipeline_identifier = None
        self._description = None
        self._input_set_type = None
        self._tags = None
        self._git_details = None
        self._created_at = None
        self._last_updated_at = None
        self._is_outdated = None
        self._input_set_error_details = None
        self._overlay_set_error_details = None
        self._entity_validity_details = None
        self._modules = None
        self.discriminator = None
        if identifier is not None:
            self.identifier = identifier
        if name is not None:
            self.name = name
        if pipeline_identifier is not None:
            self.pipeline_identifier = pipeline_identifier
        if description is not None:
            self.description = description
        if input_set_type is not None:
            self.input_set_type = input_set_type
        if tags is not None:
            self.tags = tags
        if git_details is not None:
            self.git_details = git_details
        if created_at is not None:
            self.created_at = created_at
        if last_updated_at is not None:
            self.last_updated_at = last_updated_at
        if is_outdated is not None:
            self.is_outdated = is_outdated
        if input_set_error_details is not None:
            self.input_set_error_details = input_set_error_details
        if overlay_set_error_details is not None:
            self.overlay_set_error_details = overlay_set_error_details
        if entity_validity_details is not None:
            self.entity_validity_details = entity_validity_details
        if modules is not None:
            self.modules = modules

    @property
    def identifier(self):
        """Gets the identifier of this InputSetSummaryResponse.  # noqa: E501

        Input Set Identifier  # noqa: E501

        :return: The identifier of this InputSetSummaryResponse.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this InputSetSummaryResponse.

        Input Set Identifier  # noqa: E501

        :param identifier: The identifier of this InputSetSummaryResponse.  # noqa: E501
        :type: str
        """

        self._identifier = identifier

    @property
    def name(self):
        """Gets the name of this InputSetSummaryResponse.  # noqa: E501

        Input Set Name  # noqa: E501

        :return: The name of this InputSetSummaryResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InputSetSummaryResponse.

        Input Set Name  # noqa: E501

        :param name: The name of this InputSetSummaryResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def pipeline_identifier(self):
        """Gets the pipeline_identifier of this InputSetSummaryResponse.  # noqa: E501

        Pipeline Identifier for the entity.  # noqa: E501

        :return: The pipeline_identifier of this InputSetSummaryResponse.  # noqa: E501
        :rtype: str
        """
        return self._pipeline_identifier

    @pipeline_identifier.setter
    def pipeline_identifier(self, pipeline_identifier):
        """Sets the pipeline_identifier of this InputSetSummaryResponse.

        Pipeline Identifier for the entity.  # noqa: E501

        :param pipeline_identifier: The pipeline_identifier of this InputSetSummaryResponse.  # noqa: E501
        :type: str
        """

        self._pipeline_identifier = pipeline_identifier

    @property
    def description(self):
        """Gets the description of this InputSetSummaryResponse.  # noqa: E501

        Input Set description  # noqa: E501

        :return: The description of this InputSetSummaryResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InputSetSummaryResponse.

        Input Set description  # noqa: E501

        :param description: The description of this InputSetSummaryResponse.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def input_set_type(self):
        """Gets the input_set_type of this InputSetSummaryResponse.  # noqa: E501

        Type of Input Set. The default value is ALL.  # noqa: E501

        :return: The input_set_type of this InputSetSummaryResponse.  # noqa: E501
        :rtype: str
        """
        return self._input_set_type

    @input_set_type.setter
    def input_set_type(self, input_set_type):
        """Sets the input_set_type of this InputSetSummaryResponse.

        Type of Input Set. The default value is ALL.  # noqa: E501

        :param input_set_type: The input_set_type of this InputSetSummaryResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["INPUT_SET", "OVERLAY_INPUT_SET"]  # noqa: E501
        if input_set_type not in allowed_values:
            raise ValueError(
                "Invalid value for `input_set_type` ({0}), must be one of {1}"  # noqa: E501
                .format(input_set_type, allowed_values)
            )

        self._input_set_type = input_set_type

    @property
    def tags(self):
        """Gets the tags of this InputSetSummaryResponse.  # noqa: E501

        Input Set tags  # noqa: E501

        :return: The tags of this InputSetSummaryResponse.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this InputSetSummaryResponse.

        Input Set tags  # noqa: E501

        :param tags: The tags of this InputSetSummaryResponse.  # noqa: E501
        :type: dict(str, str)
        """

        self._tags = tags

    @property
    def git_details(self):
        """Gets the git_details of this InputSetSummaryResponse.  # noqa: E501


        :return: The git_details of this InputSetSummaryResponse.  # noqa: E501
        :rtype: PipelineEntityGitDetails
        """
        return self._git_details

    @git_details.setter
    def git_details(self, git_details):
        """Sets the git_details of this InputSetSummaryResponse.


        :param git_details: The git_details of this InputSetSummaryResponse.  # noqa: E501
        :type: PipelineEntityGitDetails
        """

        self._git_details = git_details

    @property
    def created_at(self):
        """Gets the created_at of this InputSetSummaryResponse.  # noqa: E501

        Time at which the entity was created  # noqa: E501

        :return: The created_at of this InputSetSummaryResponse.  # noqa: E501
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this InputSetSummaryResponse.

        Time at which the entity was created  # noqa: E501

        :param created_at: The created_at of this InputSetSummaryResponse.  # noqa: E501
        :type: int
        """

        self._created_at = created_at

    @property
    def last_updated_at(self):
        """Gets the last_updated_at of this InputSetSummaryResponse.  # noqa: E501

        Time at which the entity was last updated  # noqa: E501

        :return: The last_updated_at of this InputSetSummaryResponse.  # noqa: E501
        :rtype: int
        """
        return self._last_updated_at

    @last_updated_at.setter
    def last_updated_at(self, last_updated_at):
        """Sets the last_updated_at of this InputSetSummaryResponse.

        Time at which the entity was last updated  # noqa: E501

        :param last_updated_at: The last_updated_at of this InputSetSummaryResponse.  # noqa: E501
        :type: int
        """

        self._last_updated_at = last_updated_at

    @property
    def is_outdated(self):
        """Gets the is_outdated of this InputSetSummaryResponse.  # noqa: E501

        This field is true if a Pipeline update has made this Input Set invalid, and cannot be used for Pipeline Execution  # noqa: E501

        :return: The is_outdated of this InputSetSummaryResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_outdated

    @is_outdated.setter
    def is_outdated(self, is_outdated):
        """Sets the is_outdated of this InputSetSummaryResponse.

        This field is true if a Pipeline update has made this Input Set invalid, and cannot be used for Pipeline Execution  # noqa: E501

        :param is_outdated: The is_outdated of this InputSetSummaryResponse.  # noqa: E501
        :type: bool
        """

        self._is_outdated = is_outdated

    @property
    def input_set_error_details(self):
        """Gets the input_set_error_details of this InputSetSummaryResponse.  # noqa: E501


        :return: The input_set_error_details of this InputSetSummaryResponse.  # noqa: E501
        :rtype: InputSetErrorWrapper
        """
        return self._input_set_error_details

    @input_set_error_details.setter
    def input_set_error_details(self, input_set_error_details):
        """Sets the input_set_error_details of this InputSetSummaryResponse.


        :param input_set_error_details: The input_set_error_details of this InputSetSummaryResponse.  # noqa: E501
        :type: InputSetErrorWrapper
        """

        self._input_set_error_details = input_set_error_details

    @property
    def overlay_set_error_details(self):
        """Gets the overlay_set_error_details of this InputSetSummaryResponse.  # noqa: E501

        This contains the invalid references in the Overlay Input Set, along with a message why they are invalid  # noqa: E501

        :return: The overlay_set_error_details of this InputSetSummaryResponse.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._overlay_set_error_details

    @overlay_set_error_details.setter
    def overlay_set_error_details(self, overlay_set_error_details):
        """Sets the overlay_set_error_details of this InputSetSummaryResponse.

        This contains the invalid references in the Overlay Input Set, along with a message why they are invalid  # noqa: E501

        :param overlay_set_error_details: The overlay_set_error_details of this InputSetSummaryResponse.  # noqa: E501
        :type: dict(str, str)
        """

        self._overlay_set_error_details = overlay_set_error_details

    @property
    def entity_validity_details(self):
        """Gets the entity_validity_details of this InputSetSummaryResponse.  # noqa: E501


        :return: The entity_validity_details of this InputSetSummaryResponse.  # noqa: E501
        :rtype: PipelineEntityGitDetails
        """
        return self._entity_validity_details

    @entity_validity_details.setter
    def entity_validity_details(self, entity_validity_details):
        """Sets the entity_validity_details of this InputSetSummaryResponse.


        :param entity_validity_details: The entity_validity_details of this InputSetSummaryResponse.  # noqa: E501
        :type: PipelineEntityGitDetails
        """

        self._entity_validity_details = entity_validity_details

    @property
    def modules(self):
        """Gets the modules of this InputSetSummaryResponse.  # noqa: E501

        Modules in which the Pipeline belongs  # noqa: E501

        :return: The modules of this InputSetSummaryResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._modules

    @modules.setter
    def modules(self, modules):
        """Sets the modules of this InputSetSummaryResponse.

        Modules in which the Pipeline belongs  # noqa: E501

        :param modules: The modules of this InputSetSummaryResponse.  # noqa: E501
        :type: list[str]
        """

        self._modules = modules

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
        if issubclass(InputSetSummaryResponse, dict):
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
        if not isinstance(other, InputSetSummaryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
