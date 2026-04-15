# spartera_api_sdk.StorageEnginesApi

All URIs are relative to *https://api.spartera.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_storage_engines_by_id**](StorageEnginesApi.md#get_storage_engines_by_id) | **GET** /cloud-providers/{provider_id}/storage-engines/{engine_id} | Get single storage engine by ID
[**list_storage_engines**](StorageEnginesApi.md#list_storage_engines) | **GET** /cloud-providers/{provider_id}/storage-engines | Get a list of all storage engines


# **get_storage_engines_by_id**
> GetStorageEnginesById200Response get_storage_engines_by_id(provider_id, engine_id)

Get single storage engine by ID

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.get_storage_engines_by_id200_response import GetStorageEnginesById200Response
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
    api_instance = spartera_api_sdk.StorageEnginesApi(api_client)
    provider_id = 'provider_id_example' # str | Unique identifier for the Provider
    engine_id = 'engine_id_example' # str | Unique identifier for the Engine

    try:
        # Get single storage engine by ID
        api_response = api_instance.get_storage_engines_by_id(provider_id, engine_id)
        print("The response of StorageEnginesApi->get_storage_engines_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageEnginesApi->get_storage_engines_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| Unique identifier for the Provider | 
 **engine_id** | **str**| Unique identifier for the Engine | 

### Return type

[**GetStorageEnginesById200Response**](GetStorageEnginesById200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved storage engines |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_storage_engines**
> ListStorageEngines200Response list_storage_engines(provider_id, page=page, limit=limit, sort_by=sort_by, sort_order=sort_order, search=search)

Get a list of all storage engines

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.list_storage_engines200_response import ListStorageEngines200Response
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
    api_instance = spartera_api_sdk.StorageEnginesApi(api_client)
    provider_id = 'provider_id_example' # str | Unique identifier for the Provider
    page = 1 # int | Page number for pagination (optional) (default to 1)
    limit = 20 # int | Number of items per page (optional) (default to 20)
    sort_by = 'sort_by_example' # str | Field to sort by (optional)
    sort_order = desc # str | Sort order (ascending or descending) (optional) (default to desc)
    search = 'search_example' # str | Search term to filter results (optional)

    try:
        # Get a list of all storage engines
        api_response = api_instance.list_storage_engines(provider_id, page=page, limit=limit, sort_by=sort_by, sort_order=sort_order, search=search)
        print("The response of StorageEnginesApi->list_storage_engines:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageEnginesApi->list_storage_engines: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| Unique identifier for the Provider | 
 **page** | **int**| Page number for pagination | [optional] [default to 1]
 **limit** | **int**| Number of items per page | [optional] [default to 20]
 **sort_by** | **str**| Field to sort by | [optional] 
 **sort_order** | **str**| Sort order (ascending or descending) | [optional] [default to desc]
 **search** | **str**| Search term to filter results | [optional] 

### Return type

[**ListStorageEngines200Response**](ListStorageEngines200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved storage engines |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

