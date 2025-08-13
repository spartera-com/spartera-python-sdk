# AssetPriceHistoryUpdate

Update schema for modifying AssetPriceHistory

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **str** |  | [optional] 
**price_usd** | **float** |  | [optional] 
**date_ended** | **datetime** | When did the price end (Datetime) | [optional] 

## Example

```python
from spartera_api_sdk.models.asset_price_history_update import AssetPriceHistoryUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of AssetPriceHistoryUpdate from a JSON string
asset_price_history_update_instance = AssetPriceHistoryUpdate.from_json(json)
# print the JSON string representation of the object
print(AssetPriceHistoryUpdate.to_json())

# convert the object into a dict
asset_price_history_update_dict = asset_price_history_update_instance.to_dict()
# create an instance of AssetPriceHistoryUpdate from a dict
asset_price_history_update_from_dict = AssetPriceHistoryUpdate.from_dict(asset_price_history_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


