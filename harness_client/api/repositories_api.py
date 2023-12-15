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


class RepositoriesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def agent_repository_service_create_repository(self, body, agent_identifier, **kwargs):  # noqa: E501
        """CreateRepository creates a new repository configuration  # noqa: E501

        CreateRepository creates a new repository configuration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_repository_service_create_repository(body, agent_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RepositoriesRepoCreateRequest body: (required)
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str account_identifier: Account Identifier for the Entity.
        :param str org_identifier: Organization Identifier for the Entity.
        :param str project_identifier: Project Identifier for the Entity.
        :param str identifier:
        :param str repo_creds_id:
        :return: Servicev1Repository
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.agent_repository_service_create_repository_with_http_info(body, agent_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.agent_repository_service_create_repository_with_http_info(body, agent_identifier, **kwargs)  # noqa: E501
            return data

    def agent_repository_service_create_repository_with_http_info(self, body, agent_identifier, **kwargs):  # noqa: E501
        """CreateRepository creates a new repository configuration  # noqa: E501

        CreateRepository creates a new repository configuration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_repository_service_create_repository_with_http_info(body, agent_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RepositoriesRepoCreateRequest body: (required)
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str account_identifier: Account Identifier for the Entity.
        :param str org_identifier: Organization Identifier for the Entity.
        :param str project_identifier: Project Identifier for the Entity.
        :param str identifier:
        :param str repo_creds_id:
        :return: Servicev1Repository
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'agent_identifier', 'account_identifier', 'org_identifier', 'project_identifier', 'identifier', 'repo_creds_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method agent_repository_service_create_repository" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `agent_repository_service_create_repository`")  # noqa: E501
        # verify the required parameter 'agent_identifier' is set
        if ('agent_identifier' not in params or
                params['agent_identifier'] is None):
            raise ValueError("Missing the required parameter `agent_identifier` when calling `agent_repository_service_create_repository`")  # noqa: E501

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
        if 'identifier' in params:
            query_params.append(('identifier', params['identifier']))  # noqa: E501
        if 'repo_creds_id' in params:
            query_params.append(('repoCredsId', params['repo_creds_id']))  # noqa: E501

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
            '/gitops/api/v1/agents/{agentIdentifier}/repositories', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Servicev1Repository',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def agent_repository_service_delete_repository(self, agent_identifier, identifier, **kwargs):  # noqa: E501
        """DeleteRepository deletes a repository from the configuration  # noqa: E501

        DeleteRepository deletes a repository from the configuration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_repository_service_delete_repository(agent_identifier, identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str identifier: (required)
        :param str account_identifier: Account Identifier for the Entity.
        :param str org_identifier: Organization Identifier for the Entity.
        :param str project_identifier: Project Identifier for the Entity.
        :param str query_repo: Repo URL for query.
        :param bool query_force_refresh: Whether to force a cache refresh on repo's connection state.
        :param str query_project: The associated project project.
        :return: RepositoriesRepoResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.agent_repository_service_delete_repository_with_http_info(agent_identifier, identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.agent_repository_service_delete_repository_with_http_info(agent_identifier, identifier, **kwargs)  # noqa: E501
            return data

    def agent_repository_service_delete_repository_with_http_info(self, agent_identifier, identifier, **kwargs):  # noqa: E501
        """DeleteRepository deletes a repository from the configuration  # noqa: E501

        DeleteRepository deletes a repository from the configuration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_repository_service_delete_repository_with_http_info(agent_identifier, identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str identifier: (required)
        :param str account_identifier: Account Identifier for the Entity.
        :param str org_identifier: Organization Identifier for the Entity.
        :param str project_identifier: Project Identifier for the Entity.
        :param str query_repo: Repo URL for query.
        :param bool query_force_refresh: Whether to force a cache refresh on repo's connection state.
        :param str query_project: The associated project project.
        :return: RepositoriesRepoResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['agent_identifier', 'identifier', 'account_identifier', 'org_identifier', 'project_identifier', 'query_repo', 'query_force_refresh', 'query_project']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method agent_repository_service_delete_repository" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'agent_identifier' is set
        if ('agent_identifier' not in params or
                params['agent_identifier'] is None):
            raise ValueError("Missing the required parameter `agent_identifier` when calling `agent_repository_service_delete_repository`")  # noqa: E501
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `agent_repository_service_delete_repository`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'agent_identifier' in params:
            path_params['agentIdentifier'] = params['agent_identifier']  # noqa: E501
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501
        if 'query_repo' in params:
            query_params.append(('query.repo', params['query_repo']))  # noqa: E501
        if 'query_force_refresh' in params:
            query_params.append(('query.forceRefresh', params['query_force_refresh']))  # noqa: E501
        if 'query_project' in params:
            query_params.append(('query.project', params['query_project']))  # noqa: E501

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
            '/gitops/api/v1/agents/{agentIdentifier}/repositories/{identifier}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RepositoriesRepoResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def agent_repository_service_get(self, agent_identifier, identifier, account_identifier, **kwargs):  # noqa: E501
        """Get returns a repository or its credentials  # noqa: E501

        Get returns a repository or its credentials.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_repository_service_get(agent_identifier, identifier, account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str identifier: (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity.
        :param str project_identifier: Project Identifier for the Entity.
        :param str query_repo: Repo URL for query.
        :param bool query_force_refresh: Whether to force a cache refresh on repo's connection state.
        :param str query_project: The associated project project.
        :return: Servicev1Repository
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.agent_repository_service_get_with_http_info(agent_identifier, identifier, account_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.agent_repository_service_get_with_http_info(agent_identifier, identifier, account_identifier, **kwargs)  # noqa: E501
            return data

    def agent_repository_service_get_with_http_info(self, agent_identifier, identifier, account_identifier, **kwargs):  # noqa: E501
        """Get returns a repository or its credentials  # noqa: E501

        Get returns a repository or its credentials.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_repository_service_get_with_http_info(agent_identifier, identifier, account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str identifier: (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity.
        :param str project_identifier: Project Identifier for the Entity.
        :param str query_repo: Repo URL for query.
        :param bool query_force_refresh: Whether to force a cache refresh on repo's connection state.
        :param str query_project: The associated project project.
        :return: Servicev1Repository
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['agent_identifier', 'identifier', 'account_identifier', 'org_identifier', 'project_identifier', 'query_repo', 'query_force_refresh', 'query_project']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method agent_repository_service_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'agent_identifier' is set
        if ('agent_identifier' not in params or
                params['agent_identifier'] is None):
            raise ValueError("Missing the required parameter `agent_identifier` when calling `agent_repository_service_get`")  # noqa: E501
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `agent_repository_service_get`")  # noqa: E501
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `agent_repository_service_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'agent_identifier' in params:
            path_params['agentIdentifier'] = params['agent_identifier']  # noqa: E501
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501
        if 'query_repo' in params:
            query_params.append(('query.repo', params['query_repo']))  # noqa: E501
        if 'query_force_refresh' in params:
            query_params.append(('query.forceRefresh', params['query_force_refresh']))  # noqa: E501
        if 'query_project' in params:
            query_params.append(('query.project', params['query_project']))  # noqa: E501

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
            '/gitops/api/v1/agents/{agentIdentifier}/repositories/{identifier}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Servicev1Repository',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def agent_repository_service_get_app_details(self, agent_identifier, identifier, account_identifier, **kwargs):  # noqa: E501
        """GetAppDetails returns application details by given path  # noqa: E501

        GetAppDetails returns application details by given path.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_repository_service_get_app_details(agent_identifier, identifier, account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str identifier: (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity.
        :param str project_identifier: Project Identifier for the Entity.
        :param str query_source_repo_url: RepoURL is the URL to the repository (Git or Helm) that contains the application manifests.
        :param str query_source_path: Path is a directory path within the Git repository, and is only valid for applications sourced from Git.
        :param str query_source_target_revision: TargetRevision defines the revision of the source to sync the application to. In case of Git, this can be commit, tag, or branch. If omitted, will equal to HEAD. In case of Helm, this is a semver tag for the Chart's version.
        :param list[str] query_source_helm_value_files: ValuesFiles is a list of Helm value files to use when generating a template.
        :param str query_source_helm_release_name: ReleaseName is the Helm release name to use. If omitted it will use the application name.
        :param str query_source_helm_values: Values specifies Helm values to be passed to helm template, typically defined as a block.
        :param str query_source_helm_version: Version is the Helm version to use for templating (either \"2\" or \"3\").
        :param bool query_source_helm_pass_credentials: PassCredentials pass credentials to all domains (Helm's --pass-credentials).
        :param str query_source_kustomize_name_prefix: NamePrefix is a prefix appended to resources for Kustomize apps.
        :param str query_source_kustomize_name_suffix: NameSuffix is a suffix appended to resources for Kustomize apps.
        :param list[str] query_source_kustomize_images: Images is a list of Kustomize image override specifications.
        :param str query_source_kustomize_version: Version controls which version of Kustomize to use for rendering manifests.
        :param bool query_source_kustomize_force_common_labels: ForceCommonLabels specifies whether to force applying common labels to resources for Kustomize apps.
        :param bool query_source_kustomize_force_common_annotations: ForceCommonAnnotations specifies whether to force applying common annotations to resources for Kustomize apps.
        :param str query_source_ksonnet_environment: Environment is a ksonnet application environment name.
        :param bool query_source_directory_recurse: Recurse specifies whether to scan a directory recursively for manifests.
        :param list[str] query_source_directory_jsonnet_libs: Additional library search dirs.
        :param str query_source_directory_exclude: Exclude contains a glob pattern to match paths against that should be explicitly excluded from being used during manifest generation.
        :param str query_source_directory_include: Include contains a glob pattern to match paths against that should be explicitly included during manifest generation.
        :param str query_source_plugin_name:
        :param str query_source_chart: Chart is a Helm chart name, and must be specified for applications sourced from a Helm repo.
        :param str query_app_name:
        :param str query_app_project:
        :return: RepositoriesRepoAppDetailsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.agent_repository_service_get_app_details_with_http_info(agent_identifier, identifier, account_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.agent_repository_service_get_app_details_with_http_info(agent_identifier, identifier, account_identifier, **kwargs)  # noqa: E501
            return data

    def agent_repository_service_get_app_details_with_http_info(self, agent_identifier, identifier, account_identifier, **kwargs):  # noqa: E501
        """GetAppDetails returns application details by given path  # noqa: E501

        GetAppDetails returns application details by given path.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_repository_service_get_app_details_with_http_info(agent_identifier, identifier, account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str identifier: (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity.
        :param str project_identifier: Project Identifier for the Entity.
        :param str query_source_repo_url: RepoURL is the URL to the repository (Git or Helm) that contains the application manifests.
        :param str query_source_path: Path is a directory path within the Git repository, and is only valid for applications sourced from Git.
        :param str query_source_target_revision: TargetRevision defines the revision of the source to sync the application to. In case of Git, this can be commit, tag, or branch. If omitted, will equal to HEAD. In case of Helm, this is a semver tag for the Chart's version.
        :param list[str] query_source_helm_value_files: ValuesFiles is a list of Helm value files to use when generating a template.
        :param str query_source_helm_release_name: ReleaseName is the Helm release name to use. If omitted it will use the application name.
        :param str query_source_helm_values: Values specifies Helm values to be passed to helm template, typically defined as a block.
        :param str query_source_helm_version: Version is the Helm version to use for templating (either \"2\" or \"3\").
        :param bool query_source_helm_pass_credentials: PassCredentials pass credentials to all domains (Helm's --pass-credentials).
        :param str query_source_kustomize_name_prefix: NamePrefix is a prefix appended to resources for Kustomize apps.
        :param str query_source_kustomize_name_suffix: NameSuffix is a suffix appended to resources for Kustomize apps.
        :param list[str] query_source_kustomize_images: Images is a list of Kustomize image override specifications.
        :param str query_source_kustomize_version: Version controls which version of Kustomize to use for rendering manifests.
        :param bool query_source_kustomize_force_common_labels: ForceCommonLabels specifies whether to force applying common labels to resources for Kustomize apps.
        :param bool query_source_kustomize_force_common_annotations: ForceCommonAnnotations specifies whether to force applying common annotations to resources for Kustomize apps.
        :param str query_source_ksonnet_environment: Environment is a ksonnet application environment name.
        :param bool query_source_directory_recurse: Recurse specifies whether to scan a directory recursively for manifests.
        :param list[str] query_source_directory_jsonnet_libs: Additional library search dirs.
        :param str query_source_directory_exclude: Exclude contains a glob pattern to match paths against that should be explicitly excluded from being used during manifest generation.
        :param str query_source_directory_include: Include contains a glob pattern to match paths against that should be explicitly included during manifest generation.
        :param str query_source_plugin_name:
        :param str query_source_chart: Chart is a Helm chart name, and must be specified for applications sourced from a Helm repo.
        :param str query_app_name:
        :param str query_app_project:
        :return: RepositoriesRepoAppDetailsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['agent_identifier', 'identifier', 'account_identifier', 'org_identifier', 'project_identifier', 'query_source_repo_url', 'query_source_path', 'query_source_target_revision', 'query_source_helm_value_files', 'query_source_helm_release_name', 'query_source_helm_values', 'query_source_helm_version', 'query_source_helm_pass_credentials', 'query_source_kustomize_name_prefix', 'query_source_kustomize_name_suffix', 'query_source_kustomize_images', 'query_source_kustomize_version', 'query_source_kustomize_force_common_labels', 'query_source_kustomize_force_common_annotations', 'query_source_ksonnet_environment', 'query_source_directory_recurse', 'query_source_directory_jsonnet_libs', 'query_source_directory_exclude', 'query_source_directory_include', 'query_source_plugin_name', 'query_source_chart', 'query_app_name', 'query_app_project']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method agent_repository_service_get_app_details" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'agent_identifier' is set
        if ('agent_identifier' not in params or
                params['agent_identifier'] is None):
            raise ValueError("Missing the required parameter `agent_identifier` when calling `agent_repository_service_get_app_details`")  # noqa: E501
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `agent_repository_service_get_app_details`")  # noqa: E501
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `agent_repository_service_get_app_details`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'agent_identifier' in params:
            path_params['agentIdentifier'] = params['agent_identifier']  # noqa: E501
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501
        if 'query_source_repo_url' in params:
            query_params.append(('query.source.repoURL', params['query_source_repo_url']))  # noqa: E501
        if 'query_source_path' in params:
            query_params.append(('query.source.path', params['query_source_path']))  # noqa: E501
        if 'query_source_target_revision' in params:
            query_params.append(('query.source.targetRevision', params['query_source_target_revision']))  # noqa: E501
        if 'query_source_helm_value_files' in params:
            query_params.append(('query.source.helm.valueFiles', params['query_source_helm_value_files']))  # noqa: E501
            collection_formats['query.source.helm.valueFiles'] = 'multi'  # noqa: E501
        if 'query_source_helm_release_name' in params:
            query_params.append(('query.source.helm.releaseName', params['query_source_helm_release_name']))  # noqa: E501
        if 'query_source_helm_values' in params:
            query_params.append(('query.source.helm.values', params['query_source_helm_values']))  # noqa: E501
        if 'query_source_helm_version' in params:
            query_params.append(('query.source.helm.version', params['query_source_helm_version']))  # noqa: E501
        if 'query_source_helm_pass_credentials' in params:
            query_params.append(('query.source.helm.passCredentials', params['query_source_helm_pass_credentials']))  # noqa: E501
        if 'query_source_kustomize_name_prefix' in params:
            query_params.append(('query.source.kustomize.namePrefix', params['query_source_kustomize_name_prefix']))  # noqa: E501
        if 'query_source_kustomize_name_suffix' in params:
            query_params.append(('query.source.kustomize.nameSuffix', params['query_source_kustomize_name_suffix']))  # noqa: E501
        if 'query_source_kustomize_images' in params:
            query_params.append(('query.source.kustomize.images', params['query_source_kustomize_images']))  # noqa: E501
            collection_formats['query.source.kustomize.images'] = 'multi'  # noqa: E501
        if 'query_source_kustomize_version' in params:
            query_params.append(('query.source.kustomize.version', params['query_source_kustomize_version']))  # noqa: E501
        if 'query_source_kustomize_force_common_labels' in params:
            query_params.append(('query.source.kustomize.forceCommonLabels', params['query_source_kustomize_force_common_labels']))  # noqa: E501
        if 'query_source_kustomize_force_common_annotations' in params:
            query_params.append(('query.source.kustomize.forceCommonAnnotations', params['query_source_kustomize_force_common_annotations']))  # noqa: E501
        if 'query_source_ksonnet_environment' in params:
            query_params.append(('query.source.ksonnet.environment', params['query_source_ksonnet_environment']))  # noqa: E501
        if 'query_source_directory_recurse' in params:
            query_params.append(('query.source.directory.recurse', params['query_source_directory_recurse']))  # noqa: E501
        if 'query_source_directory_jsonnet_libs' in params:
            query_params.append(('query.source.directory.jsonnet.libs', params['query_source_directory_jsonnet_libs']))  # noqa: E501
            collection_formats['query.source.directory.jsonnet.libs'] = 'multi'  # noqa: E501
        if 'query_source_directory_exclude' in params:
            query_params.append(('query.source.directory.exclude', params['query_source_directory_exclude']))  # noqa: E501
        if 'query_source_directory_include' in params:
            query_params.append(('query.source.directory.include', params['query_source_directory_include']))  # noqa: E501
        if 'query_source_plugin_name' in params:
            query_params.append(('query.source.plugin.name', params['query_source_plugin_name']))  # noqa: E501
        if 'query_source_chart' in params:
            query_params.append(('query.source.chart', params['query_source_chart']))  # noqa: E501
        if 'query_app_name' in params:
            query_params.append(('query.appName', params['query_app_name']))  # noqa: E501
        if 'query_app_project' in params:
            query_params.append(('query.appProject', params['query_app_project']))  # noqa: E501

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
            '/gitops/api/v1/agents/{agentIdentifier}/repositories/{identifier}/appdetails', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RepositoriesRepoAppDetailsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def agent_repository_service_get_helm_charts(self, agent_identifier, identifier, account_identifier, **kwargs):  # noqa: E501
        """GetHelmCharts returns list of helm charts in the specified repository  # noqa: E501

        GetHelmCharts returns list of helm charts in the specified repository.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_repository_service_get_helm_charts(agent_identifier, identifier, account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str identifier: (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity.
        :param str project_identifier: Project Identifier for the Entity.
        :param str query_repo: Repo URL for query.
        :param bool query_force_refresh: Whether to force a cache refresh on repo's connection state.
        :param str query_project: The associated project project.
        :return: RepositoriesHelmChartsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.agent_repository_service_get_helm_charts_with_http_info(agent_identifier, identifier, account_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.agent_repository_service_get_helm_charts_with_http_info(agent_identifier, identifier, account_identifier, **kwargs)  # noqa: E501
            return data

    def agent_repository_service_get_helm_charts_with_http_info(self, agent_identifier, identifier, account_identifier, **kwargs):  # noqa: E501
        """GetHelmCharts returns list of helm charts in the specified repository  # noqa: E501

        GetHelmCharts returns list of helm charts in the specified repository.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_repository_service_get_helm_charts_with_http_info(agent_identifier, identifier, account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str identifier: (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity.
        :param str project_identifier: Project Identifier for the Entity.
        :param str query_repo: Repo URL for query.
        :param bool query_force_refresh: Whether to force a cache refresh on repo's connection state.
        :param str query_project: The associated project project.
        :return: RepositoriesHelmChartsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['agent_identifier', 'identifier', 'account_identifier', 'org_identifier', 'project_identifier', 'query_repo', 'query_force_refresh', 'query_project']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method agent_repository_service_get_helm_charts" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'agent_identifier' is set
        if ('agent_identifier' not in params or
                params['agent_identifier'] is None):
            raise ValueError("Missing the required parameter `agent_identifier` when calling `agent_repository_service_get_helm_charts`")  # noqa: E501
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `agent_repository_service_get_helm_charts`")  # noqa: E501
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `agent_repository_service_get_helm_charts`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'agent_identifier' in params:
            path_params['agentIdentifier'] = params['agent_identifier']  # noqa: E501
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501
        if 'query_repo' in params:
            query_params.append(('query.repo', params['query_repo']))  # noqa: E501
        if 'query_force_refresh' in params:
            query_params.append(('query.forceRefresh', params['query_force_refresh']))  # noqa: E501
        if 'query_project' in params:
            query_params.append(('query.project', params['query_project']))  # noqa: E501

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
            '/gitops/api/v1/agents/{agentIdentifier}/repositories/{identifier}/helmcharts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RepositoriesHelmChartsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def agent_repository_service_list_apps(self, agent_identifier, identifier, account_identifier, **kwargs):  # noqa: E501
        """ListApps returns list of apps in the repo  # noqa: E501

        ListApps returns list of apps in the repo.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_repository_service_list_apps(agent_identifier, identifier, account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str identifier: (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity.
        :param str project_identifier: Project Identifier for the Entity.
        :param str query_repo:
        :param str query_revision:
        :param str query_app_name:
        :param str query_app_project:
        :return: RepositoriesRepoAppsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.agent_repository_service_list_apps_with_http_info(agent_identifier, identifier, account_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.agent_repository_service_list_apps_with_http_info(agent_identifier, identifier, account_identifier, **kwargs)  # noqa: E501
            return data

    def agent_repository_service_list_apps_with_http_info(self, agent_identifier, identifier, account_identifier, **kwargs):  # noqa: E501
        """ListApps returns list of apps in the repo  # noqa: E501

        ListApps returns list of apps in the repo.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_repository_service_list_apps_with_http_info(agent_identifier, identifier, account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str identifier: (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity.
        :param str project_identifier: Project Identifier for the Entity.
        :param str query_repo:
        :param str query_revision:
        :param str query_app_name:
        :param str query_app_project:
        :return: RepositoriesRepoAppsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['agent_identifier', 'identifier', 'account_identifier', 'org_identifier', 'project_identifier', 'query_repo', 'query_revision', 'query_app_name', 'query_app_project']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method agent_repository_service_list_apps" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'agent_identifier' is set
        if ('agent_identifier' not in params or
                params['agent_identifier'] is None):
            raise ValueError("Missing the required parameter `agent_identifier` when calling `agent_repository_service_list_apps`")  # noqa: E501
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `agent_repository_service_list_apps`")  # noqa: E501
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `agent_repository_service_list_apps`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'agent_identifier' in params:
            path_params['agentIdentifier'] = params['agent_identifier']  # noqa: E501
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501
        if 'query_repo' in params:
            query_params.append(('query.repo', params['query_repo']))  # noqa: E501
        if 'query_revision' in params:
            query_params.append(('query.revision', params['query_revision']))  # noqa: E501
        if 'query_app_name' in params:
            query_params.append(('query.appName', params['query_app_name']))  # noqa: E501
        if 'query_app_project' in params:
            query_params.append(('query.appProject', params['query_app_project']))  # noqa: E501

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
            '/gitops/api/v1/agents/{agentIdentifier}/repositories/{identifier}/apps', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RepositoriesRepoAppsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def agent_repository_service_list_refs(self, agent_identifier, identifier, account_identifier, **kwargs):  # noqa: E501
        """Returns a list of refs (e.g. branches and tags) in the repo  # noqa: E501

        Returns a list of refs (e.g. branches and tags) in the repo.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_repository_service_list_refs(agent_identifier, identifier, account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str identifier: (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity.
        :param str project_identifier: Project Identifier for the Entity.
        :param str query_repo: Repo URL for query.
        :param bool query_force_refresh: Whether to force a cache refresh on repo's connection state.
        :param str query_project: The associated project project.
        :return: RepositoriesRefs
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.agent_repository_service_list_refs_with_http_info(agent_identifier, identifier, account_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.agent_repository_service_list_refs_with_http_info(agent_identifier, identifier, account_identifier, **kwargs)  # noqa: E501
            return data

    def agent_repository_service_list_refs_with_http_info(self, agent_identifier, identifier, account_identifier, **kwargs):  # noqa: E501
        """Returns a list of refs (e.g. branches and tags) in the repo  # noqa: E501

        Returns a list of refs (e.g. branches and tags) in the repo.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_repository_service_list_refs_with_http_info(agent_identifier, identifier, account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str identifier: (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity.
        :param str project_identifier: Project Identifier for the Entity.
        :param str query_repo: Repo URL for query.
        :param bool query_force_refresh: Whether to force a cache refresh on repo's connection state.
        :param str query_project: The associated project project.
        :return: RepositoriesRefs
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['agent_identifier', 'identifier', 'account_identifier', 'org_identifier', 'project_identifier', 'query_repo', 'query_force_refresh', 'query_project']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method agent_repository_service_list_refs" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'agent_identifier' is set
        if ('agent_identifier' not in params or
                params['agent_identifier'] is None):
            raise ValueError("Missing the required parameter `agent_identifier` when calling `agent_repository_service_list_refs`")  # noqa: E501
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `agent_repository_service_list_refs`")  # noqa: E501
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `agent_repository_service_list_refs`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'agent_identifier' in params:
            path_params['agentIdentifier'] = params['agent_identifier']  # noqa: E501
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501
        if 'query_repo' in params:
            query_params.append(('query.repo', params['query_repo']))  # noqa: E501
        if 'query_force_refresh' in params:
            query_params.append(('query.forceRefresh', params['query_force_refresh']))  # noqa: E501
        if 'query_project' in params:
            query_params.append(('query.project', params['query_project']))  # noqa: E501

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
            '/gitops/api/v1/agents/{agentIdentifier}/repositories/{identifier}/refs', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RepositoriesRefs',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def agent_repository_service_list_repositories(self, agent_identifier, account_identifier, **kwargs):  # noqa: E501
        """ListRepositories gets a list of all configured repositories  # noqa: E501

        ListRepositories gets a list of all configured repositories.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_repository_service_list_repositories(agent_identifier, account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity.
        :param str project_identifier: Project Identifier for the Entity.
        :param str identifier:
        :param str query_repo: Repo URL for query.
        :param bool query_force_refresh: Whether to force a cache refresh on repo's connection state.
        :param str query_project: The associated project project.
        :return: RepositoriesRepositoryList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.agent_repository_service_list_repositories_with_http_info(agent_identifier, account_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.agent_repository_service_list_repositories_with_http_info(agent_identifier, account_identifier, **kwargs)  # noqa: E501
            return data

    def agent_repository_service_list_repositories_with_http_info(self, agent_identifier, account_identifier, **kwargs):  # noqa: E501
        """ListRepositories gets a list of all configured repositories  # noqa: E501

        ListRepositories gets a list of all configured repositories.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_repository_service_list_repositories_with_http_info(agent_identifier, account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity.
        :param str project_identifier: Project Identifier for the Entity.
        :param str identifier:
        :param str query_repo: Repo URL for query.
        :param bool query_force_refresh: Whether to force a cache refresh on repo's connection state.
        :param str query_project: The associated project project.
        :return: RepositoriesRepositoryList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['agent_identifier', 'account_identifier', 'org_identifier', 'project_identifier', 'identifier', 'query_repo', 'query_force_refresh', 'query_project']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method agent_repository_service_list_repositories" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'agent_identifier' is set
        if ('agent_identifier' not in params or
                params['agent_identifier'] is None):
            raise ValueError("Missing the required parameter `agent_identifier` when calling `agent_repository_service_list_repositories`")  # noqa: E501
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `agent_repository_service_list_repositories`")  # noqa: E501

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
        if 'identifier' in params:
            query_params.append(('identifier', params['identifier']))  # noqa: E501
        if 'query_repo' in params:
            query_params.append(('query.repo', params['query_repo']))  # noqa: E501
        if 'query_force_refresh' in params:
            query_params.append(('query.forceRefresh', params['query_force_refresh']))  # noqa: E501
        if 'query_project' in params:
            query_params.append(('query.project', params['query_project']))  # noqa: E501

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
            '/gitops/api/v1/agents/{agentIdentifier}/repositories', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RepositoriesRepositoryList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def agent_repository_service_update_repository(self, body, agent_identifier, identifier, **kwargs):  # noqa: E501
        """UpdateRepository updates a repository configuration  # noqa: E501

        UpdateRepository updates a repository configuration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_repository_service_update_repository(body, agent_identifier, identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RepositoriesRepoUpdateRequest body: (required)
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str identifier: (required)
        :param str account_identifier: Account Identifier for the Entity.
        :param str org_identifier: Organization Identifier for the Entity.
        :param str project_identifier: Project Identifier for the Entity.
        :return: Servicev1Repository
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.agent_repository_service_update_repository_with_http_info(body, agent_identifier, identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.agent_repository_service_update_repository_with_http_info(body, agent_identifier, identifier, **kwargs)  # noqa: E501
            return data

    def agent_repository_service_update_repository_with_http_info(self, body, agent_identifier, identifier, **kwargs):  # noqa: E501
        """UpdateRepository updates a repository configuration  # noqa: E501

        UpdateRepository updates a repository configuration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_repository_service_update_repository_with_http_info(body, agent_identifier, identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RepositoriesRepoUpdateRequest body: (required)
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str identifier: (required)
        :param str account_identifier: Account Identifier for the Entity.
        :param str org_identifier: Organization Identifier for the Entity.
        :param str project_identifier: Project Identifier for the Entity.
        :return: Servicev1Repository
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'agent_identifier', 'identifier', 'account_identifier', 'org_identifier', 'project_identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method agent_repository_service_update_repository" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `agent_repository_service_update_repository`")  # noqa: E501
        # verify the required parameter 'agent_identifier' is set
        if ('agent_identifier' not in params or
                params['agent_identifier'] is None):
            raise ValueError("Missing the required parameter `agent_identifier` when calling `agent_repository_service_update_repository`")  # noqa: E501
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `agent_repository_service_update_repository`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'agent_identifier' in params:
            path_params['agentIdentifier'] = params['agent_identifier']  # noqa: E501
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501

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
            '/gitops/api/v1/agents/{agentIdentifier}/repositories/{identifier}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Servicev1Repository',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def agent_repository_service_validate_access(self, body, account_identifier, agent_identifier, **kwargs):  # noqa: E501
        """ValidateAccess gets connection state for a repository  # noqa: E501

        ValidateAccess gets connection state for a repository.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_repository_service_validate_access(body, account_identifier, agent_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RepositoriesRepoAccessQuery body: (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str org_identifier: Organization Identifier for the Entity.
        :param str project_identifier: Project Identifier for the Entity.
        :param str identifier:
        :return: CommonsConnectionState
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.agent_repository_service_validate_access_with_http_info(body, account_identifier, agent_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.agent_repository_service_validate_access_with_http_info(body, account_identifier, agent_identifier, **kwargs)  # noqa: E501
            return data

    def agent_repository_service_validate_access_with_http_info(self, body, account_identifier, agent_identifier, **kwargs):  # noqa: E501
        """ValidateAccess gets connection state for a repository  # noqa: E501

        ValidateAccess gets connection state for a repository.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agent_repository_service_validate_access_with_http_info(body, account_identifier, agent_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RepositoriesRepoAccessQuery body: (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str agent_identifier: Agent identifier for entity. (required)
        :param str org_identifier: Organization Identifier for the Entity.
        :param str project_identifier: Project Identifier for the Entity.
        :param str identifier:
        :return: CommonsConnectionState
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'account_identifier', 'agent_identifier', 'org_identifier', 'project_identifier', 'identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method agent_repository_service_validate_access" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `agent_repository_service_validate_access`")  # noqa: E501
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `agent_repository_service_validate_access`")  # noqa: E501
        # verify the required parameter 'agent_identifier' is set
        if ('agent_identifier' not in params or
                params['agent_identifier'] is None):
            raise ValueError("Missing the required parameter `agent_identifier` when calling `agent_repository_service_validate_access`")  # noqa: E501

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
        if 'identifier' in params:
            query_params.append(('identifier', params['identifier']))  # noqa: E501

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
            '/gitops/api/v1/agents/{agentIdentifier}/repositories/validate', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CommonsConnectionState',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def repository_service_exists(self, account_identifier, **kwargs):  # noqa: E501
        """Checks whether a repository with the given name exists  # noqa: E501

        Checks whether a repository with the given name exists.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.repository_service_exists(account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity.
        :param str project_identifier: Project Identifier for the Entity.
        :param str agent_identifier: Agent identifier for entity.
        :param str url:
        :return: bool
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.repository_service_exists_with_http_info(account_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.repository_service_exists_with_http_info(account_identifier, **kwargs)  # noqa: E501
            return data

    def repository_service_exists_with_http_info(self, account_identifier, **kwargs):  # noqa: E501
        """Checks whether a repository with the given name exists  # noqa: E501

        Checks whether a repository with the given name exists.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.repository_service_exists_with_http_info(account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity.
        :param str project_identifier: Project Identifier for the Entity.
        :param str agent_identifier: Agent identifier for entity.
        :param str url:
        :return: bool
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_identifier', 'org_identifier', 'project_identifier', 'agent_identifier', 'url']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method repository_service_exists" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `repository_service_exists`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501
        if 'agent_identifier' in params:
            query_params.append(('agentIdentifier', params['agent_identifier']))  # noqa: E501
        if 'url' in params:
            query_params.append(('url', params['url']))  # noqa: E501

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
            '/gitops/api/v1/repositories/exists', 'GET',
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

    def repository_service_list_repositories(self, body, **kwargs):  # noqa: E501
        """List returns list of Repositories  # noqa: E501

        List returns list of Repositories  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.repository_service_list_repositories(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V1RepositoryQuery body: (required)
        :return: V1Repositorylist
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.repository_service_list_repositories_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.repository_service_list_repositories_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def repository_service_list_repositories_with_http_info(self, body, **kwargs):  # noqa: E501
        """List returns list of Repositories  # noqa: E501

        List returns list of Repositories  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.repository_service_list_repositories_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V1RepositoryQuery body: (required)
        :return: V1Repositorylist
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
                    " to method repository_service_list_repositories" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `repository_service_list_repositories`")  # noqa: E501

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
            '/gitops/api/v1/repositories', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1Repositorylist',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
