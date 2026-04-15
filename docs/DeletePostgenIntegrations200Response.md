# DeletePostgenIntegrations200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Response status message | 
**data** | [**DeletePostgenIntegrations200ResponseData**](DeletePostgenIntegrations200ResponseData.md) |  | 

## Example

```python
from spartera_api_sdk.models.delete_postgen_integrations200_response import DeletePostgenIntegrations200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeletePostgenIntegrations200Response from a JSON string
delete_postgen_integrations200_response_instance = DeletePostgenIntegrations200Response.from_json(json)
# print the JSON string representation of the object
print(DeletePostgenIntegrations200Response.to_json())

# convert the object into a dict
delete_postgen_integrations200_response_dict = delete_postgen_integrations200_response_instance.to_dict()
# create an instance of DeletePostgenIntegrations200Response from a dict
delete_postgen_integrations200_response_from_dict = DeletePostgenIntegrations200Response.from_dict(delete_postgen_integrations200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


