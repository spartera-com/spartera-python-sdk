# Alert

User alerts for when assets are updated

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_id** | **str** |  | [optional] [readonly] 
**asset_id** | **str** |  | 
**user_id** | **str** |  | [optional] 
**company_id** | **str** |  | 
**alert_type** | **str** |  | 
**is_active** | **str** |  | [optional] 
**last_triggered** | **str** |  | [optional] 
**date_created** | **str** |  | [optional] [readonly] 
**last_updated** | **str** |  | [optional] [readonly] 
**active** | **str** |  | [optional] 

## Example

```python
from spartera_api_sdk.models.alert import Alert

# TODO update the JSON string below
json = "{}"
# create an instance of Alert from a JSON string
alert_instance = Alert.from_json(json)
# print the JSON string representation of the object
print(Alert.to_json())

# convert the object into a dict
alert_dict = alert_instance.to_dict()
# create an instance of Alert from a dict
alert_from_dict = Alert.from_dict(alert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


