# UpdateFavorites200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Response status message | 
**data** | [**UpdateFavorites200ResponseData**](UpdateFavorites200ResponseData.md) |  | 

## Example

```python
from spartera_api_sdk.models.update_favorites200_response import UpdateFavorites200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateFavorites200Response from a JSON string
update_favorites200_response_instance = UpdateFavorites200Response.from_json(json)
# print the JSON string representation of the object
print(UpdateFavorites200Response.to_json())

# convert the object into a dict
update_favorites200_response_dict = update_favorites200_response_instance.to_dict()
# create an instance of UpdateFavorites200Response from a dict
update_favorites200_response_from_dict = UpdateFavorites200Response.from_dict(update_favorites200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


