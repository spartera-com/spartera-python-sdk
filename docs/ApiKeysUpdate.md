# ApiKeysUpdate

Update schema for modifying ApiKey

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | User who owns this API key | [optional] 
**company_id** | **str** | Company this API key belongs to | [optional] 
**role_id** | **int** | Role/permission level for this API key | [optional] 
**name** | **str** | Human-readable name for this API key | [optional] 
**expiration_date_utc** | **datetime** | When this API key expires (NULL &#x3D; never expires) | [optional] 

## Example

```python
from spartera_api_sdk.models.api_keys_update import ApiKeysUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKeysUpdate from a JSON string
api_keys_update_instance = ApiKeysUpdate.from_json(json)
# print the JSON string representation of the object
print(ApiKeysUpdate.to_json())

# convert the object into a dict
api_keys_update_dict = api_keys_update_instance.to_dict()
# create an instance of ApiKeysUpdate from a dict
api_keys_update_from_dict = ApiKeysUpdate.from_dict(api_keys_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


