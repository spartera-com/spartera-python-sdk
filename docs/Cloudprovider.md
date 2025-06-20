# Cloudprovider

Cloud providers (platforms) database

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_id** | **str** |  | [optional] [readonly] 
**name** | **str** |  | 
**parent_company** | **str** |  | [optional] 
**marketing_homepage_url** | **str** |  | [optional] 
**date_created** | **str** |  | [optional] 
**last_updated** | **str** |  | [optional] 
**active** | **str** |  | [optional] 

## Example

```python
from spartera_api_sdk.models.cloudprovider import Cloudprovider

# TODO update the JSON string below
json = "{}"
# create an instance of Cloudprovider from a JSON string
cloudprovider_instance = Cloudprovider.from_json(json)
# print the JSON string representation of the object
print(Cloudprovider.to_json())

# convert the object into a dict
cloudprovider_dict = cloudprovider_instance.to_dict()
# create an instance of Cloudprovider from a dict
cloudprovider_from_dict = Cloudprovider.from_dict(cloudprovider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


