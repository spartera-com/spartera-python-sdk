# CompaniesCompanyIdConnectionsConnectionIdGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Response status message | 
**data** | [**Connections**](Connections.md) |  | 

## Example

```python
from spartera_api_sdk.models.companies_company_id_connections_connection_id_get200_response import CompaniesCompanyIdConnectionsConnectionIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CompaniesCompanyIdConnectionsConnectionIdGet200Response from a JSON string
companies_company_id_connections_connection_id_get200_response_instance = CompaniesCompanyIdConnectionsConnectionIdGet200Response.from_json(json)
# print the JSON string representation of the object
print(CompaniesCompanyIdConnectionsConnectionIdGet200Response.to_json())

# convert the object into a dict
companies_company_id_connections_connection_id_get200_response_dict = companies_company_id_connections_connection_id_get200_response_instance.to_dict()
# create an instance of CompaniesCompanyIdConnectionsConnectionIdGet200Response from a dict
companies_company_id_connections_connection_id_get200_response_from_dict = CompaniesCompanyIdConnectionsConnectionIdGet200Response.from_dict(companies_company_id_connections_connection_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


