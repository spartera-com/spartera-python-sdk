# spartera_api_sdk.CompaniesApi

All URIs are relative to *https://api.spartera.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_companies_by_id**](CompaniesApi.md#get_companies_by_id) | **GET** /companies/{company_id} | Get details of the requestor&#39;s own company
[**list_companies**](CompaniesApi.md#list_companies) | **GET** /companies/{company_id}/requests/plan | Get the total number of requests allocated in the company&#39;s current subscription plan.
[**list_companies_analytics_assets**](CompaniesApi.md#list_companies_analytics_assets) | **GET** /companies/{company_id}/analytics/assets | Get asset performance analytics.     Query params: start_date, end_date, limit, sort_by, include
[**list_companies_analytics_customers**](CompaniesApi.md#list_companies_analytics_customers) | **GET** /companies/{company_id}/analytics/customers | Get customer analytics including growth and segmentation.     Query params: start_date, end_date, group_by, segment_by
[**list_companies_analytics_dashboard**](CompaniesApi.md#list_companies_analytics_dashboard) | **GET** /companies/{company_id}/analytics/dashboard | Get comprehensive dashboard analytics for seller dashboard.     Query params: start_date, end_date, period (day/week/month/quarter)
[**list_companies_analytics_metrics**](CompaniesApi.md#list_companies_analytics_metrics) | **GET** /companies/{company_id}/analytics/metrics | Get summary metrics (counts only). No date params needed — returns all-time totals.     Performance: &lt; 0.1s
[**list_companies_analytics_sales**](CompaniesApi.md#list_companies_analytics_sales) | **GET** /companies/{company_id}/analytics/sales | Get sales over time analytics.     Query params: start_date, end_date, group_by (day/week/month/quarter), metrics
[**list_companies_objects**](CompaniesApi.md#list_companies_objects) | **GET** /companies/{company_id}/objects | Get all objects (connections, assets) of a single company
[**list_companies_requests_usage**](CompaniesApi.md#list_companies_requests_usage) | **GET** /companies/{company_id}/requests/usage | Get company request usage data for a specific month.
[**update_companies**](CompaniesApi.md#update_companies) | **PATCH** /companies/{company_id} | Update an existing company by ID


# **get_companies_by_id**
> GetCompaniesById200Response get_companies_by_id(company_id)

Get details of the requestor's own company

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.get_companies_by_id200_response import GetCompaniesById200Response
from spartera_api_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.spartera.com
# See configuration.py for a list of all supported configuration parameters.
configuration = spartera_api_sdk.Configuration(
    host = "https://api.spartera.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with spartera_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spartera_api_sdk.CompaniesApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company

    try:
        # Get details of the requestor's own company
        api_response = api_instance.get_companies_by_id(company_id)
        print("The response of CompaniesApi->get_companies_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompaniesApi->get_companies_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 

### Return type

[**GetCompaniesById200Response**](GetCompaniesById200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved companies |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_companies**
> ListCompaniesAnalyticsAssets200Response list_companies(company_id, page=page, limit=limit, sort_by=sort_by, sort_order=sort_order, search=search)

Get the total number of requests allocated in the company's current subscription plan.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.list_companies_analytics_assets200_response import ListCompaniesAnalyticsAssets200Response
from spartera_api_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.spartera.com
# See configuration.py for a list of all supported configuration parameters.
configuration = spartera_api_sdk.Configuration(
    host = "https://api.spartera.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with spartera_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spartera_api_sdk.CompaniesApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    page = 1 # int | Page number for pagination (optional) (default to 1)
    limit = 20 # int | Number of items per page (optional) (default to 20)
    sort_by = 'sort_by_example' # str | Field to sort by (optional)
    sort_order = desc # str | Sort order (ascending or descending) (optional) (default to desc)
    search = 'search_example' # str | Search term to filter results (optional)

    try:
        # Get the total number of requests allocated in the company's current subscription plan.
        api_response = api_instance.list_companies(company_id, page=page, limit=limit, sort_by=sort_by, sort_order=sort_order, search=search)
        print("The response of CompaniesApi->list_companies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompaniesApi->list_companies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **page** | **int**| Page number for pagination | [optional] [default to 1]
 **limit** | **int**| Number of items per page | [optional] [default to 20]
 **sort_by** | **str**| Field to sort by | [optional] 
 **sort_order** | **str**| Sort order (ascending or descending) | [optional] [default to desc]
 **search** | **str**| Search term to filter results | [optional] 

### Return type

[**ListCompaniesAnalyticsAssets200Response**](ListCompaniesAnalyticsAssets200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved companies |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_companies_analytics_assets**
> ListCompaniesAnalyticsAssets200Response list_companies_analytics_assets(company_id, page=page, limit=limit, sort_by=sort_by, sort_order=sort_order, search=search)

Get asset performance analytics.     Query params: start_date, end_date, limit, sort_by, include

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.list_companies_analytics_assets200_response import ListCompaniesAnalyticsAssets200Response
from spartera_api_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.spartera.com
# See configuration.py for a list of all supported configuration parameters.
configuration = spartera_api_sdk.Configuration(
    host = "https://api.spartera.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with spartera_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spartera_api_sdk.CompaniesApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    page = 1 # int | Page number for pagination (optional) (default to 1)
    limit = 20 # int | Number of items per page (optional) (default to 20)
    sort_by = 'sort_by_example' # str | Field to sort by (optional)
    sort_order = desc # str | Sort order (ascending or descending) (optional) (default to desc)
    search = 'search_example' # str | Search term to filter results (optional)

    try:
        # Get asset performance analytics.     Query params: start_date, end_date, limit, sort_by, include
        api_response = api_instance.list_companies_analytics_assets(company_id, page=page, limit=limit, sort_by=sort_by, sort_order=sort_order, search=search)
        print("The response of CompaniesApi->list_companies_analytics_assets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompaniesApi->list_companies_analytics_assets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **page** | **int**| Page number for pagination | [optional] [default to 1]
 **limit** | **int**| Number of items per page | [optional] [default to 20]
 **sort_by** | **str**| Field to sort by | [optional] 
 **sort_order** | **str**| Sort order (ascending or descending) | [optional] [default to desc]
 **search** | **str**| Search term to filter results | [optional] 

### Return type

[**ListCompaniesAnalyticsAssets200Response**](ListCompaniesAnalyticsAssets200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved companies |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_companies_analytics_customers**
> ListCompaniesAnalyticsAssets200Response list_companies_analytics_customers(company_id, page=page, limit=limit, sort_by=sort_by, sort_order=sort_order, search=search)

Get customer analytics including growth and segmentation.     Query params: start_date, end_date, group_by, segment_by

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.list_companies_analytics_assets200_response import ListCompaniesAnalyticsAssets200Response
from spartera_api_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.spartera.com
# See configuration.py for a list of all supported configuration parameters.
configuration = spartera_api_sdk.Configuration(
    host = "https://api.spartera.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with spartera_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spartera_api_sdk.CompaniesApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    page = 1 # int | Page number for pagination (optional) (default to 1)
    limit = 20 # int | Number of items per page (optional) (default to 20)
    sort_by = 'sort_by_example' # str | Field to sort by (optional)
    sort_order = desc # str | Sort order (ascending or descending) (optional) (default to desc)
    search = 'search_example' # str | Search term to filter results (optional)

    try:
        # Get customer analytics including growth and segmentation.     Query params: start_date, end_date, group_by, segment_by
        api_response = api_instance.list_companies_analytics_customers(company_id, page=page, limit=limit, sort_by=sort_by, sort_order=sort_order, search=search)
        print("The response of CompaniesApi->list_companies_analytics_customers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompaniesApi->list_companies_analytics_customers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **page** | **int**| Page number for pagination | [optional] [default to 1]
 **limit** | **int**| Number of items per page | [optional] [default to 20]
 **sort_by** | **str**| Field to sort by | [optional] 
 **sort_order** | **str**| Sort order (ascending or descending) | [optional] [default to desc]
 **search** | **str**| Search term to filter results | [optional] 

### Return type

[**ListCompaniesAnalyticsAssets200Response**](ListCompaniesAnalyticsAssets200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved companies |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_companies_analytics_dashboard**
> ListCompaniesAnalyticsAssets200Response list_companies_analytics_dashboard(company_id, page=page, limit=limit, sort_by=sort_by, sort_order=sort_order, search=search)

Get comprehensive dashboard analytics for seller dashboard.     Query params: start_date, end_date, period (day/week/month/quarter)

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.list_companies_analytics_assets200_response import ListCompaniesAnalyticsAssets200Response
from spartera_api_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.spartera.com
# See configuration.py for a list of all supported configuration parameters.
configuration = spartera_api_sdk.Configuration(
    host = "https://api.spartera.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with spartera_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spartera_api_sdk.CompaniesApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    page = 1 # int | Page number for pagination (optional) (default to 1)
    limit = 20 # int | Number of items per page (optional) (default to 20)
    sort_by = 'sort_by_example' # str | Field to sort by (optional)
    sort_order = desc # str | Sort order (ascending or descending) (optional) (default to desc)
    search = 'search_example' # str | Search term to filter results (optional)

    try:
        # Get comprehensive dashboard analytics for seller dashboard.     Query params: start_date, end_date, period (day/week/month/quarter)
        api_response = api_instance.list_companies_analytics_dashboard(company_id, page=page, limit=limit, sort_by=sort_by, sort_order=sort_order, search=search)
        print("The response of CompaniesApi->list_companies_analytics_dashboard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompaniesApi->list_companies_analytics_dashboard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **page** | **int**| Page number for pagination | [optional] [default to 1]
 **limit** | **int**| Number of items per page | [optional] [default to 20]
 **sort_by** | **str**| Field to sort by | [optional] 
 **sort_order** | **str**| Sort order (ascending or descending) | [optional] [default to desc]
 **search** | **str**| Search term to filter results | [optional] 

### Return type

[**ListCompaniesAnalyticsAssets200Response**](ListCompaniesAnalyticsAssets200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved companies |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_companies_analytics_metrics**
> ListCompaniesAnalyticsAssets200Response list_companies_analytics_metrics(company_id, page=page, limit=limit, sort_by=sort_by, sort_order=sort_order, search=search)

Get summary metrics (counts only). No date params needed — returns all-time totals.     Performance: < 0.1s

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.list_companies_analytics_assets200_response import ListCompaniesAnalyticsAssets200Response
from spartera_api_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.spartera.com
# See configuration.py for a list of all supported configuration parameters.
configuration = spartera_api_sdk.Configuration(
    host = "https://api.spartera.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with spartera_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spartera_api_sdk.CompaniesApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    page = 1 # int | Page number for pagination (optional) (default to 1)
    limit = 20 # int | Number of items per page (optional) (default to 20)
    sort_by = 'sort_by_example' # str | Field to sort by (optional)
    sort_order = desc # str | Sort order (ascending or descending) (optional) (default to desc)
    search = 'search_example' # str | Search term to filter results (optional)

    try:
        # Get summary metrics (counts only). No date params needed — returns all-time totals.     Performance: < 0.1s
        api_response = api_instance.list_companies_analytics_metrics(company_id, page=page, limit=limit, sort_by=sort_by, sort_order=sort_order, search=search)
        print("The response of CompaniesApi->list_companies_analytics_metrics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompaniesApi->list_companies_analytics_metrics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **page** | **int**| Page number for pagination | [optional] [default to 1]
 **limit** | **int**| Number of items per page | [optional] [default to 20]
 **sort_by** | **str**| Field to sort by | [optional] 
 **sort_order** | **str**| Sort order (ascending or descending) | [optional] [default to desc]
 **search** | **str**| Search term to filter results | [optional] 

### Return type

[**ListCompaniesAnalyticsAssets200Response**](ListCompaniesAnalyticsAssets200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved companies |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_companies_analytics_sales**
> ListCompaniesAnalyticsAssets200Response list_companies_analytics_sales(company_id, page=page, limit=limit, sort_by=sort_by, sort_order=sort_order, search=search)

Get sales over time analytics.     Query params: start_date, end_date, group_by (day/week/month/quarter), metrics

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.list_companies_analytics_assets200_response import ListCompaniesAnalyticsAssets200Response
from spartera_api_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.spartera.com
# See configuration.py for a list of all supported configuration parameters.
configuration = spartera_api_sdk.Configuration(
    host = "https://api.spartera.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with spartera_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spartera_api_sdk.CompaniesApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    page = 1 # int | Page number for pagination (optional) (default to 1)
    limit = 20 # int | Number of items per page (optional) (default to 20)
    sort_by = 'sort_by_example' # str | Field to sort by (optional)
    sort_order = desc # str | Sort order (ascending or descending) (optional) (default to desc)
    search = 'search_example' # str | Search term to filter results (optional)

    try:
        # Get sales over time analytics.     Query params: start_date, end_date, group_by (day/week/month/quarter), metrics
        api_response = api_instance.list_companies_analytics_sales(company_id, page=page, limit=limit, sort_by=sort_by, sort_order=sort_order, search=search)
        print("The response of CompaniesApi->list_companies_analytics_sales:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompaniesApi->list_companies_analytics_sales: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **page** | **int**| Page number for pagination | [optional] [default to 1]
 **limit** | **int**| Number of items per page | [optional] [default to 20]
 **sort_by** | **str**| Field to sort by | [optional] 
 **sort_order** | **str**| Sort order (ascending or descending) | [optional] [default to desc]
 **search** | **str**| Search term to filter results | [optional] 

### Return type

[**ListCompaniesAnalyticsAssets200Response**](ListCompaniesAnalyticsAssets200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved companies |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_companies_objects**
> ListCompaniesAnalyticsAssets200Response list_companies_objects(company_id, page=page, limit=limit, sort_by=sort_by, sort_order=sort_order, search=search)

Get all objects (connections, assets) of a single company

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.list_companies_analytics_assets200_response import ListCompaniesAnalyticsAssets200Response
from spartera_api_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.spartera.com
# See configuration.py for a list of all supported configuration parameters.
configuration = spartera_api_sdk.Configuration(
    host = "https://api.spartera.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with spartera_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spartera_api_sdk.CompaniesApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    page = 1 # int | Page number for pagination (optional) (default to 1)
    limit = 20 # int | Number of items per page (optional) (default to 20)
    sort_by = 'sort_by_example' # str | Field to sort by (optional)
    sort_order = desc # str | Sort order (ascending or descending) (optional) (default to desc)
    search = 'search_example' # str | Search term to filter results (optional)

    try:
        # Get all objects (connections, assets) of a single company
        api_response = api_instance.list_companies_objects(company_id, page=page, limit=limit, sort_by=sort_by, sort_order=sort_order, search=search)
        print("The response of CompaniesApi->list_companies_objects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompaniesApi->list_companies_objects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **page** | **int**| Page number for pagination | [optional] [default to 1]
 **limit** | **int**| Number of items per page | [optional] [default to 20]
 **sort_by** | **str**| Field to sort by | [optional] 
 **sort_order** | **str**| Sort order (ascending or descending) | [optional] [default to desc]
 **search** | **str**| Search term to filter results | [optional] 

### Return type

[**ListCompaniesAnalyticsAssets200Response**](ListCompaniesAnalyticsAssets200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved companies |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_companies_requests_usage**
> ListCompaniesAnalyticsAssets200Response list_companies_requests_usage(company_id, page=page, limit=limit, sort_by=sort_by, sort_order=sort_order, search=search)

Get company request usage data for a specific month.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.list_companies_analytics_assets200_response import ListCompaniesAnalyticsAssets200Response
from spartera_api_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.spartera.com
# See configuration.py for a list of all supported configuration parameters.
configuration = spartera_api_sdk.Configuration(
    host = "https://api.spartera.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with spartera_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spartera_api_sdk.CompaniesApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    page = 1 # int | Page number for pagination (optional) (default to 1)
    limit = 20 # int | Number of items per page (optional) (default to 20)
    sort_by = 'sort_by_example' # str | Field to sort by (optional)
    sort_order = desc # str | Sort order (ascending or descending) (optional) (default to desc)
    search = 'search_example' # str | Search term to filter results (optional)

    try:
        # Get company request usage data for a specific month.
        api_response = api_instance.list_companies_requests_usage(company_id, page=page, limit=limit, sort_by=sort_by, sort_order=sort_order, search=search)
        print("The response of CompaniesApi->list_companies_requests_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompaniesApi->list_companies_requests_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **page** | **int**| Page number for pagination | [optional] [default to 1]
 **limit** | **int**| Number of items per page | [optional] [default to 20]
 **sort_by** | **str**| Field to sort by | [optional] 
 **sort_order** | **str**| Sort order (ascending or descending) | [optional] [default to desc]
 **search** | **str**| Search term to filter results | [optional] 

### Return type

[**ListCompaniesAnalyticsAssets200Response**](ListCompaniesAnalyticsAssets200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved companies |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_companies**
> UpdateCompanies200Response update_companies(company_id, companies_update)

Update an existing company by ID

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.companies_update import CompaniesUpdate
from spartera_api_sdk.models.update_companies200_response import UpdateCompanies200Response
from spartera_api_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.spartera.com
# See configuration.py for a list of all supported configuration parameters.
configuration = spartera_api_sdk.Configuration(
    host = "https://api.spartera.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with spartera_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spartera_api_sdk.CompaniesApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    companies_update = spartera_api_sdk.CompaniesUpdate() # CompaniesUpdate | 

    try:
        # Update an existing company by ID
        api_response = api_instance.update_companies(company_id, companies_update)
        print("The response of CompaniesApi->update_companies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompaniesApi->update_companies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **companies_update** | [**CompaniesUpdate**](CompaniesUpdate.md)|  | 

### Return type

[**UpdateCompanies200Response**](UpdateCompanies200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated companies |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**400** | Invalid input |  -  |
**409** | Resource conflict (duplicate, constraint violation) |  -  |
**422** | Request well-formed but semantically invalid |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

