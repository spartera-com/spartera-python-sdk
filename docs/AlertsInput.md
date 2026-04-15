# AlertsInput

Input schema for creating Alert

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **str** | References assets.asset_id — A published analytics asset — a calculation or visualization built on a data connection. See GET /assets for valid values. Required. | 
**user_id** | **str** | References users.user_id — An individual user account within a company. See GET /users for valid values. Optional. | [optional] 
**company_id** | **str** | References companies.company_id — A Spartera seller or buyer company account. See GET /companies for valid values. Required. | 
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


