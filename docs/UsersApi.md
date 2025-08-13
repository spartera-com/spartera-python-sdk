# spartera_api_sdk.UsersApi

All URIs are relative to *https://api.spartera.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companies_company_id_users_get**](UsersApi.md#companies_company_id_users_get) | **GET** /companies/{company_id}/users | Get a list of all users in a company
[**companies_company_id_users_post**](UsersApi.md#companies_company_id_users_post) | **POST** /companies/{company_id}/users | Create a new user
[**companies_company_id_users_user_id_delete**](UsersApi.md#companies_company_id_users_user_id_delete) | **DELETE** /companies/{company_id}/users/{user_id} | Delete single user by ID
[**companies_company_id_users_user_id_get**](UsersApi.md#companies_company_id_users_user_id_get) | **GET** /companies/{company_id}/users/{user_id} | Get single user by ID
[**companies_company_id_users_user_id_patch**](UsersApi.md#companies_company_id_users_user_id_patch) | **PATCH** /companies/{company_id}/users/{user_id} | Update an existing user by ID
[**me_get**](UsersApi.md#me_get) | **GET** /me | Get current authenticated user&#39;s profile.


# **companies_company_id_users_get**
> CompaniesCompanyIdUsersGet200Response companies_company_id_users_get(company_id)

Get a list of all users in a company

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.companies_company_id_users_get200_response import CompaniesCompanyIdUsersGet200Response
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
    api_instance = spartera_api_sdk.UsersApi(api_client)
    company_id = 'company_id_example' # str | 

    try:
        # Get a list of all users in a company
        api_response = api_instance.companies_company_id_users_get(company_id)
        print("The response of UsersApi->companies_company_id_users_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->companies_company_id_users_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  | 

### Return type

[**CompaniesCompanyIdUsersGet200Response**](CompaniesCompanyIdUsersGet200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved users |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_users_post**
> CompaniesCompanyIdUsersPost200Response companies_company_id_users_post(company_id, users_input)

Create a new user

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.companies_company_id_users_post200_response import CompaniesCompanyIdUsersPost200Response
from spartera_api_sdk.models.users_input import UsersInput
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
    api_instance = spartera_api_sdk.UsersApi(api_client)
    company_id = 'company_id_example' # str | 
    users_input = spartera_api_sdk.UsersInput() # UsersInput | 

    try:
        # Create a new user
        api_response = api_instance.companies_company_id_users_post(company_id, users_input)
        print("The response of UsersApi->companies_company_id_users_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->companies_company_id_users_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  | 
 **users_input** | [**UsersInput**](UsersInput.md)|  | 

### Return type

[**CompaniesCompanyIdUsersPost200Response**](CompaniesCompanyIdUsersPost200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created users |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**400** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_users_user_id_delete**
> CompaniesCompanyIdUsersUserIdDelete200Response companies_company_id_users_user_id_delete(company_id, user_id)

Delete single user by ID

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.companies_company_id_users_user_id_delete200_response import CompaniesCompanyIdUsersUserIdDelete200Response
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
    api_instance = spartera_api_sdk.UsersApi(api_client)
    company_id = 'company_id_example' # str | 
    user_id = 'user_id_example' # str | 

    try:
        # Delete single user by ID
        api_response = api_instance.companies_company_id_users_user_id_delete(company_id, user_id)
        print("The response of UsersApi->companies_company_id_users_user_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->companies_company_id_users_user_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**CompaniesCompanyIdUsersUserIdDelete200Response**](CompaniesCompanyIdUsersUserIdDelete200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully deleted users |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_users_user_id_get**
> CompaniesCompanyIdUsersUserIdGet200Response companies_company_id_users_user_id_get(company_id, user_id)

Get single user by ID

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.companies_company_id_users_user_id_get200_response import CompaniesCompanyIdUsersUserIdGet200Response
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
    api_instance = spartera_api_sdk.UsersApi(api_client)
    company_id = 'company_id_example' # str | 
    user_id = 'user_id_example' # str | 

    try:
        # Get single user by ID
        api_response = api_instance.companies_company_id_users_user_id_get(company_id, user_id)
        print("The response of UsersApi->companies_company_id_users_user_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->companies_company_id_users_user_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**CompaniesCompanyIdUsersUserIdGet200Response**](CompaniesCompanyIdUsersUserIdGet200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved users |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_users_user_id_patch**
> CompaniesCompanyIdUsersUserIdPatch200Response companies_company_id_users_user_id_patch(company_id, user_id, users_update)

Update an existing user by ID

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.companies_company_id_users_user_id_patch200_response import CompaniesCompanyIdUsersUserIdPatch200Response
from spartera_api_sdk.models.users_update import UsersUpdate
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
    api_instance = spartera_api_sdk.UsersApi(api_client)
    company_id = 'company_id_example' # str | 
    user_id = 'user_id_example' # str | 
    users_update = spartera_api_sdk.UsersUpdate() # UsersUpdate | 

    try:
        # Update an existing user by ID
        api_response = api_instance.companies_company_id_users_user_id_patch(company_id, user_id, users_update)
        print("The response of UsersApi->companies_company_id_users_user_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->companies_company_id_users_user_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  | 
 **user_id** | **str**|  | 
 **users_update** | [**UsersUpdate**](UsersUpdate.md)|  | 

### Return type

[**CompaniesCompanyIdUsersUserIdPatch200Response**](CompaniesCompanyIdUsersUserIdPatch200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated users |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**400** | Invalid input |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **me_get**
> CompaniesCompanyIdUsersGet200Response me_get()

Get current authenticated user's profile.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.companies_company_id_users_get200_response import CompaniesCompanyIdUsersGet200Response
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
    api_instance = spartera_api_sdk.UsersApi(api_client)

    try:
        # Get current authenticated user's profile.
        api_response = api_instance.me_get()
        print("The response of UsersApi->me_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->me_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CompaniesCompanyIdUsersGet200Response**](CompaniesCompanyIdUsersGet200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved users |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

