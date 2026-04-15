# UpdatePostgenIntegrations200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Response status message | 
**data** | [**UpdatePostgenIntegrations200ResponseData**](UpdatePostgenIntegrations200ResponseData.md) |  | 

## Example

```python
from spartera_api_sdk.models.update_postgen_integrations200_response import UpdatePostgenIntegrations200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePostgenIntegrations200Response from a JSON string
update_postgen_integrations200_response_instance = UpdatePostgenIntegrations200Response.from_json(json)
# print the JSON string representation of the object
print(UpdatePostgenIntegrations200Response.to_json())

# convert the object into a dict
update_postgen_integrations200_response_dict = update_postgen_integrations200_response_instance.to_dict()
# create an instance of UpdatePostgenIntegrations200Response from a dict
update_postgen_integrations200_response_from_dict = UpdatePostgenIntegrations200Response.from_dict(update_postgen_integrations200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


