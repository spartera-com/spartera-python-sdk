# spartera_api_sdk.ConnectionsApi

All URIs are relative to *https://api.spartera.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companies_company_id_connections_connection_id_delete**](ConnectionsApi.md#companies_company_id_connections_connection_id_delete) | **DELETE** /companies/{company_id}/connections/{connection_id} | Delete single connection by ID
[**companies_company_id_connections_connection_id_get**](ConnectionsApi.md#companies_company_id_connections_connection_id_get) | **GET** /companies/{company_id}/connections/{connection_id} | Get single connection by ID
[**companies_company_id_connections_connection_id_infoschema_get**](ConnectionsApi.md#companies_company_id_connections_connection_id_infoschema_get) | **GET** /companies/{company_id}/connections/{connection_id}/infoschema | Retrieve the information schema for the specified connection
[**companies_company_id_connections_connection_id_patch**](ConnectionsApi.md#companies_company_id_connections_connection_id_patch) | **PATCH** /companies/{company_id}/connections/{connection_id} | Update an existing connection by ID
[**companies_company_id_connections_connection_id_test_get**](ConnectionsApi.md#companies_company_id_connections_connection_id_test_get) | **GET** /companies/{company_id}/connections/{connection_id}/test | Test the specified connection
[**companies_company_id_connections_get**](ConnectionsApi.md#companies_company_id_connections_get) | **GET** /companies/{company_id}/connections | Get all connections for a specific company
[**companies_company_id_connections_post**](ConnectionsApi.md#companies_company_id_connections_post) | **POST** /companies/{company_id}/connections | Create a new connection by ID


# **companies_company_id_connections_connection_id_delete**
> CompaniesCompanyIdConnectionsConnectionIdDelete200Response companies_company_id_connections_connection_id_delete(company_id, connection_id)

Delete single connection by ID

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.companies_company_id_connections_connection_id_delete200_response import CompaniesCompanyIdConnectionsConnectionIdDelete200Response
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

[**CompaniesCompanyIdConnectionsConnectionIdDelete200Response**](CompaniesCompanyIdConnectionsConnectionIdDelete200Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_connections_connection_id_get**
> CompaniesCompanyIdConnectionsConnectionIdGet200Response companies_company_id_connections_connection_id_get(company_id, connection_id)

Get single connection by ID

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.companies_company_id_connections_connection_id_get200_response import CompaniesCompanyIdConnectionsConnectionIdGet200Response
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

[**CompaniesCompanyIdConnectionsConnectionIdGet200Response**](CompaniesCompanyIdConnectionsConnectionIdGet200Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_connections_connection_id_infoschema_get**
> CompaniesCompanyIdConnectionsGet200Response companies_company_id_connections_connection_id_infoschema_get(company_id, connection_id)

Retrieve the information schema for the specified connection

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.companies_company_id_connections_get200_response import CompaniesCompanyIdConnectionsGet200Response
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

[**CompaniesCompanyIdConnectionsGet200Response**](CompaniesCompanyIdConnectionsGet200Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_connections_connection_id_patch**
> CompaniesCompanyIdConnectionsConnectionIdPatch200Response companies_company_id_connections_connection_id_patch(company_id, connection_id, connections_update)

Update an existing connection by ID

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.companies_company_id_connections_connection_id_patch200_response import CompaniesCompanyIdConnectionsConnectionIdPatch200Response
from spartera_api_sdk.models.connections_update import ConnectionsUpdate
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
    company_id = 'company_id_example' # str | 
    connection_id = 'connection_id_example' # str | 
    connections_update = spartera_api_sdk.ConnectionsUpdate() # ConnectionsUpdate | 

    try:
        # Update an existing connection by ID
        api_response = api_instance.companies_company_id_connections_connection_id_patch(company_id, connection_id, connections_update)
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
 **connections_update** | [**ConnectionsUpdate**](ConnectionsUpdate.md)|  | 

### Return type

[**CompaniesCompanyIdConnectionsConnectionIdPatch200Response**](CompaniesCompanyIdConnectionsConnectionIdPatch200Response.md)

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
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_connections_connection_id_test_get**
> CompaniesCompanyIdConnectionsGet200Response companies_company_id_connections_connection_id_test_get(company_id, connection_id)

Test the specified connection

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.companies_company_id_connections_get200_response import CompaniesCompanyIdConnectionsGet200Response
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
    company_id = 'company_id_example' # str | 
    connection_id = 'connection_id_example' # str | 

    try:
        # Test the specified connection
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

[**CompaniesCompanyIdConnectionsGet200Response**](CompaniesCompanyIdConnectionsGet200Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_connections_get**
> CompaniesCompanyIdConnectionsGet200Response companies_company_id_connections_get(company_id)

Get all connections for a specific company

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.companies_company_id_connections_get200_response import CompaniesCompanyIdConnectionsGet200Response
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

[**CompaniesCompanyIdConnectionsGet200Response**](CompaniesCompanyIdConnectionsGet200Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_connections_post**
> CompaniesCompanyIdConnectionsPost200Response companies_company_id_connections_post(company_id, connections_input)

Create a new connection by ID

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.companies_company_id_connections_post200_response import CompaniesCompanyIdConnectionsPost200Response
from spartera_api_sdk.models.connections_input import ConnectionsInput
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
    company_id = 'company_id_example' # str | 
    connections_input = spartera_api_sdk.ConnectionsInput() # ConnectionsInput | 

    try:
        # Create a new connection by ID
        api_response = api_instance.companies_company_id_connections_post(company_id, connections_input)
        print("The response of ConnectionsApi->companies_company_id_connections_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectionsApi->companies_company_id_connections_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  | 
 **connections_input** | [**ConnectionsInput**](ConnectionsInput.md)|  | 

### Return type

[**CompaniesCompanyIdConnectionsPost200Response**](CompaniesCompanyIdConnectionsPost200Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

