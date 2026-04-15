# CloudProviders

Supported cloud platforms and database engines available for connections

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_created** | **datetime** | Optional. | [optional] 
**last_updated** | **datetime** | Optional. | [optional] 
**provider_id** | **int** | Auto-generated unique identifier. | [optional] 
**name** | **str** | Required. | 
**parent_company** | **str** | Optional. | [optional] 
**marketing_homepage_url** | **str** | Optional. | [optional] 

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


