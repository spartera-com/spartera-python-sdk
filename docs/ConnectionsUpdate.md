# ConnectionsUpdate

Update schema for modifying Connection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | References users.user_id — An individual user account within a company. See GET /users for valid values. Optional. | [optional] 
**engine_id** | **int** | References storage_engines.engine_id — Fact table of all the different storage engines we support. See GET /storage_engines for valid values. Required. | [optional] 
**company_id** | **str** | References companies.company_id — A Spartera seller or buyer company account. See GET /companies for valid values. Required. | [optional] 
**credential_type** | **str** | Optional. One of: SERVICE_ACCOUNT, USERNAME_PASSWORD, API_KEY, SERVICE_IDENTITY, ACCESS_KEY, … (8 total). | [optional] 
**name** | **str** | Optional. | [optional] 
**description** | **str** | Optional. | [optional] 
**provider_domain** | **str** | Domain of the external API provider (e.g., &#39;api.weather.com&#39;) | [optional] 
**verified_usage_ability** | **bool** | Optional. | [optional] 

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


