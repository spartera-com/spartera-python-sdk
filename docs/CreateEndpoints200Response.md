# CreateEndpoints200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Response status message | 
**data** | [**CreateEndpoints200ResponseData**](CreateEndpoints200ResponseData.md) |  | 

## Example

```python
from spartera_api_sdk.models.create_endpoints200_response import CreateEndpoints200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEndpoints200Response from a JSON string
create_endpoints200_response_instance = CreateEndpoints200Response.from_json(json)
# print the JSON string representation of the object
print(CreateEndpoints200Response.to_json())

# convert the object into a dict
create_endpoints200_response_dict = create_endpoints200_response_instance.to_dict()
# create an instance of CreateEndpoints200Response from a dict
create_endpoints200_response_from_dict = CreateEndpoints200Response.from_dict(create_endpoints200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


