# DeleteAssets200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **str** | ID of the deleted assets | 

## Example

```python
from spartera_api_sdk.models.delete_assets200_response_data import DeleteAssets200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteAssets200ResponseData from a JSON string
delete_assets200_response_data_instance = DeleteAssets200ResponseData.from_json(json)
# print the JSON string representation of the object
print(DeleteAssets200ResponseData.to_json())

# convert the object into a dict
delete_assets200_response_data_dict = delete_assets200_response_data_instance.to_dict()
# create an instance of DeleteAssets200ResponseData from a dict
delete_assets200_response_data_from_dict = DeleteAssets200ResponseData.from_dict(delete_assets200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


