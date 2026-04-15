# spartera_api_sdk.ConnectionsApi

All URIs are relative to *https://api.spartera.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_connections**](ConnectionsApi.md#create_connections) | **POST** /companies/{company_id}/connections | Create a new connection by ID
[**delete_connections**](ConnectionsApi.md#delete_connections) | **DELETE** /companies/{company_id}/connections/{connection_id} | Delete single connection by ID
[**get_connections_by_id**](ConnectionsApi.md#get_connections_by_id) | **GET** /companies/{company_id}/connections/{connection_id} | Get single connection by ID
[**get_connections_by_id2**](ConnectionsApi.md#get_connections_by_id2) | **GET** /companies/{company_id}/connections/{connection_id}/test | Test the specified connection
[**get_connections_by_id_infoschema**](ConnectionsApi.md#get_connections_by_id_infoschema) | **GET** /companies/{company_id}/connections/{connection_id}/infoschema | Retrieve the information schema for the specified connection
[**list_connections**](ConnectionsApi.md#list_connections) | **GET** /companies/{company_id}/connections | Get all connections for a specific company
[**update_connections**](ConnectionsApi.md#update_connections) | **PATCH** /companies/{company_id}/connections/{connection_id} | Update an existing connection by ID


# **create_connections**
> CreateConnections200Response create_connections(company_id, connections_input, page=page, limit=limit, sort_by=sort_by, sort_order=sort_order, search=search)

Create a new connection by ID

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.connections_input import ConnectionsInput
from spartera_api_sdk.models.create_connections200_response import CreateConnections200Response
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
    api_instance = spartera_api_sdk.ConnectionsApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    connections_input = spartera_api_sdk.ConnectionsInput() # ConnectionsInput | 
    page = 1 # int | Page number for pagination (optional) (default to 1)
    limit = 20 # int | Number of items per page (optional) (default to 20)
    sort_by = 'sort_by_example' # str | Field to sort by (optional)
    sort_order = desc # str | Sort order (ascending or descending) (optional) (default to desc)
    search = 'search_example' # str | Search term to filter results (optional)

    try:
        # Create a new connection by ID
        api_response = api_instance.create_connections(company_id, connections_input, page=page, limit=limit, sort_by=sort_by, sort_order=sort_order, search=search)
        print("The response of ConnectionsApi->create_connections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectionsApi->create_connections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **connections_input** | [**ConnectionsInput**](ConnectionsInput.md)|  | 
 **page** | **int**| Page number for pagination | [optional] [default to 1]
 **limit** | **int**| Number of items per page | [optional] [default to 20]
 **sort_by** | **str**| Field to sort by | [optional] 
 **sort_order** | **str**| Sort order (ascending or descending) | [optional] [default to desc]
 **search** | **str**| Search term to filter results | [optional] 

### Return type

[**CreateConnections200Response**](CreateConnections200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created connections |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**400** | Invalid input |  -  |
**409** | Resource conflict (duplicate, constraint violation) |  -  |
**422** | Request well-formed but semantically invalid |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_connections**
> DeleteConnections200Response delete_connections(company_id, connection_id)

Delete single connection by ID

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.delete_connections200_response import DeleteConnections200Response
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
    api_instance = spartera_api_sdk.ConnectionsApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    connection_id = 'connection_id_example' # str | Unique identifier for the Connection

    try:
        # Delete single connection by ID
        api_response = api_instance.delete_connections(company_id, connection_id)
        print("The response of ConnectionsApi->delete_connections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectionsApi->delete_connections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **connection_id** | **str**| Unique identifier for the Connection | 

### Return type

[**DeleteConnections200Response**](DeleteConnections200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully deleted connections |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connections_by_id**
> GetConnectionsById200Response get_connections_by_id(company_id, connection_id)

Get single connection by ID

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.get_connections_by_id200_response import GetConnectionsById200Response
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
    api_instance = spartera_api_sdk.ConnectionsApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    connection_id = 'connection_id_example' # str | Unique identifier for the Connection

    try:
        # Get single connection by ID
        api_response = api_instance.get_connections_by_id(company_id, connection_id)
        print("The response of ConnectionsApi->get_connections_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectionsApi->get_connections_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **connection_id** | **str**| Unique identifier for the Connection | 

### Return type

[**GetConnectionsById200Response**](GetConnectionsById200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved connections |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connections_by_id2**
> GetConnectionsById200Response get_connections_by_id2(company_id, connection_id)

Test the specified connection

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.get_connections_by_id200_response import GetConnectionsById200Response
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
    api_instance = spartera_api_sdk.ConnectionsApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    connection_id = 'connection_id_example' # str | Unique identifier for the Connection

    try:
        # Test the specified connection
        api_response = api_instance.get_connections_by_id2(company_id, connection_id)
        print("The response of ConnectionsApi->get_connections_by_id2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectionsApi->get_connections_by_id2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **connection_id** | **str**| Unique identifier for the Connection | 

### Return type

[**GetConnectionsById200Response**](GetConnectionsById200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved connections |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connections_by_id_infoschema**
> GetConnectionsById200Response get_connections_by_id_infoschema(company_id, connection_id)

Retrieve the information schema for the specified connection

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.get_connections_by_id200_response import GetConnectionsById200Response
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
    api_instance = spartera_api_sdk.ConnectionsApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    connection_id = 'connection_id_example' # str | Unique identifier for the Connection

    try:
        # Retrieve the information schema for the specified connection
        api_response = api_instance.get_connections_by_id_infoschema(company_id, connection_id)
        print("The response of ConnectionsApi->get_connections_by_id_infoschema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectionsApi->get_connections_by_id_infoschema: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **connection_id** | **str**| Unique identifier for the Connection | 

### Return type

[**GetConnectionsById200Response**](GetConnectionsById200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved connections |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_connections**
> ListConnections200Response list_connections(company_id, page=page, limit=limit, sort_by=sort_by, sort_order=sort_order, search=search)

Get all connections for a specific company

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.list_connections200_response import ListConnections200Response
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
    api_instance = spartera_api_sdk.ConnectionsApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    page = 1 # int | Page number for pagination (optional) (default to 1)
    limit = 20 # int | Number of items per page (optional) (default to 20)
    sort_by = 'sort_by_example' # str | Field to sort by (optional)
    sort_order = desc # str | Sort order (ascending or descending) (optional) (default to desc)
    search = 'search_example' # str | Search term to filter results (optional)

    try:
        # Get all connections for a specific company
        api_response = api_instance.list_connections(company_id, page=page, limit=limit, sort_by=sort_by, sort_order=sort_order, search=search)
        print("The response of ConnectionsApi->list_connections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectionsApi->list_connections: %s\n" % e)
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

[**ListConnections200Response**](ListConnections200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved connections |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_connections**
> UpdateConnections200Response update_connections(company_id, connection_id, connections_update)

Update an existing connection by ID

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.connections_update import ConnectionsUpdate
from spartera_api_sdk.models.update_connections200_response import UpdateConnections200Response
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
    api_instance = spartera_api_sdk.ConnectionsApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    connection_id = 'connection_id_example' # str | Unique identifier for the Connection
    connections_update = spartera_api_sdk.ConnectionsUpdate() # ConnectionsUpdate | 

    try:
        # Update an existing connection by ID
        api_response = api_instance.update_connections(company_id, connection_id, connections_update)
        print("The response of ConnectionsApi->update_connections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectionsApi->update_connections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **connection_id** | **str**| Unique identifier for the Connection | 
 **connections_update** | [**ConnectionsUpdate**](ConnectionsUpdate.md)|  | 

### Return type

[**UpdateConnections200Response**](UpdateConnections200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated connections |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**400** | Invalid input |  -  |
**409** | Resource conflict (duplicate, constraint violation) |  -  |
**422** | Request well-formed but semantically invalid |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

