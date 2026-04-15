# CreateConnections200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_id** | **str** | ID of the created connections | 

## Example

```python
from spartera_api_sdk.models.create_connections200_response_data import CreateConnections200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateConnections200ResponseData from a JSON string
create_connections200_response_data_instance = CreateConnections200ResponseData.from_json(json)
# print the JSON string representation of the object
print(CreateConnections200ResponseData.to_json())

# convert the object into a dict
create_connections200_response_data_dict = create_connections200_response_data_instance.to_dict()
# create an instance of CreateConnections200ResponseData from a dict
create_connections200_response_data_from_dict = CreateConnections200ResponseData.from_dict(create_connections200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


