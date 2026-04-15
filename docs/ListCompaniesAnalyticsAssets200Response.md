# ListCompaniesAnalyticsAssets200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Response status message | 
**data** | [**List[Companies]**](Companies.md) |  | 

## Example

```python
from spartera_api_sdk.models.list_companies_analytics_assets200_response import ListCompaniesAnalyticsAssets200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListCompaniesAnalyticsAssets200Response from a JSON string
list_companies_analytics_assets200_response_instance = ListCompaniesAnalyticsAssets200Response.from_json(json)
# print the JSON string representation of the object
print(ListCompaniesAnalyticsAssets200Response.to_json())

# convert the object into a dict
list_companies_analytics_assets200_response_dict = list_companies_analytics_assets200_response_instance.to_dict()
# create an instance of ListCompaniesAnalyticsAssets200Response from a dict
list_companies_analytics_assets200_response_from_dict = ListCompaniesAnalyticsAssets200Response.from_dict(list_companies_analytics_assets200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


