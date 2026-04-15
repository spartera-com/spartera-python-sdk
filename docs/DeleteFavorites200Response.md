# DeleteFavorites200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Response status message | 
**data** | [**DeleteFavorites200ResponseData**](DeleteFavorites200ResponseData.md) |  | 

## Example

```python
from spartera_api_sdk.models.delete_favorites200_response import DeleteFavorites200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteFavorites200Response from a JSON string
delete_favorites200_response_instance = DeleteFavorites200Response.from_json(json)
# print the JSON string representation of the object
print(DeleteFavorites200Response.to_json())

# convert the object into a dict
delete_favorites200_response_dict = delete_favorites200_response_instance.to_dict()
# create an instance of DeleteFavorites200Response from a dict
delete_favorites200_response_from_dict = DeleteFavorites200Response.from_dict(delete_favorites200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


