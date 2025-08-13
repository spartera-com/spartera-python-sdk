# JobFunctions

Metadata about the different kinds of job function our users have.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_created** | **datetime** |  | [optional] 
**last_updated** | **datetime** |  | [optional] 
**function_id** | **int** |  | 
**name** | **str** |  | 

## Example

```python
from spartera_api_sdk.models.job_functions import JobFunctions

# TODO update the JSON string below
json = "{}"
# create an instance of JobFunctions from a JSON string
job_functions_instance = JobFunctions.from_json(json)
# print the JSON string representation of the object
print(JobFunctions.to_json())

# convert the object into a dict
job_functions_dict = job_functions_instance.to_dict()
# create an instance of JobFunctions from a dict
job_functions_from_dict = JobFunctions.from_dict(job_functions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


