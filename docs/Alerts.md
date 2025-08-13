# Alerts

User alerts for when assets are updated

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_created** | **datetime** |  | [optional] 
**last_updated** | **datetime** |  | [optional] 
**alert_id** | **int** |  | [optional] 
**asset_id** | **str** |  | 
**user_id** | **str** |  | [optional] 
**company_id** | **str** |  | 
**is_active** | **bool** | Whether this alert is currently active | 

## Example

```python
from spartera_api_sdk.models.alerts import Alerts

# TODO update the JSON string below
json = "{}"
# create an instance of Alerts from a JSON string
alerts_instance = Alerts.from_json(json)
# print the JSON string representation of the object
print(Alerts.to_json())

# convert the object into a dict
alerts_dict = alerts_instance.to_dict()
# create an instance of Alerts from a dict
alerts_from_dict = Alerts.from_dict(alerts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


