# EndpointsUpdate

Update schema for modifying Endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_created** | **datetime** | Required. | [optional] 
**last_updated** | **datetime** | Required. | [optional] 
**user_id** | **str** | User who created this endpoint | [optional] 
**company_id** | **str** | References companies.company_id — A Spartera seller or buyer company account. See GET /companies for valid values. Required. | [optional] 
**connection_id** | **str** | Connection to the data source | [optional] 
**industry_id** | **int** | Industry / category for marketplace discovery | [optional] 
**auc_id** | **int** | Primary use case for marketplace discovery | [optional] 
**approval_status** | **str** | Approval status before marketplace publication | [optional] 
**approved_by_user_id** | **str** | User who approved this endpoint for marketplace | [optional] 
**approved_at** | **datetime** | Timestamp of marketplace approval | [optional] 
**sell_in_marketplace** | **bool** | Whether this endpoint appears in the public marketplace | [optional] 
**name** | **str** | Human-readable name for the endpoint | [optional] 
**slug** | **str** | Human-readable, URL-safe slug derived from name at creation time. e.g. &#39;NFL Live Moneyline &amp; Spread Odds&#39; → &#39;nfl-live-moneyline-spread-odds&#39;. Never changes after creation. Unique within company (DB constraint). Creation fails with 409 if a duplicate name exists in the same company. | [optional] 
**description** | **str** | Description of what this endpoint provides | [optional] 
**detailed_description** | **str** | Long-form HTML description for product pages and SEO | [optional] 
**top_questions** | **str** | Top 3 questions this endpoint can help answer, in English. Stored as JSON array of strings (1-3 items, 15-200 chars each). Strongly encouraged for marketplace endpoints but not required — nudge via UI completeness score, not hard validation. | [optional] 
**source_schema_name** | **str** | Schema/database name where the table resides | [optional] 
**source_table_name** | **str** | Table name to query from | [optional] 
**customer_name** | **str** | Named customer for B2B deals (pricing handled via asset_price_history) | [optional] 
**endpoint_schema** | **object** | Column configurations including aggregations, filters, and visibility. Format: {columns: [{name, type, aggregation, filter, is_hidden, alias, ...}]}. This is the source of truth — SQL is generated at runtime from this configuration. | [optional] 
**rate_limit_number** | **int** | Number of requests allowed per rate_limit_period | [optional] 
**rate_limit_period** | **str** | Time period for rate limiting (HOUR, DAY, MONTH) | [optional] 
**rate_limit_granularity** | **str** | How to group rate limits (IP, USER, COMPANY, API_KEY, GLOBAL) | [optional] 
**access_method** | **str** | Access control method (OPEN, API_KEY, IP, EMAIL, DOMAIN) | [optional] 
**access_whitelist** | **object** | List of allowed IPs, emails, or domains based on access_method. Format: {type: &#39;ip&#39;|&#39;email&#39;|&#39;domain&#39;, values: [&#39;192.168.1.1&#39;, ...]} | [optional] 
**status** | **str** | Current status of the endpoint (ACTIVE, INACTIVE, DEPRECATED) | [optional] 
**data_time_period_start** | **datetime** | Start date of the data time period covered | [optional] 
**data_time_period_end** | **datetime** | End date of the data time period covered | [optional] 
**date_collection_start** | **datetime** | When the seller began actively collecting this data. Distinct from data_time_period_start, which describes when the records themselves begin. Backfilled historical data will have date_collection_start &gt; data_time_period_start. | [optional] 
**geographic_coverage_type** | **str** | Type of geographic coverage | [optional] 
**geographic_coverage_details** | **str** | Specific regions/countries covered (e.g., &#39;United States, Canada, Mexico&#39;) | [optional] 
**data_source_refresh_frequency** | **str** | How often the source data is refreshed | [optional] 
**tags** | **str** | Comma-separated tags for organizing endpoints | [optional] 
**last_accessed** | **datetime** | When this endpoint was last called | [optional] 
**max_records_per_request** | **int** | Seller-enforced row cap per request. Buyers cannot exceed this. Default 1000. | [optional] 
**export_enabled** | **bool** | Whether this endpoint supports bulk export to GCS. When True, buyers can request delivery&#x3D;gcs with format&#x3D;csv|parquet. Independent of max_records_per_request, which only governs inline JSON. | [optional] 
**max_records_per_export** | **int** | Hard ceiling on rows returned per GCS export. Separate from max_records_per_request so sellers can offer larger downloads via file delivery without expanding inline JSON responses. | [optional] 
**sample_response** | **object** | Last successful {spartera, request, response} envelope. Saved on each successful marketplace run. Displayed as preview on product page load. | [optional] 
**active** | **bool** | Required. | [optional] 

## Example

```python
from spartera_api_sdk.models.endpoints_update import EndpointsUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointsUpdate from a JSON string
endpoints_update_instance = EndpointsUpdate.from_json(json)
# print the JSON string representation of the object
print(EndpointsUpdate.to_json())

# convert the object into a dict
endpoints_update_dict = endpoints_update_instance.to_dict()
# create an instance of EndpointsUpdate from a dict
endpoints_update_from_dict = EndpointsUpdate.from_dict(endpoints_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


