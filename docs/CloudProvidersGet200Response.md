# CloudProvidersGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Response status message | 
**data** | [**List[CloudProviders]**](CloudProviders.md) |  | 

## Example

```python
from spartera_api_sdk.models.cloud_providers_get200_response import CloudProvidersGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CloudProvidersGet200Response from a JSON string
cloud_providers_get200_response_instance = CloudProvidersGet200Response.from_json(json)
# print the JSON string representation of the object
print(CloudProvidersGet200Response.to_json())

# convert the object into a dict
cloud_providers_get200_response_dict = cloud_providers_get200_response_instance.to_dict()
# create an instance of CloudProvidersGet200Response from a dict
cloud_providers_get200_response_from_dict = CloudProvidersGet200Response.from_dict(cloud_providers_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


