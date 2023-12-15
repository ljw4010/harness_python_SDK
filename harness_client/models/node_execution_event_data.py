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
from swagger_client.models.audit_event_data import AuditEventData  # noqa: F401,E501

class NodeExecutionEventData(AuditEventData):
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
        'account_identifier': 'str',
        'org_identifier': 'str',
        'project_identifier': 'str',
        'pipeline_identifier': 'str',
        'stage_identifier': 'str',
        'stage_type': 'str',
        'plan_execution_id': 'str',
        'run_sequence': 'int',
        'node_execution_id': 'str',
        'status': 'str',
        'triggered_by': 'TriggeredByInfoAuditDetails',
        'start_ts': 'int',
        'end_ts': 'int'
    }
    if hasattr(AuditEventData, "swagger_types"):
        swagger_types.update(AuditEventData.swagger_types)

    attribute_map = {
        'account_identifier': 'accountIdentifier',
        'org_identifier': 'orgIdentifier',
        'project_identifier': 'projectIdentifier',
        'pipeline_identifier': 'pipelineIdentifier',
        'stage_identifier': 'stageIdentifier',
        'stage_type': 'stageType',
        'plan_execution_id': 'planExecutionId',
        'run_sequence': 'runSequence',
        'node_execution_id': 'nodeExecutionId',
        'status': 'status',
        'triggered_by': 'triggeredBy',
        'start_ts': 'startTs',
        'end_ts': 'endTs'
    }
    if hasattr(AuditEventData, "attribute_map"):
        attribute_map.update(AuditEventData.attribute_map)

    def __init__(self, account_identifier=None, org_identifier=None, project_identifier=None, pipeline_identifier=None, stage_identifier=None, stage_type=None, plan_execution_id=None, run_sequence=None, node_execution_id=None, status=None, triggered_by=None, start_ts=None, end_ts=None, *args, **kwargs):  # noqa: E501
        """NodeExecutionEventData - a model defined in Swagger"""  # noqa: E501
        self._account_identifier = None
        self._org_identifier = None
        self._project_identifier = None
        self._pipeline_identifier = None
        self._stage_identifier = None
        self._stage_type = None
        self._plan_execution_id = None
        self._run_sequence = None
        self._node_execution_id = None
        self._status = None
        self._triggered_by = None
        self._start_ts = None
        self._end_ts = None
        self.discriminator = None
        if account_identifier is not None:
            self.account_identifier = account_identifier
        if org_identifier is not None:
            self.org_identifier = org_identifier
        if project_identifier is not None:
            self.project_identifier = project_identifier
        if pipeline_identifier is not None:
            self.pipeline_identifier = pipeline_identifier
        if stage_identifier is not None:
            self.stage_identifier = stage_identifier
        if stage_type is not None:
            self.stage_type = stage_type
        if plan_execution_id is not None:
            self.plan_execution_id = plan_execution_id
        if run_sequence is not None:
            self.run_sequence = run_sequence
        if node_execution_id is not None:
            self.node_execution_id = node_execution_id
        if status is not None:
            self.status = status
        if triggered_by is not None:
            self.triggered_by = triggered_by
        if start_ts is not None:
            self.start_ts = start_ts
        if end_ts is not None:
            self.end_ts = end_ts
        AuditEventData.__init__(self, *args, **kwargs)

    @property
    def account_identifier(self):
        """Gets the account_identifier of this NodeExecutionEventData.  # noqa: E501


        :return: The account_identifier of this NodeExecutionEventData.  # noqa: E501
        :rtype: str
        """
        return self._account_identifier

    @account_identifier.setter
    def account_identifier(self, account_identifier):
        """Sets the account_identifier of this NodeExecutionEventData.


        :param account_identifier: The account_identifier of this NodeExecutionEventData.  # noqa: E501
        :type: str
        """

        self._account_identifier = account_identifier

    @property
    def org_identifier(self):
        """Gets the org_identifier of this NodeExecutionEventData.  # noqa: E501


        :return: The org_identifier of this NodeExecutionEventData.  # noqa: E501
        :rtype: str
        """
        return self._org_identifier

    @org_identifier.setter
    def org_identifier(self, org_identifier):
        """Sets the org_identifier of this NodeExecutionEventData.


        :param org_identifier: The org_identifier of this NodeExecutionEventData.  # noqa: E501
        :type: str
        """

        self._org_identifier = org_identifier

    @property
    def project_identifier(self):
        """Gets the project_identifier of this NodeExecutionEventData.  # noqa: E501


        :return: The project_identifier of this NodeExecutionEventData.  # noqa: E501
        :rtype: str
        """
        return self._project_identifier

    @project_identifier.setter
    def project_identifier(self, project_identifier):
        """Sets the project_identifier of this NodeExecutionEventData.


        :param project_identifier: The project_identifier of this NodeExecutionEventData.  # noqa: E501
        :type: str
        """

        self._project_identifier = project_identifier

    @property
    def pipeline_identifier(self):
        """Gets the pipeline_identifier of this NodeExecutionEventData.  # noqa: E501


        :return: The pipeline_identifier of this NodeExecutionEventData.  # noqa: E501
        :rtype: str
        """
        return self._pipeline_identifier

    @pipeline_identifier.setter
    def pipeline_identifier(self, pipeline_identifier):
        """Sets the pipeline_identifier of this NodeExecutionEventData.


        :param pipeline_identifier: The pipeline_identifier of this NodeExecutionEventData.  # noqa: E501
        :type: str
        """

        self._pipeline_identifier = pipeline_identifier

    @property
    def stage_identifier(self):
        """Gets the stage_identifier of this NodeExecutionEventData.  # noqa: E501


        :return: The stage_identifier of this NodeExecutionEventData.  # noqa: E501
        :rtype: str
        """
        return self._stage_identifier

    @stage_identifier.setter
    def stage_identifier(self, stage_identifier):
        """Sets the stage_identifier of this NodeExecutionEventData.


        :param stage_identifier: The stage_identifier of this NodeExecutionEventData.  # noqa: E501
        :type: str
        """

        self._stage_identifier = stage_identifier

    @property
    def stage_type(self):
        """Gets the stage_type of this NodeExecutionEventData.  # noqa: E501


        :return: The stage_type of this NodeExecutionEventData.  # noqa: E501
        :rtype: str
        """
        return self._stage_type

    @stage_type.setter
    def stage_type(self, stage_type):
        """Sets the stage_type of this NodeExecutionEventData.


        :param stage_type: The stage_type of this NodeExecutionEventData.  # noqa: E501
        :type: str
        """

        self._stage_type = stage_type

    @property
    def plan_execution_id(self):
        """Gets the plan_execution_id of this NodeExecutionEventData.  # noqa: E501


        :return: The plan_execution_id of this NodeExecutionEventData.  # noqa: E501
        :rtype: str
        """
        return self._plan_execution_id

    @plan_execution_id.setter
    def plan_execution_id(self, plan_execution_id):
        """Sets the plan_execution_id of this NodeExecutionEventData.


        :param plan_execution_id: The plan_execution_id of this NodeExecutionEventData.  # noqa: E501
        :type: str
        """

        self._plan_execution_id = plan_execution_id

    @property
    def run_sequence(self):
        """Gets the run_sequence of this NodeExecutionEventData.  # noqa: E501


        :return: The run_sequence of this NodeExecutionEventData.  # noqa: E501
        :rtype: int
        """
        return self._run_sequence

    @run_sequence.setter
    def run_sequence(self, run_sequence):
        """Sets the run_sequence of this NodeExecutionEventData.


        :param run_sequence: The run_sequence of this NodeExecutionEventData.  # noqa: E501
        :type: int
        """

        self._run_sequence = run_sequence

    @property
    def node_execution_id(self):
        """Gets the node_execution_id of this NodeExecutionEventData.  # noqa: E501


        :return: The node_execution_id of this NodeExecutionEventData.  # noqa: E501
        :rtype: str
        """
        return self._node_execution_id

    @node_execution_id.setter
    def node_execution_id(self, node_execution_id):
        """Sets the node_execution_id of this NodeExecutionEventData.


        :param node_execution_id: The node_execution_id of this NodeExecutionEventData.  # noqa: E501
        :type: str
        """

        self._node_execution_id = node_execution_id

    @property
    def status(self):
        """Gets the status of this NodeExecutionEventData.  # noqa: E501


        :return: The status of this NodeExecutionEventData.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this NodeExecutionEventData.


        :param status: The status of this NodeExecutionEventData.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def triggered_by(self):
        """Gets the triggered_by of this NodeExecutionEventData.  # noqa: E501


        :return: The triggered_by of this NodeExecutionEventData.  # noqa: E501
        :rtype: TriggeredByInfoAuditDetails
        """
        return self._triggered_by

    @triggered_by.setter
    def triggered_by(self, triggered_by):
        """Sets the triggered_by of this NodeExecutionEventData.


        :param triggered_by: The triggered_by of this NodeExecutionEventData.  # noqa: E501
        :type: TriggeredByInfoAuditDetails
        """

        self._triggered_by = triggered_by

    @property
    def start_ts(self):
        """Gets the start_ts of this NodeExecutionEventData.  # noqa: E501


        :return: The start_ts of this NodeExecutionEventData.  # noqa: E501
        :rtype: int
        """
        return self._start_ts

    @start_ts.setter
    def start_ts(self, start_ts):
        """Sets the start_ts of this NodeExecutionEventData.


        :param start_ts: The start_ts of this NodeExecutionEventData.  # noqa: E501
        :type: int
        """

        self._start_ts = start_ts

    @property
    def end_ts(self):
        """Gets the end_ts of this NodeExecutionEventData.  # noqa: E501


        :return: The end_ts of this NodeExecutionEventData.  # noqa: E501
        :rtype: int
        """
        return self._end_ts

    @end_ts.setter
    def end_ts(self, end_ts):
        """Sets the end_ts of this NodeExecutionEventData.


        :param end_ts: The end_ts of this NodeExecutionEventData.  # noqa: E501
        :type: int
        """

        self._end_ts = end_ts

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
        if issubclass(NodeExecutionEventData, dict):
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
        if not isinstance(other, NodeExecutionEventData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
