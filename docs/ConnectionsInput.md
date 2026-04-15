# ConnectionsInput

Input schema for creating Connection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | References users.user_id — An individual user account within a company. See GET /users for valid values. Optional. | [optional] 
**engine_id** | **int** | References storage_engines.engine_id — Fact table of all the different storage engines we support. See GET /storage_engines for valid values. Required. | 
**company_id** | **str** | References companies.company_id — A Spartera seller or buyer company account. See GET /companies for valid values. Required. | 
**credential_type** | **str** | Optional. One of: SERVICE_ACCOUNT, USERNAME_PASSWORD, API_KEY, SERVICE_IDENTITY, ACCESS_KEY, … (8 total). | [optional] 
**name** | **str** | Optional. | [optional] 
**description** | **str** | Optional. | [optional] 
**provider_domain** | **str** | Domain of the external API provider (e.g., &#39;api.weather.com&#39;) | [optional] 
**verified_usage_ability** | **bool** | Optional. | [optional] 

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


