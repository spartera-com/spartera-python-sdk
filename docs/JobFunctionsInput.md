# JobFunctionsInput

Input schema for creating JobFunction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 

## Example

```python
from spartera_api_sdk.models.job_functions_input import JobFunctionsInput

# TODO update the JSON string below
json = "{}"
# create an instance of JobFunctionsInput from a JSON string
job_functions_input_instance = JobFunctionsInput.from_json(json)
# print the JSON string representation of the object
print(JobFunctionsInput.to_json())

# convert the object into a dict
job_functions_input_dict = job_functions_input_instance.to_dict()
# create an instance of JobFunctionsInput from a dict
job_functions_input_from_dict = JobFunctionsInput.from_dict(job_functions_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


