# CreateFavorites200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**favorite_id** | **str** | ID of the created favorites | 

## Example

```python
from spartera_api_sdk.models.create_favorites200_response_data import CreateFavorites200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFavorites200ResponseData from a JSON string
create_favorites200_response_data_instance = CreateFavorites200ResponseData.from_json(json)
# print the JSON string representation of the object
print(CreateFavorites200ResponseData.to_json())

# convert the object into a dict
create_favorites200_response_data_dict = create_favorites200_response_data_instance.to_dict()
# create an instance of CreateFavorites200ResponseData from a dict
create_favorites200_response_data_from_dict = CreateFavorites200ResponseData.from_dict(create_favorites200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


