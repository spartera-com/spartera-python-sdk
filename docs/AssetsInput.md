# AssetsInput

Input schema for creating Asset

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | [optional] 
**company_id** | **str** |  | 
**connection_id** | **str** |  | [optional] 
**industry_id** | **int** |  | [optional] 
**approval_status** | **str** | Approval status for AI-generated assets | [optional] 
**approved_by_user_id** | **str** | User who approved this asset for marketplace | [optional] 
**approved_at** | **datetime** | When this asset was approved for marketplace | [optional] 
**name** | **str** |  | 
**slug** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**source** | **str** | Enum type: Source | 
**asset_type** | **str** | Enum type: AssetType | [optional] 
**asset_schema** | **object** | Stores database table schema data including columns, types, and metadata | [optional] 
**tags** | **str** |  | [optional] 
**sql_logic** | **str** |  | [optional] 
**source_schema_name** | **str** |  | [optional] 
**source_table_name** | **str** |  | [optional] 
**sell_in_marketplace** | **bool** |  | [optional] 
**viz_chart_library** | **str** | Enum type: PlottingLibrary | [optional] 
**viz_chart_type** | **str** | Enum type: ChartType | [optional] 
**viz_dep_var_col_name** | **str** |  | [optional] 
**viz_indep_var_col_name** | **str** |  | [optional] 
**viz_size_col_name** | **str** |  | [optional] 
**viz_color_col_name** | **str** |  | [optional] 
**viz_data_aggregation** | **str** | Enum type: AggregationType | [optional] 
**viz_sort_direction** | **str** | Enum type: SortDirection | [optional] 
**viz_data_limit** | **int** |  | [optional] 
**viz_color_scheme** | **str** | Enum type: ColorScheme | [optional] 
**allow_params** | **bool** |  | [optional] 
**accept_terms** | **bool** |  | [optional] 
**cached** | **bool** |  | [optional] 
**schedule** | **str** |  | [optional] 
**next_run** | **datetime** |  | [optional] 
**data_time_period_start** | **datetime** | Start date of the data time period covered | [optional] 
**data_time_period_end** | **datetime** | End date of the data time period covered | [optional] 
**geographic_coverage_type** | **str** | Type of geographic coverage (Enum type: GeographicCoverage) | [optional] 
**geographic_coverage_details** | **str** | Specific regions/countries covered (e.g., &#39;United States, Canada, Mexico&#39;) | [optional] 
**data_source_refresh_frequency** | **str** | How often the source data is refreshed (Enum type: DataRefreshFrequency) | [optional] 
**data_source_last_refreshed** | **datetime** | When the source data was last refreshed | [optional] 

## Example

```python
from spartera_api_sdk.models.assets_input import AssetsInput

# TODO update the JSON string below
json = "{}"
# create an instance of AssetsInput from a JSON string
assets_input_instance = AssetsInput.from_json(json)
# print the JSON string representation of the object
print(AssetsInput.to_json())

# convert the object into a dict
assets_input_dict = assets_input_instance.to_dict()
# create an instance of AssetsInput from a dict
assets_input_from_dict = AssetsInput.from_dict(assets_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


