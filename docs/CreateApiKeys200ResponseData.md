# CreateApiKeys200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key_id** | **str** | ID of the created api_keys | 

## Example

```python
from spartera_api_sdk.models.create_api_keys200_response_data import CreateApiKeys200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateApiKeys200ResponseData from a JSON string
create_api_keys200_response_data_instance = CreateApiKeys200ResponseData.from_json(json)
# print the JSON string representation of the object
print(CreateApiKeys200ResponseData.to_json())

# convert the object into a dict
create_api_keys200_response_data_dict = create_api_keys200_response_data_instance.to_dict()
# create an instance of CreateApiKeys200ResponseData from a dict
create_api_keys200_response_data_from_dict = CreateApiKeys200ResponseData.from_dict(create_api_keys200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


