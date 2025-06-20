# spartera_api_sdk.StorageEnginesApi

All URIs are relative to *https://api.spartera.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cloud_providers_provider_id_storage_engines_engine_id_get**](StorageEnginesApi.md#cloud_providers_provider_id_storage_engines_engine_id_get) | **GET** /cloud-providers/{provider_id}/storage-engines/{engine_id} | Get single storage engine by ID
[**cloud_providers_provider_id_storage_engines_get**](StorageEnginesApi.md#cloud_providers_provider_id_storage_engines_get) | **GET** /cloud-providers/{provider_id}/storage-engines | Get a list of all storage engines


# **cloud_providers_provider_id_storage_engines_engine_id_get**
> CompaniesCompanyIdApiKeysGet200Response cloud_providers_provider_id_storage_engines_engine_id_get(provider_id, engine_id)

Get single storage engine by ID

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
    api_instance = spartera_api_sdk.StorageEnginesApi(api_client)
    provider_id = 'provider_id_example' # str | 
    engine_id = 'engine_id_example' # str | 

    try:
        # Get single storage engine by ID
        api_response = api_instance.cloud_providers_provider_id_storage_engines_engine_id_get(provider_id, engine_id)
        print("The response of StorageEnginesApi->cloud_providers_provider_id_storage_engines_engine_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageEnginesApi->cloud_providers_provider_id_storage_engines_engine_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**|  | 
 **engine_id** | **str**|  | 

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
**200** | Successfully retrieved storage engines |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cloud_providers_provider_id_storage_engines_get**
> CompaniesCompanyIdApiKeysGet200Response cloud_providers_provider_id_storage_engines_get(provider_id)

Get a list of all storage engines

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
    api_instance = spartera_api_sdk.StorageEnginesApi(api_client)
    provider_id = 'provider_id_example' # str | 

    try:
        # Get a list of all storage engines
        api_response = api_instance.cloud_providers_provider_id_storage_engines_get(provider_id)
        print("The response of StorageEnginesApi->cloud_providers_provider_id_storage_engines_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageEnginesApi->cloud_providers_provider_id_storage_engines_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**|  | 

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
**200** | Successfully retrieved storage engines |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

