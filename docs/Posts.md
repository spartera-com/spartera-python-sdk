# Posts

An AI-generated article or post created by the Spartera Post Generator

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_created** | **datetime** | Optional. | [optional] 
**last_updated** | **datetime** | Optional. | [optional] 
**post_id** | **str** | Unique identifier. | [optional] 
**user_id** | **str** | User who created this post | 
**company_id** | **str** | Company this post belongs to | 
**title** | **str** | Article title | 
**category** | **str** | Article category (e.g., &#39;Sports&#39;, &#39;Business&#39;) | [optional] 
**teaser** | **str** | Article teaser/subtitle | [optional] 
**content_html** | **str** | Generated article HTML content | 
**insights_used** | **object** | Array of insights used: [{asset_id, asset_name, value, runtime, success}] | [optional] 
**generation_creativity** | **int** | Creativity level (0-100), maps to AI temperature | [optional] 
**generation_target_word_count** | **int** | Target word count (null &#x3D; auto) | [optional] 
**generation_tone** | **str** | Writing tone: professional, casual, technical, conversational | [optional] 
**generation_include_citations** | **bool** | Whether to include data source citations | [optional] 
**generation_subheading_count** | **int** | Number of subheadings (2-5) | [optional] 
**generation_temperature** | **float** | Actual temperature used for generation (0.0-2.0) | [optional] 
**data_cost_credits** | **int** | Cost in credits for data insights | 
**service_cost_credits** | **int** | Cost in credits for AI generation service | 
**total_cost_credits** | **int** | Total cost in credits (data + service) | 
**successful_insights_count** | **int** | Number of insights that succeeded | 
**failed_insights_count** | **int** | Number of insights that failed | 
**generation_time_ms** | **int** | Time taken to generate article in milliseconds | [optional] 
**is_published** | **bool** | Whether this post has been published | 
**published_at** | **datetime** | When this post was published | [optional] 
**view_count** | **int** | Number of times this post has been viewed | 
**last_edited_at** | **datetime** | When this post was last edited | [optional] 

## Example

```python
from spartera_api_sdk.models.posts import Posts

# TODO update the JSON string below
json = "{}"
# create an instance of Posts from a JSON string
posts_instance = Posts.from_json(json)
# print the JSON string representation of the object
print(Posts.to_json())

# convert the object into a dict
posts_dict = posts_instance.to_dict()
# create an instance of Posts from a dict
posts_from_dict = Posts.from_dict(posts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


