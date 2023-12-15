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

class LdapConnectionSettings(object):
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
        'host': 'str',
        'port': 'int',
        'ssl_enabled': 'bool',
        'referrals_enabled': 'bool',
        'max_referral_hops': 'int',
        'bind_dn': 'str',
        'bind_password': 'str',
        'password_type': 'str',
        'bind_secret': 'list[str]',
        'connect_timeout': 'int',
        'response_timeout': 'int',
        'use_recursive_group_membership_search': 'bool',
        'delegate_selectors': 'list[str]',
        'account_id': 'str',
        'setting_type': 'str'
    }

    attribute_map = {
        'host': 'host',
        'port': 'port',
        'ssl_enabled': 'sslEnabled',
        'referrals_enabled': 'referralsEnabled',
        'max_referral_hops': 'maxReferralHops',
        'bind_dn': 'bindDN',
        'bind_password': 'bindPassword',
        'password_type': 'passwordType',
        'bind_secret': 'bindSecret',
        'connect_timeout': 'connectTimeout',
        'response_timeout': 'responseTimeout',
        'use_recursive_group_membership_search': 'useRecursiveGroupMembershipSearch',
        'delegate_selectors': 'delegateSelectors',
        'account_id': 'accountId',
        'setting_type': 'settingType'
    }

    def __init__(self, host=None, port=None, ssl_enabled=None, referrals_enabled=None, max_referral_hops=None, bind_dn=None, bind_password=None, password_type=None, bind_secret=None, connect_timeout=None, response_timeout=None, use_recursive_group_membership_search=None, delegate_selectors=None, account_id=None, setting_type=None):  # noqa: E501
        """LdapConnectionSettings - a model defined in Swagger"""  # noqa: E501
        self._host = None
        self._port = None
        self._ssl_enabled = None
        self._referrals_enabled = None
        self._max_referral_hops = None
        self._bind_dn = None
        self._bind_password = None
        self._password_type = None
        self._bind_secret = None
        self._connect_timeout = None
        self._response_timeout = None
        self._use_recursive_group_membership_search = None
        self._delegate_selectors = None
        self._account_id = None
        self._setting_type = None
        self.discriminator = None
        self.host = host
        if port is not None:
            self.port = port
        if ssl_enabled is not None:
            self.ssl_enabled = ssl_enabled
        if referrals_enabled is not None:
            self.referrals_enabled = referrals_enabled
        if max_referral_hops is not None:
            self.max_referral_hops = max_referral_hops
        if bind_dn is not None:
            self.bind_dn = bind_dn
        if bind_password is not None:
            self.bind_password = bind_password
        if password_type is not None:
            self.password_type = password_type
        if bind_secret is not None:
            self.bind_secret = bind_secret
        if connect_timeout is not None:
            self.connect_timeout = connect_timeout
        if response_timeout is not None:
            self.response_timeout = response_timeout
        if use_recursive_group_membership_search is not None:
            self.use_recursive_group_membership_search = use_recursive_group_membership_search
        if delegate_selectors is not None:
            self.delegate_selectors = delegate_selectors
        if account_id is not None:
            self.account_id = account_id
        if setting_type is not None:
            self.setting_type = setting_type

    @property
    def host(self):
        """Gets the host of this LdapConnectionSettings.  # noqa: E501


        :return: The host of this LdapConnectionSettings.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this LdapConnectionSettings.


        :param host: The host of this LdapConnectionSettings.  # noqa: E501
        :type: str
        """
        if host is None:
            raise ValueError("Invalid value for `host`, must not be `None`")  # noqa: E501

        self._host = host

    @property
    def port(self):
        """Gets the port of this LdapConnectionSettings.  # noqa: E501


        :return: The port of this LdapConnectionSettings.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this LdapConnectionSettings.


        :param port: The port of this LdapConnectionSettings.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def ssl_enabled(self):
        """Gets the ssl_enabled of this LdapConnectionSettings.  # noqa: E501


        :return: The ssl_enabled of this LdapConnectionSettings.  # noqa: E501
        :rtype: bool
        """
        return self._ssl_enabled

    @ssl_enabled.setter
    def ssl_enabled(self, ssl_enabled):
        """Sets the ssl_enabled of this LdapConnectionSettings.


        :param ssl_enabled: The ssl_enabled of this LdapConnectionSettings.  # noqa: E501
        :type: bool
        """

        self._ssl_enabled = ssl_enabled

    @property
    def referrals_enabled(self):
        """Gets the referrals_enabled of this LdapConnectionSettings.  # noqa: E501


        :return: The referrals_enabled of this LdapConnectionSettings.  # noqa: E501
        :rtype: bool
        """
        return self._referrals_enabled

    @referrals_enabled.setter
    def referrals_enabled(self, referrals_enabled):
        """Sets the referrals_enabled of this LdapConnectionSettings.


        :param referrals_enabled: The referrals_enabled of this LdapConnectionSettings.  # noqa: E501
        :type: bool
        """

        self._referrals_enabled = referrals_enabled

    @property
    def max_referral_hops(self):
        """Gets the max_referral_hops of this LdapConnectionSettings.  # noqa: E501


        :return: The max_referral_hops of this LdapConnectionSettings.  # noqa: E501
        :rtype: int
        """
        return self._max_referral_hops

    @max_referral_hops.setter
    def max_referral_hops(self, max_referral_hops):
        """Sets the max_referral_hops of this LdapConnectionSettings.


        :param max_referral_hops: The max_referral_hops of this LdapConnectionSettings.  # noqa: E501
        :type: int
        """

        self._max_referral_hops = max_referral_hops

    @property
    def bind_dn(self):
        """Gets the bind_dn of this LdapConnectionSettings.  # noqa: E501


        :return: The bind_dn of this LdapConnectionSettings.  # noqa: E501
        :rtype: str
        """
        return self._bind_dn

    @bind_dn.setter
    def bind_dn(self, bind_dn):
        """Sets the bind_dn of this LdapConnectionSettings.


        :param bind_dn: The bind_dn of this LdapConnectionSettings.  # noqa: E501
        :type: str
        """

        self._bind_dn = bind_dn

    @property
    def bind_password(self):
        """Gets the bind_password of this LdapConnectionSettings.  # noqa: E501


        :return: The bind_password of this LdapConnectionSettings.  # noqa: E501
        :rtype: str
        """
        return self._bind_password

    @bind_password.setter
    def bind_password(self, bind_password):
        """Sets the bind_password of this LdapConnectionSettings.


        :param bind_password: The bind_password of this LdapConnectionSettings.  # noqa: E501
        :type: str
        """

        self._bind_password = bind_password

    @property
    def password_type(self):
        """Gets the password_type of this LdapConnectionSettings.  # noqa: E501


        :return: The password_type of this LdapConnectionSettings.  # noqa: E501
        :rtype: str
        """
        return self._password_type

    @password_type.setter
    def password_type(self, password_type):
        """Sets the password_type of this LdapConnectionSettings.


        :param password_type: The password_type of this LdapConnectionSettings.  # noqa: E501
        :type: str
        """

        self._password_type = password_type

    @property
    def bind_secret(self):
        """Gets the bind_secret of this LdapConnectionSettings.  # noqa: E501


        :return: The bind_secret of this LdapConnectionSettings.  # noqa: E501
        :rtype: list[str]
        """
        return self._bind_secret

    @bind_secret.setter
    def bind_secret(self, bind_secret):
        """Sets the bind_secret of this LdapConnectionSettings.


        :param bind_secret: The bind_secret of this LdapConnectionSettings.  # noqa: E501
        :type: list[str]
        """

        self._bind_secret = bind_secret

    @property
    def connect_timeout(self):
        """Gets the connect_timeout of this LdapConnectionSettings.  # noqa: E501


        :return: The connect_timeout of this LdapConnectionSettings.  # noqa: E501
        :rtype: int
        """
        return self._connect_timeout

    @connect_timeout.setter
    def connect_timeout(self, connect_timeout):
        """Sets the connect_timeout of this LdapConnectionSettings.


        :param connect_timeout: The connect_timeout of this LdapConnectionSettings.  # noqa: E501
        :type: int
        """

        self._connect_timeout = connect_timeout

    @property
    def response_timeout(self):
        """Gets the response_timeout of this LdapConnectionSettings.  # noqa: E501


        :return: The response_timeout of this LdapConnectionSettings.  # noqa: E501
        :rtype: int
        """
        return self._response_timeout

    @response_timeout.setter
    def response_timeout(self, response_timeout):
        """Sets the response_timeout of this LdapConnectionSettings.


        :param response_timeout: The response_timeout of this LdapConnectionSettings.  # noqa: E501
        :type: int
        """

        self._response_timeout = response_timeout

    @property
    def use_recursive_group_membership_search(self):
        """Gets the use_recursive_group_membership_search of this LdapConnectionSettings.  # noqa: E501


        :return: The use_recursive_group_membership_search of this LdapConnectionSettings.  # noqa: E501
        :rtype: bool
        """
        return self._use_recursive_group_membership_search

    @use_recursive_group_membership_search.setter
    def use_recursive_group_membership_search(self, use_recursive_group_membership_search):
        """Sets the use_recursive_group_membership_search of this LdapConnectionSettings.


        :param use_recursive_group_membership_search: The use_recursive_group_membership_search of this LdapConnectionSettings.  # noqa: E501
        :type: bool
        """

        self._use_recursive_group_membership_search = use_recursive_group_membership_search

    @property
    def delegate_selectors(self):
        """Gets the delegate_selectors of this LdapConnectionSettings.  # noqa: E501


        :return: The delegate_selectors of this LdapConnectionSettings.  # noqa: E501
        :rtype: list[str]
        """
        return self._delegate_selectors

    @delegate_selectors.setter
    def delegate_selectors(self, delegate_selectors):
        """Sets the delegate_selectors of this LdapConnectionSettings.


        :param delegate_selectors: The delegate_selectors of this LdapConnectionSettings.  # noqa: E501
        :type: list[str]
        """

        self._delegate_selectors = delegate_selectors

    @property
    def account_id(self):
        """Gets the account_id of this LdapConnectionSettings.  # noqa: E501


        :return: The account_id of this LdapConnectionSettings.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this LdapConnectionSettings.


        :param account_id: The account_id of this LdapConnectionSettings.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def setting_type(self):
        """Gets the setting_type of this LdapConnectionSettings.  # noqa: E501


        :return: The setting_type of this LdapConnectionSettings.  # noqa: E501
        :rtype: str
        """
        return self._setting_type

    @setting_type.setter
    def setting_type(self, setting_type):
        """Sets the setting_type of this LdapConnectionSettings.


        :param setting_type: The setting_type of this LdapConnectionSettings.  # noqa: E501
        :type: str
        """
        allowed_values = ["HOST_CONNECTION_ATTRIBUTES", "BASTION_HOST_CONNECTION_ATTRIBUTES", "SMTP", "SFTP", "JENKINS", "BAMBOO", "STRING", "SPLUNK", "ELK", "LOGZ", "SUMO", "DATA_DOG", "APM_VERIFICATION", "BUG_SNAG", "LOG_VERIFICATION", "APP_DYNAMICS", "NEW_RELIC", "DYNA_TRACE", "INSTANA", "DATA_DOG_LOG", "CLOUD_WATCH", "SCALYR", "ELB", "SLACK", "AWS", "GCS", "GCP", "AZURE", "PCF", "RANCHER", "DIRECT", "KUBERNETES_CLUSTER", "DOCKER", "ECR", "GCR", "ACR", "PHYSICAL_DATA_CENTER", "KUBERNETES", "NEXUS", "ARTIFACTORY", "SMB", "AMAZON_S3", "GIT", "SSH_SESSION_CONFIG", "SERVICE_VARIABLE", "CONFIG_FILE", "KMS", "GCP_KMS", "JIRA", "SERVICENOW", "SECRET_TEXT", "SECRET_FILE", "YAML_GIT_SYNC", "VAULT", "VAULT_SSH", "AWS_SECRETS_MANAGER", "WINRM_CONNECTION_ATTRIBUTES", "WINRM_SESSION_CONFIG", "PROMETHEUS", "INFRASTRUCTURE_MAPPING", "HTTP_HELM_REPO", "AMAZON_S3_HELM_REPO", "GCS_HELM_REPO", "SPOT_INST", "AZURE_ARTIFACTS_PAT", "CUSTOM", "CE_AWS", "CE_GCP", "CE_AZURE", "AZURE_VAULT", "KUBERNETES_CLUSTER_NG", "GIT_NG", "SSO_SAML", "LDAP", "GCP_SECRETS_MANAGER", "TRIGGER", "OCI_HELM_REPO"]  # noqa: E501
        if setting_type not in allowed_values:
            raise ValueError(
                "Invalid value for `setting_type` ({0}), must be one of {1}"  # noqa: E501
                .format(setting_type, allowed_values)
            )

        self._setting_type = setting_type

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
        if issubclass(LdapConnectionSettings, dict):
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
        if not isinstance(other, LdapConnectionSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
