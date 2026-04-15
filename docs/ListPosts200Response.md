# ListPosts200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Response status message | 
**data** | [**List[Posts]**](Posts.md) |  | 

## Example

```python
from spartera_api_sdk.models.list_posts200_response import ListPosts200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListPosts200Response from a JSON string
list_posts200_response_instance = ListPosts200Response.from_json(json)
# print the JSON string representation of the object
print(ListPosts200Response.to_json())

# convert the object into a dict
list_posts200_response_dict = list_posts200_response_instance.to_dict()
# create an instance of ListPosts200Response from a dict
list_posts200_response_from_dict = ListPosts200Response.from_dict(list_posts200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


