# PostgenIntegrations

An external publishing platform integration for PostGen

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_created** | **datetime** | Optional. | [optional] 
**last_updated** | **datetime** | Optional. | [optional] 
**integration_id** | **str** | Unique identifier. | [optional] 
**company_id** | **str** | Company this integration belongs to | 
**user_id** | **str** | User who created this integration | 
**platform** | **str** | Platform identifier (beehiiv, wordpress, medium, etc) | 
**platform_name** | **str** | Display name of the platform | 
**credentials_secret_name** | **str** | GCP Secret Manager secret name containing encrypted credentials | 
**is_active** | **bool** | Whether this integration is currently active | 
**last_used_at** | **datetime** | Last time this integration was used for publishing | [optional] 

## Example

```python
from spartera_api_sdk.models.postgen_integrations import PostgenIntegrations

# TODO update the JSON string below
json = "{}"
# create an instance of PostgenIntegrations from a JSON string
postgen_integrations_instance = PostgenIntegrations.from_json(json)
# print the JSON string representation of the object
print(PostgenIntegrations.to_json())

# convert the object into a dict
postgen_integrations_dict = postgen_integrations_instance.to_dict()
# create an instance of PostgenIntegrations from a dict
postgen_integrations_from_dict = PostgenIntegrations.from_dict(postgen_integrations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


