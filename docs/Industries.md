# Industries

Available industry categories for asset classification. Based on US NAISC codes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_created** | **datetime** | Optional. | [optional] 
**last_updated** | **datetime** | Optional. | [optional] 
**industry_id** | **int** | Auto-generated unique identifier. | [optional] 
**industry_name** | **str** | Required. Must be unique. | 
**short_name** | **str** | Required. | 
**slug** | **str** | Optional. | [optional] 
**naisc_code** | **int** | Optional. | [optional] 
**description** | **str** | Optional. | [optional] 

## Example

```python
from spartera_api_sdk.models.industries import Industries

# TODO update the JSON string below
json = "{}"
# create an instance of Industries from a JSON string
industries_instance = Industries.from_json(json)
# print the JSON string representation of the object
print(Industries.to_json())

# convert the object into a dict
industries_dict = industries_instance.to_dict()
# create an instance of Industries from a dict
industries_from_dict = Industries.from_dict(industries_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


