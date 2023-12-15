# coding: utf-8

"""
    Harness NextGen Software Delivery Platform API Reference

    The Harness Software Delivery Platform uses OpenAPI Specification v3.0. Harness constantly improves these APIs. Please be aware that some improvements could cause breaking changes. # Introduction     The Harness API allows you to integrate and use all the services and modules we provide on the Harness Platform. If you use client-side SDKs, Harness functionality can be integrated with your client-side automation, helping you reduce manual efforts and deploy code faster.    For more information about how Harness works, read our [documentation](https://developer.harness.io/docs/getting-started) or visit the [Harness Developer Hub](https://developer.harness.io/).  ## How it works    The Harness API is a RESTful API that uses standard HTTP verbs. You can send requests in JSON, YAML, or form-data format. The format of the response matches the format of your request. You must send a single request at a time and ensure that you include your authentication key. For more information about this, go to [Authentication](#section/Introduction/Authentication).  ## Get started    Before you start integrating, get to know our API better by reading the following topics:    * [Harness key concepts](https://developer.harness.io/docs/getting-started/learn-harness-key-concepts/)   * [Authentication](#section/Introduction/Authentication)   * [Requests and responses](#section/Introduction/Requests-and-Responses)   * [Common Parameters](#section/Introduction/Common-Parameters-Beta)   * [Status Codes](#section/Introduction/Status-Codes)   * [Errors](#tag/Error-Response)   * [Versioning](#section/Introduction/Versioning-Beta)   * [Pagination](/#section/Introduction/Pagination-Beta)    The methods you need to integrate with depend on the functionality you want to use. Work with  your Harness Solutions Engineer to determine which methods you need.  ## Authentication  To authenticate with the Harness API, you need to:   1. Generate an API token on the Harness Platform.   2. Send the API token you generate in the `x-api-key` header in each request.  ### Generate an API token  To generate an API token, complete the following steps:   1. Go to the [Harness Platform](https://app.harness.io/).   2. On the left-hand navigation, click **My Profile**.   3. Click **+API Key**, enter a name for your key and then click **Save**.   4. Within the API Key tile, click **+Token**.   5. Enter a name for your token and click **Generate Token**. **Important**: Make sure to save your token securely. Harness does not store the API token for future reference, so make sure to save your token securely before you leave the page.  ### Send the API token in your requests  Send the token you created in the Harness Platform in the x-api-key header. For example:   `x-api-key: YOUR_API_KEY_HERE`  ## Requests and Responses    The structure for each request and response is outlined in the API documentation. We have examples in JSON and YAML for every request and response. You can use our online editor to test the examples.  ## Common Parameters [Beta]  | Field Name | Type    | Default | Description    | |------------|---------|---------|----------------| | identifier | string  | none    | URL-friendly version of the name, used to identify a resource within it's scope and so needs to be unique within the scope.                                                                                                            | | name       | string  | none    | Human-friendly name for the resource.                                                                                       | | org        | string  | none    | Limit to provided org identifiers.                                                                                                                     | | project    | string  | none    | Limit to provided project identifiers.                                                                                                                 | | description| string  | none    | More information about the specific resource.                                                                                    | | tags       | map[string]string  | none    | List of labels applied to the resource.                                                                                                                         | | order      | string  | desc    | Order to use when sorting the specified fields. Type: enum(asc,desc).                                                                                                                                     | | sort       | string  | none    | Fields on which to sort. Note: Specify the fields that you want to use for sorting. When doing so, consider the operational overhead of sorting fields. | | limit      | int     | 30      | Pagination: Number of items to return.                                                                                                                 | | page       | int     | 1       | Pagination page number strategy: Specify the page number within the paginated collection related to the number of items in each page.                  | | created    | int64   | none    | Unix timestamp that shows when the resource was created (in milliseconds).                                                               | | updated    | int64   | none    | Unix timestamp that shows when the resource was last edited (in milliseconds).                                                           |   ## Status Codes    Harness uses conventional HTTP status codes to indicate the status of an API request.    Generally, 2xx responses are reserved for success and 4xx status codes are reserved for failures. A 5xx response code indicates an error on the Harness server.    | Error Code  | Description |   |-------------|-------------|   | 200         |     OK      |   | 201         |   Created   |   | 202         |   Accepted  |   | 204         |  No Content |   | 400         | Bad Request |   | 401         | Unauthorized |   | 403         | Forbidden |   | 412         | Precondition Failed |   | 415         | Unsupported Media Type |   | 500         | Server Error |    To view our error response structures, go [here](#tag/Error-Response).  ## Versioning [Beta]  ### Harness Version   The current version of our Beta APIs is yet to be announced. The version number will use the date-header format and will be valid only for our Beta APIs.  ### Generation   All our beta APIs are versioned as a Generation, and this version is included in the path to every API resource. For example, v1 beta APIs begin with `app.harness.io/v1/`, where v1 is the API Generation.    The version number represents the core API and does not change frequently. The version number changes only if there is a significant departure from the basic underpinnings of the existing API. For example, when Harness performs a system-wide refactoring of core concepts or resources.  ## Pagination [Beta]  We use pagination to place limits on the number of responses associated with list endpoints. Pagination is achieved by the use of limit query parameters. The limit defaults to 30. Its maximum value is 100.  Following are the pagination headers supported in the response bodies of paginated APIs:   1. X-Total-Elements : Indicates the total number of entries in a paginated response.   2. X-Page-Number : Indicates the page number currently returned for a paginated response.   3. X-Page-Size : Indicates the number of entries per page for a paginated response.  For example:    ``` X-Total-Elements : 30 X-Page-Number : 0 X-Page-Size : 10   ```   # noqa: E501

    OpenAPI spec version: 1.0
    Contact: contact@harness.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Budget(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'uuid': 'str',
        'account_id': 'str',
        'name': 'str',
        'scope': 'BudgetScope',
        'type': 'str',
        'budget_monthly_breakdown': 'BudgetMonthlyBreakdown',
        'budget_amount': 'float',
        'period': 'str',
        'growth_rate': 'float',
        'actual_cost': 'float',
        'forecast_cost': 'float',
        'last_month_cost': 'float',
        'alert_thresholds': 'list[AlertThreshold]',
        'email_addresses': 'list[str]',
        'user_group_ids': 'list[str]',
        'parent_budget_group_id': 'str',
        'notify_on_slack': 'bool',
        'is_ng_budget': 'bool',
        'start_time': 'int',
        'end_time': 'int',
        'created_at': 'int',
        'last_updated_at': 'int',
        'budget_history': 'dict(str, BudgetCostData)',
        'disable_currency_warning': 'bool',
        'ng_budget': 'bool'
    }

    attribute_map = {
        'uuid': 'uuid',
        'account_id': 'accountId',
        'name': 'name',
        'scope': 'scope',
        'type': 'type',
        'budget_monthly_breakdown': 'budgetMonthlyBreakdown',
        'budget_amount': 'budgetAmount',
        'period': 'period',
        'growth_rate': 'growthRate',
        'actual_cost': 'actualCost',
        'forecast_cost': 'forecastCost',
        'last_month_cost': 'lastMonthCost',
        'alert_thresholds': 'alertThresholds',
        'email_addresses': 'emailAddresses',
        'user_group_ids': 'userGroupIds',
        'parent_budget_group_id': 'parentBudgetGroupId',
        'notify_on_slack': 'notifyOnSlack',
        'is_ng_budget': 'isNgBudget',
        'start_time': 'startTime',
        'end_time': 'endTime',
        'created_at': 'createdAt',
        'last_updated_at': 'lastUpdatedAt',
        'budget_history': 'budgetHistory',
        'disable_currency_warning': 'disableCurrencyWarning',
        'ng_budget': 'ngBudget'
    }

    def __init__(self, uuid=None, account_id=None, name=None, scope=None, type=None, budget_monthly_breakdown=None, budget_amount=None, period=None, growth_rate=None, actual_cost=None, forecast_cost=None, last_month_cost=None, alert_thresholds=None, email_addresses=None, user_group_ids=None, parent_budget_group_id=None, notify_on_slack=None, is_ng_budget=None, start_time=None, end_time=None, created_at=None, last_updated_at=None, budget_history=None, disable_currency_warning=None, ng_budget=None):  # noqa: E501
        """Budget - a model defined in Swagger"""  # noqa: E501
        self._uuid = None
        self._account_id = None
        self._name = None
        self._scope = None
        self._type = None
        self._budget_monthly_breakdown = None
        self._budget_amount = None
        self._period = None
        self._growth_rate = None
        self._actual_cost = None
        self._forecast_cost = None
        self._last_month_cost = None
        self._alert_thresholds = None
        self._email_addresses = None
        self._user_group_ids = None
        self._parent_budget_group_id = None
        self._notify_on_slack = None
        self._is_ng_budget = None
        self._start_time = None
        self._end_time = None
        self._created_at = None
        self._last_updated_at = None
        self._budget_history = None
        self._disable_currency_warning = None
        self._ng_budget = None
        self.discriminator = None
        if uuid is not None:
            self.uuid = uuid
        self.account_id = account_id
        self.name = name
        if scope is not None:
            self.scope = scope
        if type is not None:
            self.type = type
        if budget_monthly_breakdown is not None:
            self.budget_monthly_breakdown = budget_monthly_breakdown
        if budget_amount is not None:
            self.budget_amount = budget_amount
        if period is not None:
            self.period = period
        if growth_rate is not None:
            self.growth_rate = growth_rate
        if actual_cost is not None:
            self.actual_cost = actual_cost
        if forecast_cost is not None:
            self.forecast_cost = forecast_cost
        if last_month_cost is not None:
            self.last_month_cost = last_month_cost
        if alert_thresholds is not None:
            self.alert_thresholds = alert_thresholds
        if email_addresses is not None:
            self.email_addresses = email_addresses
        if user_group_ids is not None:
            self.user_group_ids = user_group_ids
        if parent_budget_group_id is not None:
            self.parent_budget_group_id = parent_budget_group_id
        if notify_on_slack is not None:
            self.notify_on_slack = notify_on_slack
        if is_ng_budget is not None:
            self.is_ng_budget = is_ng_budget
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if created_at is not None:
            self.created_at = created_at
        if last_updated_at is not None:
            self.last_updated_at = last_updated_at
        if budget_history is not None:
            self.budget_history = budget_history
        if disable_currency_warning is not None:
            self.disable_currency_warning = disable_currency_warning
        if ng_budget is not None:
            self.ng_budget = ng_budget

    @property
    def uuid(self):
        """Gets the uuid of this Budget.  # noqa: E501


        :return: The uuid of this Budget.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this Budget.


        :param uuid: The uuid of this Budget.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def account_id(self):
        """Gets the account_id of this Budget.  # noqa: E501


        :return: The account_id of this Budget.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this Budget.


        :param account_id: The account_id of this Budget.  # noqa: E501
        :type: str
        """
        if account_id is None:
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def name(self):
        """Gets the name of this Budget.  # noqa: E501


        :return: The name of this Budget.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Budget.


        :param name: The name of this Budget.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def scope(self):
        """Gets the scope of this Budget.  # noqa: E501


        :return: The scope of this Budget.  # noqa: E501
        :rtype: BudgetScope
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this Budget.


        :param scope: The scope of this Budget.  # noqa: E501
        :type: BudgetScope
        """

        self._scope = scope

    @property
    def type(self):
        """Gets the type of this Budget.  # noqa: E501

        Whether the Budget is based on a specified amount or based on previous month's actual spend  # noqa: E501

        :return: The type of this Budget.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Budget.

        Whether the Budget is based on a specified amount or based on previous month's actual spend  # noqa: E501

        :param type: The type of this Budget.  # noqa: E501
        :type: str
        """
        allowed_values = ["SPECIFIED_AMOUNT", "PREVIOUS_MONTH_SPEND", "PREVIOUS_PERIOD_SPEND"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def budget_monthly_breakdown(self):
        """Gets the budget_monthly_breakdown of this Budget.  # noqa: E501


        :return: The budget_monthly_breakdown of this Budget.  # noqa: E501
        :rtype: BudgetMonthlyBreakdown
        """
        return self._budget_monthly_breakdown

    @budget_monthly_breakdown.setter
    def budget_monthly_breakdown(self, budget_monthly_breakdown):
        """Sets the budget_monthly_breakdown of this Budget.


        :param budget_monthly_breakdown: The budget_monthly_breakdown of this Budget.  # noqa: E501
        :type: BudgetMonthlyBreakdown
        """

        self._budget_monthly_breakdown = budget_monthly_breakdown

    @property
    def budget_amount(self):
        """Gets the budget_amount of this Budget.  # noqa: E501


        :return: The budget_amount of this Budget.  # noqa: E501
        :rtype: float
        """
        return self._budget_amount

    @budget_amount.setter
    def budget_amount(self, budget_amount):
        """Sets the budget_amount of this Budget.


        :param budget_amount: The budget_amount of this Budget.  # noqa: E501
        :type: float
        """

        self._budget_amount = budget_amount

    @property
    def period(self):
        """Gets the period of this Budget.  # noqa: E501


        :return: The period of this Budget.  # noqa: E501
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this Budget.


        :param period: The period of this Budget.  # noqa: E501
        :type: str
        """
        allowed_values = ["DAILY", "WEEKLY", "MONTHLY", "QUARTERLY", "YEARLY"]  # noqa: E501
        if period not in allowed_values:
            raise ValueError(
                "Invalid value for `period` ({0}), must be one of {1}"  # noqa: E501
                .format(period, allowed_values)
            )

        self._period = period

    @property
    def growth_rate(self):
        """Gets the growth_rate of this Budget.  # noqa: E501


        :return: The growth_rate of this Budget.  # noqa: E501
        :rtype: float
        """
        return self._growth_rate

    @growth_rate.setter
    def growth_rate(self, growth_rate):
        """Sets the growth_rate of this Budget.


        :param growth_rate: The growth_rate of this Budget.  # noqa: E501
        :type: float
        """

        self._growth_rate = growth_rate

    @property
    def actual_cost(self):
        """Gets the actual_cost of this Budget.  # noqa: E501


        :return: The actual_cost of this Budget.  # noqa: E501
        :rtype: float
        """
        return self._actual_cost

    @actual_cost.setter
    def actual_cost(self, actual_cost):
        """Sets the actual_cost of this Budget.


        :param actual_cost: The actual_cost of this Budget.  # noqa: E501
        :type: float
        """

        self._actual_cost = actual_cost

    @property
    def forecast_cost(self):
        """Gets the forecast_cost of this Budget.  # noqa: E501


        :return: The forecast_cost of this Budget.  # noqa: E501
        :rtype: float
        """
        return self._forecast_cost

    @forecast_cost.setter
    def forecast_cost(self, forecast_cost):
        """Sets the forecast_cost of this Budget.


        :param forecast_cost: The forecast_cost of this Budget.  # noqa: E501
        :type: float
        """

        self._forecast_cost = forecast_cost

    @property
    def last_month_cost(self):
        """Gets the last_month_cost of this Budget.  # noqa: E501


        :return: The last_month_cost of this Budget.  # noqa: E501
        :rtype: float
        """
        return self._last_month_cost

    @last_month_cost.setter
    def last_month_cost(self, last_month_cost):
        """Sets the last_month_cost of this Budget.


        :param last_month_cost: The last_month_cost of this Budget.  # noqa: E501
        :type: float
        """

        self._last_month_cost = last_month_cost

    @property
    def alert_thresholds(self):
        """Gets the alert_thresholds of this Budget.  # noqa: E501


        :return: The alert_thresholds of this Budget.  # noqa: E501
        :rtype: list[AlertThreshold]
        """
        return self._alert_thresholds

    @alert_thresholds.setter
    def alert_thresholds(self, alert_thresholds):
        """Sets the alert_thresholds of this Budget.


        :param alert_thresholds: The alert_thresholds of this Budget.  # noqa: E501
        :type: list[AlertThreshold]
        """

        self._alert_thresholds = alert_thresholds

    @property
    def email_addresses(self):
        """Gets the email_addresses of this Budget.  # noqa: E501


        :return: The email_addresses of this Budget.  # noqa: E501
        :rtype: list[str]
        """
        return self._email_addresses

    @email_addresses.setter
    def email_addresses(self, email_addresses):
        """Sets the email_addresses of this Budget.


        :param email_addresses: The email_addresses of this Budget.  # noqa: E501
        :type: list[str]
        """

        self._email_addresses = email_addresses

    @property
    def user_group_ids(self):
        """Gets the user_group_ids of this Budget.  # noqa: E501


        :return: The user_group_ids of this Budget.  # noqa: E501
        :rtype: list[str]
        """
        return self._user_group_ids

    @user_group_ids.setter
    def user_group_ids(self, user_group_ids):
        """Sets the user_group_ids of this Budget.


        :param user_group_ids: The user_group_ids of this Budget.  # noqa: E501
        :type: list[str]
        """

        self._user_group_ids = user_group_ids

    @property
    def parent_budget_group_id(self):
        """Gets the parent_budget_group_id of this Budget.  # noqa: E501


        :return: The parent_budget_group_id of this Budget.  # noqa: E501
        :rtype: str
        """
        return self._parent_budget_group_id

    @parent_budget_group_id.setter
    def parent_budget_group_id(self, parent_budget_group_id):
        """Sets the parent_budget_group_id of this Budget.


        :param parent_budget_group_id: The parent_budget_group_id of this Budget.  # noqa: E501
        :type: str
        """

        self._parent_budget_group_id = parent_budget_group_id

    @property
    def notify_on_slack(self):
        """Gets the notify_on_slack of this Budget.  # noqa: E501


        :return: The notify_on_slack of this Budget.  # noqa: E501
        :rtype: bool
        """
        return self._notify_on_slack

    @notify_on_slack.setter
    def notify_on_slack(self, notify_on_slack):
        """Sets the notify_on_slack of this Budget.


        :param notify_on_slack: The notify_on_slack of this Budget.  # noqa: E501
        :type: bool
        """

        self._notify_on_slack = notify_on_slack

    @property
    def is_ng_budget(self):
        """Gets the is_ng_budget of this Budget.  # noqa: E501


        :return: The is_ng_budget of this Budget.  # noqa: E501
        :rtype: bool
        """
        return self._is_ng_budget

    @is_ng_budget.setter
    def is_ng_budget(self, is_ng_budget):
        """Sets the is_ng_budget of this Budget.


        :param is_ng_budget: The is_ng_budget of this Budget.  # noqa: E501
        :type: bool
        """

        self._is_ng_budget = is_ng_budget

    @property
    def start_time(self):
        """Gets the start_time of this Budget.  # noqa: E501


        :return: The start_time of this Budget.  # noqa: E501
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this Budget.


        :param start_time: The start_time of this Budget.  # noqa: E501
        :type: int
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this Budget.  # noqa: E501


        :return: The end_time of this Budget.  # noqa: E501
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this Budget.


        :param end_time: The end_time of this Budget.  # noqa: E501
        :type: int
        """

        self._end_time = end_time

    @property
    def created_at(self):
        """Gets the created_at of this Budget.  # noqa: E501


        :return: The created_at of this Budget.  # noqa: E501
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Budget.


        :param created_at: The created_at of this Budget.  # noqa: E501
        :type: int
        """

        self._created_at = created_at

    @property
    def last_updated_at(self):
        """Gets the last_updated_at of this Budget.  # noqa: E501


        :return: The last_updated_at of this Budget.  # noqa: E501
        :rtype: int
        """
        return self._last_updated_at

    @last_updated_at.setter
    def last_updated_at(self, last_updated_at):
        """Sets the last_updated_at of this Budget.


        :param last_updated_at: The last_updated_at of this Budget.  # noqa: E501
        :type: int
        """

        self._last_updated_at = last_updated_at

    @property
    def budget_history(self):
        """Gets the budget_history of this Budget.  # noqa: E501


        :return: The budget_history of this Budget.  # noqa: E501
        :rtype: dict(str, BudgetCostData)
        """
        return self._budget_history

    @budget_history.setter
    def budget_history(self, budget_history):
        """Sets the budget_history of this Budget.


        :param budget_history: The budget_history of this Budget.  # noqa: E501
        :type: dict(str, BudgetCostData)
        """

        self._budget_history = budget_history

    @property
    def disable_currency_warning(self):
        """Gets the disable_currency_warning of this Budget.  # noqa: E501


        :return: The disable_currency_warning of this Budget.  # noqa: E501
        :rtype: bool
        """
        return self._disable_currency_warning

    @disable_currency_warning.setter
    def disable_currency_warning(self, disable_currency_warning):
        """Sets the disable_currency_warning of this Budget.


        :param disable_currency_warning: The disable_currency_warning of this Budget.  # noqa: E501
        :type: bool
        """

        self._disable_currency_warning = disable_currency_warning

    @property
    def ng_budget(self):
        """Gets the ng_budget of this Budget.  # noqa: E501


        :return: The ng_budget of this Budget.  # noqa: E501
        :rtype: bool
        """
        return self._ng_budget

    @ng_budget.setter
    def ng_budget(self, ng_budget):
        """Sets the ng_budget of this Budget.


        :param ng_budget: The ng_budget of this Budget.  # noqa: E501
        :type: bool
        """

        self._ng_budget = ng_budget

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Budget, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Budget):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
