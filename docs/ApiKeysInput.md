# ApiKeysInput

Input schema for creating ApiKey

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | User who owns this API key | [optional] 
**company_id** | **str** | Company this API key belongs to | 
**role_id** | **int** | Role/permission level for this API key | 
**name** | **str** | Human-readable name for this API key | [optional] 
**expiration_date_utc** | **datetime** | When this API key expires (NULL &#x3D; never expires) | [optional] 

## Example

```python
from spartera_api_sdk.models.api_keys_input import ApiKeysInput

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKeysInput from a JSON string
api_keys_input_instance = ApiKeysInput.from_json(json)
# print the JSON string representation of the object
print(ApiKeysInput.to_json())

# convert the object into a dict
api_keys_input_dict = api_keys_input_instance.to_dict()
# create an instance of ApiKeysInput from a dict
api_keys_input_from_dict = ApiKeysInput.from_dict(api_keys_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


