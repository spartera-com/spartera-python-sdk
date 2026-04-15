# GetAssetUsecasesById200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Response status message | 
**data** | [**AssetUsecases**](AssetUsecases.md) |  | 

## Example

```python
from spartera_api_sdk.models.get_asset_usecases_by_id200_response import GetAssetUsecasesById200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAssetUsecasesById200Response from a JSON string
get_asset_usecases_by_id200_response_instance = GetAssetUsecasesById200Response.from_json(json)
# print the JSON string representation of the object
print(GetAssetUsecasesById200Response.to_json())

# convert the object into a dict
get_asset_usecases_by_id200_response_dict = get_asset_usecases_by_id200_response_instance.to_dict()
# create an instance of GetAssetUsecasesById200Response from a dict
get_asset_usecases_by_id200_response_from_dict = GetAssetUsecasesById200Response.from_dict(get_asset_usecases_by_id200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


