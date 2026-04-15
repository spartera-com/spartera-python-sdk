# UpdateApiKeys200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Response status message | 
**data** | [**UpdateApiKeys200ResponseData**](UpdateApiKeys200ResponseData.md) |  | 

## Example

```python
from spartera_api_sdk.models.update_api_keys200_response import UpdateApiKeys200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateApiKeys200Response from a JSON string
update_api_keys200_response_instance = UpdateApiKeys200Response.from_json(json)
# print the JSON string representation of the object
print(UpdateApiKeys200Response.to_json())

# convert the object into a dict
update_api_keys200_response_dict = update_api_keys200_response_instance.to_dict()
# create an instance of UpdateApiKeys200Response from a dict
update_api_keys200_response_from_dict = UpdateApiKeys200Response.from_dict(update_api_keys200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


