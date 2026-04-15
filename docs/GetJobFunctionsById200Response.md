# GetJobFunctionsById200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Response status message | 
**data** | [**JobFunctions**](JobFunctions.md) |  | 

## Example

```python
from spartera_api_sdk.models.get_job_functions_by_id200_response import GetJobFunctionsById200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetJobFunctionsById200Response from a JSON string
get_job_functions_by_id200_response_instance = GetJobFunctionsById200Response.from_json(json)
# print the JSON string representation of the object
print(GetJobFunctionsById200Response.to_json())

# convert the object into a dict
get_job_functions_by_id200_response_dict = get_job_functions_by_id200_response_instance.to_dict()
# create an instance of GetJobFunctionsById200Response from a dict
get_job_functions_by_id200_response_from_dict = GetJobFunctionsById200Response.from_dict(get_job_functions_by_id200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


