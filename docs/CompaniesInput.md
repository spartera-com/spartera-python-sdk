# CompaniesInput

Input schema for creating Company

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**industry_id** | **int** |  | [optional] 
**country_id** | **int** |  | [optional] 
**company_name** | **str** |  | [optional] 
**company_description** | **str** |  | [optional] 
**company_handle** | **str** |  | 
**company_domain** | **str** |  | 
**credits_balance** | **int** | Current balance of credits for this company (buyer) | [optional] 
**accepted_eula** | **bool** |  | [optional] 
**stripe_account_id** | **str** | Stripe Connect account ID for marketplace sellers | [optional] 
**stripe_account_status** | **str** | Status of the Stripe account (verified, pending, etc.) | [optional] 

## Example

```python
from spartera_api_sdk.models.companies_input import CompaniesInput

# TODO update the JSON string below
json = "{}"
# create an instance of CompaniesInput from a JSON string
companies_input_instance = CompaniesInput.from_json(json)
# print the JSON string representation of the object
print(CompaniesInput.to_json())

# convert the object into a dict
companies_input_dict = companies_input_instance.to_dict()
# create an instance of CompaniesInput from a dict
companies_input_from_dict = CompaniesInput.from_dict(companies_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


