# Connection

Model for every connection setup from our platform

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_id** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**engine_id** | **str** |  | 
**company_id** | **str** |  | 
**credential_type** | **str** |  | [optional] 
**api_provider** | **str** |  | [optional] 
**api_endpoint** | **str** |  | [optional] 
**api_key_location** | **str** |  | [optional] 
**api_key_param** | **str** |  | [optional] 
**api_key_value** | **str** |  | [optional] 
**visibility** | **str** |  | 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**gcp_secret_id** | **str** |  | [optional] 
**provider_domain** | **str** |  | [optional] 
**verified_usage_ability** | **str** |  | [optional] 
**date_created** | **str** |  | [optional] 
**last_updated** | **str** |  | [optional] 
**active** | **str** |  | [optional] 

## Example

```python
from spartera_api_sdk.models.connection import Connection

# TODO update the JSON string below
json = "{}"
# create an instance of Connection from a JSON string
connection_instance = Connection.from_json(json)
# print the JSON string representation of the object
print(Connection.to_json())

# convert the object into a dict
connection_dict = connection_instance.to_dict()
# create an instance of Connection from a dict
connection_from_dict = Connection.from_dict(connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


