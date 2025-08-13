# CloudProviders

Cloud providers (platforms) database

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_created** | **datetime** |  | [optional] 
**last_updated** | **datetime** |  | [optional] 
**provider_id** | **int** |  | [optional] 
**name** | **str** |  | 
**parent_company** | **str** |  | [optional] 
**marketing_homepage_url** | **str** |  | [optional] 

## Example

```python
from spartera_api_sdk.models.cloud_providers import CloudProviders

# TODO update the JSON string below
json = "{}"
# create an instance of CloudProviders from a JSON string
cloud_providers_instance = CloudProviders.from_json(json)
# print the JSON string representation of the object
print(CloudProviders.to_json())

# convert the object into a dict
cloud_providers_dict = cloud_providers_instance.to_dict()
# create an instance of CloudProviders from a dict
cloud_providers_from_dict = CloudProviders.from_dict(cloud_providers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


