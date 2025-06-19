# User

Individual users within a company

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | [optional] 
**company_id** | **str** |  | 
**function_id** | **str** |  | [optional] 
**status** | **str** |  | 
**email_address** | **str** |  | [optional] 
**timezone** | **str** |  | [optional] 
**date_created** | **str** |  | [optional] 
**last_updated** | **str** |  | [optional] 
**active** | **str** |  | [optional] 

## Example

```python
from spartera_api_sdk.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print(User.to_json())

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_from_dict = User.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


