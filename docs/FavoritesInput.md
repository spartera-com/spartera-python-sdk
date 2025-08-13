# FavoritesInput

Input schema for creating Favorite

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **str** |  | 
**user_id** | **str** |  | [optional] 
**company_id** | **str** |  | 
**notes** | **str** | Optional user notes about this favorite | [optional] 
**category** | **str** | Optional category for organizing favorites (e.g., &#39;Work&#39;, &#39;Research&#39;) | [optional] 
**priority** | **int** | User-defined priority for sorting (higher &#x3D; more important) | [optional] 

## Example

```python
from spartera_api_sdk.models.favorites_input import FavoritesInput

# TODO update the JSON string below
json = "{}"
# create an instance of FavoritesInput from a JSON string
favorites_input_instance = FavoritesInput.from_json(json)
# print the JSON string representation of the object
print(FavoritesInput.to_json())

# convert the object into a dict
favorites_input_dict = favorites_input_instance.to_dict()
# create an instance of FavoritesInput from a dict
favorites_input_from_dict = FavoritesInput.from_dict(favorites_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


