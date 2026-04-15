# Endpoints

A configured API endpoint exposing seller data with access controls and rate limiting

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_created** | **datetime** | Required. | 
**last_updated** | **datetime** | Required. | 
**endpoint_id** | **str** | Unique identifier. | [optional] 
**user_id** | **str** | User who created this endpoint | [optional] 
**company_id** | **str** | References companies.company_id — A Spartera seller or buyer company account. See GET /companies for valid values. Required. | 
**connection_id** | **str** | Connection to the data source | 
**industry_id** | **int** | Industry / category for marketplace discovery | [optional] 
**auc_id** | **int** | Primary use case for marketplace discovery | [optional] 
**approval_status** | **str** | Approval status before marketplace publication | [optional] 
**approved_by_user_id** | **str** | User who approved this endpoint for marketplace | [optional] 
**approved_at** | **datetime** | Timestamp of marketplace approval | [optional] 
**sell_in_marketplace** | **bool** | Whether this endpoint appears in the public marketplace | 
**price_credits** | **int** | Credits deducted from the buyer&#39;s pool per successful (200 OK) request. Same credit pool as assets. price_usd kept for billing records / dashboards. | 
**name** | **str** | Human-readable name for the endpoint | 
**slug** | **str** | Human-readable, URL-safe slug derived from name at creation time. e.g. &#39;NFL Live Moneyline &amp; Spread Odds&#39; → &#39;nfl-live-moneyline-spread-odds&#39;. Never changes after creation. Unique within company (DB constraint). Creation fails with 409 if a duplicate name exists in the same company. | [optional] 
**description** | **str** | Description of what this endpoint provides | [optional] 
**source_schema_name** | **str** | Schema/database name where the table resides | [optional] 
**source_table_name** | **str** | Table name to query from | [optional] 
**customer_name** | **str** | Named customer for B2B deals (marketplace uses price_credits instead) | [optional] 
**price_usd** | **float** | USD reference price for billing records and seller dashboards | [optional] 
**endpoint_schema** | **object** | Column configurations including aggregations, filters, and visibility. Format: {columns: [{name, type, aggregation, filter, is_hidden, alias, ...}]}. This is the source of truth — SQL is generated at runtime from this configuration. | [optional] 
**rate_limit_requests** | **int** | Number of requests allowed per rate_limit_period | [optional] 
**rate_limit_period** | **str** | Time period for rate limiting (HOUR, DAY, MONTH) | [optional] 
**rate_limit_granularity** | **str** | How to group rate limits (IP, USER, COMPANY, API_KEY, GLOBAL) | [optional] 
**access_method** | **str** | Access control method (OPEN, API_KEY, IP, EMAIL, DOMAIN) | [optional] 
**access_whitelist** | **object** | List of allowed IPs, emails, or domains based on access_method. Format: {type: &#39;ip&#39;|&#39;email&#39;|&#39;domain&#39;, values: [&#39;192.168.1.1&#39;, ...]} | [optional] 
**status** | **str** | Current status of the endpoint (ACTIVE, INACTIVE, DEPRECATED) | 
**tags** | **str** | Comma-separated tags for organizing endpoints | [optional] 
**last_accessed** | **datetime** | When this endpoint was last called | [optional] 
**max_records_per_request** | **int** | Seller-enforced row cap per request. Buyers cannot exceed this. Default 1000. | [optional] 
**sample_response** | **object** | Last successful {spartera, request, response} envelope. Saved on each successful marketplace run. Displayed as preview on product page load. | [optional] 
**active** | **bool** | Required. | 

## Example

```python
from spartera_api_sdk.models.endpoints import Endpoints

# TODO update the JSON string below
json = "{}"
# create an instance of Endpoints from a JSON string
endpoints_instance = Endpoints.from_json(json)
# print the JSON string representation of the object
print(Endpoints.to_json())

# convert the object into a dict
endpoints_dict = endpoints_instance.to_dict()
# create an instance of Endpoints from a dict
endpoints_from_dict = Endpoints.from_dict(endpoints_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


