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

class BudgetMonthlyBreakdown(object):
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
        'budget_breakdown': 'str',
        'budget_monthly_amount': 'list[ValueDataPoint]',
        'actual_monthly_cost': 'list[float]',
        'forecast_monthly_cost': 'list[float]',
        'yearly_last_period_cost': 'list[float]'
    }

    attribute_map = {
        'budget_breakdown': 'budgetBreakdown',
        'budget_monthly_amount': 'budgetMonthlyAmount',
        'actual_monthly_cost': 'actualMonthlyCost',
        'forecast_monthly_cost': 'forecastMonthlyCost',
        'yearly_last_period_cost': 'yearlyLastPeriodCost'
    }

    def __init__(self, budget_breakdown=None, budget_monthly_amount=None, actual_monthly_cost=None, forecast_monthly_cost=None, yearly_last_period_cost=None):  # noqa: E501
        """BudgetMonthlyBreakdown - a model defined in Swagger"""  # noqa: E501
        self._budget_breakdown = None
        self._budget_monthly_amount = None
        self._actual_monthly_cost = None
        self._forecast_monthly_cost = None
        self._yearly_last_period_cost = None
        self.discriminator = None
        if budget_breakdown is not None:
            self.budget_breakdown = budget_breakdown
        if budget_monthly_amount is not None:
            self.budget_monthly_amount = budget_monthly_amount
        if actual_monthly_cost is not None:
            self.actual_monthly_cost = actual_monthly_cost
        if forecast_monthly_cost is not None:
            self.forecast_monthly_cost = forecast_monthly_cost
        if yearly_last_period_cost is not None:
            self.yearly_last_period_cost = yearly_last_period_cost

    @property
    def budget_breakdown(self):
        """Gets the budget_breakdown of this BudgetMonthlyBreakdown.  # noqa: E501

        Whether the Yearly budget breakdown is yearly or monthly  # noqa: E501

        :return: The budget_breakdown of this BudgetMonthlyBreakdown.  # noqa: E501
        :rtype: str
        """
        return self._budget_breakdown

    @budget_breakdown.setter
    def budget_breakdown(self, budget_breakdown):
        """Sets the budget_breakdown of this BudgetMonthlyBreakdown.

        Whether the Yearly budget breakdown is yearly or monthly  # noqa: E501

        :param budget_breakdown: The budget_breakdown of this BudgetMonthlyBreakdown.  # noqa: E501
        :type: str
        """
        allowed_values = ["YEARLY", "MONTHLY"]  # noqa: E501
        if budget_breakdown not in allowed_values:
            raise ValueError(
                "Invalid value for `budget_breakdown` ({0}), must be one of {1}"  # noqa: E501
                .format(budget_breakdown, allowed_values)
            )

        self._budget_breakdown = budget_breakdown

    @property
    def budget_monthly_amount(self):
        """Gets the budget_monthly_amount of this BudgetMonthlyBreakdown.  # noqa: E501

        Budgeted monthly amount for yearly budget  # noqa: E501

        :return: The budget_monthly_amount of this BudgetMonthlyBreakdown.  # noqa: E501
        :rtype: list[ValueDataPoint]
        """
        return self._budget_monthly_amount

    @budget_monthly_amount.setter
    def budget_monthly_amount(self, budget_monthly_amount):
        """Sets the budget_monthly_amount of this BudgetMonthlyBreakdown.

        Budgeted monthly amount for yearly budget  # noqa: E501

        :param budget_monthly_amount: The budget_monthly_amount of this BudgetMonthlyBreakdown.  # noqa: E501
        :type: list[ValueDataPoint]
        """

        self._budget_monthly_amount = budget_monthly_amount

    @property
    def actual_monthly_cost(self):
        """Gets the actual_monthly_cost of this BudgetMonthlyBreakdown.  # noqa: E501

        Actual monthly cost for yearly budget  # noqa: E501

        :return: The actual_monthly_cost of this BudgetMonthlyBreakdown.  # noqa: E501
        :rtype: list[float]
        """
        return self._actual_monthly_cost

    @actual_monthly_cost.setter
    def actual_monthly_cost(self, actual_monthly_cost):
        """Sets the actual_monthly_cost of this BudgetMonthlyBreakdown.

        Actual monthly cost for yearly budget  # noqa: E501

        :param actual_monthly_cost: The actual_monthly_cost of this BudgetMonthlyBreakdown.  # noqa: E501
        :type: list[float]
        """

        self._actual_monthly_cost = actual_monthly_cost

    @property
    def forecast_monthly_cost(self):
        """Gets the forecast_monthly_cost of this BudgetMonthlyBreakdown.  # noqa: E501

        Forecasted monthly cost for yearly budget  # noqa: E501

        :return: The forecast_monthly_cost of this BudgetMonthlyBreakdown.  # noqa: E501
        :rtype: list[float]
        """
        return self._forecast_monthly_cost

    @forecast_monthly_cost.setter
    def forecast_monthly_cost(self, forecast_monthly_cost):
        """Sets the forecast_monthly_cost of this BudgetMonthlyBreakdown.

        Forecasted monthly cost for yearly budget  # noqa: E501

        :param forecast_monthly_cost: The forecast_monthly_cost of this BudgetMonthlyBreakdown.  # noqa: E501
        :type: list[float]
        """

        self._forecast_monthly_cost = forecast_monthly_cost

    @property
    def yearly_last_period_cost(self):
        """Gets the yearly_last_period_cost of this BudgetMonthlyBreakdown.  # noqa: E501

        Yearly monthly cost for last year budget  # noqa: E501

        :return: The yearly_last_period_cost of this BudgetMonthlyBreakdown.  # noqa: E501
        :rtype: list[float]
        """
        return self._yearly_last_period_cost

    @yearly_last_period_cost.setter
    def yearly_last_period_cost(self, yearly_last_period_cost):
        """Sets the yearly_last_period_cost of this BudgetMonthlyBreakdown.

        Yearly monthly cost for last year budget  # noqa: E501

        :param yearly_last_period_cost: The yearly_last_period_cost of this BudgetMonthlyBreakdown.  # noqa: E501
        :type: list[float]
        """

        self._yearly_last_period_cost = yearly_last_period_cost

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
        if issubclass(BudgetMonthlyBreakdown, dict):
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
        if not isinstance(other, BudgetMonthlyBreakdown):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
