# coding: utf-8

"""
    Harness NextGen Software Delivery Platform API Reference

    The Harness Software Delivery Platform uses OpenAPI Specification v3.0. Harness constantly improves these APIs. Please be aware that some improvements could cause breaking changes. # Introduction     The Harness API allows you to integrate and use all the services and modules we provide on the Harness Platform. If you use client-side SDKs, Harness functionality can be integrated with your client-side automation, helping you reduce manual efforts and deploy code faster.    For more information about how Harness works, read our [documentation](https://developer.harness.io/docs/getting-started) or visit the [Harness Developer Hub](https://developer.harness.io/).  ## How it works    The Harness API is a RESTful API that uses standard HTTP verbs. You can send requests in JSON, YAML, or form-data format. The format of the response matches the format of your request. You must send a single request at a time and ensure that you include your authentication key. For more information about this, go to [Authentication](#section/Introduction/Authentication).  ## Get started    Before you start integrating, get to know our API better by reading the following topics:    * [Harness key concepts](https://developer.harness.io/docs/getting-started/learn-harness-key-concepts/)   * [Authentication](#section/Introduction/Authentication)   * [Requests and responses](#section/Introduction/Requests-and-Responses)   * [Common Parameters](#section/Introduction/Common-Parameters-Beta)   * [Status Codes](#section/Introduction/Status-Codes)   * [Errors](#tag/Error-Response)   * [Versioning](#section/Introduction/Versioning-Beta)   * [Pagination](/#section/Introduction/Pagination-Beta)    The methods you need to integrate with depend on the functionality you want to use. Work with  your Harness Solutions Engineer to determine which methods you need.  ## Authentication  To authenticate with the Harness API, you need to:   1. Generate an API token on the Harness Platform.   2. Send the API token you generate in the `x-api-key` header in each request.  ### Generate an API token  To generate an API token, complete the following steps:   1. Go to the [Harness Platform](https://app.harness.io/).   2. On the left-hand navigation, click **My Profile**.   3. Click **+API Key**, enter a name for your key and then click **Save**.   4. Within the API Key tile, click **+Token**.   5. Enter a name for your token and click **Generate Token**. **Important**: Make sure to save your token securely. Harness does not store the API token for future reference, so make sure to save your token securely before you leave the page.  ### Send the API token in your requests  Send the token you created in the Harness Platform in the x-api-key header. For example:   `x-api-key: YOUR_API_KEY_HERE`  ## Requests and Responses    The structure for each request and response is outlined in the API documentation. We have examples in JSON and YAML for every request and response. You can use our online editor to test the examples.  ## Common Parameters [Beta]  | Field Name | Type    | Default | Description    | |------------|---------|---------|----------------| | identifier | string  | none    | URL-friendly version of the name, used to identify a resource within it's scope and so needs to be unique within the scope.                                                                                                            | | name       | string  | none    | Human-friendly name for the resource.                                                                                       | | org        | string  | none    | Limit to provided org identifiers.                                                                                                                     | | project    | string  | none    | Limit to provided project identifiers.                                                                                                                 | | description| string  | none    | More information about the specific resource.                                                                                    | | tags       | map[string]string  | none    | List of labels applied to the resource.                                                                                                                         | | order      | string  | desc    | Order to use when sorting the specified fields. Type: enum(asc,desc).                                                                                                                                     | | sort       | string  | none    | Fields on which to sort. Note: Specify the fields that you want to use for sorting. When doing so, consider the operational overhead of sorting fields. | | limit      | int     | 30      | Pagination: Number of items to return.                                                                                                                 | | page       | int     | 1       | Pagination page number strategy: Specify the page number within the paginated collection related to the number of items in each page.                  | | created    | int64   | none    | Unix timestamp that shows when the resource was created (in milliseconds).                                                               | | updated    | int64   | none    | Unix timestamp that shows when the resource was last edited (in milliseconds).                                                           |   ## Status Codes    Harness uses conventional HTTP status codes to indicate the status of an API request.    Generally, 2xx responses are reserved for success and 4xx status codes are reserved for failures. A 5xx response code indicates an error on the Harness server.    | Error Code  | Description |   |-------------|-------------|   | 200         |     OK      |   | 201         |   Created   |   | 202         |   Accepted  |   | 204         |  No Content |   | 400         | Bad Request |   | 401         | Unauthorized |   | 403         | Forbidden |   | 412         | Precondition Failed |   | 415         | Unsupported Media Type |   | 500         | Server Error |    To view our error response structures, go [here](#tag/Error-Response).  ## Versioning [Beta]  ### Harness Version   The current version of our Beta APIs is yet to be announced. The version number will use the date-header format and will be valid only for our Beta APIs.  ### Generation   All our beta APIs are versioned as a Generation, and this version is included in the path to every API resource. For example, v1 beta APIs begin with `app.harness.io/v1/`, where v1 is the API Generation.    The version number represents the core API and does not change frequently. The version number changes only if there is a significant departure from the basic underpinnings of the existing API. For example, when Harness performs a system-wide refactoring of core concepts or resources.  ## Pagination [Beta]  We use pagination to place limits on the number of responses associated with list endpoints. Pagination is achieved by the use of limit query parameters. The limit defaults to 30. Its maximum value is 100.  Following are the pagination headers supported in the response bodies of paginated APIs:   1. X-Total-Elements : Indicates the total number of entries in a paginated response.   2. X-Page-Number : Indicates the page number currently returned for a paginated response.   3. X-Page-Size : Indicates the number of entries per page for a paginated response.  For example:    ``` X-Total-Elements : 30 X-Page-Number : 0 X-Page-Size : 10   ```   # noqa: E501

    OpenAPI spec version: 1.0
    Contact: contact@harness.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.authentication_settings_api import AuthenticationSettingsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestAuthenticationSettingsApi(unittest.TestCase):
    """AuthenticationSettingsApi unit test stubs"""

    def setUp(self):
        self.api = AuthenticationSettingsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_ldap_settings(self):
        """Test case for create_ldap_settings

        Create Ldap setting  # noqa: E501
        """
        pass

    def test_delete_ldap_settings(self):
        """Test case for delete_ldap_settings

        Delete Ldap settings  # noqa: E501
        """
        pass

    def test_delete_saml_meta_data(self):
        """Test case for delete_saml_meta_data

        Delete SAML meta data  # noqa: E501
        """
        pass

    def test_delete_saml_meta_data_for_saml_ssoid(self):
        """Test case for delete_saml_meta_data_for_saml_ssoid

        Delete SAML meta data for given SAML sso id  # noqa: E501
        """
        pass

    def test_enable_disable_authentication_for_saml_setting(self):
        """Test case for enable_disable_authentication_for_saml_setting

        Update authentication enabled or not for given SAML setting  # noqa: E501
        """
        pass

    def test_get_authentication_settings(self):
        """Test case for get_authentication_settings

        Gets authentication settings for the given Account ID  # noqa: E501
        """
        pass

    def test_get_authentication_settings_v2(self):
        """Test case for get_authentication_settings_v2

        Gets authentication settings version 2 for the given Account ID  # noqa: E501
        """
        pass

    def test_get_ldap_settings(self):
        """Test case for get_ldap_settings

        Return configured Ldap settings for the account  # noqa: E501
        """
        pass

    def test_get_password_strength_settings(self):
        """Test case for get_password_strength_settings

        Get password strength  # noqa: E501
        """
        pass

    def test_get_saml_login_test(self):
        """Test case for get_saml_login_test

        Test SAML connectivity  # noqa: E501
        """
        pass

    def test_get_saml_login_test_v2(self):
        """Test case for get_saml_login_test_v2

        Test SAML connectivity  # noqa: E501
        """
        pass

    def test_remove_oauth_mechanism(self):
        """Test case for remove_oauth_mechanism

        Delete OAuth Setting  # noqa: E501
        """
        pass

    def test_set_public_access(self):
        """Test case for set_public_access

        Enable/disable public access at account level  # noqa: E501
        """
        pass

    def test_set_session_timeout_at_account_level(self):
        """Test case for set_session_timeout_at_account_level

        Set session timeout at account level  # noqa: E501
        """
        pass

    def test_set_two_factor_auth_at_account_level(self):
        """Test case for set_two_factor_auth_at_account_level

        Set two factor authorization  # noqa: E501
        """
        pass

    def test_update_auth_mechanism(self):
        """Test case for update_auth_mechanism

        Update Auth mechanism  # noqa: E501
        """
        pass

    def test_update_ldap_settings(self):
        """Test case for update_ldap_settings

        Updates Ldap setting  # noqa: E501
        """
        pass

    def test_update_oauth_providers(self):
        """Test case for update_oauth_providers

        Update Oauth providers  # noqa: E501
        """
        pass

    def test_update_saml_meta_data(self):
        """Test case for update_saml_meta_data

        Update SAML metadata  # noqa: E501
        """
        pass

    def test_update_saml_meta_data_for_saml_ssoid(self):
        """Test case for update_saml_meta_data_for_saml_ssoid

        Update SAML metadata for a given SAML SSO Id  # noqa: E501
        """
        pass

    def test_update_whitelisted_domains(self):
        """Test case for update_whitelisted_domains

        Updates the whitelisted domains  # noqa: E501
        """
        pass

    def test_upload_saml_meta_data(self):
        """Test case for upload_saml_meta_data

        Upload SAML metadata  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
