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

class CvError(object):
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
        'status': 'str',
        'code': 'str',
        'message': 'str',
        'correlation_id': 'str',
        'detailed_message': 'str',
        'response_messages': 'list[CvResponseMessage]',
        'metadata': 'CvErrorMetadata'
    }

    attribute_map = {
        'status': 'status',
        'code': 'code',
        'message': 'message',
        'correlation_id': 'correlationId',
        'detailed_message': 'detailedMessage',
        'response_messages': 'responseMessages',
        'metadata': 'metadata'
    }

    def __init__(self, status=None, code=None, message=None, correlation_id=None, detailed_message=None, response_messages=None, metadata=None):  # noqa: E501
        """CvError - a model defined in Swagger"""  # noqa: E501
        self._status = None
        self._code = None
        self._message = None
        self._correlation_id = None
        self._detailed_message = None
        self._response_messages = None
        self._metadata = None
        self.discriminator = None
        if status is not None:
            self.status = status
        if code is not None:
            self.code = code
        if message is not None:
            self.message = message
        if correlation_id is not None:
            self.correlation_id = correlation_id
        if detailed_message is not None:
            self.detailed_message = detailed_message
        if response_messages is not None:
            self.response_messages = response_messages
        if metadata is not None:
            self.metadata = metadata

    @property
    def status(self):
        """Gets the status of this CvError.  # noqa: E501


        :return: The status of this CvError.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CvError.


        :param status: The status of this CvError.  # noqa: E501
        :type: str
        """
        allowed_values = ["SUCCESS", "FAILURE", "ERROR"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def code(self):
        """Gets the code of this CvError.  # noqa: E501


        :return: The code of this CvError.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this CvError.


        :param code: The code of this CvError.  # noqa: E501
        :type: str
        """
        allowed_values = ["DEFAULT_ERROR_CODE", "INVALID_ARGUMENT", "INVALID_EMAIL", "DOMAIN_NOT_ALLOWED_TO_REGISTER", "COMMNITY_EDITION_NOT_FOUND", "DEPLOY_MODE_IS_NOT_ON_PREM", "USER_ALREADY_REGISTERED", "USER_INVITATION_DOES_NOT_EXIST", "USER_DOES_NOT_EXIST", "USER_INVITE_OPERATION_FAILED", "USER_DISABLED", "ACCOUNT_DOES_NOT_EXIST", "INACTIVE_ACCOUNT", "ACCOUNT_MIGRATED", "ACCOUNT_MIGRATED_TO_NEXT_GEN", "USER_DOMAIN_NOT_ALLOWED", "MAX_FAILED_ATTEMPT_COUNT_EXCEEDED", "RESOURCE_NOT_FOUND", "INVALID_FORMAT", "ROLE_DOES_NOT_EXIST", "EMAIL_NOT_VERIFIED", "EMAIL_VERIFICATION_TOKEN_NOT_FOUND", "INVALID_TOKEN", "REVOKED_TOKEN", "INVALID_CAPTCHA_TOKEN", "NOT_ACCOUNT_MGR_NOR_HAS_ALL_APP_ACCESS", "EXPIRED_TOKEN", "INVALID_AGENT_MTLS_AUTHORITY", "TOKEN_ALREADY_REFRESHED_ONCE", "ACCESS_DENIED", "NG_ACCESS_DENIED", "INVALID_CREDENTIAL", "INVALID_CREDENTIALS_THIRD_PARTY", "INVALID_KEY", "INVALID_CONNECTOR_TYPE", "INVALID_KEYPATH", "INVALID_VARIABLE", "UNKNOWN_HOST", "UNREACHABLE_HOST", "INVALID_PORT", "SSH_SESSION_TIMEOUT", "SOCKET_CONNECTION_ERROR", "CONNECTION_ERROR", "SOCKET_CONNECTION_TIMEOUT", "WINRM_COMMAND_EXECUTION_TIMEOUT", "CONNECTION_TIMEOUT", "SSH_CONNECTION_ERROR", "USER_GROUP_ERROR", "INVALID_EXECUTION_ID", "ERROR_IN_GETTING_CHANNEL_STREAMS", "UNEXPECTED", "UNKNOWN_ERROR", "UNKNOWN_EXECUTOR_TYPE_ERROR", "DUPLICATE_STATE_NAMES", "TRANSITION_NOT_LINKED", "TRANSITION_TO_INCORRECT_STATE", "TRANSITION_TYPE_NULL", "STATES_WITH_DUP_TRANSITIONS", "BARRIERS_NOT_RUNNING_CONCURRENTLY", "NON_FORK_STATES", "NON_REPEAT_STATES", "INITIAL_STATE_NOT_DEFINED", "FILE_INTEGRITY_CHECK_FAILED", "INVALID_URL", "FILE_DOWNLOAD_FAILED", "PLATFORM_SOFTWARE_DELETE_ERROR", "INVALID_CSV_FILE", "INVALID_REQUEST", "SCHEMA_VALIDATION_FAILED", "FILTER_CREATION_ERROR", "INVALID_YAML_ERROR", "PLAN_CREATION_ERROR", "INVALID_INFRA_STATE", "PIPELINE_ALREADY_TRIGGERED", "NON_EXISTING_PIPELINE", "DUPLICATE_COMMAND_NAMES", "INVALID_PIPELINE", "COMMAND_DOES_NOT_EXIST", "DUPLICATE_ARTIFACTSTREAM_NAMES", "DUPLICATE_HOST_NAMES", "STATE_NOT_FOR_TYPE", "STATE_MACHINE_ISSUE", "STATE_DISCONTINUE_FAILED", "STATE_PAUSE_FAILED", "PAUSE_ALL_ALREADY", "RESUME_ALL_ALREADY", "ROLLBACK_ALREADY", "ABORT_ALL_ALREADY", "EXPIRE_ALL_ALREADY", "RETRY_FAILED", "UNKNOWN_ARTIFACT_TYPE", "UNKNOWN_STAGE_ELEMENT_WRAPPER_TYPE", "INIT_TIMEOUT", "LICENSE_EXPIRED", "NOT_LICENSED", "REQUEST_TIMEOUT", "SCM_REQUEST_TIMEOUT", "WORKFLOW_ALREADY_TRIGGERED", "JENKINS_ERROR", "INVALID_ARTIFACT_SOURCE", "INVALID_ARTIFACT_SERVER", "INVALID_CLOUD_PROVIDER", "UPDATE_NOT_ALLOWED", "DELETE_NOT_ALLOWED", "APPDYNAMICS_CONFIGURATION_ERROR", "APM_CONFIGURATION_ERROR", "SPLUNK_CONFIGURATION_ERROR", "ELK_CONFIGURATION_ERROR", "LOGZ_CONFIGURATION_ERROR", "SUMO_CONFIGURATION_ERROR", "INSTANA_CONFIGURATION_ERROR", "APPDYNAMICS_ERROR", "STACKDRIVER_ERROR", "STACKDRIVER_CONFIGURATION_ERROR", "NEWRELIC_CONFIGURATION_ERROR", "NEWRELIC_ERROR", "DYNA_TRACE_CONFIGURATION_ERROR", "DYNA_TRACE_ERROR", "CLOUDWATCH_ERROR", "CLOUDWATCH_CONFIGURATION_ERROR", "PROMETHEUS_CONFIGURATION_ERROR", "DATA_DOG_CONFIGURATION_ERROR", "SERVICE_GUARD_CONFIGURATION_ERROR", "ENCRYPTION_NOT_CONFIGURED", "UNAVAILABLE_DELEGATES", "WORKFLOW_EXECUTION_IN_PROGRESS", "PIPELINE_EXECUTION_IN_PROGRESS", "AWS_ACCESS_DENIED", "AWS_CLUSTER_NOT_FOUND", "AWS_SERVICE_NOT_FOUND", "IMAGE_NOT_FOUND", "ILLEGAL_ARGUMENT", "IMAGE_TAG_NOT_FOUND", "DELEGATE_NOT_AVAILABLE", "INVALID_YAML_PAYLOAD", "AUTHENTICATION_ERROR", "AUTHORIZATION_ERROR", "UNRECOGNIZED_YAML_FIELDS", "COULD_NOT_MAP_BEFORE_YAML", "MISSING_BEFORE_YAML", "MISSING_YAML", "NON_EMPTY_DELETIONS", "GENERAL_YAML_ERROR", "GENERAL_YAML_INFO", "YAML_GIT_SYNC_ERROR", "GIT_CONNECTION_ERROR", "GIT_ERROR", "ARTIFACT_SERVER_ERROR", "ENCRYPT_DECRYPT_ERROR", "SECRET_MANAGEMENT_ERROR", "SECRET_NOT_FOUND", "KMS_OPERATION_ERROR", "GCP_KMS_OPERATION_ERROR", "VAULT_OPERATION_ERROR", "AWS_SECRETS_MANAGER_OPERATION_ERROR", "AZURE_KEY_VAULT_OPERATION_ERROR", "UNSUPPORTED_OPERATION_EXCEPTION", "FEATURE_UNAVAILABLE", "GENERAL_ERROR", "BASELINE_CONFIGURATION_ERROR", "SAML_IDP_CONFIGURATION_NOT_AVAILABLE", "INVALID_AUTHENTICATION_MECHANISM", "INVALID_SAML_CONFIGURATION", "INVALID_OAUTH_CONFIGURATION", "INVALID_LDAP_CONFIGURATION", "USER_GROUP_SYNC_FAILURE", "USER_GROUP_ALREADY_EXIST", "INVALID_TWO_FACTOR_AUTHENTICATION_CONFIGURATION", "EXPLANATION", "HINT", "NOT_WHITELISTED_IP", "INVALID_TOTP_TOKEN", "EMAIL_FAILED", "SSL_HANDSHAKE_FAILED", "NO_APPS_ASSIGNED", "INVALID_INFRA_CONFIGURATION", "TEMPLATES_LINKED", "USER_HAS_NO_PERMISSIONS", "USER_NOT_AUTHORIZED", "USER_ALREADY_PRESENT", "EMAIL_ERROR", "INVALID_USAGE_RESTRICTION", "USAGE_RESTRICTION_ERROR", "STATE_EXECUTION_INSTANCE_NOT_FOUND", "DELEGATE_TASK_RETRY", "KUBERNETES_API_TASK_EXCEPTION", "KUBERNETES_TASK_EXCEPTION", "KUBERNETES_YAML_ERROR", "SAVE_FILE_INTO_GCP_STORAGE_FAILED", "READ_FILE_FROM_GCP_STORAGE_FAILED", "FILE_NOT_FOUND_ERROR", "USAGE_LIMITS_EXCEEDED", "EVENT_PUBLISH_FAILED", "CUSTOM_APPROVAL_ERROR", "JIRA_ERROR", "EXPRESSION_EVALUATION_FAILED", "KUBERNETES_VALUES_ERROR", "KUBERNETES_CLUSTER_ERROR", "INCORRECT_SIGN_IN_MECHANISM", "OAUTH_LOGIN_FAILED", "INVALID_TERRAFORM_TARGETS_REQUEST", "TERRAFORM_EXECUTION_ERROR", "FILE_READ_FAILED", "FILE_SIZE_EXCEEDS_LIMIT", "CLUSTER_NOT_FOUND", "MARKETPLACE_TOKEN_NOT_FOUND", "INVALID_MARKETPLACE_TOKEN", "INVALID_TICKETING_SERVER", "SERVICENOW_ERROR", "PASSWORD_EXPIRED", "USER_LOCKED", "PASSWORD_STRENGTH_CHECK_FAILED", "ACCOUNT_DISABLED", "INVALID_ACCOUNT_PERMISSION", "PAGERDUTY_ERROR", "HEALTH_ERROR", "SAML_TEST_SUCCESS_MECHANISM_NOT_ENABLED", "DOMAIN_WHITELIST_FILTER_CHECK_FAILED", "INVALID_DASHBOARD_UPDATE_REQUEST", "DUPLICATE_FIELD", "INVALID_AZURE_VAULT_CONFIGURATION", "USER_NOT_AUTHORIZED_DUE_TO_USAGE_RESTRICTIONS", "INVALID_ROLLBACK", "DATA_COLLECTION_ERROR", "SUMO_DATA_COLLECTION_ERROR", "DEPLOYMENT_GOVERNANCE_ERROR", "BATCH_PROCESSING_ERROR", "GRAPHQL_ERROR", "FILE_CREATE_ERROR", "ILLEGAL_STATE", "GIT_DIFF_COMMIT_NOT_IN_ORDER", "FAILED_TO_ACQUIRE_PERSISTENT_LOCK", "FAILED_TO_ACQUIRE_NON_PERSISTENT_LOCK", "POD_NOT_FOUND_ERROR", "COMMAND_EXECUTION_ERROR", "REGISTRY_EXCEPTION", "ENGINE_INTERRUPT_PROCESSING_EXCEPTION", "ENGINE_IO_EXCEPTION", "ENGINE_OUTCOME_EXCEPTION", "ENGINE_SWEEPING_OUTPUT_EXCEPTION", "CACHE_NOT_FOUND_EXCEPTION", "ENGINE_ENTITY_UPDATE_EXCEPTION", "SHELL_EXECUTION_EXCEPTION", "TEMPLATE_NOT_FOUND", "AZURE_SERVICE_EXCEPTION", "AZURE_CLIENT_EXCEPTION", "GIT_UNSEEN_REMOTE_HEAD_COMMIT", "TIMEOUT_ENGINE_EXCEPTION", "NO_AVAILABLE_DELEGATES", "NO_GLOBAL_DELEGATE_ACCOUNT", "NO_INSTALLED_DELEGATES", "DUPLICATE_DELEGATE_EXCEPTION", "GCP_MARKETPLACE_EXCEPTION", "MISSING_DEFAULT_GOOGLE_CREDENTIALS", "INCORRECT_DEFAULT_GOOGLE_CREDENTIALS", "OPTIMISTIC_LOCKING_EXCEPTION", "NG_PIPELINE_EXECUTION_EXCEPTION", "NG_PIPELINE_CREATE_EXCEPTION", "RESOURCE_NOT_FOUND_EXCEPTION", "PMS_INITIALIZE_SDK_EXCEPTION", "UNEXPECTED_SNIPPET_EXCEPTION", "UNEXPECTED_SCHEMA_EXCEPTION", "CONNECTOR_VALIDATION_EXCEPTION", "TIMESCALE_NOT_AVAILABLE", "MIGRATION_EXCEPTION", "REQUEST_PROCESSING_INTERRUPTED", "SECRET_MANAGER_ID_NOT_FOUND", "GCP_SECRET_MANAGER_OPERATION_ERROR", "GCP_SECRET_OPERATION_ERROR", "GIT_OPERATION_ERROR", "TASK_FAILURE_ERROR", "INSTANCE_STATS_PROCESS_ERROR", "INSTANCE_STATS_MIGRATION_ERROR", "DEPLOYMENT_MIGRATION_ERROR", "CG_LICENSE_USAGE_ERROR", "INSTANCE_STATS_AGGREGATION_ERROR", "UNRESOLVED_EXPRESSIONS_ERROR", "KRYO_HANDLER_NOT_FOUND_ERROR", "DELEGATE_ERROR_HANDLER_EXCEPTION", "DELEGATE_SERVICE_DRIVER_EXCEPTION", "DELEGATE_INSTALLATION_COMMAND_NOT_SUPPORTED_EXCEPTION", "UNEXPECTED_TYPE_ERROR", "EXCEPTION_HANDLER_NOT_FOUND", "CONNECTOR_NOT_FOUND_EXCEPTION", "GCP_SERVER_ERROR", "HTTP_RESPONSE_EXCEPTION", "SCM_NOT_FOUND_ERROR", "SCM_CONFLICT_ERROR", "SCM_CONFLICT_ERROR_V2", "SCM_UNPROCESSABLE_ENTITY", "PROCESS_EXECUTION_EXCEPTION", "SCM_UNAUTHORIZED", "SCM_BAD_REQUEST", "SCM_INTERNAL_SERVER_ERROR", "DATA", "CONTEXT", "PR_CREATION_ERROR", "URL_NOT_REACHABLE", "URL_NOT_PROVIDED", "ENGINE_EXPRESSION_EVALUATION_ERROR", "ENGINE_FUNCTOR_ERROR", "JIRA_CLIENT_ERROR", "SCM_NOT_MODIFIED", "APPROVAL_STEP_NG_ERROR", "BUCKET_SERVER_ERROR", "GIT_SYNC_ERROR", "TEMPLATE_EXCEPTION", "TEMPLATE_ALREADY_EXISTS_EXCEPTION", "ENTITY_REFERENCE_EXCEPTION", "ACTIVE_SERVICE_INSTANCES_PRESENT_EXCEPTION", "INVALID_INPUT_SET", "INVALID_OVERLAY_INPUT_SET", "RESOURCE_ALREADY_EXISTS", "INVALID_JSON_PAYLOAD", "POLICY_EVALUATION_FAILURE", "POLICY_SET_ERROR", "INVALID_ARTIFACTORY_REGISTRY_REQUEST", "INVALID_NEXUS_REGISTRY_REQUEST", "ENTITY_NOT_FOUND", "INVALID_AZURE_CONTAINER_REGISTRY_REQUEST", "AZURE_AUTHENTICATION_ERROR", "AZURE_CONFIG_ERROR", "DATA_PROCESSING_ERROR", "INVALID_AZURE_AKS_REQUEST", "AWS_IAM_ERROR", "AWS_CF_ERROR", "AWS_INSTANCE_ERROR", "AWS_VPC_ERROR", "AWS_TAG_ERROR", "AWS_ASG_ERROR", "AWS_LOAD_BALANCER_ERROR", "SCM_INTERNAL_SERVER_ERROR_V2", "SCM_UNAUTHORIZED_ERROR_V2", "TOO_MANY_REQUESTS", "INVALID_IDENTIFIER_REF", "SPOTINST_NULL_ERROR", "SPOTNIST_REST_EXCEPTION", "SCM_UNEXPECTED_ERROR", "DUPLICATE_FILE_IMPORT", "AZURE_APP_SERVICES_TASK_EXCEPTION", "AZURE_ARM_TASK_EXCEPTION", "AZURE_BP_TASK_EXCEPTION", "MEDIA_NOT_SUPPORTED", "AWS_ECS_ERROR", "AWS_APPLICATION_AUTO_SCALING", "AWS_ECS_SERVICE_NOT_ACTIVE", "AWS_ECS_CLIENT_ERROR", "AWS_STS_ERROR", "FREEZE_EXCEPTION", "MISSING_EXCEPTION", "DELEGATE_TASK_EXPIRED", "DELEGATE_TASK_VALIDATION_FAILED", "MONGO_EXECUTION_TIMEOUT_EXCEPTION", "DELEGATE_NOT_REGISTERED", "TERRAFORM_VAULT_SECRET_CLEANUP_FAILURE", "APPROVAL_REJECTION", "TERRAGRUNT_EXECUTION_ERROR", "ADFS_ERROR", "TERRAFORM_CLOUD_ERROR", "CLUSTER_CREDENTIALS_NOT_FOUND", "SCM_API_ERROR", "INTERNAL_SERVER_ERROR", "SCM_FORBIDDEN", "AWS_EKS_ERROR", "OPA_POLICY_EVALUATION_ERROR", "USER_MARKED_FAILURE", "SSH_RETRY", "HTTP_CLIENT_ERROR_RESPONSE", "HTTP_INTERNAL_SERVER_ERROR", "HTTP_BAD_GATEWAY", "HTTP_SERVICE_UNAVAILABLE", "HTTP_GATEWAY_TIMEOUT", "HTTP_SERVER_ERROR_RESPONSE", "PIPELINE_UPDATE_EXCEPTION", "SERVICENOW_REFRESH_TOKEN_ERROR", "PARAMETER_FIELD_CAST_ERROR", "ABORT_ALL_ALREADY_NG"]  # noqa: E501
        if code not in allowed_values:
            raise ValueError(
                "Invalid value for `code` ({0}), must be one of {1}"  # noqa: E501
                .format(code, allowed_values)
            )

        self._code = code

    @property
    def message(self):
        """Gets the message of this CvError.  # noqa: E501


        :return: The message of this CvError.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this CvError.


        :param message: The message of this CvError.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def correlation_id(self):
        """Gets the correlation_id of this CvError.  # noqa: E501


        :return: The correlation_id of this CvError.  # noqa: E501
        :rtype: str
        """
        return self._correlation_id

    @correlation_id.setter
    def correlation_id(self, correlation_id):
        """Sets the correlation_id of this CvError.


        :param correlation_id: The correlation_id of this CvError.  # noqa: E501
        :type: str
        """

        self._correlation_id = correlation_id

    @property
    def detailed_message(self):
        """Gets the detailed_message of this CvError.  # noqa: E501


        :return: The detailed_message of this CvError.  # noqa: E501
        :rtype: str
        """
        return self._detailed_message

    @detailed_message.setter
    def detailed_message(self, detailed_message):
        """Sets the detailed_message of this CvError.


        :param detailed_message: The detailed_message of this CvError.  # noqa: E501
        :type: str
        """

        self._detailed_message = detailed_message

    @property
    def response_messages(self):
        """Gets the response_messages of this CvError.  # noqa: E501


        :return: The response_messages of this CvError.  # noqa: E501
        :rtype: list[CvResponseMessage]
        """
        return self._response_messages

    @response_messages.setter
    def response_messages(self, response_messages):
        """Sets the response_messages of this CvError.


        :param response_messages: The response_messages of this CvError.  # noqa: E501
        :type: list[CvResponseMessage]
        """

        self._response_messages = response_messages

    @property
    def metadata(self):
        """Gets the metadata of this CvError.  # noqa: E501


        :return: The metadata of this CvError.  # noqa: E501
        :rtype: CvErrorMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this CvError.


        :param metadata: The metadata of this CvError.  # noqa: E501
        :type: CvErrorMetadata
        """

        self._metadata = metadata

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
        if issubclass(CvError, dict):
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
        if not isinstance(other, CvError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
