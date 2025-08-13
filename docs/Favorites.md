# Favorites

User favorites for marketplace assets

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_created** | **datetime** |  | [optional] 
**last_updated** | **datetime** |  | [optional] 
**favorite_id** | **int** |  | [optional] 
**asset_id** | **str** |  | 
**user_id** | **str** |  | [optional] 
**company_id** | **str** |  | 
**notes** | **str** | Optional user notes about this favorite | [optional] 
**category** | **str** | Optional category for organizing favorites (e.g., &#39;Work&#39;, &#39;Research&#39;) | [optional] 
**priority** | **int** | User-defined priority for sorting (higher &#x3D; more important) | 

## Example

```python
from spartera_api_sdk.models.favorites import Favorites

# TODO update the JSON string below
json = "{}"
# create an instance of Favorites from a JSON string
favorites_instance = Favorites.from_json(json)
# print the JSON string representation of the object
print(Favorites.to_json())

# convert the object into a dict
favorites_dict = favorites_instance.to_dict()
# create an instance of Favorites from a dict
favorites_from_dict = Favorites.from_dict(favorites_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


