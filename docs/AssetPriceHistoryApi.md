# spartera_api_sdk.AssetPriceHistoryApi

All URIs are relative to *https://api.spartera.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companies_company_id_assets_asset_id_prices_active_get**](AssetPriceHistoryApi.md#companies_company_id_assets_asset_id_prices_active_get) | **GET** /companies/{company_id}/assets/{asset_id}/prices/active | Get the currently active price for an asset
[**companies_company_id_assets_asset_id_prices_aph_id_delete**](AssetPriceHistoryApi.md#companies_company_id_assets_asset_id_prices_aph_id_delete) | **DELETE** /companies/{company_id}/assets/{asset_id}/prices/{aph_id} | Delete single price history record by ID
[**companies_company_id_assets_asset_id_prices_aph_id_get**](AssetPriceHistoryApi.md#companies_company_id_assets_asset_id_prices_aph_id_get) | **GET** /companies/{company_id}/assets/{asset_id}/prices/{aph_id} | Get single price history record by ID
[**companies_company_id_assets_asset_id_prices_aph_id_patch**](AssetPriceHistoryApi.md#companies_company_id_assets_asset_id_prices_aph_id_patch) | **PATCH** /companies/{company_id}/assets/{asset_id}/prices/{aph_id} | Update an existing price history record by ID
[**companies_company_id_assets_asset_id_prices_calculate_credits_post**](AssetPriceHistoryApi.md#companies_company_id_assets_asset_id_prices_calculate_credits_post) | **POST** /companies/{company_id}/assets/{asset_id}/prices/calculate_credits | Calculate the credit equivalent for a given USD price without saving
[**companies_company_id_assets_asset_id_prices_discount_post**](AssetPriceHistoryApi.md#companies_company_id_assets_asset_id_prices_discount_post) | **POST** /companies/{company_id}/assets/{asset_id}/prices/discount | Apply a discount to the active price for an asset
[**companies_company_id_assets_asset_id_prices_get**](AssetPriceHistoryApi.md#companies_company_id_assets_asset_id_prices_get) | **GET** /companies/{company_id}/assets/{asset_id}/prices | Get all price history records for a specific asset
[**companies_company_id_assets_asset_id_prices_post**](AssetPriceHistoryApi.md#companies_company_id_assets_asset_id_prices_post) | **POST** /companies/{company_id}/assets/{asset_id}/prices | Create a new price history record for an asset


# **companies_company_id_assets_asset_id_prices_active_get**
> object companies_company_id_assets_asset_id_prices_active_get(company_id, asset_id)

Get the currently active price for an asset

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import spartera_api_sdk
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = spartera_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with spartera_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spartera_api_sdk.AssetPriceHistoryApi(api_client)
    company_id = 'company_id_example' # str | 
    asset_id = 'asset_id_example' # str | 

    try:
        # Get the currently active price for an asset
        api_response = api_instance.companies_company_id_assets_asset_id_prices_active_get(company_id, asset_id)
        print("The response of AssetPriceHistoryApi->companies_company_id_assets_asset_id_prices_active_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetPriceHistoryApi->companies_company_id_assets_asset_id_prices_active_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  | 
 **asset_id** | **str**|  | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_assets_asset_id_prices_aph_id_delete**
> object companies_company_id_assets_asset_id_prices_aph_id_delete(company_id, asset_id, aph_id)

Delete single price history record by ID

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import spartera_api_sdk
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = spartera_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with spartera_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spartera_api_sdk.AssetPriceHistoryApi(api_client)
    company_id = 'company_id_example' # str | 
    asset_id = 'asset_id_example' # str | 
    aph_id = 'aph_id_example' # str | 

    try:
        # Delete single price history record by ID
        api_response = api_instance.companies_company_id_assets_asset_id_prices_aph_id_delete(company_id, asset_id, aph_id)
        print("The response of AssetPriceHistoryApi->companies_company_id_assets_asset_id_prices_aph_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetPriceHistoryApi->companies_company_id_assets_asset_id_prices_aph_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  | 
 **asset_id** | **str**|  | 
 **aph_id** | **str**|  | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_assets_asset_id_prices_aph_id_get**
> object companies_company_id_assets_asset_id_prices_aph_id_get(company_id, asset_id, aph_id)

Get single price history record by ID

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import spartera_api_sdk
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = spartera_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with spartera_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spartera_api_sdk.AssetPriceHistoryApi(api_client)
    company_id = 'company_id_example' # str | 
    asset_id = 'asset_id_example' # str | 
    aph_id = 'aph_id_example' # str | 

    try:
        # Get single price history record by ID
        api_response = api_instance.companies_company_id_assets_asset_id_prices_aph_id_get(company_id, asset_id, aph_id)
        print("The response of AssetPriceHistoryApi->companies_company_id_assets_asset_id_prices_aph_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetPriceHistoryApi->companies_company_id_assets_asset_id_prices_aph_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  | 
 **asset_id** | **str**|  | 
 **aph_id** | **str**|  | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_assets_asset_id_prices_aph_id_patch**
> object companies_company_id_assets_asset_id_prices_aph_id_patch(company_id, asset_id, aph_id)

Update an existing price history record by ID

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import spartera_api_sdk
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = spartera_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with spartera_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spartera_api_sdk.AssetPriceHistoryApi(api_client)
    company_id = 'company_id_example' # str | 
    asset_id = 'asset_id_example' # str | 
    aph_id = 'aph_id_example' # str | 

    try:
        # Update an existing price history record by ID
        api_response = api_instance.companies_company_id_assets_asset_id_prices_aph_id_patch(company_id, asset_id, aph_id)
        print("The response of AssetPriceHistoryApi->companies_company_id_assets_asset_id_prices_aph_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetPriceHistoryApi->companies_company_id_assets_asset_id_prices_aph_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  | 
 **asset_id** | **str**|  | 
 **aph_id** | **str**|  | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**400** | Invalid input |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_assets_asset_id_prices_calculate_credits_post**
> object companies_company_id_assets_asset_id_prices_calculate_credits_post(company_id, asset_id)

Calculate the credit equivalent for a given USD price without saving

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import spartera_api_sdk
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = spartera_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with spartera_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spartera_api_sdk.AssetPriceHistoryApi(api_client)
    company_id = 'company_id_example' # str | 
    asset_id = 'asset_id_example' # str | 

    try:
        # Calculate the credit equivalent for a given USD price without saving
        api_response = api_instance.companies_company_id_assets_asset_id_prices_calculate_credits_post(company_id, asset_id)
        print("The response of AssetPriceHistoryApi->companies_company_id_assets_asset_id_prices_calculate_credits_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetPriceHistoryApi->companies_company_id_assets_asset_id_prices_calculate_credits_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  | 
 **asset_id** | **str**|  | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**400** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_assets_asset_id_prices_discount_post**
> object companies_company_id_assets_asset_id_prices_discount_post(company_id, asset_id)

Apply a discount to the active price for an asset

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import spartera_api_sdk
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = spartera_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with spartera_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spartera_api_sdk.AssetPriceHistoryApi(api_client)
    company_id = 'company_id_example' # str | 
    asset_id = 'asset_id_example' # str | 

    try:
        # Apply a discount to the active price for an asset
        api_response = api_instance.companies_company_id_assets_asset_id_prices_discount_post(company_id, asset_id)
        print("The response of AssetPriceHistoryApi->companies_company_id_assets_asset_id_prices_discount_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetPriceHistoryApi->companies_company_id_assets_asset_id_prices_discount_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  | 
 **asset_id** | **str**|  | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**400** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_assets_asset_id_prices_get**
> object companies_company_id_assets_asset_id_prices_get(company_id, asset_id)

Get all price history records for a specific asset

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import spartera_api_sdk
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = spartera_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with spartera_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spartera_api_sdk.AssetPriceHistoryApi(api_client)
    company_id = 'company_id_example' # str | 
    asset_id = 'asset_id_example' # str | 

    try:
        # Get all price history records for a specific asset
        api_response = api_instance.companies_company_id_assets_asset_id_prices_get(company_id, asset_id)
        print("The response of AssetPriceHistoryApi->companies_company_id_assets_asset_id_prices_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetPriceHistoryApi->companies_company_id_assets_asset_id_prices_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  | 
 **asset_id** | **str**|  | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_assets_asset_id_prices_post**
> object companies_company_id_assets_asset_id_prices_post(company_id, asset_id)

Create a new price history record for an asset

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import spartera_api_sdk
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = spartera_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with spartera_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spartera_api_sdk.AssetPriceHistoryApi(api_client)
    company_id = 'company_id_example' # str | 
    asset_id = 'asset_id_example' # str | 

    try:
        # Create a new price history record for an asset
        api_response = api_instance.companies_company_id_assets_asset_id_prices_post(company_id, asset_id)
        print("The response of AssetPriceHistoryApi->companies_company_id_assets_asset_id_prices_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetPriceHistoryApi->companies_company_id_assets_asset_id_prices_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  | 
 **asset_id** | **str**|  | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**400** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

