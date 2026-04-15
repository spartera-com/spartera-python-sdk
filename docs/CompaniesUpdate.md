# CompaniesUpdate

Update schema for modifying Company

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**industry_id** | **int** | References industries.industry_id — Available industry categories for asset classification. Based on US NAISC codes.. See GET /industries for valid values. Optional. | [optional] 
**country_id** | **int** | References countries.country_id — List of countries of the world. See GET /countries for valid values. Optional. | [optional] 
**company_name** | **str** | Optional. | [optional] 
**company_description** | **str** | Optional. | [optional] 
**company_handle** | **str** | Required. Must be unique. | [optional] 
**company_domain** | **str** | Required. Must be unique. | [optional] 
**credits_balance** | **int** | Current balance of credits for this company (buyer) | [optional] 
**accepted_eula** | **bool** | Optional. | [optional] 
**stripe_account_id** | **str** | Stripe Connect account ID for marketplace sellers | [optional] 
**stripe_account_status** | **str** | Status of the Stripe account (verified, pending, etc.) | [optional] 
**vendor_share_percent** | **float** | Negotiated vendor revenue share (e.g. 0.85 &#x3D; 85%). NULL &#x3D; system default 80%. | [optional] 
**partnership_type** | **str** | Partnership type: SELF_MANAGED, CUSTODIAN, or null | [optional] 

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


