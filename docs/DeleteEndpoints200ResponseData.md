# DeleteEndpoints200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint_id** | **str** | ID of the deleted endpoints | 

## Example

```python
from spartera_api_sdk.models.delete_endpoints200_response_data import DeleteEndpoints200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteEndpoints200ResponseData from a JSON string
delete_endpoints200_response_data_instance = DeleteEndpoints200ResponseData.from_json(json)
# print the JSON string representation of the object
print(DeleteEndpoints200ResponseData.to_json())

# convert the object into a dict
delete_endpoints200_response_data_dict = delete_endpoints200_response_data_instance.to_dict()
# create an instance of DeleteEndpoints200ResponseData from a dict
delete_endpoints200_response_data_from_dict = DeleteEndpoints200ResponseData.from_dict(delete_endpoints200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


