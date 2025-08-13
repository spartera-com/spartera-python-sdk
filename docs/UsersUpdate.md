# UsersUpdate

Update schema for modifying User

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_id** | **str** |  | [optional] 
**function_id** | **int** |  | [optional] 
**status** | **str** | Enum type: StatusCodes | [optional] 
**email_address** | **str** |  | [optional] 
**timezone** | **str** |  | [optional] 

## Example

```python
from spartera_api_sdk.models.users_update import UsersUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of UsersUpdate from a JSON string
users_update_instance = UsersUpdate.from_json(json)
# print the JSON string representation of the object
print(UsersUpdate.to_json())

# convert the object into a dict
users_update_dict = users_update_instance.to_dict()
# create an instance of UsersUpdate from a dict
users_update_from_dict = UsersUpdate.from_dict(users_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


