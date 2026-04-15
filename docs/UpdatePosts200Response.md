# UpdatePosts200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Response status message | 
**data** | [**UpdatePosts200ResponseData**](UpdatePosts200ResponseData.md) |  | 

## Example

```python
from spartera_api_sdk.models.update_posts200_response import UpdatePosts200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePosts200Response from a JSON string
update_posts200_response_instance = UpdatePosts200Response.from_json(json)
# print the JSON string representation of the object
print(UpdatePosts200Response.to_json())

# convert the object into a dict
update_posts200_response_dict = update_posts200_response_instance.to_dict()
# create an instance of UpdatePosts200Response from a dict
update_posts200_response_from_dict = UpdatePosts200Response.from_dict(update_posts200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


