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

from swagger_client.api_client import ApiClient


class DowntimeApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_downtime_data(self, identifier, account_identifier, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """delete_downtime_data  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_downtime_data(identifier, account_identifier, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: Identifier for the Entity. (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_downtime_data_with_http_info(identifier, account_identifier, org_identifier, project_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_downtime_data_with_http_info(identifier, account_identifier, org_identifier, project_identifier, **kwargs)  # noqa: E501
            return data

    def delete_downtime_data_with_http_info(self, identifier, account_identifier, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """delete_downtime_data  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_downtime_data_with_http_info(identifier, account_identifier, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: Identifier for the Entity. (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['identifier', 'account_identifier', 'org_identifier', 'project_identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_downtime_data" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `delete_downtime_data`")  # noqa: E501
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `delete_downtime_data`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `delete_downtime_data`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `delete_downtime_data`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501
        if 'account_identifier' in params:
            path_params['accountIdentifier'] = params['account_identifier']  # noqa: E501
        if 'org_identifier' in params:
            path_params['orgIdentifier'] = params['org_identifier']  # noqa: E501
        if 'project_identifier' in params:
            path_params['projectIdentifier'] = params['project_identifier']  # noqa: E501

        query_params = []

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
            '/cv/api/account/{accountIdentifier}/org/{orgIdentifier}/project/{projectIdentifier}/downtime/identifier/{identifier}', 'DELETE',
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

    def get_associated_monitored_services(self, identifier, account_identifier, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """get_associated_monitored_services  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_associated_monitored_services(identifier, account_identifier, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: Identifier for the Entity. (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_associated_monitored_services_with_http_info(identifier, account_identifier, org_identifier, project_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.get_associated_monitored_services_with_http_info(identifier, account_identifier, org_identifier, project_identifier, **kwargs)  # noqa: E501
            return data

    def get_associated_monitored_services_with_http_info(self, identifier, account_identifier, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """get_associated_monitored_services  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_associated_monitored_services_with_http_info(identifier, account_identifier, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: Identifier for the Entity. (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['identifier', 'account_identifier', 'org_identifier', 'project_identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_associated_monitored_services" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `get_associated_monitored_services`")  # noqa: E501
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `get_associated_monitored_services`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `get_associated_monitored_services`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `get_associated_monitored_services`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501
        if 'account_identifier' in params:
            path_params['accountIdentifier'] = params['account_identifier']  # noqa: E501
        if 'org_identifier' in params:
            path_params['orgIdentifier'] = params['org_identifier']  # noqa: E501
        if 'project_identifier' in params:
            path_params['projectIdentifier'] = params['project_identifier']  # noqa: E501

        query_params = []

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
            '/cv/api/account/{accountIdentifier}/org/{orgIdentifier}/project/{projectIdentifier}/downtime/monitored-services/{identifier}', 'GET',
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

    def get_downtime(self, identifier, account_identifier, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """get_downtime  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_downtime(identifier, account_identifier, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: Identifier for the Entity. (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_downtime_with_http_info(identifier, account_identifier, org_identifier, project_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.get_downtime_with_http_info(identifier, account_identifier, org_identifier, project_identifier, **kwargs)  # noqa: E501
            return data

    def get_downtime_with_http_info(self, identifier, account_identifier, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """get_downtime  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_downtime_with_http_info(identifier, account_identifier, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: Identifier for the Entity. (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['identifier', 'account_identifier', 'org_identifier', 'project_identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_downtime" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `get_downtime`")  # noqa: E501
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `get_downtime`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `get_downtime`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `get_downtime`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501
        if 'account_identifier' in params:
            path_params['accountIdentifier'] = params['account_identifier']  # noqa: E501
        if 'org_identifier' in params:
            path_params['orgIdentifier'] = params['org_identifier']  # noqa: E501
        if 'project_identifier' in params:
            path_params['projectIdentifier'] = params['project_identifier']  # noqa: E501

        query_params = []

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
            '/cv/api/account/{accountIdentifier}/org/{orgIdentifier}/project/{projectIdentifier}/downtime/identifier/{identifier}', 'GET',
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

    def get_downtime_associated_monitored_services(self, account_identifier, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """get_downtime_associated_monitored_services  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_downtime_associated_monitored_services(account_identifier, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param int page_number: Page Index of the results to fetch.Default Value: 0
        :param int page_size: Results per page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_downtime_associated_monitored_services_with_http_info(account_identifier, org_identifier, project_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.get_downtime_associated_monitored_services_with_http_info(account_identifier, org_identifier, project_identifier, **kwargs)  # noqa: E501
            return data

    def get_downtime_associated_monitored_services_with_http_info(self, account_identifier, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """get_downtime_associated_monitored_services  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_downtime_associated_monitored_services_with_http_info(account_identifier, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param int page_number: Page Index of the results to fetch.Default Value: 0
        :param int page_size: Results per page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_identifier', 'org_identifier', 'project_identifier', 'page_number', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_downtime_associated_monitored_services" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `get_downtime_associated_monitored_services`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `get_downtime_associated_monitored_services`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `get_downtime_associated_monitored_services`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_identifier' in params:
            path_params['accountIdentifier'] = params['account_identifier']  # noqa: E501
        if 'org_identifier' in params:
            path_params['orgIdentifier'] = params['org_identifier']  # noqa: E501
        if 'project_identifier' in params:
            path_params['projectIdentifier'] = params['project_identifier']  # noqa: E501

        query_params = []
        if 'page_number' in params:
            query_params.append(('pageNumber', params['page_number']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501

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
            '/cv/api/account/{accountIdentifier}/org/{orgIdentifier}/project/{projectIdentifier}/downtime/monitored-services', 'GET',
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

    def get_history(self, account_identifier, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """get_history  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_history(account_identifier, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param int page_number: Page Index of the results to fetch.Default Value: 0
        :param int page_size: Results per page
        :param str monitored_service_identifier: For filtering on the basis of monitored services' identifiers
        :param str filter: For filtering on the basis of name
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_history_with_http_info(account_identifier, org_identifier, project_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.get_history_with_http_info(account_identifier, org_identifier, project_identifier, **kwargs)  # noqa: E501
            return data

    def get_history_with_http_info(self, account_identifier, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """get_history  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_history_with_http_info(account_identifier, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param int page_number: Page Index of the results to fetch.Default Value: 0
        :param int page_size: Results per page
        :param str monitored_service_identifier: For filtering on the basis of monitored services' identifiers
        :param str filter: For filtering on the basis of name
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_identifier', 'org_identifier', 'project_identifier', 'page_number', 'page_size', 'monitored_service_identifier', 'filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_history" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `get_history`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `get_history`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `get_history`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_identifier' in params:
            path_params['accountIdentifier'] = params['account_identifier']  # noqa: E501
        if 'org_identifier' in params:
            path_params['orgIdentifier'] = params['org_identifier']  # noqa: E501
        if 'project_identifier' in params:
            path_params['projectIdentifier'] = params['project_identifier']  # noqa: E501

        query_params = []
        if 'page_number' in params:
            query_params.append(('pageNumber', params['page_number']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501
        if 'monitored_service_identifier' in params:
            query_params.append(('monitoredServiceIdentifier', params['monitored_service_identifier']))  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501

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
            '/cv/api/account/{accountIdentifier}/org/{orgIdentifier}/project/{projectIdentifier}/downtime/history', 'GET',
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

    def list_downtimes(self, account_identifier, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """list_downtimes  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_downtimes(account_identifier, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param int page_number: Page Index of the results to fetch.Default Value: 0
        :param int page_size: Results per page
        :param str monitored_service_identifier: For filtering on the basis of monitored services' identifiers
        :param str filter: For filtering on the basis of name
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_downtimes_with_http_info(account_identifier, org_identifier, project_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.list_downtimes_with_http_info(account_identifier, org_identifier, project_identifier, **kwargs)  # noqa: E501
            return data

    def list_downtimes_with_http_info(self, account_identifier, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """list_downtimes  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_downtimes_with_http_info(account_identifier, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param int page_number: Page Index of the results to fetch.Default Value: 0
        :param int page_size: Results per page
        :param str monitored_service_identifier: For filtering on the basis of monitored services' identifiers
        :param str filter: For filtering on the basis of name
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_identifier', 'org_identifier', 'project_identifier', 'page_number', 'page_size', 'monitored_service_identifier', 'filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_downtimes" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `list_downtimes`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `list_downtimes`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `list_downtimes`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_identifier' in params:
            path_params['accountIdentifier'] = params['account_identifier']  # noqa: E501
        if 'org_identifier' in params:
            path_params['orgIdentifier'] = params['org_identifier']  # noqa: E501
        if 'project_identifier' in params:
            path_params['projectIdentifier'] = params['project_identifier']  # noqa: E501

        query_params = []
        if 'page_number' in params:
            query_params.append(('pageNumber', params['page_number']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501
        if 'monitored_service_identifier' in params:
            query_params.append(('monitoredServiceIdentifier', params['monitored_service_identifier']))  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501

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
            '/cv/api/account/{accountIdentifier}/org/{orgIdentifier}/project/{projectIdentifier}/downtime/list', 'GET',
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

    def save_downtime(self, body, account_identifier, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """save_downtime  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.save_downtime(body, account_identifier, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Downtime body: Details of the Downtime to be saved (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.save_downtime_with_http_info(body, account_identifier, org_identifier, project_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.save_downtime_with_http_info(body, account_identifier, org_identifier, project_identifier, **kwargs)  # noqa: E501
            return data

    def save_downtime_with_http_info(self, body, account_identifier, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """save_downtime  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.save_downtime_with_http_info(body, account_identifier, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Downtime body: Details of the Downtime to be saved (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'account_identifier', 'org_identifier', 'project_identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method save_downtime" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `save_downtime`")  # noqa: E501
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `save_downtime`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `save_downtime`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `save_downtime`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_identifier' in params:
            path_params['accountIdentifier'] = params['account_identifier']  # noqa: E501
        if 'org_identifier' in params:
            path_params['orgIdentifier'] = params['org_identifier']  # noqa: E501
        if 'project_identifier' in params:
            path_params['projectIdentifier'] = params['project_identifier']  # noqa: E501

        query_params = []

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
            '/cv/api/account/{accountIdentifier}/org/{orgIdentifier}/project/{projectIdentifier}/downtime', 'POST',
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

    def update_downtime_data(self, body, identifier, account_identifier, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """update_downtime_data  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_downtime_data(body, identifier, account_identifier, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Downtime body: Details of the Downtime to be updated (required)
        :param str identifier: Identifier for the Entity. (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_downtime_data_with_http_info(body, identifier, account_identifier, org_identifier, project_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.update_downtime_data_with_http_info(body, identifier, account_identifier, org_identifier, project_identifier, **kwargs)  # noqa: E501
            return data

    def update_downtime_data_with_http_info(self, body, identifier, account_identifier, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """update_downtime_data  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_downtime_data_with_http_info(body, identifier, account_identifier, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Downtime body: Details of the Downtime to be updated (required)
        :param str identifier: Identifier for the Entity. (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'identifier', 'account_identifier', 'org_identifier', 'project_identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_downtime_data" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_downtime_data`")  # noqa: E501
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `update_downtime_data`")  # noqa: E501
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `update_downtime_data`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `update_downtime_data`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `update_downtime_data`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501
        if 'account_identifier' in params:
            path_params['accountIdentifier'] = params['account_identifier']  # noqa: E501
        if 'org_identifier' in params:
            path_params['orgIdentifier'] = params['org_identifier']  # noqa: E501
        if 'project_identifier' in params:
            path_params['projectIdentifier'] = params['project_identifier']  # noqa: E501

        query_params = []

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
            '/cv/api/account/{accountIdentifier}/org/{orgIdentifier}/project/{projectIdentifier}/downtime/identifier/{identifier}', 'PUT',
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

    def update_downtime_enabled(self, identifier, account_identifier, org_identifier, project_identifier, enable, **kwargs):  # noqa: E501
        """update_downtime_enabled  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_downtime_enabled(identifier, account_identifier, org_identifier, project_identifier, enable, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: Identifier for the Entity. (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param bool enable: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_downtime_enabled_with_http_info(identifier, account_identifier, org_identifier, project_identifier, enable, **kwargs)  # noqa: E501
        else:
            (data) = self.update_downtime_enabled_with_http_info(identifier, account_identifier, org_identifier, project_identifier, enable, **kwargs)  # noqa: E501
            return data

    def update_downtime_enabled_with_http_info(self, identifier, account_identifier, org_identifier, project_identifier, enable, **kwargs):  # noqa: E501
        """update_downtime_enabled  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_downtime_enabled_with_http_info(identifier, account_identifier, org_identifier, project_identifier, enable, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: Identifier for the Entity. (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param bool enable: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['identifier', 'account_identifier', 'org_identifier', 'project_identifier', 'enable']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_downtime_enabled" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `update_downtime_enabled`")  # noqa: E501
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `update_downtime_enabled`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `update_downtime_enabled`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `update_downtime_enabled`")  # noqa: E501
        # verify the required parameter 'enable' is set
        if ('enable' not in params or
                params['enable'] is None):
            raise ValueError("Missing the required parameter `enable` when calling `update_downtime_enabled`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501
        if 'account_identifier' in params:
            path_params['accountIdentifier'] = params['account_identifier']  # noqa: E501
        if 'org_identifier' in params:
            path_params['orgIdentifier'] = params['org_identifier']  # noqa: E501
        if 'project_identifier' in params:
            path_params['projectIdentifier'] = params['project_identifier']  # noqa: E501

        query_params = []
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
            '/cv/api/account/{accountIdentifier}/org/{orgIdentifier}/project/{projectIdentifier}/downtime/flag/{identifier}', 'PUT',
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
