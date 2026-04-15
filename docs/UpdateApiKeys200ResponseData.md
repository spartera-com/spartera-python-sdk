# UpdateApiKeys200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key_id** | **str** | ID of the updated api_keys | 

## Example

```python
from spartera_api_sdk.models.update_api_keys200_response_data import UpdateApiKeys200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateApiKeys200ResponseData from a JSON string
update_api_keys200_response_data_instance = UpdateApiKeys200ResponseData.from_json(json)
# print the JSON string representation of the object
print(UpdateApiKeys200ResponseData.to_json())

# convert the object into a dict
update_api_keys200_response_data_dict = update_api_keys200_response_data_instance.to_dict()
# create an instance of UpdateApiKeys200ResponseData from a dict
update_api_keys200_response_data_from_dict = UpdateApiKeys200ResponseData.from_dict(update_api_keys200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


