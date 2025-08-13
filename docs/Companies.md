# Companies

All of our customer company entities

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_created** | **datetime** |  | [optional] 
**last_updated** | **datetime** |  | [optional] 
**company_id** | **str** |  | [optional] 
**industry_id** | **int** |  | [optional] 
**country_id** | **int** |  | [optional] 
**company_name** | **str** |  | [optional] 
**company_description** | **str** |  | [optional] 
**company_handle** | **str** |  | 
**company_domain** | **str** |  | 
**credits_balance** | **int** | Current balance of credits for this company (buyer) | 
**accepted_eula** | **bool** |  | [optional] 
**stripe_account_id** | **str** | Stripe Connect account ID for marketplace sellers | [optional] 
**stripe_account_status** | **str** | Status of the Stripe account (verified, pending, etc.) | [optional] 

## Example

```python
from spartera_api_sdk.models.companies import Companies

# TODO update the JSON string below
json = "{}"
# create an instance of Companies from a JSON string
companies_instance = Companies.from_json(json)
# print the JSON string representation of the object
print(Companies.to_json())

# convert the object into a dict
companies_dict = companies_instance.to_dict()
# create an instance of Companies from a dict
companies_from_dict = Companies.from_dict(companies_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


