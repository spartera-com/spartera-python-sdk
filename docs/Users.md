# Users

An individual user account within a company

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_created** | **datetime** | Optional. | [optional] 
**last_updated** | **datetime** | Optional. | [optional] 
**user_id** | **str** | Unique identifier. | [optional] 
**company_id** | **str** | References companies.company_id — A Spartera seller or buyer company account. See GET /companies for valid values. Required. | 
**role_id** | **int** | User&#39;s role for RBAC - single source of truth | 
**function_id** | **int** | User&#39;s job function/title | [optional] 
**status** | **str** | Required. One of: ACTIVE, PENDING, INACTIVE, BANNED. | 
**email_address** | **str** | Optional. Must be unique. | [optional] 
**timezone** | **str** | Optional. | [optional] 
**marketing_opt_out** | **bool** | Whether user has opted out of marketing communications. Default false &#x3D; opted in per ToS. | 

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


