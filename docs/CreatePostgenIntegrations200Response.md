# CreatePostgenIntegrations200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Response status message | 
**data** | [**CreatePostgenIntegrations200ResponseData**](CreatePostgenIntegrations200ResponseData.md) |  | 

## Example

```python
from spartera_api_sdk.models.create_postgen_integrations200_response import CreatePostgenIntegrations200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePostgenIntegrations200Response from a JSON string
create_postgen_integrations200_response_instance = CreatePostgenIntegrations200Response.from_json(json)
# print the JSON string representation of the object
print(CreatePostgenIntegrations200Response.to_json())

# convert the object into a dict
create_postgen_integrations200_response_dict = create_postgen_integrations200_response_instance.to_dict()
# create an instance of CreatePostgenIntegrations200Response from a dict
create_postgen_integrations200_response_from_dict = CreatePostgenIntegrations200Response.from_dict(create_postgen_integrations200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


