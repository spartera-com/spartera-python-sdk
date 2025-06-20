# MeGet200ResponseProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | User ID (primary key) | [optional] 
**type** | **str** | Profile type | [optional] 
**company_id** | **str** | Company ID | [optional] 
**function_id** | **int** | User function/role ID | [optional] 
**status** | **str** | User status | [optional] 
**email_address** | **str** | User email address | [optional] 
**timezone** | **str** | User timezone | [optional] 
**date_created** | **datetime** | Account creation date | [optional] 
**last_updated** | **datetime** | Last profile update | [optional] 
**active** | **bool** | Account active status | [optional] 

## Example

```python
from spartera_api_sdk.models.me_get200_response_profile import MeGet200ResponseProfile

# TODO update the JSON string below
json = "{}"
# create an instance of MeGet200ResponseProfile from a JSON string
me_get200_response_profile_instance = MeGet200ResponseProfile.from_json(json)
# print the JSON string representation of the object
print(MeGet200ResponseProfile.to_json())

# convert the object into a dict
me_get200_response_profile_dict = me_get200_response_profile_instance.to_dict()
# create an instance of MeGet200ResponseProfile from a dict
me_get200_response_profile_from_dict = MeGet200ResponseProfile.from_dict(me_get200_response_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


