# Users

Individual users within a company with SOC2 authentication tracking

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_created** | **datetime** |  | [optional] 
**last_updated** | **datetime** |  | [optional] 
**user_id** | **str** |  | [optional] 
**company_id** | **str** |  | 
**function_id** | **int** |  | [optional] 
**status** | **str** | Enum type: StatusCodes | 
**email_address** | **str** |  | [optional] 
**timezone** | **str** |  | [optional] 

## Example

```python
from spartera_api_sdk.models.users import Users

# TODO update the JSON string below
json = "{}"
# create an instance of Users from a JSON string
users_instance = Users.from_json(json)
# print the JSON string representation of the object
print(Users.to_json())

# convert the object into a dict
users_dict = users_instance.to_dict()
# create an instance of Users from a dict
users_from_dict = Users.from_dict(users_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


