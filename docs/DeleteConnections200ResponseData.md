# DeleteConnections200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_id** | **str** | ID of the deleted connections | 

## Example

```python
from spartera_api_sdk.models.delete_connections200_response_data import DeleteConnections200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteConnections200ResponseData from a JSON string
delete_connections200_response_data_instance = DeleteConnections200ResponseData.from_json(json)
# print the JSON string representation of the object
print(DeleteConnections200ResponseData.to_json())

# convert the object into a dict
delete_connections200_response_data_dict = delete_connections200_response_data_instance.to_dict()
# create an instance of DeleteConnections200ResponseData from a dict
delete_connections200_response_data_from_dict = DeleteConnections200ResponseData.from_dict(delete_connections200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


