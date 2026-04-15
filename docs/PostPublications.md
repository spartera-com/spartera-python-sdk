# PostPublications

Tracks where posts have been published to external platforms

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_created** | **datetime** | Optional. | [optional] 
**last_updated** | **datetime** | Optional. | [optional] 
**publication_id** | **str** | Unique identifier. | [optional] 
**post_id** | **str** | Post that was published | 
**company_id** | **str** | Company this publication belongs to | 
**integration_id** | **str** | Integration used for publishing | [optional] 
**platform** | **str** | Platform identifier (beehiiv, wordpress, etc) | 
**external_post_id** | **str** | ID of the post on the external platform | [optional] 
**external_post_url** | **str** | URL to view the post on the external platform | [optional] 
**published_at** | **datetime** | When the post was published to this platform | [optional] 
**status** | **str** | Status: published, failed, deleted | 
**error_message** | **str** | Error message if publication failed | [optional] 

## Example

```python
from spartera_api_sdk.models.post_publications import PostPublications

# TODO update the JSON string below
json = "{}"
# create an instance of PostPublications from a JSON string
post_publications_instance = PostPublications.from_json(json)
# print the JSON string representation of the object
print(PostPublications.to_json())

# convert the object into a dict
post_publications_dict = post_publications_instance.to_dict()
# create an instance of PostPublications from a dict
post_publications_from_dict = PostPublications.from_dict(post_publications_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


