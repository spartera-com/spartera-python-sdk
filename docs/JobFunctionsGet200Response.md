# JobFunctionsGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Response status message | 
**data** | [**List[JobFunctions]**](JobFunctions.md) |  | 

## Example

```python
from spartera_api_sdk.models.job_functions_get200_response import JobFunctionsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of JobFunctionsGet200Response from a JSON string
job_functions_get200_response_instance = JobFunctionsGet200Response.from_json(json)
# print the JSON string representation of the object
print(JobFunctionsGet200Response.to_json())

# convert the object into a dict
job_functions_get200_response_dict = job_functions_get200_response_instance.to_dict()
# create an instance of JobFunctionsGet200Response from a dict
job_functions_get200_response_from_dict = JobFunctionsGet200Response.from_dict(job_functions_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


