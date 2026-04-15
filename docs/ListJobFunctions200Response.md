# ListJobFunctions200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Response status message | 
**data** | [**List[JobFunctions]**](JobFunctions.md) |  | 

## Example

```python
from spartera_api_sdk.models.list_job_functions200_response import ListJobFunctions200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListJobFunctions200Response from a JSON string
list_job_functions200_response_instance = ListJobFunctions200Response.from_json(json)
# print the JSON string representation of the object
print(ListJobFunctions200Response.to_json())

# convert the object into a dict
list_job_functions200_response_dict = list_job_functions200_response_instance.to_dict()
# create an instance of ListJobFunctions200Response from a dict
list_job_functions200_response_from_dict = ListJobFunctions200Response.from_dict(list_job_functions200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


