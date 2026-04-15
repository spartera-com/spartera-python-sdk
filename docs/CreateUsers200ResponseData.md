# CreateUsers200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | ID of the created users | 

## Example

```python
from spartera_api_sdk.models.create_users200_response_data import CreateUsers200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUsers200ResponseData from a JSON string
create_users200_response_data_instance = CreateUsers200ResponseData.from_json(json)
# print the JSON string representation of the object
print(CreateUsers200ResponseData.to_json())

# convert the object into a dict
create_users200_response_data_dict = create_users200_response_data_instance.to_dict()
# create an instance of CreateUsers200ResponseData from a dict
create_users200_response_data_from_dict = CreateUsers200ResponseData.from_dict(create_users200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


