# CompaniesCompanyIdUsersUserIdAlertsGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Response status message | 
**data** | [**List[Alerts]**](Alerts.md) |  | 

## Example

```python
from spartera_api_sdk.models.companies_company_id_users_user_id_alerts_get200_response import CompaniesCompanyIdUsersUserIdAlertsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CompaniesCompanyIdUsersUserIdAlertsGet200Response from a JSON string
companies_company_id_users_user_id_alerts_get200_response_instance = CompaniesCompanyIdUsersUserIdAlertsGet200Response.from_json(json)
# print the JSON string representation of the object
print(CompaniesCompanyIdUsersUserIdAlertsGet200Response.to_json())

# convert the object into a dict
companies_company_id_users_user_id_alerts_get200_response_dict = companies_company_id_users_user_id_alerts_get200_response_instance.to_dict()
# create an instance of CompaniesCompanyIdUsersUserIdAlertsGet200Response from a dict
companies_company_id_users_user_id_alerts_get200_response_from_dict = CompaniesCompanyIdUsersUserIdAlertsGet200Response.from_dict(companies_company_id_users_user_id_alerts_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


