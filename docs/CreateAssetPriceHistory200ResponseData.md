# CreateAssetPriceHistory200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aph_id** | **str** | ID of the created asset_price_history | 

## Example

```python
from spartera_api_sdk.models.create_asset_price_history200_response_data import CreateAssetPriceHistory200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAssetPriceHistory200ResponseData from a JSON string
create_asset_price_history200_response_data_instance = CreateAssetPriceHistory200ResponseData.from_json(json)
# print the JSON string representation of the object
print(CreateAssetPriceHistory200ResponseData.to_json())

# convert the object into a dict
create_asset_price_history200_response_data_dict = create_asset_price_history200_response_data_instance.to_dict()
# create an instance of CreateAssetPriceHistory200ResponseData from a dict
create_asset_price_history200_response_data_from_dict = CreateAssetPriceHistory200ResponseData.from_dict(create_asset_price_history200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


