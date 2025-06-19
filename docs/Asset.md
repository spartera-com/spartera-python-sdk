# Asset

Asset model for every asset (insight/visualization/feed/etc.) customer creates

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**company_id** | **str** |  | 
**connection_id** | **str** |  | [optional] 
**llm_connection_id** | **str** |  | [optional] 
**snippet_id** | **str** |  | [optional] 
**industry_id** | **str** |  | [optional] 
**ai_job_id** | **str** |  | [optional] 
**approval_status** | **str** |  | [optional] 
**approved_by_user_id** | **str** |  | [optional] 
**approved_at** | **str** |  | [optional] 
**name** | **str** |  | 
**slug** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**source** | **str** |  | 
**asset_type** | **str** |  | [optional] 
**asset_schema** | **str** |  | [optional] 
**visibility** | **str** |  | [optional] 
**tags** | **str** |  | [optional] 
**sql_logic** | **str** |  | [optional] 
**source_schema_name** | **str** |  | [optional] 
**source_table_name** | **str** |  | [optional] 
**sell_in_marketplace** | **str** |  | [optional] 
**viz_chart_library** | **str** |  | [optional] 
**viz_chart_type** | **str** |  | [optional] 
**viz_dep_var_col_name** | **str** |  | [optional] 
**viz_indep_var_col_name** | **str** |  | [optional] 
**viz_size_col_name** | **str** |  | [optional] 
**viz_color_col_name** | **str** |  | [optional] 
**viz_data_aggregation** | **str** |  | [optional] 
**viz_sort_direction** | **str** |  | [optional] 
**viz_data_limit** | **str** |  | [optional] 
**viz_color_scheme** | **str** |  | [optional] 
**allow_params** | **str** |  | [optional] 
**accept_terms** | **str** |  | [optional] 
**cached** | **str** |  | [optional] 
**schedule** | **str** |  | [optional] 
**next_run** | **str** |  | [optional] 
**data_time_period_start** | **str** |  | [optional] 
**data_time_period_end** | **str** |  | [optional] 
**geographic_coverage_type** | **str** |  | [optional] 
**geographic_coverage_details** | **str** |  | [optional] 
**data_source_refresh_frequency** | **str** |  | [optional] 
**data_source_last_refreshed** | **str** |  | [optional] 
**date_created** | **str** |  | [optional] 
**last_updated** | **str** |  | [optional] 
**active** | **str** |  | [optional] 

## Example

```python
from spartera_api_sdk.models.asset import Asset

# TODO update the JSON string below
json = "{}"
# create an instance of Asset from a JSON string
asset_instance = Asset.from_json(json)
# print the JSON string representation of the object
print(Asset.to_json())

# convert the object into a dict
asset_dict = asset_instance.to_dict()
# create an instance of Asset from a dict
asset_from_dict = Asset.from_dict(asset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


