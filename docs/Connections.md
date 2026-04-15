# Connections

Secure connections from Spartera to your databases and data warehouses

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_created** | **datetime** | Optional. | [optional] 
**last_updated** | **datetime** | Optional. | [optional] 
**connection_id** | **str** | Unique identifier. | [optional] 
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


