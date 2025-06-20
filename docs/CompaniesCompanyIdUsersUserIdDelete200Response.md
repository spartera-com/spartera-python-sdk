# CompaniesCompanyIdUsersUserIdDelete200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Response status message | 
**data** | [**CompaniesCompanyIdUsersUserIdDelete200ResponseData**](CompaniesCompanyIdUsersUserIdDelete200ResponseData.md) |  | 

## Example

```python
from spartera_api_sdk.models.companies_company_id_users_user_id_delete200_response import CompaniesCompanyIdUsersUserIdDelete200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CompaniesCompanyIdUsersUserIdDelete200Response from a JSON string
companies_company_id_users_user_id_delete200_response_instance = CompaniesCompanyIdUsersUserIdDelete200Response.from_json(json)
# print the JSON string representation of the object
print(CompaniesCompanyIdUsersUserIdDelete200Response.to_json())

# convert the object into a dict
companies_company_id_users_user_id_delete200_response_dict = companies_company_id_users_user_id_delete200_response_instance.to_dict()
# create an instance of CompaniesCompanyIdUsersUserIdDelete200Response from a dict
companies_company_id_users_user_id_delete200_response_from_dict = CompaniesCompanyIdUsersUserIdDelete200Response.from_dict(companies_company_id_users_user_id_delete200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


