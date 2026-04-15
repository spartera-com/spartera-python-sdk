# PostgenIntegrationsUpdate

Update schema for modifying PostgenIntegration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_id** | **str** | Company this integration belongs to | [optional] 
**user_id** | **str** | User who created this integration | [optional] 
**platform** | **str** | Platform identifier (beehiiv, wordpress, medium, etc) | [optional] 
**platform_name** | **str** | Display name of the platform | [optional] 
**credentials_secret_name** | **str** | GCP Secret Manager secret name containing encrypted credentials | [optional] 
**is_active** | **bool** | Whether this integration is currently active | [optional] 
**last_used_at** | **datetime** | Last time this integration was used for publishing | [optional] 

## Example

```python
from spartera_api_sdk.models.postgen_integrations_update import PostgenIntegrationsUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of PostgenIntegrationsUpdate from a JSON string
postgen_integrations_update_instance = PostgenIntegrationsUpdate.from_json(json)
# print the JSON string representation of the object
print(PostgenIntegrationsUpdate.to_json())

# convert the object into a dict
postgen_integrations_update_dict = postgen_integrations_update_instance.to_dict()
# create an instance of PostgenIntegrationsUpdate from a dict
postgen_integrations_update_from_dict = PostgenIntegrationsUpdate.from_dict(postgen_integrations_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


