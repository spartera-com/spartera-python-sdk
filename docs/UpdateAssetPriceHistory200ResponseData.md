# UpdateAssetPriceHistory200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aph_id** | **str** | ID of the updated asset_price_history | 

## Example

```python
from spartera_api_sdk.models.update_asset_price_history200_response_data import UpdateAssetPriceHistory200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAssetPriceHistory200ResponseData from a JSON string
update_asset_price_history200_response_data_instance = UpdateAssetPriceHistory200ResponseData.from_json(json)
# print the JSON string representation of the object
print(UpdateAssetPriceHistory200ResponseData.to_json())

# convert the object into a dict
update_asset_price_history200_response_data_dict = update_asset_price_history200_response_data_instance.to_dict()
# create an instance of UpdateAssetPriceHistory200ResponseData from a dict
update_asset_price_history200_response_data_from_dict = UpdateAssetPriceHistory200ResponseData.from_dict(update_asset_price_history200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


