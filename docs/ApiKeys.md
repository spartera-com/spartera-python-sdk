# ApiKeys

API keys for authenticating requests to the Spartera platform

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_created** | **datetime** | Optional. | [optional] 
**last_updated** | **datetime** | Optional. | [optional] 
**api_key_id** | **int** | Unique identifier. | 
**user_id** | **str** | User who owns this API key | [optional] 
**company_id** | **str** | Company this API key belongs to | 
**role_id** | **int** | Role/permission level for this API key | 
**key_type** | **str** | Type of API key (analytics, mcp, or endpoint) | 
**is_system_generated** | **bool** | True if key was auto-generated for MCP deployment | 
**mcp_deployment_id** | **str** | MCP deployment this key is tied to (NULL for analytics/endpoint keys) | [optional] 
**endpoint_id** | **str** | Endpoint this key is tied to (NULL for analytics/mcp keys) | [optional] 
**name** | **str** | Human-readable name for this API key | [optional] 
**expiration_date_utc** | **datetime** | When this API key expires (NULL &#x3D; never expires) | [optional] 

## Example

```python
from spartera_api_sdk.models.api_keys import ApiKeys

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKeys from a JSON string
api_keys_instance = ApiKeys.from_json(json)
# print the JSON string representation of the object
print(ApiKeys.to_json())

# convert the object into a dict
api_keys_dict = api_keys_instance.to_dict()
# create an instance of ApiKeys from a dict
api_keys_from_dict = ApiKeys.from_dict(api_keys_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


