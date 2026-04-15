# UpdateAlerts200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_id** | **str** | ID of the updated alerts | 

## Example

```python
from spartera_api_sdk.models.update_alerts200_response_data import UpdateAlerts200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAlerts200ResponseData from a JSON string
update_alerts200_response_data_instance = UpdateAlerts200ResponseData.from_json(json)
# print the JSON string representation of the object
print(UpdateAlerts200ResponseData.to_json())

# convert the object into a dict
update_alerts200_response_data_dict = update_alerts200_response_data_instance.to_dict()
# create an instance of UpdateAlerts200ResponseData from a dict
update_alerts200_response_data_from_dict = UpdateAlerts200ResponseData.from_dict(update_alerts200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


