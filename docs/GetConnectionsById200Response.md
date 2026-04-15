# GetConnectionsById200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Response status message | 
**data** | [**Connections**](Connections.md) |  | 

## Example

```python
from spartera_api_sdk.models.get_connections_by_id200_response import GetConnectionsById200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetConnectionsById200Response from a JSON string
get_connections_by_id200_response_instance = GetConnectionsById200Response.from_json(json)
# print the JSON string representation of the object
print(GetConnectionsById200Response.to_json())

# convert the object into a dict
get_connections_by_id200_response_dict = get_connections_by_id200_response_instance.to_dict()
# create an instance of GetConnectionsById200Response from a dict
get_connections_by_id200_response_from_dict = GetConnectionsById200Response.from_dict(get_connections_by_id200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


