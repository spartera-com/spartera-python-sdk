# spartera_api_sdk.PostgenIntegrationsApi

All URIs are relative to *https://api.spartera.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_postgen_integrations**](PostgenIntegrationsApi.md#create_postgen_integrations) | **POST** /companies/{company_id}/postgen_integrations | POST /companies/{company_id}/postgen_integrations
[**create_postgen_integrations_test**](PostgenIntegrationsApi.md#create_postgen_integrations_test) | **POST** /companies/{company_id}/postgen_integrations/test | POST /companies/{company_id}/postgen_integrations/test
[**delete_postgen_integrations**](PostgenIntegrationsApi.md#delete_postgen_integrations) | **DELETE** /companies/{company_id}/postgen_integrations/{integration_id} | Delete single integration by ID.     Also deletes credentials from GCP Secret Manager.
[**get_postgen_integrations_by_id**](PostgenIntegrationsApi.md#get_postgen_integrations_by_id) | **GET** /companies/{company_id}/postgen_integrations/{integration_id} | Get single integration by ID.
[**list_postgen_integrations**](PostgenIntegrationsApi.md#list_postgen_integrations) | **GET** /companies/{company_id}/postgen_integrations | Get a list of all postgen integrations for the company.     All company users can view integrations.
[**update_postgen_integrations**](PostgenIntegrationsApi.md#update_postgen_integrations) | **PATCH** /companies/{company_id}/postgen_integrations/{integration_id} | Update an existing integration by ID.      Can update credentials, is_active status, etc.


# **create_postgen_integrations**
> CreatePostgenIntegrations200Response create_postgen_integrations(company_id, postgen_integrations_input, page=page, limit=limit, sort_by=sort_by, sort_order=sort_order, search=search)

POST /companies/{company_id}/postgen_integrations

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.create_postgen_integrations200_response import CreatePostgenIntegrations200Response
from spartera_api_sdk.models.postgen_integrations_input import PostgenIntegrationsInput
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
    api_instance = spartera_api_sdk.PostgenIntegrationsApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    postgen_integrations_input = spartera_api_sdk.PostgenIntegrationsInput() # PostgenIntegrationsInput | 
    page = 1 # int | Page number for pagination (optional) (default to 1)
    limit = 20 # int | Number of items per page (optional) (default to 20)
    sort_by = 'sort_by_example' # str | Field to sort by (optional)
    sort_order = desc # str | Sort order (ascending or descending) (optional) (default to desc)
    search = 'search_example' # str | Search term to filter results (optional)

    try:
        # POST /companies/{company_id}/postgen_integrations
        api_response = api_instance.create_postgen_integrations(company_id, postgen_integrations_input, page=page, limit=limit, sort_by=sort_by, sort_order=sort_order, search=search)
        print("The response of PostgenIntegrationsApi->create_postgen_integrations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostgenIntegrationsApi->create_postgen_integrations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **postgen_integrations_input** | [**PostgenIntegrationsInput**](PostgenIntegrationsInput.md)|  | 
 **page** | **int**| Page number for pagination | [optional] [default to 1]
 **limit** | **int**| Number of items per page | [optional] [default to 20]
 **sort_by** | **str**| Field to sort by | [optional] 
 **sort_order** | **str**| Sort order (ascending or descending) | [optional] [default to desc]
 **search** | **str**| Search term to filter results | [optional] 

### Return type

[**CreatePostgenIntegrations200Response**](CreatePostgenIntegrations200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created postgen integrations |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**400** | Invalid input |  -  |
**409** | Resource conflict (duplicate, constraint violation) |  -  |
**422** | Request well-formed but semantically invalid |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_postgen_integrations_test**
> CreatePostgenIntegrations200Response create_postgen_integrations_test(company_id, postgen_integrations_input)

POST /companies/{company_id}/postgen_integrations/test

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.create_postgen_integrations200_response import CreatePostgenIntegrations200Response
from spartera_api_sdk.models.postgen_integrations_input import PostgenIntegrationsInput
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
    api_instance = spartera_api_sdk.PostgenIntegrationsApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    postgen_integrations_input = spartera_api_sdk.PostgenIntegrationsInput() # PostgenIntegrationsInput | 

    try:
        # POST /companies/{company_id}/postgen_integrations/test
        api_response = api_instance.create_postgen_integrations_test(company_id, postgen_integrations_input)
        print("The response of PostgenIntegrationsApi->create_postgen_integrations_test:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostgenIntegrationsApi->create_postgen_integrations_test: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **postgen_integrations_input** | [**PostgenIntegrationsInput**](PostgenIntegrationsInput.md)|  | 

### Return type

[**CreatePostgenIntegrations200Response**](CreatePostgenIntegrations200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created postgen integrations |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**400** | Invalid input |  -  |
**409** | Resource conflict (duplicate, constraint violation) |  -  |
**422** | Request well-formed but semantically invalid |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_postgen_integrations**
> DeletePostgenIntegrations200Response delete_postgen_integrations(company_id, integration_id)

Delete single integration by ID.     Also deletes credentials from GCP Secret Manager.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.delete_postgen_integrations200_response import DeletePostgenIntegrations200Response
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
    api_instance = spartera_api_sdk.PostgenIntegrationsApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    integration_id = 'integration_id_example' # str | Unique identifier for the Integration

    try:
        # Delete single integration by ID.     Also deletes credentials from GCP Secret Manager.
        api_response = api_instance.delete_postgen_integrations(company_id, integration_id)
        print("The response of PostgenIntegrationsApi->delete_postgen_integrations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostgenIntegrationsApi->delete_postgen_integrations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **integration_id** | **str**| Unique identifier for the Integration | 

### Return type

[**DeletePostgenIntegrations200Response**](DeletePostgenIntegrations200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully deleted postgen integrations |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_postgen_integrations_by_id**
> GetPostgenIntegrationsById200Response get_postgen_integrations_by_id(company_id, integration_id)

Get single integration by ID.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.get_postgen_integrations_by_id200_response import GetPostgenIntegrationsById200Response
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
    api_instance = spartera_api_sdk.PostgenIntegrationsApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    integration_id = 'integration_id_example' # str | Unique identifier for the Integration

    try:
        # Get single integration by ID.
        api_response = api_instance.get_postgen_integrations_by_id(company_id, integration_id)
        print("The response of PostgenIntegrationsApi->get_postgen_integrations_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostgenIntegrationsApi->get_postgen_integrations_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **integration_id** | **str**| Unique identifier for the Integration | 

### Return type

[**GetPostgenIntegrationsById200Response**](GetPostgenIntegrationsById200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved postgen integrations |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_postgen_integrations**
> ListPostgenIntegrations200Response list_postgen_integrations(company_id, page=page, limit=limit, sort_by=sort_by, sort_order=sort_order, search=search)

Get a list of all postgen integrations for the company.     All company users can view integrations.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.list_postgen_integrations200_response import ListPostgenIntegrations200Response
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
    api_instance = spartera_api_sdk.PostgenIntegrationsApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    page = 1 # int | Page number for pagination (optional) (default to 1)
    limit = 20 # int | Number of items per page (optional) (default to 20)
    sort_by = 'sort_by_example' # str | Field to sort by (optional)
    sort_order = desc # str | Sort order (ascending or descending) (optional) (default to desc)
    search = 'search_example' # str | Search term to filter results (optional)

    try:
        # Get a list of all postgen integrations for the company.     All company users can view integrations.
        api_response = api_instance.list_postgen_integrations(company_id, page=page, limit=limit, sort_by=sort_by, sort_order=sort_order, search=search)
        print("The response of PostgenIntegrationsApi->list_postgen_integrations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostgenIntegrationsApi->list_postgen_integrations: %s\n" % e)
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

[**ListPostgenIntegrations200Response**](ListPostgenIntegrations200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved postgen integrations |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_postgen_integrations**
> UpdatePostgenIntegrations200Response update_postgen_integrations(company_id, integration_id, postgen_integrations_update)

Update an existing integration by ID.      Can update credentials, is_active status, etc.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.postgen_integrations_update import PostgenIntegrationsUpdate
from spartera_api_sdk.models.update_postgen_integrations200_response import UpdatePostgenIntegrations200Response
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
    api_instance = spartera_api_sdk.PostgenIntegrationsApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    integration_id = 'integration_id_example' # str | Unique identifier for the Integration
    postgen_integrations_update = spartera_api_sdk.PostgenIntegrationsUpdate() # PostgenIntegrationsUpdate | 

    try:
        # Update an existing integration by ID.      Can update credentials, is_active status, etc.
        api_response = api_instance.update_postgen_integrations(company_id, integration_id, postgen_integrations_update)
        print("The response of PostgenIntegrationsApi->update_postgen_integrations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostgenIntegrationsApi->update_postgen_integrations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **integration_id** | **str**| Unique identifier for the Integration | 
 **postgen_integrations_update** | [**PostgenIntegrationsUpdate**](PostgenIntegrationsUpdate.md)|  | 

### Return type

[**UpdatePostgenIntegrations200Response**](UpdatePostgenIntegrations200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated postgen integrations |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**400** | Invalid input |  -  |
**409** | Resource conflict (duplicate, constraint violation) |  -  |
**422** | Request well-formed but semantically invalid |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

