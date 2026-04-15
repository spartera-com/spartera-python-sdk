# UsersUpdate

Update schema for modifying User

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_id** | **str** | References companies.company_id — A Spartera seller or buyer company account. See GET /companies for valid values. Required. | [optional] 
**role_id** | **int** | User&#39;s role for RBAC - single source of truth | [optional] 
**function_id** | **int** | User&#39;s job function/title | [optional] 
**status** | **str** | Required. One of: ACTIVE, PENDING, INACTIVE, BANNED. | [optional] 
**email_address** | **str** | Optional. Must be unique. | [optional] 
**timezone** | **str** | Optional. | [optional] 
**marketing_opt_out** | **bool** | Whether user has opted out of marketing communications. Default false &#x3D; opted in per ToS. | [optional] 

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


