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


class CloudCostAutoStoppingRulesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def all_auto_stopping_resources(self, account_id, cloud_account_id, region, rule_id, account_identifier, **kwargs):  # noqa: E501
        """List all the resources for an AutoStopping Rule  # noqa: E501

        Lists all the resources for an AutoStopping Rule for the given identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.all_auto_stopping_resources(account_id, cloud_account_id, region, rule_id, account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity (required)
        :param str cloud_account_id: Connector ID (required)
        :param str region: Cloud region where resources belong to (required)
        :param float rule_id: ID of the AutoStopping Rule for which you need to list the resources (required)
        :param str account_identifier: Account Identifier for the Entity (required)
        :return: AllResourcesOfAccountResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.all_auto_stopping_resources_with_http_info(account_id, cloud_account_id, region, rule_id, account_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.all_auto_stopping_resources_with_http_info(account_id, cloud_account_id, region, rule_id, account_identifier, **kwargs)  # noqa: E501
            return data

    def all_auto_stopping_resources_with_http_info(self, account_id, cloud_account_id, region, rule_id, account_identifier, **kwargs):  # noqa: E501
        """List all the resources for an AutoStopping Rule  # noqa: E501

        Lists all the resources for an AutoStopping Rule for the given identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.all_auto_stopping_resources_with_http_info(account_id, cloud_account_id, region, rule_id, account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity (required)
        :param str cloud_account_id: Connector ID (required)
        :param str region: Cloud region where resources belong to (required)
        :param float rule_id: ID of the AutoStopping Rule for which you need to list the resources (required)
        :param str account_identifier: Account Identifier for the Entity (required)
        :return: AllResourcesOfAccountResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'cloud_account_id', 'region', 'rule_id', 'account_identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method all_auto_stopping_resources" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `all_auto_stopping_resources`")  # noqa: E501
        # verify the required parameter 'cloud_account_id' is set
        if ('cloud_account_id' not in params or
                params['cloud_account_id'] is None):
            raise ValueError("Missing the required parameter `cloud_account_id` when calling `all_auto_stopping_resources`")  # noqa: E501
        # verify the required parameter 'region' is set
        if ('region' not in params or
                params['region'] is None):
            raise ValueError("Missing the required parameter `region` when calling `all_auto_stopping_resources`")  # noqa: E501
        # verify the required parameter 'rule_id' is set
        if ('rule_id' not in params or
                params['rule_id'] is None):
            raise ValueError("Missing the required parameter `rule_id` when calling `all_auto_stopping_resources`")  # noqa: E501
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `all_auto_stopping_resources`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_id' in params:
            path_params['account_id'] = params['account_id']  # noqa: E501
        if 'rule_id' in params:
            path_params['rule_id'] = params['rule_id']  # noqa: E501

        query_params = []
        if 'cloud_account_id' in params:
            query_params.append(('cloud_account_id', params['cloud_account_id']))  # noqa: E501
        if 'region' in params:
            query_params.append(('region', params['region']))  # noqa: E501
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/gateway/lw/api/accounts/{account_id}/autostopping/rules/{rule_id}/resources', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AllResourcesOfAccountResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def auto_stopping_rule_details(self, account_id, rule_id, account_identifier, **kwargs):  # noqa: E501
        """Return AutoStopping Rule details  # noqa: E501

        Returns details of an AutoStopping Rule for the given identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.auto_stopping_rule_details(account_id, rule_id, account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity (required)
        :param float rule_id: ID of the AutoStopping Rule for which you need to fetch the details (required)
        :param str account_identifier: Account Identifier for the Entity (required)
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.auto_stopping_rule_details_with_http_info(account_id, rule_id, account_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.auto_stopping_rule_details_with_http_info(account_id, rule_id, account_identifier, **kwargs)  # noqa: E501
            return data

    def auto_stopping_rule_details_with_http_info(self, account_id, rule_id, account_identifier, **kwargs):  # noqa: E501
        """Return AutoStopping Rule details  # noqa: E501

        Returns details of an AutoStopping Rule for the given identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.auto_stopping_rule_details_with_http_info(account_id, rule_id, account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity (required)
        :param float rule_id: ID of the AutoStopping Rule for which you need to fetch the details (required)
        :param str account_identifier: Account Identifier for the Entity (required)
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'rule_id', 'account_identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method auto_stopping_rule_details" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `auto_stopping_rule_details`")  # noqa: E501
        # verify the required parameter 'rule_id' is set
        if ('rule_id' not in params or
                params['rule_id'] is None):
            raise ValueError("Missing the required parameter `rule_id` when calling `auto_stopping_rule_details`")  # noqa: E501
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `auto_stopping_rule_details`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_id' in params:
            path_params['account_id'] = params['account_id']  # noqa: E501
        if 'rule_id' in params:
            path_params['rule_id'] = params['rule_id']  # noqa: E501

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/gateway/lw/api/accounts/{account_id}/autostopping/rules/{rule_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2001',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def cool_down_autostopping_rule(self, body, account_identifier, account_id, rule_id, **kwargs):  # noqa: E501
        """Cool down an AutoStopping Rule  # noqa: E501

        Cool down resources under an Autostopping rule  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cool_down_autostopping_rule(body, account_identifier, account_id, rule_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CoolDownOption body: Cool Down Options (required)
        :param str account_identifier: Account Identifier for the Entity (required)
        :param str account_id: Account Identifier for the Entity (required)
        :param float rule_id: ID of the AutoStopping rule for which you need to fetch the diagnostics details (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.cool_down_autostopping_rule_with_http_info(body, account_identifier, account_id, rule_id, **kwargs)  # noqa: E501
        else:
            (data) = self.cool_down_autostopping_rule_with_http_info(body, account_identifier, account_id, rule_id, **kwargs)  # noqa: E501
            return data

    def cool_down_autostopping_rule_with_http_info(self, body, account_identifier, account_id, rule_id, **kwargs):  # noqa: E501
        """Cool down an AutoStopping Rule  # noqa: E501

        Cool down resources under an Autostopping rule  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cool_down_autostopping_rule_with_http_info(body, account_identifier, account_id, rule_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CoolDownOption body: Cool Down Options (required)
        :param str account_identifier: Account Identifier for the Entity (required)
        :param str account_id: Account Identifier for the Entity (required)
        :param float rule_id: ID of the AutoStopping rule for which you need to fetch the diagnostics details (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'account_identifier', 'account_id', 'rule_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cool_down_autostopping_rule" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `cool_down_autostopping_rule`")  # noqa: E501
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `cool_down_autostopping_rule`")  # noqa: E501
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `cool_down_autostopping_rule`")  # noqa: E501
        # verify the required parameter 'rule_id' is set
        if ('rule_id' not in params or
                params['rule_id'] is None):
            raise ValueError("Missing the required parameter `rule_id` when calling `cool_down_autostopping_rule`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_id' in params:
            path_params['account_id'] = params['account_id']  # noqa: E501
        if 'rule_id' in params:
            path_params['rule_id'] = params['rule_id']  # noqa: E501

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
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/gateway/lw/api/accounts/{account_id}/autostopping/rules/{rule_id}/cooldown', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def cumulative_auto_stopping_savings(self, account_id, account_identifier, **kwargs):  # noqa: E501
        """Return cumulative savings for all the AutoStopping Rules  # noqa: E501

        Returns cumulative savings for all the AutoStopping Rules.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cumulative_auto_stopping_savings(account_id, account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity (required)
        :param str account_identifier: Account Identifier for the Entity (required)
        :return: CumulativeSavingsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.cumulative_auto_stopping_savings_with_http_info(account_id, account_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.cumulative_auto_stopping_savings_with_http_info(account_id, account_identifier, **kwargs)  # noqa: E501
            return data

    def cumulative_auto_stopping_savings_with_http_info(self, account_id, account_identifier, **kwargs):  # noqa: E501
        """Return cumulative savings for all the AutoStopping Rules  # noqa: E501

        Returns cumulative savings for all the AutoStopping Rules.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cumulative_auto_stopping_savings_with_http_info(account_id, account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity (required)
        :param str account_identifier: Account Identifier for the Entity (required)
        :return: CumulativeSavingsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'account_identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cumulative_auto_stopping_savings" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `cumulative_auto_stopping_savings`")  # noqa: E501
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `cumulative_auto_stopping_savings`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_id' in params:
            path_params['account_id'] = params['account_id']  # noqa: E501

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/gateway/lw/api/accounts/{account_id}/autostopping/rules/savings/cumulative', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CumulativeSavingsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_auto_stopping_rule(self, rule_id, account_id, account_identifier, **kwargs):  # noqa: E501
        """Delete an AutoStopping Rule  # noqa: E501

        Deletes an AutoStopping Rule for the given identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_auto_stopping_rule(rule_id, account_id, account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float rule_id: ID of the AutoStopping Rule that you want to delete (required)
        :param str account_id: Account Identifier for the Entity (required)
        :param str account_identifier: Account Identifier for the Entity (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_auto_stopping_rule_with_http_info(rule_id, account_id, account_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_auto_stopping_rule_with_http_info(rule_id, account_id, account_identifier, **kwargs)  # noqa: E501
            return data

    def delete_auto_stopping_rule_with_http_info(self, rule_id, account_id, account_identifier, **kwargs):  # noqa: E501
        """Delete an AutoStopping Rule  # noqa: E501

        Deletes an AutoStopping Rule for the given identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_auto_stopping_rule_with_http_info(rule_id, account_id, account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float rule_id: ID of the AutoStopping Rule that you want to delete (required)
        :param str account_id: Account Identifier for the Entity (required)
        :param str account_identifier: Account Identifier for the Entity (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['rule_id', 'account_id', 'account_identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_auto_stopping_rule" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'rule_id' is set
        if ('rule_id' not in params or
                params['rule_id'] is None):
            raise ValueError("Missing the required parameter `rule_id` when calling `delete_auto_stopping_rule`")  # noqa: E501
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `delete_auto_stopping_rule`")  # noqa: E501
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `delete_auto_stopping_rule`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'rule_id' in params:
            path_params['rule_id'] = params['rule_id']  # noqa: E501
        if 'account_id' in params:
            path_params['account_id'] = params['account_id']  # noqa: E501

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/gateway/lw/api/accounts/{account_id}/autostopping/rules/{rule_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_auto_stopping_cool_down_meta(self, account_id, rule_id, account_identifier, **kwargs):  # noqa: E501
        """Return metadata of cool down of an AutoStopping Rule  # noqa: E501

        Return metadata of cool down of an AutoStopping Rule  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_auto_stopping_cool_down_meta(account_id, rule_id, account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity (required)
        :param float rule_id: ID of the AutoStopping rule for which you need to fetch the diagnostics details (required)
        :param str account_identifier: Account Identifier for the Entity (required)
        :return: CoolDownMetaSuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_auto_stopping_cool_down_meta_with_http_info(account_id, rule_id, account_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.get_auto_stopping_cool_down_meta_with_http_info(account_id, rule_id, account_identifier, **kwargs)  # noqa: E501
            return data

    def get_auto_stopping_cool_down_meta_with_http_info(self, account_id, rule_id, account_identifier, **kwargs):  # noqa: E501
        """Return metadata of cool down of an AutoStopping Rule  # noqa: E501

        Return metadata of cool down of an AutoStopping Rule  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_auto_stopping_cool_down_meta_with_http_info(account_id, rule_id, account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity (required)
        :param float rule_id: ID of the AutoStopping rule for which you need to fetch the diagnostics details (required)
        :param str account_identifier: Account Identifier for the Entity (required)
        :return: CoolDownMetaSuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'rule_id', 'account_identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_auto_stopping_cool_down_meta" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `get_auto_stopping_cool_down_meta`")  # noqa: E501
        # verify the required parameter 'rule_id' is set
        if ('rule_id' not in params or
                params['rule_id'] is None):
            raise ValueError("Missing the required parameter `rule_id` when calling `get_auto_stopping_cool_down_meta`")  # noqa: E501
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `get_auto_stopping_cool_down_meta`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_id' in params:
            path_params['account_id'] = params['account_id']  # noqa: E501
        if 'rule_id' in params:
            path_params['rule_id'] = params['rule_id']  # noqa: E501

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/gateway/lw/api/accounts/{account_id}/autostopping/rules/{rule_id}/cooldown_meta', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CoolDownMetaSuccessResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_auto_stopping_diagnostics(self, account_id, rule_id, account_identifier, **kwargs):  # noqa: E501
        """Return diagnostics result of an AutoStopping Rule  # noqa: E501

        Returns the diagnostics result of an AutoStopping rule for the given identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_auto_stopping_diagnostics(account_id, rule_id, account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity (required)
        :param float rule_id: ID of the AutoStopping rule for which you need to fetch the diagnostics details (required)
        :param str account_identifier: Account Identifier for the Entity (required)
        :return: ServiceDiagnosticsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_auto_stopping_diagnostics_with_http_info(account_id, rule_id, account_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.get_auto_stopping_diagnostics_with_http_info(account_id, rule_id, account_identifier, **kwargs)  # noqa: E501
            return data

    def get_auto_stopping_diagnostics_with_http_info(self, account_id, rule_id, account_identifier, **kwargs):  # noqa: E501
        """Return diagnostics result of an AutoStopping Rule  # noqa: E501

        Returns the diagnostics result of an AutoStopping rule for the given identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_auto_stopping_diagnostics_with_http_info(account_id, rule_id, account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity (required)
        :param float rule_id: ID of the AutoStopping rule for which you need to fetch the diagnostics details (required)
        :param str account_identifier: Account Identifier for the Entity (required)
        :return: ServiceDiagnosticsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'rule_id', 'account_identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_auto_stopping_diagnostics" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `get_auto_stopping_diagnostics`")  # noqa: E501
        # verify the required parameter 'rule_id' is set
        if ('rule_id' not in params or
                params['rule_id'] is None):
            raise ValueError("Missing the required parameter `rule_id` when calling `get_auto_stopping_diagnostics`")  # noqa: E501
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `get_auto_stopping_diagnostics`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_id' in params:
            path_params['account_id'] = params['account_id']  # noqa: E501
        if 'rule_id' in params:
            path_params['rule_id'] = params['rule_id']  # noqa: E501

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/gateway/lw/api/accounts/{account_id}/autostopping/rules/{rule_id}/diagnostics', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ServiceDiagnosticsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def health_of_auto_stopping_rule(self, account_id, rule_id, account_identifier, **kwargs):  # noqa: E501
        """Return health status of an AutoStopping Rule  # noqa: E501

        Returns health status of an AutoStopping Rule for the given identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.health_of_auto_stopping_rule(account_id, rule_id, account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity (required)
        :param float rule_id: ID of the AutoStopping Rule for which you need to fetch the health status (required)
        :param str account_identifier: Account Identifier for the Entity (required)
        :return: ServiceHealthResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.health_of_auto_stopping_rule_with_http_info(account_id, rule_id, account_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.health_of_auto_stopping_rule_with_http_info(account_id, rule_id, account_identifier, **kwargs)  # noqa: E501
            return data

    def health_of_auto_stopping_rule_with_http_info(self, account_id, rule_id, account_identifier, **kwargs):  # noqa: E501
        """Return health status of an AutoStopping Rule  # noqa: E501

        Returns health status of an AutoStopping Rule for the given identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.health_of_auto_stopping_rule_with_http_info(account_id, rule_id, account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity (required)
        :param float rule_id: ID of the AutoStopping Rule for which you need to fetch the health status (required)
        :param str account_identifier: Account Identifier for the Entity (required)
        :return: ServiceHealthResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'rule_id', 'account_identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method health_of_auto_stopping_rule" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `health_of_auto_stopping_rule`")  # noqa: E501
        # verify the required parameter 'rule_id' is set
        if ('rule_id' not in params or
                params['rule_id'] is None):
            raise ValueError("Missing the required parameter `rule_id` when calling `health_of_auto_stopping_rule`")  # noqa: E501
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `health_of_auto_stopping_rule`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_id' in params:
            path_params['account_id'] = params['account_id']  # noqa: E501
        if 'rule_id' in params:
            path_params['rule_id'] = params['rule_id']  # noqa: E501

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/gateway/lw/api/accounts/{account_id}/autostopping/rules/{rule_id}/health', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ServiceHealthResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_auto_stopping_rules(self, account_id, account_identifier, **kwargs):  # noqa: E501
        """List AutoStopping Rules  # noqa: E501

        Lists all the AutoStopping rules separated by comma-separated strings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_auto_stopping_rules(account_id, account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity (required)
        :param str account_identifier: Account Identifier for the Entity (required)
        :param bool dry_run: Flag which if enabled lists out only dry run rules.
        :return: ServicesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_auto_stopping_rules_with_http_info(account_id, account_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.list_auto_stopping_rules_with_http_info(account_id, account_identifier, **kwargs)  # noqa: E501
            return data

    def list_auto_stopping_rules_with_http_info(self, account_id, account_identifier, **kwargs):  # noqa: E501
        """List AutoStopping Rules  # noqa: E501

        Lists all the AutoStopping rules separated by comma-separated strings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_auto_stopping_rules_with_http_info(account_id, account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity (required)
        :param str account_identifier: Account Identifier for the Entity (required)
        :param bool dry_run: Flag which if enabled lists out only dry run rules.
        :return: ServicesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'account_identifier', 'dry_run']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_auto_stopping_rules" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `list_auto_stopping_rules`")  # noqa: E501
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `list_auto_stopping_rules`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_id' in params:
            path_params['account_id'] = params['account_id']  # noqa: E501

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501
        if 'dry_run' in params:
            query_params.append(('dry_run', params['dry_run']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/gateway/lw/api/accounts/{account_id}/autostopping/rules', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ServicesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def savings_from_auto_stopping_rule(self, account_id, rule_id, account_identifier, **kwargs):  # noqa: E501
        """Return savings details for an AutoStopping Rule  # noqa: E501

        Returns savings details for an AutoStopping rule for the given identifier and the specified time duration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.savings_from_auto_stopping_rule(account_id, rule_id, account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity (required)
        :param float rule_id: ID of the AutoStopping Rule for which you want to fetch savings detail (required)
        :param str account_identifier: Account Identifier for the Entity (required)
        :param str _from: Start time for the computation of savings
        :param str to: End time for the computation of savings
        :param str group_by:
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.savings_from_auto_stopping_rule_with_http_info(account_id, rule_id, account_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.savings_from_auto_stopping_rule_with_http_info(account_id, rule_id, account_identifier, **kwargs)  # noqa: E501
            return data

    def savings_from_auto_stopping_rule_with_http_info(self, account_id, rule_id, account_identifier, **kwargs):  # noqa: E501
        """Return savings details for an AutoStopping Rule  # noqa: E501

        Returns savings details for an AutoStopping rule for the given identifier and the specified time duration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.savings_from_auto_stopping_rule_with_http_info(account_id, rule_id, account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity (required)
        :param float rule_id: ID of the AutoStopping Rule for which you want to fetch savings detail (required)
        :param str account_identifier: Account Identifier for the Entity (required)
        :param str _from: Start time for the computation of savings
        :param str to: End time for the computation of savings
        :param str group_by:
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'rule_id', 'account_identifier', '_from', 'to', 'group_by']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method savings_from_auto_stopping_rule" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `savings_from_auto_stopping_rule`")  # noqa: E501
        # verify the required parameter 'rule_id' is set
        if ('rule_id' not in params or
                params['rule_id'] is None):
            raise ValueError("Missing the required parameter `rule_id` when calling `savings_from_auto_stopping_rule`")  # noqa: E501
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `savings_from_auto_stopping_rule`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_id' in params:
            path_params['account_id'] = params['account_id']  # noqa: E501
        if 'rule_id' in params:
            path_params['rule_id'] = params['rule_id']  # noqa: E501

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501
        if '_from' in params:
            query_params.append(('from', params['_from']))  # noqa: E501
        if 'to' in params:
            query_params.append(('to', params['to']))  # noqa: E501
        if 'group_by' in params:
            query_params.append(('group_by', params['group_by']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/gateway/lw/api/accounts/{account_id}/autostopping/rules/{rule_id}/savings', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def toggle_autostopping_rule(self, account_id, rule_id, disable, account_identifier, **kwargs):  # noqa: E501
        """Disable/Enable an Autostopping Rule  # noqa: E501

        Disables or enables an Autostopping Rule for the given identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.toggle_autostopping_rule(account_id, rule_id, disable, account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity (required)
        :param str rule_id: ID of the AutoStopping rule to be enabled/disabled (required)
        :param bool disable: (required)
        :param str account_identifier: Account Identifier for the Entity (required)
        :return: ServicesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.toggle_autostopping_rule_with_http_info(account_id, rule_id, disable, account_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.toggle_autostopping_rule_with_http_info(account_id, rule_id, disable, account_identifier, **kwargs)  # noqa: E501
            return data

    def toggle_autostopping_rule_with_http_info(self, account_id, rule_id, disable, account_identifier, **kwargs):  # noqa: E501
        """Disable/Enable an Autostopping Rule  # noqa: E501

        Disables or enables an Autostopping Rule for the given identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.toggle_autostopping_rule_with_http_info(account_id, rule_id, disable, account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity (required)
        :param str rule_id: ID of the AutoStopping rule to be enabled/disabled (required)
        :param bool disable: (required)
        :param str account_identifier: Account Identifier for the Entity (required)
        :return: ServicesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'rule_id', 'disable', 'account_identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method toggle_autostopping_rule" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `toggle_autostopping_rule`")  # noqa: E501
        # verify the required parameter 'rule_id' is set
        if ('rule_id' not in params or
                params['rule_id'] is None):
            raise ValueError("Missing the required parameter `rule_id` when calling `toggle_autostopping_rule`")  # noqa: E501
        # verify the required parameter 'disable' is set
        if ('disable' not in params or
                params['disable'] is None):
            raise ValueError("Missing the required parameter `disable` when calling `toggle_autostopping_rule`")  # noqa: E501
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `toggle_autostopping_rule`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_id' in params:
            path_params['account_id'] = params['account_id']  # noqa: E501
        if 'rule_id' in params:
            path_params['rule_id'] = params['rule_id']  # noqa: E501

        query_params = []
        if 'disable' in params:
            query_params.append(('disable', params['disable']))  # noqa: E501
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/gateway/lw/api/accounts/{account_id}/autostopping/rules/{rule_id}/toggle_state', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ServicesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_auto_stopping_rule(self, body, account_identifier, account_id, **kwargs):  # noqa: E501
        """Create an AutoStopping Rule  # noqa: E501

        Creates a new AutoStopping Rule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_auto_stopping_rule(body, account_identifier, account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SaveServiceRequest body: Service definition of an AutoStopping rule (required)
        :param str account_identifier: Account Identifier for the Entity (required)
        :param str account_id: Account Identifier for the Entity (required)
        :return: LwServiceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_auto_stopping_rule_with_http_info(body, account_identifier, account_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_auto_stopping_rule_with_http_info(body, account_identifier, account_id, **kwargs)  # noqa: E501
            return data

    def update_auto_stopping_rule_with_http_info(self, body, account_identifier, account_id, **kwargs):  # noqa: E501
        """Create an AutoStopping Rule  # noqa: E501

        Creates a new AutoStopping Rule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_auto_stopping_rule_with_http_info(body, account_identifier, account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SaveServiceRequest body: Service definition of an AutoStopping rule (required)
        :param str account_identifier: Account Identifier for the Entity (required)
        :param str account_id: Account Identifier for the Entity (required)
        :return: LwServiceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'account_identifier', 'account_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_auto_stopping_rule" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_auto_stopping_rule`")  # noqa: E501
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `update_auto_stopping_rule`")  # noqa: E501
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `update_auto_stopping_rule`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_id' in params:
            path_params['account_id'] = params['account_id']  # noqa: E501

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
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/gateway/lw/api/accounts/{account_id}/autostopping/rules', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LwServiceResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
