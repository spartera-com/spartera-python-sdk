# FavoritesUpdate

Update schema for modifying Favorite

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**company_id** | **str** |  | [optional] 
**notes** | **str** | Optional user notes about this favorite | [optional] 
**category** | **str** | Optional category for organizing favorites (e.g., &#39;Work&#39;, &#39;Research&#39;) | [optional] 
**priority** | **int** | User-defined priority for sorting (higher &#x3D; more important) | [optional] 

## Example

```python
from spartera_api_sdk.models.favorites_update import FavoritesUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of FavoritesUpdate from a JSON string
favorites_update_instance = FavoritesUpdate.from_json(json)
# print the JSON string representation of the object
print(FavoritesUpdate.to_json())

# convert the object into a dict
favorites_update_dict = favorites_update_instance.to_dict()
# create an instance of FavoritesUpdate from a dict
favorites_update_from_dict = FavoritesUpdate.from_dict(favorites_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


