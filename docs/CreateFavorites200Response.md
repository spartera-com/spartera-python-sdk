# CreateFavorites200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Response status message | 
**data** | [**CreateFavorites200ResponseData**](CreateFavorites200ResponseData.md) |  | 

## Example

```python
from spartera_api_sdk.models.create_favorites200_response import CreateFavorites200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFavorites200Response from a JSON string
create_favorites200_response_instance = CreateFavorites200Response.from_json(json)
# print the JSON string representation of the object
print(CreateFavorites200Response.to_json())

# convert the object into a dict
create_favorites200_response_dict = create_favorites200_response_instance.to_dict()
# create an instance of CreateFavorites200Response from a dict
create_favorites200_response_from_dict = CreateFavorites200Response.from_dict(create_favorites200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


