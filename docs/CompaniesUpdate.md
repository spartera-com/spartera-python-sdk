# CompaniesUpdate

Update schema for modifying Company

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**industry_id** | **int** |  | [optional] 
**country_id** | **int** |  | [optional] 
**company_name** | **str** |  | [optional] 
**company_description** | **str** |  | [optional] 
**company_handle** | **str** |  | [optional] 
**company_domain** | **str** |  | [optional] 
**credits_balance** | **int** | Current balance of credits for this company (buyer) | [optional] 
**accepted_eula** | **bool** |  | [optional] 
**stripe_account_id** | **str** | Stripe Connect account ID for marketplace sellers | [optional] 
**stripe_account_status** | **str** | Status of the Stripe account (verified, pending, etc.) | [optional] 

## Example

```python
from spartera_api_sdk.models.companies_update import CompaniesUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of CompaniesUpdate from a JSON string
companies_update_instance = CompaniesUpdate.from_json(json)
# print the JSON string representation of the object
print(CompaniesUpdate.to_json())

# convert the object into a dict
companies_update_dict = companies_update_instance.to_dict()
# create an instance of CompaniesUpdate from a dict
companies_update_from_dict = CompaniesUpdate.from_dict(companies_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


