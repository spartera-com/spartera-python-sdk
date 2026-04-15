# GetEndpointsByIdConnectionsDescribe200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Response status message | 
**data** | [**Endpoints**](Endpoints.md) |  | 

## Example

```python
from spartera_api_sdk.models.get_endpoints_by_id_connections_describe200_response import GetEndpointsByIdConnectionsDescribe200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetEndpointsByIdConnectionsDescribe200Response from a JSON string
get_endpoints_by_id_connections_describe200_response_instance = GetEndpointsByIdConnectionsDescribe200Response.from_json(json)
# print the JSON string representation of the object
print(GetEndpointsByIdConnectionsDescribe200Response.to_json())

# convert the object into a dict
get_endpoints_by_id_connections_describe200_response_dict = get_endpoints_by_id_connections_describe200_response_instance.to_dict()
# create an instance of GetEndpointsByIdConnectionsDescribe200Response from a dict
get_endpoints_by_id_connections_describe200_response_from_dict = GetEndpointsByIdConnectionsDescribe200Response.from_dict(get_endpoints_by_id_connections_describe200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


