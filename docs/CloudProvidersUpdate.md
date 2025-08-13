# CloudProvidersUpdate

Update schema for modifying CloudProvider

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**parent_company** | **str** |  | [optional] 
**marketing_homepage_url** | **str** |  | [optional] 

## Example

```python
from spartera_api_sdk.models.cloud_providers_update import CloudProvidersUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of CloudProvidersUpdate from a JSON string
cloud_providers_update_instance = CloudProvidersUpdate.from_json(json)
# print the JSON string representation of the object
print(CloudProvidersUpdate.to_json())

# convert the object into a dict
cloud_providers_update_dict = cloud_providers_update_instance.to_dict()
# create an instance of CloudProvidersUpdate from a dict
cloud_providers_update_from_dict = CloudProvidersUpdate.from_dict(cloud_providers_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


