# PostPublicationsUpdate

Update schema for modifying PostPublication

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**post_id** | **str** | Post that was published | [optional] 
**company_id** | **str** | Company this publication belongs to | [optional] 
**integration_id** | **str** | Integration used for publishing | [optional] 
**platform** | **str** | Platform identifier (beehiiv, wordpress, etc) | [optional] 
**external_post_id** | **str** | ID of the post on the external platform | [optional] 
**external_post_url** | **str** | URL to view the post on the external platform | [optional] 
**published_at** | **datetime** | When the post was published to this platform | [optional] 
**status** | **str** | Status: published, failed, deleted | [optional] 
**error_message** | **str** | Error message if publication failed | [optional] 

## Example

```python
from spartera_api_sdk.models.post_publications_update import PostPublicationsUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of PostPublicationsUpdate from a JSON string
post_publications_update_instance = PostPublicationsUpdate.from_json(json)
# print the JSON string representation of the object
print(PostPublicationsUpdate.to_json())

# convert the object into a dict
post_publications_update_dict = post_publications_update_instance.to_dict()
# create an instance of PostPublicationsUpdate from a dict
post_publications_update_from_dict = PostPublicationsUpdate.from_dict(post_publications_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


