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


class PipelineApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_pipeline(self, account_identifier, org_identifier, project_identifier, pipeline_identifier, **kwargs):  # noqa: E501
        """Delete a Pipeline  # noqa: E501

        Deletes a Pipeline by Identifier  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_pipeline(account_identifier, org_identifier, project_identifier, pipeline_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str pipeline_identifier: Pipeline Identifier (required)
        :param str if_match: Version of Entity to match
        :param str branch: Name of the branch.
        :param str repo_identifier: Git Sync Config Id.
        :param str root_folder: Path to the root folder of the Entity.
        :param str file_path: File Path of the Entity.
        :param str commit_msg: Commit Message to use for the merge commit.
        :param str last_object_id: Last Object Id
        :return: ResponseDTOBoolean
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_pipeline_with_http_info(account_identifier, org_identifier, project_identifier, pipeline_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_pipeline_with_http_info(account_identifier, org_identifier, project_identifier, pipeline_identifier, **kwargs)  # noqa: E501
            return data

    def delete_pipeline_with_http_info(self, account_identifier, org_identifier, project_identifier, pipeline_identifier, **kwargs):  # noqa: E501
        """Delete a Pipeline  # noqa: E501

        Deletes a Pipeline by Identifier  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_pipeline_with_http_info(account_identifier, org_identifier, project_identifier, pipeline_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str pipeline_identifier: Pipeline Identifier (required)
        :param str if_match: Version of Entity to match
        :param str branch: Name of the branch.
        :param str repo_identifier: Git Sync Config Id.
        :param str root_folder: Path to the root folder of the Entity.
        :param str file_path: File Path of the Entity.
        :param str commit_msg: Commit Message to use for the merge commit.
        :param str last_object_id: Last Object Id
        :return: ResponseDTOBoolean
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_identifier', 'org_identifier', 'project_identifier', 'pipeline_identifier', 'if_match', 'branch', 'repo_identifier', 'root_folder', 'file_path', 'commit_msg', 'last_object_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_pipeline" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `delete_pipeline`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `delete_pipeline`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `delete_pipeline`")  # noqa: E501
        # verify the required parameter 'pipeline_identifier' is set
        if ('pipeline_identifier' not in params or
                params['pipeline_identifier'] is None):
            raise ValueError("Missing the required parameter `pipeline_identifier` when calling `delete_pipeline`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'pipeline_identifier' in params:
            path_params['pipelineIdentifier'] = params['pipeline_identifier']  # noqa: E501

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501
        if 'branch' in params:
            query_params.append(('branch', params['branch']))  # noqa: E501
        if 'repo_identifier' in params:
            query_params.append(('repoIdentifier', params['repo_identifier']))  # noqa: E501
        if 'root_folder' in params:
            query_params.append(('rootFolder', params['root_folder']))  # noqa: E501
        if 'file_path' in params:
            query_params.append(('filePath', params['file_path']))  # noqa: E501
        if 'commit_msg' in params:
            query_params.append(('commitMsg', params['commit_msg']))  # noqa: E501
        if 'last_object_id' in params:
            query_params.append(('lastObjectId', params['last_object_id']))  # noqa: E501

        header_params = {}
        if 'if_match' in params:
            header_params['If-Match'] = params['if_match']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/yaml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/pipeline/api/pipelines/{pipelineIdentifier}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseDTOBoolean',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_pipeline(self, account_identifier, org_identifier, project_identifier, pipeline_identifier, **kwargs):  # noqa: E501
        """Fetch a Pipeline  # noqa: E501

        Returns a Pipeline by Identifier  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_pipeline(account_identifier, org_identifier, project_identifier, pipeline_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str pipeline_identifier: Pipeline Identifier (required)
        :param str branch: Name of the branch.
        :param str repo_identifier: Git Sync Config Id.
        :param bool get_default_from_other_repo: if true, return all the default entities
        :param bool get_templates_resolved_pipeline: This is a boolean value. If true, returns Templates resolved Pipeline YAML in the response else returns null.
        :param bool load_from_fallback_branch:
        :param bool validate_async:
        :param str load_from_cache:
        :return: ResponseDTOPMSPipelineResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_pipeline_with_http_info(account_identifier, org_identifier, project_identifier, pipeline_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.get_pipeline_with_http_info(account_identifier, org_identifier, project_identifier, pipeline_identifier, **kwargs)  # noqa: E501
            return data

    def get_pipeline_with_http_info(self, account_identifier, org_identifier, project_identifier, pipeline_identifier, **kwargs):  # noqa: E501
        """Fetch a Pipeline  # noqa: E501

        Returns a Pipeline by Identifier  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_pipeline_with_http_info(account_identifier, org_identifier, project_identifier, pipeline_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str pipeline_identifier: Pipeline Identifier (required)
        :param str branch: Name of the branch.
        :param str repo_identifier: Git Sync Config Id.
        :param bool get_default_from_other_repo: if true, return all the default entities
        :param bool get_templates_resolved_pipeline: This is a boolean value. If true, returns Templates resolved Pipeline YAML in the response else returns null.
        :param bool load_from_fallback_branch:
        :param bool validate_async:
        :param str load_from_cache:
        :return: ResponseDTOPMSPipelineResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_identifier', 'org_identifier', 'project_identifier', 'pipeline_identifier', 'branch', 'repo_identifier', 'get_default_from_other_repo', 'get_templates_resolved_pipeline', 'load_from_fallback_branch', 'validate_async', 'load_from_cache']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_pipeline" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `get_pipeline`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `get_pipeline`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `get_pipeline`")  # noqa: E501
        # verify the required parameter 'pipeline_identifier' is set
        if ('pipeline_identifier' not in params or
                params['pipeline_identifier'] is None):
            raise ValueError("Missing the required parameter `pipeline_identifier` when calling `get_pipeline`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'pipeline_identifier' in params:
            path_params['pipelineIdentifier'] = params['pipeline_identifier']  # noqa: E501

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501
        if 'branch' in params:
            query_params.append(('branch', params['branch']))  # noqa: E501
        if 'repo_identifier' in params:
            query_params.append(('repoIdentifier', params['repo_identifier']))  # noqa: E501
        if 'get_default_from_other_repo' in params:
            query_params.append(('getDefaultFromOtherRepo', params['get_default_from_other_repo']))  # noqa: E501
        if 'get_templates_resolved_pipeline' in params:
            query_params.append(('getTemplatesResolvedPipeline', params['get_templates_resolved_pipeline']))  # noqa: E501
        if 'load_from_fallback_branch' in params:
            query_params.append(('loadFromFallbackBranch', params['load_from_fallback_branch']))  # noqa: E501
        if 'validate_async' in params:
            query_params.append(('validateAsync', params['validate_async']))  # noqa: E501

        header_params = {}
        if 'load_from_cache' in params:
            header_params['Load-From-Cache'] = params['load_from_cache']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/yaml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/pipeline/api/pipelines/{pipelineIdentifier}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseDTOPMSPipelineResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_pipeline_list(self, account_identifier, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """List Pipelines  # noqa: E501

        Returns List of Pipelines in the Given Project  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_pipeline_list(account_identifier, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param PipelineFilterProperties body: This is the body for the filter properties for listing pipelines.
        :param int page: Page Index of the results to fetch.Default Value: 0
        :param int size: Results per page
        :param list[str] sort: Sort criteria for the elements.
        :param str search_term: Search term to filter out pipelines based on pipeline name, identifier, tags.
        :param str module:
        :param str filter_identifier:
        :param str branch: Name of the branch.
        :param str repo_identifier: Git Sync Config Id.
        :param bool get_default_from_other_repo: if true, return all the default entities
        :param bool get_distinct_from_branches: Boolean flag to get distinct pipelines from all branches.
        :return: ResponseDTOPagePMSPipelineSummaryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_pipeline_list_with_http_info(account_identifier, org_identifier, project_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.get_pipeline_list_with_http_info(account_identifier, org_identifier, project_identifier, **kwargs)  # noqa: E501
            return data

    def get_pipeline_list_with_http_info(self, account_identifier, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """List Pipelines  # noqa: E501

        Returns List of Pipelines in the Given Project  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_pipeline_list_with_http_info(account_identifier, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param PipelineFilterProperties body: This is the body for the filter properties for listing pipelines.
        :param int page: Page Index of the results to fetch.Default Value: 0
        :param int size: Results per page
        :param list[str] sort: Sort criteria for the elements.
        :param str search_term: Search term to filter out pipelines based on pipeline name, identifier, tags.
        :param str module:
        :param str filter_identifier:
        :param str branch: Name of the branch.
        :param str repo_identifier: Git Sync Config Id.
        :param bool get_default_from_other_repo: if true, return all the default entities
        :param bool get_distinct_from_branches: Boolean flag to get distinct pipelines from all branches.
        :return: ResponseDTOPagePMSPipelineSummaryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_identifier', 'org_identifier', 'project_identifier', 'body', 'page', 'size', 'sort', 'search_term', 'module', 'filter_identifier', 'branch', 'repo_identifier', 'get_default_from_other_repo', 'get_distinct_from_branches']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_pipeline_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `get_pipeline_list`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `get_pipeline_list`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `get_pipeline_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'size' in params:
            query_params.append(('size', params['size']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'multi'  # noqa: E501
        if 'search_term' in params:
            query_params.append(('searchTerm', params['search_term']))  # noqa: E501
        if 'module' in params:
            query_params.append(('module', params['module']))  # noqa: E501
        if 'filter_identifier' in params:
            query_params.append(('filterIdentifier', params['filter_identifier']))  # noqa: E501
        if 'branch' in params:
            query_params.append(('branch', params['branch']))  # noqa: E501
        if 'repo_identifier' in params:
            query_params.append(('repoIdentifier', params['repo_identifier']))  # noqa: E501
        if 'get_default_from_other_repo' in params:
            query_params.append(('getDefaultFromOtherRepo', params['get_default_from_other_repo']))  # noqa: E501
        if 'get_distinct_from_branches' in params:
            query_params.append(('getDistinctFromBranches', params['get_distinct_from_branches']))  # noqa: E501

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
            '/pipeline/api/pipelines/list', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseDTOPagePMSPipelineSummaryResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_pipeline_summary(self, account_identifier, org_identifier, project_identifier, pipeline_identifier, **kwargs):  # noqa: E501
        """Fetch Pipeline Summary  # noqa: E501

        Returns Pipeline Summary by Identifier  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_pipeline_summary(account_identifier, org_identifier, project_identifier, pipeline_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str pipeline_identifier: Pipeline Identifier (required)
        :param str branch: Name of the branch.
        :param str repo_identifier: Git Sync Config Id.
        :param bool get_default_from_other_repo: if true, return all the default entities
        :param bool load_from_fallback_branch:
        :param str load_from_cache:
        :return: ResponseDTOPMSPipelineSummaryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_pipeline_summary_with_http_info(account_identifier, org_identifier, project_identifier, pipeline_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.get_pipeline_summary_with_http_info(account_identifier, org_identifier, project_identifier, pipeline_identifier, **kwargs)  # noqa: E501
            return data

    def get_pipeline_summary_with_http_info(self, account_identifier, org_identifier, project_identifier, pipeline_identifier, **kwargs):  # noqa: E501
        """Fetch Pipeline Summary  # noqa: E501

        Returns Pipeline Summary by Identifier  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_pipeline_summary_with_http_info(account_identifier, org_identifier, project_identifier, pipeline_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str pipeline_identifier: Pipeline Identifier (required)
        :param str branch: Name of the branch.
        :param str repo_identifier: Git Sync Config Id.
        :param bool get_default_from_other_repo: if true, return all the default entities
        :param bool load_from_fallback_branch:
        :param str load_from_cache:
        :return: ResponseDTOPMSPipelineSummaryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_identifier', 'org_identifier', 'project_identifier', 'pipeline_identifier', 'branch', 'repo_identifier', 'get_default_from_other_repo', 'load_from_fallback_branch', 'load_from_cache']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_pipeline_summary" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `get_pipeline_summary`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `get_pipeline_summary`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `get_pipeline_summary`")  # noqa: E501
        # verify the required parameter 'pipeline_identifier' is set
        if ('pipeline_identifier' not in params or
                params['pipeline_identifier'] is None):
            raise ValueError("Missing the required parameter `pipeline_identifier` when calling `get_pipeline_summary`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'pipeline_identifier' in params:
            path_params['pipelineIdentifier'] = params['pipeline_identifier']  # noqa: E501

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501
        if 'branch' in params:
            query_params.append(('branch', params['branch']))  # noqa: E501
        if 'repo_identifier' in params:
            query_params.append(('repoIdentifier', params['repo_identifier']))  # noqa: E501
        if 'get_default_from_other_repo' in params:
            query_params.append(('getDefaultFromOtherRepo', params['get_default_from_other_repo']))  # noqa: E501
        if 'load_from_fallback_branch' in params:
            query_params.append(('loadFromFallbackBranch', params['load_from_fallback_branch']))  # noqa: E501

        header_params = {}
        if 'load_from_cache' in params:
            header_params['Load-From-Cache'] = params['load_from_cache']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/yaml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/pipeline/api/pipelines/summary/{pipelineIdentifier}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseDTOPMSPipelineSummaryResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def import_pipeline(self, account_identifier, org_identifier, project_identifier, pipeline_identifier, **kwargs):  # noqa: E501
        """Import and Create Pipeline from Git Repository  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.import_pipeline(account_identifier, org_identifier, project_identifier, pipeline_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str pipeline_identifier: Pipeline Identifier (required)
        :param PipelineImportRequest body:
        :param str connector_ref: Identifier of Connector needed for CRUD operations on the respective Entity
        :param str repo_name: Name of the repository.
        :param str branch: Name of the branch.
        :param str file_path: File Path of the Entity.
        :param bool is_force_import: isForceImport
        :return: ResponseDTOPipelineSaveResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.import_pipeline_with_http_info(account_identifier, org_identifier, project_identifier, pipeline_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.import_pipeline_with_http_info(account_identifier, org_identifier, project_identifier, pipeline_identifier, **kwargs)  # noqa: E501
            return data

    def import_pipeline_with_http_info(self, account_identifier, org_identifier, project_identifier, pipeline_identifier, **kwargs):  # noqa: E501
        """Import and Create Pipeline from Git Repository  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.import_pipeline_with_http_info(account_identifier, org_identifier, project_identifier, pipeline_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str pipeline_identifier: Pipeline Identifier (required)
        :param PipelineImportRequest body:
        :param str connector_ref: Identifier of Connector needed for CRUD operations on the respective Entity
        :param str repo_name: Name of the repository.
        :param str branch: Name of the branch.
        :param str file_path: File Path of the Entity.
        :param bool is_force_import: isForceImport
        :return: ResponseDTOPipelineSaveResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_identifier', 'org_identifier', 'project_identifier', 'pipeline_identifier', 'body', 'connector_ref', 'repo_name', 'branch', 'file_path', 'is_force_import']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method import_pipeline" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `import_pipeline`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `import_pipeline`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `import_pipeline`")  # noqa: E501
        # verify the required parameter 'pipeline_identifier' is set
        if ('pipeline_identifier' not in params or
                params['pipeline_identifier'] is None):
            raise ValueError("Missing the required parameter `pipeline_identifier` when calling `import_pipeline`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'pipeline_identifier' in params:
            path_params['pipelineIdentifier'] = params['pipeline_identifier']  # noqa: E501

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501
        if 'connector_ref' in params:
            query_params.append(('connectorRef', params['connector_ref']))  # noqa: E501
        if 'repo_name' in params:
            query_params.append(('repoName', params['repo_name']))  # noqa: E501
        if 'branch' in params:
            query_params.append(('branch', params['branch']))  # noqa: E501
        if 'file_path' in params:
            query_params.append(('filePath', params['file_path']))  # noqa: E501
        if 'is_force_import' in params:
            query_params.append(('isForceImport', params['is_force_import']))  # noqa: E501

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
            ['application/json', 'application/yaml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/pipeline/api/pipelines/import/{pipelineIdentifier}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseDTOPipelineSaveResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_pipeline(self, body, account_identifier, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """Create a Pipeline  # noqa: E501

        Creates a Pipeline  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_pipeline(body, account_identifier, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str body: Pipeline YAML (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str branch: Name of the branch.
        :param str repo_identifier: Git Sync Config Id.
        :param str root_folder: Path to the root folder of the Entity.
        :param str file_path: File Path of the Entity.
        :param str commit_msg: File Path of the Entity.
        :param bool is_new_branch: Checks the new branch
        :param str base_branch: Name of the default branch.
        :param str connector_ref: Identifier of Connector needed for CRUD operations on the respective Entity
        :param str store_type: Tells whether the Entity is to be saved on Git or not
        :param str repo_name: Name of the repository.
        :return: ResponseDTOString
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_pipeline_with_http_info(body, account_identifier, org_identifier, project_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.post_pipeline_with_http_info(body, account_identifier, org_identifier, project_identifier, **kwargs)  # noqa: E501
            return data

    def post_pipeline_with_http_info(self, body, account_identifier, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """Create a Pipeline  # noqa: E501

        Creates a Pipeline  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_pipeline_with_http_info(body, account_identifier, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str body: Pipeline YAML (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str branch: Name of the branch.
        :param str repo_identifier: Git Sync Config Id.
        :param str root_folder: Path to the root folder of the Entity.
        :param str file_path: File Path of the Entity.
        :param str commit_msg: File Path of the Entity.
        :param bool is_new_branch: Checks the new branch
        :param str base_branch: Name of the default branch.
        :param str connector_ref: Identifier of Connector needed for CRUD operations on the respective Entity
        :param str store_type: Tells whether the Entity is to be saved on Git or not
        :param str repo_name: Name of the repository.
        :return: ResponseDTOString
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'account_identifier', 'org_identifier', 'project_identifier', 'branch', 'repo_identifier', 'root_folder', 'file_path', 'commit_msg', 'is_new_branch', 'base_branch', 'connector_ref', 'store_type', 'repo_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_pipeline" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_pipeline`")  # noqa: E501
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `post_pipeline`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `post_pipeline`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `post_pipeline`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501
        if 'branch' in params:
            query_params.append(('branch', params['branch']))  # noqa: E501
        if 'repo_identifier' in params:
            query_params.append(('repoIdentifier', params['repo_identifier']))  # noqa: E501
        if 'root_folder' in params:
            query_params.append(('rootFolder', params['root_folder']))  # noqa: E501
        if 'file_path' in params:
            query_params.append(('filePath', params['file_path']))  # noqa: E501
        if 'commit_msg' in params:
            query_params.append(('commitMsg', params['commit_msg']))  # noqa: E501
        if 'is_new_branch' in params:
            query_params.append(('isNewBranch', params['is_new_branch']))  # noqa: E501
        if 'base_branch' in params:
            query_params.append(('baseBranch', params['base_branch']))  # noqa: E501
        if 'connector_ref' in params:
            query_params.append(('connectorRef', params['connector_ref']))  # noqa: E501
        if 'store_type' in params:
            query_params.append(('storeType', params['store_type']))  # noqa: E501
        if 'repo_name' in params:
            query_params.append(('repoName', params['repo_name']))  # noqa: E501

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
            ['application/json', 'application/yaml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/pipeline/api/pipelines', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseDTOString',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_pipeline_v2(self, body, account_identifier, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """Create a Pipeline  # noqa: E501

        Creates a Pipeline  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_pipeline_v2(body, account_identifier, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str body: Pipeline YAML (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str branch: Name of the branch.
        :param str repo_identifier: Git Sync Config Id.
        :param str root_folder: Path to the root folder of the Entity.
        :param str file_path: File Path of the Entity.
        :param str commit_msg: File Path of the Entity.
        :param bool is_new_branch: Checks the new branch
        :param str base_branch: Name of the default branch.
        :param str connector_ref: Identifier of Connector needed for CRUD operations on the respective Entity
        :param str store_type: Tells whether the Entity is to be saved on Git or not
        :param str repo_name: Name of the repository.
        :param bool public:
        :return: ResponseDTOPipelineSaveResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_pipeline_v2_with_http_info(body, account_identifier, org_identifier, project_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.post_pipeline_v2_with_http_info(body, account_identifier, org_identifier, project_identifier, **kwargs)  # noqa: E501
            return data

    def post_pipeline_v2_with_http_info(self, body, account_identifier, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """Create a Pipeline  # noqa: E501

        Creates a Pipeline  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_pipeline_v2_with_http_info(body, account_identifier, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str body: Pipeline YAML (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str branch: Name of the branch.
        :param str repo_identifier: Git Sync Config Id.
        :param str root_folder: Path to the root folder of the Entity.
        :param str file_path: File Path of the Entity.
        :param str commit_msg: File Path of the Entity.
        :param bool is_new_branch: Checks the new branch
        :param str base_branch: Name of the default branch.
        :param str connector_ref: Identifier of Connector needed for CRUD operations on the respective Entity
        :param str store_type: Tells whether the Entity is to be saved on Git or not
        :param str repo_name: Name of the repository.
        :param bool public:
        :return: ResponseDTOPipelineSaveResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'account_identifier', 'org_identifier', 'project_identifier', 'branch', 'repo_identifier', 'root_folder', 'file_path', 'commit_msg', 'is_new_branch', 'base_branch', 'connector_ref', 'store_type', 'repo_name', 'public']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_pipeline_v2" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_pipeline_v2`")  # noqa: E501
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `post_pipeline_v2`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `post_pipeline_v2`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `post_pipeline_v2`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501
        if 'branch' in params:
            query_params.append(('branch', params['branch']))  # noqa: E501
        if 'repo_identifier' in params:
            query_params.append(('repoIdentifier', params['repo_identifier']))  # noqa: E501
        if 'root_folder' in params:
            query_params.append(('rootFolder', params['root_folder']))  # noqa: E501
        if 'file_path' in params:
            query_params.append(('filePath', params['file_path']))  # noqa: E501
        if 'commit_msg' in params:
            query_params.append(('commitMsg', params['commit_msg']))  # noqa: E501
        if 'is_new_branch' in params:
            query_params.append(('isNewBranch', params['is_new_branch']))  # noqa: E501
        if 'base_branch' in params:
            query_params.append(('baseBranch', params['base_branch']))  # noqa: E501
        if 'connector_ref' in params:
            query_params.append(('connectorRef', params['connector_ref']))  # noqa: E501
        if 'store_type' in params:
            query_params.append(('storeType', params['store_type']))  # noqa: E501
        if 'repo_name' in params:
            query_params.append(('repoName', params['repo_name']))  # noqa: E501
        if 'public' in params:
            query_params.append(('public', params['public']))  # noqa: E501

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
            ['application/yaml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/pipeline/api/pipelines/v2', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseDTOPipelineSaveResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_pipeline(self, body, account_identifier, org_identifier, project_identifier, pipeline_identifier, **kwargs):  # noqa: E501
        """Update a Pipeline  # noqa: E501

        Updates a Pipeline by Identifier  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_pipeline(body, account_identifier, org_identifier, project_identifier, pipeline_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str body: Pipeline YAML to be updated (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str pipeline_identifier: Pipeline Identifier (required)
        :param str if_match: Version of Entity to match
        :param str branch: Name of the branch.
        :param str repo_identifier: Git Sync Config Id.
        :param str root_folder: Path to the root folder of the Entity.
        :param str file_path: Path to the root folder of the Entity.
        :param str commit_msg: Commit Message to use for the merge commit.
        :param str last_object_id: Its required field during update call request. It can be fetched from the response of GET API call for the entity
        :param str resolved_conflict_commit_id: If the entity is git-synced, this parameter represents the commit id against which file conflicts are resolved
        :param str base_branch: Name of the default branch.
        :param str connector_ref: Identifier of Connector needed for CRUD operations on the respective Entity
        :param bool is_new_branch: Checks the new branch
        :return: ResponseDTOString
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_pipeline_with_http_info(body, account_identifier, org_identifier, project_identifier, pipeline_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.update_pipeline_with_http_info(body, account_identifier, org_identifier, project_identifier, pipeline_identifier, **kwargs)  # noqa: E501
            return data

    def update_pipeline_with_http_info(self, body, account_identifier, org_identifier, project_identifier, pipeline_identifier, **kwargs):  # noqa: E501
        """Update a Pipeline  # noqa: E501

        Updates a Pipeline by Identifier  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_pipeline_with_http_info(body, account_identifier, org_identifier, project_identifier, pipeline_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str body: Pipeline YAML to be updated (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str pipeline_identifier: Pipeline Identifier (required)
        :param str if_match: Version of Entity to match
        :param str branch: Name of the branch.
        :param str repo_identifier: Git Sync Config Id.
        :param str root_folder: Path to the root folder of the Entity.
        :param str file_path: Path to the root folder of the Entity.
        :param str commit_msg: Commit Message to use for the merge commit.
        :param str last_object_id: Its required field during update call request. It can be fetched from the response of GET API call for the entity
        :param str resolved_conflict_commit_id: If the entity is git-synced, this parameter represents the commit id against which file conflicts are resolved
        :param str base_branch: Name of the default branch.
        :param str connector_ref: Identifier of Connector needed for CRUD operations on the respective Entity
        :param bool is_new_branch: Checks the new branch
        :return: ResponseDTOString
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'account_identifier', 'org_identifier', 'project_identifier', 'pipeline_identifier', 'if_match', 'branch', 'repo_identifier', 'root_folder', 'file_path', 'commit_msg', 'last_object_id', 'resolved_conflict_commit_id', 'base_branch', 'connector_ref', 'is_new_branch']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_pipeline" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_pipeline`")  # noqa: E501
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `update_pipeline`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `update_pipeline`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `update_pipeline`")  # noqa: E501
        # verify the required parameter 'pipeline_identifier' is set
        if ('pipeline_identifier' not in params or
                params['pipeline_identifier'] is None):
            raise ValueError("Missing the required parameter `pipeline_identifier` when calling `update_pipeline`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'pipeline_identifier' in params:
            path_params['pipelineIdentifier'] = params['pipeline_identifier']  # noqa: E501

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501
        if 'branch' in params:
            query_params.append(('branch', params['branch']))  # noqa: E501
        if 'repo_identifier' in params:
            query_params.append(('repoIdentifier', params['repo_identifier']))  # noqa: E501
        if 'root_folder' in params:
            query_params.append(('rootFolder', params['root_folder']))  # noqa: E501
        if 'file_path' in params:
            query_params.append(('filePath', params['file_path']))  # noqa: E501
        if 'commit_msg' in params:
            query_params.append(('commitMsg', params['commit_msg']))  # noqa: E501
        if 'last_object_id' in params:
            query_params.append(('lastObjectId', params['last_object_id']))  # noqa: E501
        if 'resolved_conflict_commit_id' in params:
            query_params.append(('resolvedConflictCommitId', params['resolved_conflict_commit_id']))  # noqa: E501
        if 'base_branch' in params:
            query_params.append(('baseBranch', params['base_branch']))  # noqa: E501
        if 'connector_ref' in params:
            query_params.append(('connectorRef', params['connector_ref']))  # noqa: E501
        if 'is_new_branch' in params:
            query_params.append(('isNewBranch', params['is_new_branch']))  # noqa: E501

        header_params = {}
        if 'if_match' in params:
            header_params['If-Match'] = params['if_match']  # noqa: E501

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
            ['application/json', 'application/yaml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/pipeline/api/pipelines/{pipelineIdentifier}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseDTOString',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_pipeline_git_details(self, account_identifier, org_identifier, project_identifier, pipeline_identifier, **kwargs):  # noqa: E501
        """Update git-metadata in remote pipeline Entity  # noqa: E501

        Update git-metadata in remote pipeline and returns the identifier of updated pipeline  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_pipeline_git_details(account_identifier, org_identifier, project_identifier, pipeline_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str pipeline_identifier: Pipeline Identifier (required)
        :param str connector_ref: Identifier of Connector needed for CRUD operations on the respective Entity
        :param str repo_name: Name of the repository.
        :param str file_path: File Path of the Entity.
        :return: ResponseDTOPMSGitUpdateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_pipeline_git_details_with_http_info(account_identifier, org_identifier, project_identifier, pipeline_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.update_pipeline_git_details_with_http_info(account_identifier, org_identifier, project_identifier, pipeline_identifier, **kwargs)  # noqa: E501
            return data

    def update_pipeline_git_details_with_http_info(self, account_identifier, org_identifier, project_identifier, pipeline_identifier, **kwargs):  # noqa: E501
        """Update git-metadata in remote pipeline Entity  # noqa: E501

        Update git-metadata in remote pipeline and returns the identifier of updated pipeline  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_pipeline_git_details_with_http_info(account_identifier, org_identifier, project_identifier, pipeline_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str pipeline_identifier: Pipeline Identifier (required)
        :param str connector_ref: Identifier of Connector needed for CRUD operations on the respective Entity
        :param str repo_name: Name of the repository.
        :param str file_path: File Path of the Entity.
        :return: ResponseDTOPMSGitUpdateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_identifier', 'org_identifier', 'project_identifier', 'pipeline_identifier', 'connector_ref', 'repo_name', 'file_path']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_pipeline_git_details" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `update_pipeline_git_details`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `update_pipeline_git_details`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `update_pipeline_git_details`")  # noqa: E501
        # verify the required parameter 'pipeline_identifier' is set
        if ('pipeline_identifier' not in params or
                params['pipeline_identifier'] is None):
            raise ValueError("Missing the required parameter `pipeline_identifier` when calling `update_pipeline_git_details`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'pipeline_identifier' in params:
            path_params['pipelineIdentifier'] = params['pipeline_identifier']  # noqa: E501

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501
        if 'connector_ref' in params:
            query_params.append(('connectorRef', params['connector_ref']))  # noqa: E501
        if 'repo_name' in params:
            query_params.append(('repoName', params['repo_name']))  # noqa: E501
        if 'file_path' in params:
            query_params.append(('filePath', params['file_path']))  # noqa: E501

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
            '/pipeline/api/pipelines/{pipelineIdentifier}/update-git-metadata', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseDTOPMSGitUpdateResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_pipeline_v2(self, body, account_identifier, org_identifier, project_identifier, pipeline_identifier, **kwargs):  # noqa: E501
        """Update a Pipeline  # noqa: E501

        Updates a Pipeline by Identifier  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_pipeline_v2(body, account_identifier, org_identifier, project_identifier, pipeline_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str body: Pipeline YAML to be updated (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str pipeline_identifier: Pipeline Identifier (required)
        :param str if_match: Version of Entity to match
        :param str branch: Name of the branch.
        :param str repo_identifier: Git Sync Config Id.
        :param str root_folder: Path to the root folder of the Entity.
        :param str file_path: Path to the root folder of the Entity.
        :param str commit_msg: Commit Message to use for the merge commit.
        :param str last_object_id: Its required field during update call request. It can be fetched from the response of GET API call for the entity
        :param str resolved_conflict_commit_id: If the entity is git-synced, this parameter represents the commit id against which file conflicts are resolved
        :param str base_branch: Name of the default branch.
        :param str connector_ref: Identifier of Connector needed for CRUD operations on the respective Entity
        :param bool is_new_branch: Checks the new branch
        :param bool public:
        :return: ResponseDTOPipelineSaveResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_pipeline_v2_with_http_info(body, account_identifier, org_identifier, project_identifier, pipeline_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.update_pipeline_v2_with_http_info(body, account_identifier, org_identifier, project_identifier, pipeline_identifier, **kwargs)  # noqa: E501
            return data

    def update_pipeline_v2_with_http_info(self, body, account_identifier, org_identifier, project_identifier, pipeline_identifier, **kwargs):  # noqa: E501
        """Update a Pipeline  # noqa: E501

        Updates a Pipeline by Identifier  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_pipeline_v2_with_http_info(body, account_identifier, org_identifier, project_identifier, pipeline_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str body: Pipeline YAML to be updated (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str pipeline_identifier: Pipeline Identifier (required)
        :param str if_match: Version of Entity to match
        :param str branch: Name of the branch.
        :param str repo_identifier: Git Sync Config Id.
        :param str root_folder: Path to the root folder of the Entity.
        :param str file_path: Path to the root folder of the Entity.
        :param str commit_msg: Commit Message to use for the merge commit.
        :param str last_object_id: Its required field during update call request. It can be fetched from the response of GET API call for the entity
        :param str resolved_conflict_commit_id: If the entity is git-synced, this parameter represents the commit id against which file conflicts are resolved
        :param str base_branch: Name of the default branch.
        :param str connector_ref: Identifier of Connector needed for CRUD operations on the respective Entity
        :param bool is_new_branch: Checks the new branch
        :param bool public:
        :return: ResponseDTOPipelineSaveResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'account_identifier', 'org_identifier', 'project_identifier', 'pipeline_identifier', 'if_match', 'branch', 'repo_identifier', 'root_folder', 'file_path', 'commit_msg', 'last_object_id', 'resolved_conflict_commit_id', 'base_branch', 'connector_ref', 'is_new_branch', 'public']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_pipeline_v2" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_pipeline_v2`")  # noqa: E501
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `update_pipeline_v2`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `update_pipeline_v2`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `update_pipeline_v2`")  # noqa: E501
        # verify the required parameter 'pipeline_identifier' is set
        if ('pipeline_identifier' not in params or
                params['pipeline_identifier'] is None):
            raise ValueError("Missing the required parameter `pipeline_identifier` when calling `update_pipeline_v2`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'pipeline_identifier' in params:
            path_params['pipelineIdentifier'] = params['pipeline_identifier']  # noqa: E501

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501
        if 'branch' in params:
            query_params.append(('branch', params['branch']))  # noqa: E501
        if 'repo_identifier' in params:
            query_params.append(('repoIdentifier', params['repo_identifier']))  # noqa: E501
        if 'root_folder' in params:
            query_params.append(('rootFolder', params['root_folder']))  # noqa: E501
        if 'file_path' in params:
            query_params.append(('filePath', params['file_path']))  # noqa: E501
        if 'commit_msg' in params:
            query_params.append(('commitMsg', params['commit_msg']))  # noqa: E501
        if 'last_object_id' in params:
            query_params.append(('lastObjectId', params['last_object_id']))  # noqa: E501
        if 'resolved_conflict_commit_id' in params:
            query_params.append(('resolvedConflictCommitId', params['resolved_conflict_commit_id']))  # noqa: E501
        if 'base_branch' in params:
            query_params.append(('baseBranch', params['base_branch']))  # noqa: E501
        if 'connector_ref' in params:
            query_params.append(('connectorRef', params['connector_ref']))  # noqa: E501
        if 'is_new_branch' in params:
            query_params.append(('isNewBranch', params['is_new_branch']))  # noqa: E501
        if 'public' in params:
            query_params.append(('public', params['public']))  # noqa: E501

        header_params = {}
        if 'if_match' in params:
            header_params['If-Match'] = params['if_match']  # noqa: E501

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
            ['application/yaml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/pipeline/api/pipelines/v2/{pipelineIdentifier}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseDTOPipelineSaveResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
