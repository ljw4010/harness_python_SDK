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


class MonitoredServicesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_default_monitored_service(self, account_id, org_identifier, project_identifier, environment_identifier, service_identifier, **kwargs):  # noqa: E501
        """create_default_monitored_service  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_default_monitored_service(account_id, org_identifier, project_identifier, environment_identifier, service_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str environment_identifier: (required)
        :param str service_identifier: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_default_monitored_service_with_http_info(account_id, org_identifier, project_identifier, environment_identifier, service_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.create_default_monitored_service_with_http_info(account_id, org_identifier, project_identifier, environment_identifier, service_identifier, **kwargs)  # noqa: E501
            return data

    def create_default_monitored_service_with_http_info(self, account_id, org_identifier, project_identifier, environment_identifier, service_identifier, **kwargs):  # noqa: E501
        """create_default_monitored_service  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_default_monitored_service_with_http_info(account_id, org_identifier, project_identifier, environment_identifier, service_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str environment_identifier: (required)
        :param str service_identifier: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'org_identifier', 'project_identifier', 'environment_identifier', 'service_identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_default_monitored_service" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `create_default_monitored_service`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `create_default_monitored_service`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `create_default_monitored_service`")  # noqa: E501
        # verify the required parameter 'environment_identifier' is set
        if ('environment_identifier' not in params or
                params['environment_identifier'] is None):
            raise ValueError("Missing the required parameter `environment_identifier` when calling `create_default_monitored_service`")  # noqa: E501
        # verify the required parameter 'service_identifier' is set
        if ('service_identifier' not in params or
                params['service_identifier'] is None):
            raise ValueError("Missing the required parameter `service_identifier` when calling `create_default_monitored_service`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'account_id' in params:
            query_params.append(('accountId', params['account_id']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501
        if 'environment_identifier' in params:
            query_params.append(('environmentIdentifier', params['environment_identifier']))  # noqa: E501
        if 'service_identifier' in params:
            query_params.append(('serviceIdentifier', params['service_identifier']))  # noqa: E501

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
            '/cv/api/monitored-service/create-default', 'POST',
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

    def cvget_anomalies_summary(self, account_id, org_identifier, project_identifier, identifier, start_time, end_time, **kwargs):  # noqa: E501
        """cvget_anomalies_summary  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cvget_anomalies_summary(account_id, org_identifier, project_identifier, identifier, start_time, end_time, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str identifier: (required)
        :param int start_time: (required)
        :param int end_time: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.cvget_anomalies_summary_with_http_info(account_id, org_identifier, project_identifier, identifier, start_time, end_time, **kwargs)  # noqa: E501
        else:
            (data) = self.cvget_anomalies_summary_with_http_info(account_id, org_identifier, project_identifier, identifier, start_time, end_time, **kwargs)  # noqa: E501
            return data

    def cvget_anomalies_summary_with_http_info(self, account_id, org_identifier, project_identifier, identifier, start_time, end_time, **kwargs):  # noqa: E501
        """cvget_anomalies_summary  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cvget_anomalies_summary_with_http_info(account_id, org_identifier, project_identifier, identifier, start_time, end_time, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str identifier: (required)
        :param int start_time: (required)
        :param int end_time: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'org_identifier', 'project_identifier', 'identifier', 'start_time', 'end_time']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cvget_anomalies_summary" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `cvget_anomalies_summary`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `cvget_anomalies_summary`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `cvget_anomalies_summary`")  # noqa: E501
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `cvget_anomalies_summary`")  # noqa: E501
        # verify the required parameter 'start_time' is set
        if ('start_time' not in params or
                params['start_time'] is None):
            raise ValueError("Missing the required parameter `start_time` when calling `cvget_anomalies_summary`")  # noqa: E501
        # verify the required parameter 'end_time' is set
        if ('end_time' not in params or
                params['end_time'] is None):
            raise ValueError("Missing the required parameter `end_time` when calling `cvget_anomalies_summary`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501

        query_params = []
        if 'account_id' in params:
            query_params.append(('accountId', params['account_id']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501
        if 'start_time' in params:
            query_params.append(('startTime', params['start_time']))  # noqa: E501
        if 'end_time' in params:
            query_params.append(('endTime', params['end_time']))  # noqa: E501

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
            '/cv/api/monitored-service/{identifier}/anomaliesCount', 'GET',
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

    def delete_monitored_service(self, account_id, org_identifier, project_identifier, identifier, **kwargs):  # noqa: E501
        """Delete monitored service data  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_monitored_service(account_id, org_identifier, project_identifier, identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str identifier: Identifier for the Entity. (required)
        :return: CvRestResponseBoolean
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_monitored_service_with_http_info(account_id, org_identifier, project_identifier, identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_monitored_service_with_http_info(account_id, org_identifier, project_identifier, identifier, **kwargs)  # noqa: E501
            return data

    def delete_monitored_service_with_http_info(self, account_id, org_identifier, project_identifier, identifier, **kwargs):  # noqa: E501
        """Delete monitored service data  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_monitored_service_with_http_info(account_id, org_identifier, project_identifier, identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str identifier: Identifier for the Entity. (required)
        :return: CvRestResponseBoolean
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'org_identifier', 'project_identifier', 'identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_monitored_service" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `delete_monitored_service`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `delete_monitored_service`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `delete_monitored_service`")  # noqa: E501
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `delete_monitored_service`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501

        query_params = []
        if 'account_id' in params:
            query_params.append(('accountId', params['account_id']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501

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
            '/cv/api/monitored-service/{identifier}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CvRestResponseBoolean',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_all_monitored_services_with_health_sources(self, account_id, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """get_all_monitored_services_with_health_sources  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_monitored_services_with_health_sources(account_id, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_monitored_services_with_health_sources_with_http_info(account_id, org_identifier, project_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.get_all_monitored_services_with_health_sources_with_http_info(account_id, org_identifier, project_identifier, **kwargs)  # noqa: E501
            return data

    def get_all_monitored_services_with_health_sources_with_http_info(self, account_id, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """get_all_monitored_services_with_health_sources  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_monitored_services_with_health_sources_with_http_info(account_id, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'org_identifier', 'project_identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_monitored_services_with_health_sources" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `get_all_monitored_services_with_health_sources`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `get_all_monitored_services_with_health_sources`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `get_all_monitored_services_with_health_sources`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'account_id' in params:
            query_params.append(('accountId', params['account_id']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501

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
            '/cv/api/monitored-service/all/time-series-health-sources', 'GET',
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

    def get_count_of_services(self, account_id, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """get_count_of_services  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_count_of_services(account_id, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str environment_identifier:
        :param str filter:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_count_of_services_with_http_info(account_id, org_identifier, project_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.get_count_of_services_with_http_info(account_id, org_identifier, project_identifier, **kwargs)  # noqa: E501
            return data

    def get_count_of_services_with_http_info(self, account_id, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """get_count_of_services  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_count_of_services_with_http_info(account_id, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str environment_identifier:
        :param str filter:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'org_identifier', 'project_identifier', 'environment_identifier', 'filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_count_of_services" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `get_count_of_services`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `get_count_of_services`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `get_count_of_services`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'account_id' in params:
            query_params.append(('accountId', params['account_id']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501
        if 'environment_identifier' in params:
            query_params.append(('environmentIdentifier', params['environment_identifier']))  # noqa: E501
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
            '/cv/api/monitored-service/count-of-services', 'GET',
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

    def get_environments(self, account_id, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """get_environments  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_environments(account_id, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: (required)
        :param str org_identifier: (required)
        :param str project_identifier: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_environments_with_http_info(account_id, org_identifier, project_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.get_environments_with_http_info(account_id, org_identifier, project_identifier, **kwargs)  # noqa: E501
            return data

    def get_environments_with_http_info(self, account_id, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """get_environments  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_environments_with_http_info(account_id, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: (required)
        :param str org_identifier: (required)
        :param str project_identifier: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'org_identifier', 'project_identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_environments" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `get_environments`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `get_environments`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `get_environments`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'account_id' in params:
            query_params.append(('accountId', params['account_id']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501

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
            '/cv/api/monitored-service/environments', 'GET',
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

    def get_health_sources(self, account_id, org_identifier, project_identifier, service_identifier, environment_identifier, **kwargs):  # noqa: E501
        """get_health_sources  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_health_sources(account_id, org_identifier, project_identifier, service_identifier, environment_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str service_identifier: (required)
        :param str environment_identifier: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_health_sources_with_http_info(account_id, org_identifier, project_identifier, service_identifier, environment_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.get_health_sources_with_http_info(account_id, org_identifier, project_identifier, service_identifier, environment_identifier, **kwargs)  # noqa: E501
            return data

    def get_health_sources_with_http_info(self, account_id, org_identifier, project_identifier, service_identifier, environment_identifier, **kwargs):  # noqa: E501
        """get_health_sources  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_health_sources_with_http_info(account_id, org_identifier, project_identifier, service_identifier, environment_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str service_identifier: (required)
        :param str environment_identifier: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'org_identifier', 'project_identifier', 'service_identifier', 'environment_identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_health_sources" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `get_health_sources`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `get_health_sources`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `get_health_sources`")  # noqa: E501
        # verify the required parameter 'service_identifier' is set
        if ('service_identifier' not in params or
                params['service_identifier'] is None):
            raise ValueError("Missing the required parameter `service_identifier` when calling `get_health_sources`")  # noqa: E501
        # verify the required parameter 'environment_identifier' is set
        if ('environment_identifier' not in params or
                params['environment_identifier'] is None):
            raise ValueError("Missing the required parameter `environment_identifier` when calling `get_health_sources`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'account_id' in params:
            query_params.append(('accountId', params['account_id']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501
        if 'service_identifier' in params:
            query_params.append(('serviceIdentifier', params['service_identifier']))  # noqa: E501
        if 'environment_identifier' in params:
            query_params.append(('environmentIdentifier', params['environment_identifier']))  # noqa: E501

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
            '/cv/api/monitored-service/health-sources', 'GET',
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

    def get_health_sources_for_monitored_service_identifier(self, account_id, org_identifier, project_identifier, monitored_service_identifier, **kwargs):  # noqa: E501
        """get_health_sources_for_monitored_service_identifier  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_health_sources_for_monitored_service_identifier(account_id, org_identifier, project_identifier, monitored_service_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str monitored_service_identifier: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_health_sources_for_monitored_service_identifier_with_http_info(account_id, org_identifier, project_identifier, monitored_service_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.get_health_sources_for_monitored_service_identifier_with_http_info(account_id, org_identifier, project_identifier, monitored_service_identifier, **kwargs)  # noqa: E501
            return data

    def get_health_sources_for_monitored_service_identifier_with_http_info(self, account_id, org_identifier, project_identifier, monitored_service_identifier, **kwargs):  # noqa: E501
        """get_health_sources_for_monitored_service_identifier  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_health_sources_for_monitored_service_identifier_with_http_info(account_id, org_identifier, project_identifier, monitored_service_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str monitored_service_identifier: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'org_identifier', 'project_identifier', 'monitored_service_identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_health_sources_for_monitored_service_identifier" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `get_health_sources_for_monitored_service_identifier`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `get_health_sources_for_monitored_service_identifier`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `get_health_sources_for_monitored_service_identifier`")  # noqa: E501
        # verify the required parameter 'monitored_service_identifier' is set
        if ('monitored_service_identifier' not in params or
                params['monitored_service_identifier'] is None):
            raise ValueError("Missing the required parameter `monitored_service_identifier` when calling `get_health_sources_for_monitored_service_identifier`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'monitored_service_identifier' in params:
            path_params['monitoredServiceIdentifier'] = params['monitored_service_identifier']  # noqa: E501

        query_params = []
        if 'account_id' in params:
            query_params.append(('accountId', params['account_id']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501

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
            '/cv/api/monitored-service/{monitoredServiceIdentifier}/health-sources', 'GET',
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

    def get_list(self, account_id, org_identifier, project_identifier, offset, page_size, **kwargs):  # noqa: E501
        """get_list  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_list(account_id, org_identifier, project_identifier, offset, page_size, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param int offset: (required)
        :param int page_size: (required)
        :param str environment_identifier:
        :param list[str] environment_identifiers:
        :param str filter:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_list_with_http_info(account_id, org_identifier, project_identifier, offset, page_size, **kwargs)  # noqa: E501
        else:
            (data) = self.get_list_with_http_info(account_id, org_identifier, project_identifier, offset, page_size, **kwargs)  # noqa: E501
            return data

    def get_list_with_http_info(self, account_id, org_identifier, project_identifier, offset, page_size, **kwargs):  # noqa: E501
        """get_list  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_list_with_http_info(account_id, org_identifier, project_identifier, offset, page_size, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param int offset: (required)
        :param int page_size: (required)
        :param str environment_identifier:
        :param list[str] environment_identifiers:
        :param str filter:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'org_identifier', 'project_identifier', 'offset', 'page_size', 'environment_identifier', 'environment_identifiers', 'filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `get_list`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `get_list`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `get_list`")  # noqa: E501
        # verify the required parameter 'offset' is set
        if ('offset' not in params or
                params['offset'] is None):
            raise ValueError("Missing the required parameter `offset` when calling `get_list`")  # noqa: E501
        # verify the required parameter 'page_size' is set
        if ('page_size' not in params or
                params['page_size'] is None):
            raise ValueError("Missing the required parameter `page_size` when calling `get_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'account_id' in params:
            query_params.append(('accountId', params['account_id']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501
        if 'environment_identifier' in params:
            query_params.append(('environmentIdentifier', params['environment_identifier']))  # noqa: E501
        if 'environment_identifiers' in params:
            query_params.append(('environmentIdentifiers', params['environment_identifiers']))  # noqa: E501
            collection_formats['environmentIdentifiers'] = 'multi'  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501
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
            '/cv/api/monitored-service/list', 'GET',
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

    def get_list_v2(self, account_id, org_identifier, project_identifier, offset, page_size, **kwargs):  # noqa: E501
        """get_list_v2  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_list_v2(account_id, org_identifier, project_identifier, offset, page_size, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param int offset: (required)
        :param int page_size: (required)
        :param list[str] environment_identifiers:
        :param str filter:
        :param str monitored_service_type:
        :param bool hide_not_configured_services:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_list_v2_with_http_info(account_id, org_identifier, project_identifier, offset, page_size, **kwargs)  # noqa: E501
        else:
            (data) = self.get_list_v2_with_http_info(account_id, org_identifier, project_identifier, offset, page_size, **kwargs)  # noqa: E501
            return data

    def get_list_v2_with_http_info(self, account_id, org_identifier, project_identifier, offset, page_size, **kwargs):  # noqa: E501
        """get_list_v2  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_list_v2_with_http_info(account_id, org_identifier, project_identifier, offset, page_size, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param int offset: (required)
        :param int page_size: (required)
        :param list[str] environment_identifiers:
        :param str filter:
        :param str monitored_service_type:
        :param bool hide_not_configured_services:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'org_identifier', 'project_identifier', 'offset', 'page_size', 'environment_identifiers', 'filter', 'monitored_service_type', 'hide_not_configured_services']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_list_v2" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `get_list_v2`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `get_list_v2`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `get_list_v2`")  # noqa: E501
        # verify the required parameter 'offset' is set
        if ('offset' not in params or
                params['offset'] is None):
            raise ValueError("Missing the required parameter `offset` when calling `get_list_v2`")  # noqa: E501
        # verify the required parameter 'page_size' is set
        if ('page_size' not in params or
                params['page_size'] is None):
            raise ValueError("Missing the required parameter `page_size` when calling `get_list_v2`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'account_id' in params:
            query_params.append(('accountId', params['account_id']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501
        if 'environment_identifiers' in params:
            query_params.append(('environmentIdentifiers', params['environment_identifiers']))  # noqa: E501
            collection_formats['environmentIdentifiers'] = 'multi'  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
        if 'monitored_service_type' in params:
            query_params.append(('monitoredServiceType', params['monitored_service_type']))  # noqa: E501
        if 'hide_not_configured_services' in params:
            query_params.append(('hideNotConfiguredServices', params['hide_not_configured_services']))  # noqa: E501

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
            '/cv/api/monitored-service/platform/list', 'GET',
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

    def get_monitored_service(self, identifier, account_id, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """Get monitored service data  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_monitored_service(identifier, account_id, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: (required)
        :param str account_id: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :return: ResponseDTOMonitoredServiceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_monitored_service_with_http_info(identifier, account_id, org_identifier, project_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.get_monitored_service_with_http_info(identifier, account_id, org_identifier, project_identifier, **kwargs)  # noqa: E501
            return data

    def get_monitored_service_with_http_info(self, identifier, account_id, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """Get monitored service data  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_monitored_service_with_http_info(identifier, account_id, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: (required)
        :param str account_id: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :return: ResponseDTOMonitoredServiceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['identifier', 'account_id', 'org_identifier', 'project_identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_monitored_service" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `get_monitored_service`")  # noqa: E501
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `get_monitored_service`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `get_monitored_service`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `get_monitored_service`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501

        query_params = []
        if 'account_id' in params:
            query_params.append(('accountId', params['account_id']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501

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
            '/cv/api/monitored-service/{identifier}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseDTOMonitoredServiceResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_monitored_service_change_details(self, account_id, org_identifier, project_identifier, monitored_service_identifier, **kwargs):  # noqa: E501
        """get_monitored_service_change_details  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_monitored_service_change_details(account_id, org_identifier, project_identifier, monitored_service_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str monitored_service_identifier: (required)
        :param list[str] slo_identifiers:
        :param int start_time:
        :param int end_time:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_monitored_service_change_details_with_http_info(account_id, org_identifier, project_identifier, monitored_service_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.get_monitored_service_change_details_with_http_info(account_id, org_identifier, project_identifier, monitored_service_identifier, **kwargs)  # noqa: E501
            return data

    def get_monitored_service_change_details_with_http_info(self, account_id, org_identifier, project_identifier, monitored_service_identifier, **kwargs):  # noqa: E501
        """get_monitored_service_change_details  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_monitored_service_change_details_with_http_info(account_id, org_identifier, project_identifier, monitored_service_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str monitored_service_identifier: (required)
        :param list[str] slo_identifiers:
        :param int start_time:
        :param int end_time:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'org_identifier', 'project_identifier', 'monitored_service_identifier', 'slo_identifiers', 'start_time', 'end_time']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_monitored_service_change_details" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `get_monitored_service_change_details`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `get_monitored_service_change_details`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `get_monitored_service_change_details`")  # noqa: E501
        # verify the required parameter 'monitored_service_identifier' is set
        if ('monitored_service_identifier' not in params or
                params['monitored_service_identifier'] is None):
            raise ValueError("Missing the required parameter `monitored_service_identifier` when calling `get_monitored_service_change_details`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'monitored_service_identifier' in params:
            path_params['monitoredServiceIdentifier'] = params['monitored_service_identifier']  # noqa: E501

        query_params = []
        if 'account_id' in params:
            query_params.append(('accountId', params['account_id']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501
        if 'slo_identifiers' in params:
            query_params.append(('sloIdentifiers', params['slo_identifiers']))  # noqa: E501
            collection_formats['sloIdentifiers'] = 'multi'  # noqa: E501
        if 'start_time' in params:
            query_params.append(('startTime', params['start_time']))  # noqa: E501
        if 'end_time' in params:
            query_params.append(('endTime', params['end_time']))  # noqa: E501

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
            '/cv/api/monitored-service/{monitoredServiceIdentifier}/change-details', 'GET',
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

    def get_monitored_service_details(self, account_id, org_identifier, project_identifier, monitored_service_identifier, **kwargs):  # noqa: E501
        """get_monitored_service_details  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_monitored_service_details(account_id, org_identifier, project_identifier, monitored_service_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str monitored_service_identifier: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_monitored_service_details_with_http_info(account_id, org_identifier, project_identifier, monitored_service_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.get_monitored_service_details_with_http_info(account_id, org_identifier, project_identifier, monitored_service_identifier, **kwargs)  # noqa: E501
            return data

    def get_monitored_service_details_with_http_info(self, account_id, org_identifier, project_identifier, monitored_service_identifier, **kwargs):  # noqa: E501
        """get_monitored_service_details  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_monitored_service_details_with_http_info(account_id, org_identifier, project_identifier, monitored_service_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str monitored_service_identifier: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'org_identifier', 'project_identifier', 'monitored_service_identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_monitored_service_details" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `get_monitored_service_details`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `get_monitored_service_details`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `get_monitored_service_details`")  # noqa: E501
        # verify the required parameter 'monitored_service_identifier' is set
        if ('monitored_service_identifier' not in params or
                params['monitored_service_identifier'] is None):
            raise ValueError("Missing the required parameter `monitored_service_identifier` when calling `get_monitored_service_details`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'monitored_service_identifier' in params:
            path_params['monitoredServiceIdentifier'] = params['monitored_service_identifier']  # noqa: E501

        query_params = []
        if 'account_id' in params:
            query_params.append(('accountId', params['account_id']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501

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
            '/cv/api/monitored-service/{monitoredServiceIdentifier}/service-details', 'GET',
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

    def get_monitored_service_details1(self, account_id, service_identifier, environment_identifier, **kwargs):  # noqa: E501
        """get_monitored_service_details1  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_monitored_service_details1(account_id, service_identifier, environment_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity. (required)
        :param str service_identifier: (required)
        :param str environment_identifier: (required)
        :param str org_identifier: Organization Identifier for the Entity.
        :param str project_identifier: Project Identifier for the Entity.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_monitored_service_details1_with_http_info(account_id, service_identifier, environment_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.get_monitored_service_details1_with_http_info(account_id, service_identifier, environment_identifier, **kwargs)  # noqa: E501
            return data

    def get_monitored_service_details1_with_http_info(self, account_id, service_identifier, environment_identifier, **kwargs):  # noqa: E501
        """get_monitored_service_details1  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_monitored_service_details1_with_http_info(account_id, service_identifier, environment_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity. (required)
        :param str service_identifier: (required)
        :param str environment_identifier: (required)
        :param str org_identifier: Organization Identifier for the Entity.
        :param str project_identifier: Project Identifier for the Entity.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'service_identifier', 'environment_identifier', 'org_identifier', 'project_identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_monitored_service_details1" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `get_monitored_service_details1`")  # noqa: E501
        # verify the required parameter 'service_identifier' is set
        if ('service_identifier' not in params or
                params['service_identifier'] is None):
            raise ValueError("Missing the required parameter `service_identifier` when calling `get_monitored_service_details1`")  # noqa: E501
        # verify the required parameter 'environment_identifier' is set
        if ('environment_identifier' not in params or
                params['environment_identifier'] is None):
            raise ValueError("Missing the required parameter `environment_identifier` when calling `get_monitored_service_details1`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'account_id' in params:
            query_params.append(('accountId', params['account_id']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501
        if 'service_identifier' in params:
            query_params.append(('serviceIdentifier', params['service_identifier']))  # noqa: E501
        if 'environment_identifier' in params:
            query_params.append(('environmentIdentifier', params['environment_identifier']))  # noqa: E501

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
            '/cv/api/monitored-service/service-details', 'GET',
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

    def get_monitored_service_from_service_and_environment(self, account_id, org_identifier, project_identifier, service_identifier, environment_identifier, **kwargs):  # noqa: E501
        """get_monitored_service_from_service_and_environment  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_monitored_service_from_service_and_environment(account_id, org_identifier, project_identifier, service_identifier, environment_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str service_identifier: (required)
        :param str environment_identifier: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_monitored_service_from_service_and_environment_with_http_info(account_id, org_identifier, project_identifier, service_identifier, environment_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.get_monitored_service_from_service_and_environment_with_http_info(account_id, org_identifier, project_identifier, service_identifier, environment_identifier, **kwargs)  # noqa: E501
            return data

    def get_monitored_service_from_service_and_environment_with_http_info(self, account_id, org_identifier, project_identifier, service_identifier, environment_identifier, **kwargs):  # noqa: E501
        """get_monitored_service_from_service_and_environment  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_monitored_service_from_service_and_environment_with_http_info(account_id, org_identifier, project_identifier, service_identifier, environment_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str service_identifier: (required)
        :param str environment_identifier: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'org_identifier', 'project_identifier', 'service_identifier', 'environment_identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_monitored_service_from_service_and_environment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `get_monitored_service_from_service_and_environment`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `get_monitored_service_from_service_and_environment`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `get_monitored_service_from_service_and_environment`")  # noqa: E501
        # verify the required parameter 'service_identifier' is set
        if ('service_identifier' not in params or
                params['service_identifier'] is None):
            raise ValueError("Missing the required parameter `service_identifier` when calling `get_monitored_service_from_service_and_environment`")  # noqa: E501
        # verify the required parameter 'environment_identifier' is set
        if ('environment_identifier' not in params or
                params['environment_identifier'] is None):
            raise ValueError("Missing the required parameter `environment_identifier` when calling `get_monitored_service_from_service_and_environment`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'account_id' in params:
            query_params.append(('accountId', params['account_id']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501
        if 'service_identifier' in params:
            query_params.append(('serviceIdentifier', params['service_identifier']))  # noqa: E501
        if 'environment_identifier' in params:
            query_params.append(('environmentIdentifier', params['environment_identifier']))  # noqa: E501

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
            '/cv/api/monitored-service/service-environment', 'GET',
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

    def get_monitored_service_logs(self, account_id, org_identifier, project_identifier, monitored_service_identifier, log_type, start_time, end_time, **kwargs):  # noqa: E501
        """get_monitored_service_logs  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_monitored_service_logs(account_id, org_identifier, project_identifier, monitored_service_identifier, log_type, start_time, end_time, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str monitored_service_identifier: (required)
        :param str log_type: (required)
        :param int start_time: (required)
        :param int end_time: (required)
        :param bool error_logs_only:
        :param list[str] health_sources:
        :param int page_number: Page Index of the results to fetch.Default Value: 0
        :param int page_size: Results per page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_monitored_service_logs_with_http_info(account_id, org_identifier, project_identifier, monitored_service_identifier, log_type, start_time, end_time, **kwargs)  # noqa: E501
        else:
            (data) = self.get_monitored_service_logs_with_http_info(account_id, org_identifier, project_identifier, monitored_service_identifier, log_type, start_time, end_time, **kwargs)  # noqa: E501
            return data

    def get_monitored_service_logs_with_http_info(self, account_id, org_identifier, project_identifier, monitored_service_identifier, log_type, start_time, end_time, **kwargs):  # noqa: E501
        """get_monitored_service_logs  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_monitored_service_logs_with_http_info(account_id, org_identifier, project_identifier, monitored_service_identifier, log_type, start_time, end_time, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str monitored_service_identifier: (required)
        :param str log_type: (required)
        :param int start_time: (required)
        :param int end_time: (required)
        :param bool error_logs_only:
        :param list[str] health_sources:
        :param int page_number: Page Index of the results to fetch.Default Value: 0
        :param int page_size: Results per page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'org_identifier', 'project_identifier', 'monitored_service_identifier', 'log_type', 'start_time', 'end_time', 'error_logs_only', 'health_sources', 'page_number', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_monitored_service_logs" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `get_monitored_service_logs`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `get_monitored_service_logs`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `get_monitored_service_logs`")  # noqa: E501
        # verify the required parameter 'monitored_service_identifier' is set
        if ('monitored_service_identifier' not in params or
                params['monitored_service_identifier'] is None):
            raise ValueError("Missing the required parameter `monitored_service_identifier` when calling `get_monitored_service_logs`")  # noqa: E501
        # verify the required parameter 'log_type' is set
        if ('log_type' not in params or
                params['log_type'] is None):
            raise ValueError("Missing the required parameter `log_type` when calling `get_monitored_service_logs`")  # noqa: E501
        # verify the required parameter 'start_time' is set
        if ('start_time' not in params or
                params['start_time'] is None):
            raise ValueError("Missing the required parameter `start_time` when calling `get_monitored_service_logs`")  # noqa: E501
        # verify the required parameter 'end_time' is set
        if ('end_time' not in params or
                params['end_time'] is None):
            raise ValueError("Missing the required parameter `end_time` when calling `get_monitored_service_logs`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'monitored_service_identifier' in params:
            path_params['monitoredServiceIdentifier'] = params['monitored_service_identifier']  # noqa: E501

        query_params = []
        if 'account_id' in params:
            query_params.append(('accountId', params['account_id']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501
        if 'log_type' in params:
            query_params.append(('logType', params['log_type']))  # noqa: E501
        if 'error_logs_only' in params:
            query_params.append(('errorLogsOnly', params['error_logs_only']))  # noqa: E501
        if 'start_time' in params:
            query_params.append(('startTime', params['start_time']))  # noqa: E501
        if 'end_time' in params:
            query_params.append(('endTime', params['end_time']))  # noqa: E501
        if 'health_sources' in params:
            query_params.append(('healthSources', params['health_sources']))  # noqa: E501
            collection_formats['healthSources'] = 'multi'  # noqa: E501
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
            '/cv/api/monitored-service/{monitoredServiceIdentifier}/logs', 'GET',
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

    def get_monitored_service_score(self, account_id, org_identifier, project_identifier, identifier, **kwargs):  # noqa: E501
        """get_monitored_service_score  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_monitored_service_score(account_id, org_identifier, project_identifier, identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str identifier: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_monitored_service_score_with_http_info(account_id, org_identifier, project_identifier, identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.get_monitored_service_score_with_http_info(account_id, org_identifier, project_identifier, identifier, **kwargs)  # noqa: E501
            return data

    def get_monitored_service_score_with_http_info(self, account_id, org_identifier, project_identifier, identifier, **kwargs):  # noqa: E501
        """get_monitored_service_score  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_monitored_service_score_with_http_info(account_id, org_identifier, project_identifier, identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str identifier: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'org_identifier', 'project_identifier', 'identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_monitored_service_score" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `get_monitored_service_score`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `get_monitored_service_score`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `get_monitored_service_score`")  # noqa: E501
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `get_monitored_service_score`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501

        query_params = []
        if 'account_id' in params:
            query_params.append(('accountId', params['account_id']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501

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
            '/cv/api/monitored-service/{identifier}/scores', 'GET',
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

    def get_ms_secondary_events(self, account_id, identifier, start_time, end_time, **kwargs):  # noqa: E501
        """get_ms_secondary_events  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_ms_secondary_events(account_id, identifier, start_time, end_time, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity. (required)
        :param str identifier: (required)
        :param int start_time: (required)
        :param int end_time: (required)
        :param str org_identifier: Organization Identifier for the Entity.
        :param str project_identifier: Project Identifier for the Entity.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_ms_secondary_events_with_http_info(account_id, identifier, start_time, end_time, **kwargs)  # noqa: E501
        else:
            (data) = self.get_ms_secondary_events_with_http_info(account_id, identifier, start_time, end_time, **kwargs)  # noqa: E501
            return data

    def get_ms_secondary_events_with_http_info(self, account_id, identifier, start_time, end_time, **kwargs):  # noqa: E501
        """get_ms_secondary_events  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_ms_secondary_events_with_http_info(account_id, identifier, start_time, end_time, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity. (required)
        :param str identifier: (required)
        :param int start_time: (required)
        :param int end_time: (required)
        :param str org_identifier: Organization Identifier for the Entity.
        :param str project_identifier: Project Identifier for the Entity.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'identifier', 'start_time', 'end_time', 'org_identifier', 'project_identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_ms_secondary_events" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `get_ms_secondary_events`")  # noqa: E501
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `get_ms_secondary_events`")  # noqa: E501
        # verify the required parameter 'start_time' is set
        if ('start_time' not in params or
                params['start_time'] is None):
            raise ValueError("Missing the required parameter `start_time` when calling `get_ms_secondary_events`")  # noqa: E501
        # verify the required parameter 'end_time' is set
        if ('end_time' not in params or
                params['end_time'] is None):
            raise ValueError("Missing the required parameter `end_time` when calling `get_ms_secondary_events`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501

        query_params = []
        if 'account_id' in params:
            query_params.append(('accountId', params['account_id']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501
        if 'start_time' in params:
            query_params.append(('startTime', params['start_time']))  # noqa: E501
        if 'end_time' in params:
            query_params.append(('endTime', params['end_time']))  # noqa: E501

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
            '/cv/api/monitored-service/{identifier}/secondary-events', 'GET',
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

    def get_ms_secondary_events_details(self, account_id, secondary_event_type, identifiers, **kwargs):  # noqa: E501
        """get_ms_secondary_events_details  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_ms_secondary_events_details(account_id, secondary_event_type, identifiers, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity. (required)
        :param str secondary_event_type: (required)
        :param list[str] identifiers: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_ms_secondary_events_details_with_http_info(account_id, secondary_event_type, identifiers, **kwargs)  # noqa: E501
        else:
            (data) = self.get_ms_secondary_events_details_with_http_info(account_id, secondary_event_type, identifiers, **kwargs)  # noqa: E501
            return data

    def get_ms_secondary_events_details_with_http_info(self, account_id, secondary_event_type, identifiers, **kwargs):  # noqa: E501
        """get_ms_secondary_events_details  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_ms_secondary_events_details_with_http_info(account_id, secondary_event_type, identifiers, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity. (required)
        :param str secondary_event_type: (required)
        :param list[str] identifiers: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'secondary_event_type', 'identifiers']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_ms_secondary_events_details" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `get_ms_secondary_events_details`")  # noqa: E501
        # verify the required parameter 'secondary_event_type' is set
        if ('secondary_event_type' not in params or
                params['secondary_event_type'] is None):
            raise ValueError("Missing the required parameter `secondary_event_type` when calling `get_ms_secondary_events_details`")  # noqa: E501
        # verify the required parameter 'identifiers' is set
        if ('identifiers' not in params or
                params['identifiers'] is None):
            raise ValueError("Missing the required parameter `identifiers` when calling `get_ms_secondary_events_details`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'account_id' in params:
            query_params.append(('accountId', params['account_id']))  # noqa: E501
        if 'secondary_event_type' in params:
            query_params.append(('secondaryEventType', params['secondary_event_type']))  # noqa: E501
        if 'identifiers' in params:
            query_params.append(('identifiers', params['identifiers']))  # noqa: E501
            collection_formats['identifiers'] = 'multi'  # noqa: E501

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
            '/cv/api/monitored-service/secondary-events-details', 'GET',
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

    def get_notification_rules_for_monitored_service(self, account_id, org_identifier, project_identifier, identifier, **kwargs):  # noqa: E501
        """Get notification rules for MonitoredService  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_notification_rules_for_monitored_service(account_id, org_identifier, project_identifier, identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str identifier: Identifier for the Entity. (required)
        :param int page_number: Page Index of the results to fetch.Default Value: 0
        :param int page_size: Results per page
        :return: ResponseDTOPageResponseNotificationRuleResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_notification_rules_for_monitored_service_with_http_info(account_id, org_identifier, project_identifier, identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.get_notification_rules_for_monitored_service_with_http_info(account_id, org_identifier, project_identifier, identifier, **kwargs)  # noqa: E501
            return data

    def get_notification_rules_for_monitored_service_with_http_info(self, account_id, org_identifier, project_identifier, identifier, **kwargs):  # noqa: E501
        """Get notification rules for MonitoredService  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_notification_rules_for_monitored_service_with_http_info(account_id, org_identifier, project_identifier, identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str identifier: Identifier for the Entity. (required)
        :param int page_number: Page Index of the results to fetch.Default Value: 0
        :param int page_size: Results per page
        :return: ResponseDTOPageResponseNotificationRuleResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'org_identifier', 'project_identifier', 'identifier', 'page_number', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_notification_rules_for_monitored_service" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `get_notification_rules_for_monitored_service`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `get_notification_rules_for_monitored_service`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `get_notification_rules_for_monitored_service`")  # noqa: E501
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `get_notification_rules_for_monitored_service`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501

        query_params = []
        if 'account_id' in params:
            query_params.append(('accountId', params['account_id']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501
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
            '/cv/api/monitored-service/{identifier}/notification-rules', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseDTOPageResponseNotificationRuleResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_over_all_health_score(self, account_id, org_identifier, project_identifier, identifier, end_time, **kwargs):  # noqa: E501
        """get_over_all_health_score  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_over_all_health_score(account_id, org_identifier, project_identifier, identifier, end_time, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str identifier: (required)
        :param int end_time: (required)
        :param str duration:
        :param int start_time:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_over_all_health_score_with_http_info(account_id, org_identifier, project_identifier, identifier, end_time, **kwargs)  # noqa: E501
        else:
            (data) = self.get_over_all_health_score_with_http_info(account_id, org_identifier, project_identifier, identifier, end_time, **kwargs)  # noqa: E501
            return data

    def get_over_all_health_score_with_http_info(self, account_id, org_identifier, project_identifier, identifier, end_time, **kwargs):  # noqa: E501
        """get_over_all_health_score  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_over_all_health_score_with_http_info(account_id, org_identifier, project_identifier, identifier, end_time, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str identifier: (required)
        :param int end_time: (required)
        :param str duration:
        :param int start_time:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'org_identifier', 'project_identifier', 'identifier', 'end_time', 'duration', 'start_time']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_over_all_health_score" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `get_over_all_health_score`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `get_over_all_health_score`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `get_over_all_health_score`")  # noqa: E501
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `get_over_all_health_score`")  # noqa: E501
        # verify the required parameter 'end_time' is set
        if ('end_time' not in params or
                params['end_time'] is None):
            raise ValueError("Missing the required parameter `end_time` when calling `get_over_all_health_score`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501

        query_params = []
        if 'account_id' in params:
            query_params.append(('accountId', params['account_id']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501
        if 'duration' in params:
            query_params.append(('duration', params['duration']))  # noqa: E501
        if 'end_time' in params:
            query_params.append(('endTime', params['end_time']))  # noqa: E501
        if 'start_time' in params:
            query_params.append(('startTime', params['start_time']))  # noqa: E501

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
            '/cv/api/monitored-service/{identifier}/overall-health-score', 'GET',
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

    def get_services(self, account_id, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """get_services  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_services(account_id, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: (required)
        :param str org_identifier: (required)
        :param str project_identifier: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_services_with_http_info(account_id, org_identifier, project_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.get_services_with_http_info(account_id, org_identifier, project_identifier, **kwargs)  # noqa: E501
            return data

    def get_services_with_http_info(self, account_id, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """get_services  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_services_with_http_info(account_id, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: (required)
        :param str org_identifier: (required)
        :param str project_identifier: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'org_identifier', 'project_identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_services" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `get_services`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `get_services`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `get_services`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'account_id' in params:
            query_params.append(('accountId', params['account_id']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501

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
            '/cv/api/monitored-service/services', 'GET',
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

    def get_slo_metrics(self, account_id, org_identifier, project_identifier, monitored_service_identifier, health_source_identifier, **kwargs):  # noqa: E501
        """get_slo_metrics  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_slo_metrics(account_id, org_identifier, project_identifier, monitored_service_identifier, health_source_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str monitored_service_identifier: (required)
        :param str health_source_identifier: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_slo_metrics_with_http_info(account_id, org_identifier, project_identifier, monitored_service_identifier, health_source_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.get_slo_metrics_with_http_info(account_id, org_identifier, project_identifier, monitored_service_identifier, health_source_identifier, **kwargs)  # noqa: E501
            return data

    def get_slo_metrics_with_http_info(self, account_id, org_identifier, project_identifier, monitored_service_identifier, health_source_identifier, **kwargs):  # noqa: E501
        """get_slo_metrics  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_slo_metrics_with_http_info(account_id, org_identifier, project_identifier, monitored_service_identifier, health_source_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str monitored_service_identifier: (required)
        :param str health_source_identifier: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'org_identifier', 'project_identifier', 'monitored_service_identifier', 'health_source_identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_slo_metrics" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `get_slo_metrics`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `get_slo_metrics`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `get_slo_metrics`")  # noqa: E501
        # verify the required parameter 'monitored_service_identifier' is set
        if ('monitored_service_identifier' not in params or
                params['monitored_service_identifier'] is None):
            raise ValueError("Missing the required parameter `monitored_service_identifier` when calling `get_slo_metrics`")  # noqa: E501
        # verify the required parameter 'health_source_identifier' is set
        if ('health_source_identifier' not in params or
                params['health_source_identifier'] is None):
            raise ValueError("Missing the required parameter `health_source_identifier` when calling `get_slo_metrics`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'monitored_service_identifier' in params:
            path_params['monitoredServiceIdentifier'] = params['monitored_service_identifier']  # noqa: E501
        if 'health_source_identifier' in params:
            path_params['healthSourceIdentifier'] = params['health_source_identifier']  # noqa: E501

        query_params = []
        if 'account_id' in params:
            query_params.append(('accountId', params['account_id']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501

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
            '/cv/api/monitored-service/{monitoredServiceIdentifier}/health-source/{healthSourceIdentifier}/slo-metrics', 'GET',
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

    def list(self, account_id, org_identifier, project_identifier, offset, page_size, services_at_risk_filter, **kwargs):  # noqa: E501
        """list  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list(account_id, org_identifier, project_identifier, offset, page_size, services_at_risk_filter, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param int offset: (required)
        :param int page_size: (required)
        :param bool services_at_risk_filter: (required)
        :param str environment_identifier:
        :param list[str] environment_identifiers:
        :param str service_identifier:
        :param str filter:
        :param str monitored_service_type:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_with_http_info(account_id, org_identifier, project_identifier, offset, page_size, services_at_risk_filter, **kwargs)  # noqa: E501
        else:
            (data) = self.list_with_http_info(account_id, org_identifier, project_identifier, offset, page_size, services_at_risk_filter, **kwargs)  # noqa: E501
            return data

    def list_with_http_info(self, account_id, org_identifier, project_identifier, offset, page_size, services_at_risk_filter, **kwargs):  # noqa: E501
        """list  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_with_http_info(account_id, org_identifier, project_identifier, offset, page_size, services_at_risk_filter, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param int offset: (required)
        :param int page_size: (required)
        :param bool services_at_risk_filter: (required)
        :param str environment_identifier:
        :param list[str] environment_identifiers:
        :param str service_identifier:
        :param str filter:
        :param str monitored_service_type:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'org_identifier', 'project_identifier', 'offset', 'page_size', 'services_at_risk_filter', 'environment_identifier', 'environment_identifiers', 'service_identifier', 'filter', 'monitored_service_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `list`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `list`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `list`")  # noqa: E501
        # verify the required parameter 'offset' is set
        if ('offset' not in params or
                params['offset'] is None):
            raise ValueError("Missing the required parameter `offset` when calling `list`")  # noqa: E501
        # verify the required parameter 'page_size' is set
        if ('page_size' not in params or
                params['page_size'] is None):
            raise ValueError("Missing the required parameter `page_size` when calling `list`")  # noqa: E501
        # verify the required parameter 'services_at_risk_filter' is set
        if ('services_at_risk_filter' not in params or
                params['services_at_risk_filter'] is None):
            raise ValueError("Missing the required parameter `services_at_risk_filter` when calling `list`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'account_id' in params:
            query_params.append(('accountId', params['account_id']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501
        if 'environment_identifier' in params:
            query_params.append(('environmentIdentifier', params['environment_identifier']))  # noqa: E501
        if 'environment_identifiers' in params:
            query_params.append(('environmentIdentifiers', params['environment_identifiers']))  # noqa: E501
            collection_formats['environmentIdentifiers'] = 'multi'  # noqa: E501
        if 'service_identifier' in params:
            query_params.append(('serviceIdentifier', params['service_identifier']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
        if 'monitored_service_type' in params:
            query_params.append(('monitoredServiceType', params['monitored_service_type']))  # noqa: E501
        if 'services_at_risk_filter' in params:
            query_params.append(('servicesAtRiskFilter', params['services_at_risk_filter']))  # noqa: E501

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
            '/cv/api/monitored-service', 'GET',
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

    def save_monitored_service(self, body, account_id, **kwargs):  # noqa: E501
        """Saves monitored service data  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.save_monitored_service(body, account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MonitoredService body: (required)
        :param str account_id: (required)
        :return: RestResponseMonitoredServiceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.save_monitored_service_with_http_info(body, account_id, **kwargs)  # noqa: E501
        else:
            (data) = self.save_monitored_service_with_http_info(body, account_id, **kwargs)  # noqa: E501
            return data

    def save_monitored_service_with_http_info(self, body, account_id, **kwargs):  # noqa: E501
        """Saves monitored service data  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.save_monitored_service_with_http_info(body, account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MonitoredService body: (required)
        :param str account_id: (required)
        :return: RestResponseMonitoredServiceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'account_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method save_monitored_service" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `save_monitored_service`")  # noqa: E501
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `save_monitored_service`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'account_id' in params:
            query_params.append(('accountId', params['account_id']))  # noqa: E501

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
            '/cv/api/monitored-service', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RestResponseMonitoredServiceResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def save_monitored_service_from_template_input(self, body, account_id, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """Saves monitored service from template input  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.save_monitored_service_from_template_input(body, account_id, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str body: Template input yaml for the monitored service creation from given template (required)
        :param str account_id: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :return: RestResponseMonitoredServiceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.save_monitored_service_from_template_input_with_http_info(body, account_id, org_identifier, project_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.save_monitored_service_from_template_input_with_http_info(body, account_id, org_identifier, project_identifier, **kwargs)  # noqa: E501
            return data

    def save_monitored_service_from_template_input_with_http_info(self, body, account_id, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """Saves monitored service from template input  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.save_monitored_service_from_template_input_with_http_info(body, account_id, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str body: Template input yaml for the monitored service creation from given template (required)
        :param str account_id: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :return: RestResponseMonitoredServiceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'account_id', 'org_identifier', 'project_identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method save_monitored_service_from_template_input" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `save_monitored_service_from_template_input`")  # noqa: E501
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `save_monitored_service_from_template_input`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `save_monitored_service_from_template_input`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `save_monitored_service_from_template_input`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'account_id' in params:
            query_params.append(('accountId', params['account_id']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501

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
            '/cv/api/monitored-service/template-input', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RestResponseMonitoredServiceResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def save_monitored_service_from_yaml(self, body, account_id, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """save_monitored_service_from_yaml  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.save_monitored_service_from_yaml(body, account_id, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str body: (required)
        :param str account_id: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.save_monitored_service_from_yaml_with_http_info(body, account_id, org_identifier, project_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.save_monitored_service_from_yaml_with_http_info(body, account_id, org_identifier, project_identifier, **kwargs)  # noqa: E501
            return data

    def save_monitored_service_from_yaml_with_http_info(self, body, account_id, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """save_monitored_service_from_yaml  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.save_monitored_service_from_yaml_with_http_info(body, account_id, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str body: (required)
        :param str account_id: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'account_id', 'org_identifier', 'project_identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method save_monitored_service_from_yaml" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `save_monitored_service_from_yaml`")  # noqa: E501
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `save_monitored_service_from_yaml`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `save_monitored_service_from_yaml`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `save_monitored_service_from_yaml`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'account_id' in params:
            query_params.append(('accountId', params['account_id']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501

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
            '/cv/api/monitored-service/yaml', 'POST',
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

    def set_health_monitoring_flag(self, account_id, org_identifier, project_identifier, identifier, enable, **kwargs):  # noqa: E501
        """set_health_monitoring_flag  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_health_monitoring_flag(account_id, org_identifier, project_identifier, identifier, enable, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str identifier: (required)
        :param bool enable: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.set_health_monitoring_flag_with_http_info(account_id, org_identifier, project_identifier, identifier, enable, **kwargs)  # noqa: E501
        else:
            (data) = self.set_health_monitoring_flag_with_http_info(account_id, org_identifier, project_identifier, identifier, enable, **kwargs)  # noqa: E501
            return data

    def set_health_monitoring_flag_with_http_info(self, account_id, org_identifier, project_identifier, identifier, enable, **kwargs):  # noqa: E501
        """set_health_monitoring_flag  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_health_monitoring_flag_with_http_info(account_id, org_identifier, project_identifier, identifier, enable, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str identifier: (required)
        :param bool enable: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'org_identifier', 'project_identifier', 'identifier', 'enable']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method set_health_monitoring_flag" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `set_health_monitoring_flag`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `set_health_monitoring_flag`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `set_health_monitoring_flag`")  # noqa: E501
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `set_health_monitoring_flag`")  # noqa: E501
        # verify the required parameter 'enable' is set
        if ('enable' not in params or
                params['enable'] is None):
            raise ValueError("Missing the required parameter `enable` when calling `set_health_monitoring_flag`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501

        query_params = []
        if 'account_id' in params:
            query_params.append(('accountId', params['account_id']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501
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
            '/cv/api/monitored-service/{identifier}/health-monitoring-flag', 'PUT',
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

    def update_monitored_service(self, body, account_id, identifier, **kwargs):  # noqa: E501
        """Updates monitored service data  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_monitored_service(body, account_id, identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MonitoredService body: (required)
        :param str account_id: Account Identifier for the Entity. (required)
        :param str identifier: Identifier for the Entity. (required)
        :return: RestResponseMonitoredServiceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_monitored_service_with_http_info(body, account_id, identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.update_monitored_service_with_http_info(body, account_id, identifier, **kwargs)  # noqa: E501
            return data

    def update_monitored_service_with_http_info(self, body, account_id, identifier, **kwargs):  # noqa: E501
        """Updates monitored service data  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_monitored_service_with_http_info(body, account_id, identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MonitoredService body: (required)
        :param str account_id: Account Identifier for the Entity. (required)
        :param str identifier: Identifier for the Entity. (required)
        :return: RestResponseMonitoredServiceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'account_id', 'identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_monitored_service" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_monitored_service`")  # noqa: E501
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `update_monitored_service`")  # noqa: E501
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `update_monitored_service`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501

        query_params = []
        if 'account_id' in params:
            query_params.append(('accountId', params['account_id']))  # noqa: E501

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
            '/cv/api/monitored-service/{identifier}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RestResponseMonitoredServiceResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_monitored_service_from_template_input(self, body, account_id, org_identifier, project_identifier, identifier, **kwargs):  # noqa: E501
        """Update monitored service from yaml or template  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_monitored_service_from_template_input(body, account_id, org_identifier, project_identifier, identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str body: Template input yaml for the monitored service creation from given template (required)
        :param str account_id: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str identifier: Identifier for the Entity. (required)
        :return: RestResponseMonitoredServiceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_monitored_service_from_template_input_with_http_info(body, account_id, org_identifier, project_identifier, identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.update_monitored_service_from_template_input_with_http_info(body, account_id, org_identifier, project_identifier, identifier, **kwargs)  # noqa: E501
            return data

    def update_monitored_service_from_template_input_with_http_info(self, body, account_id, org_identifier, project_identifier, identifier, **kwargs):  # noqa: E501
        """Update monitored service from yaml or template  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_monitored_service_from_template_input_with_http_info(body, account_id, org_identifier, project_identifier, identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str body: Template input yaml for the monitored service creation from given template (required)
        :param str account_id: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str identifier: Identifier for the Entity. (required)
        :return: RestResponseMonitoredServiceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'account_id', 'org_identifier', 'project_identifier', 'identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_monitored_service_from_template_input" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_monitored_service_from_template_input`")  # noqa: E501
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `update_monitored_service_from_template_input`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `update_monitored_service_from_template_input`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `update_monitored_service_from_template_input`")  # noqa: E501
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `update_monitored_service_from_template_input`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501

        query_params = []
        if 'account_id' in params:
            query_params.append(('accountId', params['account_id']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501

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
            '/cv/api/monitored-service/{identifier}/template-input', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RestResponseMonitoredServiceResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_monitored_service_from_yaml(self, body, account_id, org_identifier, project_identifier, identifier, **kwargs):  # noqa: E501
        """update_monitored_service_from_yaml  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_monitored_service_from_yaml(body, account_id, org_identifier, project_identifier, identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str body: (required)
        :param str account_id: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str identifier: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_monitored_service_from_yaml_with_http_info(body, account_id, org_identifier, project_identifier, identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.update_monitored_service_from_yaml_with_http_info(body, account_id, org_identifier, project_identifier, identifier, **kwargs)  # noqa: E501
            return data

    def update_monitored_service_from_yaml_with_http_info(self, body, account_id, org_identifier, project_identifier, identifier, **kwargs):  # noqa: E501
        """update_monitored_service_from_yaml  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_monitored_service_from_yaml_with_http_info(body, account_id, org_identifier, project_identifier, identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str body: (required)
        :param str account_id: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str identifier: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'account_id', 'org_identifier', 'project_identifier', 'identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_monitored_service_from_yaml" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_monitored_service_from_yaml`")  # noqa: E501
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `update_monitored_service_from_yaml`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `update_monitored_service_from_yaml`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `update_monitored_service_from_yaml`")  # noqa: E501
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `update_monitored_service_from_yaml`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501

        query_params = []
        if 'account_id' in params:
            query_params.append(('accountId', params['account_id']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501

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
            '/cv/api/monitored-service/{identifier}/yaml', 'PUT',
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

    def yaml_template(self, account_id, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """yaml_template  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.yaml_template(account_id, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str type:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.yaml_template_with_http_info(account_id, org_identifier, project_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.yaml_template_with_http_info(account_id, org_identifier, project_identifier, **kwargs)  # noqa: E501
            return data

    def yaml_template_with_http_info(self, account_id, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """yaml_template  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.yaml_template_with_http_info(account_id, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str type:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'org_identifier', 'project_identifier', 'type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method yaml_template" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `yaml_template`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `yaml_template`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `yaml_template`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'account_id' in params:
            query_params.append(('accountId', params['account_id']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501
        if 'type' in params:
            query_params.append(('type', params['type']))  # noqa: E501

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
            '/cv/api/monitored-service/yaml-template', 'GET',
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
