# CompaniesCompanyIdAssetsAssetIdPricesPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Response status message | 
**data** | [**CompaniesCompanyIdAssetsAssetIdPricesPost200ResponseData**](CompaniesCompanyIdAssetsAssetIdPricesPost200ResponseData.md) |  | 

## Example

```python
from spartera_api_sdk.models.companies_company_id_assets_asset_id_prices_post200_response import CompaniesCompanyIdAssetsAssetIdPricesPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CompaniesCompanyIdAssetsAssetIdPricesPost200Response from a JSON string
companies_company_id_assets_asset_id_prices_post200_response_instance = CompaniesCompanyIdAssetsAssetIdPricesPost200Response.from_json(json)
# print the JSON string representation of the object
print(CompaniesCompanyIdAssetsAssetIdPricesPost200Response.to_json())

# convert the object into a dict
companies_company_id_assets_asset_id_prices_post200_response_dict = companies_company_id_assets_asset_id_prices_post200_response_instance.to_dict()
# create an instance of CompaniesCompanyIdAssetsAssetIdPricesPost200Response from a dict
companies_company_id_assets_asset_id_prices_post200_response_from_dict = CompaniesCompanyIdAssetsAssetIdPricesPost200Response.from_dict(companies_company_id_assets_asset_id_prices_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


