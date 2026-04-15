# UpdateAssetPriceHistory200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Response status message | 
**data** | [**UpdateAssetPriceHistory200ResponseData**](UpdateAssetPriceHistory200ResponseData.md) |  | 

## Example

```python
from spartera_api_sdk.models.update_asset_price_history200_response import UpdateAssetPriceHistory200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAssetPriceHistory200Response from a JSON string
update_asset_price_history200_response_instance = UpdateAssetPriceHistory200Response.from_json(json)
# print the JSON string representation of the object
print(UpdateAssetPriceHistory200Response.to_json())

# convert the object into a dict
update_asset_price_history200_response_dict = update_asset_price_history200_response_instance.to_dict()
# create an instance of UpdateAssetPriceHistory200Response from a dict
update_asset_price_history200_response_from_dict = UpdateAssetPriceHistory200Response.from_dict(update_asset_price_history200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


