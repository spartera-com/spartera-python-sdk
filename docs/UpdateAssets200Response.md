# UpdateAssets200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Response status message | 
**data** | [**UpdateAssets200ResponseData**](UpdateAssets200ResponseData.md) |  | 

## Example

```python
from spartera_api_sdk.models.update_assets200_response import UpdateAssets200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAssets200Response from a JSON string
update_assets200_response_instance = UpdateAssets200Response.from_json(json)
# print the JSON string representation of the object
print(UpdateAssets200Response.to_json())

# convert the object into a dict
update_assets200_response_dict = update_assets200_response_instance.to_dict()
# create an instance of UpdateAssets200Response from a dict
update_assets200_response_from_dict = UpdateAssets200Response.from_dict(update_assets200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


