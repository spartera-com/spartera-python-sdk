# DeleteEndpoints200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Response status message | 
**data** | [**DeleteEndpoints200ResponseData**](DeleteEndpoints200ResponseData.md) |  | 

## Example

```python
from spartera_api_sdk.models.delete_endpoints200_response import DeleteEndpoints200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteEndpoints200Response from a JSON string
delete_endpoints200_response_instance = DeleteEndpoints200Response.from_json(json)
# print the JSON string representation of the object
print(DeleteEndpoints200Response.to_json())

# convert the object into a dict
delete_endpoints200_response_dict = delete_endpoints200_response_instance.to_dict()
# create an instance of DeleteEndpoints200Response from a dict
delete_endpoints200_response_from_dict = DeleteEndpoints200Response.from_dict(delete_endpoints200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


