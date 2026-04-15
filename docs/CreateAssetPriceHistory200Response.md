# CreateAssetPriceHistory200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Response status message | 
**data** | [**CreateAssetPriceHistory200ResponseData**](CreateAssetPriceHistory200ResponseData.md) |  | 

## Example

```python
from spartera_api_sdk.models.create_asset_price_history200_response import CreateAssetPriceHistory200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAssetPriceHistory200Response from a JSON string
create_asset_price_history200_response_instance = CreateAssetPriceHistory200Response.from_json(json)
# print the JSON string representation of the object
print(CreateAssetPriceHistory200Response.to_json())

# convert the object into a dict
create_asset_price_history200_response_dict = create_asset_price_history200_response_instance.to_dict()
# create an instance of CreateAssetPriceHistory200Response from a dict
create_asset_price_history200_response_from_dict = CreateAssetPriceHistory200Response.from_dict(create_asset_price_history200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


