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


class FeatureFlagsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_feature_flag(self, account_identifier, org_identifier, **kwargs):  # noqa: E501
        """Creates a Feature Flag  # noqa: E501

        Creates a Feature Flag in the Project  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_feature_flag(account_identifier, org_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier (required)
        :param str org_identifier: Organization Identifier (required)
        :param object body:
        :return: FeatureResponseMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_feature_flag_with_http_info(account_identifier, org_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.create_feature_flag_with_http_info(account_identifier, org_identifier, **kwargs)  # noqa: E501
            return data

    def create_feature_flag_with_http_info(self, account_identifier, org_identifier, **kwargs):  # noqa: E501
        """Creates a Feature Flag  # noqa: E501

        Creates a Feature Flag in the Project  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_feature_flag_with_http_info(account_identifier, org_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier (required)
        :param str org_identifier: Organization Identifier (required)
        :param object body:
        :return: FeatureResponseMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_identifier', 'org_identifier', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_feature_flag" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `create_feature_flag`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `create_feature_flag`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501

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
            '/cf/admin/features', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FeatureResponseMetadata',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_feature_flag(self, identifier, account_identifier, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """Delete a Feature Flag  # noqa: E501

        Delete Feature Flag for the given identifier and account ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_feature_flag(identifier, account_identifier, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: Unique identifier for the object in the API. (required)
        :param str account_identifier: Account Identifier (required)
        :param str org_identifier: Organization Identifier (required)
        :param str project_identifier: The Project identifier (required)
        :param str commit_msg: Git commit message
        :param bool force_delete: Permanently deletes the the feature flag
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_feature_flag_with_http_info(identifier, account_identifier, org_identifier, project_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_feature_flag_with_http_info(identifier, account_identifier, org_identifier, project_identifier, **kwargs)  # noqa: E501
            return data

    def delete_feature_flag_with_http_info(self, identifier, account_identifier, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """Delete a Feature Flag  # noqa: E501

        Delete Feature Flag for the given identifier and account ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_feature_flag_with_http_info(identifier, account_identifier, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: Unique identifier for the object in the API. (required)
        :param str account_identifier: Account Identifier (required)
        :param str org_identifier: Organization Identifier (required)
        :param str project_identifier: The Project identifier (required)
        :param str commit_msg: Git commit message
        :param bool force_delete: Permanently deletes the the feature flag
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['identifier', 'account_identifier', 'org_identifier', 'project_identifier', 'commit_msg', 'force_delete']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_feature_flag" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `delete_feature_flag`")  # noqa: E501
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `delete_feature_flag`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `delete_feature_flag`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `delete_feature_flag`")  # noqa: E501

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
        if 'commit_msg' in params:
            query_params.append(('commitMsg', params['commit_msg']))  # noqa: E501
        if 'force_delete' in params:
            query_params.append(('forceDelete', params['force_delete']))  # noqa: E501

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
            '/cf/admin/features/{identifier}', 'DELETE',
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

    def get_all_features(self, account_identifier, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """Returns all Feature Flags for the project  # noqa: E501

        Returns all the Feature Flag details for the given project  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_features(account_identifier, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier (required)
        :param str org_identifier: Organization Identifier (required)
        :param str project_identifier: The Project identifier (required)
        :param str environment_identifier: Environment
        :param int page_number: PageNumber
        :param int page_size: PageSize
        :param str sort_order: SortOrder
        :param str sort_by_field: SortByField
        :param str name: Name of the field
        :param str identifier: Identifier of the field
        :param bool archived: Status of the feature flag
        :param str kind: Kind of the feature flag
        :param str target_identifier: Identifier of a target
        :param str target_identifier_filter: Identifier of the target to filter on
        :param bool metrics: Parameter to indicate if metrics data is requested in response
        :param str feature_identifiers: Comma separated identifiers for multiple Features
        :param str excluded_features: Comma separated identifiers to exclude from the response
        :param str status: Filter for flags based on their status (active,never-requested,recently-accessed,potentially-stale)
        :param str lifetime: Filter for flags based on their lifetime (permanent/temporary)
        :param bool enabled: Filter for flags based on if they are enabled or disabled
        :param bool flag_counts: Returns counts for the different types of flags e.g num active, potentially-stale, recently-accessed etc
        :param bool summary: Returns summary info on flags if set to true
        :param str tags: Filter for flags based on their tag values supplied as comma separated list
        :return: Features
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_features_with_http_info(account_identifier, org_identifier, project_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.get_all_features_with_http_info(account_identifier, org_identifier, project_identifier, **kwargs)  # noqa: E501
            return data

    def get_all_features_with_http_info(self, account_identifier, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """Returns all Feature Flags for the project  # noqa: E501

        Returns all the Feature Flag details for the given project  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_features_with_http_info(account_identifier, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier (required)
        :param str org_identifier: Organization Identifier (required)
        :param str project_identifier: The Project identifier (required)
        :param str environment_identifier: Environment
        :param int page_number: PageNumber
        :param int page_size: PageSize
        :param str sort_order: SortOrder
        :param str sort_by_field: SortByField
        :param str name: Name of the field
        :param str identifier: Identifier of the field
        :param bool archived: Status of the feature flag
        :param str kind: Kind of the feature flag
        :param str target_identifier: Identifier of a target
        :param str target_identifier_filter: Identifier of the target to filter on
        :param bool metrics: Parameter to indicate if metrics data is requested in response
        :param str feature_identifiers: Comma separated identifiers for multiple Features
        :param str excluded_features: Comma separated identifiers to exclude from the response
        :param str status: Filter for flags based on their status (active,never-requested,recently-accessed,potentially-stale)
        :param str lifetime: Filter for flags based on their lifetime (permanent/temporary)
        :param bool enabled: Filter for flags based on if they are enabled or disabled
        :param bool flag_counts: Returns counts for the different types of flags e.g num active, potentially-stale, recently-accessed etc
        :param bool summary: Returns summary info on flags if set to true
        :param str tags: Filter for flags based on their tag values supplied as comma separated list
        :return: Features
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_identifier', 'org_identifier', 'project_identifier', 'environment_identifier', 'page_number', 'page_size', 'sort_order', 'sort_by_field', 'name', 'identifier', 'archived', 'kind', 'target_identifier', 'target_identifier_filter', 'metrics', 'feature_identifiers', 'excluded_features', 'status', 'lifetime', 'enabled', 'flag_counts', 'summary', 'tags']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_features" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `get_all_features`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `get_all_features`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `get_all_features`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'account_identifier' in params:
            query_params.append(('accountIdentifier', params['account_identifier']))  # noqa: E501
        if 'org_identifier' in params:
            query_params.append(('orgIdentifier', params['org_identifier']))  # noqa: E501
        if 'project_identifier' in params:
            query_params.append(('projectIdentifier', params['project_identifier']))  # noqa: E501
        if 'environment_identifier' in params:
            query_params.append(('environmentIdentifier', params['environment_identifier']))  # noqa: E501
        if 'page_number' in params:
            query_params.append(('pageNumber', params['page_number']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501
        if 'sort_order' in params:
            query_params.append(('sortOrder', params['sort_order']))  # noqa: E501
        if 'sort_by_field' in params:
            query_params.append(('sortByField', params['sort_by_field']))  # noqa: E501
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501
        if 'identifier' in params:
            query_params.append(('identifier', params['identifier']))  # noqa: E501
        if 'archived' in params:
            query_params.append(('archived', params['archived']))  # noqa: E501
        if 'kind' in params:
            query_params.append(('kind', params['kind']))  # noqa: E501
        if 'target_identifier' in params:
            query_params.append(('targetIdentifier', params['target_identifier']))  # noqa: E501
        if 'target_identifier_filter' in params:
            query_params.append(('targetIdentifierFilter', params['target_identifier_filter']))  # noqa: E501
        if 'metrics' in params:
            query_params.append(('metrics', params['metrics']))  # noqa: E501
        if 'feature_identifiers' in params:
            query_params.append(('featureIdentifiers', params['feature_identifiers']))  # noqa: E501
        if 'excluded_features' in params:
            query_params.append(('excludedFeatures', params['excluded_features']))  # noqa: E501
        if 'status' in params:
            query_params.append(('status', params['status']))  # noqa: E501
        if 'lifetime' in params:
            query_params.append(('lifetime', params['lifetime']))  # noqa: E501
        if 'enabled' in params:
            query_params.append(('enabled', params['enabled']))  # noqa: E501
        if 'flag_counts' in params:
            query_params.append(('flagCounts', params['flag_counts']))  # noqa: E501
        if 'summary' in params:
            query_params.append(('summary', params['summary']))  # noqa: E501
        if 'tags' in params:
            query_params.append(('tags', params['tags']))  # noqa: E501

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
            '/cf/admin/features', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Features',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_dependent_features(self, identifier, account_identifier, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """Return a list of dependant flags  # noqa: E501

        Given identifier return list all the flags which depend on it.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dependent_features(identifier, account_identifier, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: Unique identifier for the object in the API. (required)
        :param str account_identifier: Account Identifier (required)
        :param str org_identifier: Organization Identifier (required)
        :param str project_identifier: The Project identifier (required)
        :param str environment_identifier: Environment
        :param int page_number: PageNumber
        :param int page_size: PageSize
        :param str sort_order: SortOrder
        :param str sort_by_field: SortByField
        :param str name: Name of the field
        :param bool archived: Status of the feature flag
        :param str kind: Kind of the feature flag
        :param str target_identifier: Identifier of a target
        :param str target_identifier_filter: Identifier of the target to filter on
        :param bool metrics: Parameter to indicate if metrics data is requested in response
        :param str feature_identifiers: Comma separated identifiers for multiple Features
        :param str excluded_features: Comma separated identifiers to exclude from the response
        :param str status: Filter for flags based on their status (active,never-requested,recently-accessed,potentially-stale)
        :param str lifetime: Filter for flags based on their lifetime (permanent/temporary)
        :param bool enabled: Filter for flags based on if they are enabled or disabled
        :param bool flag_counts: Returns counts for the different types of flags e.g num active, potentially-stale, recently-accessed etc
        :param bool summary: Returns summary info on flags if set to true
        :param str tags: Filter for flags based on their tag values supplied as comma separated list
        :return: Features
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_dependent_features_with_http_info(identifier, account_identifier, org_identifier, project_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.get_dependent_features_with_http_info(identifier, account_identifier, org_identifier, project_identifier, **kwargs)  # noqa: E501
            return data

    def get_dependent_features_with_http_info(self, identifier, account_identifier, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """Return a list of dependant flags  # noqa: E501

        Given identifier return list all the flags which depend on it.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dependent_features_with_http_info(identifier, account_identifier, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: Unique identifier for the object in the API. (required)
        :param str account_identifier: Account Identifier (required)
        :param str org_identifier: Organization Identifier (required)
        :param str project_identifier: The Project identifier (required)
        :param str environment_identifier: Environment
        :param int page_number: PageNumber
        :param int page_size: PageSize
        :param str sort_order: SortOrder
        :param str sort_by_field: SortByField
        :param str name: Name of the field
        :param bool archived: Status of the feature flag
        :param str kind: Kind of the feature flag
        :param str target_identifier: Identifier of a target
        :param str target_identifier_filter: Identifier of the target to filter on
        :param bool metrics: Parameter to indicate if metrics data is requested in response
        :param str feature_identifiers: Comma separated identifiers for multiple Features
        :param str excluded_features: Comma separated identifiers to exclude from the response
        :param str status: Filter for flags based on their status (active,never-requested,recently-accessed,potentially-stale)
        :param str lifetime: Filter for flags based on their lifetime (permanent/temporary)
        :param bool enabled: Filter for flags based on if they are enabled or disabled
        :param bool flag_counts: Returns counts for the different types of flags e.g num active, potentially-stale, recently-accessed etc
        :param bool summary: Returns summary info on flags if set to true
        :param str tags: Filter for flags based on their tag values supplied as comma separated list
        :return: Features
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['identifier', 'account_identifier', 'org_identifier', 'project_identifier', 'environment_identifier', 'page_number', 'page_size', 'sort_order', 'sort_by_field', 'name', 'archived', 'kind', 'target_identifier', 'target_identifier_filter', 'metrics', 'feature_identifiers', 'excluded_features', 'status', 'lifetime', 'enabled', 'flag_counts', 'summary', 'tags']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dependent_features" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `get_dependent_features`")  # noqa: E501
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `get_dependent_features`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `get_dependent_features`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `get_dependent_features`")  # noqa: E501

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
        if 'environment_identifier' in params:
            query_params.append(('environmentIdentifier', params['environment_identifier']))  # noqa: E501
        if 'page_number' in params:
            query_params.append(('pageNumber', params['page_number']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501
        if 'sort_order' in params:
            query_params.append(('sortOrder', params['sort_order']))  # noqa: E501
        if 'sort_by_field' in params:
            query_params.append(('sortByField', params['sort_by_field']))  # noqa: E501
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501
        if 'archived' in params:
            query_params.append(('archived', params['archived']))  # noqa: E501
        if 'kind' in params:
            query_params.append(('kind', params['kind']))  # noqa: E501
        if 'target_identifier' in params:
            query_params.append(('targetIdentifier', params['target_identifier']))  # noqa: E501
        if 'target_identifier_filter' in params:
            query_params.append(('targetIdentifierFilter', params['target_identifier_filter']))  # noqa: E501
        if 'metrics' in params:
            query_params.append(('metrics', params['metrics']))  # noqa: E501
        if 'feature_identifiers' in params:
            query_params.append(('featureIdentifiers', params['feature_identifiers']))  # noqa: E501
        if 'excluded_features' in params:
            query_params.append(('excludedFeatures', params['excluded_features']))  # noqa: E501
        if 'status' in params:
            query_params.append(('status', params['status']))  # noqa: E501
        if 'lifetime' in params:
            query_params.append(('lifetime', params['lifetime']))  # noqa: E501
        if 'enabled' in params:
            query_params.append(('enabled', params['enabled']))  # noqa: E501
        if 'flag_counts' in params:
            query_params.append(('flagCounts', params['flag_counts']))  # noqa: E501
        if 'summary' in params:
            query_params.append(('summary', params['summary']))  # noqa: E501
        if 'tags' in params:
            query_params.append(('tags', params['tags']))  # noqa: E501

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
            '/cf/admin/features/{identifier}/dependants', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Features',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_feature_flag(self, identifier, account_identifier, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """Returns a Feature Flag  # noqa: E501

        Returns details such as Variation name, identifier etc for the given Feature Flag  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_feature_flag(identifier, account_identifier, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: Unique identifier for the object in the API. (required)
        :param str account_identifier: Account Identifier (required)
        :param str org_identifier: Organization Identifier (required)
        :param str project_identifier: The Project identifier (required)
        :param str environment_identifier: Environment
        :param bool metrics: Parameter to indicate if metrics data is requested in response
        :param bool archived: Status of the feature flag
        :return: Feature
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_feature_flag_with_http_info(identifier, account_identifier, org_identifier, project_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.get_feature_flag_with_http_info(identifier, account_identifier, org_identifier, project_identifier, **kwargs)  # noqa: E501
            return data

    def get_feature_flag_with_http_info(self, identifier, account_identifier, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """Returns a Feature Flag  # noqa: E501

        Returns details such as Variation name, identifier etc for the given Feature Flag  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_feature_flag_with_http_info(identifier, account_identifier, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: Unique identifier for the object in the API. (required)
        :param str account_identifier: Account Identifier (required)
        :param str org_identifier: Organization Identifier (required)
        :param str project_identifier: The Project identifier (required)
        :param str environment_identifier: Environment
        :param bool metrics: Parameter to indicate if metrics data is requested in response
        :param bool archived: Status of the feature flag
        :return: Feature
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['identifier', 'account_identifier', 'org_identifier', 'project_identifier', 'environment_identifier', 'metrics', 'archived']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_feature_flag" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `get_feature_flag`")  # noqa: E501
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `get_feature_flag`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `get_feature_flag`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `get_feature_flag`")  # noqa: E501

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
        if 'environment_identifier' in params:
            query_params.append(('environmentIdentifier', params['environment_identifier']))  # noqa: E501
        if 'metrics' in params:
            query_params.append(('metrics', params['metrics']))  # noqa: E501
        if 'archived' in params:
            query_params.append(('archived', params['archived']))  # noqa: E501

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
            '/cf/admin/features/{identifier}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Feature',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def patch_feature(self, account_identifier, org_identifier, project_identifier, identifier, **kwargs):  # noqa: E501
        """Updates a Feature Flag  # noqa: E501

        This operation is used to modify a Feature Flag.  The request body can include one or more instructions that can modify flag attributes such as the state (off|on), the variations that are returned and serving rules. For example if you want to turn a flag off you can use this opeartion and send the setFeatureFlagState  {   \"kind\": \"setFeatureFlagState\",   \"parameters\": {     \"state\": \"off\"   } }   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_feature(account_identifier, org_identifier, project_identifier, identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier (required)
        :param str org_identifier: Organization Identifier (required)
        :param str project_identifier: The Project identifier (required)
        :param str identifier: Unique identifier for the object in the API. (required)
        :param GitSyncPatchOperation body:
        :param str environment_identifier: Environment
        :return: FeatureResponseMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.patch_feature_with_http_info(account_identifier, org_identifier, project_identifier, identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.patch_feature_with_http_info(account_identifier, org_identifier, project_identifier, identifier, **kwargs)  # noqa: E501
            return data

    def patch_feature_with_http_info(self, account_identifier, org_identifier, project_identifier, identifier, **kwargs):  # noqa: E501
        """Updates a Feature Flag  # noqa: E501

        This operation is used to modify a Feature Flag.  The request body can include one or more instructions that can modify flag attributes such as the state (off|on), the variations that are returned and serving rules. For example if you want to turn a flag off you can use this opeartion and send the setFeatureFlagState  {   \"kind\": \"setFeatureFlagState\",   \"parameters\": {     \"state\": \"off\"   } }   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_feature_with_http_info(account_identifier, org_identifier, project_identifier, identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_identifier: Account Identifier (required)
        :param str org_identifier: Organization Identifier (required)
        :param str project_identifier: The Project identifier (required)
        :param str identifier: Unique identifier for the object in the API. (required)
        :param GitSyncPatchOperation body:
        :param str environment_identifier: Environment
        :return: FeatureResponseMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_identifier', 'org_identifier', 'project_identifier', 'identifier', 'body', 'environment_identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_feature" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `patch_feature`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `patch_feature`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `patch_feature`")  # noqa: E501
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `patch_feature`")  # noqa: E501

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
        if 'environment_identifier' in params:
            query_params.append(('environmentIdentifier', params['environment_identifier']))  # noqa: E501

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
            '/cf/admin/features/{identifier}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FeatureResponseMetadata',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def restore_feature_flag(self, identifier, account_identifier, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """Restore a Feature Flag  # noqa: E501

        Restore Feature Flag for the given identifier and account ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.restore_feature_flag(identifier, account_identifier, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: Unique identifier for the object in the API. (required)
        :param str account_identifier: Account Identifier (required)
        :param str org_identifier: Organization Identifier (required)
        :param str project_identifier: The Project identifier (required)
        :param str commit_msg: Git commit message
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.restore_feature_flag_with_http_info(identifier, account_identifier, org_identifier, project_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.restore_feature_flag_with_http_info(identifier, account_identifier, org_identifier, project_identifier, **kwargs)  # noqa: E501
            return data

    def restore_feature_flag_with_http_info(self, identifier, account_identifier, org_identifier, project_identifier, **kwargs):  # noqa: E501
        """Restore a Feature Flag  # noqa: E501

        Restore Feature Flag for the given identifier and account ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.restore_feature_flag_with_http_info(identifier, account_identifier, org_identifier, project_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: Unique identifier for the object in the API. (required)
        :param str account_identifier: Account Identifier (required)
        :param str org_identifier: Organization Identifier (required)
        :param str project_identifier: The Project identifier (required)
        :param str commit_msg: Git commit message
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['identifier', 'account_identifier', 'org_identifier', 'project_identifier', 'commit_msg']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method restore_feature_flag" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `restore_feature_flag`")  # noqa: E501
        # verify the required parameter 'account_identifier' is set
        if ('account_identifier' not in params or
                params['account_identifier'] is None):
            raise ValueError("Missing the required parameter `account_identifier` when calling `restore_feature_flag`")  # noqa: E501
        # verify the required parameter 'org_identifier' is set
        if ('org_identifier' not in params or
                params['org_identifier'] is None):
            raise ValueError("Missing the required parameter `org_identifier` when calling `restore_feature_flag`")  # noqa: E501
        # verify the required parameter 'project_identifier' is set
        if ('project_identifier' not in params or
                params['project_identifier'] is None):
            raise ValueError("Missing the required parameter `project_identifier` when calling `restore_feature_flag`")  # noqa: E501

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
        if 'commit_msg' in params:
            query_params.append(('commitMsg', params['commit_msg']))  # noqa: E501

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
            '/cf/admin/features/{identifier}/restore', 'POST',
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
