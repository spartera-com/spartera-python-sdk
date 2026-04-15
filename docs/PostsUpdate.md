# PostsUpdate

Update schema for modifying Post

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | User who created this post | [optional] 
**company_id** | **str** | Company this post belongs to | [optional] 
**title** | **str** | Article title | [optional] 
**category** | **str** | Article category (e.g., &#39;Sports&#39;, &#39;Business&#39;) | [optional] 
**teaser** | **str** | Article teaser/subtitle | [optional] 
**content_html** | **str** | Generated article HTML content | [optional] 
**insights_used** | **object** | Array of insights used: [{asset_id, asset_name, value, runtime, success}] | [optional] 
**generation_creativity** | **int** | Creativity level (0-100), maps to AI temperature | [optional] 
**generation_target_word_count** | **int** | Target word count (null &#x3D; auto) | [optional] 
**generation_tone** | **str** | Writing tone: professional, casual, technical, conversational | [optional] 
**generation_include_citations** | **bool** | Whether to include data source citations | [optional] 
**generation_subheading_count** | **int** | Number of subheadings (2-5) | [optional] 
**generation_temperature** | **float** | Actual temperature used for generation (0.0-2.0) | [optional] 
**data_cost_credits** | **int** | Cost in credits for data insights | [optional] 
**service_cost_credits** | **int** | Cost in credits for AI generation service | [optional] 
**total_cost_credits** | **int** | Total cost in credits (data + service) | [optional] 
**successful_insights_count** | **int** | Number of insights that succeeded | [optional] 
**failed_insights_count** | **int** | Number of insights that failed | [optional] 
**generation_time_ms** | **int** | Time taken to generate article in milliseconds | [optional] 
**is_published** | **bool** | Whether this post has been published | [optional] 
**published_at** | **datetime** | When this post was published | [optional] 
**view_count** | **int** | Number of times this post has been viewed | [optional] 
**last_edited_at** | **datetime** | When this post was last edited | [optional] 

## Example

```python
from spartera_api_sdk.models.posts_update import PostsUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of PostsUpdate from a JSON string
posts_update_instance = PostsUpdate.from_json(json)
# print the JSON string representation of the object
print(PostsUpdate.to_json())

# convert the object into a dict
posts_update_dict = posts_update_instance.to_dict()
# create an instance of PostsUpdate from a dict
posts_update_from_dict = PostsUpdate.from_dict(posts_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


