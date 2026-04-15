# DeleteAssetPriceHistory200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Response status message | 
**data** | [**DeleteAssetPriceHistory200ResponseData**](DeleteAssetPriceHistory200ResponseData.md) |  | 

## Example

```python
from spartera_api_sdk.models.delete_asset_price_history200_response import DeleteAssetPriceHistory200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteAssetPriceHistory200Response from a JSON string
delete_asset_price_history200_response_instance = DeleteAssetPriceHistory200Response.from_json(json)
# print the JSON string representation of the object
print(DeleteAssetPriceHistory200Response.to_json())

# convert the object into a dict
delete_asset_price_history200_response_dict = delete_asset_price_history200_response_instance.to_dict()
# create an instance of DeleteAssetPriceHistory200Response from a dict
delete_asset_price_history200_response_from_dict = DeleteAssetPriceHistory200Response.from_dict(delete_asset_price_history200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


