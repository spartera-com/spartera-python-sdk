# ConnectionsUpdate

Update schema for modifying Connection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | [optional] 
**engine_id** | **int** |  | [optional] 
**company_id** | **str** |  | [optional] 
**credential_type** | **str** | Enum type: CredentialType | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**provider_domain** | **str** |  | [optional] 
**verified_usage_ability** | **bool** |  | [optional] 

## Example

```python
from spartera_api_sdk.models.connections_update import ConnectionsUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionsUpdate from a JSON string
connections_update_instance = ConnectionsUpdate.from_json(json)
# print the JSON string representation of the object
print(ConnectionsUpdate.to_json())

# convert the object into a dict
connections_update_dict = connections_update_instance.to_dict()
# create an instance of ConnectionsUpdate from a dict
connections_update_from_dict = ConnectionsUpdate.from_dict(connections_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


