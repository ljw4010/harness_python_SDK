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

class EntityDetailProtoDTO(object):
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
        'unknown_fields': 'UnknownFieldSet',
        'name': 'str',
        'type': 'str',
        'name_bytes': 'ByteString',
        'entity_git_metadata': 'EntityGitMetadata',
        'initialized': 'bool',
        'identifier_ref': 'IdentifierRefProtoDTO',
        'identifier_ref_or_builder': 'IdentifierRefProtoDTOOrBuilder',
        'input_set_ref_or_builder': 'InputSetReferenceProtoDTOOrBuilder',
        'template_ref_or_builder': 'TemplateReferenceProtoDTOOrBuilder',
        'type_value': 'int',
        'infra_def_ref_or_builder': 'InfraDefinitionReferenceProtoDTOOrBuilder',
        'trigger_ref_or_builder': 'TriggerReferenceProtoDTOOrBuilder',
        'entity_git_metadata_or_builder': 'EntityGitMetadataOrBuilder',
        'entity_ref_case': 'str',
        'input_set_ref': 'InputSetReferenceProtoDTO',
        'infra_def_ref': 'InfraDefinitionReferenceProtoDTO',
        'trigger_ref': 'TriggerReferenceProtoDTO',
        'template_ref': 'TemplateReferenceProtoDTO',
        'serialized_size': 'int',
        'parser_for_type': 'ParserEntityDetailProtoDTO',
        'default_instance_for_type': 'EntityDetailProtoDTO',
        'all_fields': 'dict(str, object)',
        'initialization_error_string': 'str',
        'descriptor_for_type': 'Descriptor',
        'memoized_serialized_size': 'int'
    }

    attribute_map = {
        'unknown_fields': 'unknownFields',
        'name': 'name',
        'type': 'type',
        'name_bytes': 'nameBytes',
        'entity_git_metadata': 'entityGitMetadata',
        'initialized': 'initialized',
        'identifier_ref': 'identifierRef',
        'identifier_ref_or_builder': 'identifierRefOrBuilder',
        'input_set_ref_or_builder': 'inputSetRefOrBuilder',
        'template_ref_or_builder': 'templateRefOrBuilder',
        'type_value': 'typeValue',
        'infra_def_ref_or_builder': 'infraDefRefOrBuilder',
        'trigger_ref_or_builder': 'triggerRefOrBuilder',
        'entity_git_metadata_or_builder': 'entityGitMetadataOrBuilder',
        'entity_ref_case': 'entityRefCase',
        'input_set_ref': 'inputSetRef',
        'infra_def_ref': 'infraDefRef',
        'trigger_ref': 'triggerRef',
        'template_ref': 'templateRef',
        'serialized_size': 'serializedSize',
        'parser_for_type': 'parserForType',
        'default_instance_for_type': 'defaultInstanceForType',
        'all_fields': 'allFields',
        'initialization_error_string': 'initializationErrorString',
        'descriptor_for_type': 'descriptorForType',
        'memoized_serialized_size': 'memoizedSerializedSize'
    }

    def __init__(self, unknown_fields=None, name=None, type=None, name_bytes=None, entity_git_metadata=None, initialized=None, identifier_ref=None, identifier_ref_or_builder=None, input_set_ref_or_builder=None, template_ref_or_builder=None, type_value=None, infra_def_ref_or_builder=None, trigger_ref_or_builder=None, entity_git_metadata_or_builder=None, entity_ref_case=None, input_set_ref=None, infra_def_ref=None, trigger_ref=None, template_ref=None, serialized_size=None, parser_for_type=None, default_instance_for_type=None, all_fields=None, initialization_error_string=None, descriptor_for_type=None, memoized_serialized_size=None):  # noqa: E501
        """EntityDetailProtoDTO - a model defined in Swagger"""  # noqa: E501
        self._unknown_fields = None
        self._name = None
        self._type = None
        self._name_bytes = None
        self._entity_git_metadata = None
        self._initialized = None
        self._identifier_ref = None
        self._identifier_ref_or_builder = None
        self._input_set_ref_or_builder = None
        self._template_ref_or_builder = None
        self._type_value = None
        self._infra_def_ref_or_builder = None
        self._trigger_ref_or_builder = None
        self._entity_git_metadata_or_builder = None
        self._entity_ref_case = None
        self._input_set_ref = None
        self._infra_def_ref = None
        self._trigger_ref = None
        self._template_ref = None
        self._serialized_size = None
        self._parser_for_type = None
        self._default_instance_for_type = None
        self._all_fields = None
        self._initialization_error_string = None
        self._descriptor_for_type = None
        self._memoized_serialized_size = None
        self.discriminator = None
        if unknown_fields is not None:
            self.unknown_fields = unknown_fields
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if name_bytes is not None:
            self.name_bytes = name_bytes
        if entity_git_metadata is not None:
            self.entity_git_metadata = entity_git_metadata
        if initialized is not None:
            self.initialized = initialized
        if identifier_ref is not None:
            self.identifier_ref = identifier_ref
        if identifier_ref_or_builder is not None:
            self.identifier_ref_or_builder = identifier_ref_or_builder
        if input_set_ref_or_builder is not None:
            self.input_set_ref_or_builder = input_set_ref_or_builder
        if template_ref_or_builder is not None:
            self.template_ref_or_builder = template_ref_or_builder
        if type_value is not None:
            self.type_value = type_value
        if infra_def_ref_or_builder is not None:
            self.infra_def_ref_or_builder = infra_def_ref_or_builder
        if trigger_ref_or_builder is not None:
            self.trigger_ref_or_builder = trigger_ref_or_builder
        if entity_git_metadata_or_builder is not None:
            self.entity_git_metadata_or_builder = entity_git_metadata_or_builder
        if entity_ref_case is not None:
            self.entity_ref_case = entity_ref_case
        if input_set_ref is not None:
            self.input_set_ref = input_set_ref
        if infra_def_ref is not None:
            self.infra_def_ref = infra_def_ref
        if trigger_ref is not None:
            self.trigger_ref = trigger_ref
        if template_ref is not None:
            self.template_ref = template_ref
        if serialized_size is not None:
            self.serialized_size = serialized_size
        if parser_for_type is not None:
            self.parser_for_type = parser_for_type
        if default_instance_for_type is not None:
            self.default_instance_for_type = default_instance_for_type
        if all_fields is not None:
            self.all_fields = all_fields
        if initialization_error_string is not None:
            self.initialization_error_string = initialization_error_string
        if descriptor_for_type is not None:
            self.descriptor_for_type = descriptor_for_type
        if memoized_serialized_size is not None:
            self.memoized_serialized_size = memoized_serialized_size

    @property
    def unknown_fields(self):
        """Gets the unknown_fields of this EntityDetailProtoDTO.  # noqa: E501


        :return: The unknown_fields of this EntityDetailProtoDTO.  # noqa: E501
        :rtype: UnknownFieldSet
        """
        return self._unknown_fields

    @unknown_fields.setter
    def unknown_fields(self, unknown_fields):
        """Sets the unknown_fields of this EntityDetailProtoDTO.


        :param unknown_fields: The unknown_fields of this EntityDetailProtoDTO.  # noqa: E501
        :type: UnknownFieldSet
        """

        self._unknown_fields = unknown_fields

    @property
    def name(self):
        """Gets the name of this EntityDetailProtoDTO.  # noqa: E501


        :return: The name of this EntityDetailProtoDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EntityDetailProtoDTO.


        :param name: The name of this EntityDetailProtoDTO.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this EntityDetailProtoDTO.  # noqa: E501


        :return: The type of this EntityDetailProtoDTO.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EntityDetailProtoDTO.


        :param type: The type of this EntityDetailProtoDTO.  # noqa: E501
        :type: str
        """
        allowed_values = ["PROJECTS", "PIPELINES", "CONNECTORS", "SECRETS", "SERVICE", "ENVIRONMENT", "INPUT_SETS", "CV_CONFIG", "DELEGATES", "DELEGATE_CONFIGURATIONS", "CV_VERIFICATION_JOB", "CV_KUBERNETES_ACTIVITY_SOURCE", "INTEGRATION_STEPS", "INTEGRATION_STAGE", "DEPLOYMENT_STAGE", "DEPLOYMENT_STEPS", "PIPELINE_STEPS", "APPROVAL_STAGE", "TRIGGERS", "FEATURE_FLAG_STAGE", "MONITORED_SERVICE", "TEMPLATE", "GIT_REPOSITORIES", "FEATURE_FLAGS", "HTTP_STEP", "SHELL_SCRIPT_STEP", "K8S_CANARY_DEPLOY_STEP", "JIRA_CREATE_STEP", "SERVICENOW_APPROVAL_STEP", "JIRA_UPDATE_STEP", "JIRA_APPROVAL_STEP", "HARNESS_APPROVAL_STEP", "BARRIER_STEP", "VERIFY_STEP", "OPAPOLICIES", "POLICY_STEP", "ARTIFACTORY_UPLOAD", "GCS_UPLOAD", "S3_UPLOAD", "BUILD_AND_PUSH_GCR", "BUILD_AND_PUSH_ECR", "BUILD_AND_PUSH_DOCKER_REGISTRY", "RUN_STEP", "RUN_TEST", "PLUGIN", "RESTORE_CACHE_GCS", "RESTORE_CACHE_S3", "SAVE_CACHE_GCS", "SAVE_CACHE_S3", "FLAG_CONFIGURATION", "SECURITY", "K8S_APPLY_STEP", "K8S_BLUE_GREEN_DEPLOY_STEP", "K8S_ROLLING_DEPLOY_STEP", "K8S_ROLLING_ROLLBACK_STEP", "K8S_SCALE_STEP", "K8S_DELETE_STEP", "K8S_BG_SWAP_SERVICES_STEP", "K8S_CANARY_DELETE_STEP", "TERRAFORM_APPLY_STEP", "TERRAFORM_PLAN_STEP", "TERRAFORM_DESTROY_STEP", "TERRAFORM_ROLLBACK_STEP", "HELM_DEPLOY_STEP", "HELM_ROLLBACK_STEP", "SERVICENOW_CREATE_STEP", "SERVICENOW_UPDATE_STEP", "ENVIRONMENT_GROUP", "SECURITY_STAGE", "SECURITY_STEPS", "FILES", "SERVERLESS_AWS_LAMBDA_DEPLOY_STEP", "SERVERLESS_AWS_LAMBDA_ROLLBACK_STEP", "CUSTOM_STAGE", "CLOUDFORMATION_CREATE_STACK_STEP", "CLOUDFORMATION_DELETE_STACK_STEP", "CLOUDFORMATION_ROLLBACK_STACK_STEP", "INFRASTRUCTURE", "GITOPS_CREATE_PR", "COMMAND_STEP", "STRATEGY_NODE", "AZURE_SLOT_DEPLOYMENT_STEP", "AZURE_TRAFFIC_SHIFT_STEP", "AZURE_SWAP_SLOT_STEP", "AZURE_WEBAPP_ROLLBACK_STEP", "GITOPS_MERGE_PR", "QUEUE_STEP", "CUSTOM_APPROVAL_STEP", "JENKINS_BUILD", "TEMPLATE_STAGE", "EMAIL_STEP", "BUILD_AND_PUSH_ACR", "AZURE_CREATE_ARM_RESOURCE_STEP", "GIT_CLONE", "AZURE_CREATE_BP_RESOURCE_STEP", "AZURE_ROLLBACK_ARM_RESOURCE_STEP", "BACKGROUND_STEP", "ECS_ROLLING_DEPLOY_STEP", "ECS_ROLLING_ROLLBACK_STEP", "ECS_CANARY_DEPLOY_STEP", "ECS_CANARY_DELETE_STEP", "TEMPLATE_CUSTOM_DEPLOYMENT", "WAIT_STEP", "ARTIFACT_SOURCE_TEMPLATE", "ECS_BLUE_GREEN_CREATE_SERVICE_STEP", "ECS_BLUE_GREEN_SWAP_TARGET_GROUPS_STEP", "ECS_BLUE_GREEN_ROLLBACK_STEP", "FETCH_INSTANCE_SCRIPT_STEP", "PIPELINE_STAGE", "SHELL_SCRIPT_PROVISION_STEP", "SERVICENOW_IMPORT_SET_STEP", "GITOPS_UPDATE_RELEASE_REPO", "FREEZE", "ECS_RUN_TASK_STEP", "CHAOS_STEP", "ELASTIGROUP_DEPLOY_STEP", "ELASTIGROUP_ROLLBACK_STEP", "ACTION_STEP", "AWS_ECR", "BANDIT", "BLACKDUCK", "BRAKEMAN", "BURP", "CHECKMARX", "CLAIR", "DATA_THEOREM", "DOCKER_CONTENT_TRUST", "EXTERNAL", "FORTIFY_ON_DEMAND", "GRYPE", "JFROG_XRAY", "MEND", "METASPLOIT", "NESSUS", "NEXUS_IQ", "NIKTO", "NMAP", "OPENVAS", "OWASP", "PRISMA_CLOUD", "PROWLER", "QUALYS", "REAPSAW", "SHIFT_LEFT", "SNIPER", "SNYK", "SONARQUBE", "SYSDIG", "TENABLE", "VERACODE", "ZAP", "AQUA_TRIVY", "ELASTIGROUP_SETUP_STEP", "BITRISE_STEP", "GITOPS_FETCH_LINKED_APPS", "TERRAGRUNT_PLAN_STEP", "TERRAGRUNT_APPLY_STEP", "TERRAGRUNT_DESTROY_STEP", "TERRAGRUNT_ROLLBACK_STEP", "IACM", "IACM_STAGE", "IACM_STEPS", "CONTAINER_STEP", "ASG_CANARY_DEPLOY_STEP", "ELASTIGROUP_BG_STAGE_SETUP_STEP", "ELASTIGROUP_SWAP_ROUTE_STEP", "ASG_CANARY_DELETE_STEP", "TAS_CANARY_APP_SETUP_STEP", "TAS_BG_APP_SETUP_STEP", "TAS_BASIC_APP_SETUP_STEP", "TANZU_COMMAND_STEP", "IACM_TERRAFORM_PLUGIN", "TAS_APP_RESIZE_STEP", "TAS_ROLLBACK_STEP", "TAS_SWAP_ROUTES_STEP", "TAS_SWAP_ROLLBACK_STEP", "ASG_ROLLING_DEPLOY_STEP", "ASG_ROLLING_ROLLBACK_STEP", "IACM_APPROVAL", "CCM_GOVERNANCE_RULE_AWS", "TAS_ROLLING_DEPLOY", "TAS_ROLLING_ROLLBACK", "K8S_DRY_RUN_MANIFEST_STEP", "ASG_BLUE_GREEN_SWAP_SERVICE_STEP", "ASG_BLUE_GREEN_DEPLOY_STEP", "ASG_BLUE_GREEN_ROLLBACK_STEP", "TERRAFORM_CLOUD_RUN", "GOOGLE_CLOUD_FUNCTIONS_DEPLOY", "GOOGLE_CLOUD_FUNCTIONS_DEPLOY_WITHOUT_TRAFFIC", "GOOGLE_CLOUD_FUNCTIONS_TRAFFIC_SHIFT", "GOOGLE_CLOUD_FUNCTIONS_ROLLBACK", "AWS_LAMBDA_DEPLOY", "TERRAFORM_CLOUD_ROLLBACK", "AWS_SAM_DEPLOY", "AWS_SAM_ROLLBACK", "SSCA_ORCHESTRATION", "AWS_LAMBDA_ROLLBACK", "GITOPS_SYNC", "BAMBOO_BUILD", "CD_SSCA_ORCHESTRATION", "TAS_ROUTE_MAPPING", "AWS_SECURITY_HUB", "CUSTOM_INGEST", "BACKSTAGE_ENVIRONMENT_VARIABLE", "CODEQL", "FOSSA", "GIT_LEAKS", "GOOGLE_CLOUD_FUNCTIONS_GEN_ONE_DEPLOY", "GOOGLE_CLOUD_FUNCTIONS_GEN_ONE_ROLLBACK", "K8S_BLUE_GREEN_STAGE_SCALE_DOWN", "AWS_SAM_BUILD", "SEMGREP", "SSCA_ENFORCEMENT", "IDP_CONNECTOR", "CD_SSCA_ENFORCEMENT", "DOWNLOAD_MANIFESTS", "SERVERLESS_AWS_LAMBDA_PREPARE_ROLLBACK_V2", "SERVERLESS_AWS_LAMBDA_ROLLBACK_V2", "COVERITY", "SERVERLESS_AWS_LAMBDA_DEPLOY_V2", "ANALYZE_DEPLOYMENT_IMPACT_STEP", "SERVERLESS_AWS_LAMBDA_PACKAGE_V2", "GITOPS_REVERT_PR", "AWS_CDK_BOOTSTRAP", "AWS_CDK_SYNTH", "AWS_CDK_DIFF", "AWS_CDK_DEPLOY", "AWS_CDK_DESTROY", "IDP_SCORECARD", "IDP_CHECK", "AWS_CDK_ROLLBACK", "SLSA_VERIFICATION", "UPDATE_GITOPS_APP", "ECS_SERVICE_SETUP_STEP", "ECS_UPGRADE_CONTAINER_STEP", "ECS_BASIC_ROLLBACK_STEP", "CHAOS_INFRASTRUCTURE", "BUILD_AND_PUSH_GAR", "ANCHORE", "OVERRIDES", "ASG_SHIFT_TRAFFIC_STEP", "AQUA_SECURITY", "IDP_STAGE", "CHAOS_HUB", "IDP_COOKIECUTTER", "IDP_CREATE_REPO", "UNRECOGNIZED"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def name_bytes(self):
        """Gets the name_bytes of this EntityDetailProtoDTO.  # noqa: E501


        :return: The name_bytes of this EntityDetailProtoDTO.  # noqa: E501
        :rtype: ByteString
        """
        return self._name_bytes

    @name_bytes.setter
    def name_bytes(self, name_bytes):
        """Sets the name_bytes of this EntityDetailProtoDTO.


        :param name_bytes: The name_bytes of this EntityDetailProtoDTO.  # noqa: E501
        :type: ByteString
        """

        self._name_bytes = name_bytes

    @property
    def entity_git_metadata(self):
        """Gets the entity_git_metadata of this EntityDetailProtoDTO.  # noqa: E501


        :return: The entity_git_metadata of this EntityDetailProtoDTO.  # noqa: E501
        :rtype: EntityGitMetadata
        """
        return self._entity_git_metadata

    @entity_git_metadata.setter
    def entity_git_metadata(self, entity_git_metadata):
        """Sets the entity_git_metadata of this EntityDetailProtoDTO.


        :param entity_git_metadata: The entity_git_metadata of this EntityDetailProtoDTO.  # noqa: E501
        :type: EntityGitMetadata
        """

        self._entity_git_metadata = entity_git_metadata

    @property
    def initialized(self):
        """Gets the initialized of this EntityDetailProtoDTO.  # noqa: E501


        :return: The initialized of this EntityDetailProtoDTO.  # noqa: E501
        :rtype: bool
        """
        return self._initialized

    @initialized.setter
    def initialized(self, initialized):
        """Sets the initialized of this EntityDetailProtoDTO.


        :param initialized: The initialized of this EntityDetailProtoDTO.  # noqa: E501
        :type: bool
        """

        self._initialized = initialized

    @property
    def identifier_ref(self):
        """Gets the identifier_ref of this EntityDetailProtoDTO.  # noqa: E501


        :return: The identifier_ref of this EntityDetailProtoDTO.  # noqa: E501
        :rtype: IdentifierRefProtoDTO
        """
        return self._identifier_ref

    @identifier_ref.setter
    def identifier_ref(self, identifier_ref):
        """Sets the identifier_ref of this EntityDetailProtoDTO.


        :param identifier_ref: The identifier_ref of this EntityDetailProtoDTO.  # noqa: E501
        :type: IdentifierRefProtoDTO
        """

        self._identifier_ref = identifier_ref

    @property
    def identifier_ref_or_builder(self):
        """Gets the identifier_ref_or_builder of this EntityDetailProtoDTO.  # noqa: E501


        :return: The identifier_ref_or_builder of this EntityDetailProtoDTO.  # noqa: E501
        :rtype: IdentifierRefProtoDTOOrBuilder
        """
        return self._identifier_ref_or_builder

    @identifier_ref_or_builder.setter
    def identifier_ref_or_builder(self, identifier_ref_or_builder):
        """Sets the identifier_ref_or_builder of this EntityDetailProtoDTO.


        :param identifier_ref_or_builder: The identifier_ref_or_builder of this EntityDetailProtoDTO.  # noqa: E501
        :type: IdentifierRefProtoDTOOrBuilder
        """

        self._identifier_ref_or_builder = identifier_ref_or_builder

    @property
    def input_set_ref_or_builder(self):
        """Gets the input_set_ref_or_builder of this EntityDetailProtoDTO.  # noqa: E501


        :return: The input_set_ref_or_builder of this EntityDetailProtoDTO.  # noqa: E501
        :rtype: InputSetReferenceProtoDTOOrBuilder
        """
        return self._input_set_ref_or_builder

    @input_set_ref_or_builder.setter
    def input_set_ref_or_builder(self, input_set_ref_or_builder):
        """Sets the input_set_ref_or_builder of this EntityDetailProtoDTO.


        :param input_set_ref_or_builder: The input_set_ref_or_builder of this EntityDetailProtoDTO.  # noqa: E501
        :type: InputSetReferenceProtoDTOOrBuilder
        """

        self._input_set_ref_or_builder = input_set_ref_or_builder

    @property
    def template_ref_or_builder(self):
        """Gets the template_ref_or_builder of this EntityDetailProtoDTO.  # noqa: E501


        :return: The template_ref_or_builder of this EntityDetailProtoDTO.  # noqa: E501
        :rtype: TemplateReferenceProtoDTOOrBuilder
        """
        return self._template_ref_or_builder

    @template_ref_or_builder.setter
    def template_ref_or_builder(self, template_ref_or_builder):
        """Sets the template_ref_or_builder of this EntityDetailProtoDTO.


        :param template_ref_or_builder: The template_ref_or_builder of this EntityDetailProtoDTO.  # noqa: E501
        :type: TemplateReferenceProtoDTOOrBuilder
        """

        self._template_ref_or_builder = template_ref_or_builder

    @property
    def type_value(self):
        """Gets the type_value of this EntityDetailProtoDTO.  # noqa: E501


        :return: The type_value of this EntityDetailProtoDTO.  # noqa: E501
        :rtype: int
        """
        return self._type_value

    @type_value.setter
    def type_value(self, type_value):
        """Sets the type_value of this EntityDetailProtoDTO.


        :param type_value: The type_value of this EntityDetailProtoDTO.  # noqa: E501
        :type: int
        """

        self._type_value = type_value

    @property
    def infra_def_ref_or_builder(self):
        """Gets the infra_def_ref_or_builder of this EntityDetailProtoDTO.  # noqa: E501


        :return: The infra_def_ref_or_builder of this EntityDetailProtoDTO.  # noqa: E501
        :rtype: InfraDefinitionReferenceProtoDTOOrBuilder
        """
        return self._infra_def_ref_or_builder

    @infra_def_ref_or_builder.setter
    def infra_def_ref_or_builder(self, infra_def_ref_or_builder):
        """Sets the infra_def_ref_or_builder of this EntityDetailProtoDTO.


        :param infra_def_ref_or_builder: The infra_def_ref_or_builder of this EntityDetailProtoDTO.  # noqa: E501
        :type: InfraDefinitionReferenceProtoDTOOrBuilder
        """

        self._infra_def_ref_or_builder = infra_def_ref_or_builder

    @property
    def trigger_ref_or_builder(self):
        """Gets the trigger_ref_or_builder of this EntityDetailProtoDTO.  # noqa: E501


        :return: The trigger_ref_or_builder of this EntityDetailProtoDTO.  # noqa: E501
        :rtype: TriggerReferenceProtoDTOOrBuilder
        """
        return self._trigger_ref_or_builder

    @trigger_ref_or_builder.setter
    def trigger_ref_or_builder(self, trigger_ref_or_builder):
        """Sets the trigger_ref_or_builder of this EntityDetailProtoDTO.


        :param trigger_ref_or_builder: The trigger_ref_or_builder of this EntityDetailProtoDTO.  # noqa: E501
        :type: TriggerReferenceProtoDTOOrBuilder
        """

        self._trigger_ref_or_builder = trigger_ref_or_builder

    @property
    def entity_git_metadata_or_builder(self):
        """Gets the entity_git_metadata_or_builder of this EntityDetailProtoDTO.  # noqa: E501


        :return: The entity_git_metadata_or_builder of this EntityDetailProtoDTO.  # noqa: E501
        :rtype: EntityGitMetadataOrBuilder
        """
        return self._entity_git_metadata_or_builder

    @entity_git_metadata_or_builder.setter
    def entity_git_metadata_or_builder(self, entity_git_metadata_or_builder):
        """Sets the entity_git_metadata_or_builder of this EntityDetailProtoDTO.


        :param entity_git_metadata_or_builder: The entity_git_metadata_or_builder of this EntityDetailProtoDTO.  # noqa: E501
        :type: EntityGitMetadataOrBuilder
        """

        self._entity_git_metadata_or_builder = entity_git_metadata_or_builder

    @property
    def entity_ref_case(self):
        """Gets the entity_ref_case of this EntityDetailProtoDTO.  # noqa: E501


        :return: The entity_ref_case of this EntityDetailProtoDTO.  # noqa: E501
        :rtype: str
        """
        return self._entity_ref_case

    @entity_ref_case.setter
    def entity_ref_case(self, entity_ref_case):
        """Sets the entity_ref_case of this EntityDetailProtoDTO.


        :param entity_ref_case: The entity_ref_case of this EntityDetailProtoDTO.  # noqa: E501
        :type: str
        """
        allowed_values = ["IDENTIFIERREF", "INPUTSETREF", "TEMPLATEREF", "INFRADEFREF", "TRIGGERREF", "ENTITYREF_NOT_SET"]  # noqa: E501
        if entity_ref_case not in allowed_values:
            raise ValueError(
                "Invalid value for `entity_ref_case` ({0}), must be one of {1}"  # noqa: E501
                .format(entity_ref_case, allowed_values)
            )

        self._entity_ref_case = entity_ref_case

    @property
    def input_set_ref(self):
        """Gets the input_set_ref of this EntityDetailProtoDTO.  # noqa: E501


        :return: The input_set_ref of this EntityDetailProtoDTO.  # noqa: E501
        :rtype: InputSetReferenceProtoDTO
        """
        return self._input_set_ref

    @input_set_ref.setter
    def input_set_ref(self, input_set_ref):
        """Sets the input_set_ref of this EntityDetailProtoDTO.


        :param input_set_ref: The input_set_ref of this EntityDetailProtoDTO.  # noqa: E501
        :type: InputSetReferenceProtoDTO
        """

        self._input_set_ref = input_set_ref

    @property
    def infra_def_ref(self):
        """Gets the infra_def_ref of this EntityDetailProtoDTO.  # noqa: E501


        :return: The infra_def_ref of this EntityDetailProtoDTO.  # noqa: E501
        :rtype: InfraDefinitionReferenceProtoDTO
        """
        return self._infra_def_ref

    @infra_def_ref.setter
    def infra_def_ref(self, infra_def_ref):
        """Sets the infra_def_ref of this EntityDetailProtoDTO.


        :param infra_def_ref: The infra_def_ref of this EntityDetailProtoDTO.  # noqa: E501
        :type: InfraDefinitionReferenceProtoDTO
        """

        self._infra_def_ref = infra_def_ref

    @property
    def trigger_ref(self):
        """Gets the trigger_ref of this EntityDetailProtoDTO.  # noqa: E501


        :return: The trigger_ref of this EntityDetailProtoDTO.  # noqa: E501
        :rtype: TriggerReferenceProtoDTO
        """
        return self._trigger_ref

    @trigger_ref.setter
    def trigger_ref(self, trigger_ref):
        """Sets the trigger_ref of this EntityDetailProtoDTO.


        :param trigger_ref: The trigger_ref of this EntityDetailProtoDTO.  # noqa: E501
        :type: TriggerReferenceProtoDTO
        """

        self._trigger_ref = trigger_ref

    @property
    def template_ref(self):
        """Gets the template_ref of this EntityDetailProtoDTO.  # noqa: E501


        :return: The template_ref of this EntityDetailProtoDTO.  # noqa: E501
        :rtype: TemplateReferenceProtoDTO
        """
        return self._template_ref

    @template_ref.setter
    def template_ref(self, template_ref):
        """Sets the template_ref of this EntityDetailProtoDTO.


        :param template_ref: The template_ref of this EntityDetailProtoDTO.  # noqa: E501
        :type: TemplateReferenceProtoDTO
        """

        self._template_ref = template_ref

    @property
    def serialized_size(self):
        """Gets the serialized_size of this EntityDetailProtoDTO.  # noqa: E501


        :return: The serialized_size of this EntityDetailProtoDTO.  # noqa: E501
        :rtype: int
        """
        return self._serialized_size

    @serialized_size.setter
    def serialized_size(self, serialized_size):
        """Sets the serialized_size of this EntityDetailProtoDTO.


        :param serialized_size: The serialized_size of this EntityDetailProtoDTO.  # noqa: E501
        :type: int
        """

        self._serialized_size = serialized_size

    @property
    def parser_for_type(self):
        """Gets the parser_for_type of this EntityDetailProtoDTO.  # noqa: E501


        :return: The parser_for_type of this EntityDetailProtoDTO.  # noqa: E501
        :rtype: ParserEntityDetailProtoDTO
        """
        return self._parser_for_type

    @parser_for_type.setter
    def parser_for_type(self, parser_for_type):
        """Sets the parser_for_type of this EntityDetailProtoDTO.


        :param parser_for_type: The parser_for_type of this EntityDetailProtoDTO.  # noqa: E501
        :type: ParserEntityDetailProtoDTO
        """

        self._parser_for_type = parser_for_type

    @property
    def default_instance_for_type(self):
        """Gets the default_instance_for_type of this EntityDetailProtoDTO.  # noqa: E501


        :return: The default_instance_for_type of this EntityDetailProtoDTO.  # noqa: E501
        :rtype: EntityDetailProtoDTO
        """
        return self._default_instance_for_type

    @default_instance_for_type.setter
    def default_instance_for_type(self, default_instance_for_type):
        """Sets the default_instance_for_type of this EntityDetailProtoDTO.


        :param default_instance_for_type: The default_instance_for_type of this EntityDetailProtoDTO.  # noqa: E501
        :type: EntityDetailProtoDTO
        """

        self._default_instance_for_type = default_instance_for_type

    @property
    def all_fields(self):
        """Gets the all_fields of this EntityDetailProtoDTO.  # noqa: E501


        :return: The all_fields of this EntityDetailProtoDTO.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._all_fields

    @all_fields.setter
    def all_fields(self, all_fields):
        """Sets the all_fields of this EntityDetailProtoDTO.


        :param all_fields: The all_fields of this EntityDetailProtoDTO.  # noqa: E501
        :type: dict(str, object)
        """

        self._all_fields = all_fields

    @property
    def initialization_error_string(self):
        """Gets the initialization_error_string of this EntityDetailProtoDTO.  # noqa: E501


        :return: The initialization_error_string of this EntityDetailProtoDTO.  # noqa: E501
        :rtype: str
        """
        return self._initialization_error_string

    @initialization_error_string.setter
    def initialization_error_string(self, initialization_error_string):
        """Sets the initialization_error_string of this EntityDetailProtoDTO.


        :param initialization_error_string: The initialization_error_string of this EntityDetailProtoDTO.  # noqa: E501
        :type: str
        """

        self._initialization_error_string = initialization_error_string

    @property
    def descriptor_for_type(self):
        """Gets the descriptor_for_type of this EntityDetailProtoDTO.  # noqa: E501


        :return: The descriptor_for_type of this EntityDetailProtoDTO.  # noqa: E501
        :rtype: Descriptor
        """
        return self._descriptor_for_type

    @descriptor_for_type.setter
    def descriptor_for_type(self, descriptor_for_type):
        """Sets the descriptor_for_type of this EntityDetailProtoDTO.


        :param descriptor_for_type: The descriptor_for_type of this EntityDetailProtoDTO.  # noqa: E501
        :type: Descriptor
        """

        self._descriptor_for_type = descriptor_for_type

    @property
    def memoized_serialized_size(self):
        """Gets the memoized_serialized_size of this EntityDetailProtoDTO.  # noqa: E501


        :return: The memoized_serialized_size of this EntityDetailProtoDTO.  # noqa: E501
        :rtype: int
        """
        return self._memoized_serialized_size

    @memoized_serialized_size.setter
    def memoized_serialized_size(self, memoized_serialized_size):
        """Sets the memoized_serialized_size of this EntityDetailProtoDTO.


        :param memoized_serialized_size: The memoized_serialized_size of this EntityDetailProtoDTO.  # noqa: E501
        :type: int
        """

        self._memoized_serialized_size = memoized_serialized_size

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
        if issubclass(EntityDetailProtoDTO, dict):
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
        if not isinstance(other, EntityDetailProtoDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
