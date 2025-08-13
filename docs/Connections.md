# Connections

Model for every connection setup from our platform

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_created** | **datetime** |  | [optional] 
**last_updated** | **datetime** |  | [optional] 
**connection_id** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**engine_id** | **int** |  | 
**company_id** | **str** |  | 
**credential_type** | **str** | Enum type: CredentialType | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**provider_domain** | **str** |  | [optional] 
**verified_usage_ability** | **bool** |  | [optional] 

## Example

```python
from spartera_api_sdk.models.connections import Connections

# TODO update the JSON string below
json = "{}"
# create an instance of Connections from a JSON string
connections_instance = Connections.from_json(json)
# print the JSON string representation of the object
print(Connections.to_json())

# convert the object into a dict
connections_dict = connections_instance.to_dict()
# create an instance of Connections from a dict
connections_from_dict = Connections.from_dict(connections_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


