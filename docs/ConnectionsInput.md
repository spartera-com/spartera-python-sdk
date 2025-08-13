# ConnectionsInput

Input schema for creating Connection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
from spartera_api_sdk.models.connections_input import ConnectionsInput

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionsInput from a JSON string
connections_input_instance = ConnectionsInput.from_json(json)
# print the JSON string representation of the object
print(ConnectionsInput.to_json())

# convert the object into a dict
connections_input_dict = connections_input_instance.to_dict()
# create an instance of ConnectionsInput from a dict
connections_input_from_dict = ConnectionsInput.from_dict(connections_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


