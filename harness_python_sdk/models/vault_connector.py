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
from harness_python_sdk.models.connector_config import ConnectorConfig  # noqa: F401,E501

class VaultConnector(ConnectorConfig):
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
        'auth_token': 'str',
        'base_path': 'str',
        'vault_url': 'str',
        'renewal_interval_minutes': 'int',
        'secret_engine_manually_configured': 'bool',
        'secret_engine_name': 'str',
        'app_role_id': 'str',
        'secret_id': 'str',
        'secret_engine_version': 'int',
        'delegate_selectors': 'list[str]',
        'namespace': 'str',
        'sink_path': 'str',
        'use_vault_agent': 'bool',
        'use_aws_iam': 'bool',
        'aws_region': 'str',
        'vault_aws_iam_role': 'str',
        'use_k8s_auth': 'bool',
        'vault_k8s_auth_role': 'str',
        'service_account_token_path': 'str',
        'k8s_auth_endpoint': 'str',
        'renew_app_role_token': 'bool',
        'enable_cache': 'bool',
        'read_only': 'bool',
        'default': 'bool',
        'access_type': 'str',
        'xvault_aws_iam_server_id': 'str'
    }
    if hasattr(ConnectorConfig, "swagger_types"):
        swagger_types.update(ConnectorConfig.swagger_types)

    attribute_map = {
        'auth_token': 'authToken',
        'base_path': 'basePath',
        'vault_url': 'vaultUrl',
        'renewal_interval_minutes': 'renewalIntervalMinutes',
        'secret_engine_manually_configured': 'secretEngineManuallyConfigured',
        'secret_engine_name': 'secretEngineName',
        'app_role_id': 'appRoleId',
        'secret_id': 'secretId',
        'secret_engine_version': 'secretEngineVersion',
        'delegate_selectors': 'delegateSelectors',
        'namespace': 'namespace',
        'sink_path': 'sinkPath',
        'use_vault_agent': 'useVaultAgent',
        'use_aws_iam': 'useAwsIam',
        'aws_region': 'awsRegion',
        'vault_aws_iam_role': 'vaultAwsIamRole',
        'use_k8s_auth': 'useK8sAuth',
        'vault_k8s_auth_role': 'vaultK8sAuthRole',
        'service_account_token_path': 'serviceAccountTokenPath',
        'k8s_auth_endpoint': 'k8sAuthEndpoint',
        'renew_app_role_token': 'renewAppRoleToken',
        'enable_cache': 'enableCache',
        'read_only': 'readOnly',
        'default': 'default',
        'access_type': 'accessType',
        'xvault_aws_iam_server_id': 'xvaultAwsIamServerId'
    }
    if hasattr(ConnectorConfig, "attribute_map"):
        attribute_map.update(ConnectorConfig.attribute_map)

    def __init__(self, auth_token=None, base_path=None, vault_url=None, renewal_interval_minutes=None, secret_engine_manually_configured=None, secret_engine_name=None, app_role_id=None, secret_id=None, secret_engine_version=None, delegate_selectors=None, namespace=None, sink_path=None, use_vault_agent=None, use_aws_iam=None, aws_region=None, vault_aws_iam_role=None, use_k8s_auth=None, vault_k8s_auth_role=None, service_account_token_path=None, k8s_auth_endpoint=None, renew_app_role_token=None, enable_cache=None, read_only=None, default=None, access_type=None, xvault_aws_iam_server_id=None, *args, **kwargs):  # noqa: E501
        """VaultConnector - a model defined in Swagger"""  # noqa: E501
        self._auth_token = None
        self._base_path = None
        self._vault_url = None
        self._renewal_interval_minutes = None
        self._secret_engine_manually_configured = None
        self._secret_engine_name = None
        self._app_role_id = None
        self._secret_id = None
        self._secret_engine_version = None
        self._delegate_selectors = None
        self._namespace = None
        self._sink_path = None
        self._use_vault_agent = None
        self._use_aws_iam = None
        self._aws_region = None
        self._vault_aws_iam_role = None
        self._use_k8s_auth = None
        self._vault_k8s_auth_role = None
        self._service_account_token_path = None
        self._k8s_auth_endpoint = None
        self._renew_app_role_token = None
        self._enable_cache = None
        self._read_only = None
        self._default = None
        self._access_type = None
        self._xvault_aws_iam_server_id = None
        self.discriminator = None
        if auth_token is not None:
            self.auth_token = auth_token
        if base_path is not None:
            self.base_path = base_path
        self.vault_url = vault_url
        self.renewal_interval_minutes = renewal_interval_minutes
        if secret_engine_manually_configured is not None:
            self.secret_engine_manually_configured = secret_engine_manually_configured
        if secret_engine_name is not None:
            self.secret_engine_name = secret_engine_name
        if app_role_id is not None:
            self.app_role_id = app_role_id
        if secret_id is not None:
            self.secret_id = secret_id
        if secret_engine_version is not None:
            self.secret_engine_version = secret_engine_version
        if delegate_selectors is not None:
            self.delegate_selectors = delegate_selectors
        if namespace is not None:
            self.namespace = namespace
        if sink_path is not None:
            self.sink_path = sink_path
        if use_vault_agent is not None:
            self.use_vault_agent = use_vault_agent
        if use_aws_iam is not None:
            self.use_aws_iam = use_aws_iam
        if aws_region is not None:
            self.aws_region = aws_region
        if vault_aws_iam_role is not None:
            self.vault_aws_iam_role = vault_aws_iam_role
        if use_k8s_auth is not None:
            self.use_k8s_auth = use_k8s_auth
        if vault_k8s_auth_role is not None:
            self.vault_k8s_auth_role = vault_k8s_auth_role
        if service_account_token_path is not None:
            self.service_account_token_path = service_account_token_path
        if k8s_auth_endpoint is not None:
            self.k8s_auth_endpoint = k8s_auth_endpoint
        if renew_app_role_token is not None:
            self.renew_app_role_token = renew_app_role_token
        if enable_cache is not None:
            self.enable_cache = enable_cache
        if read_only is not None:
            self.read_only = read_only
        if default is not None:
            self.default = default
        if access_type is not None:
            self.access_type = access_type
        if xvault_aws_iam_server_id is not None:
            self.xvault_aws_iam_server_id = xvault_aws_iam_server_id
        ConnectorConfig.__init__(self, *args, **kwargs)

    @property
    def auth_token(self):
        """Gets the auth_token of this VaultConnector.  # noqa: E501

        This is the authentication token for Vault.  # noqa: E501

        :return: The auth_token of this VaultConnector.  # noqa: E501
        :rtype: str
        """
        return self._auth_token

    @auth_token.setter
    def auth_token(self, auth_token):
        """Sets the auth_token of this VaultConnector.

        This is the authentication token for Vault.  # noqa: E501

        :param auth_token: The auth_token of this VaultConnector.  # noqa: E501
        :type: str
        """

        self._auth_token = auth_token

    @property
    def base_path(self):
        """Gets the base_path of this VaultConnector.  # noqa: E501

        This is the location of the Vault directory where Secret will be stored.  # noqa: E501

        :return: The base_path of this VaultConnector.  # noqa: E501
        :rtype: str
        """
        return self._base_path

    @base_path.setter
    def base_path(self, base_path):
        """Sets the base_path of this VaultConnector.

        This is the location of the Vault directory where Secret will be stored.  # noqa: E501

        :param base_path: The base_path of this VaultConnector.  # noqa: E501
        :type: str
        """

        self._base_path = base_path

    @property
    def vault_url(self):
        """Gets the vault_url of this VaultConnector.  # noqa: E501

        URL of the HashiCorp Vault.  # noqa: E501

        :return: The vault_url of this VaultConnector.  # noqa: E501
        :rtype: str
        """
        return self._vault_url

    @vault_url.setter
    def vault_url(self, vault_url):
        """Sets the vault_url of this VaultConnector.

        URL of the HashiCorp Vault.  # noqa: E501

        :param vault_url: The vault_url of this VaultConnector.  # noqa: E501
        :type: str
        """
        if vault_url is None:
            raise ValueError("Invalid value for `vault_url`, must not be `None`")  # noqa: E501

        self._vault_url = vault_url

    @property
    def renewal_interval_minutes(self):
        """Gets the renewal_interval_minutes of this VaultConnector.  # noqa: E501

        This is the time interval for token renewal.  # noqa: E501

        :return: The renewal_interval_minutes of this VaultConnector.  # noqa: E501
        :rtype: int
        """
        return self._renewal_interval_minutes

    @renewal_interval_minutes.setter
    def renewal_interval_minutes(self, renewal_interval_minutes):
        """Sets the renewal_interval_minutes of this VaultConnector.

        This is the time interval for token renewal.  # noqa: E501

        :param renewal_interval_minutes: The renewal_interval_minutes of this VaultConnector.  # noqa: E501
        :type: int
        """
        if renewal_interval_minutes is None:
            raise ValueError("Invalid value for `renewal_interval_minutes`, must not be `None`")  # noqa: E501

        self._renewal_interval_minutes = renewal_interval_minutes

    @property
    def secret_engine_manually_configured(self):
        """Gets the secret_engine_manually_configured of this VaultConnector.  # noqa: E501

        Manually entered Secret Engine.  # noqa: E501

        :return: The secret_engine_manually_configured of this VaultConnector.  # noqa: E501
        :rtype: bool
        """
        return self._secret_engine_manually_configured

    @secret_engine_manually_configured.setter
    def secret_engine_manually_configured(self, secret_engine_manually_configured):
        """Sets the secret_engine_manually_configured of this VaultConnector.

        Manually entered Secret Engine.  # noqa: E501

        :param secret_engine_manually_configured: The secret_engine_manually_configured of this VaultConnector.  # noqa: E501
        :type: bool
        """

        self._secret_engine_manually_configured = secret_engine_manually_configured

    @property
    def secret_engine_name(self):
        """Gets the secret_engine_name of this VaultConnector.  # noqa: E501

        Name of the Secret Engine.  # noqa: E501

        :return: The secret_engine_name of this VaultConnector.  # noqa: E501
        :rtype: str
        """
        return self._secret_engine_name

    @secret_engine_name.setter
    def secret_engine_name(self, secret_engine_name):
        """Sets the secret_engine_name of this VaultConnector.

        Name of the Secret Engine.  # noqa: E501

        :param secret_engine_name: The secret_engine_name of this VaultConnector.  # noqa: E501
        :type: str
        """

        self._secret_engine_name = secret_engine_name

    @property
    def app_role_id(self):
        """Gets the app_role_id of this VaultConnector.  # noqa: E501

        ID of App Role.  # noqa: E501

        :return: The app_role_id of this VaultConnector.  # noqa: E501
        :rtype: str
        """
        return self._app_role_id

    @app_role_id.setter
    def app_role_id(self, app_role_id):
        """Sets the app_role_id of this VaultConnector.

        ID of App Role.  # noqa: E501

        :param app_role_id: The app_role_id of this VaultConnector.  # noqa: E501
        :type: str
        """

        self._app_role_id = app_role_id

    @property
    def secret_id(self):
        """Gets the secret_id of this VaultConnector.  # noqa: E501

        ID of the Secret.  # noqa: E501

        :return: The secret_id of this VaultConnector.  # noqa: E501
        :rtype: str
        """
        return self._secret_id

    @secret_id.setter
    def secret_id(self, secret_id):
        """Sets the secret_id of this VaultConnector.

        ID of the Secret.  # noqa: E501

        :param secret_id: The secret_id of this VaultConnector.  # noqa: E501
        :type: str
        """

        self._secret_id = secret_id

    @property
    def secret_engine_version(self):
        """Gets the secret_engine_version of this VaultConnector.  # noqa: E501

        Version of Secret Engine.  # noqa: E501

        :return: The secret_engine_version of this VaultConnector.  # noqa: E501
        :rtype: int
        """
        return self._secret_engine_version

    @secret_engine_version.setter
    def secret_engine_version(self, secret_engine_version):
        """Sets the secret_engine_version of this VaultConnector.

        Version of Secret Engine.  # noqa: E501

        :param secret_engine_version: The secret_engine_version of this VaultConnector.  # noqa: E501
        :type: int
        """

        self._secret_engine_version = secret_engine_version

    @property
    def delegate_selectors(self):
        """Gets the delegate_selectors of this VaultConnector.  # noqa: E501

        List of Delegate Selectors that belong to the same Delegate and are used to connect to the Secret Manager.  # noqa: E501

        :return: The delegate_selectors of this VaultConnector.  # noqa: E501
        :rtype: list[str]
        """
        return self._delegate_selectors

    @delegate_selectors.setter
    def delegate_selectors(self, delegate_selectors):
        """Sets the delegate_selectors of this VaultConnector.

        List of Delegate Selectors that belong to the same Delegate and are used to connect to the Secret Manager.  # noqa: E501

        :param delegate_selectors: The delegate_selectors of this VaultConnector.  # noqa: E501
        :type: list[str]
        """

        self._delegate_selectors = delegate_selectors

    @property
    def namespace(self):
        """Gets the namespace of this VaultConnector.  # noqa: E501

        This is the Vault namespace where Secret will be created.  # noqa: E501

        :return: The namespace of this VaultConnector.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this VaultConnector.

        This is the Vault namespace where Secret will be created.  # noqa: E501

        :param namespace: The namespace of this VaultConnector.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

    @property
    def sink_path(self):
        """Gets the sink_path of this VaultConnector.  # noqa: E501

        This is the location at which auth token is to be read from.  # noqa: E501

        :return: The sink_path of this VaultConnector.  # noqa: E501
        :rtype: str
        """
        return self._sink_path

    @sink_path.setter
    def sink_path(self, sink_path):
        """Sets the sink_path of this VaultConnector.

        This is the location at which auth token is to be read from.  # noqa: E501

        :param sink_path: The sink_path of this VaultConnector.  # noqa: E501
        :type: str
        """

        self._sink_path = sink_path

    @property
    def use_vault_agent(self):
        """Gets the use_vault_agent of this VaultConnector.  # noqa: E501

        Boolean value to indicate if Vault Agent is used for authentication.  # noqa: E501

        :return: The use_vault_agent of this VaultConnector.  # noqa: E501
        :rtype: bool
        """
        return self._use_vault_agent

    @use_vault_agent.setter
    def use_vault_agent(self, use_vault_agent):
        """Sets the use_vault_agent of this VaultConnector.

        Boolean value to indicate if Vault Agent is used for authentication.  # noqa: E501

        :param use_vault_agent: The use_vault_agent of this VaultConnector.  # noqa: E501
        :type: bool
        """

        self._use_vault_agent = use_vault_agent

    @property
    def use_aws_iam(self):
        """Gets the use_aws_iam of this VaultConnector.  # noqa: E501

        Boolean value to indicate if Aws Iam is used for authentication.  # noqa: E501

        :return: The use_aws_iam of this VaultConnector.  # noqa: E501
        :rtype: bool
        """
        return self._use_aws_iam

    @use_aws_iam.setter
    def use_aws_iam(self, use_aws_iam):
        """Sets the use_aws_iam of this VaultConnector.

        Boolean value to indicate if Aws Iam is used for authentication.  # noqa: E501

        :param use_aws_iam: The use_aws_iam of this VaultConnector.  # noqa: E501
        :type: bool
        """

        self._use_aws_iam = use_aws_iam

    @property
    def aws_region(self):
        """Gets the aws_region of this VaultConnector.  # noqa: E501

        This is the Aws region where aws iam auth will happen.  # noqa: E501

        :return: The aws_region of this VaultConnector.  # noqa: E501
        :rtype: str
        """
        return self._aws_region

    @aws_region.setter
    def aws_region(self, aws_region):
        """Sets the aws_region of this VaultConnector.

        This is the Aws region where aws iam auth will happen.  # noqa: E501

        :param aws_region: The aws_region of this VaultConnector.  # noqa: E501
        :type: str
        """

        self._aws_region = aws_region

    @property
    def vault_aws_iam_role(self):
        """Gets the vault_aws_iam_role of this VaultConnector.  # noqa: E501

        This is the Vault role defined to bind to aws iam account/role being accessed.  # noqa: E501

        :return: The vault_aws_iam_role of this VaultConnector.  # noqa: E501
        :rtype: str
        """
        return self._vault_aws_iam_role

    @vault_aws_iam_role.setter
    def vault_aws_iam_role(self, vault_aws_iam_role):
        """Sets the vault_aws_iam_role of this VaultConnector.

        This is the Vault role defined to bind to aws iam account/role being accessed.  # noqa: E501

        :param vault_aws_iam_role: The vault_aws_iam_role of this VaultConnector.  # noqa: E501
        :type: str
        """

        self._vault_aws_iam_role = vault_aws_iam_role

    @property
    def use_k8s_auth(self):
        """Gets the use_k8s_auth of this VaultConnector.  # noqa: E501

        Boolean value to indicate if K8s Auth is used for authentication.  # noqa: E501

        :return: The use_k8s_auth of this VaultConnector.  # noqa: E501
        :rtype: bool
        """
        return self._use_k8s_auth

    @use_k8s_auth.setter
    def use_k8s_auth(self, use_k8s_auth):
        """Sets the use_k8s_auth of this VaultConnector.

        Boolean value to indicate if K8s Auth is used for authentication.  # noqa: E501

        :param use_k8s_auth: The use_k8s_auth of this VaultConnector.  # noqa: E501
        :type: bool
        """

        self._use_k8s_auth = use_k8s_auth

    @property
    def vault_k8s_auth_role(self):
        """Gets the vault_k8s_auth_role of this VaultConnector.  # noqa: E501

        This is the role where K8s auth will happen.  # noqa: E501

        :return: The vault_k8s_auth_role of this VaultConnector.  # noqa: E501
        :rtype: str
        """
        return self._vault_k8s_auth_role

    @vault_k8s_auth_role.setter
    def vault_k8s_auth_role(self, vault_k8s_auth_role):
        """Sets the vault_k8s_auth_role of this VaultConnector.

        This is the role where K8s auth will happen.  # noqa: E501

        :param vault_k8s_auth_role: The vault_k8s_auth_role of this VaultConnector.  # noqa: E501
        :type: str
        """

        self._vault_k8s_auth_role = vault_k8s_auth_role

    @property
    def service_account_token_path(self):
        """Gets the service_account_token_path of this VaultConnector.  # noqa: E501

        This is the SA token path where the token is mounted in the K8s Pod.  # noqa: E501

        :return: The service_account_token_path of this VaultConnector.  # noqa: E501
        :rtype: str
        """
        return self._service_account_token_path

    @service_account_token_path.setter
    def service_account_token_path(self, service_account_token_path):
        """Sets the service_account_token_path of this VaultConnector.

        This is the SA token path where the token is mounted in the K8s Pod.  # noqa: E501

        :param service_account_token_path: The service_account_token_path of this VaultConnector.  # noqa: E501
        :type: str
        """

        self._service_account_token_path = service_account_token_path

    @property
    def k8s_auth_endpoint(self):
        """Gets the k8s_auth_endpoint of this VaultConnector.  # noqa: E501

        This is the path where kubernetes auth is enabled in Vault.  # noqa: E501

        :return: The k8s_auth_endpoint of this VaultConnector.  # noqa: E501
        :rtype: str
        """
        return self._k8s_auth_endpoint

    @k8s_auth_endpoint.setter
    def k8s_auth_endpoint(self, k8s_auth_endpoint):
        """Sets the k8s_auth_endpoint of this VaultConnector.

        This is the path where kubernetes auth is enabled in Vault.  # noqa: E501

        :param k8s_auth_endpoint: The k8s_auth_endpoint of this VaultConnector.  # noqa: E501
        :type: str
        """

        self._k8s_auth_endpoint = k8s_auth_endpoint

    @property
    def renew_app_role_token(self):
        """Gets the renew_app_role_token of this VaultConnector.  # noqa: E501

        Boolean value to indicate if appRole token renewal is enabled or not.  # noqa: E501

        :return: The renew_app_role_token of this VaultConnector.  # noqa: E501
        :rtype: bool
        """
        return self._renew_app_role_token

    @renew_app_role_token.setter
    def renew_app_role_token(self, renew_app_role_token):
        """Sets the renew_app_role_token of this VaultConnector.

        Boolean value to indicate if appRole token renewal is enabled or not.  # noqa: E501

        :param renew_app_role_token: The renew_app_role_token of this VaultConnector.  # noqa: E501
        :type: bool
        """

        self._renew_app_role_token = renew_app_role_token

    @property
    def enable_cache(self):
        """Gets the enable_cache of this VaultConnector.  # noqa: E501

        Boolean value to indicate if cache is enabled for App Role Token.  # noqa: E501

        :return: The enable_cache of this VaultConnector.  # noqa: E501
        :rtype: bool
        """
        return self._enable_cache

    @enable_cache.setter
    def enable_cache(self, enable_cache):
        """Sets the enable_cache of this VaultConnector.

        Boolean value to indicate if cache is enabled for App Role Token.  # noqa: E501

        :param enable_cache: The enable_cache of this VaultConnector.  # noqa: E501
        :type: bool
        """

        self._enable_cache = enable_cache

    @property
    def read_only(self):
        """Gets the read_only of this VaultConnector.  # noqa: E501


        :return: The read_only of this VaultConnector.  # noqa: E501
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this VaultConnector.


        :param read_only: The read_only of this VaultConnector.  # noqa: E501
        :type: bool
        """

        self._read_only = read_only

    @property
    def default(self):
        """Gets the default of this VaultConnector.  # noqa: E501


        :return: The default of this VaultConnector.  # noqa: E501
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this VaultConnector.


        :param default: The default of this VaultConnector.  # noqa: E501
        :type: bool
        """

        self._default = default

    @property
    def access_type(self):
        """Gets the access_type of this VaultConnector.  # noqa: E501


        :return: The access_type of this VaultConnector.  # noqa: E501
        :rtype: str
        """
        return self._access_type

    @access_type.setter
    def access_type(self, access_type):
        """Sets the access_type of this VaultConnector.


        :param access_type: The access_type of this VaultConnector.  # noqa: E501
        :type: str
        """
        allowed_values = ["APP_ROLE", "TOKEN", "VAULT_AGENT", "AWS_IAM", "K8s_AUTH"]  # noqa: E501
        if access_type not in allowed_values:
            raise ValueError(
                "Invalid value for `access_type` ({0}), must be one of {1}"  # noqa: E501
                .format(access_type, allowed_values)
            )

        self._access_type = access_type

    @property
    def xvault_aws_iam_server_id(self):
        """Gets the xvault_aws_iam_server_id of this VaultConnector.  # noqa: E501

        This is the Aws Iam Header Server ID that has been configured for this Aws Iam instance.  # noqa: E501

        :return: The xvault_aws_iam_server_id of this VaultConnector.  # noqa: E501
        :rtype: str
        """
        return self._xvault_aws_iam_server_id

    @xvault_aws_iam_server_id.setter
    def xvault_aws_iam_server_id(self, xvault_aws_iam_server_id):
        """Sets the xvault_aws_iam_server_id of this VaultConnector.

        This is the Aws Iam Header Server ID that has been configured for this Aws Iam instance.  # noqa: E501

        :param xvault_aws_iam_server_id: The xvault_aws_iam_server_id of this VaultConnector.  # noqa: E501
        :type: str
        """

        self._xvault_aws_iam_server_id = xvault_aws_iam_server_id

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
        if issubclass(VaultConnector, dict):
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
        if not isinstance(other, VaultConnector):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
