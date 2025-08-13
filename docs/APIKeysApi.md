# spartera_api_sdk.APIKeysApi

All URIs are relative to *https://api.spartera.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companies_company_id_api_keys_api_key_id_delete**](APIKeysApi.md#companies_company_id_api_keys_api_key_id_delete) | **DELETE** /companies/{company_id}/api-keys/{api_key_id} | Delete (deactivate) single API key by api_key_id.     Uses the api_key_id returned during creation for clean identification.     Fixed to use correct primary key lookup.
[**companies_company_id_api_keys_api_key_id_get**](APIKeysApi.md#companies_company_id_api_keys_api_key_id_get) | **GET** /companies/{company_id}/api-keys/{api_key_id} | Get single API key by ID.     Returns masked API key for security (sk_****1234).
[**companies_company_id_api_keys_api_key_id_patch**](APIKeysApi.md#companies_company_id_api_keys_api_key_id_patch) | **PATCH** /companies/{company_id}/api-keys/{api_key_id} | Update an existing API key by ID.     Can update metadata like name, expiration, rate limits, etc.     Cannot update the actual key value (for security).
[**companies_company_id_api_keys_api_key_id_revoke_post**](APIKeysApi.md#companies_company_id_api_keys_api_key_id_revoke_post) | **POST** /companies/{company_id}/api-keys/{api_key_id}/revoke | Explicitly revoke an API key with reason tracking.     This is different from delete as it includes revocation metadata.
[**companies_company_id_api_keys_api_key_id_stats_get**](APIKeysApi.md#companies_company_id_api_keys_api_key_id_stats_get) | **GET** /companies/{company_id}/api-keys/{api_key_id}/stats | Get usage statistics for a specific API key.     Returns usage count, last used date, failed attempts, etc.
[**companies_company_id_api_keys_get**](APIKeysApi.md#companies_company_id_api_keys_get) | **GET** /companies/{company_id}/api-keys | Get all API keys for a company.     Returns masked API keys for security (sk_****1234).
[**companies_company_id_api_keys_post**](APIKeysApi.md#companies_company_id_api_keys_post) | **POST** /companies/{company_id}/api-keys | Create single API key.     Returns the actual sk_ key (only time it&#39;s exposed) and api_key_id for future operations.


# **companies_company_id_api_keys_api_key_id_delete**
> CompaniesCompanyIdApiKeysApiKeyIdDelete200Response companies_company_id_api_keys_api_key_id_delete(company_id, api_key_id)

Delete (deactivate) single API key by api_key_id.     Uses the api_key_id returned during creation for clean identification.     Fixed to use correct primary key lookup.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.companies_company_id_api_keys_api_key_id_delete200_response import CompaniesCompanyIdApiKeysApiKeyIdDelete200Response
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
    company_id = 'company_id_example' # str | 
    api_key_id = 'api_key_id_example' # str | 

    try:
        # Delete (deactivate) single API key by api_key_id.     Uses the api_key_id returned during creation for clean identification.     Fixed to use correct primary key lookup.
        api_response = api_instance.companies_company_id_api_keys_api_key_id_delete(company_id, api_key_id)
        print("The response of APIKeysApi->companies_company_id_api_keys_api_key_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIKeysApi->companies_company_id_api_keys_api_key_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  | 
 **api_key_id** | **str**|  | 

### Return type

[**CompaniesCompanyIdApiKeysApiKeyIdDelete200Response**](CompaniesCompanyIdApiKeysApiKeyIdDelete200Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_api_keys_api_key_id_get**
> CompaniesCompanyIdApiKeysApiKeyIdGet200Response companies_company_id_api_keys_api_key_id_get(company_id, api_key_id)

Get single API key by ID.     Returns masked API key for security (sk_****1234).

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.companies_company_id_api_keys_api_key_id_get200_response import CompaniesCompanyIdApiKeysApiKeyIdGet200Response
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
    company_id = 'company_id_example' # str | 
    api_key_id = 'api_key_id_example' # str | 

    try:
        # Get single API key by ID.     Returns masked API key for security (sk_****1234).
        api_response = api_instance.companies_company_id_api_keys_api_key_id_get(company_id, api_key_id)
        print("The response of APIKeysApi->companies_company_id_api_keys_api_key_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIKeysApi->companies_company_id_api_keys_api_key_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  | 
 **api_key_id** | **str**|  | 

### Return type

[**CompaniesCompanyIdApiKeysApiKeyIdGet200Response**](CompaniesCompanyIdApiKeysApiKeyIdGet200Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_api_keys_api_key_id_patch**
> CompaniesCompanyIdApiKeysApiKeyIdPatch200Response companies_company_id_api_keys_api_key_id_patch(company_id, api_key_id, api_keys_update)

Update an existing API key by ID.     Can update metadata like name, expiration, rate limits, etc.     Cannot update the actual key value (for security).

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.api_keys_update import ApiKeysUpdate
from spartera_api_sdk.models.companies_company_id_api_keys_api_key_id_patch200_response import CompaniesCompanyIdApiKeysApiKeyIdPatch200Response
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
    company_id = 'company_id_example' # str | 
    api_key_id = 'api_key_id_example' # str | 
    api_keys_update = spartera_api_sdk.ApiKeysUpdate() # ApiKeysUpdate | 

    try:
        # Update an existing API key by ID.     Can update metadata like name, expiration, rate limits, etc.     Cannot update the actual key value (for security).
        api_response = api_instance.companies_company_id_api_keys_api_key_id_patch(company_id, api_key_id, api_keys_update)
        print("The response of APIKeysApi->companies_company_id_api_keys_api_key_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIKeysApi->companies_company_id_api_keys_api_key_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  | 
 **api_key_id** | **str**|  | 
 **api_keys_update** | [**ApiKeysUpdate**](ApiKeysUpdate.md)|  | 

### Return type

[**CompaniesCompanyIdApiKeysApiKeyIdPatch200Response**](CompaniesCompanyIdApiKeysApiKeyIdPatch200Response.md)

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
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_api_keys_api_key_id_revoke_post**
> CompaniesCompanyIdApiKeysPost200Response companies_company_id_api_keys_api_key_id_revoke_post(company_id, api_key_id, api_keys_input)

Explicitly revoke an API key with reason tracking.     This is different from delete as it includes revocation metadata.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.api_keys_input import ApiKeysInput
from spartera_api_sdk.models.companies_company_id_api_keys_post200_response import CompaniesCompanyIdApiKeysPost200Response
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
    company_id = 'company_id_example' # str | 
    api_key_id = 'api_key_id_example' # str | 
    api_keys_input = spartera_api_sdk.ApiKeysInput() # ApiKeysInput | 

    try:
        # Explicitly revoke an API key with reason tracking.     This is different from delete as it includes revocation metadata.
        api_response = api_instance.companies_company_id_api_keys_api_key_id_revoke_post(company_id, api_key_id, api_keys_input)
        print("The response of APIKeysApi->companies_company_id_api_keys_api_key_id_revoke_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIKeysApi->companies_company_id_api_keys_api_key_id_revoke_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  | 
 **api_key_id** | **str**|  | 
 **api_keys_input** | [**ApiKeysInput**](ApiKeysInput.md)|  | 

### Return type

[**CompaniesCompanyIdApiKeysPost200Response**](CompaniesCompanyIdApiKeysPost200Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_api_keys_api_key_id_stats_get**
> CompaniesCompanyIdApiKeysGet200Response companies_company_id_api_keys_api_key_id_stats_get(company_id, api_key_id)

Get usage statistics for a specific API key.     Returns usage count, last used date, failed attempts, etc.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.companies_company_id_api_keys_get200_response import CompaniesCompanyIdApiKeysGet200Response
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
    company_id = 'company_id_example' # str | 
    api_key_id = 'api_key_id_example' # str | 

    try:
        # Get usage statistics for a specific API key.     Returns usage count, last used date, failed attempts, etc.
        api_response = api_instance.companies_company_id_api_keys_api_key_id_stats_get(company_id, api_key_id)
        print("The response of APIKeysApi->companies_company_id_api_keys_api_key_id_stats_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIKeysApi->companies_company_id_api_keys_api_key_id_stats_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  | 
 **api_key_id** | **str**|  | 

### Return type

[**CompaniesCompanyIdApiKeysGet200Response**](CompaniesCompanyIdApiKeysGet200Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_api_keys_get**
> CompaniesCompanyIdApiKeysGet200Response companies_company_id_api_keys_get(company_id)

Get all API keys for a company.     Returns masked API keys for security (sk_****1234).

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.companies_company_id_api_keys_get200_response import CompaniesCompanyIdApiKeysGet200Response
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
    company_id = 'company_id_example' # str | 

    try:
        # Get all API keys for a company.     Returns masked API keys for security (sk_****1234).
        api_response = api_instance.companies_company_id_api_keys_get(company_id)
        print("The response of APIKeysApi->companies_company_id_api_keys_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIKeysApi->companies_company_id_api_keys_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  | 

### Return type

[**CompaniesCompanyIdApiKeysGet200Response**](CompaniesCompanyIdApiKeysGet200Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_api_keys_post**
> CompaniesCompanyIdApiKeysPost200Response companies_company_id_api_keys_post(company_id, api_keys_input)

Create single API key.     Returns the actual sk_ key (only time it's exposed) and api_key_id for future operations.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.api_keys_input import ApiKeysInput
from spartera_api_sdk.models.companies_company_id_api_keys_post200_response import CompaniesCompanyIdApiKeysPost200Response
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
    company_id = 'company_id_example' # str | 
    api_keys_input = spartera_api_sdk.ApiKeysInput() # ApiKeysInput | 

    try:
        # Create single API key.     Returns the actual sk_ key (only time it's exposed) and api_key_id for future operations.
        api_response = api_instance.companies_company_id_api_keys_post(company_id, api_keys_input)
        print("The response of APIKeysApi->companies_company_id_api_keys_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIKeysApi->companies_company_id_api_keys_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  | 
 **api_keys_input** | [**ApiKeysInput**](ApiKeysInput.md)|  | 

### Return type

[**CompaniesCompanyIdApiKeysPost200Response**](CompaniesCompanyIdApiKeysPost200Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

