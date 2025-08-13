# spartera_api_sdk.AssetsApi

All URIs are relative to *https://api.spartera.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analyze_company_handle_assets_asset_slug_get**](AssetsApi.md#analyze_company_handle_assets_asset_slug_get) | **GET** /analyze/{company_handle}/assets/{asset_slug} | Process (analyze) an asset.
[**companies_company_id_assets_asset_id_delete**](AssetsApi.md#companies_company_id_assets_asset_id_delete) | **DELETE** /companies/{company_id}/assets/{asset_id} | Delete single asset by ID
[**companies_company_id_assets_asset_id_get**](AssetsApi.md#companies_company_id_assets_asset_id_get) | **GET** /companies/{company_id}/assets/{asset_id} | Get single asset by ID
[**companies_company_id_assets_asset_id_infoschema_get**](AssetsApi.md#companies_company_id_assets_asset_id_infoschema_get) | **GET** /companies/{company_id}/assets/{asset_id}/infoschema | Get the information schema for a specific asset&#39;s table
[**companies_company_id_assets_asset_id_infoschema_save_get**](AssetsApi.md#companies_company_id_assets_asset_id_infoschema_save_get) | **GET** /companies/{company_id}/assets/{asset_id}/infoschema/save | Retrieve and save an asset&#39;s information schema
[**companies_company_id_assets_asset_id_patch**](AssetsApi.md#companies_company_id_assets_asset_id_patch) | **PATCH** /companies/{company_id}/assets/{asset_id} | Update an existing asset by ID
[**companies_company_id_assets_asset_id_predicted_price_get**](AssetsApi.md#companies_company_id_assets_asset_id_predicted_price_get) | **GET** /companies/{company_id}/assets/{asset_id}/predicted_price | Get AI-predicted pricing for a specific asset
[**companies_company_id_assets_asset_id_statistics_get**](AssetsApi.md#companies_company_id_assets_asset_id_statistics_get) | **GET** /companies/{company_id}/assets/{asset_id}/statistics | Get statistics for a specific asset (public endpoint)
[**companies_company_id_assets_asset_id_test_get**](AssetsApi.md#companies_company_id_assets_asset_id_test_get) | **GET** /companies/{company_id}/assets/{asset_id}/test | Test out an Asset (on a subset of data)
[**companies_company_id_assets_get**](AssetsApi.md#companies_company_id_assets_get) | **GET** /companies/{company_id}/assets | Get all assets for a specific company
[**companies_company_id_assets_post**](AssetsApi.md#companies_company_id_assets_post) | **POST** /companies/{company_id}/assets | Create a new asset
[**companies_company_id_assets_statistics_get**](AssetsApi.md#companies_company_id_assets_statistics_get) | **GET** /companies/{company_id}/assets/statistics | Get statistics for all assets the user has access to


# **analyze_company_handle_assets_asset_slug_get**
> AnalyzeCompanyHandleAssetsAssetSlugGet200Response analyze_company_handle_assets_asset_slug_get(asset_slug, company_handle)

Process (analyze) an asset.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.analyze_company_handle_assets_asset_slug_get200_response import AnalyzeCompanyHandleAssetsAssetSlugGet200Response
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
    asset_slug = 'asset_slug_example' # str | 
    company_handle = 'company_handle_example' # str | 

    try:
        # Process (analyze) an asset.
        api_response = api_instance.analyze_company_handle_assets_asset_slug_get(asset_slug, company_handle)
        print("The response of AssetsApi->analyze_company_handle_assets_asset_slug_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->analyze_company_handle_assets_asset_slug_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_slug** | **str**|  | 
 **company_handle** | **str**|  | 

### Return type

[**AnalyzeCompanyHandleAssetsAssetSlugGet200Response**](AnalyzeCompanyHandleAssetsAssetSlugGet200Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_assets_asset_id_delete**
> CompaniesCompanyIdAssetsAssetIdDelete200Response companies_company_id_assets_asset_id_delete(company_id, asset_id)

Delete single asset by ID

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.companies_company_id_assets_asset_id_delete200_response import CompaniesCompanyIdAssetsAssetIdDelete200Response
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
    company_id = 'company_id_example' # str | 
    asset_id = 'asset_id_example' # str | 

    try:
        # Delete single asset by ID
        api_response = api_instance.companies_company_id_assets_asset_id_delete(company_id, asset_id)
        print("The response of AssetsApi->companies_company_id_assets_asset_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->companies_company_id_assets_asset_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  | 
 **asset_id** | **str**|  | 

### Return type

[**CompaniesCompanyIdAssetsAssetIdDelete200Response**](CompaniesCompanyIdAssetsAssetIdDelete200Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_assets_asset_id_get**
> AnalyzeCompanyHandleAssetsAssetSlugGet200Response companies_company_id_assets_asset_id_get(company_id, asset_id)

Get single asset by ID

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.analyze_company_handle_assets_asset_slug_get200_response import AnalyzeCompanyHandleAssetsAssetSlugGet200Response
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
    company_id = 'company_id_example' # str | 
    asset_id = 'asset_id_example' # str | 

    try:
        # Get single asset by ID
        api_response = api_instance.companies_company_id_assets_asset_id_get(company_id, asset_id)
        print("The response of AssetsApi->companies_company_id_assets_asset_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->companies_company_id_assets_asset_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  | 
 **asset_id** | **str**|  | 

### Return type

[**AnalyzeCompanyHandleAssetsAssetSlugGet200Response**](AnalyzeCompanyHandleAssetsAssetSlugGet200Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_assets_asset_id_infoschema_get**
> CompaniesCompanyIdAssetsGet200Response companies_company_id_assets_asset_id_infoschema_get(company_id, asset_id)

Get the information schema for a specific asset's table

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.companies_company_id_assets_get200_response import CompaniesCompanyIdAssetsGet200Response
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
    company_id = 'company_id_example' # str | 
    asset_id = 'asset_id_example' # str | 

    try:
        # Get the information schema for a specific asset's table
        api_response = api_instance.companies_company_id_assets_asset_id_infoschema_get(company_id, asset_id)
        print("The response of AssetsApi->companies_company_id_assets_asset_id_infoschema_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->companies_company_id_assets_asset_id_infoschema_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  | 
 **asset_id** | **str**|  | 

### Return type

[**CompaniesCompanyIdAssetsGet200Response**](CompaniesCompanyIdAssetsGet200Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_assets_asset_id_infoschema_save_get**
> CompaniesCompanyIdAssetsGet200Response companies_company_id_assets_asset_id_infoschema_save_get(company_id, asset_id)

Retrieve and save an asset's information schema

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.companies_company_id_assets_get200_response import CompaniesCompanyIdAssetsGet200Response
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
    company_id = 'company_id_example' # str | 
    asset_id = 'asset_id_example' # str | 

    try:
        # Retrieve and save an asset's information schema
        api_response = api_instance.companies_company_id_assets_asset_id_infoschema_save_get(company_id, asset_id)
        print("The response of AssetsApi->companies_company_id_assets_asset_id_infoschema_save_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->companies_company_id_assets_asset_id_infoschema_save_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  | 
 **asset_id** | **str**|  | 

### Return type

[**CompaniesCompanyIdAssetsGet200Response**](CompaniesCompanyIdAssetsGet200Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_assets_asset_id_patch**
> CompaniesCompanyIdAssetsAssetIdPatch200Response companies_company_id_assets_asset_id_patch(company_id, asset_id, assets_update)

Update an existing asset by ID

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.assets_update import AssetsUpdate
from spartera_api_sdk.models.companies_company_id_assets_asset_id_patch200_response import CompaniesCompanyIdAssetsAssetIdPatch200Response
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
    company_id = 'company_id_example' # str | 
    asset_id = 'asset_id_example' # str | 
    assets_update = spartera_api_sdk.AssetsUpdate() # AssetsUpdate | 

    try:
        # Update an existing asset by ID
        api_response = api_instance.companies_company_id_assets_asset_id_patch(company_id, asset_id, assets_update)
        print("The response of AssetsApi->companies_company_id_assets_asset_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->companies_company_id_assets_asset_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  | 
 **asset_id** | **str**|  | 
 **assets_update** | [**AssetsUpdate**](AssetsUpdate.md)|  | 

### Return type

[**CompaniesCompanyIdAssetsAssetIdPatch200Response**](CompaniesCompanyIdAssetsAssetIdPatch200Response.md)

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
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_assets_asset_id_predicted_price_get**
> CompaniesCompanyIdAssetsGet200Response companies_company_id_assets_asset_id_predicted_price_get(company_id, asset_id)

Get AI-predicted pricing for a specific asset

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.companies_company_id_assets_get200_response import CompaniesCompanyIdAssetsGet200Response
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
    company_id = 'company_id_example' # str | 
    asset_id = 'asset_id_example' # str | 

    try:
        # Get AI-predicted pricing for a specific asset
        api_response = api_instance.companies_company_id_assets_asset_id_predicted_price_get(company_id, asset_id)
        print("The response of AssetsApi->companies_company_id_assets_asset_id_predicted_price_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->companies_company_id_assets_asset_id_predicted_price_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  | 
 **asset_id** | **str**|  | 

### Return type

[**CompaniesCompanyIdAssetsGet200Response**](CompaniesCompanyIdAssetsGet200Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_assets_asset_id_statistics_get**
> CompaniesCompanyIdAssetsGet200Response companies_company_id_assets_asset_id_statistics_get(company_id, asset_id)

Get statistics for a specific asset (public endpoint)

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.companies_company_id_assets_get200_response import CompaniesCompanyIdAssetsGet200Response
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
    company_id = 'company_id_example' # str | 
    asset_id = 'asset_id_example' # str | 

    try:
        # Get statistics for a specific asset (public endpoint)
        api_response = api_instance.companies_company_id_assets_asset_id_statistics_get(company_id, asset_id)
        print("The response of AssetsApi->companies_company_id_assets_asset_id_statistics_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->companies_company_id_assets_asset_id_statistics_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  | 
 **asset_id** | **str**|  | 

### Return type

[**CompaniesCompanyIdAssetsGet200Response**](CompaniesCompanyIdAssetsGet200Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_assets_asset_id_test_get**
> CompaniesCompanyIdAssetsGet200Response companies_company_id_assets_asset_id_test_get(company_id, asset_id)

Test out an Asset (on a subset of data)

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.companies_company_id_assets_get200_response import CompaniesCompanyIdAssetsGet200Response
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
    company_id = 'company_id_example' # str | 
    asset_id = 'asset_id_example' # str | 

    try:
        # Test out an Asset (on a subset of data)
        api_response = api_instance.companies_company_id_assets_asset_id_test_get(company_id, asset_id)
        print("The response of AssetsApi->companies_company_id_assets_asset_id_test_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->companies_company_id_assets_asset_id_test_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  | 
 **asset_id** | **str**|  | 

### Return type

[**CompaniesCompanyIdAssetsGet200Response**](CompaniesCompanyIdAssetsGet200Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_assets_get**
> CompaniesCompanyIdAssetsGet200Response companies_company_id_assets_get(company_id)

Get all assets for a specific company

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.companies_company_id_assets_get200_response import CompaniesCompanyIdAssetsGet200Response
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
    company_id = 'company_id_example' # str | 

    try:
        # Get all assets for a specific company
        api_response = api_instance.companies_company_id_assets_get(company_id)
        print("The response of AssetsApi->companies_company_id_assets_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->companies_company_id_assets_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  | 

### Return type

[**CompaniesCompanyIdAssetsGet200Response**](CompaniesCompanyIdAssetsGet200Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_assets_post**
> CompaniesCompanyIdAssetsPost200Response companies_company_id_assets_post(company_id, assets_input)

Create a new asset

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.assets_input import AssetsInput
from spartera_api_sdk.models.companies_company_id_assets_post200_response import CompaniesCompanyIdAssetsPost200Response
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
    company_id = 'company_id_example' # str | 
    assets_input = spartera_api_sdk.AssetsInput() # AssetsInput | 

    try:
        # Create a new asset
        api_response = api_instance.companies_company_id_assets_post(company_id, assets_input)
        print("The response of AssetsApi->companies_company_id_assets_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->companies_company_id_assets_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  | 
 **assets_input** | [**AssetsInput**](AssetsInput.md)|  | 

### Return type

[**CompaniesCompanyIdAssetsPost200Response**](CompaniesCompanyIdAssetsPost200Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_assets_statistics_get**
> CompaniesCompanyIdAssetsGet200Response companies_company_id_assets_statistics_get(company_id)

Get statistics for all assets the user has access to

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.companies_company_id_assets_get200_response import CompaniesCompanyIdAssetsGet200Response
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
    company_id = 'company_id_example' # str | 

    try:
        # Get statistics for all assets the user has access to
        api_response = api_instance.companies_company_id_assets_statistics_get(company_id)
        print("The response of AssetsApi->companies_company_id_assets_statistics_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->companies_company_id_assets_statistics_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  | 

### Return type

[**CompaniesCompanyIdAssetsGet200Response**](CompaniesCompanyIdAssetsGet200Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

