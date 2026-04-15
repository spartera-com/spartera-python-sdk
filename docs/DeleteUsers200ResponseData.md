# DeleteUsers200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | ID of the deleted users | 

## Example

```python
from spartera_api_sdk.models.delete_users200_response_data import DeleteUsers200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteUsers200ResponseData from a JSON string
delete_users200_response_data_instance = DeleteUsers200ResponseData.from_json(json)
# print the JSON string representation of the object
print(DeleteUsers200ResponseData.to_json())

# convert the object into a dict
delete_users200_response_data_dict = delete_users200_response_data_instance.to_dict()
# create an instance of DeleteUsers200ResponseData from a dict
delete_users200_response_data_from_dict = DeleteUsers200ResponseData.from_dict(delete_users200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


