# CreateAssetsAnalyze200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Response status message | 
**data** | [**CreateAssetsAnalyze200ResponseData**](CreateAssetsAnalyze200ResponseData.md) |  | 

## Example

```python
from spartera_api_sdk.models.create_assets_analyze200_response import CreateAssetsAnalyze200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAssetsAnalyze200Response from a JSON string
create_assets_analyze200_response_instance = CreateAssetsAnalyze200Response.from_json(json)
# print the JSON string representation of the object
print(CreateAssetsAnalyze200Response.to_json())

# convert the object into a dict
create_assets_analyze200_response_dict = create_assets_analyze200_response_instance.to_dict()
# create an instance of CreateAssetsAnalyze200Response from a dict
create_assets_analyze200_response_from_dict = CreateAssetsAnalyze200Response.from_dict(create_assets_analyze200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


