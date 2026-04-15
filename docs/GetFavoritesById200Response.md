# GetFavoritesById200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Response status message | 
**data** | [**Favorites**](Favorites.md) |  | 

## Example

```python
from spartera_api_sdk.models.get_favorites_by_id200_response import GetFavoritesById200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetFavoritesById200Response from a JSON string
get_favorites_by_id200_response_instance = GetFavoritesById200Response.from_json(json)
# print the JSON string representation of the object
print(GetFavoritesById200Response.to_json())

# convert the object into a dict
get_favorites_by_id200_response_dict = get_favorites_by_id200_response_instance.to_dict()
# create an instance of GetFavoritesById200Response from a dict
get_favorites_by_id200_response_from_dict = GetFavoritesById200Response.from_dict(get_favorites_by_id200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


