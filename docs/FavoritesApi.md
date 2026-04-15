# spartera_api_sdk.FavoritesApi

All URIs are relative to *https://api.spartera.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_favorites**](FavoritesApi.md#create_favorites) | **POST** /companies/{company_id}/users/{user_id}/favorites | POST /companies/{company_id}/users/{user_id}/favorites
[**delete_favorites**](FavoritesApi.md#delete_favorites) | **DELETE** /companies/{company_id}/users/{user_id}/favorites/{favorite_id} | Delete single favorite by ID (unfavorite an asset)
[**get_favorites_by_id**](FavoritesApi.md#get_favorites_by_id) | **GET** /companies/{company_id}/users/{user_id}/favorites | Get a list of all favorites for a specific user
[**get_favorites_by_id_users**](FavoritesApi.md#get_favorites_by_id_users) | **GET** /companies/{company_id}/users/{user_id}/favorites/{favorite_id} | Get single favorite by ID
[**get_favorites_by_id_users_category**](FavoritesApi.md#get_favorites_by_id_users_category) | **GET** /companies/{company_id}/users/{user_id}/favorites/category/{category} | Get all favorites for the specified user in a specific category
[**get_favorites_by_id_users_check**](FavoritesApi.md#get_favorites_by_id_users_check) | **GET** /companies/{company_id}/users/{user_id}/favorites/check/{asset_id} | Check if the specified user has favorited a specific asset
[**get_favorites_by_id_users_uncategorized**](FavoritesApi.md#get_favorites_by_id_users_uncategorized) | **GET** /companies/{company_id}/users/{user_id}/favorites/uncategorized | Get all favorites for the specified user that don&#39;t have a category
[**update_favorites**](FavoritesApi.md#update_favorites) | **PATCH** /companies/{company_id}/users/{user_id}/favorites/{favorite_id} | Update an existing favorite by ID


# **create_favorites**
> CreateFavorites200Response create_favorites(company_id, user_id, favorites_input)

POST /companies/{company_id}/users/{user_id}/favorites

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.create_favorites200_response import CreateFavorites200Response
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
    company_id = 'company_id_example' # str | Unique identifier for the Company
    user_id = 'user_id_example' # str | Unique identifier for the User
    favorites_input = spartera_api_sdk.FavoritesInput() # FavoritesInput | 

    try:
        # POST /companies/{company_id}/users/{user_id}/favorites
        api_response = api_instance.create_favorites(company_id, user_id, favorites_input)
        print("The response of FavoritesApi->create_favorites:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FavoritesApi->create_favorites: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **user_id** | **str**| Unique identifier for the User | 
 **favorites_input** | [**FavoritesInput**](FavoritesInput.md)|  | 

### Return type

[**CreateFavorites200Response**](CreateFavorites200Response.md)

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
**409** | Resource conflict (duplicate, constraint violation) |  -  |
**422** | Request well-formed but semantically invalid |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_favorites**
> DeleteFavorites200Response delete_favorites(company_id, user_id, favorite_id)

Delete single favorite by ID (unfavorite an asset)

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.delete_favorites200_response import DeleteFavorites200Response
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
    company_id = 'company_id_example' # str | Unique identifier for the Company
    user_id = 'user_id_example' # str | Unique identifier for the User
    favorite_id = 'favorite_id_example' # str | Unique identifier for the Favorite

    try:
        # Delete single favorite by ID (unfavorite an asset)
        api_response = api_instance.delete_favorites(company_id, user_id, favorite_id)
        print("The response of FavoritesApi->delete_favorites:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FavoritesApi->delete_favorites: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **user_id** | **str**| Unique identifier for the User | 
 **favorite_id** | **str**| Unique identifier for the Favorite | 

### Return type

[**DeleteFavorites200Response**](DeleteFavorites200Response.md)

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
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_favorites_by_id**
> GetFavoritesById200Response get_favorites_by_id(company_id, user_id)

Get a list of all favorites for a specific user

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.get_favorites_by_id200_response import GetFavoritesById200Response
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
    company_id = 'company_id_example' # str | Unique identifier for the Company
    user_id = 'user_id_example' # str | Unique identifier for the User

    try:
        # Get a list of all favorites for a specific user
        api_response = api_instance.get_favorites_by_id(company_id, user_id)
        print("The response of FavoritesApi->get_favorites_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FavoritesApi->get_favorites_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **user_id** | **str**| Unique identifier for the User | 

### Return type

[**GetFavoritesById200Response**](GetFavoritesById200Response.md)

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
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_favorites_by_id_users**
> GetFavoritesById200Response get_favorites_by_id_users(company_id, user_id, favorite_id)

Get single favorite by ID

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.get_favorites_by_id200_response import GetFavoritesById200Response
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
    company_id = 'company_id_example' # str | Unique identifier for the Company
    user_id = 'user_id_example' # str | Unique identifier for the User
    favorite_id = 'favorite_id_example' # str | Unique identifier for the Favorite

    try:
        # Get single favorite by ID
        api_response = api_instance.get_favorites_by_id_users(company_id, user_id, favorite_id)
        print("The response of FavoritesApi->get_favorites_by_id_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FavoritesApi->get_favorites_by_id_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **user_id** | **str**| Unique identifier for the User | 
 **favorite_id** | **str**| Unique identifier for the Favorite | 

### Return type

[**GetFavoritesById200Response**](GetFavoritesById200Response.md)

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
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_favorites_by_id_users_category**
> GetFavoritesById200Response get_favorites_by_id_users_category(company_id, user_id, category)

Get all favorites for the specified user in a specific category

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.get_favorites_by_id200_response import GetFavoritesById200Response
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
    company_id = 'company_id_example' # str | Unique identifier for the Company
    user_id = 'user_id_example' # str | Unique identifier for the User
    category = 'category_example' # str | Parameter for category

    try:
        # Get all favorites for the specified user in a specific category
        api_response = api_instance.get_favorites_by_id_users_category(company_id, user_id, category)
        print("The response of FavoritesApi->get_favorites_by_id_users_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FavoritesApi->get_favorites_by_id_users_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **user_id** | **str**| Unique identifier for the User | 
 **category** | **str**| Parameter for category | 

### Return type

[**GetFavoritesById200Response**](GetFavoritesById200Response.md)

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
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_favorites_by_id_users_check**
> GetFavoritesById200Response get_favorites_by_id_users_check(company_id, user_id, asset_id)

Check if the specified user has favorited a specific asset

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.get_favorites_by_id200_response import GetFavoritesById200Response
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
    company_id = 'company_id_example' # str | Unique identifier for the Company
    user_id = 'user_id_example' # str | Unique identifier for the User
    asset_id = 'asset_id_example' # str | Unique identifier for the Asset

    try:
        # Check if the specified user has favorited a specific asset
        api_response = api_instance.get_favorites_by_id_users_check(company_id, user_id, asset_id)
        print("The response of FavoritesApi->get_favorites_by_id_users_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FavoritesApi->get_favorites_by_id_users_check: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **user_id** | **str**| Unique identifier for the User | 
 **asset_id** | **str**| Unique identifier for the Asset | 

### Return type

[**GetFavoritesById200Response**](GetFavoritesById200Response.md)

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
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_favorites_by_id_users_uncategorized**
> GetFavoritesById200Response get_favorites_by_id_users_uncategorized(company_id, user_id)

Get all favorites for the specified user that don't have a category

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.get_favorites_by_id200_response import GetFavoritesById200Response
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
    company_id = 'company_id_example' # str | Unique identifier for the Company
    user_id = 'user_id_example' # str | Unique identifier for the User

    try:
        # Get all favorites for the specified user that don't have a category
        api_response = api_instance.get_favorites_by_id_users_uncategorized(company_id, user_id)
        print("The response of FavoritesApi->get_favorites_by_id_users_uncategorized:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FavoritesApi->get_favorites_by_id_users_uncategorized: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **user_id** | **str**| Unique identifier for the User | 

### Return type

[**GetFavoritesById200Response**](GetFavoritesById200Response.md)

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
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_favorites**
> UpdateFavorites200Response update_favorites(company_id, user_id, favorite_id, favorites_update)

Update an existing favorite by ID

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.favorites_update import FavoritesUpdate
from spartera_api_sdk.models.update_favorites200_response import UpdateFavorites200Response
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
    company_id = 'company_id_example' # str | Unique identifier for the Company
    user_id = 'user_id_example' # str | Unique identifier for the User
    favorite_id = 'favorite_id_example' # str | Unique identifier for the Favorite
    favorites_update = spartera_api_sdk.FavoritesUpdate() # FavoritesUpdate | 

    try:
        # Update an existing favorite by ID
        api_response = api_instance.update_favorites(company_id, user_id, favorite_id, favorites_update)
        print("The response of FavoritesApi->update_favorites:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FavoritesApi->update_favorites: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **user_id** | **str**| Unique identifier for the User | 
 **favorite_id** | **str**| Unique identifier for the Favorite | 
 **favorites_update** | [**FavoritesUpdate**](FavoritesUpdate.md)|  | 

### Return type

[**UpdateFavorites200Response**](UpdateFavorites200Response.md)

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
**409** | Resource conflict (duplicate, constraint violation) |  -  |
**422** | Request well-formed but semantically invalid |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

