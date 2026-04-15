# Alerts

A notification alert triggered when a subscribed asset is updated

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_created** | **datetime** | Optional. | [optional] 
**last_updated** | **datetime** | Optional. | [optional] 
**alert_id** | **int** | Auto-generated unique identifier. | [optional] 
**asset_id** | **str** | References assets.asset_id — A published analytics asset — a calculation or visualization built on a data connection. See GET /assets for valid values. Required. | 
**user_id** | **str** | References users.user_id — An individual user account within a company. See GET /users for valid values. Optional. | [optional] 
**company_id** | **str** | References companies.company_id — A Spartera seller or buyer company account. See GET /companies for valid values. Required. | 
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


