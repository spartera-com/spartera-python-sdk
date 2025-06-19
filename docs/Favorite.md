# Favorite

User favorites for marketplace assets

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**favorite_id** | **str** |  | [optional] [readonly] 
**asset_id** | **str** |  | 
**user_id** | **str** |  | [optional] 
**company_id** | **str** |  | 
**notes** | **str** |  | [optional] 
**category** | **str** |  | [optional] 
**priority** | **str** |  | 
**date_created** | **str** |  | [optional] [readonly] 
**last_updated** | **str** |  | [optional] [readonly] 
**active** | **str** |  | [optional] 

## Example

```python
from spartera_api_sdk.models.favorite import Favorite

# TODO update the JSON string below
json = "{}"
# create an instance of Favorite from a JSON string
favorite_instance = Favorite.from_json(json)
# print the JSON string representation of the object
print(Favorite.to_json())

# convert the object into a dict
favorite_dict = favorite_instance.to_dict()
# create an instance of Favorite from a dict
favorite_from_dict = Favorite.from_dict(favorite_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


