# spartera_api_sdk.AssetsApi

All URIs are relative to *https://api.spartera.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_assets**](AssetsApi.md#create_assets) | **POST** /companies/{company_id}/assets | Create a new asset
[**create_assets_analyze**](AssetsApi.md#create_assets_analyze) | **POST** /analyze/{company_handle}/assets/{asset_slug} | Process (analyze) an asset with dynamic rate limiting applied via decorator.
[**create_assets_scan_column**](AssetsApi.md#create_assets_scan_column) | **POST** /companies/{company_id}/assets/{asset_id}/scan_column | Scan a column in the asset&#39;s table to retrieve distinct values      Request Body:         column (str): Column name to scan         limit (int, optional): Maximum distinct values to return (default 1000, max 5000)      Returns:         Flask Response with scan results
[**create_assets_test**](AssetsApi.md#create_assets_test) | **POST** /companies/{company_id}/assets/{asset_id}/test | POST /companies/{company_id}/assets/{asset_id}/test
[**delete_assets**](AssetsApi.md#delete_assets) | **DELETE** /companies/{company_id}/assets/{asset_id} | Delete single asset by ID
[**get_assets_by_id**](AssetsApi.md#get_assets_by_id) | **GET** /companies/{company_id}/assets/{asset_id} | Get single asset by ID
[**get_assets_by_id2**](AssetsApi.md#get_assets_by_id2) | **GET** /companies/{company_id}/assets/{asset_id}/statistics | Get statistics for a specific asset (public endpoint)
[**get_assets_by_id_analyze**](AssetsApi.md#get_assets_by_id_analyze) | **GET** /analyze/{company_handle}/assets/{asset_slug} | Process (analyze) an asset with dynamic rate limiting applied via decorator.
[**get_assets_by_id_infoschema**](AssetsApi.md#get_assets_by_id_infoschema) | **GET** /companies/{company_id}/assets/{asset_id}/infoschema | Get the information schema for a specific asset&#39;s table
[**get_assets_by_id_infoschema_save**](AssetsApi.md#get_assets_by_id_infoschema_save) | **GET** /companies/{company_id}/assets/{asset_id}/infoschema/save | Retrieve and save an asset&#39;s information schema
[**get_assets_by_id_predicted_price**](AssetsApi.md#get_assets_by_id_predicted_price) | **GET** /companies/{company_id}/assets/{asset_id}/predicted_price | Get AI-predicted pricing for a specific asset
[**get_assets_by_id_statistics**](AssetsApi.md#get_assets_by_id_statistics) | **GET** /companies/{company_id}/assets/statistics | Get statistics for all assets the user has access to
[**get_assets_by_id_test**](AssetsApi.md#get_assets_by_id_test) | **GET** /companies/{company_id}/assets/{asset_id}/test | GET /companies/{company_id}/assets/{asset_id}/test
[**list_assets**](AssetsApi.md#list_assets) | **GET** /companies/{company_id}/assets | Get all assets for a specific company
[**list_assets_search**](AssetsApi.md#list_assets_search) | **GET** /companies/{company_id}/assets/search | Search and filter assets with advanced options      Query Parameters:         q: Search query string         category: Filter by category         sport: Filter by sport tag         sort_by: Sort field (name|recent|popular|trending)         limit: Number of results (default 20, max 100)         offset: Offset for pagination         include_recommended: Include recommendations (true/false)         include_schema: Include asset_schema in response (true/false, default false)
[**update_assets**](AssetsApi.md#update_assets) | **PATCH** /companies/{company_id}/assets/{asset_id} | Update an existing asset by ID


# **create_assets**
> CreateAssetsAnalyze200Response create_assets(company_id, assets_input, page=page, limit=limit, sort_by=sort_by, sort_order=sort_order, search=search)

Create a new asset

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.assets_input import AssetsInput
from spartera_api_sdk.models.create_assets_analyze200_response import CreateAssetsAnalyze200Response
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
    api_instance = spartera_api_sdk.AssetsApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    assets_input = spartera_api_sdk.AssetsInput() # AssetsInput | 
    page = 1 # int | Page number for pagination (optional) (default to 1)
    limit = 20 # int | Number of items per page (optional) (default to 20)
    sort_by = 'sort_by_example' # str | Field to sort by (optional)
    sort_order = desc # str | Sort order (ascending or descending) (optional) (default to desc)
    search = 'search_example' # str | Search term to filter results (optional)

    try:
        # Create a new asset
        api_response = api_instance.create_assets(company_id, assets_input, page=page, limit=limit, sort_by=sort_by, sort_order=sort_order, search=search)
        print("The response of AssetsApi->create_assets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->create_assets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **assets_input** | [**AssetsInput**](AssetsInput.md)|  | 
 **page** | **int**| Page number for pagination | [optional] [default to 1]
 **limit** | **int**| Number of items per page | [optional] [default to 20]
 **sort_by** | **str**| Field to sort by | [optional] 
 **sort_order** | **str**| Sort order (ascending or descending) | [optional] [default to desc]
 **search** | **str**| Search term to filter results | [optional] 

### Return type

[**CreateAssetsAnalyze200Response**](CreateAssetsAnalyze200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created assets |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**400** | Invalid input |  -  |
**409** | Resource conflict (duplicate, constraint violation) |  -  |
**422** | Request well-formed but semantically invalid |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_assets_analyze**
> CreateAssetsAnalyze200Response create_assets_analyze(asset_slug, company_handle, assets_input)

Process (analyze) an asset with dynamic rate limiting applied via decorator.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.assets_input import AssetsInput
from spartera_api_sdk.models.create_assets_analyze200_response import CreateAssetsAnalyze200Response
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
    api_instance = spartera_api_sdk.AssetsApi(api_client)
    asset_slug = 'asset_slug_example' # str | URL-friendly slug for the Asset
    company_handle = 'company_handle_example' # str | Human-readable handle for the Company
    assets_input = spartera_api_sdk.AssetsInput() # AssetsInput | 

    try:
        # Process (analyze) an asset with dynamic rate limiting applied via decorator.
        api_response = api_instance.create_assets_analyze(asset_slug, company_handle, assets_input)
        print("The response of AssetsApi->create_assets_analyze:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->create_assets_analyze: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_slug** | **str**| URL-friendly slug for the Asset | 
 **company_handle** | **str**| Human-readable handle for the Company | 
 **assets_input** | [**AssetsInput**](AssetsInput.md)|  | 

### Return type

[**CreateAssetsAnalyze200Response**](CreateAssetsAnalyze200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created assets |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**400** | Invalid input |  -  |
**409** | Resource conflict (duplicate, constraint violation) |  -  |
**422** | Request well-formed but semantically invalid |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_assets_scan_column**
> CreateAssetsAnalyze200Response create_assets_scan_column(company_id, asset_id, assets_input)

Scan a column in the asset's table to retrieve distinct values      Request Body:         column (str): Column name to scan         limit (int, optional): Maximum distinct values to return (default 1000, max 5000)      Returns:         Flask Response with scan results

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.assets_input import AssetsInput
from spartera_api_sdk.models.create_assets_analyze200_response import CreateAssetsAnalyze200Response
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
    api_instance = spartera_api_sdk.AssetsApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    asset_id = 'asset_id_example' # str | Unique identifier for the Asset
    assets_input = spartera_api_sdk.AssetsInput() # AssetsInput | 

    try:
        # Scan a column in the asset's table to retrieve distinct values      Request Body:         column (str): Column name to scan         limit (int, optional): Maximum distinct values to return (default 1000, max 5000)      Returns:         Flask Response with scan results
        api_response = api_instance.create_assets_scan_column(company_id, asset_id, assets_input)
        print("The response of AssetsApi->create_assets_scan_column:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->create_assets_scan_column: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **asset_id** | **str**| Unique identifier for the Asset | 
 **assets_input** | [**AssetsInput**](AssetsInput.md)|  | 

### Return type

[**CreateAssetsAnalyze200Response**](CreateAssetsAnalyze200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created assets |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**400** | Invalid input |  -  |
**409** | Resource conflict (duplicate, constraint violation) |  -  |
**422** | Request well-formed but semantically invalid |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_assets_test**
> CreateAssetsAnalyze200Response create_assets_test(company_id, asset_id, assets_input)

POST /companies/{company_id}/assets/{asset_id}/test

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.assets_input import AssetsInput
from spartera_api_sdk.models.create_assets_analyze200_response import CreateAssetsAnalyze200Response
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
    api_instance = spartera_api_sdk.AssetsApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    asset_id = 'asset_id_example' # str | Unique identifier for the Asset
    assets_input = spartera_api_sdk.AssetsInput() # AssetsInput | 

    try:
        # POST /companies/{company_id}/assets/{asset_id}/test
        api_response = api_instance.create_assets_test(company_id, asset_id, assets_input)
        print("The response of AssetsApi->create_assets_test:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->create_assets_test: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **asset_id** | **str**| Unique identifier for the Asset | 
 **assets_input** | [**AssetsInput**](AssetsInput.md)|  | 

### Return type

[**CreateAssetsAnalyze200Response**](CreateAssetsAnalyze200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created assets |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**400** | Invalid input |  -  |
**409** | Resource conflict (duplicate, constraint violation) |  -  |
**422** | Request well-formed but semantically invalid |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_assets**
> DeleteAssets200Response delete_assets(company_id, asset_id)

Delete single asset by ID

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.delete_assets200_response import DeleteAssets200Response
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
    api_instance = spartera_api_sdk.AssetsApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    asset_id = 'asset_id_example' # str | Unique identifier for the Asset

    try:
        # Delete single asset by ID
        api_response = api_instance.delete_assets(company_id, asset_id)
        print("The response of AssetsApi->delete_assets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->delete_assets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **asset_id** | **str**| Unique identifier for the Asset | 

### Return type

[**DeleteAssets200Response**](DeleteAssets200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully deleted assets |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_assets_by_id**
> GetAssetsByIdAnalyze200Response get_assets_by_id(company_id, asset_id)

Get single asset by ID

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.get_assets_by_id_analyze200_response import GetAssetsByIdAnalyze200Response
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
    api_instance = spartera_api_sdk.AssetsApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    asset_id = 'asset_id_example' # str | Unique identifier for the Asset

    try:
        # Get single asset by ID
        api_response = api_instance.get_assets_by_id(company_id, asset_id)
        print("The response of AssetsApi->get_assets_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->get_assets_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **asset_id** | **str**| Unique identifier for the Asset | 

### Return type

[**GetAssetsByIdAnalyze200Response**](GetAssetsByIdAnalyze200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved assets |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_assets_by_id2**
> GetAssetsByIdAnalyze200Response get_assets_by_id2(company_id, asset_id)

Get statistics for a specific asset (public endpoint)

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.get_assets_by_id_analyze200_response import GetAssetsByIdAnalyze200Response
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
    api_instance = spartera_api_sdk.AssetsApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    asset_id = 'asset_id_example' # str | Unique identifier for the Asset

    try:
        # Get statistics for a specific asset (public endpoint)
        api_response = api_instance.get_assets_by_id2(company_id, asset_id)
        print("The response of AssetsApi->get_assets_by_id2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->get_assets_by_id2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **asset_id** | **str**| Unique identifier for the Asset | 

### Return type

[**GetAssetsByIdAnalyze200Response**](GetAssetsByIdAnalyze200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved assets |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_assets_by_id_analyze**
> GetAssetsByIdAnalyze200Response get_assets_by_id_analyze(asset_slug, company_handle)

Process (analyze) an asset with dynamic rate limiting applied via decorator.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.get_assets_by_id_analyze200_response import GetAssetsByIdAnalyze200Response
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
    api_instance = spartera_api_sdk.AssetsApi(api_client)
    asset_slug = 'asset_slug_example' # str | URL-friendly slug for the Asset
    company_handle = 'company_handle_example' # str | Human-readable handle for the Company

    try:
        # Process (analyze) an asset with dynamic rate limiting applied via decorator.
        api_response = api_instance.get_assets_by_id_analyze(asset_slug, company_handle)
        print("The response of AssetsApi->get_assets_by_id_analyze:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->get_assets_by_id_analyze: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_slug** | **str**| URL-friendly slug for the Asset | 
 **company_handle** | **str**| Human-readable handle for the Company | 

### Return type

[**GetAssetsByIdAnalyze200Response**](GetAssetsByIdAnalyze200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved assets |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_assets_by_id_infoschema**
> GetAssetsByIdAnalyze200Response get_assets_by_id_infoschema(company_id, asset_id)

Get the information schema for a specific asset's table

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.get_assets_by_id_analyze200_response import GetAssetsByIdAnalyze200Response
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
    api_instance = spartera_api_sdk.AssetsApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    asset_id = 'asset_id_example' # str | Unique identifier for the Asset

    try:
        # Get the information schema for a specific asset's table
        api_response = api_instance.get_assets_by_id_infoschema(company_id, asset_id)
        print("The response of AssetsApi->get_assets_by_id_infoschema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->get_assets_by_id_infoschema: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **asset_id** | **str**| Unique identifier for the Asset | 

### Return type

[**GetAssetsByIdAnalyze200Response**](GetAssetsByIdAnalyze200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved assets |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_assets_by_id_infoschema_save**
> GetAssetsByIdAnalyze200Response get_assets_by_id_infoschema_save(company_id, asset_id)

Retrieve and save an asset's information schema

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.get_assets_by_id_analyze200_response import GetAssetsByIdAnalyze200Response
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
    api_instance = spartera_api_sdk.AssetsApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    asset_id = 'asset_id_example' # str | Unique identifier for the Asset

    try:
        # Retrieve and save an asset's information schema
        api_response = api_instance.get_assets_by_id_infoschema_save(company_id, asset_id)
        print("The response of AssetsApi->get_assets_by_id_infoschema_save:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->get_assets_by_id_infoschema_save: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **asset_id** | **str**| Unique identifier for the Asset | 

### Return type

[**GetAssetsByIdAnalyze200Response**](GetAssetsByIdAnalyze200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved assets |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_assets_by_id_predicted_price**
> GetAssetsByIdAnalyze200Response get_assets_by_id_predicted_price(company_id, asset_id)

Get AI-predicted pricing for a specific asset

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.get_assets_by_id_analyze200_response import GetAssetsByIdAnalyze200Response
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
    api_instance = spartera_api_sdk.AssetsApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    asset_id = 'asset_id_example' # str | Unique identifier for the Asset

    try:
        # Get AI-predicted pricing for a specific asset
        api_response = api_instance.get_assets_by_id_predicted_price(company_id, asset_id)
        print("The response of AssetsApi->get_assets_by_id_predicted_price:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->get_assets_by_id_predicted_price: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **asset_id** | **str**| Unique identifier for the Asset | 

### Return type

[**GetAssetsByIdAnalyze200Response**](GetAssetsByIdAnalyze200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved assets |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_assets_by_id_statistics**
> GetAssetsByIdAnalyze200Response get_assets_by_id_statistics(company_id)

Get statistics for all assets the user has access to

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.get_assets_by_id_analyze200_response import GetAssetsByIdAnalyze200Response
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
    api_instance = spartera_api_sdk.AssetsApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company

    try:
        # Get statistics for all assets the user has access to
        api_response = api_instance.get_assets_by_id_statistics(company_id)
        print("The response of AssetsApi->get_assets_by_id_statistics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->get_assets_by_id_statistics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 

### Return type

[**GetAssetsByIdAnalyze200Response**](GetAssetsByIdAnalyze200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved assets |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_assets_by_id_test**
> GetAssetsByIdAnalyze200Response get_assets_by_id_test(company_id, asset_id)

GET /companies/{company_id}/assets/{asset_id}/test

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.get_assets_by_id_analyze200_response import GetAssetsByIdAnalyze200Response
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
    api_instance = spartera_api_sdk.AssetsApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    asset_id = 'asset_id_example' # str | Unique identifier for the Asset

    try:
        # GET /companies/{company_id}/assets/{asset_id}/test
        api_response = api_instance.get_assets_by_id_test(company_id, asset_id)
        print("The response of AssetsApi->get_assets_by_id_test:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->get_assets_by_id_test: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **asset_id** | **str**| Unique identifier for the Asset | 

### Return type

[**GetAssetsByIdAnalyze200Response**](GetAssetsByIdAnalyze200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved assets |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_assets**
> ListAssets200Response list_assets(company_id, page=page, limit=limit, sort_by=sort_by, sort_order=sort_order, search=search)

Get all assets for a specific company

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.list_assets200_response import ListAssets200Response
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
    api_instance = spartera_api_sdk.AssetsApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    page = 1 # int | Page number for pagination (optional) (default to 1)
    limit = 20 # int | Number of items per page (optional) (default to 20)
    sort_by = 'sort_by_example' # str | Field to sort by (optional)
    sort_order = desc # str | Sort order (ascending or descending) (optional) (default to desc)
    search = 'search_example' # str | Search term to filter results (optional)

    try:
        # Get all assets for a specific company
        api_response = api_instance.list_assets(company_id, page=page, limit=limit, sort_by=sort_by, sort_order=sort_order, search=search)
        print("The response of AssetsApi->list_assets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->list_assets: %s\n" % e)
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

[**ListAssets200Response**](ListAssets200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved assets |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_assets_search**
> ListAssets200Response list_assets_search(company_id, page=page, limit=limit, sort_by=sort_by, sort_order=sort_order, search=search)

Search and filter assets with advanced options      Query Parameters:         q: Search query string         category: Filter by category         sport: Filter by sport tag         sort_by: Sort field (name|recent|popular|trending)         limit: Number of results (default 20, max 100)         offset: Offset for pagination         include_recommended: Include recommendations (true/false)         include_schema: Include asset_schema in response (true/false, default false)

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.list_assets200_response import ListAssets200Response
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
    api_instance = spartera_api_sdk.AssetsApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    page = 1 # int | Page number for pagination (optional) (default to 1)
    limit = 20 # int | Number of items per page (optional) (default to 20)
    sort_by = 'sort_by_example' # str | Field to sort by (optional)
    sort_order = desc # str | Sort order (ascending or descending) (optional) (default to desc)
    search = 'search_example' # str | Search term to filter results (optional)

    try:
        # Search and filter assets with advanced options      Query Parameters:         q: Search query string         category: Filter by category         sport: Filter by sport tag         sort_by: Sort field (name|recent|popular|trending)         limit: Number of results (default 20, max 100)         offset: Offset for pagination         include_recommended: Include recommendations (true/false)         include_schema: Include asset_schema in response (true/false, default false)
        api_response = api_instance.list_assets_search(company_id, page=page, limit=limit, sort_by=sort_by, sort_order=sort_order, search=search)
        print("The response of AssetsApi->list_assets_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->list_assets_search: %s\n" % e)
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

[**ListAssets200Response**](ListAssets200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved assets |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_assets**
> UpdateAssets200Response update_assets(company_id, asset_id, assets_update)

Update an existing asset by ID

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.assets_update import AssetsUpdate
from spartera_api_sdk.models.update_assets200_response import UpdateAssets200Response
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
    api_instance = spartera_api_sdk.AssetsApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    asset_id = 'asset_id_example' # str | Unique identifier for the Asset
    assets_update = spartera_api_sdk.AssetsUpdate() # AssetsUpdate | 

    try:
        # Update an existing asset by ID
        api_response = api_instance.update_assets(company_id, asset_id, assets_update)
        print("The response of AssetsApi->update_assets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->update_assets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **asset_id** | **str**| Unique identifier for the Asset | 
 **assets_update** | [**AssetsUpdate**](AssetsUpdate.md)|  | 

### Return type

[**UpdateAssets200Response**](UpdateAssets200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated assets |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**400** | Invalid input |  -  |
**409** | Resource conflict (duplicate, constraint violation) |  -  |
**422** | Request well-formed but semantically invalid |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

