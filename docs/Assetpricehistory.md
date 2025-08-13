# AssetPriceHistory

Pricing history for an asset

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_created** | **datetime** |  | [optional] 
**last_updated** | **datetime** |  | [optional] 
**aph_id** | **str** |  | [optional] 
**asset_id** | **str** |  | 
**price_usd** | **float** |  | [optional] 
**date_ended** | **datetime** | When did the price end (Datetime) | [optional] 

## Example

```python
from spartera_api_sdk.models.asset_price_history import AssetPriceHistory

# TODO update the JSON string below
json = "{}"
# create an instance of AssetPriceHistory from a JSON string
asset_price_history_instance = AssetPriceHistory.from_json(json)
# print the JSON string representation of the object
print(AssetPriceHistory.to_json())

# convert the object into a dict
asset_price_history_dict = asset_price_history_instance.to_dict()
# create an instance of AssetPriceHistory from a dict
asset_price_history_from_dict = AssetPriceHistory.from_dict(asset_price_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


