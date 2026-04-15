# DeleteFavorites200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**favorite_id** | **str** | ID of the deleted favorites | 

## Example

```python
from spartera_api_sdk.models.delete_favorites200_response_data import DeleteFavorites200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteFavorites200ResponseData from a JSON string
delete_favorites200_response_data_instance = DeleteFavorites200ResponseData.from_json(json)
# print the JSON string representation of the object
print(DeleteFavorites200ResponseData.to_json())

# convert the object into a dict
delete_favorites200_response_data_dict = delete_favorites200_response_data_instance.to_dict()
# create an instance of DeleteFavorites200ResponseData from a dict
delete_favorites200_response_data_from_dict = DeleteFavorites200ResponseData.from_dict(delete_favorites200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


