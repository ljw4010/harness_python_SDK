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


class ApplicationsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def agent_application_service_create(self, body, agent_identifier, **kwargs):  # noqa: E501
        """Create creates an application  # noqa: E501

        Creates application in project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_application_service_create(body, agent_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ApplicationsApplicationCreateRequest body: (required)
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str account_identifier: Account Identifier for the Entity.
        :param str org_identifier: Organization Identifier for the Entity.
        :param str project_identifier: Project Identifier for the Entity.
        :param str cluster_identifier:
        :param str repo_identifier:
        :return: Servicev1Application
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.agent_application_service_create_with_http_info(body, agent_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.agent_application_service_create_with_http_info(body, agent_identifier, **kwargs)  # noqa: E501
            return data

    def agent_application_service_create_with_http_info(self, body, agent_identifier, **kwargs):  # noqa: E501
        """Create creates an application  # noqa: E501

        Creates application in project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_application_service_create_with_http_info(body, agent_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ApplicationsApplicationCreateRequest body: (required)
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str account_identifier: Account Identifier for the Entity.
        :param str org_identifier: Organization Identifier for the Entity.
        :param str project_identifier: Project Identifier for the Entity.
        :param str cluster_identifier:
        :param str repo_identifier:
        :return: Servicev1Application
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'agent_identifier', 'account_identifier', 'org_identifier', 'project_identifier', 'cluster_identifier', 'repo_identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method agent_application_service_create" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `agent_application_service_create`")  # noqa: E501
        # verify the required parameter 'agent_identifier' is set
        if ('agent_identifier' not in params or
                params['agent_identifier'] is None):
            raise ValueError("Missing the required parameter `agent_identifier` when calling `agent_application_service_create`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'agent_identifier' in params:
            path_params['agentIdentifier'] = params['agent_identifier']  # noqa: E501

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501
        if 'cluster_identifier' in params:
            query_params.append(('clusterIdentifier', params['cluster_identifier']))  # noqa: E501
        if 'repo_identifier' in params:
            query_params.append(('repoIdentifier', params['repo_identifier']))  # noqa: E501

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
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/gitops/api/v1/agents/{agentIdentifier}/applications', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Servicev1Application',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def agent_application_service_delete(self, agent_identifier, request_name, **kwargs):  # noqa: E501
        """Delete deletes an application  # noqa: E501

        Delete deletes an application.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_application_service_delete(agent_identifier, request_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str request_name: (required)
        :param str account_identifier: Account Identifier for the Entity.
        :param str org_identifier: Organization Identifier for the Entity.
        :param str project_identifier: Project Identifier for the Entity.
        :param bool request_cascade:
        :param str request_propagation_policy:
        :param bool options_remove_existing_finalizers:
        :return: ApplicationsApplicationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.agent_application_service_delete_with_http_info(agent_identifier, request_name, **kwargs)  # noqa: E501
        else:
            (data) = self.agent_application_service_delete_with_http_info(agent_identifier, request_name, **kwargs)  # noqa: E501
            return data

    def agent_application_service_delete_with_http_info(self, agent_identifier, request_name, **kwargs):  # noqa: E501
        """Delete deletes an application  # noqa: E501

        Delete deletes an application.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_application_service_delete_with_http_info(agent_identifier, request_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str request_name: (required)
        :param str account_identifier: Account Identifier for the Entity.
        :param str org_identifier: Organization Identifier for the Entity.
        :param str project_identifier: Project Identifier for the Entity.
        :param bool request_cascade:
        :param str request_propagation_policy:
        :param bool options_remove_existing_finalizers:
        :return: ApplicationsApplicationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['agent_identifier', 'request_name', 'account_identifier', 'org_identifier', 'project_identifier', 'request_cascade', 'request_propagation_policy', 'options_remove_existing_finalizers']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method agent_application_service_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'agent_identifier' is set
        if ('agent_identifier' not in params or
                params['agent_identifier'] is None):
            raise ValueError("Missing the required parameter `agent_identifier` when calling `agent_application_service_delete`")  # noqa: E501
        # verify the required parameter 'request_name' is set
        if ('request_name' not in params or
                params['request_name'] is None):
            raise ValueError("Missing the required parameter `request_name` when calling `agent_application_service_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'agent_identifier' in params:
            path_params['agentIdentifier'] = params['agent_identifier']  # noqa: E501
        if 'request_name' in params:
            path_params['request.name'] = params['request_name']  # noqa: E501

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501
        if 'request_cascade' in params:
            query_params.append(('request.cascade', params['request_cascade']))  # noqa: E501
        if 'request_propagation_policy' in params:
            query_params.append(('request.propagationPolicy', params['request_propagation_policy']))  # noqa: E501
        if 'options_remove_existing_finalizers' in params:
            query_params.append(('options.removeExistingFinalizers', params['options_remove_existing_finalizers']))  # noqa: E501

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
            '/gitops/api/v1/agents/{agentIdentifier}/applications/{request.name}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApplicationsApplicationResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def agent_application_service_delete_resource(self, agent_identifier, request_name, **kwargs):  # noqa: E501
        """DeleteResource deletes a single application resource  # noqa: E501

        DeleteResource deletes a single application resource.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_application_service_delete_resource(agent_identifier, request_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str request_name: (required)
        :param str account_identifier: Account Identifier for the Entity.
        :param str org_identifier: Organization Identifier for the Entity.
        :param str project_identifier: Project Identifier for the Entity.
        :param str request_namespace:
        :param str request_resource_name:
        :param str request_version:
        :param str request_group:
        :param str request_kind:
        :param bool request_force:
        :param bool request_orphan:
        :return: ApplicationsApplicationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.agent_application_service_delete_resource_with_http_info(agent_identifier, request_name, **kwargs)  # noqa: E501
        else:
            (data) = self.agent_application_service_delete_resource_with_http_info(agent_identifier, request_name, **kwargs)  # noqa: E501
            return data

    def agent_application_service_delete_resource_with_http_info(self, agent_identifier, request_name, **kwargs):  # noqa: E501
        """DeleteResource deletes a single application resource  # noqa: E501

        DeleteResource deletes a single application resource.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_application_service_delete_resource_with_http_info(agent_identifier, request_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str request_name: (required)
        :param str account_identifier: Account Identifier for the Entity.
        :param str org_identifier: Organization Identifier for the Entity.
        :param str project_identifier: Project Identifier for the Entity.
        :param str request_namespace:
        :param str request_resource_name:
        :param str request_version:
        :param str request_group:
        :param str request_kind:
        :param bool request_force:
        :param bool request_orphan:
        :return: ApplicationsApplicationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['agent_identifier', 'request_name', 'account_identifier', 'org_identifier', 'project_identifier', 'request_namespace', 'request_resource_name', 'request_version', 'request_group', 'request_kind', 'request_force', 'request_orphan']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method agent_application_service_delete_resource" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'agent_identifier' is set
        if ('agent_identifier' not in params or
                params['agent_identifier'] is None):
            raise ValueError("Missing the required parameter `agent_identifier` when calling `agent_application_service_delete_resource`")  # noqa: E501
        # verify the required parameter 'request_name' is set
        if ('request_name' not in params or
                params['request_name'] is None):
            raise ValueError("Missing the required parameter `request_name` when calling `agent_application_service_delete_resource`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'agent_identifier' in params:
            path_params['agentIdentifier'] = params['agent_identifier']  # noqa: E501
        if 'request_name' in params:
            path_params['request.name'] = params['request_name']  # noqa: E501

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501
        if 'request_namespace' in params:
            query_params.append(('request.namespace', params['request_namespace']))  # noqa: E501
        if 'request_resource_name' in params:
            query_params.append(('request.resourceName', params['request_resource_name']))  # noqa: E501
        if 'request_version' in params:
            query_params.append(('request.version', params['request_version']))  # noqa: E501
        if 'request_group' in params:
            query_params.append(('request.group', params['request_group']))  # noqa: E501
        if 'request_kind' in params:
            query_params.append(('request.kind', params['request_kind']))  # noqa: E501
        if 'request_force' in params:
            query_params.append(('request.force', params['request_force']))  # noqa: E501
        if 'request_orphan' in params:
            query_params.append(('request.orphan', params['request_orphan']))  # noqa: E501

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
            '/gitops/api/v1/agents/{agentIdentifier}/applications/{request.name}/resource', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApplicationsApplicationResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def agent_application_service_get(self, agent_identifier, query_name, account_identifier, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """Get returns an application by name  # noqa: E501

         Get returns an application by name  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_application_service_get(agent_identifier, query_name, account_identifier, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str query_name: the application's name (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str query_refresh: forces application reconciliation if set to true.
        :param list[str] query_project: the project names to restrict returned list applications.
        :param str query_resource_version: when specified with a watch call, shows changes that occur after that particular version of a resource.
        :param str query_selector: the selector to to restrict returned list to applications only with matched labels.
        :param str query_repo: the repoURL to restrict returned list applications.
        :return: Servicev1Application
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.agent_application_service_get_with_http_info(agent_identifier, query_name, account_identifier, org_identifier, project_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.agent_application_service_get_with_http_info(agent_identifier, query_name, account_identifier, org_identifier, project_identifier, **kwargs)  # noqa: E501
            return data

    def agent_application_service_get_with_http_info(self, agent_identifier, query_name, account_identifier, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """Get returns an application by name  # noqa: E501

         Get returns an application by name  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_application_service_get_with_http_info(agent_identifier, query_name, account_identifier, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str query_name: the application's name (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str query_refresh: forces application reconciliation if set to true.
        :param list[str] query_project: the project names to restrict returned list applications.
        :param str query_resource_version: when specified with a watch call, shows changes that occur after that particular version of a resource.
        :param str query_selector: the selector to to restrict returned list to applications only with matched labels.
        :param str query_repo: the repoURL to restrict returned list applications.
        :return: Servicev1Application
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['agent_identifier', 'query_name', 'account_identifier', 'org_identifier', 'project_identifier', 'query_refresh', 'query_project', 'query_resource_version', 'query_selector', 'query_repo']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method agent_application_service_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'agent_identifier' is set
        if ('agent_identifier' not in params or
                params['agent_identifier'] is None):
            raise ValueError("Missing the required parameter `agent_identifier` when calling `agent_application_service_get`")  # noqa: E501
        # verify the required parameter 'query_name' is set
        if ('query_name' not in params or
                params['query_name'] is None):
            raise ValueError("Missing the required parameter `query_name` when calling `agent_application_service_get`")  # noqa: E501
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `agent_application_service_get`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `agent_application_service_get`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `agent_application_service_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'agent_identifier' in params:
            path_params['agentIdentifier'] = params['agent_identifier']  # noqa: E501
        if 'query_name' in params:
            path_params['query.name'] = params['query_name']  # noqa: E501

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501
        if 'query_refresh' in params:
            query_params.append(('query.refresh', params['query_refresh']))  # noqa: E501
        if 'query_project' in params:
            query_params.append(('query.project', params['query_project']))  # noqa: E501
            collection_formats['query.project'] = 'multi'  # noqa: E501
        if 'query_resource_version' in params:
            query_params.append(('query.resourceVersion', params['query_resource_version']))  # noqa: E501
        if 'query_selector' in params:
            query_params.append(('query.selector', params['query_selector']))  # noqa: E501
        if 'query_repo' in params:
            query_params.append(('query.repo', params['query_repo']))  # noqa: E501

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
            '/gitops/api/v1/agents/{agentIdentifier}/applications/{query.name}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Servicev1Application',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def agent_application_service_get_application_sync_windows(self, agent_identifier, query_name, account_identifier, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """Get returns sync windows of the application  # noqa: E501

        GetApplicationSyncWindows returns sync windows of the application.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_application_service_get_application_sync_windows(agent_identifier, query_name, account_identifier, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str query_name: (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :return: ApplicationsApplicationSyncWindowsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.agent_application_service_get_application_sync_windows_with_http_info(agent_identifier, query_name, account_identifier, org_identifier, project_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.agent_application_service_get_application_sync_windows_with_http_info(agent_identifier, query_name, account_identifier, org_identifier, project_identifier, **kwargs)  # noqa: E501
            return data

    def agent_application_service_get_application_sync_windows_with_http_info(self, agent_identifier, query_name, account_identifier, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """Get returns sync windows of the application  # noqa: E501

        GetApplicationSyncWindows returns sync windows of the application.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_application_service_get_application_sync_windows_with_http_info(agent_identifier, query_name, account_identifier, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str query_name: (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :return: ApplicationsApplicationSyncWindowsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['agent_identifier', 'query_name', 'account_identifier', 'org_identifier', 'project_identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method agent_application_service_get_application_sync_windows" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'agent_identifier' is set
        if ('agent_identifier' not in params or
                params['agent_identifier'] is None):
            raise ValueError("Missing the required parameter `agent_identifier` when calling `agent_application_service_get_application_sync_windows`")  # noqa: E501
        # verify the required parameter 'query_name' is set
        if ('query_name' not in params or
                params['query_name'] is None):
            raise ValueError("Missing the required parameter `query_name` when calling `agent_application_service_get_application_sync_windows`")  # noqa: E501
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `agent_application_service_get_application_sync_windows`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `agent_application_service_get_application_sync_windows`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `agent_application_service_get_application_sync_windows`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'agent_identifier' in params:
            path_params['agentIdentifier'] = params['agent_identifier']  # noqa: E501
        if 'query_name' in params:
            path_params['query.name'] = params['query_name']  # noqa: E501

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501
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
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/gitops/api/v1/agents/{agentIdentifier}/applications/{query.name}/syncwindows', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApplicationsApplicationSyncWindowsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def agent_application_service_get_manifests(self, agent_identifier, query_name, account_identifier, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """GetManifests returns application manifests  # noqa: E501

        GetManifests returns application manifests.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_application_service_get_manifests(agent_identifier, query_name, account_identifier, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str query_name: (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str query_revision:
        :return: RepositoriesManifestResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.agent_application_service_get_manifests_with_http_info(agent_identifier, query_name, account_identifier, org_identifier, project_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.agent_application_service_get_manifests_with_http_info(agent_identifier, query_name, account_identifier, org_identifier, project_identifier, **kwargs)  # noqa: E501
            return data

    def agent_application_service_get_manifests_with_http_info(self, agent_identifier, query_name, account_identifier, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """GetManifests returns application manifests  # noqa: E501

        GetManifests returns application manifests.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_application_service_get_manifests_with_http_info(agent_identifier, query_name, account_identifier, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str query_name: (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str query_revision:
        :return: RepositoriesManifestResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['agent_identifier', 'query_name', 'account_identifier', 'org_identifier', 'project_identifier', 'query_revision']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method agent_application_service_get_manifests" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'agent_identifier' is set
        if ('agent_identifier' not in params or
                params['agent_identifier'] is None):
            raise ValueError("Missing the required parameter `agent_identifier` when calling `agent_application_service_get_manifests`")  # noqa: E501
        # verify the required parameter 'query_name' is set
        if ('query_name' not in params or
                params['query_name'] is None):
            raise ValueError("Missing the required parameter `query_name` when calling `agent_application_service_get_manifests`")  # noqa: E501
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `agent_application_service_get_manifests`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `agent_application_service_get_manifests`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `agent_application_service_get_manifests`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'agent_identifier' in params:
            path_params['agentIdentifier'] = params['agent_identifier']  # noqa: E501
        if 'query_name' in params:
            path_params['query.name'] = params['query_name']  # noqa: E501

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501
        if 'query_revision' in params:
            query_params.append(('query.revision', params['query_revision']))  # noqa: E501

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
            '/gitops/api/v1/agents/{agentIdentifier}/applications/{query.name}/manifests', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RepositoriesManifestResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def agent_application_service_get_resource(self, agent_identifier, request_name, **kwargs):  # noqa: E501
        """GetResource returns single application resource  # noqa: E501

        GetResource returns single application resource.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_application_service_get_resource(agent_identifier, request_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str request_name: (required)
        :param str account_identifier: Account Identifier for the Entity.
        :param str org_identifier: Organization Identifier for the Entity.
        :param str project_identifier: Project Identifier for the Entity.
        :param str request_namespace:
        :param str request_resource_name:
        :param str request_version:
        :param str request_group:
        :param str request_kind:
        :return: ApplicationsApplicationResourceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.agent_application_service_get_resource_with_http_info(agent_identifier, request_name, **kwargs)  # noqa: E501
        else:
            (data) = self.agent_application_service_get_resource_with_http_info(agent_identifier, request_name, **kwargs)  # noqa: E501
            return data

    def agent_application_service_get_resource_with_http_info(self, agent_identifier, request_name, **kwargs):  # noqa: E501
        """GetResource returns single application resource  # noqa: E501

        GetResource returns single application resource.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_application_service_get_resource_with_http_info(agent_identifier, request_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str request_name: (required)
        :param str account_identifier: Account Identifier for the Entity.
        :param str org_identifier: Organization Identifier for the Entity.
        :param str project_identifier: Project Identifier for the Entity.
        :param str request_namespace:
        :param str request_resource_name:
        :param str request_version:
        :param str request_group:
        :param str request_kind:
        :return: ApplicationsApplicationResourceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['agent_identifier', 'request_name', 'account_identifier', 'org_identifier', 'project_identifier', 'request_namespace', 'request_resource_name', 'request_version', 'request_group', 'request_kind']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method agent_application_service_get_resource" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'agent_identifier' is set
        if ('agent_identifier' not in params or
                params['agent_identifier'] is None):
            raise ValueError("Missing the required parameter `agent_identifier` when calling `agent_application_service_get_resource`")  # noqa: E501
        # verify the required parameter 'request_name' is set
        if ('request_name' not in params or
                params['request_name'] is None):
            raise ValueError("Missing the required parameter `request_name` when calling `agent_application_service_get_resource`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'agent_identifier' in params:
            path_params['agentIdentifier'] = params['agent_identifier']  # noqa: E501
        if 'request_name' in params:
            path_params['request.name'] = params['request_name']  # noqa: E501

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501
        if 'request_namespace' in params:
            query_params.append(('request.namespace', params['request_namespace']))  # noqa: E501
        if 'request_resource_name' in params:
            query_params.append(('request.resourceName', params['request_resource_name']))  # noqa: E501
        if 'request_version' in params:
            query_params.append(('request.version', params['request_version']))  # noqa: E501
        if 'request_group' in params:
            query_params.append(('request.group', params['request_group']))  # noqa: E501
        if 'request_kind' in params:
            query_params.append(('request.kind', params['request_kind']))  # noqa: E501

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
            '/gitops/api/v1/agents/{agentIdentifier}/applications/{request.name}/resource', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApplicationsApplicationResourceResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def agent_application_service_list(self, agent_identifier, account_identifier, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """List returns list of applications for a specific agent  # noqa: E501

        List returns list of applications for a specific agent.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_application_service_list(agent_identifier, account_identifier, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str query_name: the application's name.
        :param str query_refresh: forces application reconciliation if set to true.
        :param list[str] query_project: the project names to restrict returned list applications.
        :param str query_resource_version: when specified with a watch call, shows changes that occur after that particular version of a resource.
        :param str query_selector: the selector to to restrict returned list to applications only with matched labels.
        :param str query_repo: the repoURL to restrict returned list applications.
        :return: ApplicationsApplicationList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.agent_application_service_list_with_http_info(agent_identifier, account_identifier, org_identifier, project_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.agent_application_service_list_with_http_info(agent_identifier, account_identifier, org_identifier, project_identifier, **kwargs)  # noqa: E501
            return data

    def agent_application_service_list_with_http_info(self, agent_identifier, account_identifier, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """List returns list of applications for a specific agent  # noqa: E501

        List returns list of applications for a specific agent.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_application_service_list_with_http_info(agent_identifier, account_identifier, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str query_name: the application's name.
        :param str query_refresh: forces application reconciliation if set to true.
        :param list[str] query_project: the project names to restrict returned list applications.
        :param str query_resource_version: when specified with a watch call, shows changes that occur after that particular version of a resource.
        :param str query_selector: the selector to to restrict returned list to applications only with matched labels.
        :param str query_repo: the repoURL to restrict returned list applications.
        :return: ApplicationsApplicationList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['agent_identifier', 'account_identifier', 'org_identifier', 'project_identifier', 'query_name', 'query_refresh', 'query_project', 'query_resource_version', 'query_selector', 'query_repo']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method agent_application_service_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'agent_identifier' is set
        if ('agent_identifier' not in params or
                params['agent_identifier'] is None):
            raise ValueError("Missing the required parameter `agent_identifier` when calling `agent_application_service_list`")  # noqa: E501
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `agent_application_service_list`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `agent_application_service_list`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `agent_application_service_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'agent_identifier' in params:
            path_params['agentIdentifier'] = params['agent_identifier']  # noqa: E501

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501
        if 'query_name' in params:
            query_params.append(('query.name', params['query_name']))  # noqa: E501
        if 'query_refresh' in params:
            query_params.append(('query.refresh', params['query_refresh']))  # noqa: E501
        if 'query_project' in params:
            query_params.append(('query.project', params['query_project']))  # noqa: E501
            collection_formats['query.project'] = 'multi'  # noqa: E501
        if 'query_resource_version' in params:
            query_params.append(('query.resourceVersion', params['query_resource_version']))  # noqa: E501
        if 'query_selector' in params:
            query_params.append(('query.selector', params['query_selector']))  # noqa: E501
        if 'query_repo' in params:
            query_params.append(('query.repo', params['query_repo']))  # noqa: E501

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
            '/gitops/api/v1/agents/{agentIdentifier}/applications', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApplicationsApplicationList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def agent_application_service_list_resource_actions(self, agent_identifier, request_name, account_identifier, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """ListResourceActions returns list of resource actions  # noqa: E501

        ListResourceActions returns list of resource actions.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_application_service_list_resource_actions(agent_identifier, request_name, account_identifier, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str request_name: (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str request_namespace:
        :param str request_resource_name:
        :param str request_version:
        :param str request_group:
        :param str request_kind:
        :return: ApplicationsResourceActionsListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.agent_application_service_list_resource_actions_with_http_info(agent_identifier, request_name, account_identifier, org_identifier, project_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.agent_application_service_list_resource_actions_with_http_info(agent_identifier, request_name, account_identifier, org_identifier, project_identifier, **kwargs)  # noqa: E501
            return data

    def agent_application_service_list_resource_actions_with_http_info(self, agent_identifier, request_name, account_identifier, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """ListResourceActions returns list of resource actions  # noqa: E501

        ListResourceActions returns list of resource actions.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_application_service_list_resource_actions_with_http_info(agent_identifier, request_name, account_identifier, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str request_name: (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str request_namespace:
        :param str request_resource_name:
        :param str request_version:
        :param str request_group:
        :param str request_kind:
        :return: ApplicationsResourceActionsListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['agent_identifier', 'request_name', 'account_identifier', 'org_identifier', 'project_identifier', 'request_namespace', 'request_resource_name', 'request_version', 'request_group', 'request_kind']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method agent_application_service_list_resource_actions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'agent_identifier' is set
        if ('agent_identifier' not in params or
                params['agent_identifier'] is None):
            raise ValueError("Missing the required parameter `agent_identifier` when calling `agent_application_service_list_resource_actions`")  # noqa: E501
        # verify the required parameter 'request_name' is set
        if ('request_name' not in params or
                params['request_name'] is None):
            raise ValueError("Missing the required parameter `request_name` when calling `agent_application_service_list_resource_actions`")  # noqa: E501
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `agent_application_service_list_resource_actions`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `agent_application_service_list_resource_actions`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `agent_application_service_list_resource_actions`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'agent_identifier' in params:
            path_params['agentIdentifier'] = params['agent_identifier']  # noqa: E501
        if 'request_name' in params:
            path_params['request.name'] = params['request_name']  # noqa: E501

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501
        if 'request_namespace' in params:
            query_params.append(('request.namespace', params['request_namespace']))  # noqa: E501
        if 'request_resource_name' in params:
            query_params.append(('request.resourceName', params['request_resource_name']))  # noqa: E501
        if 'request_version' in params:
            query_params.append(('request.version', params['request_version']))  # noqa: E501
        if 'request_group' in params:
            query_params.append(('request.group', params['request_group']))  # noqa: E501
        if 'request_kind' in params:
            query_params.append(('request.kind', params['request_kind']))  # noqa: E501

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
            '/gitops/api/v1/agents/{agentIdentifier}/applications/{request.name}/resource/actions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApplicationsResourceActionsListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def agent_application_service_list_resource_events(self, agent_identifier, query_name, account_identifier, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """ListResourceEvents returns a list of event resources  # noqa: E501

        ListResourceEvents returns list of event resources.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_application_service_list_resource_events(agent_identifier, query_name, account_identifier, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str query_name: (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str query_resource_namespace:
        :param str query_resource_name:
        :param str query_resource_uid:
        :return: V1EventList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.agent_application_service_list_resource_events_with_http_info(agent_identifier, query_name, account_identifier, org_identifier, project_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.agent_application_service_list_resource_events_with_http_info(agent_identifier, query_name, account_identifier, org_identifier, project_identifier, **kwargs)  # noqa: E501
            return data

    def agent_application_service_list_resource_events_with_http_info(self, agent_identifier, query_name, account_identifier, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """ListResourceEvents returns a list of event resources  # noqa: E501

        ListResourceEvents returns list of event resources.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_application_service_list_resource_events_with_http_info(agent_identifier, query_name, account_identifier, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str query_name: (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str query_resource_namespace:
        :param str query_resource_name:
        :param str query_resource_uid:
        :return: V1EventList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['agent_identifier', 'query_name', 'account_identifier', 'org_identifier', 'project_identifier', 'query_resource_namespace', 'query_resource_name', 'query_resource_uid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method agent_application_service_list_resource_events" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'agent_identifier' is set
        if ('agent_identifier' not in params or
                params['agent_identifier'] is None):
            raise ValueError("Missing the required parameter `agent_identifier` when calling `agent_application_service_list_resource_events`")  # noqa: E501
        # verify the required parameter 'query_name' is set
        if ('query_name' not in params or
                params['query_name'] is None):
            raise ValueError("Missing the required parameter `query_name` when calling `agent_application_service_list_resource_events`")  # noqa: E501
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `agent_application_service_list_resource_events`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `agent_application_service_list_resource_events`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `agent_application_service_list_resource_events`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'agent_identifier' in params:
            path_params['agentIdentifier'] = params['agent_identifier']  # noqa: E501
        if 'query_name' in params:
            path_params['query.name'] = params['query_name']  # noqa: E501

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501
        if 'query_resource_namespace' in params:
            query_params.append(('query.resourceNamespace', params['query_resource_namespace']))  # noqa: E501
        if 'query_resource_name' in params:
            query_params.append(('query.resourceName', params['query_resource_name']))  # noqa: E501
        if 'query_resource_uid' in params:
            query_params.append(('query.resourceUID', params['query_resource_uid']))  # noqa: E501

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
            '/gitops/api/v1/agents/{agentIdentifier}/applications/{query.name}/events', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1EventList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def agent_application_service_managed_resources(self, agent_identifier, query_application_name, account_identifier, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """ManagedResources returns list of managed resources  # noqa: E501

        ManagedResources returns list of managed resources.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_application_service_managed_resources(agent_identifier, query_application_name, account_identifier, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str query_application_name: (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str query_namespace:
        :param str query_name:
        :param str query_version:
        :param str query_group:
        :param str query_kind:
        :return: ApplicationsManagedResourcesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.agent_application_service_managed_resources_with_http_info(agent_identifier, query_application_name, account_identifier, org_identifier, project_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.agent_application_service_managed_resources_with_http_info(agent_identifier, query_application_name, account_identifier, org_identifier, project_identifier, **kwargs)  # noqa: E501
            return data

    def agent_application_service_managed_resources_with_http_info(self, agent_identifier, query_application_name, account_identifier, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """ManagedResources returns list of managed resources  # noqa: E501

        ManagedResources returns list of managed resources.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_application_service_managed_resources_with_http_info(agent_identifier, query_application_name, account_identifier, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str query_application_name: (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str query_namespace:
        :param str query_name:
        :param str query_version:
        :param str query_group:
        :param str query_kind:
        :return: ApplicationsManagedResourcesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['agent_identifier', 'query_application_name', 'account_identifier', 'org_identifier', 'project_identifier', 'query_namespace', 'query_name', 'query_version', 'query_group', 'query_kind']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method agent_application_service_managed_resources" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'agent_identifier' is set
        if ('agent_identifier' not in params or
                params['agent_identifier'] is None):
            raise ValueError("Missing the required parameter `agent_identifier` when calling `agent_application_service_managed_resources`")  # noqa: E501
        # verify the required parameter 'query_application_name' is set
        if ('query_application_name' not in params or
                params['query_application_name'] is None):
            raise ValueError("Missing the required parameter `query_application_name` when calling `agent_application_service_managed_resources`")  # noqa: E501
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `agent_application_service_managed_resources`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `agent_application_service_managed_resources`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `agent_application_service_managed_resources`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'agent_identifier' in params:
            path_params['agentIdentifier'] = params['agent_identifier']  # noqa: E501
        if 'query_application_name' in params:
            path_params['query.applicationName'] = params['query_application_name']  # noqa: E501

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501
        if 'query_namespace' in params:
            query_params.append(('query.namespace', params['query_namespace']))  # noqa: E501
        if 'query_name' in params:
            query_params.append(('query.name', params['query_name']))  # noqa: E501
        if 'query_version' in params:
            query_params.append(('query.version', params['query_version']))  # noqa: E501
        if 'query_group' in params:
            query_params.append(('query.group', params['query_group']))  # noqa: E501
        if 'query_kind' in params:
            query_params.append(('query.kind', params['query_kind']))  # noqa: E501

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
            '/gitops/api/v1/agents/{agentIdentifier}/applications/{query.applicationName}/managed-resources', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApplicationsManagedResourcesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def agent_application_service_patch(self, body, agent_identifier, request_name, **kwargs):  # noqa: E501
        """Patch patch an application  # noqa: E501

        Patch applys a patches to an application.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_application_service_patch(body, agent_identifier, request_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Servicev1ApplicationPatchRequest body: (required)
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str request_name: (required)
        :return: Servicev1Application
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.agent_application_service_patch_with_http_info(body, agent_identifier, request_name, **kwargs)  # noqa: E501
        else:
            (data) = self.agent_application_service_patch_with_http_info(body, agent_identifier, request_name, **kwargs)  # noqa: E501
            return data

    def agent_application_service_patch_with_http_info(self, body, agent_identifier, request_name, **kwargs):  # noqa: E501
        """Patch patch an application  # noqa: E501

        Patch applys a patches to an application.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_application_service_patch_with_http_info(body, agent_identifier, request_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Servicev1ApplicationPatchRequest body: (required)
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str request_name: (required)
        :return: Servicev1Application
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'agent_identifier', 'request_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method agent_application_service_patch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `agent_application_service_patch`")  # noqa: E501
        # verify the required parameter 'agent_identifier' is set
        if ('agent_identifier' not in params or
                params['agent_identifier'] is None):
            raise ValueError("Missing the required parameter `agent_identifier` when calling `agent_application_service_patch`")  # noqa: E501
        # verify the required parameter 'request_name' is set
        if ('request_name' not in params or
                params['request_name'] is None):
            raise ValueError("Missing the required parameter `request_name` when calling `agent_application_service_patch`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'agent_identifier' in params:
            path_params['agentIdentifier'] = params['agent_identifier']  # noqa: E501
        if 'request_name' in params:
            path_params['request.name'] = params['request_name']  # noqa: E501

        query_params = []

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
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/gitops/api/v1/agents/{agentIdentifier}/applications/{request.name}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Servicev1Application',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def agent_application_service_patch_resource(self, body, agent_identifier, request_name, **kwargs):  # noqa: E501
        """PatchResource patch single application resource  # noqa: E501

        PatchResource patch single application resource.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_application_service_patch_resource(body, agent_identifier, request_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ApplicationsApplicationResourcePatchRequest body: (required)
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str request_name: (required)
        :param str account_identifier: Account Identifier for the Entity.
        :param str org_identifier: Organization Identifier for the Entity.
        :param str project_identifier: Project Identifier for the Entity.
        :return: ApplicationsApplicationResourceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.agent_application_service_patch_resource_with_http_info(body, agent_identifier, request_name, **kwargs)  # noqa: E501
        else:
            (data) = self.agent_application_service_patch_resource_with_http_info(body, agent_identifier, request_name, **kwargs)  # noqa: E501
            return data

    def agent_application_service_patch_resource_with_http_info(self, body, agent_identifier, request_name, **kwargs):  # noqa: E501
        """PatchResource patch single application resource  # noqa: E501

        PatchResource patch single application resource.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_application_service_patch_resource_with_http_info(body, agent_identifier, request_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ApplicationsApplicationResourcePatchRequest body: (required)
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str request_name: (required)
        :param str account_identifier: Account Identifier for the Entity.
        :param str org_identifier: Organization Identifier for the Entity.
        :param str project_identifier: Project Identifier for the Entity.
        :return: ApplicationsApplicationResourceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'agent_identifier', 'request_name', 'account_identifier', 'org_identifier', 'project_identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method agent_application_service_patch_resource" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `agent_application_service_patch_resource`")  # noqa: E501
        # verify the required parameter 'agent_identifier' is set
        if ('agent_identifier' not in params or
                params['agent_identifier'] is None):
            raise ValueError("Missing the required parameter `agent_identifier` when calling `agent_application_service_patch_resource`")  # noqa: E501
        # verify the required parameter 'request_name' is set
        if ('request_name' not in params or
                params['request_name'] is None):
            raise ValueError("Missing the required parameter `request_name` when calling `agent_application_service_patch_resource`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'agent_identifier' in params:
            path_params['agentIdentifier'] = params['agent_identifier']  # noqa: E501
        if 'request_name' in params:
            path_params['request.name'] = params['request_name']  # noqa: E501

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501
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
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/gitops/api/v1/agents/{agentIdentifier}/applications/{request.name}/resource', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApplicationsApplicationResourceResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def agent_application_service_pod_logs(self, agent_identifier, query_name, query_pod_name, account_identifier, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """PodLogs returns stream of log entries for the specified pod(s).  # noqa: E501

        PodLogs returns stream of log entries for the specified pod(s).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_application_service_pod_logs(agent_identifier, query_name, query_pod_name, account_identifier, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str query_name: (required)
        :param str query_pod_name: (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str query_namespace:
        :param str query_container:
        :param str query_since_seconds:
        :param str query_since_time_seconds: Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be from 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z inclusive.
        :param int query_since_time_nanos: Non-negative fractions of a second at nanosecond resolution. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be from 0 to 999,999,999 inclusive. This field may be limited in precision depending on context.
        :param str query_tail_lines:
        :param bool query_follow:
        :param str query_until_time:
        :param str query_filter:
        :param str query_kind:
        :param str query_group:
        :param str query_resource_name:
        :param bool query_previous:
        :return: StreamResultOfApplicationsLogEntry
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.agent_application_service_pod_logs_with_http_info(agent_identifier, query_name, query_pod_name, account_identifier, org_identifier, project_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.agent_application_service_pod_logs_with_http_info(agent_identifier, query_name, query_pod_name, account_identifier, org_identifier, project_identifier, **kwargs)  # noqa: E501
            return data

    def agent_application_service_pod_logs_with_http_info(self, agent_identifier, query_name, query_pod_name, account_identifier, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """PodLogs returns stream of log entries for the specified pod(s).  # noqa: E501

        PodLogs returns stream of log entries for the specified pod(s).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_application_service_pod_logs_with_http_info(agent_identifier, query_name, query_pod_name, account_identifier, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str query_name: (required)
        :param str query_pod_name: (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str query_namespace:
        :param str query_container:
        :param str query_since_seconds:
        :param str query_since_time_seconds: Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be from 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z inclusive.
        :param int query_since_time_nanos: Non-negative fractions of a second at nanosecond resolution. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be from 0 to 999,999,999 inclusive. This field may be limited in precision depending on context.
        :param str query_tail_lines:
        :param bool query_follow:
        :param str query_until_time:
        :param str query_filter:
        :param str query_kind:
        :param str query_group:
        :param str query_resource_name:
        :param bool query_previous:
        :return: StreamResultOfApplicationsLogEntry
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['agent_identifier', 'query_name', 'query_pod_name', 'account_identifier', 'org_identifier', 'project_identifier', 'query_namespace', 'query_container', 'query_since_seconds', 'query_since_time_seconds', 'query_since_time_nanos', 'query_tail_lines', 'query_follow', 'query_until_time', 'query_filter', 'query_kind', 'query_group', 'query_resource_name', 'query_previous']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method agent_application_service_pod_logs" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'agent_identifier' is set
        if ('agent_identifier' not in params or
                params['agent_identifier'] is None):
            raise ValueError("Missing the required parameter `agent_identifier` when calling `agent_application_service_pod_logs`")  # noqa: E501
        # verify the required parameter 'query_name' is set
        if ('query_name' not in params or
                params['query_name'] is None):
            raise ValueError("Missing the required parameter `query_name` when calling `agent_application_service_pod_logs`")  # noqa: E501
        # verify the required parameter 'query_pod_name' is set
        if ('query_pod_name' not in params or
                params['query_pod_name'] is None):
            raise ValueError("Missing the required parameter `query_pod_name` when calling `agent_application_service_pod_logs`")  # noqa: E501
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `agent_application_service_pod_logs`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `agent_application_service_pod_logs`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `agent_application_service_pod_logs`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'agent_identifier' in params:
            path_params['agentIdentifier'] = params['agent_identifier']  # noqa: E501
        if 'query_name' in params:
            path_params['query.name'] = params['query_name']  # noqa: E501
        if 'query_pod_name' in params:
            path_params['query.podName'] = params['query_pod_name']  # noqa: E501

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501
        if 'query_namespace' in params:
            query_params.append(('query.namespace', params['query_namespace']))  # noqa: E501
        if 'query_container' in params:
            query_params.append(('query.container', params['query_container']))  # noqa: E501
        if 'query_since_seconds' in params:
            query_params.append(('query.sinceSeconds', params['query_since_seconds']))  # noqa: E501
        if 'query_since_time_seconds' in params:
            query_params.append(('query.sinceTime.seconds', params['query_since_time_seconds']))  # noqa: E501
        if 'query_since_time_nanos' in params:
            query_params.append(('query.sinceTime.nanos', params['query_since_time_nanos']))  # noqa: E501
        if 'query_tail_lines' in params:
            query_params.append(('query.tailLines', params['query_tail_lines']))  # noqa: E501
        if 'query_follow' in params:
            query_params.append(('query.follow', params['query_follow']))  # noqa: E501
        if 'query_until_time' in params:
            query_params.append(('query.untilTime', params['query_until_time']))  # noqa: E501
        if 'query_filter' in params:
            query_params.append(('query.filter', params['query_filter']))  # noqa: E501
        if 'query_kind' in params:
            query_params.append(('query.kind', params['query_kind']))  # noqa: E501
        if 'query_group' in params:
            query_params.append(('query.group', params['query_group']))  # noqa: E501
        if 'query_resource_name' in params:
            query_params.append(('query.resourceName', params['query_resource_name']))  # noqa: E501
        if 'query_previous' in params:
            query_params.append(('query.previous', params['query_previous']))  # noqa: E501

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
            '/gitops/api/v1/agents/{agentIdentifier}/applications/{query.name}/pods/{query.podName}/logs', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StreamResultOfApplicationsLogEntry',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def agent_application_service_pod_logs2(self, agent_identifier, query_name, account_identifier, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """PodLogs returns stream of log entries for the specified pod(s).  # noqa: E501

        PodLogs returns stream of log entries for the specified pod(s).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_application_service_pod_logs2(agent_identifier, query_name, account_identifier, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str query_name: (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str query_namespace:
        :param str query_pod_name:
        :param str query_container:
        :param str query_since_seconds:
        :param str query_since_time_seconds: Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be from 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z inclusive.
        :param int query_since_time_nanos: Non-negative fractions of a second at nanosecond resolution. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be from 0 to 999,999,999 inclusive. This field may be limited in precision depending on context.
        :param str query_tail_lines:
        :param bool query_follow:
        :param str query_until_time:
        :param str query_filter:
        :param str query_kind:
        :param str query_group:
        :param str query_resource_name:
        :param bool query_previous:
        :return: StreamResultOfApplicationsLogEntry
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.agent_application_service_pod_logs2_with_http_info(agent_identifier, query_name, account_identifier, org_identifier, project_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.agent_application_service_pod_logs2_with_http_info(agent_identifier, query_name, account_identifier, org_identifier, project_identifier, **kwargs)  # noqa: E501
            return data

    def agent_application_service_pod_logs2_with_http_info(self, agent_identifier, query_name, account_identifier, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """PodLogs returns stream of log entries for the specified pod(s).  # noqa: E501

        PodLogs returns stream of log entries for the specified pod(s).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_application_service_pod_logs2_with_http_info(agent_identifier, query_name, account_identifier, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str query_name: (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str query_namespace:
        :param str query_pod_name:
        :param str query_container:
        :param str query_since_seconds:
        :param str query_since_time_seconds: Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be from 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z inclusive.
        :param int query_since_time_nanos: Non-negative fractions of a second at nanosecond resolution. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be from 0 to 999,999,999 inclusive. This field may be limited in precision depending on context.
        :param str query_tail_lines:
        :param bool query_follow:
        :param str query_until_time:
        :param str query_filter:
        :param str query_kind:
        :param str query_group:
        :param str query_resource_name:
        :param bool query_previous:
        :return: StreamResultOfApplicationsLogEntry
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['agent_identifier', 'query_name', 'account_identifier', 'org_identifier', 'project_identifier', 'query_namespace', 'query_pod_name', 'query_container', 'query_since_seconds', 'query_since_time_seconds', 'query_since_time_nanos', 'query_tail_lines', 'query_follow', 'query_until_time', 'query_filter', 'query_kind', 'query_group', 'query_resource_name', 'query_previous']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method agent_application_service_pod_logs2" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'agent_identifier' is set
        if ('agent_identifier' not in params or
                params['agent_identifier'] is None):
            raise ValueError("Missing the required parameter `agent_identifier` when calling `agent_application_service_pod_logs2`")  # noqa: E501
        # verify the required parameter 'query_name' is set
        if ('query_name' not in params or
                params['query_name'] is None):
            raise ValueError("Missing the required parameter `query_name` when calling `agent_application_service_pod_logs2`")  # noqa: E501
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `agent_application_service_pod_logs2`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `agent_application_service_pod_logs2`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `agent_application_service_pod_logs2`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'agent_identifier' in params:
            path_params['agentIdentifier'] = params['agent_identifier']  # noqa: E501
        if 'query_name' in params:
            path_params['query.name'] = params['query_name']  # noqa: E501

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501
        if 'query_namespace' in params:
            query_params.append(('query.namespace', params['query_namespace']))  # noqa: E501
        if 'query_pod_name' in params:
            query_params.append(('query.podName', params['query_pod_name']))  # noqa: E501
        if 'query_container' in params:
            query_params.append(('query.container', params['query_container']))  # noqa: E501
        if 'query_since_seconds' in params:
            query_params.append(('query.sinceSeconds', params['query_since_seconds']))  # noqa: E501
        if 'query_since_time_seconds' in params:
            query_params.append(('query.sinceTime.seconds', params['query_since_time_seconds']))  # noqa: E501
        if 'query_since_time_nanos' in params:
            query_params.append(('query.sinceTime.nanos', params['query_since_time_nanos']))  # noqa: E501
        if 'query_tail_lines' in params:
            query_params.append(('query.tailLines', params['query_tail_lines']))  # noqa: E501
        if 'query_follow' in params:
            query_params.append(('query.follow', params['query_follow']))  # noqa: E501
        if 'query_until_time' in params:
            query_params.append(('query.untilTime', params['query_until_time']))  # noqa: E501
        if 'query_filter' in params:
            query_params.append(('query.filter', params['query_filter']))  # noqa: E501
        if 'query_kind' in params:
            query_params.append(('query.kind', params['query_kind']))  # noqa: E501
        if 'query_group' in params:
            query_params.append(('query.group', params['query_group']))  # noqa: E501
        if 'query_resource_name' in params:
            query_params.append(('query.resourceName', params['query_resource_name']))  # noqa: E501
        if 'query_previous' in params:
            query_params.append(('query.previous', params['query_previous']))  # noqa: E501

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
            '/gitops/api/v1/agents/{agentIdentifier}/applications/{query.name}/logs', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StreamResultOfApplicationsLogEntry',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def agent_application_service_resource_tree(self, agent_identifier, query_name, account_identifier, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """ResourceTree returns resource tree  # noqa: E501

        ResourceTree returns resource tree.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_application_service_resource_tree(agent_identifier, query_name, account_identifier, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str query_name: (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str query_application_name:
        :param str query_namespace:
        :param str query_version:
        :param str query_group:
        :param str query_kind:
        :return: ApplicationsApplicationTree
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.agent_application_service_resource_tree_with_http_info(agent_identifier, query_name, account_identifier, org_identifier, project_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.agent_application_service_resource_tree_with_http_info(agent_identifier, query_name, account_identifier, org_identifier, project_identifier, **kwargs)  # noqa: E501
            return data

    def agent_application_service_resource_tree_with_http_info(self, agent_identifier, query_name, account_identifier, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """ResourceTree returns resource tree  # noqa: E501

        ResourceTree returns resource tree.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_application_service_resource_tree_with_http_info(agent_identifier, query_name, account_identifier, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str query_name: (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str query_application_name:
        :param str query_namespace:
        :param str query_version:
        :param str query_group:
        :param str query_kind:
        :return: ApplicationsApplicationTree
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['agent_identifier', 'query_name', 'account_identifier', 'org_identifier', 'project_identifier', 'query_application_name', 'query_namespace', 'query_version', 'query_group', 'query_kind']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method agent_application_service_resource_tree" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'agent_identifier' is set
        if ('agent_identifier' not in params or
                params['agent_identifier'] is None):
            raise ValueError("Missing the required parameter `agent_identifier` when calling `agent_application_service_resource_tree`")  # noqa: E501
        # verify the required parameter 'query_name' is set
        if ('query_name' not in params or
                params['query_name'] is None):
            raise ValueError("Missing the required parameter `query_name` when calling `agent_application_service_resource_tree`")  # noqa: E501
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `agent_application_service_resource_tree`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `agent_application_service_resource_tree`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `agent_application_service_resource_tree`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'agent_identifier' in params:
            path_params['agentIdentifier'] = params['agent_identifier']  # noqa: E501
        if 'query_name' in params:
            path_params['query.name'] = params['query_name']  # noqa: E501

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501
        if 'query_application_name' in params:
            query_params.append(('query.applicationName', params['query_application_name']))  # noqa: E501
        if 'query_namespace' in params:
            query_params.append(('query.namespace', params['query_namespace']))  # noqa: E501
        if 'query_version' in params:
            query_params.append(('query.version', params['query_version']))  # noqa: E501
        if 'query_group' in params:
            query_params.append(('query.group', params['query_group']))  # noqa: E501
        if 'query_kind' in params:
            query_params.append(('query.kind', params['query_kind']))  # noqa: E501

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
            '/gitops/api/v1/agents/{agentIdentifier}/applications/{query.name}/resource-tree', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApplicationsApplicationTree',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def agent_application_service_revision_metadata(self, agent_identifier, query_name, query_revision, account_identifier, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """Get the meta-data (author, date, tags, message) for a specific revision of the application  # noqa: E501

        RevisionMetadata returns metadata for a specific revision of the application.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_application_service_revision_metadata(agent_identifier, query_name, query_revision, account_identifier, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str query_name: the application's name (required)
        :param str query_revision: the revision of the app (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :return: RepositoriesRevisionMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.agent_application_service_revision_metadata_with_http_info(agent_identifier, query_name, query_revision, account_identifier, org_identifier, project_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.agent_application_service_revision_metadata_with_http_info(agent_identifier, query_name, query_revision, account_identifier, org_identifier, project_identifier, **kwargs)  # noqa: E501
            return data

    def agent_application_service_revision_metadata_with_http_info(self, agent_identifier, query_name, query_revision, account_identifier, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """Get the meta-data (author, date, tags, message) for a specific revision of the application  # noqa: E501

        RevisionMetadata returns metadata for a specific revision of the application.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_application_service_revision_metadata_with_http_info(agent_identifier, query_name, query_revision, account_identifier, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str query_name: the application's name (required)
        :param str query_revision: the revision of the app (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :return: RepositoriesRevisionMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['agent_identifier', 'query_name', 'query_revision', 'account_identifier', 'org_identifier', 'project_identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method agent_application_service_revision_metadata" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'agent_identifier' is set
        if ('agent_identifier' not in params or
                params['agent_identifier'] is None):
            raise ValueError("Missing the required parameter `agent_identifier` when calling `agent_application_service_revision_metadata`")  # noqa: E501
        # verify the required parameter 'query_name' is set
        if ('query_name' not in params or
                params['query_name'] is None):
            raise ValueError("Missing the required parameter `query_name` when calling `agent_application_service_revision_metadata`")  # noqa: E501
        # verify the required parameter 'query_revision' is set
        if ('query_revision' not in params or
                params['query_revision'] is None):
            raise ValueError("Missing the required parameter `query_revision` when calling `agent_application_service_revision_metadata`")  # noqa: E501
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `agent_application_service_revision_metadata`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `agent_application_service_revision_metadata`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `agent_application_service_revision_metadata`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'agent_identifier' in params:
            path_params['agentIdentifier'] = params['agent_identifier']  # noqa: E501
        if 'query_name' in params:
            path_params['query.name'] = params['query_name']  # noqa: E501
        if 'query_revision' in params:
            path_params['query.revision'] = params['query_revision']  # noqa: E501

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501
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
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/gitops/api/v1/agents/{agentIdentifier}/applications/{query.name}/revisions/{query.revision}/metadata', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RepositoriesRevisionMetadata',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def agent_application_service_rollback(self, body, account_identifier, org_identifier, project_identifier, agent_identifier, request_name, **kwargs):  # noqa: E501
        """Rollback syncs an application to its target state Harness Event type (rollback)  # noqa: E501

        Rollback syncs an application to its target state Harness Event type (rollback).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_application_service_rollback(body, account_identifier, org_identifier, project_identifier, agent_identifier, request_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ApplicationsApplicationRollbackRequest body: (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str request_name: (required)
        :return: Servicev1Application
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.agent_application_service_rollback_with_http_info(body, account_identifier, org_identifier, project_identifier, agent_identifier, request_name, **kwargs)  # noqa: E501
        else:
            (data) = self.agent_application_service_rollback_with_http_info(body, account_identifier, org_identifier, project_identifier, agent_identifier, request_name, **kwargs)  # noqa: E501
            return data

    def agent_application_service_rollback_with_http_info(self, body, account_identifier, org_identifier, project_identifier, agent_identifier, request_name, **kwargs):  # noqa: E501
        """Rollback syncs an application to its target state Harness Event type (rollback)  # noqa: E501

        Rollback syncs an application to its target state Harness Event type (rollback).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_application_service_rollback_with_http_info(body, account_identifier, org_identifier, project_identifier, agent_identifier, request_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ApplicationsApplicationRollbackRequest body: (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str request_name: (required)
        :return: Servicev1Application
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'account_identifier', 'org_identifier', 'project_identifier', 'agent_identifier', 'request_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method agent_application_service_rollback" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `agent_application_service_rollback`")  # noqa: E501
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `agent_application_service_rollback`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `agent_application_service_rollback`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `agent_application_service_rollback`")  # noqa: E501
        # verify the required parameter 'agent_identifier' is set
        if ('agent_identifier' not in params or
                params['agent_identifier'] is None):
            raise ValueError("Missing the required parameter `agent_identifier` when calling `agent_application_service_rollback`")  # noqa: E501
        # verify the required parameter 'request_name' is set
        if ('request_name' not in params or
                params['request_name'] is None):
            raise ValueError("Missing the required parameter `request_name` when calling `agent_application_service_rollback`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'agent_identifier' in params:
            path_params['agentIdentifier'] = params['agent_identifier']  # noqa: E501
        if 'request_name' in params:
            path_params['request.name'] = params['request_name']  # noqa: E501

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501
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
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/gitops/api/v1/agents/{agentIdentifier}/applications/{request.name}/rollback', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Servicev1Application',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def agent_application_service_run_resource_action(self, body, agent_identifier, request_name, **kwargs):  # noqa: E501
        """RunResourceAction run resource action  # noqa: E501

        RunResourceAction run resource action.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_application_service_run_resource_action(body, agent_identifier, request_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ApplicationsResourceActionRunRequest body: (required)
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str request_name: (required)
        :param str account_identifier: Account Identifier for the Entity.
        :param str org_identifier: Organization Identifier for the Entity.
        :param str project_identifier: Project Identifier for the Entity.
        :return: ApplicationsApplicationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.agent_application_service_run_resource_action_with_http_info(body, agent_identifier, request_name, **kwargs)  # noqa: E501
        else:
            (data) = self.agent_application_service_run_resource_action_with_http_info(body, agent_identifier, request_name, **kwargs)  # noqa: E501
            return data

    def agent_application_service_run_resource_action_with_http_info(self, body, agent_identifier, request_name, **kwargs):  # noqa: E501
        """RunResourceAction run resource action  # noqa: E501

        RunResourceAction run resource action.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_application_service_run_resource_action_with_http_info(body, agent_identifier, request_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ApplicationsResourceActionRunRequest body: (required)
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str request_name: (required)
        :param str account_identifier: Account Identifier for the Entity.
        :param str org_identifier: Organization Identifier for the Entity.
        :param str project_identifier: Project Identifier for the Entity.
        :return: ApplicationsApplicationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'agent_identifier', 'request_name', 'account_identifier', 'org_identifier', 'project_identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method agent_application_service_run_resource_action" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `agent_application_service_run_resource_action`")  # noqa: E501
        # verify the required parameter 'agent_identifier' is set
        if ('agent_identifier' not in params or
                params['agent_identifier'] is None):
            raise ValueError("Missing the required parameter `agent_identifier` when calling `agent_application_service_run_resource_action`")  # noqa: E501
        # verify the required parameter 'request_name' is set
        if ('request_name' not in params or
                params['request_name'] is None):
            raise ValueError("Missing the required parameter `request_name` when calling `agent_application_service_run_resource_action`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'agent_identifier' in params:
            path_params['agentIdentifier'] = params['agent_identifier']  # noqa: E501
        if 'request_name' in params:
            path_params['request.name'] = params['request_name']  # noqa: E501

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501
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
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/gitops/api/v1/agents/{agentIdentifier}/applications/{request.name}/resource/actions', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApplicationsApplicationResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def agent_application_service_sync(self, body, account_identifier, org_identifier, project_identifier, agent_identifier, request_name, **kwargs):  # noqa: E501
        """Sync syncs an application to its target state Harness Event type (deploy)  # noqa: E501

        Delete deletes an application.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_application_service_sync(body, account_identifier, org_identifier, project_identifier, agent_identifier, request_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ApplicationsApplicationSyncRequest body: (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str request_name: (required)
        :return: Servicev1Application
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.agent_application_service_sync_with_http_info(body, account_identifier, org_identifier, project_identifier, agent_identifier, request_name, **kwargs)  # noqa: E501
        else:
            (data) = self.agent_application_service_sync_with_http_info(body, account_identifier, org_identifier, project_identifier, agent_identifier, request_name, **kwargs)  # noqa: E501
            return data

    def agent_application_service_sync_with_http_info(self, body, account_identifier, org_identifier, project_identifier, agent_identifier, request_name, **kwargs):  # noqa: E501
        """Sync syncs an application to its target state Harness Event type (deploy)  # noqa: E501

        Delete deletes an application.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_application_service_sync_with_http_info(body, account_identifier, org_identifier, project_identifier, agent_identifier, request_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ApplicationsApplicationSyncRequest body: (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str request_name: (required)
        :return: Servicev1Application
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'account_identifier', 'org_identifier', 'project_identifier', 'agent_identifier', 'request_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method agent_application_service_sync" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `agent_application_service_sync`")  # noqa: E501
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `agent_application_service_sync`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `agent_application_service_sync`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `agent_application_service_sync`")  # noqa: E501
        # verify the required parameter 'agent_identifier' is set
        if ('agent_identifier' not in params or
                params['agent_identifier'] is None):
            raise ValueError("Missing the required parameter `agent_identifier` when calling `agent_application_service_sync`")  # noqa: E501
        # verify the required parameter 'request_name' is set
        if ('request_name' not in params or
                params['request_name'] is None):
            raise ValueError("Missing the required parameter `request_name` when calling `agent_application_service_sync`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'agent_identifier' in params:
            path_params['agentIdentifier'] = params['agent_identifier']  # noqa: E501
        if 'request_name' in params:
            path_params['request.name'] = params['request_name']  # noqa: E501

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501
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
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/gitops/api/v1/agents/{agentIdentifier}/applications/{request.name}/sync', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Servicev1Application',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def agent_application_service_terminate_operation(self, agent_identifier, request_name, account_identifier, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """TerminateOperation terminates the currently running operation  # noqa: E501

        TerminateOperation terminates the currently running operation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_application_service_terminate_operation(agent_identifier, request_name, account_identifier, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str request_name: (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :return: ApplicationsOperationTerminateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.agent_application_service_terminate_operation_with_http_info(agent_identifier, request_name, account_identifier, org_identifier, project_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.agent_application_service_terminate_operation_with_http_info(agent_identifier, request_name, account_identifier, org_identifier, project_identifier, **kwargs)  # noqa: E501
            return data

    def agent_application_service_terminate_operation_with_http_info(self, agent_identifier, request_name, account_identifier, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """TerminateOperation terminates the currently running operation  # noqa: E501

        TerminateOperation terminates the currently running operation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_application_service_terminate_operation_with_http_info(agent_identifier, request_name, account_identifier, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str request_name: (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :return: ApplicationsOperationTerminateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['agent_identifier', 'request_name', 'account_identifier', 'org_identifier', 'project_identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method agent_application_service_terminate_operation" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'agent_identifier' is set
        if ('agent_identifier' not in params or
                params['agent_identifier'] is None):
            raise ValueError("Missing the required parameter `agent_identifier` when calling `agent_application_service_terminate_operation`")  # noqa: E501
        # verify the required parameter 'request_name' is set
        if ('request_name' not in params or
                params['request_name'] is None):
            raise ValueError("Missing the required parameter `request_name` when calling `agent_application_service_terminate_operation`")  # noqa: E501
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `agent_application_service_terminate_operation`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `agent_application_service_terminate_operation`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `agent_application_service_terminate_operation`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'agent_identifier' in params:
            path_params['agentIdentifier'] = params['agent_identifier']  # noqa: E501
        if 'request_name' in params:
            path_params['request.name'] = params['request_name']  # noqa: E501

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501
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
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/gitops/api/v1/agents/{agentIdentifier}/applications/{request.name}/operation', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApplicationsOperationTerminateResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def agent_application_service_update(self, body, account_identifier, org_identifier, project_identifier, agent_identifier, request_application_metadata_name, **kwargs):  # noqa: E501
        """Update updates an application  # noqa: E501

        Update updates an application.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_application_service_update(body, account_identifier, org_identifier, project_identifier, agent_identifier, request_application_metadata_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ApplicationsApplicationUpdateRequest body: (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str request_application_metadata_name: Name must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names +optional (required)
        :param str cluster_identifier:
        :param str repo_identifier:
        :return: Servicev1Application
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.agent_application_service_update_with_http_info(body, account_identifier, org_identifier, project_identifier, agent_identifier, request_application_metadata_name, **kwargs)  # noqa: E501
        else:
            (data) = self.agent_application_service_update_with_http_info(body, account_identifier, org_identifier, project_identifier, agent_identifier, request_application_metadata_name, **kwargs)  # noqa: E501
            return data

    def agent_application_service_update_with_http_info(self, body, account_identifier, org_identifier, project_identifier, agent_identifier, request_application_metadata_name, **kwargs):  # noqa: E501
        """Update updates an application  # noqa: E501

        Update updates an application.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_application_service_update_with_http_info(body, account_identifier, org_identifier, project_identifier, agent_identifier, request_application_metadata_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ApplicationsApplicationUpdateRequest body: (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str request_application_metadata_name: Name must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names +optional (required)
        :param str cluster_identifier:
        :param str repo_identifier:
        :return: Servicev1Application
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'account_identifier', 'org_identifier', 'project_identifier', 'agent_identifier', 'request_application_metadata_name', 'cluster_identifier', 'repo_identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method agent_application_service_update" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `agent_application_service_update`")  # noqa: E501
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `agent_application_service_update`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `agent_application_service_update`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `agent_application_service_update`")  # noqa: E501
        # verify the required parameter 'agent_identifier' is set
        if ('agent_identifier' not in params or
                params['agent_identifier'] is None):
            raise ValueError("Missing the required parameter `agent_identifier` when calling `agent_application_service_update`")  # noqa: E501
        # verify the required parameter 'request_application_metadata_name' is set
        if ('request_application_metadata_name' not in params or
                params['request_application_metadata_name'] is None):
            raise ValueError("Missing the required parameter `request_application_metadata_name` when calling `agent_application_service_update`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'agent_identifier' in params:
            path_params['agentIdentifier'] = params['agent_identifier']  # noqa: E501
        if 'request_application_metadata_name' in params:
            path_params['request.application.metadata.name'] = params['request_application_metadata_name']  # noqa: E501

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501
        if 'cluster_identifier' in params:
            query_params.append(('clusterIdentifier', params['cluster_identifier']))  # noqa: E501
        if 'repo_identifier' in params:
            query_params.append(('repoIdentifier', params['repo_identifier']))  # noqa: E501

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
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/gitops/api/v1/agents/{agentIdentifier}/applications/{request.application.metadata.name}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Servicev1Application',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def agent_application_service_update_spec(self, body, account_identifier, org_identifier, project_identifier, agent_identifier, request_name, **kwargs):  # noqa: E501
        """UpdateSpec updates an application spec  # noqa: E501

        UpdateSpec updates an application spec.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_application_service_update_spec(body, account_identifier, org_identifier, project_identifier, agent_identifier, request_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ApplicationsApplicationUpdateSpecRequest body: (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str request_name: (required)
        :return: ApplicationsApplicationSpec
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.agent_application_service_update_spec_with_http_info(body, account_identifier, org_identifier, project_identifier, agent_identifier, request_name, **kwargs)  # noqa: E501
        else:
            (data) = self.agent_application_service_update_spec_with_http_info(body, account_identifier, org_identifier, project_identifier, agent_identifier, request_name, **kwargs)  # noqa: E501
            return data

    def agent_application_service_update_spec_with_http_info(self, body, account_identifier, org_identifier, project_identifier, agent_identifier, request_name, **kwargs):  # noqa: E501
        """UpdateSpec updates an application spec  # noqa: E501

        UpdateSpec updates an application spec.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_application_service_update_spec_with_http_info(body, account_identifier, org_identifier, project_identifier, agent_identifier, request_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ApplicationsApplicationUpdateSpecRequest body: (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str request_name: (required)
        :return: ApplicationsApplicationSpec
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'account_identifier', 'org_identifier', 'project_identifier', 'agent_identifier', 'request_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method agent_application_service_update_spec" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `agent_application_service_update_spec`")  # noqa: E501
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `agent_application_service_update_spec`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `agent_application_service_update_spec`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `agent_application_service_update_spec`")  # noqa: E501
        # verify the required parameter 'agent_identifier' is set
        if ('agent_identifier' not in params or
                params['agent_identifier'] is None):
            raise ValueError("Missing the required parameter `agent_identifier` when calling `agent_application_service_update_spec`")  # noqa: E501
        # verify the required parameter 'request_name' is set
        if ('request_name' not in params or
                params['request_name'] is None):
            raise ValueError("Missing the required parameter `request_name` when calling `agent_application_service_update_spec`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'agent_identifier' in params:
            path_params['agentIdentifier'] = params['agent_identifier']  # noqa: E501
        if 'request_name' in params:
            path_params['request.name'] = params['request_name']  # noqa: E501

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501
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
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/gitops/api/v1/agents/{agentIdentifier}/applications/{request.name}/spec', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApplicationsApplicationSpec',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def agent_application_service_watch(self, agent_identifier, account_identifier, org_identifier, project_identifier, query_name, **kwargs):  # noqa: E501
        """Watch returns stream of application change events  # noqa: E501

        Watch returns stream of application change events.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_application_service_watch(agent_identifier, account_identifier, org_identifier, project_identifier, query_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str query_name: the application's name. (required)
        :param str query_refresh: forces application reconciliation if set to true.
        :param list[str] query_project: the project names to restrict returned list applications.
        :param str query_resource_version: when specified with a watch call, shows changes that occur after that particular version of a resource.
        :param str query_selector: the selector to to restrict returned list to applications only with matched labels.
        :param str query_repo: the repoURL to restrict returned list applications.
        :return: StreamResultOfApplicationsApplicationWatchEvent
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.agent_application_service_watch_with_http_info(agent_identifier, account_identifier, org_identifier, project_identifier, query_name, **kwargs)  # noqa: E501
        else:
            (data) = self.agent_application_service_watch_with_http_info(agent_identifier, account_identifier, org_identifier, project_identifier, query_name, **kwargs)  # noqa: E501
            return data

    def agent_application_service_watch_with_http_info(self, agent_identifier, account_identifier, org_identifier, project_identifier, query_name, **kwargs):  # noqa: E501
        """Watch returns stream of application change events  # noqa: E501

        Watch returns stream of application change events.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_application_service_watch_with_http_info(agent_identifier, account_identifier, org_identifier, project_identifier, query_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str query_name: the application's name. (required)
        :param str query_refresh: forces application reconciliation if set to true.
        :param list[str] query_project: the project names to restrict returned list applications.
        :param str query_resource_version: when specified with a watch call, shows changes that occur after that particular version of a resource.
        :param str query_selector: the selector to to restrict returned list to applications only with matched labels.
        :param str query_repo: the repoURL to restrict returned list applications.
        :return: StreamResultOfApplicationsApplicationWatchEvent
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['agent_identifier', 'account_identifier', 'org_identifier', 'project_identifier', 'query_name', 'query_refresh', 'query_project', 'query_resource_version', 'query_selector', 'query_repo']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method agent_application_service_watch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'agent_identifier' is set
        if ('agent_identifier' not in params or
                params['agent_identifier'] is None):
            raise ValueError("Missing the required parameter `agent_identifier` when calling `agent_application_service_watch`")  # noqa: E501
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `agent_application_service_watch`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `agent_application_service_watch`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `agent_application_service_watch`")  # noqa: E501
        # verify the required parameter 'query_name' is set
        if ('query_name' not in params or
                params['query_name'] is None):
            raise ValueError("Missing the required parameter `query_name` when calling `agent_application_service_watch`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'agent_identifier' in params:
            path_params['agentIdentifier'] = params['agent_identifier']  # noqa: E501

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501
        if 'query_name' in params:
            query_params.append(('query.name', params['query_name']))  # noqa: E501
        if 'query_refresh' in params:
            query_params.append(('query.refresh', params['query_refresh']))  # noqa: E501
        if 'query_project' in params:
            query_params.append(('query.project', params['query_project']))  # noqa: E501
            collection_formats['query.project'] = 'multi'  # noqa: E501
        if 'query_resource_version' in params:
            query_params.append(('query.resourceVersion', params['query_resource_version']))  # noqa: E501
        if 'query_selector' in params:
            query_params.append(('query.selector', params['query_selector']))  # noqa: E501
        if 'query_repo' in params:
            query_params.append(('query.repo', params['query_repo']))  # noqa: E501

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
            '/gitops/api/v1/agents/{agentIdentifier}/stream/applications', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StreamResultOfApplicationsApplicationWatchEvent',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def agent_application_service_watch_resource_tree(self, agent_identifier, query_application_name, account_identifier, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """WatchResourceTree returns stream of application resource tree  # noqa: E501

        WatchResourceTree returns stream of application resource tree.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_application_service_watch_resource_tree(agent_identifier, query_application_name, account_identifier, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str query_application_name: (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str query_namespace:
        :param str query_name:
        :param str query_version:
        :param str query_group:
        :param str query_kind:
        :return: StreamResultOfApplicationsApplicationTree
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.agent_application_service_watch_resource_tree_with_http_info(agent_identifier, query_application_name, account_identifier, org_identifier, project_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.agent_application_service_watch_resource_tree_with_http_info(agent_identifier, query_application_name, account_identifier, org_identifier, project_identifier, **kwargs)  # noqa: E501
            return data

    def agent_application_service_watch_resource_tree_with_http_info(self, agent_identifier, query_application_name, account_identifier, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """WatchResourceTree returns stream of application resource tree  # noqa: E501

        WatchResourceTree returns stream of application resource tree.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_application_service_watch_resource_tree_with_http_info(agent_identifier, query_application_name, account_identifier, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str query_application_name: (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str query_namespace:
        :param str query_name:
        :param str query_version:
        :param str query_group:
        :param str query_kind:
        :return: StreamResultOfApplicationsApplicationTree
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['agent_identifier', 'query_application_name', 'account_identifier', 'org_identifier', 'project_identifier', 'query_namespace', 'query_name', 'query_version', 'query_group', 'query_kind']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method agent_application_service_watch_resource_tree" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'agent_identifier' is set
        if ('agent_identifier' not in params or
                params['agent_identifier'] is None):
            raise ValueError("Missing the required parameter `agent_identifier` when calling `agent_application_service_watch_resource_tree`")  # noqa: E501
        # verify the required parameter 'query_application_name' is set
        if ('query_application_name' not in params or
                params['query_application_name'] is None):
            raise ValueError("Missing the required parameter `query_application_name` when calling `agent_application_service_watch_resource_tree`")  # noqa: E501
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `agent_application_service_watch_resource_tree`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `agent_application_service_watch_resource_tree`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `agent_application_service_watch_resource_tree`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'agent_identifier' in params:
            path_params['agentIdentifier'] = params['agent_identifier']  # noqa: E501
        if 'query_application_name' in params:
            path_params['query.applicationName'] = params['query_application_name']  # noqa: E501

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501
        if 'query_namespace' in params:
            query_params.append(('query.namespace', params['query_namespace']))  # noqa: E501
        if 'query_name' in params:
            query_params.append(('query.name', params['query_name']))  # noqa: E501
        if 'query_version' in params:
            query_params.append(('query.version', params['query_version']))  # noqa: E501
        if 'query_group' in params:
            query_params.append(('query.group', params['query_group']))  # noqa: E501
        if 'query_kind' in params:
            query_params.append(('query.kind', params['query_kind']))  # noqa: E501

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
            '/gitops/api/v1/agents/{agentIdentifier}/stream/applications/{query.applicationName}/resource-tree', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StreamResultOfApplicationsApplicationTree',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def application_service_exists(self, name, account_identifier, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """Checks whether an app with the given name exists  # noqa: E501

        Checks whether an app with the given name exists  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.application_service_exists(name, account_identifier, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str agent_identifier: Agent identifier for entity.
        :return: bool
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.application_service_exists_with_http_info(name, account_identifier, org_identifier, project_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.application_service_exists_with_http_info(name, account_identifier, org_identifier, project_identifier, **kwargs)  # noqa: E501
            return data

    def application_service_exists_with_http_info(self, name, account_identifier, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """Checks whether an app with the given name exists  # noqa: E501

        Checks whether an app with the given name exists  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.application_service_exists_with_http_info(name, account_identifier, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str agent_identifier: Agent identifier for entity.
        :return: bool
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'account_identifier', 'org_identifier', 'project_identifier', 'agent_identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method application_service_exists" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `application_service_exists`")  # noqa: E501
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `application_service_exists`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `application_service_exists`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `application_service_exists`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501
        if 'agent_identifier' in params:
            query_params.append(('agentIdentifier', params['agent_identifier']))  # noqa: E501

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
            '/gitops/api/v1/applications/{name}/exists', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='bool',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def application_service_list_app_sync(self, body, **kwargs):  # noqa: E501
        """List returns list of application sync status  # noqa: E501

        List returns list of application sync status  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.application_service_list_app_sync(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V1ApplicationSyncStatusQuery body: (required)
        :return: V1ApplicationSyncStatuslist
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.application_service_list_app_sync_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.application_service_list_app_sync_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def application_service_list_app_sync_with_http_info(self, body, **kwargs):  # noqa: E501
        """List returns list of application sync status  # noqa: E501

        List returns list of application sync status  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.application_service_list_app_sync_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V1ApplicationSyncStatusQuery body: (required)
        :return: V1ApplicationSyncStatuslist
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method application_service_list_app_sync" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `application_service_list_app_sync`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

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
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/gitops/api/v1/applications/sync', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1ApplicationSyncStatuslist',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
