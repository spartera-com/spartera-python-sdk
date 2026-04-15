# AssetUsecases

Mapping of primary use cases for analytics assets, derived from clustering analysis

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_created** | **datetime** | Optional. | [optional] 
**last_updated** | **datetime** | Optional. | [optional] 
**auc_id** | **int** | Unique identifier. | [optional] 
**auc_name** | **str** | Required. Must be unique. | 
**slug** | **str** | URL-friendly slug derived from auc_name (e.g. &#39;competitive-benchmarking&#39;) | [optional] 
**auc_description** | **str** | Optional. | [optional] 

## Example

```python
from spartera_api_sdk.models.asset_usecases import AssetUsecases

# TODO update the JSON string below
json = "{}"
# create an instance of AssetUsecases from a JSON string
asset_usecases_instance = AssetUsecases.from_json(json)
# print the JSON string representation of the object
print(AssetUsecases.to_json())

# convert the object into a dict
asset_usecases_dict = asset_usecases_instance.to_dict()
# create an instance of AssetUsecases from a dict
asset_usecases_from_dict = AssetUsecases.from_dict(asset_usecases_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


