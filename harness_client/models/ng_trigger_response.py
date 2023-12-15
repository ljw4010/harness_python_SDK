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

class NGTriggerResponse(object):
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
        'identifier': 'str',
        'description': 'str',
        'type': 'str',
        'account_identifier': 'str',
        'org_identifier': 'str',
        'project_identifier': 'str',
        'target_identifier': 'str',
        'yaml': 'str',
        'enabled': 'bool',
        'errors': 'dict(str, dict(str, str))',
        'error_response': 'bool',
        'stages_to_execute': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'identifier': 'identifier',
        'description': 'description',
        'type': 'type',
        'account_identifier': 'accountIdentifier',
        'org_identifier': 'orgIdentifier',
        'project_identifier': 'projectIdentifier',
        'target_identifier': 'targetIdentifier',
        'yaml': 'yaml',
        'enabled': 'enabled',
        'errors': 'errors',
        'error_response': 'errorResponse',
        'stages_to_execute': 'stagesToExecute'
    }

    def __init__(self, name=None, identifier=None, description=None, type=None, account_identifier=None, org_identifier=None, project_identifier=None, target_identifier=None, yaml=None, enabled=None, errors=None, error_response=None, stages_to_execute=None):  # noqa: E501
        """NGTriggerResponse - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._identifier = None
        self._description = None
        self._type = None
        self._account_identifier = None
        self._org_identifier = None
        self._project_identifier = None
        self._target_identifier = None
        self._yaml = None
        self._enabled = None
        self._errors = None
        self._error_response = None
        self._stages_to_execute = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if identifier is not None:
            self.identifier = identifier
        if description is not None:
            self.description = description
        if type is not None:
            self.type = type
        if account_identifier is not None:
            self.account_identifier = account_identifier
        if org_identifier is not None:
            self.org_identifier = org_identifier
        if project_identifier is not None:
            self.project_identifier = project_identifier
        if target_identifier is not None:
            self.target_identifier = target_identifier
        if yaml is not None:
            self.yaml = yaml
        if enabled is not None:
            self.enabled = enabled
        if errors is not None:
            self.errors = errors
        if error_response is not None:
            self.error_response = error_response
        if stages_to_execute is not None:
            self.stages_to_execute = stages_to_execute

    @property
    def name(self):
        """Gets the name of this NGTriggerResponse.  # noqa: E501


        :return: The name of this NGTriggerResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NGTriggerResponse.


        :param name: The name of this NGTriggerResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def identifier(self):
        """Gets the identifier of this NGTriggerResponse.  # noqa: E501


        :return: The identifier of this NGTriggerResponse.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this NGTriggerResponse.


        :param identifier: The identifier of this NGTriggerResponse.  # noqa: E501
        :type: str
        """

        self._identifier = identifier

    @property
    def description(self):
        """Gets the description of this NGTriggerResponse.  # noqa: E501


        :return: The description of this NGTriggerResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NGTriggerResponse.


        :param description: The description of this NGTriggerResponse.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def type(self):
        """Gets the type of this NGTriggerResponse.  # noqa: E501


        :return: The type of this NGTriggerResponse.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this NGTriggerResponse.


        :param type: The type of this NGTriggerResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["Webhook", "Artifact", "Manifest", "Scheduled", "MultiRegionArtifact"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def account_identifier(self):
        """Gets the account_identifier of this NGTriggerResponse.  # noqa: E501


        :return: The account_identifier of this NGTriggerResponse.  # noqa: E501
        :rtype: str
        """
        return self._account_identifier

    @account_identifier.setter
    def account_identifier(self, account_identifier):
        """Sets the account_identifier of this NGTriggerResponse.


        :param account_identifier: The account_identifier of this NGTriggerResponse.  # noqa: E501
        :type: str
        """

        self._account_identifier = account_identifier

    @property
    def org_identifier(self):
        """Gets the org_identifier of this NGTriggerResponse.  # noqa: E501


        :return: The org_identifier of this NGTriggerResponse.  # noqa: E501
        :rtype: str
        """
        return self._org_identifier

    @org_identifier.setter
    def org_identifier(self, org_identifier):
        """Sets the org_identifier of this NGTriggerResponse.


        :param org_identifier: The org_identifier of this NGTriggerResponse.  # noqa: E501
        :type: str
        """

        self._org_identifier = org_identifier

    @property
    def project_identifier(self):
        """Gets the project_identifier of this NGTriggerResponse.  # noqa: E501


        :return: The project_identifier of this NGTriggerResponse.  # noqa: E501
        :rtype: str
        """
        return self._project_identifier

    @project_identifier.setter
    def project_identifier(self, project_identifier):
        """Sets the project_identifier of this NGTriggerResponse.


        :param project_identifier: The project_identifier of this NGTriggerResponse.  # noqa: E501
        :type: str
        """

        self._project_identifier = project_identifier

    @property
    def target_identifier(self):
        """Gets the target_identifier of this NGTriggerResponse.  # noqa: E501


        :return: The target_identifier of this NGTriggerResponse.  # noqa: E501
        :rtype: str
        """
        return self._target_identifier

    @target_identifier.setter
    def target_identifier(self, target_identifier):
        """Sets the target_identifier of this NGTriggerResponse.


        :param target_identifier: The target_identifier of this NGTriggerResponse.  # noqa: E501
        :type: str
        """

        self._target_identifier = target_identifier

    @property
    def yaml(self):
        """Gets the yaml of this NGTriggerResponse.  # noqa: E501


        :return: The yaml of this NGTriggerResponse.  # noqa: E501
        :rtype: str
        """
        return self._yaml

    @yaml.setter
    def yaml(self, yaml):
        """Sets the yaml of this NGTriggerResponse.


        :param yaml: The yaml of this NGTriggerResponse.  # noqa: E501
        :type: str
        """

        self._yaml = yaml

    @property
    def enabled(self):
        """Gets the enabled of this NGTriggerResponse.  # noqa: E501


        :return: The enabled of this NGTriggerResponse.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this NGTriggerResponse.


        :param enabled: The enabled of this NGTriggerResponse.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def errors(self):
        """Gets the errors of this NGTriggerResponse.  # noqa: E501


        :return: The errors of this NGTriggerResponse.  # noqa: E501
        :rtype: dict(str, dict(str, str))
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this NGTriggerResponse.


        :param errors: The errors of this NGTriggerResponse.  # noqa: E501
        :type: dict(str, dict(str, str))
        """

        self._errors = errors

    @property
    def error_response(self):
        """Gets the error_response of this NGTriggerResponse.  # noqa: E501


        :return: The error_response of this NGTriggerResponse.  # noqa: E501
        :rtype: bool
        """
        return self._error_response

    @error_response.setter
    def error_response(self, error_response):
        """Sets the error_response of this NGTriggerResponse.


        :param error_response: The error_response of this NGTriggerResponse.  # noqa: E501
        :type: bool
        """

        self._error_response = error_response

    @property
    def stages_to_execute(self):
        """Gets the stages_to_execute of this NGTriggerResponse.  # noqa: E501


        :return: The stages_to_execute of this NGTriggerResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._stages_to_execute

    @stages_to_execute.setter
    def stages_to_execute(self, stages_to_execute):
        """Sets the stages_to_execute of this NGTriggerResponse.


        :param stages_to_execute: The stages_to_execute of this NGTriggerResponse.  # noqa: E501
        :type: list[str]
        """

        self._stages_to_execute = stages_to_execute

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
        if issubclass(NGTriggerResponse, dict):
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
        if not isinstance(other, NGTriggerResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other