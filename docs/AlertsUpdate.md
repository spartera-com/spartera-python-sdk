# AlertsUpdate

Update schema for modifying Alert

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**company_id** | **str** |  | [optional] 
**is_active** | **bool** | Whether this alert is currently active | [optional] 

## Example

```python
from spartera_api_sdk.models.alerts_update import AlertsUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of AlertsUpdate from a JSON string
alerts_update_instance = AlertsUpdate.from_json(json)
# print the JSON string representation of the object
print(AlertsUpdate.to_json())

# convert the object into a dict
alerts_update_dict = alerts_update_instance.to_dict()
# create an instance of AlertsUpdate from a dict
alerts_update_from_dict = AlertsUpdate.from_dict(alerts_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


