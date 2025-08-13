# UsersInput

Input schema for creating User

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_id** | **str** |  | 
**function_id** | **int** |  | [optional] 
**status** | **str** | Enum type: StatusCodes | [optional] 
**email_address** | **str** |  | [optional] 
**timezone** | **str** |  | [optional] 

## Example

```python
from spartera_api_sdk.models.users_input import UsersInput

# TODO update the JSON string below
json = "{}"
# create an instance of UsersInput from a JSON string
users_input_instance = UsersInput.from_json(json)
# print the JSON string representation of the object
print(UsersInput.to_json())

# convert the object into a dict
users_input_dict = users_input_instance.to_dict()
# create an instance of UsersInput from a dict
users_input_from_dict = UsersInput.from_dict(users_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


