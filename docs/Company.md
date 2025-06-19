# Company

All of our customer company entities

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_id** | **str** |  | [optional] 
**industry_id** | **str** |  | [optional] 
**country_id** | **str** |  | [optional] 
**company_name** | **str** |  | [optional] 
**company_description** | **str** |  | [optional] 
**company_handle** | **str** |  | 
**company_domain** | **str** |  | 
**credits_balance** | **str** |  | 
**accepted_eula** | **str** |  | [optional] 
**stripe_account_id** | **str** |  | [optional] 
**stripe_account_status** | **str** |  | [optional] 
**date_created** | **str** |  | [optional] 
**last_updated** | **str** |  | [optional] 
**active** | **str** |  | [optional] 

## Example

```python
from spartera_api_sdk.models.company import Company

# TODO update the JSON string below
json = "{}"
# create an instance of Company from a JSON string
company_instance = Company.from_json(json)
# print the JSON string representation of the object
print(Company.to_json())

# convert the object into a dict
company_dict = company_instance.to_dict()
# create an instance of Company from a dict
company_from_dict = Company.from_dict(company_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


