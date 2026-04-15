# spartera_api_sdk.APIKeysApi

All URIs are relative to *https://api.spartera.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_api_keys**](APIKeysApi.md#create_api_keys) | **POST** /companies/{company_id}/api-keys | Create single API key.     Returns the actual sk_ key (only time it&#39;s exposed) and api_key_id for future operations.
[**create_api_keys_api_keys_revoke**](APIKeysApi.md#create_api_keys_api_keys_revoke) | **POST** /companies/{company_id}/api-keys/{api_key_id}/revoke | Explicitly revoke an API key with reason tracking.     This is different from delete as it includes revocation metadata.
[**delete_api_keys**](APIKeysApi.md#delete_api_keys) | **DELETE** /companies/{company_id}/api-keys/{api_key_id} | Delete (deactivate) single API key by api_key_id.     Uses the api_key_id returned during creation for clean identification.     Fixed to use correct primary key lookup.
[**get_api_keys_by_id**](APIKeysApi.md#get_api_keys_by_id) | **GET** /companies/{company_id}/api-keys/{api_key_id} | Get single API key by ID.     Returns masked API key for security (sk_****1234).
[**get_api_keys_by_id_api_keys_stats**](APIKeysApi.md#get_api_keys_by_id_api_keys_stats) | **GET** /companies/{company_id}/api-keys/{api_key_id}/stats | Get usage statistics for a specific API key.     Returns usage count, last used date, failed attempts, etc.
[**list_api_keys**](APIKeysApi.md#list_api_keys) | **GET** /companies/{company_id}/api-keys | Get all API keys for a company.     Returns masked API keys for security (sk_****1234).
[**update_api_keys**](APIKeysApi.md#update_api_keys) | **PATCH** /companies/{company_id}/api-keys/{api_key_id} | Update an existing API key by ID.     Can update metadata like name, expiration, rate limits, etc.     Cannot update the actual key value (for security).


# **create_api_keys**
> CreateApiKeys200Response create_api_keys(company_id, api_keys_input, page=page, limit=limit, sort_by=sort_by, sort_order=sort_order, search=search)

Create single API key.     Returns the actual sk_ key (only time it's exposed) and api_key_id for future operations.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.api_keys_input import ApiKeysInput
from spartera_api_sdk.models.create_api_keys200_response import CreateApiKeys200Response
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
    api_instance = spartera_api_sdk.APIKeysApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    api_keys_input = spartera_api_sdk.ApiKeysInput() # ApiKeysInput | 
    page = 1 # int | Page number for pagination (optional) (default to 1)
    limit = 20 # int | Number of items per page (optional) (default to 20)
    sort_by = 'sort_by_example' # str | Field to sort by (optional)
    sort_order = desc # str | Sort order (ascending or descending) (optional) (default to desc)
    search = 'search_example' # str | Search term to filter results (optional)

    try:
        # Create single API key.     Returns the actual sk_ key (only time it's exposed) and api_key_id for future operations.
        api_response = api_instance.create_api_keys(company_id, api_keys_input, page=page, limit=limit, sort_by=sort_by, sort_order=sort_order, search=search)
        print("The response of APIKeysApi->create_api_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIKeysApi->create_api_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **api_keys_input** | [**ApiKeysInput**](ApiKeysInput.md)|  | 
 **page** | **int**| Page number for pagination | [optional] [default to 1]
 **limit** | **int**| Number of items per page | [optional] [default to 20]
 **sort_by** | **str**| Field to sort by | [optional] 
 **sort_order** | **str**| Sort order (ascending or descending) | [optional] [default to desc]
 **search** | **str**| Search term to filter results | [optional] 

### Return type

[**CreateApiKeys200Response**](CreateApiKeys200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created api keys |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**400** | Invalid input |  -  |
**409** | Resource conflict (duplicate, constraint violation) |  -  |
**422** | Request well-formed but semantically invalid |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_api_keys_api_keys_revoke**
> CreateApiKeys200Response create_api_keys_api_keys_revoke(company_id, api_key_id, api_keys_input)

Explicitly revoke an API key with reason tracking.     This is different from delete as it includes revocation metadata.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.api_keys_input import ApiKeysInput
from spartera_api_sdk.models.create_api_keys200_response import CreateApiKeys200Response
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
    api_instance = spartera_api_sdk.APIKeysApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    api_key_id = 'api_key_id_example' # str | Unique identifier for the Api Key
    api_keys_input = spartera_api_sdk.ApiKeysInput() # ApiKeysInput | 

    try:
        # Explicitly revoke an API key with reason tracking.     This is different from delete as it includes revocation metadata.
        api_response = api_instance.create_api_keys_api_keys_revoke(company_id, api_key_id, api_keys_input)
        print("The response of APIKeysApi->create_api_keys_api_keys_revoke:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIKeysApi->create_api_keys_api_keys_revoke: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **api_key_id** | **str**| Unique identifier for the Api Key | 
 **api_keys_input** | [**ApiKeysInput**](ApiKeysInput.md)|  | 

### Return type

[**CreateApiKeys200Response**](CreateApiKeys200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created api keys |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**400** | Invalid input |  -  |
**409** | Resource conflict (duplicate, constraint violation) |  -  |
**422** | Request well-formed but semantically invalid |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_api_keys**
> DeleteApiKeys200Response delete_api_keys(company_id, api_key_id)

Delete (deactivate) single API key by api_key_id.     Uses the api_key_id returned during creation for clean identification.     Fixed to use correct primary key lookup.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.delete_api_keys200_response import DeleteApiKeys200Response
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
    api_instance = spartera_api_sdk.APIKeysApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    api_key_id = 'api_key_id_example' # str | Unique identifier for the Api Key

    try:
        # Delete (deactivate) single API key by api_key_id.     Uses the api_key_id returned during creation for clean identification.     Fixed to use correct primary key lookup.
        api_response = api_instance.delete_api_keys(company_id, api_key_id)
        print("The response of APIKeysApi->delete_api_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIKeysApi->delete_api_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **api_key_id** | **str**| Unique identifier for the Api Key | 

### Return type

[**DeleteApiKeys200Response**](DeleteApiKeys200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully deleted api keys |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_keys_by_id**
> GetApiKeysById200Response get_api_keys_by_id(company_id, api_key_id)

Get single API key by ID.     Returns masked API key for security (sk_****1234).

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.get_api_keys_by_id200_response import GetApiKeysById200Response
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
    api_instance = spartera_api_sdk.APIKeysApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    api_key_id = 'api_key_id_example' # str | Unique identifier for the Api Key

    try:
        # Get single API key by ID.     Returns masked API key for security (sk_****1234).
        api_response = api_instance.get_api_keys_by_id(company_id, api_key_id)
        print("The response of APIKeysApi->get_api_keys_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIKeysApi->get_api_keys_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **api_key_id** | **str**| Unique identifier for the Api Key | 

### Return type

[**GetApiKeysById200Response**](GetApiKeysById200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved api keys |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_keys_by_id_api_keys_stats**
> GetApiKeysById200Response get_api_keys_by_id_api_keys_stats(company_id, api_key_id)

Get usage statistics for a specific API key.     Returns usage count, last used date, failed attempts, etc.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.get_api_keys_by_id200_response import GetApiKeysById200Response
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
    api_instance = spartera_api_sdk.APIKeysApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    api_key_id = 'api_key_id_example' # str | Unique identifier for the Api Key

    try:
        # Get usage statistics for a specific API key.     Returns usage count, last used date, failed attempts, etc.
        api_response = api_instance.get_api_keys_by_id_api_keys_stats(company_id, api_key_id)
        print("The response of APIKeysApi->get_api_keys_by_id_api_keys_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIKeysApi->get_api_keys_by_id_api_keys_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **api_key_id** | **str**| Unique identifier for the Api Key | 

### Return type

[**GetApiKeysById200Response**](GetApiKeysById200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved api keys |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_api_keys**
> ListApiKeys200Response list_api_keys(company_id, page=page, limit=limit, sort_by=sort_by, sort_order=sort_order, search=search)

Get all API keys for a company.     Returns masked API keys for security (sk_****1234).

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.list_api_keys200_response import ListApiKeys200Response
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
    api_instance = spartera_api_sdk.APIKeysApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    page = 1 # int | Page number for pagination (optional) (default to 1)
    limit = 20 # int | Number of items per page (optional) (default to 20)
    sort_by = 'sort_by_example' # str | Field to sort by (optional)
    sort_order = desc # str | Sort order (ascending or descending) (optional) (default to desc)
    search = 'search_example' # str | Search term to filter results (optional)

    try:
        # Get all API keys for a company.     Returns masked API keys for security (sk_****1234).
        api_response = api_instance.list_api_keys(company_id, page=page, limit=limit, sort_by=sort_by, sort_order=sort_order, search=search)
        print("The response of APIKeysApi->list_api_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIKeysApi->list_api_keys: %s\n" % e)
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

[**ListApiKeys200Response**](ListApiKeys200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved api keys |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_api_keys**
> UpdateApiKeys200Response update_api_keys(company_id, api_key_id, api_keys_update)

Update an existing API key by ID.     Can update metadata like name, expiration, rate limits, etc.     Cannot update the actual key value (for security).

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.api_keys_update import ApiKeysUpdate
from spartera_api_sdk.models.update_api_keys200_response import UpdateApiKeys200Response
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
    api_instance = spartera_api_sdk.APIKeysApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    api_key_id = 'api_key_id_example' # str | Unique identifier for the Api Key
    api_keys_update = spartera_api_sdk.ApiKeysUpdate() # ApiKeysUpdate | 

    try:
        # Update an existing API key by ID.     Can update metadata like name, expiration, rate limits, etc.     Cannot update the actual key value (for security).
        api_response = api_instance.update_api_keys(company_id, api_key_id, api_keys_update)
        print("The response of APIKeysApi->update_api_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIKeysApi->update_api_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **api_key_id** | **str**| Unique identifier for the Api Key | 
 **api_keys_update** | [**ApiKeysUpdate**](ApiKeysUpdate.md)|  | 

### Return type

[**UpdateApiKeys200Response**](UpdateApiKeys200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated api keys |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**400** | Invalid input |  -  |
**409** | Resource conflict (duplicate, constraint violation) |  -  |
**422** | Request well-formed but semantically invalid |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

