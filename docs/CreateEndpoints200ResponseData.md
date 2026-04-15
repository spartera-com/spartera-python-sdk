# CreateEndpoints200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint_id** | **str** | ID of the created endpoints | 

## Example

```python
from spartera_api_sdk.models.create_endpoints200_response_data import CreateEndpoints200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEndpoints200ResponseData from a JSON string
create_endpoints200_response_data_instance = CreateEndpoints200ResponseData.from_json(json)
# print the JSON string representation of the object
print(CreateEndpoints200ResponseData.to_json())

# convert the object into a dict
create_endpoints200_response_data_dict = create_endpoints200_response_data_instance.to_dict()
# create an instance of CreateEndpoints200ResponseData from a dict
create_endpoints200_response_data_from_dict = CreateEndpoints200ResponseData.from_dict(create_endpoints200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


