# CompaniesCompanyIdApiKeysApiKeyIdDelete200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Response status message | 
**data** | [**CompaniesCompanyIdApiKeysApiKeyIdDelete200ResponseData**](CompaniesCompanyIdApiKeysApiKeyIdDelete200ResponseData.md) |  | 

## Example

```python
from spartera_api_sdk.models.companies_company_id_api_keys_api_key_id_delete200_response import CompaniesCompanyIdApiKeysApiKeyIdDelete200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CompaniesCompanyIdApiKeysApiKeyIdDelete200Response from a JSON string
companies_company_id_api_keys_api_key_id_delete200_response_instance = CompaniesCompanyIdApiKeysApiKeyIdDelete200Response.from_json(json)
# print the JSON string representation of the object
print(CompaniesCompanyIdApiKeysApiKeyIdDelete200Response.to_json())

# convert the object into a dict
companies_company_id_api_keys_api_key_id_delete200_response_dict = companies_company_id_api_keys_api_key_id_delete200_response_instance.to_dict()
# create an instance of CompaniesCompanyIdApiKeysApiKeyIdDelete200Response from a dict
companies_company_id_api_keys_api_key_id_delete200_response_from_dict = CompaniesCompanyIdApiKeysApiKeyIdDelete200Response.from_dict(companies_company_id_api_keys_api_key_id_delete200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


