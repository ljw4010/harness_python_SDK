# coding: utf-8

"""
    Harness NextGen Software Delivery Platform API Reference

    The Harness Software Delivery Platform uses OpenAPI Specification v3.0. Harness constantly improves these APIs. Please be aware that some improvements could cause breaking changes. # Introduction     The Harness API allows you to integrate and use all the services and modules we provide on the Harness Platform. If you use client-side SDKs, Harness functionality can be integrated with your client-side automation, helping you reduce manual efforts and deploy code faster.    For more information about how Harness works, read our [documentation](https://developer.harness.io/docs/getting-started) or visit the [Harness Developer Hub](https://developer.harness.io/).  ## How it works    The Harness API is a RESTful API that uses standard HTTP verbs. You can send requests in JSON, YAML, or form-data format. The format of the response matches the format of your request. You must send a single request at a time and ensure that you include your authentication key. For more information about this, go to [Authentication](#section/Introduction/Authentication).  ## Get started    Before you start integrating, get to know our API better by reading the following topics:    * [Harness key concepts](https://developer.harness.io/docs/getting-started/learn-harness-key-concepts/)   * [Authentication](#section/Introduction/Authentication)   * [Requests and responses](#section/Introduction/Requests-and-Responses)   * [Common Parameters](#section/Introduction/Common-Parameters-Beta)   * [Status Codes](#section/Introduction/Status-Codes)   * [Errors](#tag/Error-Response)   * [Versioning](#section/Introduction/Versioning-Beta)   * [Pagination](/#section/Introduction/Pagination-Beta)    The methods you need to integrate with depend on the functionality you want to use. Work with  your Harness Solutions Engineer to determine which methods you need.  ## Authentication  To authenticate with the Harness API, you need to:   1. Generate an API token on the Harness Platform.   2. Send the API token you generate in the `x-api-key` header in each request.  ### Generate an API token  To generate an API token, complete the following steps:   1. Go to the [Harness Platform](https://app.harness.io/).   2. On the left-hand navigation, click **My Profile**.   3. Click **+API Key**, enter a name for your key and then click **Save**.   4. Within the API Key tile, click **+Token**.   5. Enter a name for your token and click **Generate Token**. **Important**: Make sure to save your token securely. Harness does not store the API token for future reference, so make sure to save your token securely before you leave the page.  ### Send the API token in your requests  Send the token you created in the Harness Platform in the x-api-key header. For example:   `x-api-key: YOUR_API_KEY_HERE`  ## Requests and Responses    The structure for each request and response is outlined in the API documentation. We have examples in JSON and YAML for every request and response. You can use our online editor to test the examples.  ## Common Parameters [Beta]  | Field Name | Type    | Default | Description    | |------------|---------|---------|----------------| | identifier | string  | none    | URL-friendly version of the name, used to identify a resource within it's scope and so needs to be unique within the scope.                                                                                                            | | name       | string  | none    | Human-friendly name for the resource.                                                                                       | | org        | string  | none    | Limit to provided org identifiers.                                                                                                                     | | project    | string  | none    | Limit to provided project identifiers.                                                                                                                 | | description| string  | none    | More information about the specific resource.                                                                                    | | tags       | map[string]string  | none    | List of labels applied to the resource.                                                                                                                         | | order      | string  | desc    | Order to use when sorting the specified fields. Type: enum(asc,desc).                                                                                                                                     | | sort       | string  | none    | Fields on which to sort. Note: Specify the fields that you want to use for sorting. When doing so, consider the operational overhead of sorting fields. | | limit      | int     | 30      | Pagination: Number of items to return.                                                                                                                 | | page       | int     | 1       | Pagination page number strategy: Specify the page number within the paginated collection related to the number of items in each page.                  | | created    | int64   | none    | Unix timestamp that shows when the resource was created (in milliseconds).                                                               | | updated    | int64   | none    | Unix timestamp that shows when the resource was last edited (in milliseconds).                                                           |   ## Status Codes    Harness uses conventional HTTP status codes to indicate the status of an API request.    Generally, 2xx responses are reserved for success and 4xx status codes are reserved for failures. A 5xx response code indicates an error on the Harness server.    | Error Code  | Description |   |-------------|-------------|   | 200         |     OK      |   | 201         |   Created   |   | 202         |   Accepted  |   | 204         |  No Content |   | 400         | Bad Request |   | 401         | Unauthorized |   | 403         | Forbidden |   | 412         | Precondition Failed |   | 415         | Unsupported Media Type |   | 500         | Server Error |    To view our error response structures, go [here](#tag/Error-Response).  ## Versioning [Beta]  ### Harness Version   The current version of our Beta APIs is yet to be announced. The version number will use the date-header format and will be valid only for our Beta APIs.  ### Generation   All our beta APIs are versioned as a Generation, and this version is included in the path to every API resource. For example, v1 beta APIs begin with `app.harness.io/v1/`, where v1 is the API Generation.    The version number represents the core API and does not change frequently. The version number changes only if there is a significant departure from the basic underpinnings of the existing API. For example, when Harness performs a system-wide refactoring of core concepts or resources.  ## Pagination [Beta]  We use pagination to place limits on the number of responses associated with list endpoints. Pagination is achieved by the use of limit query parameters. The limit defaults to 30. Its maximum value is 100.  Following are the pagination headers supported in the response bodies of paginated APIs:   1. X-Total-Elements : Indicates the total number of entries in a paginated response.   2. X-Page-Number : Indicates the page number currently returned for a paginated response.   3. X-Page-Size : Indicates the number of entries per page for a paginated response.  For example:    ``` X-Total-Elements : 30 X-Page-Number : 0 X-Page-Size : 10   ```   # noqa: E501

    OpenAPI spec version: 1.0
    Contact: contact@harness.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from harness_python_sdk.api_client import ApiClient


class AuthenticationSettingsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_ldap_settings(self, body, account_identifier, **kwargs):  # noqa: E501
        """Create Ldap setting  # noqa: E501

        Creates Ldap settings along with the user, group queries.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_ldap_settings(body, account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param LDAPSettings body: Create LdapSettings request body. Values for connection settings are needed, user and group settings can also be provided (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :return: RestResponseLDAPSettings
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_ldap_settings_with_http_info(body, account_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.create_ldap_settings_with_http_info(body, account_identifier, **kwargs)  # noqa: E501
            return data

    def create_ldap_settings_with_http_info(self, body, account_identifier, **kwargs):  # noqa: E501
        """Create Ldap setting  # noqa: E501

        Creates Ldap settings along with the user, group queries.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_ldap_settings_with_http_info(body, account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param LDAPSettings body: Create LdapSettings request body. Values for connection settings are needed, user and group settings can also be provided (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :return: RestResponseLDAPSettings
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'account_identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_ldap_settings" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_ldap_settings`")  # noqa: E501
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `create_ldap_settings`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/yaml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/ng/api/authentication-settings/ldap/settings', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RestResponseLDAPSettings',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_ldap_settings(self, account_identifier, **kwargs):  # noqa: E501
        """Delete Ldap settings  # noqa: E501

        Delete configured Ldap settings on this account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_ldap_settings(account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :return: RestResponseBoolean
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_ldap_settings_with_http_info(account_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_ldap_settings_with_http_info(account_identifier, **kwargs)  # noqa: E501
            return data

    def delete_ldap_settings_with_http_info(self, account_identifier, **kwargs):  # noqa: E501
        """Delete Ldap settings  # noqa: E501

        Delete configured Ldap settings on this account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_ldap_settings_with_http_info(account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :return: RestResponseBoolean
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_ldap_settings" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `delete_ldap_settings`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/yaml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/ng/api/authentication-settings/ldap/settings', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RestResponseBoolean',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_saml_meta_data(self, account_identifier, **kwargs):  # noqa: E501
        """Delete SAML meta data  # noqa: E501

        Deletes SAML metadata for the given Account ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_saml_meta_data(account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :return: RestResponseSSOConfig
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_saml_meta_data_with_http_info(account_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_saml_meta_data_with_http_info(account_identifier, **kwargs)  # noqa: E501
            return data

    def delete_saml_meta_data_with_http_info(self, account_identifier, **kwargs):  # noqa: E501
        """Delete SAML meta data  # noqa: E501

        Deletes SAML metadata for the given Account ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_saml_meta_data_with_http_info(account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :return: RestResponseSSOConfig
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_saml_meta_data" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `delete_saml_meta_data`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/yaml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/ng/api/authentication-settings/delete-saml-metadata', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RestResponseSSOConfig',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_saml_meta_data_for_saml_ssoid(self, account_identifier, saml_ssoid, **kwargs):  # noqa: E501
        """Delete SAML meta data for given SAML sso id  # noqa: E501

        Deletes SAML metadata for the given Account and SAML sso id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_saml_meta_data_for_saml_ssoid(account_identifier, saml_ssoid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str saml_ssoid: Saml Settings Identifier (required)
        :return: RestResponseSSOConfig
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_saml_meta_data_for_saml_ssoid_with_http_info(account_identifier, saml_ssoid, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_saml_meta_data_for_saml_ssoid_with_http_info(account_identifier, saml_ssoid, **kwargs)  # noqa: E501
            return data

    def delete_saml_meta_data_for_saml_ssoid_with_http_info(self, account_identifier, saml_ssoid, **kwargs):  # noqa: E501
        """Delete SAML meta data for given SAML sso id  # noqa: E501

        Deletes SAML metadata for the given Account and SAML sso id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_saml_meta_data_for_saml_ssoid_with_http_info(account_identifier, saml_ssoid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str saml_ssoid: Saml Settings Identifier (required)
        :return: RestResponseSSOConfig
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_identifier', 'saml_ssoid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_saml_meta_data_for_saml_ssoid" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `delete_saml_meta_data_for_saml_ssoid`")  # noqa: E501
        # verify the required parameter 'saml_ssoid' is set
        if ('saml_ssoid' not in params or
                params['saml_ssoid'] is None):
            raise ValueError("Missing the required parameter `saml_ssoid` when calling `delete_saml_meta_data_for_saml_ssoid`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'saml_ssoid' in params:
            path_params['samlSSOId'] = params['saml_ssoid']  # noqa: E501

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/yaml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/ng/api/authentication-settings/saml-metadata/{samlSSOId}/delete', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RestResponseSSOConfig',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def enable_disable_authentication_for_saml_setting(self, account_identifier, enable, saml_ssoid, **kwargs):  # noqa: E501
        """Update authentication enabled or not for given SAML setting  # noqa: E501

        Updates if authentication is enabled or not for given SAML setting in Account ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.enable_disable_authentication_for_saml_setting(account_identifier, enable, saml_ssoid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param bool enable: (required)
        :param str saml_ssoid: Saml Settings Identifier (required)
        :return: RestResponseBoolean
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.enable_disable_authentication_for_saml_setting_with_http_info(account_identifier, enable, saml_ssoid, **kwargs)  # noqa: E501
        else:
            (data) = self.enable_disable_authentication_for_saml_setting_with_http_info(account_identifier, enable, saml_ssoid, **kwargs)  # noqa: E501
            return data

    def enable_disable_authentication_for_saml_setting_with_http_info(self, account_identifier, enable, saml_ssoid, **kwargs):  # noqa: E501
        """Update authentication enabled or not for given SAML setting  # noqa: E501

        Updates if authentication is enabled or not for given SAML setting in Account ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.enable_disable_authentication_for_saml_setting_with_http_info(account_identifier, enable, saml_ssoid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param bool enable: (required)
        :param str saml_ssoid: Saml Settings Identifier (required)
        :return: RestResponseBoolean
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_identifier', 'enable', 'saml_ssoid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method enable_disable_authentication_for_saml_setting" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `enable_disable_authentication_for_saml_setting`")  # noqa: E501
        # verify the required parameter 'enable' is set
        if ('enable' not in params or
                params['enable'] is None):
            raise ValueError("Missing the required parameter `enable` when calling `enable_disable_authentication_for_saml_setting`")  # noqa: E501
        # verify the required parameter 'saml_ssoid' is set
        if ('saml_ssoid' not in params or
                params['saml_ssoid'] is None):
            raise ValueError("Missing the required parameter `saml_ssoid` when calling `enable_disable_authentication_for_saml_setting`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'saml_ssoid' in params:
            path_params['samlSSOId'] = params['saml_ssoid']  # noqa: E501

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501
        if 'enable' in params:
            query_params.append(('enable', params['enable']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/yaml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/ng/api/authentication-settings/saml-metadata-upload/{samlSSOId}/authentication', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RestResponseBoolean',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_authentication_settings(self, account_identifier, **kwargs):  # noqa: E501
        """Gets authentication settings for the given Account ID  # noqa: E501

        Gets authentication settings for the given Account ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_authentication_settings(account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :return: RestResponseAuthenticationSettingsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_authentication_settings_with_http_info(account_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.get_authentication_settings_with_http_info(account_identifier, **kwargs)  # noqa: E501
            return data

    def get_authentication_settings_with_http_info(self, account_identifier, **kwargs):  # noqa: E501
        """Gets authentication settings for the given Account ID  # noqa: E501

        Gets authentication settings for the given Account ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_authentication_settings_with_http_info(account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :return: RestResponseAuthenticationSettingsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_authentication_settings" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `get_authentication_settings`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/yaml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/ng/api/authentication-settings', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RestResponseAuthenticationSettingsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_authentication_settings_v2(self, account_identifier, **kwargs):  # noqa: E501
        """Gets authentication settings version 2 for the given Account ID  # noqa: E501

        Gets authentication settings version 2 for the given Account ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_authentication_settings_v2(account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :return: RestResponseAuthenticationSettingsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_authentication_settings_v2_with_http_info(account_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.get_authentication_settings_v2_with_http_info(account_identifier, **kwargs)  # noqa: E501
            return data

    def get_authentication_settings_v2_with_http_info(self, account_identifier, **kwargs):  # noqa: E501
        """Gets authentication settings version 2 for the given Account ID  # noqa: E501

        Gets authentication settings version 2 for the given Account ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_authentication_settings_v2_with_http_info(account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :return: RestResponseAuthenticationSettingsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_authentication_settings_v2" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `get_authentication_settings_v2`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/yaml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/ng/api/authentication-settings/v2', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RestResponseAuthenticationSettingsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_ldap_settings(self, account_identifier, **kwargs):  # noqa: E501
        """Return configured Ldap settings for the account  # noqa: E501

        Returns configured Ldap settings and its details for the account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_ldap_settings(account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :return: RestResponseLDAPSettings
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_ldap_settings_with_http_info(account_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.get_ldap_settings_with_http_info(account_identifier, **kwargs)  # noqa: E501
            return data

    def get_ldap_settings_with_http_info(self, account_identifier, **kwargs):  # noqa: E501
        """Return configured Ldap settings for the account  # noqa: E501

        Returns configured Ldap settings and its details for the account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_ldap_settings_with_http_info(account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :return: RestResponseLDAPSettings
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_ldap_settings" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `get_ldap_settings`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/yaml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/ng/api/authentication-settings/ldap/settings', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RestResponseLDAPSettings',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_password_strength_settings(self, account_identifier, **kwargs):  # noqa: E501
        """Get password strength  # noqa: E501

        Gets password strength for the given Account ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_password_strength_settings(account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :return: RestResponsePasswordStrengthPolicy
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_password_strength_settings_with_http_info(account_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.get_password_strength_settings_with_http_info(account_identifier, **kwargs)  # noqa: E501
            return data

    def get_password_strength_settings_with_http_info(self, account_identifier, **kwargs):  # noqa: E501
        """Get password strength  # noqa: E501

        Gets password strength for the given Account ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_password_strength_settings_with_http_info(account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :return: RestResponsePasswordStrengthPolicy
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_password_strength_settings" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `get_password_strength_settings`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/yaml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/ng/api/authentication-settings/login-settings/password-strength', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RestResponsePasswordStrengthPolicy',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_saml_login_test(self, account_id, **kwargs):  # noqa: E501
        """Test SAML connectivity  # noqa: E501

        Tests SAML connectivity for the given Account ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_saml_login_test(account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity. (required)
        :return: RestResponseLoginTypeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_saml_login_test_with_http_info(account_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_saml_login_test_with_http_info(account_id, **kwargs)  # noqa: E501
            return data

    def get_saml_login_test_with_http_info(self, account_id, **kwargs):  # noqa: E501
        """Test SAML connectivity  # noqa: E501

        Tests SAML connectivity for the given Account ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_saml_login_test_with_http_info(account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity. (required)
        :return: RestResponseLoginTypeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_saml_login_test" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `get_saml_login_test`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'account_id' in params:
            query_params.append(('accountId', params['account_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/yaml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/ng/api/authentication-settings/saml-login-test', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RestResponseLoginTypeResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_saml_login_test_v2(self, account_identifier, saml_ssoid, **kwargs):  # noqa: E501
        """Test SAML connectivity  # noqa: E501

        Tests SAML connectivity for the given Account ID and SAML setting.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_saml_login_test_v2(account_identifier, saml_ssoid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str saml_ssoid: Saml Settings Identifier (required)
        :return: RestResponseLoginTypeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_saml_login_test_v2_with_http_info(account_identifier, saml_ssoid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_saml_login_test_v2_with_http_info(account_identifier, saml_ssoid, **kwargs)  # noqa: E501
            return data

    def get_saml_login_test_v2_with_http_info(self, account_identifier, saml_ssoid, **kwargs):  # noqa: E501
        """Test SAML connectivity  # noqa: E501

        Tests SAML connectivity for the given Account ID and SAML setting.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_saml_login_test_v2_with_http_info(account_identifier, saml_ssoid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str saml_ssoid: Saml Settings Identifier (required)
        :return: RestResponseLoginTypeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_identifier', 'saml_ssoid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_saml_login_test_v2" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `get_saml_login_test_v2`")  # noqa: E501
        # verify the required parameter 'saml_ssoid' is set
        if ('saml_ssoid' not in params or
                params['saml_ssoid'] is None):
            raise ValueError("Missing the required parameter `saml_ssoid` when calling `get_saml_login_test_v2`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'saml_ssoid' in params:
            path_params['samlSSOId'] = params['saml_ssoid']  # noqa: E501

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/yaml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/ng/api/authentication-settings/saml-login-test/{samlSSOId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RestResponseLoginTypeResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def remove_oauth_mechanism(self, account_identifier, **kwargs):  # noqa: E501
        """Delete OAuth Setting  # noqa: E501

        Deletes OAuth settings for a given Account ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_oauth_mechanism(account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :return: RestResponseBoolean
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_oauth_mechanism_with_http_info(account_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_oauth_mechanism_with_http_info(account_identifier, **kwargs)  # noqa: E501
            return data

    def remove_oauth_mechanism_with_http_info(self, account_identifier, **kwargs):  # noqa: E501
        """Delete OAuth Setting  # noqa: E501

        Deletes OAuth settings for a given Account ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_oauth_mechanism_with_http_info(account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :return: RestResponseBoolean
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_oauth_mechanism" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `remove_oauth_mechanism`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/yaml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/ng/api/authentication-settings/oauth/remove-mechanism', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RestResponseBoolean',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def set_public_access(self, body, account_identifier, **kwargs):  # noqa: E501
        """Enable/disable public access at account level  # noqa: E501

        Enable/disable public access for the given Account ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_public_access(body, account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool body: Information about the session timeout for all users of this account in minutes. (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :return: RestResponseBoolean
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.set_public_access_with_http_info(body, account_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.set_public_access_with_http_info(body, account_identifier, **kwargs)  # noqa: E501
            return data

    def set_public_access_with_http_info(self, body, account_identifier, **kwargs):  # noqa: E501
        """Enable/disable public access at account level  # noqa: E501

        Enable/disable public access for the given Account ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_public_access_with_http_info(body, account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool body: Information about the session timeout for all users of this account in minutes. (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :return: RestResponseBoolean
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'account_identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method set_public_access" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `set_public_access`")  # noqa: E501
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `set_public_access`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/yaml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/ng/api/authentication-settings/public-access', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RestResponseBoolean',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def set_session_timeout_at_account_level(self, body, account_identifier, **kwargs):  # noqa: E501
        """Set session timeout at account level  # noqa: E501

        Sets session timeout of all users for the given Account ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_session_timeout_at_account_level(body, account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SessionTimeoutSettings body: Information about the session timeout for all users of this account in minutes. (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :return: RestResponseBoolean
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.set_session_timeout_at_account_level_with_http_info(body, account_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.set_session_timeout_at_account_level_with_http_info(body, account_identifier, **kwargs)  # noqa: E501
            return data

    def set_session_timeout_at_account_level_with_http_info(self, body, account_identifier, **kwargs):  # noqa: E501
        """Set session timeout at account level  # noqa: E501

        Sets session timeout of all users for the given Account ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_session_timeout_at_account_level_with_http_info(body, account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SessionTimeoutSettings body: Information about the session timeout for all users of this account in minutes. (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :return: RestResponseBoolean
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'account_identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method set_session_timeout_at_account_level" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `set_session_timeout_at_account_level`")  # noqa: E501
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `set_session_timeout_at_account_level`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/yaml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/ng/api/authentication-settings/session-timeout-account-level', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RestResponseBoolean',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def set_two_factor_auth_at_account_level(self, body, account_identifier, **kwargs):  # noqa: E501
        """Set two factor authorization  # noqa: E501

        Sets Two-Factor authorization for the given Account ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_two_factor_auth_at_account_level(body, account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TwoFactorAdminOverrideSettings body: Boolean that specify whether or not to override two factor enabled setting (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :return: RestResponseBoolean
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.set_two_factor_auth_at_account_level_with_http_info(body, account_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.set_two_factor_auth_at_account_level_with_http_info(body, account_identifier, **kwargs)  # noqa: E501
            return data

    def set_two_factor_auth_at_account_level_with_http_info(self, body, account_identifier, **kwargs):  # noqa: E501
        """Set two factor authorization  # noqa: E501

        Sets Two-Factor authorization for the given Account ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_two_factor_auth_at_account_level_with_http_info(body, account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TwoFactorAdminOverrideSettings body: Boolean that specify whether or not to override two factor enabled setting (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :return: RestResponseBoolean
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'account_identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method set_two_factor_auth_at_account_level" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `set_two_factor_auth_at_account_level`")  # noqa: E501
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `set_two_factor_auth_at_account_level`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/yaml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/ng/api/authentication-settings/two-factor-admin-override-settings', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RestResponseBoolean',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_auth_mechanism(self, account_identifier, **kwargs):  # noqa: E501
        """Update Auth mechanism  # noqa: E501

        Updates the authentication mechanism for the given Account ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_auth_mechanism(account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str authentication_mechanism: Type of Authentication Mechanism SSO or NON_SSO
        :return: RestResponseBoolean
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_auth_mechanism_with_http_info(account_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.update_auth_mechanism_with_http_info(account_identifier, **kwargs)  # noqa: E501
            return data

    def update_auth_mechanism_with_http_info(self, account_identifier, **kwargs):  # noqa: E501
        """Update Auth mechanism  # noqa: E501

        Updates the authentication mechanism for the given Account ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_auth_mechanism_with_http_info(account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str authentication_mechanism: Type of Authentication Mechanism SSO or NON_SSO
        :return: RestResponseBoolean
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_identifier', 'authentication_mechanism']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_auth_mechanism" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `update_auth_mechanism`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501
        if 'authentication_mechanism' in params:
            query_params.append(('authenticationMechanism', params['authentication_mechanism']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/yaml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/ng/api/authentication-settings/update-auth-mechanism', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RestResponseBoolean',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_ldap_settings(self, body, account_identifier, **kwargs):  # noqa: E501
        """Updates Ldap setting  # noqa: E501

        Updates configured Ldap settings along with the user, group queries.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_ldap_settings(body, account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param LDAPSettings body: This is the updated LdapSettings. Values for all fields is needed, not just the fields you are updating (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :return: RestResponseLDAPSettings
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_ldap_settings_with_http_info(body, account_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.update_ldap_settings_with_http_info(body, account_identifier, **kwargs)  # noqa: E501
            return data

    def update_ldap_settings_with_http_info(self, body, account_identifier, **kwargs):  # noqa: E501
        """Updates Ldap setting  # noqa: E501

        Updates configured Ldap settings along with the user, group queries.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_ldap_settings_with_http_info(body, account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param LDAPSettings body: This is the updated LdapSettings. Values for all fields is needed, not just the fields you are updating (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :return: RestResponseLDAPSettings
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'account_identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_ldap_settings" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_ldap_settings`")  # noqa: E501
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `update_ldap_settings`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/yaml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/ng/api/authentication-settings/ldap/settings', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RestResponseLDAPSettings',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_oauth_providers(self, body, account_identifier, **kwargs):  # noqa: E501
        """Update Oauth providers  # noqa: E501

        Updates OAuth providers for the given Account ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_oauth_providers(body, account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param OAuthSettings body: This is the updated OAuthSettings. Please provide values for all fields, not just the fields you are updating (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :return: RestResponseBoolean
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_oauth_providers_with_http_info(body, account_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.update_oauth_providers_with_http_info(body, account_identifier, **kwargs)  # noqa: E501
            return data

    def update_oauth_providers_with_http_info(self, body, account_identifier, **kwargs):  # noqa: E501
        """Update Oauth providers  # noqa: E501

        Updates OAuth providers for the given Account ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_oauth_providers_with_http_info(body, account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param OAuthSettings body: This is the updated OAuthSettings. Please provide values for all fields, not just the fields you are updating (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :return: RestResponseBoolean
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'account_identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_oauth_providers" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_oauth_providers`")  # noqa: E501
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `update_oauth_providers`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/yaml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/ng/api/authentication-settings/oauth/update-providers', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RestResponseBoolean',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_saml_meta_data(self, account_id, **kwargs):  # noqa: E501
        """Update SAML metadata  # noqa: E501

        Updates SAML metadata of the SAML configuration configured for an account  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_saml_meta_data(account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity. (required)
        :param object file:
        :param FormDataContentDisposition file_metadata:
        :param str display_name:
        :param str group_membership_attr:
        :param bool authorization_enabled:
        :param str logout_url:
        :param str entity_identifier:
        :param str saml_provider_type:
        :param str client_id:
        :param str client_secret:
        :param bool jit_enabled:
        :param str jit_validation_key:
        :param str jit_validation_value:
        :return: RestResponseSSOConfig
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_saml_meta_data_with_http_info(account_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_saml_meta_data_with_http_info(account_id, **kwargs)  # noqa: E501
            return data

    def update_saml_meta_data_with_http_info(self, account_id, **kwargs):  # noqa: E501
        """Update SAML metadata  # noqa: E501

        Updates SAML metadata of the SAML configuration configured for an account  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_saml_meta_data_with_http_info(account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity. (required)
        :param object file:
        :param FormDataContentDisposition file_metadata:
        :param str display_name:
        :param str group_membership_attr:
        :param bool authorization_enabled:
        :param str logout_url:
        :param str entity_identifier:
        :param str saml_provider_type:
        :param str client_id:
        :param str client_secret:
        :param bool jit_enabled:
        :param str jit_validation_key:
        :param str jit_validation_value:
        :return: RestResponseSSOConfig
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'file', 'file_metadata', 'display_name', 'group_membership_attr', 'authorization_enabled', 'logout_url', 'entity_identifier', 'saml_provider_type', 'client_id', 'client_secret', 'jit_enabled', 'jit_validation_key', 'jit_validation_value']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_saml_meta_data" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `update_saml_meta_data`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'account_id' in params:
            query_params.append(('accountId', params['account_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'file' in params:
            form_params.append(('file', params['file']))  # noqa: E501
        if 'file_metadata' in params:
            form_params.append(('fileMetadata', params['file_metadata']))  # noqa: E501
        if 'display_name' in params:
            form_params.append(('displayName', params['display_name']))  # noqa: E501
        if 'group_membership_attr' in params:
            form_params.append(('groupMembershipAttr', params['group_membership_attr']))  # noqa: E501
        if 'authorization_enabled' in params:
            form_params.append(('authorizationEnabled', params['authorization_enabled']))  # noqa: E501
        if 'logout_url' in params:
            form_params.append(('logoutUrl', params['logout_url']))  # noqa: E501
        if 'entity_identifier' in params:
            form_params.append(('entityIdentifier', params['entity_identifier']))  # noqa: E501
        if 'saml_provider_type' in params:
            form_params.append(('samlProviderType', params['saml_provider_type']))  # noqa: E501
        if 'client_id' in params:
            form_params.append(('clientId', params['client_id']))  # noqa: E501
        if 'client_secret' in params:
            form_params.append(('clientSecret', params['client_secret']))  # noqa: E501
        if 'jit_enabled' in params:
            form_params.append(('jitEnabled', params['jit_enabled']))  # noqa: E501
        if 'jit_validation_key' in params:
            form_params.append(('jitValidationKey', params['jit_validation_key']))  # noqa: E501
        if 'jit_validation_value' in params:
            form_params.append(('jitValidationValue', params['jit_validation_value']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/yaml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/ng/api/authentication-settings/saml-metadata-upload', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RestResponseSSOConfig',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_saml_meta_data_for_saml_ssoid(self, account_identifier, saml_ssoid, **kwargs):  # noqa: E501
        """Update SAML metadata for a given SAML SSO Id  # noqa: E501

        Updates SAML metadata of the SAML configuration with given SSO Id, configured for an account  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_saml_meta_data_for_saml_ssoid(account_identifier, saml_ssoid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str saml_ssoid: Saml Settings Identifier (required)
        :param object file:
        :param FormDataContentDisposition file_metadata:
        :param str display_name:
        :param str group_membership_attr:
        :param bool authorization_enabled:
        :param str logout_url:
        :param str entity_identifier:
        :param str saml_provider_type:
        :param str client_id:
        :param str client_secret:
        :param str friendly_saml_name:
        :param bool jit_enabled:
        :param str jit_validation_key:
        :param str jit_validation_value:
        :return: RestResponseSSOConfig
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_saml_meta_data_for_saml_ssoid_with_http_info(account_identifier, saml_ssoid, **kwargs)  # noqa: E501
        else:
            (data) = self.update_saml_meta_data_for_saml_ssoid_with_http_info(account_identifier, saml_ssoid, **kwargs)  # noqa: E501
            return data

    def update_saml_meta_data_for_saml_ssoid_with_http_info(self, account_identifier, saml_ssoid, **kwargs):  # noqa: E501
        """Update SAML metadata for a given SAML SSO Id  # noqa: E501

        Updates SAML metadata of the SAML configuration with given SSO Id, configured for an account  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_saml_meta_data_for_saml_ssoid_with_http_info(account_identifier, saml_ssoid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str saml_ssoid: Saml Settings Identifier (required)
        :param object file:
        :param FormDataContentDisposition file_metadata:
        :param str display_name:
        :param str group_membership_attr:
        :param bool authorization_enabled:
        :param str logout_url:
        :param str entity_identifier:
        :param str saml_provider_type:
        :param str client_id:
        :param str client_secret:
        :param str friendly_saml_name:
        :param bool jit_enabled:
        :param str jit_validation_key:
        :param str jit_validation_value:
        :return: RestResponseSSOConfig
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_identifier', 'saml_ssoid', 'file', 'file_metadata', 'display_name', 'group_membership_attr', 'authorization_enabled', 'logout_url', 'entity_identifier', 'saml_provider_type', 'client_id', 'client_secret', 'friendly_saml_name', 'jit_enabled', 'jit_validation_key', 'jit_validation_value']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_saml_meta_data_for_saml_ssoid" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `update_saml_meta_data_for_saml_ssoid`")  # noqa: E501
        # verify the required parameter 'saml_ssoid' is set
        if ('saml_ssoid' not in params or
                params['saml_ssoid'] is None):
            raise ValueError("Missing the required parameter `saml_ssoid` when calling `update_saml_meta_data_for_saml_ssoid`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'saml_ssoid' in params:
            path_params['samlSSOId'] = params['saml_ssoid']  # noqa: E501

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'file' in params:
            form_params.append(('file', params['file']))  # noqa: E501
        if 'file_metadata' in params:
            form_params.append(('fileMetadata', params['file_metadata']))  # noqa: E501
        if 'display_name' in params:
            form_params.append(('displayName', params['display_name']))  # noqa: E501
        if 'group_membership_attr' in params:
            form_params.append(('groupMembershipAttr', params['group_membership_attr']))  # noqa: E501
        if 'authorization_enabled' in params:
            form_params.append(('authorizationEnabled', params['authorization_enabled']))  # noqa: E501
        if 'logout_url' in params:
            form_params.append(('logoutUrl', params['logout_url']))  # noqa: E501
        if 'entity_identifier' in params:
            form_params.append(('entityIdentifier', params['entity_identifier']))  # noqa: E501
        if 'saml_provider_type' in params:
            form_params.append(('samlProviderType', params['saml_provider_type']))  # noqa: E501
        if 'client_id' in params:
            form_params.append(('clientId', params['client_id']))  # noqa: E501
        if 'client_secret' in params:
            form_params.append(('clientSecret', params['client_secret']))  # noqa: E501
        if 'friendly_saml_name' in params:
            form_params.append(('friendlySamlName', params['friendly_saml_name']))  # noqa: E501
        if 'jit_enabled' in params:
            form_params.append(('jitEnabled', params['jit_enabled']))  # noqa: E501
        if 'jit_validation_key' in params:
            form_params.append(('jitValidationKey', params['jit_validation_key']))  # noqa: E501
        if 'jit_validation_value' in params:
            form_params.append(('jitValidationValue', params['jit_validation_value']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/yaml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/ng/api/authentication-settings/saml-metadata-upload/{samlSSOId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RestResponseSSOConfig',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_whitelisted_domains(self, account_identifier, **kwargs):  # noqa: E501
        """Updates the whitelisted domains  # noqa: E501

        Updates whitelisted domains configured for an account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_whitelisted_domains(account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param list[str] body: Set of whitelisted domains and IPs for the account
        :return: RestResponseBoolean
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_whitelisted_domains_with_http_info(account_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.update_whitelisted_domains_with_http_info(account_identifier, **kwargs)  # noqa: E501
            return data

    def update_whitelisted_domains_with_http_info(self, account_identifier, **kwargs):  # noqa: E501
        """Updates the whitelisted domains  # noqa: E501

        Updates whitelisted domains configured for an account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_whitelisted_domains_with_http_info(account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param list[str] body: Set of whitelisted domains and IPs for the account
        :return: RestResponseBoolean
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_identifier', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_whitelisted_domains" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `update_whitelisted_domains`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/yaml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/ng/api/authentication-settings/whitelisted-domains', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RestResponseBoolean',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def upload_saml_meta_data(self, account_id, **kwargs):  # noqa: E501
        """Upload SAML metadata  # noqa: E501

        Updates the SAML metadata for the given Account ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upload_saml_meta_data(account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity. (required)
        :param object file:
        :param FormDataContentDisposition file_metadata:
        :param str display_name:
        :param str group_membership_attr:
        :param bool authorization_enabled:
        :param str logout_url:
        :param str entity_identifier:
        :param str saml_provider_type:
        :param str client_id:
        :param str client_secret:
        :param str friendly_saml_name:
        :param bool jit_enabled:
        :param str jit_validation_key:
        :param str jit_validation_value:
        :return: RestResponseSSOConfig
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.upload_saml_meta_data_with_http_info(account_id, **kwargs)  # noqa: E501
        else:
            (data) = self.upload_saml_meta_data_with_http_info(account_id, **kwargs)  # noqa: E501
            return data

    def upload_saml_meta_data_with_http_info(self, account_id, **kwargs):  # noqa: E501
        """Upload SAML metadata  # noqa: E501

        Updates the SAML metadata for the given Account ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upload_saml_meta_data_with_http_info(account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity. (required)
        :param object file:
        :param FormDataContentDisposition file_metadata:
        :param str display_name:
        :param str group_membership_attr:
        :param bool authorization_enabled:
        :param str logout_url:
        :param str entity_identifier:
        :param str saml_provider_type:
        :param str client_id:
        :param str client_secret:
        :param str friendly_saml_name:
        :param bool jit_enabled:
        :param str jit_validation_key:
        :param str jit_validation_value:
        :return: RestResponseSSOConfig
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'file', 'file_metadata', 'display_name', 'group_membership_attr', 'authorization_enabled', 'logout_url', 'entity_identifier', 'saml_provider_type', 'client_id', 'client_secret', 'friendly_saml_name', 'jit_enabled', 'jit_validation_key', 'jit_validation_value']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method upload_saml_meta_data" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `upload_saml_meta_data`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'account_id' in params:
            query_params.append(('accountId', params['account_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'file' in params:
            form_params.append(('file', params['file']))  # noqa: E501
        if 'file_metadata' in params:
            form_params.append(('fileMetadata', params['file_metadata']))  # noqa: E501
        if 'display_name' in params:
            form_params.append(('displayName', params['display_name']))  # noqa: E501
        if 'group_membership_attr' in params:
            form_params.append(('groupMembershipAttr', params['group_membership_attr']))  # noqa: E501
        if 'authorization_enabled' in params:
            form_params.append(('authorizationEnabled', params['authorization_enabled']))  # noqa: E501
        if 'logout_url' in params:
            form_params.append(('logoutUrl', params['logout_url']))  # noqa: E501
        if 'entity_identifier' in params:
            form_params.append(('entityIdentifier', params['entity_identifier']))  # noqa: E501
        if 'saml_provider_type' in params:
            form_params.append(('samlProviderType', params['saml_provider_type']))  # noqa: E501
        if 'client_id' in params:
            form_params.append(('clientId', params['client_id']))  # noqa: E501
        if 'client_secret' in params:
            form_params.append(('clientSecret', params['client_secret']))  # noqa: E501
        if 'friendly_saml_name' in params:
            form_params.append(('friendlySamlName', params['friendly_saml_name']))  # noqa: E501
        if 'jit_enabled' in params:
            form_params.append(('jitEnabled', params['jit_enabled']))  # noqa: E501
        if 'jit_validation_key' in params:
            form_params.append(('jitValidationKey', params['jit_validation_key']))  # noqa: E501
        if 'jit_validation_value' in params:
            form_params.append(('jitValidationValue', params['jit_validation_value']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/yaml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/ng/api/authentication-settings/saml-metadata-upload', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RestResponseSSOConfig',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
