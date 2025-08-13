# JobFunctionsUpdate

Update schema for modifying JobFunction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 

## Example

```python
from spartera_api_sdk.models.job_functions_update import JobFunctionsUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of JobFunctionsUpdate from a JSON string
job_functions_update_instance = JobFunctionsUpdate.from_json(json)
# print the JSON string representation of the object
print(JobFunctionsUpdate.to_json())

# convert the object into a dict
job_functions_update_dict = job_functions_update_instance.to_dict()
# create an instance of JobFunctionsUpdate from a dict
job_functions_update_from_dict = JobFunctionsUpdate.from_dict(job_functions_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


