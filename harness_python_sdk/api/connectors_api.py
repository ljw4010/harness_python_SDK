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


class ConnectorsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_connector(self, body, account_identifier, **kwargs):  # noqa: E501
        """Create a Connector  # noqa: E501

        Creates a new Harness Connector.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_connector(body, account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Connector2 body: Details of the Connector to create (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
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
        :return: ResponseDTOConnectorResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_connector_with_http_info(body, account_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.create_connector_with_http_info(body, account_identifier, **kwargs)  # noqa: E501
            return data

    def create_connector_with_http_info(self, body, account_identifier, **kwargs):  # noqa: E501
        """Create a Connector  # noqa: E501

        Creates a new Harness Connector.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_connector_with_http_info(body, account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Connector2 body: Details of the Connector to create (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
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
        :return: ResponseDTOConnectorResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'account_identifier', 'branch', 'repo_identifier', 'root_folder', 'file_path', 'commit_msg', 'is_new_branch', 'base_branch', 'connector_ref', 'store_type', 'repo_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_connector" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_connector`")  # noqa: E501
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `create_connector`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501
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
            ['application/json', 'application/yaml', 'text/yaml', 'text/html'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/yaml', 'text/html', 'text/plain'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/ng/api/connectors', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseDTOConnectorResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_connector(self, account_identifier, identifier, **kwargs):  # noqa: E501
        """Delete a Connector  # noqa: E501

        Deletes a Connector for the given ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_connector(account_identifier, identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str identifier: Connector ID (required)
        :param str org_identifier: Organization Identifier for the Entity.
        :param str project_identifier: Project Identifier for the Entity.
        :param str branch: Name of the branch.
        :param str repo_identifier: Git Sync Config Id.
        :param str root_folder: Path to the root folder of the Entity.
        :param str file_path: File Path of the Entity.
        :param str commit_msg: Commit Message to use for the merge commit.
        :param str last_object_id: Last Object Id
        :param bool force_delete: If true, the Entity will be forced delete, without checking any references/usages
        :return: ResponseDTOBoolean
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_connector_with_http_info(account_identifier, identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_connector_with_http_info(account_identifier, identifier, **kwargs)  # noqa: E501
            return data

    def delete_connector_with_http_info(self, account_identifier, identifier, **kwargs):  # noqa: E501
        """Delete a Connector  # noqa: E501

        Deletes a Connector for the given ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_connector_with_http_info(account_identifier, identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str identifier: Connector ID (required)
        :param str org_identifier: Organization Identifier for the Entity.
        :param str project_identifier: Project Identifier for the Entity.
        :param str branch: Name of the branch.
        :param str repo_identifier: Git Sync Config Id.
        :param str root_folder: Path to the root folder of the Entity.
        :param str file_path: File Path of the Entity.
        :param str commit_msg: Commit Message to use for the merge commit.
        :param str last_object_id: Last Object Id
        :param bool force_delete: If true, the Entity will be forced delete, without checking any references/usages
        :return: ResponseDTOBoolean
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_identifier', 'identifier', 'org_identifier', 'project_identifier', 'branch', 'repo_identifier', 'root_folder', 'file_path', 'commit_msg', 'last_object_id', 'force_delete']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_connector" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `delete_connector`")  # noqa: E501
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `delete_connector`")  # noqa: E501

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
        if 'force_delete' in params:
            query_params.append(('forceDelete', params['force_delete']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/yaml', 'text/yaml', 'text/html'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/ng/api/connectors/{identifier}', 'DELETE',
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

    def get_all_allowed_field_values(self, account_identifier, connector_type, **kwargs):  # noqa: E501
        """List all the configured field values for the given Connector type.  # noqa: E501

        Returns all the configured field values for the given Connector type, which can be used during connector creation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_allowed_field_values(account_identifier, connector_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str connector_type: Connector type (required)
        :return: ResponseDTOFieldValues
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_allowed_field_values_with_http_info(account_identifier, connector_type, **kwargs)  # noqa: E501
        else:
            (data) = self.get_all_allowed_field_values_with_http_info(account_identifier, connector_type, **kwargs)  # noqa: E501
            return data

    def get_all_allowed_field_values_with_http_info(self, account_identifier, connector_type, **kwargs):  # noqa: E501
        """List all the configured field values for the given Connector type.  # noqa: E501

        Returns all the configured field values for the given Connector type, which can be used during connector creation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_allowed_field_values_with_http_info(account_identifier, connector_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str connector_type: Connector type (required)
        :return: ResponseDTOFieldValues
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_identifier', 'connector_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_allowed_field_values" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `get_all_allowed_field_values`")  # noqa: E501
        # verify the required parameter 'connector_type' is set
        if ('connector_type' not in params or
                params['connector_type'] is None):
            raise ValueError("Missing the required parameter `connector_type` when calling `get_all_allowed_field_values`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501
        if 'connector_type' in params:
            query_params.append(('connectorType', params['connector_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/yaml', 'text/yaml', 'text/html'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/ng/api/connectors/fieldValues', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseDTOFieldValues',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_ccmk8_s_connector_list(self, body, account_identifier, **kwargs):  # noqa: E501
        """Fetches the list of CMC K8S Connectors corresponding to the request's filter criteria.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_ccmk8_s_connector_list(body, account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConnectorFilterProperties body: Details of the filters applied (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str search_term: This would be used to filter Connectors. Any Connector having the specified string in its Name, ID and Tag would be filtered.
        :param str org_identifier: Organization Identifier for the Entity.
        :param str project_identifier: Project Identifier for the Entity.
        :param str filter_identifier:
        :param bool include_all_connectors_available_at_scope: Specify whether or not to include all the Connectors accessible at the scope. For eg if set as true, at the Project scope we will get org and account Connector also in the response
        :param str branch: Name of the branch.
        :param str repo_identifier: Git Sync Config Id.
        :param bool get_default_from_other_repo: if true, return all the default entities
        :param bool get_distinct_from_branches: This when set to true along with GitSync enabled for the Connector, you can get one connector entity from each identifier. The connector entity can belong to any branch
        :param int page_index: Page Index of the results to fetch.Default Value: 0
        :param int page_size: Results per page(max 100)Default Value: 50
        :param list[SortOrder] sort_orders: Sort criteria for the elements.
        :param str page_token: Page Token of the next results to fetch.Default Value: ''
        :return: ResponseDTOPageResponseCcmK8sConnectorResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_ccmk8_s_connector_list_with_http_info(body, account_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.get_ccmk8_s_connector_list_with_http_info(body, account_identifier, **kwargs)  # noqa: E501
            return data

    def get_ccmk8_s_connector_list_with_http_info(self, body, account_identifier, **kwargs):  # noqa: E501
        """Fetches the list of CMC K8S Connectors corresponding to the request's filter criteria.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_ccmk8_s_connector_list_with_http_info(body, account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConnectorFilterProperties body: Details of the filters applied (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str search_term: This would be used to filter Connectors. Any Connector having the specified string in its Name, ID and Tag would be filtered.
        :param str org_identifier: Organization Identifier for the Entity.
        :param str project_identifier: Project Identifier for the Entity.
        :param str filter_identifier:
        :param bool include_all_connectors_available_at_scope: Specify whether or not to include all the Connectors accessible at the scope. For eg if set as true, at the Project scope we will get org and account Connector also in the response
        :param str branch: Name of the branch.
        :param str repo_identifier: Git Sync Config Id.
        :param bool get_default_from_other_repo: if true, return all the default entities
        :param bool get_distinct_from_branches: This when set to true along with GitSync enabled for the Connector, you can get one connector entity from each identifier. The connector entity can belong to any branch
        :param int page_index: Page Index of the results to fetch.Default Value: 0
        :param int page_size: Results per page(max 100)Default Value: 50
        :param list[SortOrder] sort_orders: Sort criteria for the elements.
        :param str page_token: Page Token of the next results to fetch.Default Value: ''
        :return: ResponseDTOPageResponseCcmK8sConnectorResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'account_identifier', 'search_term', 'org_identifier', 'project_identifier', 'filter_identifier', 'include_all_connectors_available_at_scope', 'branch', 'repo_identifier', 'get_default_from_other_repo', 'get_distinct_from_branches', 'page_index', 'page_size', 'sort_orders', 'page_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_ccmk8_s_connector_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `get_ccmk8_s_connector_list`")  # noqa: E501
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `get_ccmk8_s_connector_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501
        if 'search_term' in params:
            query_params.append(('searchTerm', params['search_term']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501
        if 'filter_identifier' in params:
            query_params.append(('filterIdentifier', params['filter_identifier']))  # noqa: E501
        if 'include_all_connectors_available_at_scope' in params:
            query_params.append(('includeAllConnectorsAvailableAtScope', params['include_all_connectors_available_at_scope']))  # noqa: E501
        if 'branch' in params:
            query_params.append(('branch', params['branch']))  # noqa: E501
        if 'repo_identifier' in params:
            query_params.append(('repoIdentifier', params['repo_identifier']))  # noqa: E501
        if 'get_default_from_other_repo' in params:
            query_params.append(('getDefaultFromOtherRepo', params['get_default_from_other_repo']))  # noqa: E501
        if 'get_distinct_from_branches' in params:
            query_params.append(('getDistinctFromBranches', params['get_distinct_from_branches']))  # noqa: E501
        if 'page_index' in params:
            query_params.append(('pageIndex', params['page_index']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501
        if 'sort_orders' in params:
            query_params.append(('sortOrders', params['sort_orders']))  # noqa: E501
            collection_formats['sortOrders'] = 'multi'  # noqa: E501
        if 'page_token' in params:
            query_params.append(('pageToken', params['page_token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/yaml', 'text/yaml', 'text/html'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/yaml', 'text/html', 'text/plain'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/ng/api/connectors/ccmK8sList', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseDTOPageResponseCcmK8sConnectorResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_ce_aws_template(self, **kwargs):  # noqa: E501
        """Get the Template URL of connector  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_ce_aws_template(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool events_enabled: Specify whether or not to enable events
        :param bool cur_enabled: Specify whether or not to enable CUR
        :param bool optimization_enabled: Specify whether or not to enable optimization
        :return: ResponseDTOString
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_ce_aws_template_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_ce_aws_template_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_ce_aws_template_with_http_info(self, **kwargs):  # noqa: E501
        """Get the Template URL of connector  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_ce_aws_template_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool events_enabled: Specify whether or not to enable events
        :param bool cur_enabled: Specify whether or not to enable CUR
        :param bool optimization_enabled: Specify whether or not to enable optimization
        :return: ResponseDTOString
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['events_enabled', 'cur_enabled', 'optimization_enabled']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_ce_aws_template" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'events_enabled' in params:
            query_params.append(('eventsEnabled', params['events_enabled']))  # noqa: E501
        if 'cur_enabled' in params:
            query_params.append(('curEnabled', params['cur_enabled']))  # noqa: E501
        if 'optimization_enabled' in params:
            query_params.append(('optimizationEnabled', params['optimization_enabled']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/yaml', 'text/yaml', 'text/html'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/ng/api/connectors/getceawstemplateurl', 'POST',
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

    def get_connector(self, account_identifier, identifier, **kwargs):  # noqa: E501
        """Return Connector details  # noqa: E501

        Returns the Connector's details for the given Account and Connector ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_connector(account_identifier, identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str identifier: Connector Identifier (required)
        :param str org_identifier: Organization Identifier for the Entity.
        :param str project_identifier: Project Identifier for the Entity.
        :param str branch: Name of the branch.
        :param str repo_identifier: Git Sync Config Id.
        :param bool get_default_from_other_repo: if true, return all the default entities
        :return: ResponseDTOConnectorResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_connector_with_http_info(account_identifier, identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.get_connector_with_http_info(account_identifier, identifier, **kwargs)  # noqa: E501
            return data

    def get_connector_with_http_info(self, account_identifier, identifier, **kwargs):  # noqa: E501
        """Return Connector details  # noqa: E501

        Returns the Connector's details for the given Account and Connector ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_connector_with_http_info(account_identifier, identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str identifier: Connector Identifier (required)
        :param str org_identifier: Organization Identifier for the Entity.
        :param str project_identifier: Project Identifier for the Entity.
        :param str branch: Name of the branch.
        :param str repo_identifier: Git Sync Config Id.
        :param bool get_default_from_other_repo: if true, return all the default entities
        :return: ResponseDTOConnectorResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_identifier', 'identifier', 'org_identifier', 'project_identifier', 'branch', 'repo_identifier', 'get_default_from_other_repo']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_connector" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `get_connector`")  # noqa: E501
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `get_connector`")  # noqa: E501

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
            ['application/json', 'application/yaml', 'text/yaml', 'text/html'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/ng/api/connectors/{identifier}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseDTOConnectorResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_connector_catalogue(self, account_identifier, **kwargs):  # noqa: E501
        """Lists all Connectors for an account  # noqa: E501

        Lists all the Connectors for the given Account ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_connector_catalogue(account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :return: ResponseDTOConnectorCatalogueResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_connector_catalogue_with_http_info(account_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.get_connector_catalogue_with_http_info(account_identifier, **kwargs)  # noqa: E501
            return data

    def get_connector_catalogue_with_http_info(self, account_identifier, **kwargs):  # noqa: E501
        """Lists all Connectors for an account  # noqa: E501

        Lists all the Connectors for the given Account ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_connector_catalogue_with_http_info(account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :return: ResponseDTOConnectorCatalogueResponse
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
                    " to method get_connector_catalogue" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `get_connector_catalogue`")  # noqa: E501

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
            ['application/json', 'application/yaml', 'text/yaml', 'text/html'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/ng/api/connectors/catalogue', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseDTOConnectorCatalogueResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_connector_list(self, account_identifier, **kwargs):  # noqa: E501
        """List all Connectors using filters  # noqa: E501

        Lists all the Connectors matching the specified filters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_connector_list(account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param int page_index: Page number of navigation. By default, it is set to 0.
        :param int page_size: Number of entries per page.The default number of entries per page is 100, while the maximum number allowed is 1000.
        :param str org_identifier: Organization Identifier for the Entity.
        :param str project_identifier: Project Identifier for the Entity.
        :param str search_term: This would be used to filter Connectors. Any Connector having the specified string in its Name, ID and Tag would be filtered.
        :param str type: Filter Connectors by type
        :param str category: Filter Connectors by category
        :param str source_category: Filter Connectors by Source Category. Available Source Categories are CLOUD_PROVIDER, SECRET_MANAGER, CLOUD_COST, ARTIFACTORY, CODE_REPO,  MONITORING and TICKETING
        :param str version:
        :param str branch: Name of the branch.
        :param str repo_identifier: Git Sync Config Id.
        :param bool get_default_from_other_repo: if true, return all the default entities
        :return: ResponseDTOPageResponseConnectorResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_connector_list_with_http_info(account_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.get_connector_list_with_http_info(account_identifier, **kwargs)  # noqa: E501
            return data

    def get_connector_list_with_http_info(self, account_identifier, **kwargs):  # noqa: E501
        """List all Connectors using filters  # noqa: E501

        Lists all the Connectors matching the specified filters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_connector_list_with_http_info(account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param int page_index: Page number of navigation. By default, it is set to 0.
        :param int page_size: Number of entries per page.The default number of entries per page is 100, while the maximum number allowed is 1000.
        :param str org_identifier: Organization Identifier for the Entity.
        :param str project_identifier: Project Identifier for the Entity.
        :param str search_term: This would be used to filter Connectors. Any Connector having the specified string in its Name, ID and Tag would be filtered.
        :param str type: Filter Connectors by type
        :param str category: Filter Connectors by category
        :param str source_category: Filter Connectors by Source Category. Available Source Categories are CLOUD_PROVIDER, SECRET_MANAGER, CLOUD_COST, ARTIFACTORY, CODE_REPO,  MONITORING and TICKETING
        :param str version:
        :param str branch: Name of the branch.
        :param str repo_identifier: Git Sync Config Id.
        :param bool get_default_from_other_repo: if true, return all the default entities
        :return: ResponseDTOPageResponseConnectorResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_identifier', 'page_index', 'page_size', 'org_identifier', 'project_identifier', 'search_term', 'type', 'category', 'source_category', 'version', 'branch', 'repo_identifier', 'get_default_from_other_repo']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_connector_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `get_connector_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page_index' in params:
            query_params.append(('pageIndex', params['page_index']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501
        if 'search_term' in params:
            query_params.append(('searchTerm', params['search_term']))  # noqa: E501
        if 'type' in params:
            query_params.append(('type', params['type']))  # noqa: E501
        if 'category' in params:
            query_params.append(('category', params['category']))  # noqa: E501
        if 'source_category' in params:
            query_params.append(('source_category', params['source_category']))  # noqa: E501
        if 'version' in params:
            query_params.append(('version', params['version']))  # noqa: E501
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
            ['application/json', 'application/yaml', 'text/yaml', 'text/html'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/ng/api/connectors', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseDTOPageResponseConnectorResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_connector_list_v2(self, body, account_identifier, **kwargs):  # noqa: E501
        """Fetches the list of Connectors corresponding to the request's filter criteria.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_connector_list_v2(body, account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConnectorFilterProperties body: Details of the filters applied (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str search_term: This would be used to filter Connectors. Any Connector having the specified string in its Name, ID and Tag would be filtered.
        :param str org_identifier: Organization Identifier for the Entity.
        :param str project_identifier: Project Identifier for the Entity.
        :param str filter_identifier:
        :param bool include_all_connectors_available_at_scope: Specify whether or not to include all the Connectors accessible at the scope. For eg if set as true, at the Project scope we will get org and account Connector also in the response
        :param str branch: Name of the branch.
        :param str repo_identifier: Git Sync Config Id.
        :param bool get_default_from_other_repo: if true, return all the default entities
        :param bool get_distinct_from_branches: This when set to true along with GitSync enabled for the Connector, you can get one connector entity from each identifier. The connector entity can belong to any branch
        :param str version:
        :param bool only_favorites:
        :param int page_index: Page Index of the results to fetch.Default Value: 0
        :param int page_size: Results per page(max 100)Default Value: 50
        :param list[SortOrder] sort_orders: Sort criteria for the elements.
        :param str page_token: Page Token of the next results to fetch.Default Value: ''
        :return: ResponseDTOPageResponseConnectorResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_connector_list_v2_with_http_info(body, account_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.get_connector_list_v2_with_http_info(body, account_identifier, **kwargs)  # noqa: E501
            return data

    def get_connector_list_v2_with_http_info(self, body, account_identifier, **kwargs):  # noqa: E501
        """Fetches the list of Connectors corresponding to the request's filter criteria.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_connector_list_v2_with_http_info(body, account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConnectorFilterProperties body: Details of the filters applied (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str search_term: This would be used to filter Connectors. Any Connector having the specified string in its Name, ID and Tag would be filtered.
        :param str org_identifier: Organization Identifier for the Entity.
        :param str project_identifier: Project Identifier for the Entity.
        :param str filter_identifier:
        :param bool include_all_connectors_available_at_scope: Specify whether or not to include all the Connectors accessible at the scope. For eg if set as true, at the Project scope we will get org and account Connector also in the response
        :param str branch: Name of the branch.
        :param str repo_identifier: Git Sync Config Id.
        :param bool get_default_from_other_repo: if true, return all the default entities
        :param bool get_distinct_from_branches: This when set to true along with GitSync enabled for the Connector, you can get one connector entity from each identifier. The connector entity can belong to any branch
        :param str version:
        :param bool only_favorites:
        :param int page_index: Page Index of the results to fetch.Default Value: 0
        :param int page_size: Results per page(max 100)Default Value: 50
        :param list[SortOrder] sort_orders: Sort criteria for the elements.
        :param str page_token: Page Token of the next results to fetch.Default Value: ''
        :return: ResponseDTOPageResponseConnectorResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'account_identifier', 'search_term', 'org_identifier', 'project_identifier', 'filter_identifier', 'include_all_connectors_available_at_scope', 'branch', 'repo_identifier', 'get_default_from_other_repo', 'get_distinct_from_branches', 'version', 'only_favorites', 'page_index', 'page_size', 'sort_orders', 'page_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_connector_list_v2" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `get_connector_list_v2`")  # noqa: E501
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `get_connector_list_v2`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501
        if 'search_term' in params:
            query_params.append(('searchTerm', params['search_term']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501
        if 'filter_identifier' in params:
            query_params.append(('filterIdentifier', params['filter_identifier']))  # noqa: E501
        if 'include_all_connectors_available_at_scope' in params:
            query_params.append(('includeAllConnectorsAvailableAtScope', params['include_all_connectors_available_at_scope']))  # noqa: E501
        if 'branch' in params:
            query_params.append(('branch', params['branch']))  # noqa: E501
        if 'repo_identifier' in params:
            query_params.append(('repoIdentifier', params['repo_identifier']))  # noqa: E501
        if 'get_default_from_other_repo' in params:
            query_params.append(('getDefaultFromOtherRepo', params['get_default_from_other_repo']))  # noqa: E501
        if 'get_distinct_from_branches' in params:
            query_params.append(('getDistinctFromBranches', params['get_distinct_from_branches']))  # noqa: E501
        if 'version' in params:
            query_params.append(('version', params['version']))  # noqa: E501
        if 'only_favorites' in params:
            query_params.append(('onlyFavorites', params['only_favorites']))  # noqa: E501
        if 'page_index' in params:
            query_params.append(('pageIndex', params['page_index']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501
        if 'sort_orders' in params:
            query_params.append(('sortOrders', params['sort_orders']))  # noqa: E501
            collection_formats['sortOrders'] = 'multi'  # noqa: E501
        if 'page_token' in params:
            query_params.append(('pageToken', params['page_token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/yaml', 'text/yaml', 'text/html'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/yaml', 'text/html', 'text/plain'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/ng/api/connectors/listV2', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseDTOPageResponseConnectorResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_connector_statistics(self, account_identifier, **kwargs):  # noqa: E501
        """Gets the connector's statistics by Account Identifier, Project Identifier and Organization Identifier  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_connector_statistics(account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity.
        :param str project_identifier: Project Identifier for the Entity.
        :param str branch: Name of the branch.
        :param str repo_identifier: Git Sync Config Id.
        :param bool get_default_from_other_repo: if true, return all the default entities
        :return: ResponseDTOConnectorStatistics
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_connector_statistics_with_http_info(account_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.get_connector_statistics_with_http_info(account_identifier, **kwargs)  # noqa: E501
            return data

    def get_connector_statistics_with_http_info(self, account_identifier, **kwargs):  # noqa: E501
        """Gets the connector's statistics by Account Identifier, Project Identifier and Organization Identifier  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_connector_statistics_with_http_info(account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity.
        :param str project_identifier: Project Identifier for the Entity.
        :param str branch: Name of the branch.
        :param str repo_identifier: Git Sync Config Id.
        :param bool get_default_from_other_repo: if true, return all the default entities
        :return: ResponseDTOConnectorStatistics
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_identifier', 'org_identifier', 'project_identifier', 'branch', 'repo_identifier', 'get_default_from_other_repo']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_connector_statistics" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `get_connector_statistics`")  # noqa: E501

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
        if 'get_default_from_other_repo' in params:
            query_params.append(('getDefaultFromOtherRepo', params['get_default_from_other_repo']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/yaml', 'text/yaml', 'text/html'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/ng/api/connectors/stats', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseDTOConnectorStatistics',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_test_connection_result(self, account_identifier, identifier, **kwargs):  # noqa: E501
        """Test Harness Connector connection with third-party tool  # noqa: E501

        Tests if a Harness Connector can successfully connect Harness to a third-party tool.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_test_connection_result(account_identifier, identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str identifier: Connector ID (required)
        :param str org_identifier: Organization Identifier for the Entity.
        :param str project_identifier: Project Identifier for the Entity.
        :param str branch: Name of the branch.
        :param str repo_identifier: Git Sync Config Id.
        :param bool get_default_from_other_repo: if true, return all the default entities
        :return: ResponseDTOConnectorValidationResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_test_connection_result_with_http_info(account_identifier, identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.get_test_connection_result_with_http_info(account_identifier, identifier, **kwargs)  # noqa: E501
            return data

    def get_test_connection_result_with_http_info(self, account_identifier, identifier, **kwargs):  # noqa: E501
        """Test Harness Connector connection with third-party tool  # noqa: E501

        Tests if a Harness Connector can successfully connect Harness to a third-party tool.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_test_connection_result_with_http_info(account_identifier, identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str identifier: Connector ID (required)
        :param str org_identifier: Organization Identifier for the Entity.
        :param str project_identifier: Project Identifier for the Entity.
        :param str branch: Name of the branch.
        :param str repo_identifier: Git Sync Config Id.
        :param bool get_default_from_other_repo: if true, return all the default entities
        :return: ResponseDTOConnectorValidationResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_identifier', 'identifier', 'org_identifier', 'project_identifier', 'branch', 'repo_identifier', 'get_default_from_other_repo']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_test_connection_result" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `get_test_connection_result`")  # noqa: E501
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `get_test_connection_result`")  # noqa: E501

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
            ['application/json', 'application/yaml', 'text/yaml', 'text/html'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/ng/api/connectors/testConnection/{identifier}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseDTOConnectorValidationResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_test_git_repo_connection_result(self, account_identifier, identifier, **kwargs):  # noqa: E501
        """Test Git Connector sync with repo  # noqa: E501

        Tests if a Git Repo Connector can successfully connect Harness to a Git provider.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_test_git_repo_connection_result(account_identifier, identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str identifier: Connector ID (required)
        :param str org_identifier: Organization Identifier for the Entity.
        :param str project_identifier: Project Identifier for the Entity.
        :param str repo_url: URL of the repository, specify only in the case of Account Type Git Connector
        :return: ResponseDTOConnectorValidationResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_test_git_repo_connection_result_with_http_info(account_identifier, identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.get_test_git_repo_connection_result_with_http_info(account_identifier, identifier, **kwargs)  # noqa: E501
            return data

    def get_test_git_repo_connection_result_with_http_info(self, account_identifier, identifier, **kwargs):  # noqa: E501
        """Test Git Connector sync with repo  # noqa: E501

        Tests if a Git Repo Connector can successfully connect Harness to a Git provider.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_test_git_repo_connection_result_with_http_info(account_identifier, identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str identifier: Connector ID (required)
        :param str org_identifier: Organization Identifier for the Entity.
        :param str project_identifier: Project Identifier for the Entity.
        :param str repo_url: URL of the repository, specify only in the case of Account Type Git Connector
        :return: ResponseDTOConnectorValidationResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_identifier', 'identifier', 'org_identifier', 'project_identifier', 'repo_url']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_test_git_repo_connection_result" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `get_test_git_repo_connection_result`")  # noqa: E501
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `get_test_git_repo_connection_result`")  # noqa: E501

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
        if 'repo_url' in params:
            query_params.append(('repoURL', params['repo_url']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/yaml', 'text/yaml', 'text/html'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/ng/api/connectors/testGitRepoConnection/{identifier}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseDTOConnectorValidationResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_connector_by_fqn(self, body, account_identifier, **kwargs):  # noqa: E501
        """Get list of Connectors by FQN  # noqa: E501

        Lists all Connectors for an Account by Fully Qualified Name (FQN).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_connector_by_fqn(body, account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] body: A list of connectors' FQNs as strings. A maximum of 1000 characters is allowed. (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :return: ResponseDTOListConnectorResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_connector_by_fqn_with_http_info(body, account_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.list_connector_by_fqn_with_http_info(body, account_identifier, **kwargs)  # noqa: E501
            return data

    def list_connector_by_fqn_with_http_info(self, body, account_identifier, **kwargs):  # noqa: E501
        """Get list of Connectors by FQN  # noqa: E501

        Lists all Connectors for an Account by Fully Qualified Name (FQN).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_connector_by_fqn_with_http_info(body, account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] body: A list of connectors' FQNs as strings. A maximum of 1000 characters is allowed. (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
        :return: ResponseDTOListConnectorResponse
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
                    " to method list_connector_by_fqn" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `list_connector_by_fqn`")  # noqa: E501
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `list_connector_by_fqn`")  # noqa: E501

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
            ['application/json', 'application/yaml', 'text/yaml', 'text/html'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/yaml', 'text/html', 'text/plain'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/ng/api/connectors/listbyfqn', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseDTOListConnectorResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_connector(self, body, account_identifier, **kwargs):  # noqa: E501
        """Update a Connector  # noqa: E501

        Updates a Connector for the given ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_connector(body, account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Connector2 body: This is the updated Connector. Please provide values for all fields, not just the fields you are updating (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
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
        :return: ResponseDTOConnectorResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_connector_with_http_info(body, account_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.update_connector_with_http_info(body, account_identifier, **kwargs)  # noqa: E501
            return data

    def update_connector_with_http_info(self, body, account_identifier, **kwargs):  # noqa: E501
        """Update a Connector  # noqa: E501

        Updates a Connector for the given ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_connector_with_http_info(body, account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Connector2 body: This is the updated Connector. Please provide values for all fields, not just the fields you are updating (required)
        :param str account_identifier: Account Identifier for the Entity. (required)
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
        :return: ResponseDTOConnectorResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'account_identifier', 'branch', 'repo_identifier', 'root_folder', 'file_path', 'commit_msg', 'last_object_id', 'resolved_conflict_commit_id', 'base_branch', 'connector_ref', 'is_new_branch']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_connector" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_connector`")  # noqa: E501
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `update_connector`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501
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

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/yaml', 'text/yaml', 'text/html'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/yaml', 'text/html', 'text/plain'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/ng/api/connectors', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseDTOConnectorResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def validate_the_identifier_is_unique(self, account_identifier, **kwargs):  # noqa: E501
        """Test a Harness Connector  # noqa: E501

        Tests if a Connector can successfully connect Harness to a third-party tool using the an Account and Connector ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.validate_the_identifier_is_unique(account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity.
        :param str project_identifier: Project Identifier for the Entity.
        :param str identifier: Connector ID
        :return: ResponseDTOBoolean
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.validate_the_identifier_is_unique_with_http_info(account_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.validate_the_identifier_is_unique_with_http_info(account_identifier, **kwargs)  # noqa: E501
            return data

    def validate_the_identifier_is_unique_with_http_info(self, account_identifier, **kwargs):  # noqa: E501
        """Test a Harness Connector  # noqa: E501

        Tests if a Connector can successfully connect Harness to a third-party tool using the an Account and Connector ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.validate_the_identifier_is_unique_with_http_info(account_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier for the Entity. (required)
        :param str org_identifier: Organization Identifier for the Entity.
        :param str project_identifier: Project Identifier for the Entity.
        :param str identifier: Connector ID
        :return: ResponseDTOBoolean
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_identifier', 'org_identifier', 'project_identifier', 'identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method validate_the_identifier_is_unique" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `validate_the_identifier_is_unique`")  # noqa: E501

        collection_formats = {}

        path_params = {}

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
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/yaml', 'text/yaml', 'text/html'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/ng/api/connectors/validateUniqueIdentifier', 'GET',
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
