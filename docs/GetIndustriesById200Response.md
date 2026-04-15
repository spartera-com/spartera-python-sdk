# GetIndustriesById200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Response status message | 
**data** | [**Industries**](Industries.md) |  | 

## Example

```python
from spartera_api_sdk.models.get_industries_by_id200_response import GetIndustriesById200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetIndustriesById200Response from a JSON string
get_industries_by_id200_response_instance = GetIndustriesById200Response.from_json(json)
# print the JSON string representation of the object
print(GetIndustriesById200Response.to_json())

# convert the object into a dict
get_industries_by_id200_response_dict = get_industries_by_id200_response_instance.to_dict()
# create an instance of GetIndustriesById200Response from a dict
get_industries_by_id200_response_from_dict = GetIndustriesById200Response.from_dict(get_industries_by_id200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


