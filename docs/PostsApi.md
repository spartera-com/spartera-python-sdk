# spartera_api_sdk.PostsApi

All URIs are relative to *https://api.spartera.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_posts**](PostsApi.md#create_posts) | **POST** /companies/{company_id}/posts | POST /companies/{company_id}/posts
[**create_posts2**](PostsApi.md#create_posts2) | **POST** /companies/{company_id}/posts/{post_id}/publish/{integration_id} | Publish a post to an external platform via an integration.      Args:         post_id: ID of the post to publish         integration_id: ID of the integration to use (from postgen_integrations)      Returns:         Publication record with external_url and external_post_id
[**create_posts_publish**](PostsApi.md#create_posts_publish) | **POST** /companies/{company_id}/posts/{post_id}/publish | Publish a post (make it publicly visible).
[**create_posts_unpublish**](PostsApi.md#create_posts_unpublish) | **POST** /companies/{company_id}/posts/{post_id}/unpublish | Unpublish a post (make it private/draft again).
[**create_posts_view**](PostsApi.md#create_posts_view) | **POST** /companies/{company_id}/posts/{post_id}/view | Increment view count for a post.     Public endpoint (no authentication required).
[**delete_posts**](PostsApi.md#delete_posts) | **DELETE** /companies/{company_id}/posts/{post_id} | Delete single post by ID.
[**get_posts_by_id**](PostsApi.md#get_posts_by_id) | **GET** /companies/{company_id}/posts/{post_id} | Get single post by ID.
[**get_posts_by_id_publications**](PostsApi.md#get_posts_by_id_publications) | **GET** /companies/{company_id}/posts/{post_id}/publications | Get all publications for a post.     Shows where this post has been published to external platforms.      Returns:         Array of publication records with platform, URL, status
[**list_posts**](PostsApi.md#list_posts) | **GET** /companies/{company_id}/posts | Get a list of all posts for the user&#39;s company.     Supports filtering, sorting, pagination.
[**list_posts_summary**](PostsApi.md#list_posts_summary) | **GET** /companies/{company_id}/posts/summary | GET /companies/{company_id}/posts/summary
[**update_posts**](PostsApi.md#update_posts) | **PATCH** /companies/{company_id}/posts/{post_id} | Update an existing post by ID.      Note: last_edited_at is automatically updated.


# **create_posts**
> CreatePosts200Response create_posts(company_id, posts_input, page=page, limit=limit, sort_by=sort_by, sort_order=sort_order, search=search)

POST /companies/{company_id}/posts

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.create_posts200_response import CreatePosts200Response
from spartera_api_sdk.models.posts_input import PostsInput
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
    api_instance = spartera_api_sdk.PostsApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    posts_input = spartera_api_sdk.PostsInput() # PostsInput | 
    page = 1 # int | Page number for pagination (optional) (default to 1)
    limit = 20 # int | Number of items per page (optional) (default to 20)
    sort_by = 'sort_by_example' # str | Field to sort by (optional)
    sort_order = desc # str | Sort order (ascending or descending) (optional) (default to desc)
    search = 'search_example' # str | Search term to filter results (optional)

    try:
        # POST /companies/{company_id}/posts
        api_response = api_instance.create_posts(company_id, posts_input, page=page, limit=limit, sort_by=sort_by, sort_order=sort_order, search=search)
        print("The response of PostsApi->create_posts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostsApi->create_posts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **posts_input** | [**PostsInput**](PostsInput.md)|  | 
 **page** | **int**| Page number for pagination | [optional] [default to 1]
 **limit** | **int**| Number of items per page | [optional] [default to 20]
 **sort_by** | **str**| Field to sort by | [optional] 
 **sort_order** | **str**| Sort order (ascending or descending) | [optional] [default to desc]
 **search** | **str**| Search term to filter results | [optional] 

### Return type

[**CreatePosts200Response**](CreatePosts200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created posts |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**400** | Invalid input |  -  |
**409** | Resource conflict (duplicate, constraint violation) |  -  |
**422** | Request well-formed but semantically invalid |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_posts2**
> CreatePosts200Response create_posts2(company_id, post_id, integration_id, posts_input)

Publish a post to an external platform via an integration.      Args:         post_id: ID of the post to publish         integration_id: ID of the integration to use (from postgen_integrations)      Returns:         Publication record with external_url and external_post_id

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.create_posts200_response import CreatePosts200Response
from spartera_api_sdk.models.posts_input import PostsInput
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
    api_instance = spartera_api_sdk.PostsApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    post_id = 'post_id_example' # str | Unique identifier for the Post
    integration_id = 'integration_id_example' # str | Unique identifier for the Integration
    posts_input = spartera_api_sdk.PostsInput() # PostsInput | 

    try:
        # Publish a post to an external platform via an integration.      Args:         post_id: ID of the post to publish         integration_id: ID of the integration to use (from postgen_integrations)      Returns:         Publication record with external_url and external_post_id
        api_response = api_instance.create_posts2(company_id, post_id, integration_id, posts_input)
        print("The response of PostsApi->create_posts2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostsApi->create_posts2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **post_id** | **str**| Unique identifier for the Post | 
 **integration_id** | **str**| Unique identifier for the Integration | 
 **posts_input** | [**PostsInput**](PostsInput.md)|  | 

### Return type

[**CreatePosts200Response**](CreatePosts200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created posts |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**400** | Invalid input |  -  |
**409** | Resource conflict (duplicate, constraint violation) |  -  |
**422** | Request well-formed but semantically invalid |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_posts_publish**
> CreatePosts200Response create_posts_publish(company_id, post_id, posts_input)

Publish a post (make it publicly visible).

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.create_posts200_response import CreatePosts200Response
from spartera_api_sdk.models.posts_input import PostsInput
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
    api_instance = spartera_api_sdk.PostsApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    post_id = 'post_id_example' # str | Unique identifier for the Post
    posts_input = spartera_api_sdk.PostsInput() # PostsInput | 

    try:
        # Publish a post (make it publicly visible).
        api_response = api_instance.create_posts_publish(company_id, post_id, posts_input)
        print("The response of PostsApi->create_posts_publish:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostsApi->create_posts_publish: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **post_id** | **str**| Unique identifier for the Post | 
 **posts_input** | [**PostsInput**](PostsInput.md)|  | 

### Return type

[**CreatePosts200Response**](CreatePosts200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created posts |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**400** | Invalid input |  -  |
**409** | Resource conflict (duplicate, constraint violation) |  -  |
**422** | Request well-formed but semantically invalid |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_posts_unpublish**
> CreatePosts200Response create_posts_unpublish(company_id, post_id, posts_input)

Unpublish a post (make it private/draft again).

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.create_posts200_response import CreatePosts200Response
from spartera_api_sdk.models.posts_input import PostsInput
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
    api_instance = spartera_api_sdk.PostsApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    post_id = 'post_id_example' # str | Unique identifier for the Post
    posts_input = spartera_api_sdk.PostsInput() # PostsInput | 

    try:
        # Unpublish a post (make it private/draft again).
        api_response = api_instance.create_posts_unpublish(company_id, post_id, posts_input)
        print("The response of PostsApi->create_posts_unpublish:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostsApi->create_posts_unpublish: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **post_id** | **str**| Unique identifier for the Post | 
 **posts_input** | [**PostsInput**](PostsInput.md)|  | 

### Return type

[**CreatePosts200Response**](CreatePosts200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created posts |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**400** | Invalid input |  -  |
**409** | Resource conflict (duplicate, constraint violation) |  -  |
**422** | Request well-formed but semantically invalid |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_posts_view**
> CreatePosts200Response create_posts_view(company_id, post_id, posts_input)

Increment view count for a post.     Public endpoint (no authentication required).

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.create_posts200_response import CreatePosts200Response
from spartera_api_sdk.models.posts_input import PostsInput
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
    api_instance = spartera_api_sdk.PostsApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    post_id = 'post_id_example' # str | Unique identifier for the Post
    posts_input = spartera_api_sdk.PostsInput() # PostsInput | 

    try:
        # Increment view count for a post.     Public endpoint (no authentication required).
        api_response = api_instance.create_posts_view(company_id, post_id, posts_input)
        print("The response of PostsApi->create_posts_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostsApi->create_posts_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **post_id** | **str**| Unique identifier for the Post | 
 **posts_input** | [**PostsInput**](PostsInput.md)|  | 

### Return type

[**CreatePosts200Response**](CreatePosts200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created posts |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**400** | Invalid input |  -  |
**409** | Resource conflict (duplicate, constraint violation) |  -  |
**422** | Request well-formed but semantically invalid |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_posts**
> DeletePosts200Response delete_posts(company_id, post_id)

Delete single post by ID.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.delete_posts200_response import DeletePosts200Response
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
    api_instance = spartera_api_sdk.PostsApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    post_id = 'post_id_example' # str | Unique identifier for the Post

    try:
        # Delete single post by ID.
        api_response = api_instance.delete_posts(company_id, post_id)
        print("The response of PostsApi->delete_posts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostsApi->delete_posts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **post_id** | **str**| Unique identifier for the Post | 

### Return type

[**DeletePosts200Response**](DeletePosts200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully deleted posts |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_posts_by_id**
> GetPostsById200Response get_posts_by_id(company_id, post_id)

Get single post by ID.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.get_posts_by_id200_response import GetPostsById200Response
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
    api_instance = spartera_api_sdk.PostsApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    post_id = 'post_id_example' # str | Unique identifier for the Post

    try:
        # Get single post by ID.
        api_response = api_instance.get_posts_by_id(company_id, post_id)
        print("The response of PostsApi->get_posts_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostsApi->get_posts_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **post_id** | **str**| Unique identifier for the Post | 

### Return type

[**GetPostsById200Response**](GetPostsById200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved posts |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_posts_by_id_publications**
> GetPostsById200Response get_posts_by_id_publications(company_id, post_id)

Get all publications for a post.     Shows where this post has been published to external platforms.      Returns:         Array of publication records with platform, URL, status

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.get_posts_by_id200_response import GetPostsById200Response
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
    api_instance = spartera_api_sdk.PostsApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    post_id = 'post_id_example' # str | Unique identifier for the Post

    try:
        # Get all publications for a post.     Shows where this post has been published to external platforms.      Returns:         Array of publication records with platform, URL, status
        api_response = api_instance.get_posts_by_id_publications(company_id, post_id)
        print("The response of PostsApi->get_posts_by_id_publications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostsApi->get_posts_by_id_publications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **post_id** | **str**| Unique identifier for the Post | 

### Return type

[**GetPostsById200Response**](GetPostsById200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved posts |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_posts**
> ListPosts200Response list_posts(company_id, page=page, limit=limit, sort_by=sort_by, sort_order=sort_order, search=search)

Get a list of all posts for the user's company.     Supports filtering, sorting, pagination.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.list_posts200_response import ListPosts200Response
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
    api_instance = spartera_api_sdk.PostsApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    page = 1 # int | Page number for pagination (optional) (default to 1)
    limit = 20 # int | Number of items per page (optional) (default to 20)
    sort_by = 'sort_by_example' # str | Field to sort by (optional)
    sort_order = desc # str | Sort order (ascending or descending) (optional) (default to desc)
    search = 'search_example' # str | Search term to filter results (optional)

    try:
        # Get a list of all posts for the user's company.     Supports filtering, sorting, pagination.
        api_response = api_instance.list_posts(company_id, page=page, limit=limit, sort_by=sort_by, sort_order=sort_order, search=search)
        print("The response of PostsApi->list_posts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostsApi->list_posts: %s\n" % e)
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

[**ListPosts200Response**](ListPosts200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved posts |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_posts_summary**
> ListPosts200Response list_posts_summary(company_id, page=page, limit=limit, sort_by=sort_by, sort_order=sort_order, search=search)

GET /companies/{company_id}/posts/summary

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.list_posts200_response import ListPosts200Response
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
    api_instance = spartera_api_sdk.PostsApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    page = 1 # int | Page number for pagination (optional) (default to 1)
    limit = 20 # int | Number of items per page (optional) (default to 20)
    sort_by = 'sort_by_example' # str | Field to sort by (optional)
    sort_order = desc # str | Sort order (ascending or descending) (optional) (default to desc)
    search = 'search_example' # str | Search term to filter results (optional)

    try:
        # GET /companies/{company_id}/posts/summary
        api_response = api_instance.list_posts_summary(company_id, page=page, limit=limit, sort_by=sort_by, sort_order=sort_order, search=search)
        print("The response of PostsApi->list_posts_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostsApi->list_posts_summary: %s\n" % e)
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

[**ListPosts200Response**](ListPosts200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved posts |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_posts**
> UpdatePosts200Response update_posts(company_id, post_id, posts_update)

Update an existing post by ID.      Note: last_edited_at is automatically updated.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import spartera_api_sdk
from spartera_api_sdk.models.posts_update import PostsUpdate
from spartera_api_sdk.models.update_posts200_response import UpdatePosts200Response
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
    api_instance = spartera_api_sdk.PostsApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier for the Company
    post_id = 'post_id_example' # str | Unique identifier for the Post
    posts_update = spartera_api_sdk.PostsUpdate() # PostsUpdate | 

    try:
        # Update an existing post by ID.      Note: last_edited_at is automatically updated.
        api_response = api_instance.update_posts(company_id, post_id, posts_update)
        print("The response of PostsApi->update_posts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostsApi->update_posts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier for the Company | 
 **post_id** | **str**| Unique identifier for the Post | 
 **posts_update** | [**PostsUpdate**](PostsUpdate.md)|  | 

### Return type

[**UpdatePosts200Response**](UpdatePosts200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated posts |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**400** | Invalid input |  -  |
**409** | Resource conflict (duplicate, constraint violation) |  -  |
**422** | Request well-formed but semantically invalid |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

