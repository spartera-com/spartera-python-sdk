# MeGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | Firebase user ID | 
**email** | **str** | User email address | [optional] 
**auth_method** | **str** | Authentication method used | 
**platform** | **str** | Platform origin | [optional] 
**origin_domain** | **str** | Request origin domain | [optional] 
**profile** | [**MeGet200ResponseProfile**](MeGet200ResponseProfile.md) |  | 
**company_id** | **str** | Company ID from authentication claims | 
**role_id** | **int** | Role ID from authentication claims | 
**token_metadata** | [**MeGet200ResponseTokenMetadata**](MeGet200ResponseTokenMetadata.md) |  | [optional] 
**api_key_info** | [**MeGet200ResponseApiKeyInfo**](MeGet200ResponseApiKeyInfo.md) |  | [optional] 

## Example

```python
from spartera_api_sdk.models.me_get200_response import MeGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of MeGet200Response from a JSON string
me_get200_response_instance = MeGet200Response.from_json(json)
# print the JSON string representation of the object
print(MeGet200Response.to_json())

# convert the object into a dict
me_get200_response_dict = me_get200_response_instance.to_dict()
# create an instance of MeGet200Response from a dict
me_get200_response_from_dict = MeGet200Response.from_dict(me_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


