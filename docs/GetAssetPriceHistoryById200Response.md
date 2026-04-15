# GetAssetPriceHistoryById200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Response status message | 
**data** | [**AssetPriceHistory**](AssetPriceHistory.md) |  | 

## Example

```python
from spartera_api_sdk.models.get_asset_price_history_by_id200_response import GetAssetPriceHistoryById200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAssetPriceHistoryById200Response from a JSON string
get_asset_price_history_by_id200_response_instance = GetAssetPriceHistoryById200Response.from_json(json)
# print the JSON string representation of the object
print(GetAssetPriceHistoryById200Response.to_json())

# convert the object into a dict
get_asset_price_history_by_id200_response_dict = get_asset_price_history_by_id200_response_instance.to_dict()
# create an instance of GetAssetPriceHistoryById200Response from a dict
get_asset_price_history_by_id200_response_from_dict = GetAssetPriceHistoryById200Response.from_dict(get_asset_price_history_by_id200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


