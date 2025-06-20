# MeGet200ResponseApiKeyInfo

API key information (only for API key authentication)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key_id** | **str** | API key ID | [optional] 
**api_key_name** | **str** | API key name | [optional] 

## Example

```python
from spartera_api_sdk.models.me_get200_response_api_key_info import MeGet200ResponseApiKeyInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MeGet200ResponseApiKeyInfo from a JSON string
me_get200_response_api_key_info_instance = MeGet200ResponseApiKeyInfo.from_json(json)
# print the JSON string representation of the object
print(MeGet200ResponseApiKeyInfo.to_json())

# convert the object into a dict
me_get200_response_api_key_info_dict = me_get200_response_api_key_info_instance.to_dict()
# create an instance of MeGet200ResponseApiKeyInfo from a dict
me_get200_response_api_key_info_from_dict = MeGet200ResponseApiKeyInfo.from_dict(me_get200_response_api_key_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


