# Companies

A Spartera seller or buyer company account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_created** | **datetime** | Optional. | [optional] 
**last_updated** | **datetime** | Optional. | [optional] 
**company_id** | **str** | Unique identifier. | [optional] 
**industry_id** | **int** | References industries.industry_id — Available industry categories for asset classification. Based on US NAISC codes.. See GET /industries for valid values. Optional. | [optional] 
**country_id** | **int** | References countries.country_id — List of countries of the world. See GET /countries for valid values. Optional. | [optional] 
**company_name** | **str** | Optional. | [optional] 
**company_description** | **str** | Optional. | [optional] 
**company_handle** | **str** | Required. Must be unique. | 
**company_domain** | **str** | Required. Must be unique. | 
**credits_balance** | **int** | Current balance of credits for this company (buyer) | 
**accepted_eula** | **bool** | Optional. | [optional] 
**stripe_account_id** | **str** | Stripe Connect account ID for marketplace sellers | [optional] 
**stripe_account_status** | **str** | Status of the Stripe account (verified, pending, etc.) | [optional] 
**vendor_share_percent** | **float** | Negotiated vendor revenue share (e.g. 0.85 &#x3D; 85%). NULL &#x3D; system default 80%. | [optional] 
**partnership_type** | **str** | Partnership type: SELF_MANAGED, CUSTODIAN, or null | [optional] 

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


