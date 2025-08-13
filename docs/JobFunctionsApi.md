# spartera_api_sdk.JobFunctionsApi

All URIs are relative to *https://api.spartera.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**job_functions_function_id_get**](JobFunctionsApi.md#job_functions_function_id_get) | **GET** /job-functions/{function_id} | Get single job function by ID
[**job_functions_get**](JobFunctionsApi.md#job_functions_get) | **GET** /job-functions | Get a list of all job functions


# **job_functions_function_id_get**
> JobFunctionsFunctionIdGet200Response job_functions_function_id_get(function_id)

Get single job function by ID

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.job_functions_function_id_get200_response import JobFunctionsFunctionIdGet200Response
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
    api_instance = spartera_api_sdk.JobFunctionsApi(api_client)
    function_id = 'function_id_example' # str | 

    try:
        # Get single job function by ID
        api_response = api_instance.job_functions_function_id_get(function_id)
        print("The response of JobFunctionsApi->job_functions_function_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobFunctionsApi->job_functions_function_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_id** | **str**|  | 

### Return type

[**JobFunctionsFunctionIdGet200Response**](JobFunctionsFunctionIdGet200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved job functions |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **job_functions_get**
> JobFunctionsGet200Response job_functions_get()

Get a list of all job functions

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.job_functions_get200_response import JobFunctionsGet200Response
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
    api_instance = spartera_api_sdk.JobFunctionsApi(api_client)

    try:
        # Get a list of all job functions
        api_response = api_instance.job_functions_get()
        print("The response of JobFunctionsApi->job_functions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobFunctionsApi->job_functions_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**JobFunctionsGet200Response**](JobFunctionsGet200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved job functions |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

