# ListStorageEngines200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Response status message | 
**data** | [**List[StorageEngines]**](StorageEngines.md) |  | 

## Example

```python
from spartera_api_sdk.models.list_storage_engines200_response import ListStorageEngines200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListStorageEngines200Response from a JSON string
list_storage_engines200_response_instance = ListStorageEngines200Response.from_json(json)
# print the JSON string representation of the object
print(ListStorageEngines200Response.to_json())

# convert the object into a dict
list_storage_engines200_response_dict = list_storage_engines200_response_instance.to_dict()
# create an instance of ListStorageEngines200Response from a dict
list_storage_engines200_response_from_dict = ListStorageEngines200Response.from_dict(list_storage_engines200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


