# spartera_api_sdk.CompaniesApi

All URIs are relative to *https://api.spartera.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companies_company_id_analytics_assets_get**](CompaniesApi.md#companies_company_id_analytics_assets_get) | **GET** /companies/{company_id}/analytics/assets | Get asset performance analytics     Query params: start_date, end_date, limit, sort_by, include
[**companies_company_id_analytics_customers_get**](CompaniesApi.md#companies_company_id_analytics_customers_get) | **GET** /companies/{company_id}/analytics/customers | Get customer analytics including growth and segmentation     Query params: start_date, end_date, group_by, segment_by
[**companies_company_id_analytics_dashboard_get**](CompaniesApi.md#companies_company_id_analytics_dashboard_get) | **GET** /companies/{company_id}/analytics/dashboard | Get comprehensive dashboard analytics for seller dashboard     Includes all metrics needed for dashboard charts in one call     Query params: start_date, end_date, period (day/week/month/quarter)
[**companies_company_id_analytics_sales_get**](CompaniesApi.md#companies_company_id_analytics_sales_get) | **GET** /companies/{company_id}/analytics/sales | Get sales over time analytics     Query params: start_date, end_date, group_by (day/week/month/quarter), metrics
[**companies_company_id_get**](CompaniesApi.md#companies_company_id_get) | **GET** /companies/{company_id} | Get details of the requestor&#39;s own company
[**companies_company_id_objects_get**](CompaniesApi.md#companies_company_id_objects_get) | **GET** /companies/{company_id}/objects | Get all objects (connections, assets) of a single company
[**companies_company_id_patch**](CompaniesApi.md#companies_company_id_patch) | **PATCH** /companies/{company_id} | Update an existing company by ID
[**companies_company_id_requests_plan_get**](CompaniesApi.md#companies_company_id_requests_plan_get) | **GET** /companies/{company_id}/requests/plan | Get the total number of requests allocated in the company&#39;s current subscription plan.
[**companies_company_id_requests_usage_get**](CompaniesApi.md#companies_company_id_requests_usage_get) | **GET** /companies/{company_id}/requests/usage | Get company request usage data for a specific month. Returns JSON metrics by default or CSV logs when download parameter is included.


# **companies_company_id_analytics_assets_get**
> CompaniesCompanyIdAnalyticsAssetsGet200Response companies_company_id_analytics_assets_get(company_id)

Get asset performance analytics     Query params: start_date, end_date, limit, sort_by, include

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.companies_company_id_analytics_assets_get200_response import CompaniesCompanyIdAnalyticsAssetsGet200Response
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
    company_id = 'company_id_example' # str | 

    try:
        # Get asset performance analytics     Query params: start_date, end_date, limit, sort_by, include
        api_response = api_instance.companies_company_id_analytics_assets_get(company_id)
        print("The response of CompaniesApi->companies_company_id_analytics_assets_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompaniesApi->companies_company_id_analytics_assets_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  | 

### Return type

[**CompaniesCompanyIdAnalyticsAssetsGet200Response**](CompaniesCompanyIdAnalyticsAssetsGet200Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_analytics_customers_get**
> CompaniesCompanyIdAnalyticsAssetsGet200Response companies_company_id_analytics_customers_get(company_id)

Get customer analytics including growth and segmentation     Query params: start_date, end_date, group_by, segment_by

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.companies_company_id_analytics_assets_get200_response import CompaniesCompanyIdAnalyticsAssetsGet200Response
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
    company_id = 'company_id_example' # str | 

    try:
        # Get customer analytics including growth and segmentation     Query params: start_date, end_date, group_by, segment_by
        api_response = api_instance.companies_company_id_analytics_customers_get(company_id)
        print("The response of CompaniesApi->companies_company_id_analytics_customers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompaniesApi->companies_company_id_analytics_customers_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  | 

### Return type

[**CompaniesCompanyIdAnalyticsAssetsGet200Response**](CompaniesCompanyIdAnalyticsAssetsGet200Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_analytics_dashboard_get**
> CompaniesCompanyIdAnalyticsAssetsGet200Response companies_company_id_analytics_dashboard_get(company_id)

Get comprehensive dashboard analytics for seller dashboard     Includes all metrics needed for dashboard charts in one call     Query params: start_date, end_date, period (day/week/month/quarter)

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.companies_company_id_analytics_assets_get200_response import CompaniesCompanyIdAnalyticsAssetsGet200Response
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
    company_id = 'company_id_example' # str | 

    try:
        # Get comprehensive dashboard analytics for seller dashboard     Includes all metrics needed for dashboard charts in one call     Query params: start_date, end_date, period (day/week/month/quarter)
        api_response = api_instance.companies_company_id_analytics_dashboard_get(company_id)
        print("The response of CompaniesApi->companies_company_id_analytics_dashboard_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompaniesApi->companies_company_id_analytics_dashboard_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  | 

### Return type

[**CompaniesCompanyIdAnalyticsAssetsGet200Response**](CompaniesCompanyIdAnalyticsAssetsGet200Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_analytics_sales_get**
> CompaniesCompanyIdAnalyticsAssetsGet200Response companies_company_id_analytics_sales_get(company_id)

Get sales over time analytics     Query params: start_date, end_date, group_by (day/week/month/quarter), metrics

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.companies_company_id_analytics_assets_get200_response import CompaniesCompanyIdAnalyticsAssetsGet200Response
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
    company_id = 'company_id_example' # str | 

    try:
        # Get sales over time analytics     Query params: start_date, end_date, group_by (day/week/month/quarter), metrics
        api_response = api_instance.companies_company_id_analytics_sales_get(company_id)
        print("The response of CompaniesApi->companies_company_id_analytics_sales_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompaniesApi->companies_company_id_analytics_sales_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  | 

### Return type

[**CompaniesCompanyIdAnalyticsAssetsGet200Response**](CompaniesCompanyIdAnalyticsAssetsGet200Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_get**
> CompaniesCompanyIdGet200Response companies_company_id_get(company_id)

Get details of the requestor's own company

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.companies_company_id_get200_response import CompaniesCompanyIdGet200Response
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
    company_id = 'company_id_example' # str | 

    try:
        # Get details of the requestor's own company
        api_response = api_instance.companies_company_id_get(company_id)
        print("The response of CompaniesApi->companies_company_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompaniesApi->companies_company_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  | 

### Return type

[**CompaniesCompanyIdGet200Response**](CompaniesCompanyIdGet200Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_objects_get**
> CompaniesCompanyIdAnalyticsAssetsGet200Response companies_company_id_objects_get(company_id)

Get all objects (connections, assets) of a single company

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.companies_company_id_analytics_assets_get200_response import CompaniesCompanyIdAnalyticsAssetsGet200Response
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
    company_id = 'company_id_example' # str | 

    try:
        # Get all objects (connections, assets) of a single company
        api_response = api_instance.companies_company_id_objects_get(company_id)
        print("The response of CompaniesApi->companies_company_id_objects_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompaniesApi->companies_company_id_objects_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  | 

### Return type

[**CompaniesCompanyIdAnalyticsAssetsGet200Response**](CompaniesCompanyIdAnalyticsAssetsGet200Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_patch**
> CompaniesCompanyIdPatch200Response companies_company_id_patch(company_id, companies_update)

Update an existing company by ID

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.companies_company_id_patch200_response import CompaniesCompanyIdPatch200Response
from spartera_api_sdk.models.companies_update import CompaniesUpdate
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
    company_id = 'company_id_example' # str | 
    companies_update = spartera_api_sdk.CompaniesUpdate() # CompaniesUpdate | 

    try:
        # Update an existing company by ID
        api_response = api_instance.companies_company_id_patch(company_id, companies_update)
        print("The response of CompaniesApi->companies_company_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompaniesApi->companies_company_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  | 
 **companies_update** | [**CompaniesUpdate**](CompaniesUpdate.md)|  | 

### Return type

[**CompaniesCompanyIdPatch200Response**](CompaniesCompanyIdPatch200Response.md)

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
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_requests_plan_get**
> CompaniesCompanyIdAnalyticsAssetsGet200Response companies_company_id_requests_plan_get(company_id)

Get the total number of requests allocated in the company's current subscription plan.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.companies_company_id_analytics_assets_get200_response import CompaniesCompanyIdAnalyticsAssetsGet200Response
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
    company_id = 'company_id_example' # str | 

    try:
        # Get the total number of requests allocated in the company's current subscription plan.
        api_response = api_instance.companies_company_id_requests_plan_get(company_id)
        print("The response of CompaniesApi->companies_company_id_requests_plan_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompaniesApi->companies_company_id_requests_plan_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  | 

### Return type

[**CompaniesCompanyIdAnalyticsAssetsGet200Response**](CompaniesCompanyIdAnalyticsAssetsGet200Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_requests_usage_get**
> CompaniesCompanyIdAnalyticsAssetsGet200Response companies_company_id_requests_usage_get(company_id)

Get company request usage data for a specific month. Returns JSON metrics by default or CSV logs when download parameter is included.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.companies_company_id_analytics_assets_get200_response import CompaniesCompanyIdAnalyticsAssetsGet200Response
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
    company_id = 'company_id_example' # str | 

    try:
        # Get company request usage data for a specific month. Returns JSON metrics by default or CSV logs when download parameter is included.
        api_response = api_instance.companies_company_id_requests_usage_get(company_id)
        print("The response of CompaniesApi->companies_company_id_requests_usage_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompaniesApi->companies_company_id_requests_usage_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  | 

### Return type

[**CompaniesCompanyIdAnalyticsAssetsGet200Response**](CompaniesCompanyIdAnalyticsAssetsGet200Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

