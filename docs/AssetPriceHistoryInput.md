# AssetPriceHistoryInput

Input schema for creating AssetPriceHistory

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **str** | FK to assets. NULL when this record belongs to an endpoint. | [optional] 
**endpoint_id** | **str** | FK to endpoints. NULL when this record belongs to an asset. | [optional] 
**price_usd** | **float** | Optional. | [optional] 
**date_ended** | **datetime** | SCD Type 2 — when this price record was superseded | [optional] 

## Example

```python
from spartera_api_sdk.models.asset_price_history_input import AssetPriceHistoryInput

# TODO update the JSON string below
json = "{}"
# create an instance of AssetPriceHistoryInput from a JSON string
asset_price_history_input_instance = AssetPriceHistoryInput.from_json(json)
# print the JSON string representation of the object
print(AssetPriceHistoryInput.to_json())

# convert the object into a dict
asset_price_history_input_dict = asset_price_history_input_instance.to_dict()
# create an instance of AssetPriceHistoryInput from a dict
asset_price_history_input_from_dict = AssetPriceHistoryInput.from_dict(asset_price_history_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


