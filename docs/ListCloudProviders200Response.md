# ListCloudProviders200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Response status message | 
**data** | [**List[CloudProviders]**](CloudProviders.md) |  | 

## Example

```python
from spartera_api_sdk.models.list_cloud_providers200_response import ListCloudProviders200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListCloudProviders200Response from a JSON string
list_cloud_providers200_response_instance = ListCloudProviders200Response.from_json(json)
# print the JSON string representation of the object
print(ListCloudProviders200Response.to_json())

# convert the object into a dict
list_cloud_providers200_response_dict = list_cloud_providers200_response_instance.to_dict()
# create an instance of ListCloudProviders200Response from a dict
list_cloud_providers200_response_from_dict = ListCloudProviders200Response.from_dict(list_cloud_providers200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


