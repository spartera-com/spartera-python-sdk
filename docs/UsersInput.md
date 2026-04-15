# UsersInput

Input schema for creating User

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_id** | **str** | References companies.company_id — A Spartera seller or buyer company account. See GET /companies for valid values. Required. | 
**role_id** | **int** | User&#39;s role for RBAC - single source of truth | [optional] 
**function_id** | **int** | User&#39;s job function/title | [optional] 
**status** | **str** | Required. One of: ACTIVE, PENDING, INACTIVE, BANNED. | [optional] 
**email_address** | **str** | Optional. Must be unique. | [optional] 
**timezone** | **str** | Optional. | [optional] 
**marketing_opt_out** | **bool** | Whether user has opted out of marketing communications. Default false &#x3D; opted in per ToS. | [optional] 

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


