# StorageEngines

Fact table of all the different storage engines we support

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_created** | **datetime** | Optional. | [optional] 
**last_updated** | **datetime** | Optional. | [optional] 
**engine_id** | **int** | Unique identifier. | [optional] 
**provider_id** | **int** | References cloud_providers.provider_id — Supported cloud platforms and database engines available for connections. See GET /cloud_providers for valid values. Required. | 
**service_name** | **str** | Required. | 
**engine_type** | **str** | Required. One of: EDW, LLM, RDBMS, OBJ, API_MODEL, … (6 total). | 
**integration_complete** | **bool** | Optional. | [optional] 
**test_func_complete** | **bool** | Optional. | [optional] 

## Example

```python
from spartera_api_sdk.models.storage_engines import StorageEngines

# TODO update the JSON string below
json = "{}"
# create an instance of StorageEngines from a JSON string
storage_engines_instance = StorageEngines.from_json(json)
# print the JSON string representation of the object
print(StorageEngines.to_json())

# convert the object into a dict
storage_engines_dict = storage_engines_instance.to_dict()
# create an instance of StorageEngines from a dict
storage_engines_from_dict = StorageEngines.from_dict(storage_engines_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


