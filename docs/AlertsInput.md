# AlertsInput

Input schema for creating Alert

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **str** |  | 
**user_id** | **str** |  | [optional] 
**company_id** | **str** |  | 
**is_active** | **bool** | Whether this alert is currently active | [optional] 

## Example

```python
from spartera_api_sdk.models.alerts_input import AlertsInput

# TODO update the JSON string below
json = "{}"
# create an instance of AlertsInput from a JSON string
alerts_input_instance = AlertsInput.from_json(json)
# print the JSON string representation of the object
print(AlertsInput.to_json())

# convert the object into a dict
alerts_input_dict = alerts_input_instance.to_dict()
# create an instance of AlertsInput from a dict
alerts_input_from_dict = AlertsInput.from_dict(alerts_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


