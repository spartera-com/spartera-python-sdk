# CreatePosts200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Response status message | 
**data** | [**CreatePosts200ResponseData**](CreatePosts200ResponseData.md) |  | 

## Example

```python
from spartera_api_sdk.models.create_posts200_response import CreatePosts200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePosts200Response from a JSON string
create_posts200_response_instance = CreatePosts200Response.from_json(json)
# print the JSON string representation of the object
print(CreatePosts200Response.to_json())

# convert the object into a dict
create_posts200_response_dict = create_posts200_response_instance.to_dict()
# create an instance of CreatePosts200Response from a dict
create_posts200_response_from_dict = CreatePosts200Response.from_dict(create_posts200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


