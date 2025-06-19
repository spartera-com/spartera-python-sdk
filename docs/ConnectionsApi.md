# spartera_api_sdk.ConnectionsApi

All URIs are relative to *https://api.spartera.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companies_company_id_connections_connection_id_delete**](ConnectionsApi.md#companies_company_id_connections_connection_id_delete) | **DELETE** /companies/{company_id}/connections/{connection_id} | Delete single connection by ID
[**companies_company_id_connections_connection_id_get**](ConnectionsApi.md#companies_company_id_connections_connection_id_get) | **GET** /companies/{company_id}/connections/{connection_id} | Get single connection by ID
[**companies_company_id_connections_connection_id_infoschema_get**](ConnectionsApi.md#companies_company_id_connections_connection_id_infoschema_get) | **GET** /companies/{company_id}/connections/{connection_id}/infoschema | Retrieve the information schema for the specified connection
[**companies_company_id_connections_connection_id_patch**](ConnectionsApi.md#companies_company_id_connections_connection_id_patch) | **PATCH** /companies/{company_id}/connections/{connection_id} | Update an existing connection by ID
[**companies_company_id_connections_connection_id_test_get**](ConnectionsApi.md#companies_company_id_connections_connection_id_test_get) | **GET** /companies/{company_id}/connections/{connection_id}/test | Verify the specified connection to ensure it is functioning correctly
[**companies_company_id_connections_get**](ConnectionsApi.md#companies_company_id_connections_get) | **GET** /companies/{company_id}/connections | Get all connections for a specific company
[**companies_company_id_connections_post**](ConnectionsApi.md#companies_company_id_connections_post) | **POST** /companies/{company_id}/connections | Create a new connection by ID


# **companies_company_id_connections_connection_id_delete**
> object companies_company_id_connections_connection_id_delete(company_id, connection_id)

Delete single connection by ID

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
    api_instance = spartera_api_sdk.ConnectionsApi(api_client)
    company_id = 'company_id_example' # str | 
    connection_id = 'connection_id_example' # str | 

    try:
        # Delete single connection by ID
        api_response = api_instance.companies_company_id_connections_connection_id_delete(company_id, connection_id)
        print("The response of ConnectionsApi->companies_company_id_connections_connection_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectionsApi->companies_company_id_connections_connection_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  | 
 **connection_id** | **str**|  | 

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

# **companies_company_id_connections_connection_id_get**
> object companies_company_id_connections_connection_id_get(company_id, connection_id)

Get single connection by ID

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
    api_instance = spartera_api_sdk.ConnectionsApi(api_client)
    company_id = 'company_id_example' # str | 
    connection_id = 'connection_id_example' # str | 

    try:
        # Get single connection by ID
        api_response = api_instance.companies_company_id_connections_connection_id_get(company_id, connection_id)
        print("The response of ConnectionsApi->companies_company_id_connections_connection_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectionsApi->companies_company_id_connections_connection_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  | 
 **connection_id** | **str**|  | 

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

# **companies_company_id_connections_connection_id_infoschema_get**
> object companies_company_id_connections_connection_id_infoschema_get(company_id, connection_id)

Retrieve the information schema for the specified connection

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
    api_instance = spartera_api_sdk.ConnectionsApi(api_client)
    company_id = 'company_id_example' # str | 
    connection_id = 'connection_id_example' # str | 

    try:
        # Retrieve the information schema for the specified connection
        api_response = api_instance.companies_company_id_connections_connection_id_infoschema_get(company_id, connection_id)
        print("The response of ConnectionsApi->companies_company_id_connections_connection_id_infoschema_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectionsApi->companies_company_id_connections_connection_id_infoschema_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  | 
 **connection_id** | **str**|  | 

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

# **companies_company_id_connections_connection_id_patch**
> object companies_company_id_connections_connection_id_patch(company_id, connection_id, connection)

Update an existing connection by ID

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.connection import Connection
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
    api_instance = spartera_api_sdk.ConnectionsApi(api_client)
    company_id = 'company_id_example' # str | 
    connection_id = 'connection_id_example' # str | 
    connection = spartera_api_sdk.Connection() # Connection | 

    try:
        # Update an existing connection by ID
        api_response = api_instance.companies_company_id_connections_connection_id_patch(company_id, connection_id, connection)
        print("The response of ConnectionsApi->companies_company_id_connections_connection_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectionsApi->companies_company_id_connections_connection_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  | 
 **connection_id** | **str**|  | 
 **connection** | [**Connection**](Connection.md)|  | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
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

# **companies_company_id_connections_connection_id_test_get**
> object companies_company_id_connections_connection_id_test_get(company_id, connection_id)

Verify the specified connection to ensure it is functioning correctly

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
    api_instance = spartera_api_sdk.ConnectionsApi(api_client)
    company_id = 'company_id_example' # str | 
    connection_id = 'connection_id_example' # str | 

    try:
        # Verify the specified connection to ensure it is functioning correctly
        api_response = api_instance.companies_company_id_connections_connection_id_test_get(company_id, connection_id)
        print("The response of ConnectionsApi->companies_company_id_connections_connection_id_test_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectionsApi->companies_company_id_connections_connection_id_test_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  | 
 **connection_id** | **str**|  | 

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

# **companies_company_id_connections_get**
> object companies_company_id_connections_get(company_id)

Get all connections for a specific company

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
    api_instance = spartera_api_sdk.ConnectionsApi(api_client)
    company_id = 'company_id_example' # str | 

    try:
        # Get all connections for a specific company
        api_response = api_instance.companies_company_id_connections_get(company_id)
        print("The response of ConnectionsApi->companies_company_id_connections_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectionsApi->companies_company_id_connections_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  | 

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

# **companies_company_id_connections_post**
> object companies_company_id_connections_post(company_id, connection)

Create a new connection by ID

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.connection import Connection
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
    api_instance = spartera_api_sdk.ConnectionsApi(api_client)
    company_id = 'company_id_example' # str | 
    connection = spartera_api_sdk.Connection() # Connection | 

    try:
        # Create a new connection by ID
        api_response = api_instance.companies_company_id_connections_post(company_id, connection)
        print("The response of ConnectionsApi->companies_company_id_connections_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectionsApi->companies_company_id_connections_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  | 
 **connection** | [**Connection**](Connection.md)|  | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**400** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

