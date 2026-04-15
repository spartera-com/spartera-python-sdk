# spartera_api_sdk.EndpointsApi

All URIs are relative to *https://api.spartera.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_endpoints**](EndpointsApi.md#create_endpoints) | **POST** /companies/{company_id}/endpoints | Create a new endpoint
[**create_endpoints_keys**](EndpointsApi.md#create_endpoints_keys) | **POST** /companies/{company_id}/endpoints/{endpoint_id}/keys | POST /companies/{company_id}/endpoints/{endpoint_id}/keys
[**delete_endpoints**](EndpointsApi.md#delete_endpoints) | **DELETE** /companies/{company_id}/endpoints/{endpoint_id} | Delete single endpoint by ID
[**delete_endpoints_keys**](EndpointsApi.md#delete_endpoints_keys) | **DELETE** /companies/{company_id}/endpoints/{endpoint_id}/keys/{api_key_id} | DELETE /companies/{company_id}/endpoints/{endpoint_id}/keys/{api_key_id}
[**get_endpoints_by_id**](EndpointsApi.md#get_endpoints_by_id) | **GET** /companies/{company_id}/endpoints/{endpoint_id} | Get single endpoint by ID
[**get_endpoints_by_id_available_endpoints**](EndpointsApi.md#get_endpoints_by_id_available_endpoints) | **GET** /companies/{company_id}/endpoints/{endpoint_id}/available-endpoints | GET /companies/{company_id}/endpoints/{endpoint_id}/available-endpoints
[**get_endpoints_by_id_connections_describe**](EndpointsApi.md#get_endpoints_by_id_connections_describe) | **GET** /companies/{company_id}/endpoints/../connections/{connection_id}/describe | Get schema information for a connection      Query parameters:         include_fields: Whether to include field information (default: true)         schemas: Optional comma-separated schemas to include         tables: Optional comma-separated tables to include
[**get_endpoints_by_id_execute**](EndpointsApi.md#get_endpoints_by_id_execute) | **GET** /companies/{company_id}/endpoints/{endpoint_id}/execute | Execute an endpoint with pagination support.      Customer-facing route that returns paginated data.     Query params: ?start&#x3D;0&amp;limit&#x3D;100
[**get_endpoints_by_id_keys**](EndpointsApi.md#get_endpoints_by_id_keys) | **GET** /companies/{company_id}/endpoints/{endpoint_id}/keys | GET /companies/{company_id}/endpoints/{endpoint_id}/keys
[**get_endpoints_by_id_stats**](EndpointsApi.md#get_endpoints_by_id_stats) | **GET** /companies/{company_id}/endpoints/{endpoint_id}/stats | Get usage statistics for an endpoint      Query parameters:         days: Number of days to analyze (default: 30)
[**get_endpoints_by_id_test**](EndpointsApi.md#get_endpoints_by_id_test) | **GET** /companies/{company_id}/endpoints/{endpoint_id}/test | Test an endpoint with sample data      Request body (optional):         limit: Number of sample rows to return (default: 10)
[**get_endpoints_by_id_url**](EndpointsApi.md#get_endpoints_by_id_url) | **GET** /companies/{company_id}/endpoints/{endpoint_id}/url | GET /companies/{company_id}/endpoints/{endpoint_id}/url
[**list_endpoints**](EndpointsApi.md#list_endpoints) | **GET** /companies/{company_id}/endpoints | Get all endpoints for a specific company with pagination, filtering, and sorting
[**update_endpoints**](EndpointsApi.md#update_endpoints) | **PATCH** /companies/{company_id}/endpoints/{endpoint_id} | Update an existing endpoint by ID


# **create_endpoints**
> CreateEndpoints200Response create_endpoints(company_id, endpoints_input, page=page, limit=limit, sort_by=sort_by, sort_order=sort_order, search=search)

Create a new endpoint

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.create_endpoints200_response import CreateEndpoints200Response
from spartera_api_sdk.models.endpoints_input import EndpointsInput
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
    api_instance = spartera_api_sdk.EndpointsApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    endpoints_input = spartera_api_sdk.EndpointsInput() # EndpointsInput | 
    page = 1 # int | Page number for pagination (optional) (default to 1)
    limit = 20 # int | Number of items per page (optional) (default to 20)
    sort_by = 'sort_by_example' # str | Field to sort by (optional)
    sort_order = desc # str | Sort order (ascending or descending) (optional) (default to desc)
    search = 'search_example' # str | Search term to filter results (optional)

    try:
        # Create a new endpoint
        api_response = api_instance.create_endpoints(company_id, endpoints_input, page=page, limit=limit, sort_by=sort_by, sort_order=sort_order, search=search)
        print("The response of EndpointsApi->create_endpoints:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->create_endpoints: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **endpoints_input** | [**EndpointsInput**](EndpointsInput.md)|  | 
 **page** | **int**| Page number for pagination | [optional] [default to 1]
 **limit** | **int**| Number of items per page | [optional] [default to 20]
 **sort_by** | **str**| Field to sort by | [optional] 
 **sort_order** | **str**| Sort order (ascending or descending) | [optional] [default to desc]
 **search** | **str**| Search term to filter results | [optional] 

### Return type

[**CreateEndpoints200Response**](CreateEndpoints200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created endpoints |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**400** | Invalid input |  -  |
**409** | Resource conflict (duplicate, constraint violation) |  -  |
**422** | Request well-formed but semantically invalid |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_endpoints_keys**
> CreateEndpoints200Response create_endpoints_keys(company_id, endpoint_id, endpoints_input)

POST /companies/{company_id}/endpoints/{endpoint_id}/keys

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.create_endpoints200_response import CreateEndpoints200Response
from spartera_api_sdk.models.endpoints_input import EndpointsInput
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
    api_instance = spartera_api_sdk.EndpointsApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    endpoint_id = 'endpoint_id_example' # str | Unique identifier for the Endpoint
    endpoints_input = spartera_api_sdk.EndpointsInput() # EndpointsInput | 

    try:
        # POST /companies/{company_id}/endpoints/{endpoint_id}/keys
        api_response = api_instance.create_endpoints_keys(company_id, endpoint_id, endpoints_input)
        print("The response of EndpointsApi->create_endpoints_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->create_endpoints_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **endpoint_id** | **str**| Unique identifier for the Endpoint | 
 **endpoints_input** | [**EndpointsInput**](EndpointsInput.md)|  | 

### Return type

[**CreateEndpoints200Response**](CreateEndpoints200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created endpoints |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**400** | Invalid input |  -  |
**409** | Resource conflict (duplicate, constraint violation) |  -  |
**422** | Request well-formed but semantically invalid |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_endpoints**
> DeleteEndpoints200Response delete_endpoints(company_id, endpoint_id)

Delete single endpoint by ID

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.delete_endpoints200_response import DeleteEndpoints200Response
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
    api_instance = spartera_api_sdk.EndpointsApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    endpoint_id = 'endpoint_id_example' # str | Unique identifier for the Endpoint

    try:
        # Delete single endpoint by ID
        api_response = api_instance.delete_endpoints(company_id, endpoint_id)
        print("The response of EndpointsApi->delete_endpoints:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->delete_endpoints: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **endpoint_id** | **str**| Unique identifier for the Endpoint | 

### Return type

[**DeleteEndpoints200Response**](DeleteEndpoints200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully deleted endpoints |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_endpoints_keys**
> DeleteEndpoints200Response delete_endpoints_keys(company_id, endpoint_id, api_key_id)

DELETE /companies/{company_id}/endpoints/{endpoint_id}/keys/{api_key_id}

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.delete_endpoints200_response import DeleteEndpoints200Response
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
    api_instance = spartera_api_sdk.EndpointsApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    endpoint_id = 'endpoint_id_example' # str | Unique identifier for the Endpoint
    api_key_id = 'api_key_id_example' # str | Unique identifier for the Api Key

    try:
        # DELETE /companies/{company_id}/endpoints/{endpoint_id}/keys/{api_key_id}
        api_response = api_instance.delete_endpoints_keys(company_id, endpoint_id, api_key_id)
        print("The response of EndpointsApi->delete_endpoints_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->delete_endpoints_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **endpoint_id** | **str**| Unique identifier for the Endpoint | 
 **api_key_id** | **str**| Unique identifier for the Api Key | 

### Return type

[**DeleteEndpoints200Response**](DeleteEndpoints200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully deleted endpoints |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_endpoints_by_id**
> GetEndpointsByIdConnectionsDescribe200Response get_endpoints_by_id(company_id, endpoint_id)

Get single endpoint by ID

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.get_endpoints_by_id_connections_describe200_response import GetEndpointsByIdConnectionsDescribe200Response
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
    api_instance = spartera_api_sdk.EndpointsApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    endpoint_id = 'endpoint_id_example' # str | Unique identifier for the Endpoint

    try:
        # Get single endpoint by ID
        api_response = api_instance.get_endpoints_by_id(company_id, endpoint_id)
        print("The response of EndpointsApi->get_endpoints_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->get_endpoints_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **endpoint_id** | **str**| Unique identifier for the Endpoint | 

### Return type

[**GetEndpointsByIdConnectionsDescribe200Response**](GetEndpointsByIdConnectionsDescribe200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved endpoints |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_endpoints_by_id_available_endpoints**
> GetEndpointsByIdConnectionsDescribe200Response get_endpoints_by_id_available_endpoints(company_id, endpoint_id)

GET /companies/{company_id}/endpoints/{endpoint_id}/available-endpoints

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.get_endpoints_by_id_connections_describe200_response import GetEndpointsByIdConnectionsDescribe200Response
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
    api_instance = spartera_api_sdk.EndpointsApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    endpoint_id = 'endpoint_id_example' # str | Unique identifier for the Endpoint

    try:
        # GET /companies/{company_id}/endpoints/{endpoint_id}/available-endpoints
        api_response = api_instance.get_endpoints_by_id_available_endpoints(company_id, endpoint_id)
        print("The response of EndpointsApi->get_endpoints_by_id_available_endpoints:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->get_endpoints_by_id_available_endpoints: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **endpoint_id** | **str**| Unique identifier for the Endpoint | 

### Return type

[**GetEndpointsByIdConnectionsDescribe200Response**](GetEndpointsByIdConnectionsDescribe200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved endpoints |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_endpoints_by_id_connections_describe**
> GetEndpointsByIdConnectionsDescribe200Response get_endpoints_by_id_connections_describe(company_id, connection_id)

Get schema information for a connection      Query parameters:         include_fields: Whether to include field information (default: true)         schemas: Optional comma-separated schemas to include         tables: Optional comma-separated tables to include

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.get_endpoints_by_id_connections_describe200_response import GetEndpointsByIdConnectionsDescribe200Response
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
    api_instance = spartera_api_sdk.EndpointsApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    connection_id = 'connection_id_example' # str | Unique identifier for the Connection

    try:
        # Get schema information for a connection      Query parameters:         include_fields: Whether to include field information (default: true)         schemas: Optional comma-separated schemas to include         tables: Optional comma-separated tables to include
        api_response = api_instance.get_endpoints_by_id_connections_describe(company_id, connection_id)
        print("The response of EndpointsApi->get_endpoints_by_id_connections_describe:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->get_endpoints_by_id_connections_describe: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **connection_id** | **str**| Unique identifier for the Connection | 

### Return type

[**GetEndpointsByIdConnectionsDescribe200Response**](GetEndpointsByIdConnectionsDescribe200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved endpoints |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_endpoints_by_id_execute**
> GetEndpointsByIdConnectionsDescribe200Response get_endpoints_by_id_execute(company_id, endpoint_id)

Execute an endpoint with pagination support.      Customer-facing route that returns paginated data.     Query params: ?start=0&limit=100

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.get_endpoints_by_id_connections_describe200_response import GetEndpointsByIdConnectionsDescribe200Response
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
    api_instance = spartera_api_sdk.EndpointsApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    endpoint_id = 'endpoint_id_example' # str | Unique identifier for the Endpoint

    try:
        # Execute an endpoint with pagination support.      Customer-facing route that returns paginated data.     Query params: ?start=0&limit=100
        api_response = api_instance.get_endpoints_by_id_execute(company_id, endpoint_id)
        print("The response of EndpointsApi->get_endpoints_by_id_execute:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->get_endpoints_by_id_execute: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **endpoint_id** | **str**| Unique identifier for the Endpoint | 

### Return type

[**GetEndpointsByIdConnectionsDescribe200Response**](GetEndpointsByIdConnectionsDescribe200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved endpoints |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_endpoints_by_id_keys**
> GetEndpointsByIdConnectionsDescribe200Response get_endpoints_by_id_keys(company_id, endpoint_id)

GET /companies/{company_id}/endpoints/{endpoint_id}/keys

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.get_endpoints_by_id_connections_describe200_response import GetEndpointsByIdConnectionsDescribe200Response
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
    api_instance = spartera_api_sdk.EndpointsApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    endpoint_id = 'endpoint_id_example' # str | Unique identifier for the Endpoint

    try:
        # GET /companies/{company_id}/endpoints/{endpoint_id}/keys
        api_response = api_instance.get_endpoints_by_id_keys(company_id, endpoint_id)
        print("The response of EndpointsApi->get_endpoints_by_id_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->get_endpoints_by_id_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **endpoint_id** | **str**| Unique identifier for the Endpoint | 

### Return type

[**GetEndpointsByIdConnectionsDescribe200Response**](GetEndpointsByIdConnectionsDescribe200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved endpoints |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_endpoints_by_id_stats**
> GetEndpointsByIdConnectionsDescribe200Response get_endpoints_by_id_stats(company_id, endpoint_id)

Get usage statistics for an endpoint      Query parameters:         days: Number of days to analyze (default: 30)

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.get_endpoints_by_id_connections_describe200_response import GetEndpointsByIdConnectionsDescribe200Response
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
    api_instance = spartera_api_sdk.EndpointsApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    endpoint_id = 'endpoint_id_example' # str | Unique identifier for the Endpoint

    try:
        # Get usage statistics for an endpoint      Query parameters:         days: Number of days to analyze (default: 30)
        api_response = api_instance.get_endpoints_by_id_stats(company_id, endpoint_id)
        print("The response of EndpointsApi->get_endpoints_by_id_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->get_endpoints_by_id_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **endpoint_id** | **str**| Unique identifier for the Endpoint | 

### Return type

[**GetEndpointsByIdConnectionsDescribe200Response**](GetEndpointsByIdConnectionsDescribe200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved endpoints |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_endpoints_by_id_test**
> GetEndpointsByIdConnectionsDescribe200Response get_endpoints_by_id_test(company_id, endpoint_id)

Test an endpoint with sample data      Request body (optional):         limit: Number of sample rows to return (default: 10)

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.get_endpoints_by_id_connections_describe200_response import GetEndpointsByIdConnectionsDescribe200Response
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
    api_instance = spartera_api_sdk.EndpointsApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    endpoint_id = 'endpoint_id_example' # str | Unique identifier for the Endpoint

    try:
        # Test an endpoint with sample data      Request body (optional):         limit: Number of sample rows to return (default: 10)
        api_response = api_instance.get_endpoints_by_id_test(company_id, endpoint_id)
        print("The response of EndpointsApi->get_endpoints_by_id_test:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->get_endpoints_by_id_test: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **endpoint_id** | **str**| Unique identifier for the Endpoint | 

### Return type

[**GetEndpointsByIdConnectionsDescribe200Response**](GetEndpointsByIdConnectionsDescribe200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved endpoints |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_endpoints_by_id_url**
> GetEndpointsByIdConnectionsDescribe200Response get_endpoints_by_id_url(company_id, endpoint_id)

GET /companies/{company_id}/endpoints/{endpoint_id}/url

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.get_endpoints_by_id_connections_describe200_response import GetEndpointsByIdConnectionsDescribe200Response
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
    api_instance = spartera_api_sdk.EndpointsApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    endpoint_id = 'endpoint_id_example' # str | Unique identifier for the Endpoint

    try:
        # GET /companies/{company_id}/endpoints/{endpoint_id}/url
        api_response = api_instance.get_endpoints_by_id_url(company_id, endpoint_id)
        print("The response of EndpointsApi->get_endpoints_by_id_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->get_endpoints_by_id_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **endpoint_id** | **str**| Unique identifier for the Endpoint | 

### Return type

[**GetEndpointsByIdConnectionsDescribe200Response**](GetEndpointsByIdConnectionsDescribe200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved endpoints |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_endpoints**
> ListEndpoints200Response list_endpoints(company_id, page=page, limit=limit, sort_by=sort_by, sort_order=sort_order, search=search)

Get all endpoints for a specific company with pagination, filtering, and sorting

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.list_endpoints200_response import ListEndpoints200Response
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
    api_instance = spartera_api_sdk.EndpointsApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    page = 1 # int | Page number for pagination (optional) (default to 1)
    limit = 20 # int | Number of items per page (optional) (default to 20)
    sort_by = 'sort_by_example' # str | Field to sort by (optional)
    sort_order = desc # str | Sort order (ascending or descending) (optional) (default to desc)
    search = 'search_example' # str | Search term to filter results (optional)

    try:
        # Get all endpoints for a specific company with pagination, filtering, and sorting
        api_response = api_instance.list_endpoints(company_id, page=page, limit=limit, sort_by=sort_by, sort_order=sort_order, search=search)
        print("The response of EndpointsApi->list_endpoints:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->list_endpoints: %s\n" % e)
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

[**ListEndpoints200Response**](ListEndpoints200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved endpoints |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_endpoints**
> UpdateEndpoints200Response update_endpoints(company_id, endpoint_id, endpoints_update)

Update an existing endpoint by ID

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.endpoints_update import EndpointsUpdate
from spartera_api_sdk.models.update_endpoints200_response import UpdateEndpoints200Response
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
    api_instance = spartera_api_sdk.EndpointsApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    endpoint_id = 'endpoint_id_example' # str | Unique identifier for the Endpoint
    endpoints_update = spartera_api_sdk.EndpointsUpdate() # EndpointsUpdate | 

    try:
        # Update an existing endpoint by ID
        api_response = api_instance.update_endpoints(company_id, endpoint_id, endpoints_update)
        print("The response of EndpointsApi->update_endpoints:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->update_endpoints: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **endpoint_id** | **str**| Unique identifier for the Endpoint | 
 **endpoints_update** | [**EndpointsUpdate**](EndpointsUpdate.md)|  | 

### Return type

[**UpdateEndpoints200Response**](UpdateEndpoints200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated endpoints |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**400** | Invalid input |  -  |
**409** | Resource conflict (duplicate, constraint violation) |  -  |
**422** | Request well-formed but semantically invalid |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

