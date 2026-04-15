# spartera_api_sdk.AlertsApi

All URIs are relative to *https://api.spartera.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_alerts**](AlertsApi.md#create_alerts) | **POST** /companies/{company_id}/users/{user_id}/alerts | POST /companies/{company_id}/users/{user_id}/alerts
[**delete_alerts**](AlertsApi.md#delete_alerts) | **DELETE** /companies/{company_id}/users/{user_id}/alerts/{alert_id} | Delete single alert by ID
[**get_alerts_by_id**](AlertsApi.md#get_alerts_by_id) | **GET** /companies/{company_id}/users/{user_id}/alerts | Get a list of all alerts for a specific user
[**get_alerts_by_id_asset_all**](AlertsApi.md#get_alerts_by_id_asset_all) | **GET** /companies/{company_id}/users/{user_id}/alerts/asset/{asset_id}/all | Get all alerts for a specific asset
[**get_alerts_by_id_users**](AlertsApi.md#get_alerts_by_id_users) | **GET** /companies/{company_id}/users/{user_id}/alerts/{alert_id} | Get single alert by ID
[**get_alerts_by_id_users_asset**](AlertsApi.md#get_alerts_by_id_users_asset) | **GET** /companies/{company_id}/users/{user_id}/alerts/asset/{asset_id} | Get all alerts for a specific asset (by user)
[**update_alerts**](AlertsApi.md#update_alerts) | **PATCH** /companies/{company_id}/users/{user_id}/alerts/{alert_id} | Update an existing alert by ID


# **create_alerts**
> CreateAlerts200Response create_alerts(company_id, user_id, alerts_input)

POST /companies/{company_id}/users/{user_id}/alerts

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.alerts_input import AlertsInput
from spartera_api_sdk.models.create_alerts200_response import CreateAlerts200Response
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
    api_instance = spartera_api_sdk.AlertsApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    user_id = 'user_id_example' # str | Unique identifier for the User
    alerts_input = spartera_api_sdk.AlertsInput() # AlertsInput | 

    try:
        # POST /companies/{company_id}/users/{user_id}/alerts
        api_response = api_instance.create_alerts(company_id, user_id, alerts_input)
        print("The response of AlertsApi->create_alerts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->create_alerts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **user_id** | **str**| Unique identifier for the User | 
 **alerts_input** | [**AlertsInput**](AlertsInput.md)|  | 

### Return type

[**CreateAlerts200Response**](CreateAlerts200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created alerts |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**400** | Invalid input |  -  |
**409** | Resource conflict (duplicate, constraint violation) |  -  |
**422** | Request well-formed but semantically invalid |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_alerts**
> DeleteAlerts200Response delete_alerts(company_id, user_id, alert_id)

Delete single alert by ID

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.delete_alerts200_response import DeleteAlerts200Response
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
    api_instance = spartera_api_sdk.AlertsApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    user_id = 'user_id_example' # str | Unique identifier for the User
    alert_id = 'alert_id_example' # str | Unique identifier for the Alert

    try:
        # Delete single alert by ID
        api_response = api_instance.delete_alerts(company_id, user_id, alert_id)
        print("The response of AlertsApi->delete_alerts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->delete_alerts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **user_id** | **str**| Unique identifier for the User | 
 **alert_id** | **str**| Unique identifier for the Alert | 

### Return type

[**DeleteAlerts200Response**](DeleteAlerts200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully deleted alerts |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alerts_by_id**
> GetAlertsById200Response get_alerts_by_id(company_id, user_id)

Get a list of all alerts for a specific user

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.get_alerts_by_id200_response import GetAlertsById200Response
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
    api_instance = spartera_api_sdk.AlertsApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    user_id = 'user_id_example' # str | Unique identifier for the User

    try:
        # Get a list of all alerts for a specific user
        api_response = api_instance.get_alerts_by_id(company_id, user_id)
        print("The response of AlertsApi->get_alerts_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->get_alerts_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **user_id** | **str**| Unique identifier for the User | 

### Return type

[**GetAlertsById200Response**](GetAlertsById200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved alerts |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alerts_by_id_asset_all**
> GetAlertsById200Response get_alerts_by_id_asset_all(company_id, user_id, asset_id)

Get all alerts for a specific asset

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.get_alerts_by_id200_response import GetAlertsById200Response
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
    api_instance = spartera_api_sdk.AlertsApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    user_id = 'user_id_example' # str | Unique identifier for the User
    asset_id = 'asset_id_example' # str | Unique identifier for the Asset

    try:
        # Get all alerts for a specific asset
        api_response = api_instance.get_alerts_by_id_asset_all(company_id, user_id, asset_id)
        print("The response of AlertsApi->get_alerts_by_id_asset_all:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->get_alerts_by_id_asset_all: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **user_id** | **str**| Unique identifier for the User | 
 **asset_id** | **str**| Unique identifier for the Asset | 

### Return type

[**GetAlertsById200Response**](GetAlertsById200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved alerts |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alerts_by_id_users**
> GetAlertsById200Response get_alerts_by_id_users(company_id, user_id, alert_id)

Get single alert by ID

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.get_alerts_by_id200_response import GetAlertsById200Response
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
    api_instance = spartera_api_sdk.AlertsApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    user_id = 'user_id_example' # str | Unique identifier for the User
    alert_id = 'alert_id_example' # str | Unique identifier for the Alert

    try:
        # Get single alert by ID
        api_response = api_instance.get_alerts_by_id_users(company_id, user_id, alert_id)
        print("The response of AlertsApi->get_alerts_by_id_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->get_alerts_by_id_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **user_id** | **str**| Unique identifier for the User | 
 **alert_id** | **str**| Unique identifier for the Alert | 

### Return type

[**GetAlertsById200Response**](GetAlertsById200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved alerts |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alerts_by_id_users_asset**
> GetAlertsById200Response get_alerts_by_id_users_asset(company_id, user_id, asset_id)

Get all alerts for a specific asset (by user)

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.get_alerts_by_id200_response import GetAlertsById200Response
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
    api_instance = spartera_api_sdk.AlertsApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    user_id = 'user_id_example' # str | Unique identifier for the User
    asset_id = 'asset_id_example' # str | Unique identifier for the Asset

    try:
        # Get all alerts for a specific asset (by user)
        api_response = api_instance.get_alerts_by_id_users_asset(company_id, user_id, asset_id)
        print("The response of AlertsApi->get_alerts_by_id_users_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->get_alerts_by_id_users_asset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **user_id** | **str**| Unique identifier for the User | 
 **asset_id** | **str**| Unique identifier for the Asset | 

### Return type

[**GetAlertsById200Response**](GetAlertsById200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved alerts |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_alerts**
> UpdateAlerts200Response update_alerts(company_id, user_id, alert_id, alerts_update)

Update an existing alert by ID

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.alerts_update import AlertsUpdate
from spartera_api_sdk.models.update_alerts200_response import UpdateAlerts200Response
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
    api_instance = spartera_api_sdk.AlertsApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    user_id = 'user_id_example' # str | Unique identifier for the User
    alert_id = 'alert_id_example' # str | Unique identifier for the Alert
    alerts_update = spartera_api_sdk.AlertsUpdate() # AlertsUpdate | 

    try:
        # Update an existing alert by ID
        api_response = api_instance.update_alerts(company_id, user_id, alert_id, alerts_update)
        print("The response of AlertsApi->update_alerts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->update_alerts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **user_id** | **str**| Unique identifier for the User | 
 **alert_id** | **str**| Unique identifier for the Alert | 
 **alerts_update** | [**AlertsUpdate**](AlertsUpdate.md)|  | 

### Return type

[**UpdateAlerts200Response**](UpdateAlerts200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated alerts |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**400** | Invalid input |  -  |
**409** | Resource conflict (duplicate, constraint violation) |  -  |
**422** | Request well-formed but semantically invalid |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

