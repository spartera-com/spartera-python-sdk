# GetAlertsById200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Response status message | 
**data** | [**Alerts**](Alerts.md) |  | 

## Example

```python
from spartera_api_sdk.models.get_alerts_by_id200_response import GetAlertsById200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAlertsById200Response from a JSON string
get_alerts_by_id200_response_instance = GetAlertsById200Response.from_json(json)
# print the JSON string representation of the object
print(GetAlertsById200Response.to_json())

# convert the object into a dict
get_alerts_by_id200_response_dict = get_alerts_by_id200_response_instance.to_dict()
# create an instance of GetAlertsById200Response from a dict
get_alerts_by_id200_response_from_dict = GetAlertsById200Response.from_dict(get_alerts_by_id200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


