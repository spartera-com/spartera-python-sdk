# spartera_api_sdk.AssetPriceHistoryApi

All URIs are relative to *https://api.spartera.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companies_company_id_assets_asset_id_prices_active_get**](AssetPriceHistoryApi.md#companies_company_id_assets_asset_id_prices_active_get) | **GET** /companies/{company_id}/assets/{asset_id}/prices/active | Get the currently active price for an asset
[**companies_company_id_assets_asset_id_prices_aph_id_delete**](AssetPriceHistoryApi.md#companies_company_id_assets_asset_id_prices_aph_id_delete) | **DELETE** /companies/{company_id}/assets/{asset_id}/prices/{aph_id} | Delete single price history record by ID
[**companies_company_id_assets_asset_id_prices_aph_id_get**](AssetPriceHistoryApi.md#companies_company_id_assets_asset_id_prices_aph_id_get) | **GET** /companies/{company_id}/assets/{asset_id}/prices/{aph_id} | Get single price history record by ID
[**companies_company_id_assets_asset_id_prices_aph_id_patch**](AssetPriceHistoryApi.md#companies_company_id_assets_asset_id_prices_aph_id_patch) | **PATCH** /companies/{company_id}/assets/{asset_id}/prices/{aph_id} | Update an existing price history record by ID
[**companies_company_id_assets_asset_id_prices_calculate_credits_post**](AssetPriceHistoryApi.md#companies_company_id_assets_asset_id_prices_calculate_credits_post) | **POST** /companies/{company_id}/assets/{asset_id}/prices/calculate_credits | Calculate the credit equivalent for a given USD price without saving
[**companies_company_id_assets_asset_id_prices_discount_post**](AssetPriceHistoryApi.md#companies_company_id_assets_asset_id_prices_discount_post) | **POST** /companies/{company_id}/assets/{asset_id}/prices/discount | POST /companies/{company_id}/assets/{asset_id}/prices/discount
[**companies_company_id_assets_asset_id_prices_get**](AssetPriceHistoryApi.md#companies_company_id_assets_asset_id_prices_get) | **GET** /companies/{company_id}/assets/{asset_id}/prices | Get all price history records for a specific asset
[**companies_company_id_assets_asset_id_prices_post**](AssetPriceHistoryApi.md#companies_company_id_assets_asset_id_prices_post) | **POST** /companies/{company_id}/assets/{asset_id}/prices | Create a new price history record for an asset


# **companies_company_id_assets_asset_id_prices_active_get**
> CompaniesCompanyIdAssetsAssetIdPricesGet200Response companies_company_id_assets_asset_id_prices_active_get(company_id, asset_id)

Get the currently active price for an asset

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.companies_company_id_assets_asset_id_prices_get200_response import CompaniesCompanyIdAssetsAssetIdPricesGet200Response
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

[**CompaniesCompanyIdAssetsAssetIdPricesGet200Response**](CompaniesCompanyIdAssetsAssetIdPricesGet200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved asset price history |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_assets_asset_id_prices_aph_id_delete**
> CompaniesCompanyIdAssetsAssetIdPricesAphIdDelete200Response companies_company_id_assets_asset_id_prices_aph_id_delete(company_id, asset_id, aph_id)

Delete single price history record by ID

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.companies_company_id_assets_asset_id_prices_aph_id_delete200_response import CompaniesCompanyIdAssetsAssetIdPricesAphIdDelete200Response
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

[**CompaniesCompanyIdAssetsAssetIdPricesAphIdDelete200Response**](CompaniesCompanyIdAssetsAssetIdPricesAphIdDelete200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully deleted asset price history |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_assets_asset_id_prices_aph_id_get**
> CompaniesCompanyIdAssetsAssetIdPricesAphIdGet200Response companies_company_id_assets_asset_id_prices_aph_id_get(company_id, asset_id, aph_id)

Get single price history record by ID

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.companies_company_id_assets_asset_id_prices_aph_id_get200_response import CompaniesCompanyIdAssetsAssetIdPricesAphIdGet200Response
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

[**CompaniesCompanyIdAssetsAssetIdPricesAphIdGet200Response**](CompaniesCompanyIdAssetsAssetIdPricesAphIdGet200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved asset price history |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_assets_asset_id_prices_aph_id_patch**
> CompaniesCompanyIdAssetsAssetIdPricesAphIdPatch200Response companies_company_id_assets_asset_id_prices_aph_id_patch(company_id, asset_id, aph_id, asset_price_history_update)

Update an existing price history record by ID

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.asset_price_history_update import AssetPriceHistoryUpdate
from spartera_api_sdk.models.companies_company_id_assets_asset_id_prices_aph_id_patch200_response import CompaniesCompanyIdAssetsAssetIdPricesAphIdPatch200Response
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
    api_instance = spartera_api_sdk.AssetPriceHistoryApi(api_client)
    company_id = 'company_id_example' # str | 
    asset_id = 'asset_id_example' # str | 
    aph_id = 'aph_id_example' # str | 
    asset_price_history_update = spartera_api_sdk.AssetPriceHistoryUpdate() # AssetPriceHistoryUpdate | 

    try:
        # Update an existing price history record by ID
        api_response = api_instance.companies_company_id_assets_asset_id_prices_aph_id_patch(company_id, asset_id, aph_id, asset_price_history_update)
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
 **asset_price_history_update** | [**AssetPriceHistoryUpdate**](AssetPriceHistoryUpdate.md)|  | 

### Return type

[**CompaniesCompanyIdAssetsAssetIdPricesAphIdPatch200Response**](CompaniesCompanyIdAssetsAssetIdPricesAphIdPatch200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated asset price history |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**400** | Invalid input |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_assets_asset_id_prices_calculate_credits_post**
> CompaniesCompanyIdAssetsAssetIdPricesPost200Response companies_company_id_assets_asset_id_prices_calculate_credits_post(company_id, asset_id, asset_price_history_input)

Calculate the credit equivalent for a given USD price without saving

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.asset_price_history_input import AssetPriceHistoryInput
from spartera_api_sdk.models.companies_company_id_assets_asset_id_prices_post200_response import CompaniesCompanyIdAssetsAssetIdPricesPost200Response
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
    api_instance = spartera_api_sdk.AssetPriceHistoryApi(api_client)
    company_id = 'company_id_example' # str | 
    asset_id = 'asset_id_example' # str | 
    asset_price_history_input = spartera_api_sdk.AssetPriceHistoryInput() # AssetPriceHistoryInput | 

    try:
        # Calculate the credit equivalent for a given USD price without saving
        api_response = api_instance.companies_company_id_assets_asset_id_prices_calculate_credits_post(company_id, asset_id, asset_price_history_input)
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
 **asset_price_history_input** | [**AssetPriceHistoryInput**](AssetPriceHistoryInput.md)|  | 

### Return type

[**CompaniesCompanyIdAssetsAssetIdPricesPost200Response**](CompaniesCompanyIdAssetsAssetIdPricesPost200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created asset price history |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**400** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_assets_asset_id_prices_discount_post**
> CompaniesCompanyIdAssetsAssetIdPricesPost200Response companies_company_id_assets_asset_id_prices_discount_post(company_id, asset_id, asset_price_history_input)

POST /companies/{company_id}/assets/{asset_id}/prices/discount

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.asset_price_history_input import AssetPriceHistoryInput
from spartera_api_sdk.models.companies_company_id_assets_asset_id_prices_post200_response import CompaniesCompanyIdAssetsAssetIdPricesPost200Response
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
    api_instance = spartera_api_sdk.AssetPriceHistoryApi(api_client)
    company_id = 'company_id_example' # str | 
    asset_id = 'asset_id_example' # str | 
    asset_price_history_input = spartera_api_sdk.AssetPriceHistoryInput() # AssetPriceHistoryInput | 

    try:
        # POST /companies/{company_id}/assets/{asset_id}/prices/discount
        api_response = api_instance.companies_company_id_assets_asset_id_prices_discount_post(company_id, asset_id, asset_price_history_input)
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
 **asset_price_history_input** | [**AssetPriceHistoryInput**](AssetPriceHistoryInput.md)|  | 

### Return type

[**CompaniesCompanyIdAssetsAssetIdPricesPost200Response**](CompaniesCompanyIdAssetsAssetIdPricesPost200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created asset price history |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**400** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_assets_asset_id_prices_get**
> CompaniesCompanyIdAssetsAssetIdPricesGet200Response companies_company_id_assets_asset_id_prices_get(company_id, asset_id)

Get all price history records for a specific asset

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.companies_company_id_assets_asset_id_prices_get200_response import CompaniesCompanyIdAssetsAssetIdPricesGet200Response
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

[**CompaniesCompanyIdAssetsAssetIdPricesGet200Response**](CompaniesCompanyIdAssetsAssetIdPricesGet200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved asset price history |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_assets_asset_id_prices_post**
> CompaniesCompanyIdAssetsAssetIdPricesPost200Response companies_company_id_assets_asset_id_prices_post(company_id, asset_id, asset_price_history_input)

Create a new price history record for an asset

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.asset_price_history_input import AssetPriceHistoryInput
from spartera_api_sdk.models.companies_company_id_assets_asset_id_prices_post200_response import CompaniesCompanyIdAssetsAssetIdPricesPost200Response
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
    api_instance = spartera_api_sdk.AssetPriceHistoryApi(api_client)
    company_id = 'company_id_example' # str | 
    asset_id = 'asset_id_example' # str | 
    asset_price_history_input = spartera_api_sdk.AssetPriceHistoryInput() # AssetPriceHistoryInput | 

    try:
        # Create a new price history record for an asset
        api_response = api_instance.companies_company_id_assets_asset_id_prices_post(company_id, asset_id, asset_price_history_input)
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
 **asset_price_history_input** | [**AssetPriceHistoryInput**](AssetPriceHistoryInput.md)|  | 

### Return type

[**CompaniesCompanyIdAssetsAssetIdPricesPost200Response**](CompaniesCompanyIdAssetsAssetIdPricesPost200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created asset price history |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**400** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

