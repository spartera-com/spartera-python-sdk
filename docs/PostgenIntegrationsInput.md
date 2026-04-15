# PostgenIntegrationsInput

Input schema for creating PostgenIntegration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_id** | **str** | Company this integration belongs to | 
**user_id** | **str** | User who created this integration | 
**platform** | **str** | Platform identifier (beehiiv, wordpress, medium, etc) | 
**platform_name** | **str** | Display name of the platform | 
**credentials_secret_name** | **str** | GCP Secret Manager secret name containing encrypted credentials | 
**is_active** | **bool** | Whether this integration is currently active | [optional] 
**last_used_at** | **datetime** | Last time this integration was used for publishing | [optional] 

## Example

```python
from spartera_api_sdk.models.postgen_integrations_input import PostgenIntegrationsInput

# TODO update the JSON string below
json = "{}"
# create an instance of PostgenIntegrationsInput from a JSON string
postgen_integrations_input_instance = PostgenIntegrationsInput.from_json(json)
# print the JSON string representation of the object
print(PostgenIntegrationsInput.to_json())

# convert the object into a dict
postgen_integrations_input_dict = postgen_integrations_input_instance.to_dict()
# create an instance of PostgenIntegrationsInput from a dict
postgen_integrations_input_from_dict = PostgenIntegrationsInput.from_dict(postgen_integrations_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


