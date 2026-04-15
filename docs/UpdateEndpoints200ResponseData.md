# UpdateEndpoints200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint_id** | **str** | ID of the updated endpoints | 

## Example

```python
from spartera_api_sdk.models.update_endpoints200_response_data import UpdateEndpoints200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateEndpoints200ResponseData from a JSON string
update_endpoints200_response_data_instance = UpdateEndpoints200ResponseData.from_json(json)
# print the JSON string representation of the object
print(UpdateEndpoints200ResponseData.to_json())

# convert the object into a dict
update_endpoints200_response_data_dict = update_endpoints200_response_data_instance.to_dict()
# create an instance of UpdateEndpoints200ResponseData from a dict
update_endpoints200_response_data_from_dict = UpdateEndpoints200ResponseData.from_dict(update_endpoints200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


