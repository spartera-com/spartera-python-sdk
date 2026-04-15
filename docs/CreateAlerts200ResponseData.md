# CreateAlerts200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_id** | **str** | ID of the created alerts | 

## Example

```python
from spartera_api_sdk.models.create_alerts200_response_data import CreateAlerts200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAlerts200ResponseData from a JSON string
create_alerts200_response_data_instance = CreateAlerts200ResponseData.from_json(json)
# print the JSON string representation of the object
print(CreateAlerts200ResponseData.to_json())

# convert the object into a dict
create_alerts200_response_data_dict = create_alerts200_response_data_instance.to_dict()
# create an instance of CreateAlerts200ResponseData from a dict
create_alerts200_response_data_from_dict = CreateAlerts200ResponseData.from_dict(create_alerts200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


