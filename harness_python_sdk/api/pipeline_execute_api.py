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


class PipelineExecuteApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def handle_stage_interrupt(self, account_identifier, org_identifier, project_identifier, interrupt_type, plan_execution_id, node_execution_id, **kwargs):  # noqa: E501
        """Handles the interrupt for a given stage in a pipeline  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.handle_stage_interrupt(account_identifier, org_identifier, project_identifier, interrupt_type, plan_execution_id, node_execution_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str interrupt_type: The Interrupt type needed to be applied to the execution. Choose a value from the enum list. (required)
        :param str plan_execution_id: The Pipeline Execution Id on which the Interrupt needs to be applied. (required)
        :param str node_execution_id: The runtime Id of the step/stage on which the Interrupt needs to be applied. (required)
        :return: ResponseDTOInterruptResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.handle_stage_interrupt_with_http_info(account_identifier, org_identifier, project_identifier, interrupt_type, plan_execution_id, node_execution_id, **kwargs)  # noqa: E501
        else:
            (data) = self.handle_stage_interrupt_with_http_info(account_identifier, org_identifier, project_identifier, interrupt_type, plan_execution_id, node_execution_id, **kwargs)  # noqa: E501
            return data

    def handle_stage_interrupt_with_http_info(self, account_identifier, org_identifier, project_identifier, interrupt_type, plan_execution_id, node_execution_id, **kwargs):  # noqa: E501
        """Handles the interrupt for a given stage in a pipeline  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.handle_stage_interrupt_with_http_info(account_identifier, org_identifier, project_identifier, interrupt_type, plan_execution_id, node_execution_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str interrupt_type: The Interrupt type needed to be applied to the execution. Choose a value from the enum list. (required)
        :param str plan_execution_id: The Pipeline Execution Id on which the Interrupt needs to be applied. (required)
        :param str node_execution_id: The runtime Id of the step/stage on which the Interrupt needs to be applied. (required)
        :return: ResponseDTOInterruptResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_identifier', 'org_identifier', 'project_identifier', 'interrupt_type', 'plan_execution_id', 'node_execution_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method handle_stage_interrupt" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `handle_stage_interrupt`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `handle_stage_interrupt`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `handle_stage_interrupt`")  # noqa: E501
        # verify the required parameter 'interrupt_type' is set
        if ('interrupt_type' not in params or
                params['interrupt_type'] is None):
            raise ValueError("Missing the required parameter `interrupt_type` when calling `handle_stage_interrupt`")  # noqa: E501
        # verify the required parameter 'plan_execution_id' is set
        if ('plan_execution_id' not in params or
                params['plan_execution_id'] is None):
            raise ValueError("Missing the required parameter `plan_execution_id` when calling `handle_stage_interrupt`")  # noqa: E501
        # verify the required parameter 'node_execution_id' is set
        if ('node_execution_id' not in params or
                params['node_execution_id'] is None):
            raise ValueError("Missing the required parameter `node_execution_id` when calling `handle_stage_interrupt`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'plan_execution_id' in params:
            path_params['planExecutionId'] = params['plan_execution_id']  # noqa: E501
        if 'node_execution_id' in params:
            path_params['nodeExecutionId'] = params['node_execution_id']  # noqa: E501

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501
        if 'interrupt_type' in params:
            query_params.append(('interruptType', params['interrupt_type']))  # noqa: E501

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
            '/pipeline/api/pipeline/execute/interrupt/{planExecutionId}/{nodeExecutionId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseDTOInterruptResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_pipeline_execute_with_input_set_list(self, body, account_identifier, org_identifier, project_identifier, identifier, **kwargs):  # noqa: E501
        """Execute a Pipeline with Input Set References  # noqa: E501

        Execute a Pipeline with Input Set References  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_pipeline_execute_with_input_set_list(body, account_identifier, org_identifier, project_identifier, identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MergeInputSetRequest body: (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str identifier: Pipeline identifier for the entity. Identifier of the Pipeline to be executed (required)
        :param str module_type: Module type for the entity. If its from deployments,type will be CD , if its from build type will be CI
        :param str branch: Name of the branch.
        :param str repo_identifier: Git Sync Config Id.
        :param bool get_default_from_other_repo: if true, return all the default entities
        :param bool use_fqnif_error:
        :param str notes_for_pipeline_execution: Notes of a pipeline execution
        :return: ResponseDTOPlanExecutionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_pipeline_execute_with_input_set_list_with_http_info(body, account_identifier, org_identifier, project_identifier, identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.post_pipeline_execute_with_input_set_list_with_http_info(body, account_identifier, org_identifier, project_identifier, identifier, **kwargs)  # noqa: E501
            return data

    def post_pipeline_execute_with_input_set_list_with_http_info(self, body, account_identifier, org_identifier, project_identifier, identifier, **kwargs):  # noqa: E501
        """Execute a Pipeline with Input Set References  # noqa: E501

        Execute a Pipeline with Input Set References  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_pipeline_execute_with_input_set_list_with_http_info(body, account_identifier, org_identifier, project_identifier, identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MergeInputSetRequest body: (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str identifier: Pipeline identifier for the entity. Identifier of the Pipeline to be executed (required)
        :param str module_type: Module type for the entity. If its from deployments,type will be CD , if its from build type will be CI
        :param str branch: Name of the branch.
        :param str repo_identifier: Git Sync Config Id.
        :param bool get_default_from_other_repo: if true, return all the default entities
        :param bool use_fqnif_error:
        :param str notes_for_pipeline_execution: Notes of a pipeline execution
        :return: ResponseDTOPlanExecutionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'account_identifier', 'org_identifier', 'project_identifier', 'identifier', 'module_type', 'branch', 'repo_identifier', 'get_default_from_other_repo', 'use_fqnif_error', 'notes_for_pipeline_execution']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_pipeline_execute_with_input_set_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_pipeline_execute_with_input_set_list`")  # noqa: E501
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `post_pipeline_execute_with_input_set_list`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `post_pipeline_execute_with_input_set_list`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `post_pipeline_execute_with_input_set_list`")  # noqa: E501
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `post_pipeline_execute_with_input_set_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501
        if 'module_type' in params:
            query_params.append(('moduleType', params['module_type']))  # noqa: E501
        if 'branch' in params:
            query_params.append(('branch', params['branch']))  # noqa: E501
        if 'repo_identifier' in params:
            query_params.append(('repoIdentifier', params['repo_identifier']))  # noqa: E501
        if 'get_default_from_other_repo' in params:
            query_params.append(('getDefaultFromOtherRepo', params['get_default_from_other_repo']))  # noqa: E501
        if 'use_fqnif_error' in params:
            query_params.append(('useFQNIfError', params['use_fqnif_error']))  # noqa: E501
        if 'notes_for_pipeline_execution' in params:
            query_params.append(('notesForPipelineExecution', params['notes_for_pipeline_execution']))  # noqa: E501

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
            '/pipeline/api/pipeline/execute/{identifier}/inputSetList', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseDTOPlanExecutionResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_pipeline_execute_with_input_set_yaml(self, account_identifier, org_identifier, project_identifier, identifier, **kwargs):  # noqa: E501
        """Execute a Pipeline with Runtime Input YAML  # noqa: E501

        Execute a Pipeline with Runtime Input YAML  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_pipeline_execute_with_input_set_yaml(account_identifier, org_identifier, project_identifier, identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str identifier: Pipeline identifier for the entity. Identifier of the Pipeline to be executed (required)
        :param str body: Enter Runtime Input YAML if the Pipeline contains Runtime Inputs. Template for this can be Fetched from /inputSets/template API.
        :param str module_type: Module type for the entity. If its from deployments,type will be CD , if its from build type will be CI
        :param str branch: Name of the branch.
        :param str repo_identifier: Git Sync Config Id.
        :param bool get_default_from_other_repo: if true, return all the default entities
        :param bool use_fqnif_error:
        :param bool notify_only_user:
        :param str notes_for_pipeline_execution: Notes of a pipeline execution
        :return: ResponseDTOPlanExecutionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_pipeline_execute_with_input_set_yaml_with_http_info(account_identifier, org_identifier, project_identifier, identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.post_pipeline_execute_with_input_set_yaml_with_http_info(account_identifier, org_identifier, project_identifier, identifier, **kwargs)  # noqa: E501
            return data

    def post_pipeline_execute_with_input_set_yaml_with_http_info(self, account_identifier, org_identifier, project_identifier, identifier, **kwargs):  # noqa: E501
        """Execute a Pipeline with Runtime Input YAML  # noqa: E501

        Execute a Pipeline with Runtime Input YAML  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_pipeline_execute_with_input_set_yaml_with_http_info(account_identifier, org_identifier, project_identifier, identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str identifier: Pipeline identifier for the entity. Identifier of the Pipeline to be executed (required)
        :param str body: Enter Runtime Input YAML if the Pipeline contains Runtime Inputs. Template for this can be Fetched from /inputSets/template API.
        :param str module_type: Module type for the entity. If its from deployments,type will be CD , if its from build type will be CI
        :param str branch: Name of the branch.
        :param str repo_identifier: Git Sync Config Id.
        :param bool get_default_from_other_repo: if true, return all the default entities
        :param bool use_fqnif_error:
        :param bool notify_only_user:
        :param str notes_for_pipeline_execution: Notes of a pipeline execution
        :return: ResponseDTOPlanExecutionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_identifier', 'org_identifier', 'project_identifier', 'identifier', 'body', 'module_type', 'branch', 'repo_identifier', 'get_default_from_other_repo', 'use_fqnif_error', 'notify_only_user', 'notes_for_pipeline_execution']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_pipeline_execute_with_input_set_yaml" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `post_pipeline_execute_with_input_set_yaml`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `post_pipeline_execute_with_input_set_yaml`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `post_pipeline_execute_with_input_set_yaml`")  # noqa: E501
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `post_pipeline_execute_with_input_set_yaml`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501
        if 'module_type' in params:
            query_params.append(('moduleType', params['module_type']))  # noqa: E501
        if 'branch' in params:
            query_params.append(('branch', params['branch']))  # noqa: E501
        if 'repo_identifier' in params:
            query_params.append(('repoIdentifier', params['repo_identifier']))  # noqa: E501
        if 'get_default_from_other_repo' in params:
            query_params.append(('getDefaultFromOtherRepo', params['get_default_from_other_repo']))  # noqa: E501
        if 'use_fqnif_error' in params:
            query_params.append(('useFQNIfError', params['use_fqnif_error']))  # noqa: E501
        if 'notify_only_user' in params:
            query_params.append(('notifyOnlyUser', params['notify_only_user']))  # noqa: E501
        if 'notes_for_pipeline_execution' in params:
            query_params.append(('notesForPipelineExecution', params['notes_for_pipeline_execution']))  # noqa: E501

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
            '/pipeline/api/pipeline/execute/{identifier}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseDTOPlanExecutionResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_handle_interrupt(self, account_identifier, org_identifier, project_identifier, interrupt_type, plan_execution_id, **kwargs):  # noqa: E501
        """Execute an Interrupt  # noqa: E501

        Executes an Interrupt on a Given Execution  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_handle_interrupt(account_identifier, org_identifier, project_identifier, interrupt_type, plan_execution_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str interrupt_type: The Interrupt type needed to be applied to the execution. Choose a value from the enum list. (required)
        :param str plan_execution_id: The Pipeline Execution Id on which the Interrupt needs to be applied. (required)
        :return: ResponseDTOInterruptResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.put_handle_interrupt_with_http_info(account_identifier, org_identifier, project_identifier, interrupt_type, plan_execution_id, **kwargs)  # noqa: E501
        else:
            (data) = self.put_handle_interrupt_with_http_info(account_identifier, org_identifier, project_identifier, interrupt_type, plan_execution_id, **kwargs)  # noqa: E501
            return data

    def put_handle_interrupt_with_http_info(self, account_identifier, org_identifier, project_identifier, interrupt_type, plan_execution_id, **kwargs):  # noqa: E501
        """Execute an Interrupt  # noqa: E501

        Executes an Interrupt on a Given Execution  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_handle_interrupt_with_http_info(account_identifier, org_identifier, project_identifier, interrupt_type, plan_execution_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str interrupt_type: The Interrupt type needed to be applied to the execution. Choose a value from the enum list. (required)
        :param str plan_execution_id: The Pipeline Execution Id on which the Interrupt needs to be applied. (required)
        :return: ResponseDTOInterruptResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_identifier', 'org_identifier', 'project_identifier', 'interrupt_type', 'plan_execution_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_handle_interrupt" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `put_handle_interrupt`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `put_handle_interrupt`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `put_handle_interrupt`")  # noqa: E501
        # verify the required parameter 'interrupt_type' is set
        if ('interrupt_type' not in params or
                params['interrupt_type'] is None):
            raise ValueError("Missing the required parameter `interrupt_type` when calling `put_handle_interrupt`")  # noqa: E501
        # verify the required parameter 'plan_execution_id' is set
        if ('plan_execution_id' not in params or
                params['plan_execution_id'] is None):
            raise ValueError("Missing the required parameter `plan_execution_id` when calling `put_handle_interrupt`")  # noqa: E501

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
        if 'interrupt_type' in params:
            query_params.append(('interruptType', params['interrupt_type']))  # noqa: E501

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
            '/pipeline/api/pipeline/execute/interrupt/{planExecutionId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseDTOInterruptResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retry_history(self, account_identifier, org_identifier, project_identifier, pipeline_identifier, plan_execution_id, **kwargs):  # noqa: E501
        """Retry History for a given execution  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retry_history(account_identifier, org_identifier, project_identifier, pipeline_identifier, plan_execution_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str pipeline_identifier: Pipeline Identifier (required)
        :param str plan_execution_id: planExecutionId of the execution of whose we need to find the retry history (required)
        :return: ResponseDTORetryHistoryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retry_history_with_http_info(account_identifier, org_identifier, project_identifier, pipeline_identifier, plan_execution_id, **kwargs)  # noqa: E501
        else:
            (data) = self.retry_history_with_http_info(account_identifier, org_identifier, project_identifier, pipeline_identifier, plan_execution_id, **kwargs)  # noqa: E501
            return data

    def retry_history_with_http_info(self, account_identifier, org_identifier, project_identifier, pipeline_identifier, plan_execution_id, **kwargs):  # noqa: E501
        """Retry History for a given execution  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retry_history_with_http_info(account_identifier, org_identifier, project_identifier, pipeline_identifier, plan_execution_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str pipeline_identifier: Pipeline Identifier (required)
        :param str plan_execution_id: planExecutionId of the execution of whose we need to find the retry history (required)
        :return: ResponseDTORetryHistoryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_identifier', 'org_identifier', 'project_identifier', 'pipeline_identifier', 'plan_execution_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retry_history" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `retry_history`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `retry_history`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `retry_history`")  # noqa: E501
        # verify the required parameter 'pipeline_identifier' is set
        if ('pipeline_identifier' not in params or
                params['pipeline_identifier'] is None):
            raise ValueError("Missing the required parameter `pipeline_identifier` when calling `retry_history`")  # noqa: E501
        # verify the required parameter 'plan_execution_id' is set
        if ('plan_execution_id' not in params or
                params['plan_execution_id'] is None):
            raise ValueError("Missing the required parameter `plan_execution_id` when calling `retry_history`")  # noqa: E501

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
        if 'pipeline_identifier' in params:
            query_params.append(('pipelineIdentifier', params['pipeline_identifier']))  # noqa: E501

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
            '/pipeline/api/pipeline/execute/retryHistory/{planExecutionId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseDTORetryHistoryResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retry_pipeline(self, account_identifier, org_identifier, project_identifier, plan_execution_id, retry_stages, identifier, **kwargs):  # noqa: E501
        """Retry a executed pipeline with inputSet pipeline yaml  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retry_pipeline(account_identifier, org_identifier, project_identifier, plan_execution_id, retry_stages, identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str plan_execution_id: This param contains the previous execution execution id. This is basically when we are rerunning a Pipeline. (required)
        :param list[str] retry_stages: This param contains the identifier of stages from where to resume. It will be a list if we want to retry from parallel group  (required)
        :param str identifier: Pipeline Identifier (required)
        :param str body:
        :param str module_type: Module type for the entity. If its from deployments,type will be CD , if its from build type will be CI
        :param bool run_all_stages: This param provides an option to run only the failed stages when Pipeline fails at parallel group. By default, it will run all the stages in the failed parallel group.
        :param str notes_for_pipeline_execution: Notes of a pipeline execution
        :return: ResponseDTOPlanExecutionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retry_pipeline_with_http_info(account_identifier, org_identifier, project_identifier, plan_execution_id, retry_stages, identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.retry_pipeline_with_http_info(account_identifier, org_identifier, project_identifier, plan_execution_id, retry_stages, identifier, **kwargs)  # noqa: E501
            return data

    def retry_pipeline_with_http_info(self, account_identifier, org_identifier, project_identifier, plan_execution_id, retry_stages, identifier, **kwargs):  # noqa: E501
        """Retry a executed pipeline with inputSet pipeline yaml  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retry_pipeline_with_http_info(account_identifier, org_identifier, project_identifier, plan_execution_id, retry_stages, identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity. (required)
        :param str project_identifier: Project Identifier for the Entity. (required)
        :param str plan_execution_id: This param contains the previous execution execution id. This is basically when we are rerunning a Pipeline. (required)
        :param list[str] retry_stages: This param contains the identifier of stages from where to resume. It will be a list if we want to retry from parallel group  (required)
        :param str identifier: Pipeline Identifier (required)
        :param str body:
        :param str module_type: Module type for the entity. If its from deployments,type will be CD , if its from build type will be CI
        :param bool run_all_stages: This param provides an option to run only the failed stages when Pipeline fails at parallel group. By default, it will run all the stages in the failed parallel group.
        :param str notes_for_pipeline_execution: Notes of a pipeline execution
        :return: ResponseDTOPlanExecutionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_identifier', 'org_identifier', 'project_identifier', 'plan_execution_id', 'retry_stages', 'identifier', 'body', 'module_type', 'run_all_stages', 'notes_for_pipeline_execution']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retry_pipeline" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `retry_pipeline`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `retry_pipeline`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `retry_pipeline`")  # noqa: E501
        # verify the required parameter 'plan_execution_id' is set
        if ('plan_execution_id' not in params or
                params['plan_execution_id'] is None):
            raise ValueError("Missing the required parameter `plan_execution_id` when calling `retry_pipeline`")  # noqa: E501
        # verify the required parameter 'retry_stages' is set
        if ('retry_stages' not in params or
                params['retry_stages'] is None):
            raise ValueError("Missing the required parameter `retry_stages` when calling `retry_pipeline`")  # noqa: E501
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `retry_pipeline`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501
        if 'module_type' in params:
            query_params.append(('moduleType', params['module_type']))  # noqa: E501
        if 'plan_execution_id' in params:
            query_params.append(('planExecutionId', params['plan_execution_id']))  # noqa: E501
        if 'retry_stages' in params:
            query_params.append(('retryStages', params['retry_stages']))  # noqa: E501
            collection_formats['retryStages'] = 'multi'  # noqa: E501
        if 'run_all_stages' in params:
            query_params.append(('runAllStages', params['run_all_stages']))  # noqa: E501
        if 'notes_for_pipeline_execution' in params:
            query_params.append(('notesForPipelineExecution', params['notes_for_pipeline_execution']))  # noqa: E501

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
            '/pipeline/api/pipeline/execute/retry/{identifier}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseDTOPlanExecutionResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
