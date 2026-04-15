# ListAssetUsecases200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Response status message | 
**data** | [**List[AssetUsecases]**](AssetUsecases.md) |  | 

## Example

```python
from spartera_api_sdk.models.list_asset_usecases200_response import ListAssetUsecases200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListAssetUsecases200Response from a JSON string
list_asset_usecases200_response_instance = ListAssetUsecases200Response.from_json(json)
# print the JSON string representation of the object
print(ListAssetUsecases200Response.to_json())

# convert the object into a dict
list_asset_usecases200_response_dict = list_asset_usecases200_response_instance.to_dict()
# create an instance of ListAssetUsecases200Response from a dict
list_asset_usecases200_response_from_dict = ListAssetUsecases200Response.from_dict(list_asset_usecases200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


