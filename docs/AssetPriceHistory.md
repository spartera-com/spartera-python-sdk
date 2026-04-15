# AssetPriceHistory

Per-execution pricing history for a marketplace asset

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_created** | **datetime** | Optional. | [optional] 
**last_updated** | **datetime** | Optional. | [optional] 
**aph_id** | **str** | Unique identifier. | [optional] 
**asset_id** | **str** | FK to assets. NULL when this record belongs to an endpoint. | [optional] 
**endpoint_id** | **str** | FK to endpoints. NULL when this record belongs to an asset. | [optional] 
**price_usd** | **float** | Optional. | [optional] 
**date_ended** | **datetime** | SCD Type 2 — when this price record was superseded | [optional] 

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


