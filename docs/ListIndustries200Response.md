# ListIndustries200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Response status message | 
**data** | [**List[Industries]**](Industries.md) |  | 

## Example

```python
from spartera_api_sdk.models.list_industries200_response import ListIndustries200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListIndustries200Response from a JSON string
list_industries200_response_instance = ListIndustries200Response.from_json(json)
# print the JSON string representation of the object
print(ListIndustries200Response.to_json())

# convert the object into a dict
list_industries200_response_dict = list_industries200_response_instance.to_dict()
# create an instance of ListIndustries200Response from a dict
list_industries200_response_from_dict = ListIndustries200Response.from_dict(list_industries200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


