# DeleteUsers200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Response status message | 
**data** | [**DeleteUsers200ResponseData**](DeleteUsers200ResponseData.md) |  | 

## Example

```python
from spartera_api_sdk.models.delete_users200_response import DeleteUsers200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteUsers200Response from a JSON string
delete_users200_response_instance = DeleteUsers200Response.from_json(json)
# print the JSON string representation of the object
print(DeleteUsers200Response.to_json())

# convert the object into a dict
delete_users200_response_dict = delete_users200_response_instance.to_dict()
# create an instance of DeleteUsers200Response from a dict
delete_users200_response_from_dict = DeleteUsers200Response.from_dict(delete_users200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


