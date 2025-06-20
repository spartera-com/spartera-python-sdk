# spartera_api_sdk.CloudProvidersApi

All URIs are relative to *https://api.spartera.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cloud_providers_get**](CloudProvidersApi.md#cloud_providers_get) | **GET** /cloud-providers | Get a list of all cloud providers
[**cloud_providers_post**](CloudProvidersApi.md#cloud_providers_post) | **POST** /cloud-providers | Create single cloud provider
[**cloud_providers_provider_id_delete**](CloudProvidersApi.md#cloud_providers_provider_id_delete) | **DELETE** /cloud-providers/{provider_id} | Delete single cloud provider by ID
[**cloud_providers_provider_id_get**](CloudProvidersApi.md#cloud_providers_provider_id_get) | **GET** /cloud-providers/{provider_id} | Get single cloud provider by ID
[**cloud_providers_provider_id_patch**](CloudProvidersApi.md#cloud_providers_provider_id_patch) | **PATCH** /cloud-providers/{provider_id} | Update an existing cloud provider by ID


# **cloud_providers_get**
> object cloud_providers_get()

Get a list of all cloud providers

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
    api_instance = spartera_api_sdk.CloudProvidersApi(api_client)

    try:
        # Get a list of all cloud providers
        api_response = api_instance.cloud_providers_get()
        print("The response of CloudProvidersApi->cloud_providers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudProvidersApi->cloud_providers_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

# **cloud_providers_post**
> object cloud_providers_post()

Create single cloud provider

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
    api_instance = spartera_api_sdk.CloudProvidersApi(api_client)

    try:
        # Create single cloud provider
        api_response = api_instance.cloud_providers_post()
        print("The response of CloudProvidersApi->cloud_providers_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudProvidersApi->cloud_providers_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

# **cloud_providers_provider_id_delete**
> object cloud_providers_provider_id_delete(provider_id)

Delete single cloud provider by ID

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
    api_instance = spartera_api_sdk.CloudProvidersApi(api_client)
    provider_id = 'provider_id_example' # str | 

    try:
        # Delete single cloud provider by ID
        api_response = api_instance.cloud_providers_provider_id_delete(provider_id)
        print("The response of CloudProvidersApi->cloud_providers_provider_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudProvidersApi->cloud_providers_provider_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**|  | 

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

# **cloud_providers_provider_id_get**
> object cloud_providers_provider_id_get(provider_id)

Get single cloud provider by ID

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
    api_instance = spartera_api_sdk.CloudProvidersApi(api_client)
    provider_id = 'provider_id_example' # str | 

    try:
        # Get single cloud provider by ID
        api_response = api_instance.cloud_providers_provider_id_get(provider_id)
        print("The response of CloudProvidersApi->cloud_providers_provider_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudProvidersApi->cloud_providers_provider_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**|  | 

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

# **cloud_providers_provider_id_patch**
> object cloud_providers_provider_id_patch(provider_id)

Update an existing cloud provider by ID

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
    api_instance = spartera_api_sdk.CloudProvidersApi(api_client)
    provider_id = 'provider_id_example' # str | 

    try:
        # Update an existing cloud provider by ID
        api_response = api_instance.cloud_providers_provider_id_patch(provider_id)
        print("The response of CloudProvidersApi->cloud_providers_provider_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudProvidersApi->cloud_providers_provider_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**|  | 

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

