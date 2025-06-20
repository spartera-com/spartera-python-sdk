# spartera_api_sdk.AlertsApi

All URIs are relative to *https://api.spartera.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companies_company_id_users_user_id_alerts_alert_id_delete**](AlertsApi.md#companies_company_id_users_user_id_alerts_alert_id_delete) | **DELETE** /companies/{company_id}/users/{user_id}/alerts/{alert_id} | Delete single alert by ID
[**companies_company_id_users_user_id_alerts_alert_id_get**](AlertsApi.md#companies_company_id_users_user_id_alerts_alert_id_get) | **GET** /companies/{company_id}/users/{user_id}/alerts/{alert_id} | Get single alert by ID
[**companies_company_id_users_user_id_alerts_alert_id_patch**](AlertsApi.md#companies_company_id_users_user_id_alerts_alert_id_patch) | **PATCH** /companies/{company_id}/users/{user_id}/alerts/{alert_id} | Update an existing alert by ID
[**companies_company_id_users_user_id_alerts_asset_asset_id_all_get**](AlertsApi.md#companies_company_id_users_user_id_alerts_asset_asset_id_all_get) | **GET** /companies/{company_id}/users/{user_id}/alerts/asset/{asset_id}/all | Get all alerts for a specific asset
[**companies_company_id_users_user_id_alerts_asset_asset_id_get**](AlertsApi.md#companies_company_id_users_user_id_alerts_asset_asset_id_get) | **GET** /companies/{company_id}/users/{user_id}/alerts/asset/{asset_id} | Get all alerts for a specific asset (by user)
[**companies_company_id_users_user_id_alerts_get**](AlertsApi.md#companies_company_id_users_user_id_alerts_get) | **GET** /companies/{company_id}/users/{user_id}/alerts | Get a list of all alerts for a specific user
[**companies_company_id_users_user_id_alerts_post**](AlertsApi.md#companies_company_id_users_user_id_alerts_post) | **POST** /companies/{company_id}/users/{user_id}/alerts | POST /companies/{company_id}/users/{user_id}/alerts


# **companies_company_id_users_user_id_alerts_alert_id_delete**
> CompaniesCompanyIdUsersUserIdAlertsAlertIdDelete200Response companies_company_id_users_user_id_alerts_alert_id_delete(company_id, user_id, alert_id)

Delete single alert by ID

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.companies_company_id_users_user_id_alerts_alert_id_delete200_response import CompaniesCompanyIdUsersUserIdAlertsAlertIdDelete200Response
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
    company_id = 'company_id_example' # str | 
    user_id = 'user_id_example' # str | 
    alert_id = 'alert_id_example' # str | 

    try:
        # Delete single alert by ID
        api_response = api_instance.companies_company_id_users_user_id_alerts_alert_id_delete(company_id, user_id, alert_id)
        print("The response of AlertsApi->companies_company_id_users_user_id_alerts_alert_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->companies_company_id_users_user_id_alerts_alert_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  | 
 **user_id** | **str**|  | 
 **alert_id** | **str**|  | 

### Return type

[**CompaniesCompanyIdUsersUserIdAlertsAlertIdDelete200Response**](CompaniesCompanyIdUsersUserIdAlertsAlertIdDelete200Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_users_user_id_alerts_alert_id_get**
> CompaniesCompanyIdUsersUserIdAlertsAlertIdGet200Response companies_company_id_users_user_id_alerts_alert_id_get(company_id, user_id, alert_id)

Get single alert by ID

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.companies_company_id_users_user_id_alerts_alert_id_get200_response import CompaniesCompanyIdUsersUserIdAlertsAlertIdGet200Response
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
    company_id = 'company_id_example' # str | 
    user_id = 'user_id_example' # str | 
    alert_id = 'alert_id_example' # str | 

    try:
        # Get single alert by ID
        api_response = api_instance.companies_company_id_users_user_id_alerts_alert_id_get(company_id, user_id, alert_id)
        print("The response of AlertsApi->companies_company_id_users_user_id_alerts_alert_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->companies_company_id_users_user_id_alerts_alert_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  | 
 **user_id** | **str**|  | 
 **alert_id** | **str**|  | 

### Return type

[**CompaniesCompanyIdUsersUserIdAlertsAlertIdGet200Response**](CompaniesCompanyIdUsersUserIdAlertsAlertIdGet200Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_users_user_id_alerts_alert_id_patch**
> CompaniesCompanyIdUsersUserIdAlertsAlertIdPatch200Response companies_company_id_users_user_id_alerts_alert_id_patch(company_id, user_id, alert_id, alert)

Update an existing alert by ID

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.alert import Alert
from spartera_api_sdk.models.companies_company_id_users_user_id_alerts_alert_id_patch200_response import CompaniesCompanyIdUsersUserIdAlertsAlertIdPatch200Response
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
    company_id = 'company_id_example' # str | 
    user_id = 'user_id_example' # str | 
    alert_id = 'alert_id_example' # str | 
    alert = spartera_api_sdk.Alert() # Alert | 

    try:
        # Update an existing alert by ID
        api_response = api_instance.companies_company_id_users_user_id_alerts_alert_id_patch(company_id, user_id, alert_id, alert)
        print("The response of AlertsApi->companies_company_id_users_user_id_alerts_alert_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->companies_company_id_users_user_id_alerts_alert_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  | 
 **user_id** | **str**|  | 
 **alert_id** | **str**|  | 
 **alert** | [**Alert**](Alert.md)|  | 

### Return type

[**CompaniesCompanyIdUsersUserIdAlertsAlertIdPatch200Response**](CompaniesCompanyIdUsersUserIdAlertsAlertIdPatch200Response.md)

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
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_users_user_id_alerts_asset_asset_id_all_get**
> CompaniesCompanyIdUsersUserIdAlertsGet200Response companies_company_id_users_user_id_alerts_asset_asset_id_all_get(company_id, user_id, asset_id)

Get all alerts for a specific asset

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.companies_company_id_users_user_id_alerts_get200_response import CompaniesCompanyIdUsersUserIdAlertsGet200Response
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
    company_id = 'company_id_example' # str | 
    user_id = 'user_id_example' # str | 
    asset_id = 'asset_id_example' # str | 

    try:
        # Get all alerts for a specific asset
        api_response = api_instance.companies_company_id_users_user_id_alerts_asset_asset_id_all_get(company_id, user_id, asset_id)
        print("The response of AlertsApi->companies_company_id_users_user_id_alerts_asset_asset_id_all_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->companies_company_id_users_user_id_alerts_asset_asset_id_all_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  | 
 **user_id** | **str**|  | 
 **asset_id** | **str**|  | 

### Return type

[**CompaniesCompanyIdUsersUserIdAlertsGet200Response**](CompaniesCompanyIdUsersUserIdAlertsGet200Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_users_user_id_alerts_asset_asset_id_get**
> CompaniesCompanyIdUsersUserIdAlertsAlertIdGet200Response companies_company_id_users_user_id_alerts_asset_asset_id_get(company_id, user_id, asset_id)

Get all alerts for a specific asset (by user)

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.companies_company_id_users_user_id_alerts_alert_id_get200_response import CompaniesCompanyIdUsersUserIdAlertsAlertIdGet200Response
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
    company_id = 'company_id_example' # str | 
    user_id = 'user_id_example' # str | 
    asset_id = 'asset_id_example' # str | 

    try:
        # Get all alerts for a specific asset (by user)
        api_response = api_instance.companies_company_id_users_user_id_alerts_asset_asset_id_get(company_id, user_id, asset_id)
        print("The response of AlertsApi->companies_company_id_users_user_id_alerts_asset_asset_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->companies_company_id_users_user_id_alerts_asset_asset_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  | 
 **user_id** | **str**|  | 
 **asset_id** | **str**|  | 

### Return type

[**CompaniesCompanyIdUsersUserIdAlertsAlertIdGet200Response**](CompaniesCompanyIdUsersUserIdAlertsAlertIdGet200Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_users_user_id_alerts_get**
> CompaniesCompanyIdUsersUserIdAlertsGet200Response companies_company_id_users_user_id_alerts_get(company_id, user_id)

Get a list of all alerts for a specific user

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.companies_company_id_users_user_id_alerts_get200_response import CompaniesCompanyIdUsersUserIdAlertsGet200Response
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
    company_id = 'company_id_example' # str | 
    user_id = 'user_id_example' # str | 

    try:
        # Get a list of all alerts for a specific user
        api_response = api_instance.companies_company_id_users_user_id_alerts_get(company_id, user_id)
        print("The response of AlertsApi->companies_company_id_users_user_id_alerts_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->companies_company_id_users_user_id_alerts_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**CompaniesCompanyIdUsersUserIdAlertsGet200Response**](CompaniesCompanyIdUsersUserIdAlertsGet200Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_users_user_id_alerts_post**
> CompaniesCompanyIdUsersUserIdAlertsPost200Response companies_company_id_users_user_id_alerts_post(company_id, user_id, alert)

POST /companies/{company_id}/users/{user_id}/alerts

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.alert import Alert
from spartera_api_sdk.models.companies_company_id_users_user_id_alerts_post200_response import CompaniesCompanyIdUsersUserIdAlertsPost200Response
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
    company_id = 'company_id_example' # str | 
    user_id = 'user_id_example' # str | 
    alert = spartera_api_sdk.Alert() # Alert | 

    try:
        # POST /companies/{company_id}/users/{user_id}/alerts
        api_response = api_instance.companies_company_id_users_user_id_alerts_post(company_id, user_id, alert)
        print("The response of AlertsApi->companies_company_id_users_user_id_alerts_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->companies_company_id_users_user_id_alerts_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  | 
 **user_id** | **str**|  | 
 **alert** | [**Alert**](Alert.md)|  | 

### Return type

[**CompaniesCompanyIdUsersUserIdAlertsPost200Response**](CompaniesCompanyIdUsersUserIdAlertsPost200Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

