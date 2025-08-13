# spartera_api_sdk.FavoritesApi

All URIs are relative to *https://api.spartera.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companies_company_id_users_user_id_favorites_category_category_get**](FavoritesApi.md#companies_company_id_users_user_id_favorites_category_category_get) | **GET** /companies/{company_id}/users/{user_id}/favorites/category/{category} | Get all favorites for the specified user in a specific category
[**companies_company_id_users_user_id_favorites_check_asset_id_get**](FavoritesApi.md#companies_company_id_users_user_id_favorites_check_asset_id_get) | **GET** /companies/{company_id}/users/{user_id}/favorites/check/{asset_id} | Check if the specified user has favorited a specific asset
[**companies_company_id_users_user_id_favorites_favorite_id_delete**](FavoritesApi.md#companies_company_id_users_user_id_favorites_favorite_id_delete) | **DELETE** /companies/{company_id}/users/{user_id}/favorites/{favorite_id} | Delete single favorite by ID (unfavorite an asset)
[**companies_company_id_users_user_id_favorites_favorite_id_get**](FavoritesApi.md#companies_company_id_users_user_id_favorites_favorite_id_get) | **GET** /companies/{company_id}/users/{user_id}/favorites/{favorite_id} | Get single favorite by ID
[**companies_company_id_users_user_id_favorites_favorite_id_patch**](FavoritesApi.md#companies_company_id_users_user_id_favorites_favorite_id_patch) | **PATCH** /companies/{company_id}/users/{user_id}/favorites/{favorite_id} | Update an existing favorite by ID
[**companies_company_id_users_user_id_favorites_get**](FavoritesApi.md#companies_company_id_users_user_id_favorites_get) | **GET** /companies/{company_id}/users/{user_id}/favorites | Get a list of all favorites for a specific user
[**companies_company_id_users_user_id_favorites_post**](FavoritesApi.md#companies_company_id_users_user_id_favorites_post) | **POST** /companies/{company_id}/users/{user_id}/favorites | POST /companies/{company_id}/users/{user_id}/favorites
[**companies_company_id_users_user_id_favorites_uncategorized_get**](FavoritesApi.md#companies_company_id_users_user_id_favorites_uncategorized_get) | **GET** /companies/{company_id}/users/{user_id}/favorites/uncategorized | Get all favorites for the specified user that don&#39;t have a category


# **companies_company_id_users_user_id_favorites_category_category_get**
> CompaniesCompanyIdUsersUserIdFavoritesCategoryCategoryGet200Response companies_company_id_users_user_id_favorites_category_category_get(company_id, user_id, category)

Get all favorites for the specified user in a specific category

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.companies_company_id_users_user_id_favorites_category_category_get200_response import CompaniesCompanyIdUsersUserIdFavoritesCategoryCategoryGet200Response
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
    api_instance = spartera_api_sdk.FavoritesApi(api_client)
    company_id = 'company_id_example' # str | 
    user_id = 'user_id_example' # str | 
    category = 'category_example' # str | 

    try:
        # Get all favorites for the specified user in a specific category
        api_response = api_instance.companies_company_id_users_user_id_favorites_category_category_get(company_id, user_id, category)
        print("The response of FavoritesApi->companies_company_id_users_user_id_favorites_category_category_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FavoritesApi->companies_company_id_users_user_id_favorites_category_category_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  | 
 **user_id** | **str**|  | 
 **category** | **str**|  | 

### Return type

[**CompaniesCompanyIdUsersUserIdFavoritesCategoryCategoryGet200Response**](CompaniesCompanyIdUsersUserIdFavoritesCategoryCategoryGet200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved favorites |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_users_user_id_favorites_check_asset_id_get**
> CompaniesCompanyIdUsersUserIdFavoritesCategoryCategoryGet200Response companies_company_id_users_user_id_favorites_check_asset_id_get(company_id, user_id, asset_id)

Check if the specified user has favorited a specific asset

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.companies_company_id_users_user_id_favorites_category_category_get200_response import CompaniesCompanyIdUsersUserIdFavoritesCategoryCategoryGet200Response
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
    api_instance = spartera_api_sdk.FavoritesApi(api_client)
    company_id = 'company_id_example' # str | 
    user_id = 'user_id_example' # str | 
    asset_id = 'asset_id_example' # str | 

    try:
        # Check if the specified user has favorited a specific asset
        api_response = api_instance.companies_company_id_users_user_id_favorites_check_asset_id_get(company_id, user_id, asset_id)
        print("The response of FavoritesApi->companies_company_id_users_user_id_favorites_check_asset_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FavoritesApi->companies_company_id_users_user_id_favorites_check_asset_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  | 
 **user_id** | **str**|  | 
 **asset_id** | **str**|  | 

### Return type

[**CompaniesCompanyIdUsersUserIdFavoritesCategoryCategoryGet200Response**](CompaniesCompanyIdUsersUserIdFavoritesCategoryCategoryGet200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved favorites |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_users_user_id_favorites_favorite_id_delete**
> CompaniesCompanyIdUsersUserIdFavoritesFavoriteIdDelete200Response companies_company_id_users_user_id_favorites_favorite_id_delete(company_id, user_id, favorite_id)

Delete single favorite by ID (unfavorite an asset)

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.companies_company_id_users_user_id_favorites_favorite_id_delete200_response import CompaniesCompanyIdUsersUserIdFavoritesFavoriteIdDelete200Response
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
    api_instance = spartera_api_sdk.FavoritesApi(api_client)
    company_id = 'company_id_example' # str | 
    user_id = 'user_id_example' # str | 
    favorite_id = 'favorite_id_example' # str | 

    try:
        # Delete single favorite by ID (unfavorite an asset)
        api_response = api_instance.companies_company_id_users_user_id_favorites_favorite_id_delete(company_id, user_id, favorite_id)
        print("The response of FavoritesApi->companies_company_id_users_user_id_favorites_favorite_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FavoritesApi->companies_company_id_users_user_id_favorites_favorite_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  | 
 **user_id** | **str**|  | 
 **favorite_id** | **str**|  | 

### Return type

[**CompaniesCompanyIdUsersUserIdFavoritesFavoriteIdDelete200Response**](CompaniesCompanyIdUsersUserIdFavoritesFavoriteIdDelete200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully deleted favorites |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_users_user_id_favorites_favorite_id_get**
> CompaniesCompanyIdUsersUserIdFavoritesCategoryCategoryGet200Response companies_company_id_users_user_id_favorites_favorite_id_get(company_id, user_id, favorite_id)

Get single favorite by ID

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.companies_company_id_users_user_id_favorites_category_category_get200_response import CompaniesCompanyIdUsersUserIdFavoritesCategoryCategoryGet200Response
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
    api_instance = spartera_api_sdk.FavoritesApi(api_client)
    company_id = 'company_id_example' # str | 
    user_id = 'user_id_example' # str | 
    favorite_id = 'favorite_id_example' # str | 

    try:
        # Get single favorite by ID
        api_response = api_instance.companies_company_id_users_user_id_favorites_favorite_id_get(company_id, user_id, favorite_id)
        print("The response of FavoritesApi->companies_company_id_users_user_id_favorites_favorite_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FavoritesApi->companies_company_id_users_user_id_favorites_favorite_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  | 
 **user_id** | **str**|  | 
 **favorite_id** | **str**|  | 

### Return type

[**CompaniesCompanyIdUsersUserIdFavoritesCategoryCategoryGet200Response**](CompaniesCompanyIdUsersUserIdFavoritesCategoryCategoryGet200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved favorites |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_users_user_id_favorites_favorite_id_patch**
> CompaniesCompanyIdUsersUserIdFavoritesFavoriteIdPatch200Response companies_company_id_users_user_id_favorites_favorite_id_patch(company_id, user_id, favorite_id, favorites_update)

Update an existing favorite by ID

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.companies_company_id_users_user_id_favorites_favorite_id_patch200_response import CompaniesCompanyIdUsersUserIdFavoritesFavoriteIdPatch200Response
from spartera_api_sdk.models.favorites_update import FavoritesUpdate
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
    api_instance = spartera_api_sdk.FavoritesApi(api_client)
    company_id = 'company_id_example' # str | 
    user_id = 'user_id_example' # str | 
    favorite_id = 'favorite_id_example' # str | 
    favorites_update = spartera_api_sdk.FavoritesUpdate() # FavoritesUpdate | 

    try:
        # Update an existing favorite by ID
        api_response = api_instance.companies_company_id_users_user_id_favorites_favorite_id_patch(company_id, user_id, favorite_id, favorites_update)
        print("The response of FavoritesApi->companies_company_id_users_user_id_favorites_favorite_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FavoritesApi->companies_company_id_users_user_id_favorites_favorite_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  | 
 **user_id** | **str**|  | 
 **favorite_id** | **str**|  | 
 **favorites_update** | [**FavoritesUpdate**](FavoritesUpdate.md)|  | 

### Return type

[**CompaniesCompanyIdUsersUserIdFavoritesFavoriteIdPatch200Response**](CompaniesCompanyIdUsersUserIdFavoritesFavoriteIdPatch200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated favorites |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**400** | Invalid input |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_users_user_id_favorites_get**
> CompaniesCompanyIdUsersUserIdFavoritesGet200Response companies_company_id_users_user_id_favorites_get(company_id, user_id)

Get a list of all favorites for a specific user

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.companies_company_id_users_user_id_favorites_get200_response import CompaniesCompanyIdUsersUserIdFavoritesGet200Response
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
    api_instance = spartera_api_sdk.FavoritesApi(api_client)
    company_id = 'company_id_example' # str | 
    user_id = 'user_id_example' # str | 

    try:
        # Get a list of all favorites for a specific user
        api_response = api_instance.companies_company_id_users_user_id_favorites_get(company_id, user_id)
        print("The response of FavoritesApi->companies_company_id_users_user_id_favorites_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FavoritesApi->companies_company_id_users_user_id_favorites_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**CompaniesCompanyIdUsersUserIdFavoritesGet200Response**](CompaniesCompanyIdUsersUserIdFavoritesGet200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved favorites |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_users_user_id_favorites_post**
> CompaniesCompanyIdUsersUserIdFavoritesPost200Response companies_company_id_users_user_id_favorites_post(company_id, user_id, favorites_input)

POST /companies/{company_id}/users/{user_id}/favorites

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.companies_company_id_users_user_id_favorites_post200_response import CompaniesCompanyIdUsersUserIdFavoritesPost200Response
from spartera_api_sdk.models.favorites_input import FavoritesInput
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
    api_instance = spartera_api_sdk.FavoritesApi(api_client)
    company_id = 'company_id_example' # str | 
    user_id = 'user_id_example' # str | 
    favorites_input = spartera_api_sdk.FavoritesInput() # FavoritesInput | 

    try:
        # POST /companies/{company_id}/users/{user_id}/favorites
        api_response = api_instance.companies_company_id_users_user_id_favorites_post(company_id, user_id, favorites_input)
        print("The response of FavoritesApi->companies_company_id_users_user_id_favorites_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FavoritesApi->companies_company_id_users_user_id_favorites_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  | 
 **user_id** | **str**|  | 
 **favorites_input** | [**FavoritesInput**](FavoritesInput.md)|  | 

### Return type

[**CompaniesCompanyIdUsersUserIdFavoritesPost200Response**](CompaniesCompanyIdUsersUserIdFavoritesPost200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created favorites |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**400** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_users_user_id_favorites_uncategorized_get**
> CompaniesCompanyIdUsersUserIdFavoritesGet200Response companies_company_id_users_user_id_favorites_uncategorized_get(company_id, user_id)

Get all favorites for the specified user that don't have a category

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.companies_company_id_users_user_id_favorites_get200_response import CompaniesCompanyIdUsersUserIdFavoritesGet200Response
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
    api_instance = spartera_api_sdk.FavoritesApi(api_client)
    company_id = 'company_id_example' # str | 
    user_id = 'user_id_example' # str | 

    try:
        # Get all favorites for the specified user that don't have a category
        api_response = api_instance.companies_company_id_users_user_id_favorites_uncategorized_get(company_id, user_id)
        print("The response of FavoritesApi->companies_company_id_users_user_id_favorites_uncategorized_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FavoritesApi->companies_company_id_users_user_id_favorites_uncategorized_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**CompaniesCompanyIdUsersUserIdFavoritesGet200Response**](CompaniesCompanyIdUsersUserIdFavoritesGet200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved favorites |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

