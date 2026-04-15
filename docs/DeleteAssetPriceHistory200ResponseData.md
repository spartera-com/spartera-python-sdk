# DeleteAssetPriceHistory200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aph_id** | **str** | ID of the deleted asset_price_history | 

## Example

```python
from spartera_api_sdk.models.delete_asset_price_history200_response_data import DeleteAssetPriceHistory200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteAssetPriceHistory200ResponseData from a JSON string
delete_asset_price_history200_response_data_instance = DeleteAssetPriceHistory200ResponseData.from_json(json)
# print the JSON string representation of the object
print(DeleteAssetPriceHistory200ResponseData.to_json())

# convert the object into a dict
delete_asset_price_history200_response_data_dict = delete_asset_price_history200_response_data_instance.to_dict()
# create an instance of DeleteAssetPriceHistory200ResponseData from a dict
delete_asset_price_history200_response_data_from_dict = DeleteAssetPriceHistory200ResponseData.from_dict(delete_asset_price_history200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


