# CloudProvidersInput

Input schema for creating CloudProvider

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**parent_company** | **str** |  | [optional] 
**marketing_homepage_url** | **str** |  | [optional] 

## Example

```python
from spartera_api_sdk.models.cloud_providers_input import CloudProvidersInput

# TODO update the JSON string below
json = "{}"
# create an instance of CloudProvidersInput from a JSON string
cloud_providers_input_instance = CloudProvidersInput.from_json(json)
# print the JSON string representation of the object
print(CloudProvidersInput.to_json())

# convert the object into a dict
cloud_providers_input_dict = cloud_providers_input_instance.to_dict()
# create an instance of CloudProvidersInput from a dict
cloud_providers_input_from_dict = CloudProvidersInput.from_dict(cloud_providers_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


