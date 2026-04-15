# ListConnections200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Response status message | 
**data** | [**List[Connections]**](Connections.md) |  | 

## Example

```python
from spartera_api_sdk.models.list_connections200_response import ListConnections200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListConnections200Response from a JSON string
list_connections200_response_instance = ListConnections200Response.from_json(json)
# print the JSON string representation of the object
print(ListConnections200Response.to_json())

# convert the object into a dict
list_connections200_response_dict = list_connections200_response_instance.to_dict()
# create an instance of ListConnections200Response from a dict
list_connections200_response_from_dict = ListConnections200Response.from_dict(list_connections200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


