# DeletePosts200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Response status message | 
**data** | [**DeletePosts200ResponseData**](DeletePosts200ResponseData.md) |  | 

## Example

```python
from spartera_api_sdk.models.delete_posts200_response import DeletePosts200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeletePosts200Response from a JSON string
delete_posts200_response_instance = DeletePosts200Response.from_json(json)
# print the JSON string representation of the object
print(DeletePosts200Response.to_json())

# convert the object into a dict
delete_posts200_response_dict = delete_posts200_response_instance.to_dict()
# create an instance of DeletePosts200Response from a dict
delete_posts200_response_from_dict = DeletePosts200Response.from_dict(delete_posts200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


