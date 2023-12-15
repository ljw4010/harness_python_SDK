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

class TemplateDTO(object):
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
        'template_ref': 'str',
        'version_label': 'str',
        'template_version_number': 'int',
        'input_set_yaml': 'str',
        'is_template_by_reference': 'bool',
        'last_reconciliation_time': 'int',
        'template_by_reference': 'bool'
    }

    attribute_map = {
        'template_ref': 'templateRef',
        'version_label': 'versionLabel',
        'template_version_number': 'templateVersionNumber',
        'input_set_yaml': 'inputSetYaml',
        'is_template_by_reference': 'isTemplateByReference',
        'last_reconciliation_time': 'lastReconciliationTime',
        'template_by_reference': 'templateByReference'
    }

    def __init__(self, template_ref=None, version_label=None, template_version_number=None, input_set_yaml=None, is_template_by_reference=None, last_reconciliation_time=None, template_by_reference=None):  # noqa: E501
        """TemplateDTO - a model defined in Swagger"""  # noqa: E501
        self._template_ref = None
        self._version_label = None
        self._template_version_number = None
        self._input_set_yaml = None
        self._is_template_by_reference = None
        self._last_reconciliation_time = None
        self._template_by_reference = None
        self.discriminator = None
        self.template_ref = template_ref
        if version_label is not None:
            self.version_label = version_label
        if template_version_number is not None:
            self.template_version_number = template_version_number
        if input_set_yaml is not None:
            self.input_set_yaml = input_set_yaml
        if is_template_by_reference is not None:
            self.is_template_by_reference = is_template_by_reference
        if last_reconciliation_time is not None:
            self.last_reconciliation_time = last_reconciliation_time
        if template_by_reference is not None:
            self.template_by_reference = template_by_reference

    @property
    def template_ref(self):
        """Gets the template_ref of this TemplateDTO.  # noqa: E501


        :return: The template_ref of this TemplateDTO.  # noqa: E501
        :rtype: str
        """
        return self._template_ref

    @template_ref.setter
    def template_ref(self, template_ref):
        """Sets the template_ref of this TemplateDTO.


        :param template_ref: The template_ref of this TemplateDTO.  # noqa: E501
        :type: str
        """
        if template_ref is None:
            raise ValueError("Invalid value for `template_ref`, must not be `None`")  # noqa: E501

        self._template_ref = template_ref

    @property
    def version_label(self):
        """Gets the version_label of this TemplateDTO.  # noqa: E501


        :return: The version_label of this TemplateDTO.  # noqa: E501
        :rtype: str
        """
        return self._version_label

    @version_label.setter
    def version_label(self, version_label):
        """Sets the version_label of this TemplateDTO.


        :param version_label: The version_label of this TemplateDTO.  # noqa: E501
        :type: str
        """

        self._version_label = version_label

    @property
    def template_version_number(self):
        """Gets the template_version_number of this TemplateDTO.  # noqa: E501


        :return: The template_version_number of this TemplateDTO.  # noqa: E501
        :rtype: int
        """
        return self._template_version_number

    @template_version_number.setter
    def template_version_number(self, template_version_number):
        """Sets the template_version_number of this TemplateDTO.


        :param template_version_number: The template_version_number of this TemplateDTO.  # noqa: E501
        :type: int
        """

        self._template_version_number = template_version_number

    @property
    def input_set_yaml(self):
        """Gets the input_set_yaml of this TemplateDTO.  # noqa: E501


        :return: The input_set_yaml of this TemplateDTO.  # noqa: E501
        :rtype: str
        """
        return self._input_set_yaml

    @input_set_yaml.setter
    def input_set_yaml(self, input_set_yaml):
        """Sets the input_set_yaml of this TemplateDTO.


        :param input_set_yaml: The input_set_yaml of this TemplateDTO.  # noqa: E501
        :type: str
        """

        self._input_set_yaml = input_set_yaml

    @property
    def is_template_by_reference(self):
        """Gets the is_template_by_reference of this TemplateDTO.  # noqa: E501


        :return: The is_template_by_reference of this TemplateDTO.  # noqa: E501
        :rtype: bool
        """
        return self._is_template_by_reference

    @is_template_by_reference.setter
    def is_template_by_reference(self, is_template_by_reference):
        """Sets the is_template_by_reference of this TemplateDTO.


        :param is_template_by_reference: The is_template_by_reference of this TemplateDTO.  # noqa: E501
        :type: bool
        """

        self._is_template_by_reference = is_template_by_reference

    @property
    def last_reconciliation_time(self):
        """Gets the last_reconciliation_time of this TemplateDTO.  # noqa: E501


        :return: The last_reconciliation_time of this TemplateDTO.  # noqa: E501
        :rtype: int
        """
        return self._last_reconciliation_time

    @last_reconciliation_time.setter
    def last_reconciliation_time(self, last_reconciliation_time):
        """Sets the last_reconciliation_time of this TemplateDTO.


        :param last_reconciliation_time: The last_reconciliation_time of this TemplateDTO.  # noqa: E501
        :type: int
        """

        self._last_reconciliation_time = last_reconciliation_time

    @property
    def template_by_reference(self):
        """Gets the template_by_reference of this TemplateDTO.  # noqa: E501


        :return: The template_by_reference of this TemplateDTO.  # noqa: E501
        :rtype: bool
        """
        return self._template_by_reference

    @template_by_reference.setter
    def template_by_reference(self, template_by_reference):
        """Sets the template_by_reference of this TemplateDTO.


        :param template_by_reference: The template_by_reference of this TemplateDTO.  # noqa: E501
        :type: bool
        """

        self._template_by_reference = template_by_reference

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
        if issubclass(TemplateDTO, dict):
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
        if not isinstance(other, TemplateDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
