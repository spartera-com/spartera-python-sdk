# ApiKeys

API Keys model storing every key created with SOC2 compliance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_created** | **datetime** |  | [optional] 
**last_updated** | **datetime** |  | [optional] 
**api_key_id** | **int** |  | 
**user_id** | **str** | User who owns this API key | [optional] 
**company_id** | **str** | Company this API key belongs to | 
**role_id** | **int** | Role/permission level for this API key | 
**name** | **str** | Human-readable name for this API key | [optional] 
**expiration_date_utc** | **datetime** | When this API key expires (NULL &#x3D; never expires) | [optional] 

## Example

```python
from spartera_api_sdk.models.api_keys import ApiKeys

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKeys from a JSON string
api_keys_instance = ApiKeys.from_json(json)
# print the JSON string representation of the object
print(ApiKeys.to_json())

# convert the object into a dict
api_keys_dict = api_keys_instance.to_dict()
# create an instance of ApiKeys from a dict
api_keys_from_dict = ApiKeys.from_dict(api_keys_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


