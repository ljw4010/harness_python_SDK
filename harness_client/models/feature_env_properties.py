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

class FeatureEnvProperties(object):
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
        'default_serve': 'Serve',
        'environment': 'str',
        'jira_enabled': 'bool',
        'jira_issues': 'list[JiraIssue]',
        'modified_at': 'int',
        'off_variation': 'str',
        'pipeline_configured': 'bool',
        'pipeline_details': 'FeaturePipeline',
        'pipeline_error_reason': 'str',
        'pipeline_error_state': 'bool',
        'rules': 'list[ServingRule]',
        'state': 'FeatureState',
        'variation_map': 'list[VariationMap]',
        'version': 'int'
    }

    attribute_map = {
        'default_serve': 'defaultServe',
        'environment': 'environment',
        'jira_enabled': 'jiraEnabled',
        'jira_issues': 'jiraIssues',
        'modified_at': 'modifiedAt',
        'off_variation': 'offVariation',
        'pipeline_configured': 'pipelineConfigured',
        'pipeline_details': 'pipelineDetails',
        'pipeline_error_reason': 'pipelineErrorReason',
        'pipeline_error_state': 'pipelineErrorState',
        'rules': 'rules',
        'state': 'state',
        'variation_map': 'variationMap',
        'version': 'version'
    }

    def __init__(self, default_serve=None, environment=None, jira_enabled=None, jira_issues=None, modified_at=None, off_variation=None, pipeline_configured=None, pipeline_details=None, pipeline_error_reason=None, pipeline_error_state=None, rules=None, state=None, variation_map=None, version=None):  # noqa: E501
        """FeatureEnvProperties - a model defined in Swagger"""  # noqa: E501
        self._default_serve = None
        self._environment = None
        self._jira_enabled = None
        self._jira_issues = None
        self._modified_at = None
        self._off_variation = None
        self._pipeline_configured = None
        self._pipeline_details = None
        self._pipeline_error_reason = None
        self._pipeline_error_state = None
        self._rules = None
        self._state = None
        self._variation_map = None
        self._version = None
        self.discriminator = None
        self.default_serve = default_serve
        self.environment = environment
        if jira_enabled is not None:
            self.jira_enabled = jira_enabled
        if jira_issues is not None:
            self.jira_issues = jira_issues
        if modified_at is not None:
            self.modified_at = modified_at
        self.off_variation = off_variation
        self.pipeline_configured = pipeline_configured
        if pipeline_details is not None:
            self.pipeline_details = pipeline_details
        if pipeline_error_reason is not None:
            self.pipeline_error_reason = pipeline_error_reason
        if pipeline_error_state is not None:
            self.pipeline_error_state = pipeline_error_state
        if rules is not None:
            self.rules = rules
        self.state = state
        if variation_map is not None:
            self.variation_map = variation_map
        if version is not None:
            self.version = version

    @property
    def default_serve(self):
        """Gets the default_serve of this FeatureEnvProperties.  # noqa: E501


        :return: The default_serve of this FeatureEnvProperties.  # noqa: E501
        :rtype: Serve
        """
        return self._default_serve

    @default_serve.setter
    def default_serve(self, default_serve):
        """Sets the default_serve of this FeatureEnvProperties.


        :param default_serve: The default_serve of this FeatureEnvProperties.  # noqa: E501
        :type: Serve
        """
        if default_serve is None:
            raise ValueError("Invalid value for `default_serve`, must not be `None`")  # noqa: E501

        self._default_serve = default_serve

    @property
    def environment(self):
        """Gets the environment of this FeatureEnvProperties.  # noqa: E501

        The environment identifier  # noqa: E501

        :return: The environment of this FeatureEnvProperties.  # noqa: E501
        :rtype: str
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this FeatureEnvProperties.

        The environment identifier  # noqa: E501

        :param environment: The environment of this FeatureEnvProperties.  # noqa: E501
        :type: str
        """
        if environment is None:
            raise ValueError("Invalid value for `environment`, must not be `None`")  # noqa: E501

        self._environment = environment

    @property
    def jira_enabled(self):
        """Gets the jira_enabled of this FeatureEnvProperties.  # noqa: E501

        Indicates whether jira functionality is enabled for the given account, project, org, and environment  # noqa: E501

        :return: The jira_enabled of this FeatureEnvProperties.  # noqa: E501
        :rtype: bool
        """
        return self._jira_enabled

    @jira_enabled.setter
    def jira_enabled(self, jira_enabled):
        """Sets the jira_enabled of this FeatureEnvProperties.

        Indicates whether jira functionality is enabled for the given account, project, org, and environment  # noqa: E501

        :param jira_enabled: The jira_enabled of this FeatureEnvProperties.  # noqa: E501
        :type: bool
        """

        self._jira_enabled = jira_enabled

    @property
    def jira_issues(self):
        """Gets the jira_issues of this FeatureEnvProperties.  # noqa: E501

        An array of Jira Issues linked to this Feature. Returns empty if none exist  # noqa: E501

        :return: The jira_issues of this FeatureEnvProperties.  # noqa: E501
        :rtype: list[JiraIssue]
        """
        return self._jira_issues

    @jira_issues.setter
    def jira_issues(self, jira_issues):
        """Sets the jira_issues of this FeatureEnvProperties.

        An array of Jira Issues linked to this Feature. Returns empty if none exist  # noqa: E501

        :param jira_issues: The jira_issues of this FeatureEnvProperties.  # noqa: E501
        :type: list[JiraIssue]
        """

        self._jira_issues = jira_issues

    @property
    def modified_at(self):
        """Gets the modified_at of this FeatureEnvProperties.  # noqa: E501

        The last time the flag was modified in this environment  # noqa: E501

        :return: The modified_at of this FeatureEnvProperties.  # noqa: E501
        :rtype: int
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """Sets the modified_at of this FeatureEnvProperties.

        The last time the flag was modified in this environment  # noqa: E501

        :param modified_at: The modified_at of this FeatureEnvProperties.  # noqa: E501
        :type: int
        """

        self._modified_at = modified_at

    @property
    def off_variation(self):
        """Gets the off_variation of this FeatureEnvProperties.  # noqa: E501

        The variation to serve for this flag in this environment when the flag is off  # noqa: E501

        :return: The off_variation of this FeatureEnvProperties.  # noqa: E501
        :rtype: str
        """
        return self._off_variation

    @off_variation.setter
    def off_variation(self, off_variation):
        """Sets the off_variation of this FeatureEnvProperties.

        The variation to serve for this flag in this environment when the flag is off  # noqa: E501

        :param off_variation: The off_variation of this FeatureEnvProperties.  # noqa: E501
        :type: str
        """
        if off_variation is None:
            raise ValueError("Invalid value for `off_variation`, must not be `None`")  # noqa: E501

        self._off_variation = off_variation

    @property
    def pipeline_configured(self):
        """Gets the pipeline_configured of this FeatureEnvProperties.  # noqa: E501


        :return: The pipeline_configured of this FeatureEnvProperties.  # noqa: E501
        :rtype: bool
        """
        return self._pipeline_configured

    @pipeline_configured.setter
    def pipeline_configured(self, pipeline_configured):
        """Sets the pipeline_configured of this FeatureEnvProperties.


        :param pipeline_configured: The pipeline_configured of this FeatureEnvProperties.  # noqa: E501
        :type: bool
        """
        if pipeline_configured is None:
            raise ValueError("Invalid value for `pipeline_configured`, must not be `None`")  # noqa: E501

        self._pipeline_configured = pipeline_configured

    @property
    def pipeline_details(self):
        """Gets the pipeline_details of this FeatureEnvProperties.  # noqa: E501


        :return: The pipeline_details of this FeatureEnvProperties.  # noqa: E501
        :rtype: FeaturePipeline
        """
        return self._pipeline_details

    @pipeline_details.setter
    def pipeline_details(self, pipeline_details):
        """Sets the pipeline_details of this FeatureEnvProperties.


        :param pipeline_details: The pipeline_details of this FeatureEnvProperties.  # noqa: E501
        :type: FeaturePipeline
        """

        self._pipeline_details = pipeline_details

    @property
    def pipeline_error_reason(self):
        """Gets the pipeline_error_reason of this FeatureEnvProperties.  # noqa: E501


        :return: The pipeline_error_reason of this FeatureEnvProperties.  # noqa: E501
        :rtype: str
        """
        return self._pipeline_error_reason

    @pipeline_error_reason.setter
    def pipeline_error_reason(self, pipeline_error_reason):
        """Sets the pipeline_error_reason of this FeatureEnvProperties.


        :param pipeline_error_reason: The pipeline_error_reason of this FeatureEnvProperties.  # noqa: E501
        :type: str
        """

        self._pipeline_error_reason = pipeline_error_reason

    @property
    def pipeline_error_state(self):
        """Gets the pipeline_error_state of this FeatureEnvProperties.  # noqa: E501


        :return: The pipeline_error_state of this FeatureEnvProperties.  # noqa: E501
        :rtype: bool
        """
        return self._pipeline_error_state

    @pipeline_error_state.setter
    def pipeline_error_state(self, pipeline_error_state):
        """Sets the pipeline_error_state of this FeatureEnvProperties.


        :param pipeline_error_state: The pipeline_error_state of this FeatureEnvProperties.  # noqa: E501
        :type: bool
        """

        self._pipeline_error_state = pipeline_error_state

    @property
    def rules(self):
        """Gets the rules of this FeatureEnvProperties.  # noqa: E501

        A list of rules to use when evaluating this flag in this environment  # noqa: E501

        :return: The rules of this FeatureEnvProperties.  # noqa: E501
        :rtype: list[ServingRule]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this FeatureEnvProperties.

        A list of rules to use when evaluating this flag in this environment  # noqa: E501

        :param rules: The rules of this FeatureEnvProperties.  # noqa: E501
        :type: list[ServingRule]
        """

        self._rules = rules

    @property
    def state(self):
        """Gets the state of this FeatureEnvProperties.  # noqa: E501


        :return: The state of this FeatureEnvProperties.  # noqa: E501
        :rtype: FeatureState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this FeatureEnvProperties.


        :param state: The state of this FeatureEnvProperties.  # noqa: E501
        :type: FeatureState
        """
        if state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501

        self._state = state

    @property
    def variation_map(self):
        """Gets the variation_map of this FeatureEnvProperties.  # noqa: E501

        A list of the variations that will be served to specific targets or target groups in an environment.  # noqa: E501

        :return: The variation_map of this FeatureEnvProperties.  # noqa: E501
        :rtype: list[VariationMap]
        """
        return self._variation_map

    @variation_map.setter
    def variation_map(self, variation_map):
        """Sets the variation_map of this FeatureEnvProperties.

        A list of the variations that will be served to specific targets or target groups in an environment.  # noqa: E501

        :param variation_map: The variation_map of this FeatureEnvProperties.  # noqa: E501
        :type: list[VariationMap]
        """

        self._variation_map = variation_map

    @property
    def version(self):
        """Gets the version of this FeatureEnvProperties.  # noqa: E501

        The version of the flag.  This is incremented each time it is changed  # noqa: E501

        :return: The version of this FeatureEnvProperties.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this FeatureEnvProperties.

        The version of the flag.  This is incremented each time it is changed  # noqa: E501

        :param version: The version of this FeatureEnvProperties.  # noqa: E501
        :type: int
        """

        self._version = version

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
        if issubclass(FeatureEnvProperties, dict):
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
        if not isinstance(other, FeatureEnvProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
