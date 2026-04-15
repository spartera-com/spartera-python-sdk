# CreateConnections200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Response status message | 
**data** | [**CreateConnections200ResponseData**](CreateConnections200ResponseData.md) |  | 

## Example

```python
from spartera_api_sdk.models.create_connections200_response import CreateConnections200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateConnections200Response from a JSON string
create_connections200_response_instance = CreateConnections200Response.from_json(json)
# print the JSON string representation of the object
print(CreateConnections200Response.to_json())

# convert the object into a dict
create_connections200_response_dict = create_connections200_response_instance.to_dict()
# create an instance of CreateConnections200Response from a dict
create_connections200_response_from_dict = CreateConnections200Response.from_dict(create_connections200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


