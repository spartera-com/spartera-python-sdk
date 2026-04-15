# spartera_api_sdk.AssetPriceHistoryApi

All URIs are relative to *https://api.spartera.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_asset_price_history**](AssetPriceHistoryApi.md#create_asset_price_history) | **POST** /companies/{company_id}/assets/{asset_id}/prices | Create a new price history record for an asset
[**create_asset_price_history_prices_calculate_credits**](AssetPriceHistoryApi.md#create_asset_price_history_prices_calculate_credits) | **POST** /companies/{company_id}/assets/{asset_id}/prices/calculate_credits | Calculate the credit equivalent for a given USD price without saving
[**create_asset_price_history_prices_discount**](AssetPriceHistoryApi.md#create_asset_price_history_prices_discount) | **POST** /companies/{company_id}/assets/{asset_id}/prices/discount | POST /companies/{company_id}/assets/{asset_id}/prices/discount
[**delete_asset_price_history**](AssetPriceHistoryApi.md#delete_asset_price_history) | **DELETE** /companies/{company_id}/assets/{asset_id}/prices/{aph_id} | Delete single price history record by ID
[**get_asset_price_history_by_id**](AssetPriceHistoryApi.md#get_asset_price_history_by_id) | **GET** /companies/{company_id}/assets/{asset_id}/prices | Get all price history records for a specific asset
[**get_asset_price_history_by_id_assets_prices**](AssetPriceHistoryApi.md#get_asset_price_history_by_id_assets_prices) | **GET** /companies/{company_id}/assets/{asset_id}/prices/{aph_id} | Get single price history record by ID
[**get_asset_price_history_by_id_prices_active**](AssetPriceHistoryApi.md#get_asset_price_history_by_id_prices_active) | **GET** /companies/{company_id}/assets/{asset_id}/prices/active | Get the currently active price for an asset
[**update_asset_price_history**](AssetPriceHistoryApi.md#update_asset_price_history) | **PATCH** /companies/{company_id}/assets/{asset_id}/prices/{aph_id} | Update an existing price history record by ID


# **create_asset_price_history**
> CreateAssetPriceHistory200Response create_asset_price_history(company_id, asset_id, asset_price_history_input)

Create a new price history record for an asset

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.asset_price_history_input import AssetPriceHistoryInput
from spartera_api_sdk.models.create_asset_price_history200_response import CreateAssetPriceHistory200Response
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
    company_id = 'company_id_example' # str | Unique identifier for the Company
    asset_id = 'asset_id_example' # str | Unique identifier for the Asset
    asset_price_history_input = spartera_api_sdk.AssetPriceHistoryInput() # AssetPriceHistoryInput | 

    try:
        # Create a new price history record for an asset
        api_response = api_instance.create_asset_price_history(company_id, asset_id, asset_price_history_input)
        print("The response of AssetPriceHistoryApi->create_asset_price_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetPriceHistoryApi->create_asset_price_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **asset_id** | **str**| Unique identifier for the Asset | 
 **asset_price_history_input** | [**AssetPriceHistoryInput**](AssetPriceHistoryInput.md)|  | 

### Return type

[**CreateAssetPriceHistory200Response**](CreateAssetPriceHistory200Response.md)

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
**409** | Resource conflict (duplicate, constraint violation) |  -  |
**422** | Request well-formed but semantically invalid |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_asset_price_history_prices_calculate_credits**
> CreateAssetPriceHistory200Response create_asset_price_history_prices_calculate_credits(company_id, asset_id, asset_price_history_input)

Calculate the credit equivalent for a given USD price without saving

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.asset_price_history_input import AssetPriceHistoryInput
from spartera_api_sdk.models.create_asset_price_history200_response import CreateAssetPriceHistory200Response
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
    company_id = 'company_id_example' # str | Unique identifier for the Company
    asset_id = 'asset_id_example' # str | Unique identifier for the Asset
    asset_price_history_input = spartera_api_sdk.AssetPriceHistoryInput() # AssetPriceHistoryInput | 

    try:
        # Calculate the credit equivalent for a given USD price without saving
        api_response = api_instance.create_asset_price_history_prices_calculate_credits(company_id, asset_id, asset_price_history_input)
        print("The response of AssetPriceHistoryApi->create_asset_price_history_prices_calculate_credits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetPriceHistoryApi->create_asset_price_history_prices_calculate_credits: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **asset_id** | **str**| Unique identifier for the Asset | 
 **asset_price_history_input** | [**AssetPriceHistoryInput**](AssetPriceHistoryInput.md)|  | 

### Return type

[**CreateAssetPriceHistory200Response**](CreateAssetPriceHistory200Response.md)

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
**409** | Resource conflict (duplicate, constraint violation) |  -  |
**422** | Request well-formed but semantically invalid |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_asset_price_history_prices_discount**
> CreateAssetPriceHistory200Response create_asset_price_history_prices_discount(company_id, asset_id, asset_price_history_input)

POST /companies/{company_id}/assets/{asset_id}/prices/discount

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.asset_price_history_input import AssetPriceHistoryInput
from spartera_api_sdk.models.create_asset_price_history200_response import CreateAssetPriceHistory200Response
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
    company_id = 'company_id_example' # str | Unique identifier for the Company
    asset_id = 'asset_id_example' # str | Unique identifier for the Asset
    asset_price_history_input = spartera_api_sdk.AssetPriceHistoryInput() # AssetPriceHistoryInput | 

    try:
        # POST /companies/{company_id}/assets/{asset_id}/prices/discount
        api_response = api_instance.create_asset_price_history_prices_discount(company_id, asset_id, asset_price_history_input)
        print("The response of AssetPriceHistoryApi->create_asset_price_history_prices_discount:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetPriceHistoryApi->create_asset_price_history_prices_discount: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **asset_id** | **str**| Unique identifier for the Asset | 
 **asset_price_history_input** | [**AssetPriceHistoryInput**](AssetPriceHistoryInput.md)|  | 

### Return type

[**CreateAssetPriceHistory200Response**](CreateAssetPriceHistory200Response.md)

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
**409** | Resource conflict (duplicate, constraint violation) |  -  |
**422** | Request well-formed but semantically invalid |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_asset_price_history**
> DeleteAssetPriceHistory200Response delete_asset_price_history(company_id, asset_id, aph_id)

Delete single price history record by ID

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.delete_asset_price_history200_response import DeleteAssetPriceHistory200Response
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
    company_id = 'company_id_example' # str | Unique identifier for the Company
    asset_id = 'asset_id_example' # str | Unique identifier for the Asset
    aph_id = 'aph_id_example' # str | Unique identifier for the Aph

    try:
        # Delete single price history record by ID
        api_response = api_instance.delete_asset_price_history(company_id, asset_id, aph_id)
        print("The response of AssetPriceHistoryApi->delete_asset_price_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetPriceHistoryApi->delete_asset_price_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **asset_id** | **str**| Unique identifier for the Asset | 
 **aph_id** | **str**| Unique identifier for the Aph | 

### Return type

[**DeleteAssetPriceHistory200Response**](DeleteAssetPriceHistory200Response.md)

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
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_price_history_by_id**
> GetAssetPriceHistoryById200Response get_asset_price_history_by_id(company_id, asset_id)

Get all price history records for a specific asset

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.get_asset_price_history_by_id200_response import GetAssetPriceHistoryById200Response
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
    company_id = 'company_id_example' # str | Unique identifier for the Company
    asset_id = 'asset_id_example' # str | Unique identifier for the Asset

    try:
        # Get all price history records for a specific asset
        api_response = api_instance.get_asset_price_history_by_id(company_id, asset_id)
        print("The response of AssetPriceHistoryApi->get_asset_price_history_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetPriceHistoryApi->get_asset_price_history_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **asset_id** | **str**| Unique identifier for the Asset | 

### Return type

[**GetAssetPriceHistoryById200Response**](GetAssetPriceHistoryById200Response.md)

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
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_price_history_by_id_assets_prices**
> GetAssetPriceHistoryById200Response get_asset_price_history_by_id_assets_prices(company_id, asset_id, aph_id)

Get single price history record by ID

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.get_asset_price_history_by_id200_response import GetAssetPriceHistoryById200Response
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
    company_id = 'company_id_example' # str | Unique identifier for the Company
    asset_id = 'asset_id_example' # str | Unique identifier for the Asset
    aph_id = 'aph_id_example' # str | Unique identifier for the Aph

    try:
        # Get single price history record by ID
        api_response = api_instance.get_asset_price_history_by_id_assets_prices(company_id, asset_id, aph_id)
        print("The response of AssetPriceHistoryApi->get_asset_price_history_by_id_assets_prices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetPriceHistoryApi->get_asset_price_history_by_id_assets_prices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **asset_id** | **str**| Unique identifier for the Asset | 
 **aph_id** | **str**| Unique identifier for the Aph | 

### Return type

[**GetAssetPriceHistoryById200Response**](GetAssetPriceHistoryById200Response.md)

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
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_price_history_by_id_prices_active**
> GetAssetPriceHistoryById200Response get_asset_price_history_by_id_prices_active(company_id, asset_id)

Get the currently active price for an asset

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.get_asset_price_history_by_id200_response import GetAssetPriceHistoryById200Response
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
    company_id = 'company_id_example' # str | Unique identifier for the Company
    asset_id = 'asset_id_example' # str | Unique identifier for the Asset

    try:
        # Get the currently active price for an asset
        api_response = api_instance.get_asset_price_history_by_id_prices_active(company_id, asset_id)
        print("The response of AssetPriceHistoryApi->get_asset_price_history_by_id_prices_active:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetPriceHistoryApi->get_asset_price_history_by_id_prices_active: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **asset_id** | **str**| Unique identifier for the Asset | 

### Return type

[**GetAssetPriceHistoryById200Response**](GetAssetPriceHistoryById200Response.md)

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
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_asset_price_history**
> UpdateAssetPriceHistory200Response update_asset_price_history(company_id, asset_id, aph_id, asset_price_history_update)

Update an existing price history record by ID

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.asset_price_history_update import AssetPriceHistoryUpdate
from spartera_api_sdk.models.update_asset_price_history200_response import UpdateAssetPriceHistory200Response
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
    company_id = 'company_id_example' # str | Unique identifier for the Company
    asset_id = 'asset_id_example' # str | Unique identifier for the Asset
    aph_id = 'aph_id_example' # str | Unique identifier for the Aph
    asset_price_history_update = spartera_api_sdk.AssetPriceHistoryUpdate() # AssetPriceHistoryUpdate | 

    try:
        # Update an existing price history record by ID
        api_response = api_instance.update_asset_price_history(company_id, asset_id, aph_id, asset_price_history_update)
        print("The response of AssetPriceHistoryApi->update_asset_price_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetPriceHistoryApi->update_asset_price_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **asset_id** | **str**| Unique identifier for the Asset | 
 **aph_id** | **str**| Unique identifier for the Aph | 
 **asset_price_history_update** | [**AssetPriceHistoryUpdate**](AssetPriceHistoryUpdate.md)|  | 

### Return type

[**UpdateAssetPriceHistory200Response**](UpdateAssetPriceHistory200Response.md)

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
**409** | Resource conflict (duplicate, constraint violation) |  -  |
**422** | Request well-formed but semantically invalid |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

