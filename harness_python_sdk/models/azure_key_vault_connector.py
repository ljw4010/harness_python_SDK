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

class AzureKeyVaultConnector(ConnectorConfig):
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
        'client_id': 'str',
        'secret_key': 'str',
        'tenant_id': 'str',
        'vault_name': 'str',
        'subscription': 'str',
        'is_default': 'bool',
        'vault_configured_manually': 'bool',
        'azure_environment_type': 'str',
        'delegate_selectors': 'list[str]',
        'use_managed_identity': 'bool',
        'azure_managed_identity_type': 'str',
        'managed_client_id': 'str',
        'enable_purge': 'bool',
        'default': 'bool'
    }
    if hasattr(ConnectorConfig, "swagger_types"):
        swagger_types.update(ConnectorConfig.swagger_types)

    attribute_map = {
        'client_id': 'clientId',
        'secret_key': 'secretKey',
        'tenant_id': 'tenantId',
        'vault_name': 'vaultName',
        'subscription': 'subscription',
        'is_default': 'isDefault',
        'vault_configured_manually': 'vaultConfiguredManually',
        'azure_environment_type': 'azureEnvironmentType',
        'delegate_selectors': 'delegateSelectors',
        'use_managed_identity': 'useManagedIdentity',
        'azure_managed_identity_type': 'azureManagedIdentityType',
        'managed_client_id': 'managedClientId',
        'enable_purge': 'enablePurge',
        'default': 'default'
    }
    if hasattr(ConnectorConfig, "attribute_map"):
        attribute_map.update(ConnectorConfig.attribute_map)

    def __init__(self, client_id=None, secret_key=None, tenant_id=None, vault_name=None, subscription=None, is_default=None, vault_configured_manually=None, azure_environment_type=None, delegate_selectors=None, use_managed_identity=None, azure_managed_identity_type=None, managed_client_id=None, enable_purge=None, default=None, *args, **kwargs):  # noqa: E501
        """AzureKeyVaultConnector - a model defined in Swagger"""  # noqa: E501
        self._client_id = None
        self._secret_key = None
        self._tenant_id = None
        self._vault_name = None
        self._subscription = None
        self._is_default = None
        self._vault_configured_manually = None
        self._azure_environment_type = None
        self._delegate_selectors = None
        self._use_managed_identity = None
        self._azure_managed_identity_type = None
        self._managed_client_id = None
        self._enable_purge = None
        self._default = None
        self.discriminator = None
        if client_id is not None:
            self.client_id = client_id
        if secret_key is not None:
            self.secret_key = secret_key
        if tenant_id is not None:
            self.tenant_id = tenant_id
        self.vault_name = vault_name
        self.subscription = subscription
        if is_default is not None:
            self.is_default = is_default
        if vault_configured_manually is not None:
            self.vault_configured_manually = vault_configured_manually
        if azure_environment_type is not None:
            self.azure_environment_type = azure_environment_type
        if delegate_selectors is not None:
            self.delegate_selectors = delegate_selectors
        if use_managed_identity is not None:
            self.use_managed_identity = use_managed_identity
        if azure_managed_identity_type is not None:
            self.azure_managed_identity_type = azure_managed_identity_type
        if managed_client_id is not None:
            self.managed_client_id = managed_client_id
        if enable_purge is not None:
            self.enable_purge = enable_purge
        if default is not None:
            self.default = default
        ConnectorConfig.__init__(self, *args, **kwargs)

    @property
    def client_id(self):
        """Gets the client_id of this AzureKeyVaultConnector.  # noqa: E501

        Application ID of the Azure App.  # noqa: E501

        :return: The client_id of this AzureKeyVaultConnector.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this AzureKeyVaultConnector.

        Application ID of the Azure App.  # noqa: E501

        :param client_id: The client_id of this AzureKeyVaultConnector.  # noqa: E501
        :type: str
        """

        self._client_id = client_id

    @property
    def secret_key(self):
        """Gets the secret_key of this AzureKeyVaultConnector.  # noqa: E501

        This is the Harness text secret with the Azure authentication key as its value.  # noqa: E501

        :return: The secret_key of this AzureKeyVaultConnector.  # noqa: E501
        :rtype: str
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        """Sets the secret_key of this AzureKeyVaultConnector.

        This is the Harness text secret with the Azure authentication key as its value.  # noqa: E501

        :param secret_key: The secret_key of this AzureKeyVaultConnector.  # noqa: E501
        :type: str
        """

        self._secret_key = secret_key

    @property
    def tenant_id(self):
        """Gets the tenant_id of this AzureKeyVaultConnector.  # noqa: E501

        The Azure Active Directory (AAD) directory ID where you created your application.  # noqa: E501

        :return: The tenant_id of this AzureKeyVaultConnector.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this AzureKeyVaultConnector.

        The Azure Active Directory (AAD) directory ID where you created your application.  # noqa: E501

        :param tenant_id: The tenant_id of this AzureKeyVaultConnector.  # noqa: E501
        :type: str
        """

        self._tenant_id = tenant_id

    @property
    def vault_name(self):
        """Gets the vault_name of this AzureKeyVaultConnector.  # noqa: E501

        The Azure Vault name  # noqa: E501

        :return: The vault_name of this AzureKeyVaultConnector.  # noqa: E501
        :rtype: str
        """
        return self._vault_name

    @vault_name.setter
    def vault_name(self, vault_name):
        """Sets the vault_name of this AzureKeyVaultConnector.

        The Azure Vault name  # noqa: E501

        :param vault_name: The vault_name of this AzureKeyVaultConnector.  # noqa: E501
        :type: str
        """
        if vault_name is None:
            raise ValueError("Invalid value for `vault_name`, must not be `None`")  # noqa: E501

        self._vault_name = vault_name

    @property
    def subscription(self):
        """Gets the subscription of this AzureKeyVaultConnector.  # noqa: E501

        Azure Subscription ID.  # noqa: E501

        :return: The subscription of this AzureKeyVaultConnector.  # noqa: E501
        :rtype: str
        """
        return self._subscription

    @subscription.setter
    def subscription(self, subscription):
        """Sets the subscription of this AzureKeyVaultConnector.

        Azure Subscription ID.  # noqa: E501

        :param subscription: The subscription of this AzureKeyVaultConnector.  # noqa: E501
        :type: str
        """
        if subscription is None:
            raise ValueError("Invalid value for `subscription`, must not be `None`")  # noqa: E501

        self._subscription = subscription

    @property
    def is_default(self):
        """Gets the is_default of this AzureKeyVaultConnector.  # noqa: E501


        :return: The is_default of this AzureKeyVaultConnector.  # noqa: E501
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this AzureKeyVaultConnector.


        :param is_default: The is_default of this AzureKeyVaultConnector.  # noqa: E501
        :type: bool
        """

        self._is_default = is_default

    @property
    def vault_configured_manually(self):
        """Gets the vault_configured_manually of this AzureKeyVaultConnector.  # noqa: E501


        :return: The vault_configured_manually of this AzureKeyVaultConnector.  # noqa: E501
        :rtype: bool
        """
        return self._vault_configured_manually

    @vault_configured_manually.setter
    def vault_configured_manually(self, vault_configured_manually):
        """Sets the vault_configured_manually of this AzureKeyVaultConnector.


        :param vault_configured_manually: The vault_configured_manually of this AzureKeyVaultConnector.  # noqa: E501
        :type: bool
        """

        self._vault_configured_manually = vault_configured_manually

    @property
    def azure_environment_type(self):
        """Gets the azure_environment_type of this AzureKeyVaultConnector.  # noqa: E501

        This specifies the Azure Environment type, which is AZURE by default.  # noqa: E501

        :return: The azure_environment_type of this AzureKeyVaultConnector.  # noqa: E501
        :rtype: str
        """
        return self._azure_environment_type

    @azure_environment_type.setter
    def azure_environment_type(self, azure_environment_type):
        """Sets the azure_environment_type of this AzureKeyVaultConnector.

        This specifies the Azure Environment type, which is AZURE by default.  # noqa: E501

        :param azure_environment_type: The azure_environment_type of this AzureKeyVaultConnector.  # noqa: E501
        :type: str
        """
        allowed_values = ["AZURE", "AZURE_US_GOVERNMENT"]  # noqa: E501
        if azure_environment_type not in allowed_values:
            raise ValueError(
                "Invalid value for `azure_environment_type` ({0}), must be one of {1}"  # noqa: E501
                .format(azure_environment_type, allowed_values)
            )

        self._azure_environment_type = azure_environment_type

    @property
    def delegate_selectors(self):
        """Gets the delegate_selectors of this AzureKeyVaultConnector.  # noqa: E501

        List of Delegate Selectors that belong to the same Delegate and are used to connect to the Secret Manager.  # noqa: E501

        :return: The delegate_selectors of this AzureKeyVaultConnector.  # noqa: E501
        :rtype: list[str]
        """
        return self._delegate_selectors

    @delegate_selectors.setter
    def delegate_selectors(self, delegate_selectors):
        """Sets the delegate_selectors of this AzureKeyVaultConnector.

        List of Delegate Selectors that belong to the same Delegate and are used to connect to the Secret Manager.  # noqa: E501

        :param delegate_selectors: The delegate_selectors of this AzureKeyVaultConnector.  # noqa: E501
        :type: list[str]
        """

        self._delegate_selectors = delegate_selectors

    @property
    def use_managed_identity(self):
        """Gets the use_managed_identity of this AzureKeyVaultConnector.  # noqa: E501

        Boolean value to indicate if managed identity is used  # noqa: E501

        :return: The use_managed_identity of this AzureKeyVaultConnector.  # noqa: E501
        :rtype: bool
        """
        return self._use_managed_identity

    @use_managed_identity.setter
    def use_managed_identity(self, use_managed_identity):
        """Sets the use_managed_identity of this AzureKeyVaultConnector.

        Boolean value to indicate if managed identity is used  # noqa: E501

        :param use_managed_identity: The use_managed_identity of this AzureKeyVaultConnector.  # noqa: E501
        :type: bool
        """

        self._use_managed_identity = use_managed_identity

    @property
    def azure_managed_identity_type(self):
        """Gets the azure_managed_identity_type of this AzureKeyVaultConnector.  # noqa: E501

        Managed Identity Type  # noqa: E501

        :return: The azure_managed_identity_type of this AzureKeyVaultConnector.  # noqa: E501
        :rtype: str
        """
        return self._azure_managed_identity_type

    @azure_managed_identity_type.setter
    def azure_managed_identity_type(self, azure_managed_identity_type):
        """Sets the azure_managed_identity_type of this AzureKeyVaultConnector.

        Managed Identity Type  # noqa: E501

        :param azure_managed_identity_type: The azure_managed_identity_type of this AzureKeyVaultConnector.  # noqa: E501
        :type: str
        """
        allowed_values = ["SystemAssignedManagedIdentity", "UserAssignedManagedIdentity"]  # noqa: E501
        if azure_managed_identity_type not in allowed_values:
            raise ValueError(
                "Invalid value for `azure_managed_identity_type` ({0}), must be one of {1}"  # noqa: E501
                .format(azure_managed_identity_type, allowed_values)
            )

        self._azure_managed_identity_type = azure_managed_identity_type

    @property
    def managed_client_id(self):
        """Gets the managed_client_id of this AzureKeyVaultConnector.  # noqa: E501

        Client Id of the ManagedIdentity resource  # noqa: E501

        :return: The managed_client_id of this AzureKeyVaultConnector.  # noqa: E501
        :rtype: str
        """
        return self._managed_client_id

    @managed_client_id.setter
    def managed_client_id(self, managed_client_id):
        """Sets the managed_client_id of this AzureKeyVaultConnector.

        Client Id of the ManagedIdentity resource  # noqa: E501

        :param managed_client_id: The managed_client_id of this AzureKeyVaultConnector.  # noqa: E501
        :type: str
        """

        self._managed_client_id = managed_client_id

    @property
    def enable_purge(self):
        """Gets the enable_purge of this AzureKeyVaultConnector.  # noqa: E501

        Boolean value to indicate if purge is enabled  # noqa: E501

        :return: The enable_purge of this AzureKeyVaultConnector.  # noqa: E501
        :rtype: bool
        """
        return self._enable_purge

    @enable_purge.setter
    def enable_purge(self, enable_purge):
        """Sets the enable_purge of this AzureKeyVaultConnector.

        Boolean value to indicate if purge is enabled  # noqa: E501

        :param enable_purge: The enable_purge of this AzureKeyVaultConnector.  # noqa: E501
        :type: bool
        """

        self._enable_purge = enable_purge

    @property
    def default(self):
        """Gets the default of this AzureKeyVaultConnector.  # noqa: E501


        :return: The default of this AzureKeyVaultConnector.  # noqa: E501
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this AzureKeyVaultConnector.


        :param default: The default of this AzureKeyVaultConnector.  # noqa: E501
        :type: bool
        """

        self._default = default

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
        if issubclass(AzureKeyVaultConnector, dict):
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
        if not isinstance(other, AzureKeyVaultConnector):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
