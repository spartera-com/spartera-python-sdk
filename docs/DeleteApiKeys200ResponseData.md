# DeleteApiKeys200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key_id** | **str** | ID of the deleted api_keys | 

## Example

```python
from spartera_api_sdk.models.delete_api_keys200_response_data import DeleteApiKeys200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteApiKeys200ResponseData from a JSON string
delete_api_keys200_response_data_instance = DeleteApiKeys200ResponseData.from_json(json)
# print the JSON string representation of the object
print(DeleteApiKeys200ResponseData.to_json())

# convert the object into a dict
delete_api_keys200_response_data_dict = delete_api_keys200_response_data_instance.to_dict()
# create an instance of DeleteApiKeys200ResponseData from a dict
delete_api_keys200_response_data_from_dict = DeleteApiKeys200ResponseData.from_dict(delete_api_keys200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


