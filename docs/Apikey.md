# Apikey

API Keys model storing every key created

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key_id** | **str** |  | [readonly] 
**user_id** | **str** |  | [optional] 
**company_id** | **str** |  | 
**role_id** | **str** |  | 
**token** | **str** |  | 
**name** | **str** |  | [optional] 
**expiration_date_utc** | **str** |  | [optional] 
**date_created** | **str** |  | [optional] 
**last_updated** | **str** |  | [optional] 
**active** | **str** |  | [optional] 

## Example

```python
from spartera_api_sdk.models.apikey import Apikey

# TODO update the JSON string below
json = "{}"
# create an instance of Apikey from a JSON string
apikey_instance = Apikey.from_json(json)
# print the JSON string representation of the object
print(Apikey.to_json())

# convert the object into a dict
apikey_dict = apikey_instance.to_dict()
# create an instance of Apikey from a dict
apikey_from_dict = Apikey.from_dict(apikey_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


