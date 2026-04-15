# CreatePosts200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**post_id** | **str** | ID of the created posts | 

## Example

```python
from spartera_api_sdk.models.create_posts200_response_data import CreatePosts200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePosts200ResponseData from a JSON string
create_posts200_response_data_instance = CreatePosts200ResponseData.from_json(json)
# print the JSON string representation of the object
print(CreatePosts200ResponseData.to_json())

# convert the object into a dict
create_posts200_response_data_dict = create_posts200_response_data_instance.to_dict()
# create an instance of CreatePosts200ResponseData from a dict
create_posts200_response_data_from_dict = CreatePosts200ResponseData.from_dict(create_posts200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


