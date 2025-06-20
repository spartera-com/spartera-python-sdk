# MeGet200ResponseTokenMetadata

JWT token metadata (null for API keys)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issuer** | **str** | Token issuer | [optional] 
**auth_time** | **int** | Authentication time | [optional] 
**issued_at** | **int** | Token issued timestamp | [optional] 
**expires_at** | **int** | Token expiration timestamp | [optional] 

## Example

```python
from spartera_api_sdk.models.me_get200_response_token_metadata import MeGet200ResponseTokenMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of MeGet200ResponseTokenMetadata from a JSON string
me_get200_response_token_metadata_instance = MeGet200ResponseTokenMetadata.from_json(json)
# print the JSON string representation of the object
print(MeGet200ResponseTokenMetadata.to_json())

# convert the object into a dict
me_get200_response_token_metadata_dict = me_get200_response_token_metadata_instance.to_dict()
# create an instance of MeGet200ResponseTokenMetadata from a dict
me_get200_response_token_metadata_from_dict = MeGet200ResponseTokenMetadata.from_dict(me_get200_response_token_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


