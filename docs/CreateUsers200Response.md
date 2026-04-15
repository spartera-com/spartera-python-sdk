# CreateUsers200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Response status message | 
**data** | [**CreateUsers200ResponseData**](CreateUsers200ResponseData.md) |  | 

## Example

```python
from spartera_api_sdk.models.create_users200_response import CreateUsers200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUsers200Response from a JSON string
create_users200_response_instance = CreateUsers200Response.from_json(json)
# print the JSON string representation of the object
print(CreateUsers200Response.to_json())

# convert the object into a dict
create_users200_response_dict = create_users200_response_instance.to_dict()
# create an instance of CreateUsers200Response from a dict
create_users200_response_from_dict = CreateUsers200Response.from_dict(create_users200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


