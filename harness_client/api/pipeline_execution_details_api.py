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


class PipelineExecutionDetailsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_execution_detail(self, account_identifier, org_identifier, project_identifier, plan_execution_id, **kwargs):  # noqa: E501
        """Fetch Execution Details  # noqa: E501

        Returns the Pipeline Execution Details for a Given PlanExecution ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_execution_detail(account_identifier, org_identifier, project_identifier, plan_execution_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str plan_execution_id: Plan Execution Id for which we want to get the Execution details (required)
        :param str stage_node_id: Stage Node Identifier for which Stage Graph needs to be Rendered
        :param str stage_node_execution_id: Stage Node Execution ID for which Stage Graph needs to be Rendered. (Needed only when there are Multiple Runs for a Given Stage. It can be Extracted from LayoutNodeMap Field)
        :return: ResponseDTOPipelineExecutionDetail
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_execution_detail_with_http_info(account_identifier, org_identifier, project_identifier, plan_execution_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_execution_detail_with_http_info(account_identifier, org_identifier, project_identifier, plan_execution_id, **kwargs)  # noqa: E501
            return data

    def get_execution_detail_with_http_info(self, account_identifier, org_identifier, project_identifier, plan_execution_id, **kwargs):  # noqa: E501
        """Fetch Execution Details  # noqa: E501

        Returns the Pipeline Execution Details for a Given PlanExecution ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_execution_detail_with_http_info(account_identifier, org_identifier, project_identifier, plan_execution_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str plan_execution_id: Plan Execution Id for which we want to get the Execution details (required)
        :param str stage_node_id: Stage Node Identifier for which Stage Graph needs to be Rendered
        :param str stage_node_execution_id: Stage Node Execution ID for which Stage Graph needs to be Rendered. (Needed only when there are Multiple Runs for a Given Stage. It can be Extracted from LayoutNodeMap Field)
        :return: ResponseDTOPipelineExecutionDetail
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_identifier', 'org_identifier', 'project_identifier', 'plan_execution_id', 'stage_node_id', 'stage_node_execution_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_execution_detail" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `get_execution_detail`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `get_execution_detail`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `get_execution_detail`")  # noqa: E501
        # verify the required parameter 'plan_execution_id' is set
        if ('plan_execution_id' not in params or
                params['plan_execution_id'] is None):
            raise ValueError("Missing the required parameter `plan_execution_id` when calling `get_execution_detail`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'plan_execution_id' in params:
            path_params['planExecutionId'] = params['plan_execution_id']  # noqa: E501

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501
        if 'stage_node_id' in params:
            query_params.append(('stageNodeId', params['stage_node_id']))  # noqa: E501
        if 'stage_node_execution_id' in params:
            query_params.append(('stageNodeExecutionId', params['stage_node_execution_id']))  # noqa: E501

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
            '/pipeline/api/pipelines/execution/{planExecutionId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseDTOPipelineExecutionDetail',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_execution_detail_v2(self, account_identifier, org_identifier, project_identifier, plan_execution_id, **kwargs):  # noqa: E501
        """Fetch Execution Details  # noqa: E501

        Returns the Pipeline Execution Details for a Given PlanExecution ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_execution_detail_v2(account_identifier, org_identifier, project_identifier, plan_execution_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str plan_execution_id: Plan Execution Id for which we want to get the Execution details (required)
        :param str stage_node_id: Stage Node Identifier for which Stage Graph needs to be Rendered
        :param str stage_node_execution_id: Stage Node Execution ID for which Stage Graph needs to be Rendered. (Needed only when there are Multiple Runs for a Given Stage. It can be Extracted from LayoutNodeMap Field)
        :param str child_stage_node_id: Stage Node Execution ID for which Stage Graph needs to be Rendered. (Needed only when there are Multiple Runs for a Given Stage. It can be Extracted from LayoutNodeMap Field)
        :param bool render_full_bottom_graph: Generate Graph for all the Stages including Steps in each Stage
        :return: ResponseDTOPipelineExecutionDetail
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_execution_detail_v2_with_http_info(account_identifier, org_identifier, project_identifier, plan_execution_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_execution_detail_v2_with_http_info(account_identifier, org_identifier, project_identifier, plan_execution_id, **kwargs)  # noqa: E501
            return data

    def get_execution_detail_v2_with_http_info(self, account_identifier, org_identifier, project_identifier, plan_execution_id, **kwargs):  # noqa: E501
        """Fetch Execution Details  # noqa: E501

        Returns the Pipeline Execution Details for a Given PlanExecution ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_execution_detail_v2_with_http_info(account_identifier, org_identifier, project_identifier, plan_execution_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str plan_execution_id: Plan Execution Id for which we want to get the Execution details (required)
        :param str stage_node_id: Stage Node Identifier for which Stage Graph needs to be Rendered
        :param str stage_node_execution_id: Stage Node Execution ID for which Stage Graph needs to be Rendered. (Needed only when there are Multiple Runs for a Given Stage. It can be Extracted from LayoutNodeMap Field)
        :param str child_stage_node_id: Stage Node Execution ID for which Stage Graph needs to be Rendered. (Needed only when there are Multiple Runs for a Given Stage. It can be Extracted from LayoutNodeMap Field)
        :param bool render_full_bottom_graph: Generate Graph for all the Stages including Steps in each Stage
        :return: ResponseDTOPipelineExecutionDetail
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_identifier', 'org_identifier', 'project_identifier', 'plan_execution_id', 'stage_node_id', 'stage_node_execution_id', 'child_stage_node_id', 'render_full_bottom_graph']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_execution_detail_v2" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `get_execution_detail_v2`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `get_execution_detail_v2`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `get_execution_detail_v2`")  # noqa: E501
        # verify the required parameter 'plan_execution_id' is set
        if ('plan_execution_id' not in params or
                params['plan_execution_id'] is None):
            raise ValueError("Missing the required parameter `plan_execution_id` when calling `get_execution_detail_v2`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'plan_execution_id' in params:
            path_params['planExecutionId'] = params['plan_execution_id']  # noqa: E501

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501
        if 'stage_node_id' in params:
            query_params.append(('stageNodeId', params['stage_node_id']))  # noqa: E501
        if 'stage_node_execution_id' in params:
            query_params.append(('stageNodeExecutionId', params['stage_node_execution_id']))  # noqa: E501
        if 'child_stage_node_id' in params:
            query_params.append(('childStageNodeId', params['child_stage_node_id']))  # noqa: E501
        if 'render_full_bottom_graph' in params:
            query_params.append(('renderFullBottomGraph', params['render_full_bottom_graph']))  # noqa: E501

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
            '/pipeline/api/pipelines/execution/v2/{planExecutionId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseDTOPipelineExecutionDetail',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_execution_sub_graph_for_node_execution(self, account_identifier, org_identifier, project_identifier, node_execution_id, plan_execution_id, **kwargs):  # noqa: E501
        """Fetch Execution SubGraph for a Given NodeExecution ID  # noqa: E501

        Returns the Pipeline Execution SubGraph for a Given NodeExecution ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_execution_sub_graph_for_node_execution(account_identifier, org_identifier, project_identifier, node_execution_id, plan_execution_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str node_execution_id: Node Execution Id for which we want to get the Execution SubGraph (required)
        :param str plan_execution_id: Plan Execution Id for which we want to get the Execution details (required)
        :return: ResponseDTONodeExecutionDetails
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_execution_sub_graph_for_node_execution_with_http_info(account_identifier, org_identifier, project_identifier, node_execution_id, plan_execution_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_execution_sub_graph_for_node_execution_with_http_info(account_identifier, org_identifier, project_identifier, node_execution_id, plan_execution_id, **kwargs)  # noqa: E501
            return data

    def get_execution_sub_graph_for_node_execution_with_http_info(self, account_identifier, org_identifier, project_identifier, node_execution_id, plan_execution_id, **kwargs):  # noqa: E501
        """Fetch Execution SubGraph for a Given NodeExecution ID  # noqa: E501

        Returns the Pipeline Execution SubGraph for a Given NodeExecution ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_execution_sub_graph_for_node_execution_with_http_info(account_identifier, org_identifier, project_identifier, node_execution_id, plan_execution_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str node_execution_id: Node Execution Id for which we want to get the Execution SubGraph (required)
        :param str plan_execution_id: Plan Execution Id for which we want to get the Execution details (required)
        :return: ResponseDTONodeExecutionDetails
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_identifier', 'org_identifier', 'project_identifier', 'node_execution_id', 'plan_execution_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_execution_sub_graph_for_node_execution" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `get_execution_sub_graph_for_node_execution`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `get_execution_sub_graph_for_node_execution`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `get_execution_sub_graph_for_node_execution`")  # noqa: E501
        # verify the required parameter 'node_execution_id' is set
        if ('node_execution_id' not in params or
                params['node_execution_id'] is None):
            raise ValueError("Missing the required parameter `node_execution_id` when calling `get_execution_sub_graph_for_node_execution`")  # noqa: E501
        # verify the required parameter 'plan_execution_id' is set
        if ('plan_execution_id' not in params or
                params['plan_execution_id'] is None):
            raise ValueError("Missing the required parameter `plan_execution_id` when calling `get_execution_sub_graph_for_node_execution`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'node_execution_id' in params:
            path_params['nodeExecutionId'] = params['node_execution_id']  # noqa: E501
        if 'plan_execution_id' in params:
            path_params['planExecutionId'] = params['plan_execution_id']  # noqa: E501

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
            ['application/json', 'application/yaml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/pipeline/api/pipelines/execution/subGraph/{planExecutionId}/{nodeExecutionId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseDTONodeExecutionDetails',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_inputset_yaml_v2(self, account_identifier, org_identifier, project_identifier, plan_execution_id, **kwargs):  # noqa: E501
        """Get the Input Set YAML used for given Plan Execution  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_inputset_yaml_v2(account_identifier, org_identifier, project_identifier, plan_execution_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str plan_execution_id: Plan Execution Id for which we want to get the Input Set YAML (required)
        :param bool resolve_expressions: A boolean that indicates whether or not expressions should be resolved in input set yaml 
        :param str resolve_expressions_type: Resolve Expressions Type indicates what kind of expressions should be resolved in input set yaml. The default value is UNKNOWN in which case no expressions will be resolvedChoose a value from the enum list: [RESOLVE_ALL_EXPRESSIONS, RESOLVE_TRIGGER_EXPRESSIONS, UNKNOWN]
        :return: ResponseDTOInputSetTemplateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_inputset_yaml_v2_with_http_info(account_identifier, org_identifier, project_identifier, plan_execution_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_inputset_yaml_v2_with_http_info(account_identifier, org_identifier, project_identifier, plan_execution_id, **kwargs)  # noqa: E501
            return data

    def get_inputset_yaml_v2_with_http_info(self, account_identifier, org_identifier, project_identifier, plan_execution_id, **kwargs):  # noqa: E501
        """Get the Input Set YAML used for given Plan Execution  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_inputset_yaml_v2_with_http_info(account_identifier, org_identifier, project_identifier, plan_execution_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str plan_execution_id: Plan Execution Id for which we want to get the Input Set YAML (required)
        :param bool resolve_expressions: A boolean that indicates whether or not expressions should be resolved in input set yaml 
        :param str resolve_expressions_type: Resolve Expressions Type indicates what kind of expressions should be resolved in input set yaml. The default value is UNKNOWN in which case no expressions will be resolvedChoose a value from the enum list: [RESOLVE_ALL_EXPRESSIONS, RESOLVE_TRIGGER_EXPRESSIONS, UNKNOWN]
        :return: ResponseDTOInputSetTemplateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_identifier', 'org_identifier', 'project_identifier', 'plan_execution_id', 'resolve_expressions', 'resolve_expressions_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_inputset_yaml_v2" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `get_inputset_yaml_v2`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `get_inputset_yaml_v2`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `get_inputset_yaml_v2`")  # noqa: E501
        # verify the required parameter 'plan_execution_id' is set
        if ('plan_execution_id' not in params or
                params['plan_execution_id'] is None):
            raise ValueError("Missing the required parameter `plan_execution_id` when calling `get_inputset_yaml_v2`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'plan_execution_id' in params:
            path_params['planExecutionId'] = params['plan_execution_id']  # noqa: E501

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501
        if 'resolve_expressions' in params:
            query_params.append(('resolveExpressions', params['resolve_expressions']))  # noqa: E501
        if 'resolve_expressions_type' in params:
            query_params.append(('resolveExpressionsType', params['resolve_expressions_type']))  # noqa: E501

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
            '/pipeline/api/pipelines/execution/{planExecutionId}/inputsetV2', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseDTOInputSetTemplateResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_list_of_execution_identifier(self, account_identifier, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """List Execution Identifier  # noqa: E501

        Returns a List of Pipeline Executions Identifier with Specific Filter  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_list_of_execution_identifier(account_identifier, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str pipeline_identifier: Pipeline Identifier filter if exact pipelines needs to be filtered.
        :param int page: Page Index of the results to fetch.Default Value: 0
        :param int size: Results per page
        :param str branch: Name of the branch.
        :param str repo_identifier: Git Sync Config Id.
        :param bool get_default_from_other_repo: if true, return all the default entities
        :return: ResponseDTOPagePipelineExecutionIdentifierSummary
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_list_of_execution_identifier_with_http_info(account_identifier, org_identifier, project_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.get_list_of_execution_identifier_with_http_info(account_identifier, org_identifier, project_identifier, **kwargs)  # noqa: E501
            return data

    def get_list_of_execution_identifier_with_http_info(self, account_identifier, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """List Execution Identifier  # noqa: E501

        Returns a List of Pipeline Executions Identifier with Specific Filter  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_list_of_execution_identifier_with_http_info(account_identifier, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str pipeline_identifier: Pipeline Identifier filter if exact pipelines needs to be filtered.
        :param int page: Page Index of the results to fetch.Default Value: 0
        :param int size: Results per page
        :param str branch: Name of the branch.
        :param str repo_identifier: Git Sync Config Id.
        :param bool get_default_from_other_repo: if true, return all the default entities
        :return: ResponseDTOPagePipelineExecutionIdentifierSummary
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_identifier', 'org_identifier', 'project_identifier', 'pipeline_identifier', 'page', 'size', 'branch', 'repo_identifier', 'get_default_from_other_repo']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_list_of_execution_identifier" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `get_list_of_execution_identifier`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `get_list_of_execution_identifier`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `get_list_of_execution_identifier`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501
        if 'pipeline_identifier' in params:
            query_params.append(('pipelineIdentifier', params['pipeline_identifier']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'size' in params:
            query_params.append(('size', params['size']))  # noqa: E501
        if 'branch' in params:
            query_params.append(('branch', params['branch']))  # noqa: E501
        if 'repo_identifier' in params:
            query_params.append(('repoIdentifier', params['repo_identifier']))  # noqa: E501
        if 'get_default_from_other_repo' in params:
            query_params.append(('getDefaultFromOtherRepo', params['get_default_from_other_repo']))  # noqa: E501

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
            '/pipeline/api/pipelines/execution/executionSummary', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseDTOPagePipelineExecutionIdentifierSummary',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_list_of_executions(self, account_identifier, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """List Executions  # noqa: E501

        Returns a List of Pipeline Executions with Specific Filter  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_list_of_executions(account_identifier, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param FilterProperties body: Returns a List of Pipeline Executions with Specific Filters
        :param str search_term: Search term to filter out pipelines based on pipeline name, identifier, tags.
        :param str pipeline_identifier: Pipeline Identifier filter if exact pipelines needs to be filtered.
        :param int page: Page Index of the results to fetch.Default Value: 0
        :param int size: Results per page
        :param list[str] sort: Sort criteria for the elements.
        :param str filter_identifier:
        :param bool show_all_executions:
        :param str module:
        :param list[str] status:
        :param bool my_deployments:
        :param str branch: Name of the branch.
        :param str repo_identifier: Git Sync Config Id.
        :param bool get_default_from_other_repo: if true, return all the default entities
        :return: ResponseDTOPagePipelineExecutionSummary
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_list_of_executions_with_http_info(account_identifier, org_identifier, project_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.get_list_of_executions_with_http_info(account_identifier, org_identifier, project_identifier, **kwargs)  # noqa: E501
            return data

    def get_list_of_executions_with_http_info(self, account_identifier, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """List Executions  # noqa: E501

        Returns a List of Pipeline Executions with Specific Filter  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_list_of_executions_with_http_info(account_identifier, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param FilterProperties body: Returns a List of Pipeline Executions with Specific Filters
        :param str search_term: Search term to filter out pipelines based on pipeline name, identifier, tags.
        :param str pipeline_identifier: Pipeline Identifier filter if exact pipelines needs to be filtered.
        :param int page: Page Index of the results to fetch.Default Value: 0
        :param int size: Results per page
        :param list[str] sort: Sort criteria for the elements.
        :param str filter_identifier:
        :param bool show_all_executions:
        :param str module:
        :param list[str] status:
        :param bool my_deployments:
        :param str branch: Name of the branch.
        :param str repo_identifier: Git Sync Config Id.
        :param bool get_default_from_other_repo: if true, return all the default entities
        :return: ResponseDTOPagePipelineExecutionSummary
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_identifier', 'org_identifier', 'project_identifier', 'body', 'search_term', 'pipeline_identifier', 'page', 'size', 'sort', 'filter_identifier', 'show_all_executions', 'module', 'status', 'my_deployments', 'branch', 'repo_identifier', 'get_default_from_other_repo']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_list_of_executions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `get_list_of_executions`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `get_list_of_executions`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `get_list_of_executions`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501
        if 'search_term' in params:
            query_params.append(('searchTerm', params['search_term']))  # noqa: E501
        if 'pipeline_identifier' in params:
            query_params.append(('pipelineIdentifier', params['pipeline_identifier']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'size' in params:
            query_params.append(('size', params['size']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'multi'  # noqa: E501
        if 'filter_identifier' in params:
            query_params.append(('filterIdentifier', params['filter_identifier']))  # noqa: E501
        if 'show_all_executions' in params:
            query_params.append(('showAllExecutions', params['show_all_executions']))  # noqa: E501
        if 'module' in params:
            query_params.append(('module', params['module']))  # noqa: E501
        if 'status' in params:
            query_params.append(('status', params['status']))  # noqa: E501
            collection_formats['status'] = 'multi'  # noqa: E501
        if 'my_deployments' in params:
            query_params.append(('myDeployments', params['my_deployments']))  # noqa: E501
        if 'branch' in params:
            query_params.append(('branch', params['branch']))  # noqa: E501
        if 'repo_identifier' in params:
            query_params.append(('repoIdentifier', params['repo_identifier']))  # noqa: E501
        if 'get_default_from_other_repo' in params:
            query_params.append(('getDefaultFromOtherRepo', params['get_default_from_other_repo']))  # noqa: E501

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
            '/pipeline/api/pipelines/execution/summary', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseDTOPagePipelineExecutionSummary',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_notes_for_execution(self, account_identifier, plan_execution_id, **kwargs):  # noqa: E501
        """Get Notes for a pipelineExecution  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_notes_for_execution(account_identifier, plan_execution_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str plan_execution_id: ExecutionId of the execution for which we want to get notes (required)
        :return: ResponseDTOPipelineExecutionNotes
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_notes_for_execution_with_http_info(account_identifier, plan_execution_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_notes_for_execution_with_http_info(account_identifier, plan_execution_id, **kwargs)  # noqa: E501
            return data

    def get_notes_for_execution_with_http_info(self, account_identifier, plan_execution_id, **kwargs):  # noqa: E501
        """Get Notes for a pipelineExecution  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_notes_for_execution_with_http_info(account_identifier, plan_execution_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str plan_execution_id: ExecutionId of the execution for which we want to get notes (required)
        :return: ResponseDTOPipelineExecutionNotes
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_identifier', 'plan_execution_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_notes_for_execution" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `get_notes_for_execution`")  # noqa: E501
        # verify the required parameter 'plan_execution_id' is set
        if ('plan_execution_id' not in params or
                params['plan_execution_id'] is None):
            raise ValueError("Missing the required parameter `plan_execution_id` when calling `get_notes_for_execution`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'plan_execution_id' in params:
            path_params['planExecutionId'] = params['plan_execution_id']  # noqa: E501

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
            '/pipeline/api/pipelines/execution/{planExecutionId}/notes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseDTOPipelineExecutionNotes',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_notes_for_execution(self, account_identifier, org_identifier, project_identifier, notes_for_pipeline_execution, plan_execution_id, **kwargs):  # noqa: E501
        """Updates Notes for a pipelineExecution  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_notes_for_execution(account_identifier, org_identifier, project_identifier, notes_for_pipeline_execution, plan_execution_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str notes_for_pipeline_execution: Notes of a Pipeline Execution (required)
        :param str plan_execution_id: ExecutionId of the execution for which we want to update notes (required)
        :return: ResponseDTOPipelineExecutionNotes
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_notes_for_execution_with_http_info(account_identifier, org_identifier, project_identifier, notes_for_pipeline_execution, plan_execution_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_notes_for_execution_with_http_info(account_identifier, org_identifier, project_identifier, notes_for_pipeline_execution, plan_execution_id, **kwargs)  # noqa: E501
            return data

    def update_notes_for_execution_with_http_info(self, account_identifier, org_identifier, project_identifier, notes_for_pipeline_execution, plan_execution_id, **kwargs):  # noqa: E501
        """Updates Notes for a pipelineExecution  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_notes_for_execution_with_http_info(account_identifier, org_identifier, project_identifier, notes_for_pipeline_execution, plan_execution_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str notes_for_pipeline_execution: Notes of a Pipeline Execution (required)
        :param str plan_execution_id: ExecutionId of the execution for which we want to update notes (required)
        :return: ResponseDTOPipelineExecutionNotes
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_identifier', 'org_identifier', 'project_identifier', 'notes_for_pipeline_execution', 'plan_execution_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_notes_for_execution" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `update_notes_for_execution`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `update_notes_for_execution`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `update_notes_for_execution`")  # noqa: E501
        # verify the required parameter 'notes_for_pipeline_execution' is set
        if ('notes_for_pipeline_execution' not in params or
                params['notes_for_pipeline_execution'] is None):
            raise ValueError("Missing the required parameter `notes_for_pipeline_execution` when calling `update_notes_for_execution`")  # noqa: E501
        # verify the required parameter 'plan_execution_id' is set
        if ('plan_execution_id' not in params or
                params['plan_execution_id'] is None):
            raise ValueError("Missing the required parameter `plan_execution_id` when calling `update_notes_for_execution`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'plan_execution_id' in params:
            path_params['planExecutionId'] = params['plan_execution_id']  # noqa: E501

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501
        if 'notes_for_pipeline_execution' in params:
            query_params.append(('notesForPipelineExecution', params['notes_for_pipeline_execution']))  # noqa: E501

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
            '/pipeline/api/pipelines/execution/{planExecutionId}/notes', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseDTOPipelineExecutionNotes',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
