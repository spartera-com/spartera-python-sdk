# spartera_api_sdk.JobFunctionsApi

All URIs are relative to *https://api.spartera.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_job_functions_by_id**](JobFunctionsApi.md#get_job_functions_by_id) | **GET** /job-functions/{function_id} | Get single job function by ID
[**list_job_functions**](JobFunctionsApi.md#list_job_functions) | **GET** /job-functions | Get a list of all job functions


# **get_job_functions_by_id**
> GetJobFunctionsById200Response get_job_functions_by_id(function_id)

Get single job function by ID

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.get_job_functions_by_id200_response import GetJobFunctionsById200Response
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
    function_id = 'function_id_example' # str | Unique identifier for the Function

    try:
        # Get single job function by ID
        api_response = api_instance.get_job_functions_by_id(function_id)
        print("The response of JobFunctionsApi->get_job_functions_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobFunctionsApi->get_job_functions_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_id** | **str**| Unique identifier for the Function | 

### Return type

[**GetJobFunctionsById200Response**](GetJobFunctionsById200Response.md)

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
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_job_functions**
> ListJobFunctions200Response list_job_functions(page=page, limit=limit, sort_by=sort_by, sort_order=sort_order, search=search)

Get a list of all job functions

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.list_job_functions200_response import ListJobFunctions200Response
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
    page = 1 # int | Page number for pagination (optional) (default to 1)
    limit = 20 # int | Number of items per page (optional) (default to 20)
    sort_by = 'sort_by_example' # str | Field to sort by (optional)
    sort_order = desc # str | Sort order (ascending or descending) (optional) (default to desc)
    search = 'search_example' # str | Search term to filter results (optional)

    try:
        # Get a list of all job functions
        api_response = api_instance.list_job_functions(page=page, limit=limit, sort_by=sort_by, sort_order=sort_order, search=search)
        print("The response of JobFunctionsApi->list_job_functions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobFunctionsApi->list_job_functions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number for pagination | [optional] [default to 1]
 **limit** | **int**| Number of items per page | [optional] [default to 20]
 **sort_by** | **str**| Field to sort by | [optional] 
 **sort_order** | **str**| Sort order (ascending or descending) | [optional] [default to desc]
 **search** | **str**| Search term to filter results | [optional] 

### Return type

[**ListJobFunctions200Response**](ListJobFunctions200Response.md)

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
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

