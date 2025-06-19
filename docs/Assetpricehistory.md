# Assetpricehistory

Pricing history for an asset

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aph_id** | **str** |  | [optional] 
**asset_id** | **str** |  | 
**price_usd** | **float** |  | [optional] 
**price_credits** | **str** |  | [optional] 
**discount_percentage** | **float** |  | [optional] 
**sale_start_date** | **str** |  | [optional] 
**sale_end_date** | **str** |  | [optional] 
**date_ended** | **str** |  | [optional] 
**date_created** | **str** |  | [optional] [readonly] 
**last_updated** | **str** |  | [optional] [readonly] 
**active** | **str** |  | 

## Example

```python
from spartera_api_sdk.models.assetpricehistory import Assetpricehistory

# TODO update the JSON string below
json = "{}"
# create an instance of Assetpricehistory from a JSON string
assetpricehistory_instance = Assetpricehistory.from_json(json)
# print the JSON string representation of the object
print(Assetpricehistory.to_json())

# convert the object into a dict
assetpricehistory_dict = assetpricehistory_instance.to_dict()
# create an instance of Assetpricehistory from a dict
assetpricehistory_from_dict = Assetpricehistory.from_dict(assetpricehistory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


