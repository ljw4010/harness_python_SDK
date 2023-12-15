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

class GitSyncError(object):
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
        'repo_url': 'str',
        'repo_id': 'str',
        'branch_name': 'str',
        'scopes': 'list[Scope1]',
        'change_type': 'str',
        'complete_file_path': 'str',
        'entity_type': 'str',
        'failure_reason': 'str',
        'status': 'str',
        'error_type': 'str',
        'additional_error_details': 'GitSyncErrorDetails',
        'created_at': 'int'
    }

    attribute_map = {
        'account_identifier': 'accountIdentifier',
        'repo_url': 'repoUrl',
        'repo_id': 'repoId',
        'branch_name': 'branchName',
        'scopes': 'scopes',
        'change_type': 'changeType',
        'complete_file_path': 'completeFilePath',
        'entity_type': 'entityType',
        'failure_reason': 'failureReason',
        'status': 'status',
        'error_type': 'errorType',
        'additional_error_details': 'additionalErrorDetails',
        'created_at': 'createdAt'
    }

    def __init__(self, account_identifier=None, repo_url=None, repo_id=None, branch_name=None, scopes=None, change_type=None, complete_file_path=None, entity_type=None, failure_reason=None, status=None, error_type=None, additional_error_details=None, created_at=None):  # noqa: E501
        """GitSyncError - a model defined in Swagger"""  # noqa: E501
        self._account_identifier = None
        self._repo_url = None
        self._repo_id = None
        self._branch_name = None
        self._scopes = None
        self._change_type = None
        self._complete_file_path = None
        self._entity_type = None
        self._failure_reason = None
        self._status = None
        self._error_type = None
        self._additional_error_details = None
        self._created_at = None
        self.discriminator = None
        if account_identifier is not None:
            self.account_identifier = account_identifier
        if repo_url is not None:
            self.repo_url = repo_url
        if repo_id is not None:
            self.repo_id = repo_id
        if branch_name is not None:
            self.branch_name = branch_name
        if scopes is not None:
            self.scopes = scopes
        if change_type is not None:
            self.change_type = change_type
        if complete_file_path is not None:
            self.complete_file_path = complete_file_path
        if entity_type is not None:
            self.entity_type = entity_type
        if failure_reason is not None:
            self.failure_reason = failure_reason
        if status is not None:
            self.status = status
        if error_type is not None:
            self.error_type = error_type
        if additional_error_details is not None:
            self.additional_error_details = additional_error_details
        if created_at is not None:
            self.created_at = created_at

    @property
    def account_identifier(self):
        """Gets the account_identifier of this GitSyncError.  # noqa: E501

        Account Identifier for the Entity.  # noqa: E501

        :return: The account_identifier of this GitSyncError.  # noqa: E501
        :rtype: str
        """
        return self._account_identifier

    @account_identifier.setter
    def account_identifier(self, account_identifier):
        """Sets the account_identifier of this GitSyncError.

        Account Identifier for the Entity.  # noqa: E501

        :param account_identifier: The account_identifier of this GitSyncError.  # noqa: E501
        :type: str
        """

        self._account_identifier = account_identifier

    @property
    def repo_url(self):
        """Gets the repo_url of this GitSyncError.  # noqa: E501

        URL of the repository.  # noqa: E501

        :return: The repo_url of this GitSyncError.  # noqa: E501
        :rtype: str
        """
        return self._repo_url

    @repo_url.setter
    def repo_url(self, repo_url):
        """Sets the repo_url of this GitSyncError.

        URL of the repository.  # noqa: E501

        :param repo_url: The repo_url of this GitSyncError.  # noqa: E501
        :type: str
        """

        self._repo_url = repo_url

    @property
    def repo_id(self):
        """Gets the repo_id of this GitSyncError.  # noqa: E501

        Git Sync Config Id.  # noqa: E501

        :return: The repo_id of this GitSyncError.  # noqa: E501
        :rtype: str
        """
        return self._repo_id

    @repo_id.setter
    def repo_id(self, repo_id):
        """Sets the repo_id of this GitSyncError.

        Git Sync Config Id.  # noqa: E501

        :param repo_id: The repo_id of this GitSyncError.  # noqa: E501
        :type: str
        """

        self._repo_id = repo_id

    @property
    def branch_name(self):
        """Gets the branch_name of this GitSyncError.  # noqa: E501

        Name of the branch.  # noqa: E501

        :return: The branch_name of this GitSyncError.  # noqa: E501
        :rtype: str
        """
        return self._branch_name

    @branch_name.setter
    def branch_name(self, branch_name):
        """Sets the branch_name of this GitSyncError.

        Name of the branch.  # noqa: E501

        :param branch_name: The branch_name of this GitSyncError.  # noqa: E501
        :type: str
        """

        self._branch_name = branch_name

    @property
    def scopes(self):
        """Gets the scopes of this GitSyncError.  # noqa: E501

        List of scope of the Git Sync Error  # noqa: E501

        :return: The scopes of this GitSyncError.  # noqa: E501
        :rtype: list[Scope1]
        """
        return self._scopes

    @scopes.setter
    def scopes(self, scopes):
        """Sets the scopes of this GitSyncError.

        List of scope of the Git Sync Error  # noqa: E501

        :param scopes: The scopes of this GitSyncError.  # noqa: E501
        :type: list[Scope1]
        """

        self._scopes = scopes

    @property
    def change_type(self):
        """Gets the change_type of this GitSyncError.  # noqa: E501

        Type of operation done in file  # noqa: E501

        :return: The change_type of this GitSyncError.  # noqa: E501
        :rtype: str
        """
        return self._change_type

    @change_type.setter
    def change_type(self, change_type):
        """Sets the change_type of this GitSyncError.

        Type of operation done in file  # noqa: E501

        :param change_type: The change_type of this GitSyncError.  # noqa: E501
        :type: str
        """
        allowed_values = ["ADD", "RENAME", "MODIFY", "DELETE", "NONE", "ADD_V2", "UPDATE_V2"]  # noqa: E501
        if change_type not in allowed_values:
            raise ValueError(
                "Invalid value for `change_type` ({0}), must be one of {1}"  # noqa: E501
                .format(change_type, allowed_values)
            )

        self._change_type = change_type

    @property
    def complete_file_path(self):
        """Gets the complete_file_path of this GitSyncError.  # noqa: E501

        Complete File Path of the Entity  # noqa: E501

        :return: The complete_file_path of this GitSyncError.  # noqa: E501
        :rtype: str
        """
        return self._complete_file_path

    @complete_file_path.setter
    def complete_file_path(self, complete_file_path):
        """Sets the complete_file_path of this GitSyncError.

        Complete File Path of the Entity  # noqa: E501

        :param complete_file_path: The complete_file_path of this GitSyncError.  # noqa: E501
        :type: str
        """

        self._complete_file_path = complete_file_path

    @property
    def entity_type(self):
        """Gets the entity_type of this GitSyncError.  # noqa: E501

        Entity Type.  # noqa: E501

        :return: The entity_type of this GitSyncError.  # noqa: E501
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this GitSyncError.

        Entity Type.  # noqa: E501

        :param entity_type: The entity_type of this GitSyncError.  # noqa: E501
        :type: str
        """
        allowed_values = ["CreatePR", "MergePR", "Projects", "Pipelines", "PipelineSteps", "Http", "Email", "JiraCreate", "JiraUpdate", "JiraApproval", "HarnessApproval", "CustomApproval", "Barrier", "Queue", "FlagConfiguration", "ShellScript", "K8sCanaryDeploy", "K8sApply", "K8sBlueGreenDeploy", "K8sRollingDeploy", "K8sRollingRollback", "K8sScale", "K8sDelete", "K8sBGSwapServices", "K8sCanaryDelete", "TerraformApply", "TerraformPlan", "TerraformDestroy", "TerraformRollback", "HelmDeploy", "HelmRollback", "Connectors", "Secrets", "Files", "Service", "Environment", "EnvironmentGroup", "InputSets", "CvConfig", "Verify", "Delegates", "DelegateConfigurations", "CvVerificationJob", "IntegrationStage", "IntegrationSteps", "SecurityStage", "SecuritySteps", "CvKubernetesActivitySource", "DeploymentSteps", "DeploymentStage", "ApprovalStage", "PipelineStage", "FeatureFlagStage", "Template", "TemplateStage", "CustomDeployment", "Triggers", "MonitoredService", "GitRepositories", "FeatureFlags", "ServiceNowApproval", "ServiceNowCreate", "ServiceNowUpdate", "ServiceNowImportSet", "GovernancePolicies", "Policy", "Run", "RunTests", "Plugin", "RestoreCacheGCS", "RestoreCacheS3", "SaveCacheGCS", "SaveCacheS3", "Security", "AquaTrivy", "AWSECR", "Bandit", "BlackDuck", "Brakeman", "Burp", "Checkmarx", "Clair", "DataTheorem", "DockerContentTrust", "External", "FortifyOnDemand", "Grype", "JfrogXray", "Mend", "Metasploit", "Nessus", "NexusIQ", "Nikto", "Nmap", "Openvas", "Owasp", "PrismaCloud", "Prowler", "Qualys", "Reapsaw", "ShiftLeft", "Sniper", "Snyk", "Sonarqube", "Sysdig", "Tenable", "Veracode", "Zap", "GitClone", "ArtifactoryUpload", "GCSUpload", "S3Upload", "BuildAndPushGCR", "BuildAndPushGAR", "BuildAndPushECR", "BuildAndPushDockerRegistry", "CreateStack", "DeleteStack", "ServerlessAwsLambdaDeploy", "ServerlessAwsLambdaRollback", "CustomStage", "RollbackStack", "Infrastructure", "Command", "StrategyNode", "AzureSlotDeployment", "AzureTrafficShift", "FetchInstanceScript", "AzureSwapSlot", "AzureWebAppRollback", "JenkinsBuild", "EcsRollingDeploy", "EcsRollingRollback", "EcsCanaryDeploy", "EcsCanaryDelete", "AzureCreateARMResource", "BuildAndPushACR", "AzureCreateBPResource", "AzureARMRollback", "Background", "Wait", "ArtifactSource", "EcsBlueGreenCreateService", "EcsBlueGreenSwapTargetGroups", "EcsBlueGreenRollback", "ShellScriptProvision", "Freeze", "GitOpsUpdateReleaseRepo", "GitOpsFetchLinkedApps", "EcsRunTask", "Chaos", "ElastigroupDeploy", "ElastigroupRollback", "Action", "ElastigroupSetup", "Bitrise", "TerragruntPlan", "TerragruntApply", "TerragruntDestroy", "TerragruntRollback", "IACMStage", "IACMStep", "IACM", "Container", "IACMTerraformPlugin", "IACMApproval", "ElastigroupBGStageSetup", "ElastigroupSwapRoute", "AsgCanaryDeploy", "AsgCanaryDelete", "SwapRoutes", "SwapRollback", "AppResize", "AppRollback", "CanaryAppSetup", "BGAppSetup", "BasicAppSetup", "TanzuCommand", "AsgRollingDeploy", "AsgRollingRollback", "GovernanceRuleAWS", "TasRollingDeploy", "TasRollingRollback", "K8sDryRun", "AsgBlueGreenSwapService", "AsgBlueGreenDeploy", "AsgBlueGreenRollback", "TerraformCloudRun", "TerraformCloudRollback", "DeployCloudFunction", "DeployCloudFunctionWithNoTraffic", "CloudFunctionTrafficShift", "CloudFunctionRollback", "AwsLambdaDeploy", "AwsSamDeploy", "AwsSamRollback", "SscaOrchestration", "AwsLambdaRollback", "GitOpsSync", "BambooBuild", "CdSscaOrchestration", "RouteMapping", "AWSSecurityHub", "CustomIngest", "BackstageEnvironmentVariable", "Fossa", "CodeQL", "Gitleaks", "DeployCloudFunctionGenOne", "RollbackCloudFunctionGenOne", "K8sBlueGreenStageScaleDown", "AwsSamBuild", "Semgrep", "SscaEnforcement", "IdpConnector", "CdSscaEnforcement", "DownloadManifests", "ServerlessAwsLambdaPrepareRollbackV2", "ServerlessAwsLambdaRollbackV2", "Coverity", "ServerlessAwsLambdaDeployV2", "AnalyzeDeploymentImpact", "ServerlessAwsLambdaPackageV2", "RevertPR", "AwsCdkBootstrap", "AwsCdkSynth", "AwsCdkDiff", "AwsCdkDeploy", "AwsCdkDestroy", "IdpScorecard", "IdpCheck", "AwsCdkRollback", "SlsaVerification", "UpdateGitOpsApp", "EcsServiceSetup", "EcsUpgradeContainer", "EcsBasicRollback", "ChaosInfrastructure", "Anchore", "Overrides", "AsgShiftTraffic", "AquaSecurity", "IDPStage", "ChaosHub", "IdpCookieCutter", "IdpCreateRepo"]  # noqa: E501
        if entity_type not in allowed_values:
            raise ValueError(
                "Invalid value for `entity_type` ({0}), must be one of {1}"  # noqa: E501
                .format(entity_type, allowed_values)
            )

        self._entity_type = entity_type

    @property
    def failure_reason(self):
        """Gets the failure_reason of this GitSyncError.  # noqa: E501

        Error Message  # noqa: E501

        :return: The failure_reason of this GitSyncError.  # noqa: E501
        :rtype: str
        """
        return self._failure_reason

    @failure_reason.setter
    def failure_reason(self, failure_reason):
        """Sets the failure_reason of this GitSyncError.

        Error Message  # noqa: E501

        :param failure_reason: The failure_reason of this GitSyncError.  # noqa: E501
        :type: str
        """

        self._failure_reason = failure_reason

    @property
    def status(self):
        """Gets the status of this GitSyncError.  # noqa: E501

        Status of Git Sync Error  # noqa: E501

        :return: The status of this GitSyncError.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GitSyncError.

        Status of Git Sync Error  # noqa: E501

        :param status: The status of this GitSyncError.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACTIVE", "DISCARDED", "EXPIRED", "RESOLVED", "OVERRIDDEN"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def error_type(self):
        """Gets the error_type of this GitSyncError.  # noqa: E501

        Type of Git Sync Error  # noqa: E501

        :return: The error_type of this GitSyncError.  # noqa: E501
        :rtype: str
        """
        return self._error_type

    @error_type.setter
    def error_type(self, error_type):
        """Sets the error_type of this GitSyncError.

        Type of Git Sync Error  # noqa: E501

        :param error_type: The error_type of this GitSyncError.  # noqa: E501
        :type: str
        """
        allowed_values = ["GIT_TO_HARNESS", "CONNECTIVITY_ISSUE", "FULL_SYNC"]  # noqa: E501
        if error_type not in allowed_values:
            raise ValueError(
                "Invalid value for `error_type` ({0}), must be one of {1}"  # noqa: E501
                .format(error_type, allowed_values)
            )

        self._error_type = error_type

    @property
    def additional_error_details(self):
        """Gets the additional_error_details of this GitSyncError.  # noqa: E501


        :return: The additional_error_details of this GitSyncError.  # noqa: E501
        :rtype: GitSyncErrorDetails
        """
        return self._additional_error_details

    @additional_error_details.setter
    def additional_error_details(self, additional_error_details):
        """Sets the additional_error_details of this GitSyncError.


        :param additional_error_details: The additional_error_details of this GitSyncError.  # noqa: E501
        :type: GitSyncErrorDetails
        """

        self._additional_error_details = additional_error_details

    @property
    def created_at(self):
        """Gets the created_at of this GitSyncError.  # noqa: E501

        Time at which the Git Sync error was logged  # noqa: E501

        :return: The created_at of this GitSyncError.  # noqa: E501
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this GitSyncError.

        Time at which the Git Sync error was logged  # noqa: E501

        :param created_at: The created_at of this GitSyncError.  # noqa: E501
        :type: int
        """

        self._created_at = created_at

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
        if issubclass(GitSyncError, dict):
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
        if not isinstance(other, GitSyncError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
